use std::process::{Command, Stdio};
use std::path::Path;
use std::time::Duration;
use regex::Regex;
use wait_timeout::ChildExt;

use crate::models::{TestResult, TestRunResult};

/// Test timeout in seconds
const TEST_TIMEOUT_SECS: u64 = 30;

/// Find Python executable on the system
fn find_python() -> Result<String, String> {
    // Try common Python locations on Windows
    let candidates = [
        // Windows Python launcher (most reliable on Windows)
        "py",
        // Standard Python command
        "python3",
        "python",
        // Common Windows installation paths
        r"C:\Users\Rackl\AppData\Local\Programs\Python\Python312\python.exe",
        r"C:\Users\Rackl\AppData\Local\Programs\Python\Python311\python.exe",
        r"C:\Users\Rackl\AppData\Local\Programs\Python\Python310\python.exe",
        r"C:\Python312\python.exe",
        r"C:\Python311\python.exe",
        r"C:\Python310\python.exe",
    ];

    for candidate in candidates {
        let result = Command::new(candidate)
            .args(["--version"])
            .output();

        if let Ok(output) = result {
            if output.status.success() {
                return Ok(candidate.to_string());
            }
        }
    }

    Err("Python not found. Please install Python and ensure it's in your PATH.".to_string())
}

/// Run pytest for a specific problem
#[tauri::command]
pub fn run_tests(problem_path: String) -> Result<TestRunResult, String> {
    let path = Path::new(&problem_path);
    let test_file = path.join("test_solution.py");

    if !test_file.exists() {
        return Err(format!("Test file not found: {:?}", test_file));
    }

    // Get the problems root directory (3 levels up from problem folder)
    let problems_root = path
        .parent() // difficulty
        .and_then(|p| p.parent()) // pattern
        .and_then(|p| p.parent()) // problems
        .and_then(|p| p.parent()) // root
        .ok_or("Cannot determine project root")?;

    // Find Python
    let python = find_python()?;

    // Clear pycache to ensure fresh imports
    let pycache_dir = path.join("__pycache__");
    if pycache_dir.exists() {
        let _ = std::fs::remove_dir_all(&pycache_dir);
    }

    // Run pytest with cache disabled and no compiled files
    let mut child = Command::new(&python)
        .args(["-B", "-m", "pytest", test_file.to_str().unwrap(), "-v", "--tb=short", "-p", "no:cacheprovider"])
        .current_dir(problems_root)
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|e| format!("Failed to execute pytest: {}", e))?;

    // Wait with timeout
    let timeout = Duration::from_secs(TEST_TIMEOUT_SECS);
    let status = match child.wait_timeout(timeout).map_err(|e| format!("Failed to wait for pytest: {}", e))? {
        Some(status) => status,
        None => {
            // Timeout - kill the process
            let _ = child.kill();
            let _ = child.wait(); // Clean up zombie process
            return Ok(TestRunResult {
                success: false,
                total: 0,
                passed: 0,
                failed: 0,
                results: vec![],
                raw_output: format!("Test execution timed out after {} seconds. Your solution may have an infinite loop.", TEST_TIMEOUT_SECS),
            });
        }
    };

    // Read output
    let stdout = child.stdout.take()
        .map(|mut s| {
            let mut buf = String::new();
            use std::io::Read;
            let _ = s.read_to_string(&mut buf);
            buf
        })
        .unwrap_or_default();
    
    let stderr = child.stderr.take()
        .map(|mut s| {
            let mut buf = String::new();
            use std::io::Read;
            let _ = s.read_to_string(&mut buf);
            buf
        })
        .unwrap_or_default();

    let raw_output = format!("{}\n{}", stdout, stderr);

    // Parse pytest output
    let results = parse_pytest_output(&stdout);
    let passed = results.iter().filter(|r| r.passed).count() as i32;
    let failed = results.iter().filter(|r| !r.passed).count() as i32;
    let total = results.len() as i32;

    Ok(TestRunResult {
        success: status.success(),
        total,
        passed,
        failed,
        results,
        raw_output,
    })
}

fn parse_pytest_output(output: &str) -> Vec<TestResult> {
    let mut results = Vec::new();

    // Match test result lines like:
    // test_solution.py::TestClassName::test_name PASSED [ 20%]
    // test_solution.py::TestClassName::test_name FAILED [ 40%]
    let test_re = Regex::new(r"test_solution\.py::(\w+)::(\w+)\s+(PASSED|FAILED)").ok();

    if let Some(re) = test_re {
        for caps in re.captures_iter(output) {
            let class_name = caps.get(1).map(|m| m.as_str()).unwrap_or("");
            let test_name = caps.get(2).map(|m| m.as_str()).unwrap_or("");
            let status = caps.get(3).map(|m| m.as_str()).unwrap_or("");

            let passed = status == "PASSED";
            let full_name = format!("{}::{}", class_name, test_name);

            // Try to extract error for failed tests
            let error = if !passed {
                extract_test_error(output, &full_name)
            } else {
                None
            };

            results.push(TestResult {
                passed,
                test_name: full_name,
                output: String::new(),
                error,
                duration: 0.0,
            });
        }
    }

    // If no results parsed, try simpler pattern
    if results.is_empty() {
        let simple_re = Regex::new(r"(test_\w+)\s+(PASSED|FAILED)").ok();
        if let Some(re) = simple_re {
            for caps in re.captures_iter(output) {
                let test_name = caps.get(1).map(|m| m.as_str().to_string()).unwrap_or_default();
                let status = caps.get(2).map(|m| m.as_str()).unwrap_or("");
                let passed = status == "PASSED";

                results.push(TestResult {
                    passed,
                    test_name,
                    output: String::new(),
                    error: None,
                    duration: 0.0,
                });
            }
        }
    }

    results
}

fn extract_test_error(output: &str, test_name: &str) -> Option<String> {
    // Look for the error section for this test
    let pattern = format!(r"(?s){}.*?FAILED.*?\n(.*?)(?:\n\n|\z)", regex::escape(test_name));
    let re = Regex::new(&pattern).ok()?;

    re.captures(output)
        .and_then(|caps| caps.get(1))
        .map(|m| m.as_str().trim().to_string())
}
