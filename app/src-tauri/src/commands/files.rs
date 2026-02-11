use std::fs;
use std::path::PathBuf;

/// Read solution.py file content
#[tauri::command]
pub fn read_solution(path: String) -> Result<String, String> {
    // Normalize the path for the current OS
    let normalized_path: PathBuf = path.replace("/", "\\").into();
    fs::read_to_string(&normalized_path).map_err(|e| format!("Failed to read file: {}", e))
}
