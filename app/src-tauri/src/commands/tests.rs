use std::process::Command;
use std::path::Path;
use regex::Regex;

use crate::models::{TestResult, TestRunResult};

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

    // Run pytest
    let output = Command::new("python")
        .args(["-m", "pytest", test_file.to_str().unwrap(), "-v", "--tb=short"])
        .current_dir(problems_root)
        .output()
        .map_err(|e| format!("Failed to execute pytest: {}", e))?;

    let stdout = String::from_utf8_lossy(&output.stdout).to_string();
    let stderr = String::from_utf8_lossy(&output.stderr).to_string();
    let raw_output = format!("{}\n{}", stdout, stderr);

    // Parse pytest output
    let results = parse_pytest_output(&stdout);
    let passed = results.iter().filter(|r| r.passed).count() as i32;
    let failed = results.iter().filter(|r| !r.passed).count() as i32;
    let total = results.len() as i32;

    Ok(TestRunResult {
        success: output.status.success(),
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
