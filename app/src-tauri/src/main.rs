// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod commands;
mod models;

use commands::{
    get_problems_dir,
    get_problem_tree,
    get_problem_content,
    read_solution,
    run_tests,
};

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            get_problems_dir,
            get_problem_tree,
            get_problem_content,
            read_solution,
            run_tests,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
