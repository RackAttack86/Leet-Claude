use std::fs;
use std::path::PathBuf;

/// Read solution.py file content
#[tauri::command]
pub fn read_solution(path: String) -> Result<String, String> {
    // Normalize the path for the current OS
    let normalized_path: PathBuf = path.replace("/", "\\").into();
    fs::read_to_string(&normalized_path).map_err(|e| format!("Failed to read file: {}", e))
}

/// Write solution.py file content (auto-save)
#[tauri::command]
pub fn write_solution(path: String, content: String) -> Result<(), String> {
    // Normalize the path for the current OS
    let normalized_path: PathBuf = path.replace("/", "\\").into();

    // Ensure parent directory exists
    if let Some(parent) = normalized_path.parent() {
        if !parent.exists() {
            return Err(format!("Parent directory does not exist: {:?}", parent));
        }
    }

    fs::write(&normalized_path, content).map_err(|e| format!("Failed to write file: {}", e))
}
