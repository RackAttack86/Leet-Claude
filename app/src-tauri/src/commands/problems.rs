use std::collections::HashMap;
use std::fs;
use std::path::Path;
use walkdir::WalkDir;
use regex::Regex;

use crate::models::{Problem, ProblemContent, TreeNode};
use super::parser::{parse_metadata, extract_docstring, extract_hints, extract_explanation, strip_code_for_editor};

/// Get the problems directory path
#[tauri::command]
pub fn get_problems_dir() -> Result<String, String> {
    let exe_path = std::env::current_exe().map_err(|e| e.to_string())?;
    let base_dir = exe_path.parent().ok_or("Cannot get parent directory")?;

    let possible_paths = vec![
        base_dir.join("..").join("..").join("..").join("problems"),
        base_dir.join("problems"),
        Path::new("D:\\Leet-Claude\\problems").to_path_buf(),
    ];

    for path in possible_paths {
        if path.exists() {
            return path.canonicalize()
                .map(|p| p.to_string_lossy().to_string())
                .map_err(|e| e.to_string());
        }
    }

    Ok("D:\\Leet-Claude\\problems".to_string())
}

/// Scan the problems directory and build the tree structure
#[tauri::command]
pub fn get_problem_tree(problems_dir: String) -> Result<Vec<TreeNode>, String> {
    let problems_path = Path::new(&problems_dir);

    if !problems_path.exists() {
        return Err(format!("Problems directory not found: {}", problems_dir));
    }

    let mut patterns: HashMap<String, HashMap<String, Vec<Problem>>> = HashMap::new();

    for entry in WalkDir::new(problems_path)
        .min_depth(3)
        .max_depth(3)
        .into_iter()
        .filter_map(|e| e.ok())
    {
        let path = entry.path();
        if !path.is_dir() {
            continue;
        }

        let solution_path = path.join("solution.py");
        if !solution_path.exists() {
            continue;
        }

        let components: Vec<&str> = path
            .strip_prefix(problems_path)
            .ok()
            .map(|p| p.components().map(|c| c.as_os_str().to_str().unwrap_or("")).collect())
            .unwrap_or_default();

        if components.len() < 3 {
            continue;
        }

        let pattern = components[0].to_string();
        let difficulty = components[1].to_string();
        let folder_name = components[2];

        let folder_re = Regex::new(r"p(\d+)_(.+)").ok();
        let (number, slug) = if let Some(re) = folder_re {
            if let Some(caps) = re.captures(folder_name) {
                let num: i32 = caps.get(1).and_then(|m| m.as_str().parse().ok()).unwrap_or(0);
                let s = caps.get(2).map(|m| m.as_str().to_string()).unwrap_or_default();
                (num, s)
            } else {
                continue;
            }
        } else {
            continue;
        };

        let solution_content = fs::read_to_string(&solution_path).unwrap_or_default();
        let metadata = parse_metadata(&solution_content);

        let problem = if let Some(meta) = metadata {
            Problem {
                number: meta.number,
                name: meta.name,
                slug,
                difficulty: meta.difficulty,
                pattern: meta.pattern,
                topics: meta.topics,
                url: meta.url,
                companies: meta.companies,
                time_complexity: meta.time_complexity,
                space_complexity: meta.space_complexity,
                path: path.to_string_lossy().to_string(),
            }
        } else {
            Problem {
                number,
                name: slug.replace("-", " "),
                slug,
                difficulty: difficulty.clone(),
                pattern: pattern.clone(),
                topics: vec![],
                url: String::new(),
                companies: vec![],
                time_complexity: String::new(),
                space_complexity: String::new(),
                path: path.to_string_lossy().to_string(),
            }
        };

        patterns
            .entry(pattern.clone())
            .or_default()
            .entry(difficulty.clone())
            .or_default()
            .push(problem);
    }

    let mut tree: Vec<TreeNode> = Vec::new();

    let mut pattern_names: Vec<_> = patterns.keys().cloned().collect();
    pattern_names.sort();

    for pattern_name in pattern_names {
        let difficulties = patterns.get(&pattern_name).unwrap();

        let mut difficulty_nodes: Vec<TreeNode> = Vec::new();

        let difficulty_order = ["easy", "medium", "hard"];
        for diff in difficulty_order.iter() {
            if let Some(problems) = difficulties.get(*diff) {
                let mut sorted_problems = problems.clone();
                sorted_problems.sort_by_key(|p| p.number);

                let problem_nodes: Vec<TreeNode> = sorted_problems
                    .iter()
                    .map(|p| TreeNode {
                        id: format!("problem-{}", p.number),
                        label: format!("{}. {}", p.number, p.name),
                        node_type: "problem".to_string(),
                        children: None,
                        data: Some(p.clone()),
                        expanded: None,
                    })
                    .collect();

                difficulty_nodes.push(TreeNode {
                    id: format!("{}-{}", pattern_name, diff),
                    label: capitalize(diff),
                    node_type: "difficulty".to_string(),
                    children: Some(problem_nodes),
                    data: None,
                    expanded: Some(false),
                });
            }
        }

        tree.push(TreeNode {
            id: pattern_name.clone(),
            label: format_pattern_name(&pattern_name),
            node_type: "pattern".to_string(),
            children: Some(difficulty_nodes),
            data: None,
            expanded: Some(false),
        });
    }

    Ok(tree)
}

/// Get full content for a selected problem
#[tauri::command]
pub fn get_problem_content(problem_path: String) -> Result<ProblemContent, String> {
    let path = Path::new(&problem_path);

    let solution_path = path.join("solution.py");
    let solution_content = fs::read_to_string(&solution_path)
        .map_err(|e| format!("Failed to read solution.py: {}", e))?;

    // Full solution (stripped) for the Full Solution panel
    let full_solution = strip_code_for_editor(&solution_content);

    // For editor starter code, use template.py or fallback to stripped solution
    let template_path = path.join("template.py");

    let starter_code = if template_path.exists() {
        fs::read_to_string(&template_path)
            .unwrap_or_else(|_| full_solution.clone())
    } else {
        full_solution.clone()
    };

    let readme_path = path.join("README.md");
    let readme_content = fs::read_to_string(&readme_path).unwrap_or_default();

    let definition = extract_docstring(&solution_content);
    let hints = extract_hints(&readme_content);
    let explanation = extract_explanation(&readme_content);

    Ok(ProblemContent {
        definition,
        hints,
        solution: full_solution,
        starter_code,
        explanation,
        readme: readme_content,
    })
}

fn capitalize(s: &str) -> String {
    let mut chars = s.chars();
    match chars.next() {
        None => String::new(),
        Some(c) => c.to_uppercase().collect::<String>() + chars.as_str(),
    }
}

fn format_pattern_name(s: &str) -> String {
    s.split('_')
        .map(capitalize)
        .collect::<Vec<_>>()
        .join(" ")
}
