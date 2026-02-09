use regex::Regex;
use crate::models::ProblemMetadata;

/// Parse PROBLEM_METADATA from solution.py content
pub fn parse_metadata(content: &str) -> Option<ProblemMetadata> {
    // Find the PROBLEM_METADATA dict
    let re = Regex::new(r#"PROBLEM_METADATA\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}"#).ok()?;
    let caps = re.captures(content)?;
    let dict_content = caps.get(1)?.as_str();

    // Extract individual fields
    let number = extract_int(dict_content, "number").unwrap_or(0);
    let name = extract_string(dict_content, "name").unwrap_or_default();
    let difficulty = extract_string(dict_content, "difficulty").unwrap_or_default();
    let pattern = extract_string(dict_content, "pattern").unwrap_or_default();
    let url = extract_string(dict_content, "url").unwrap_or_default();
    let time_complexity = extract_string(dict_content, "time_complexity").unwrap_or_default();
    let space_complexity = extract_string(dict_content, "space_complexity").unwrap_or_default();
    let topics = extract_list(dict_content, "topics").unwrap_or_default();
    let companies = extract_list(dict_content, "companies").unwrap_or_default();

    Some(ProblemMetadata {
        number,
        name,
        difficulty,
        pattern,
        topics,
        url,
        companies,
        time_complexity,
        space_complexity,
    })
}

fn extract_string(content: &str, key: &str) -> Option<String> {
    let pattern = format!(r#"["']{}["']\s*:\s*["']([^"']+)["']"#, key);
    let re = Regex::new(&pattern).ok()?;
    re.captures(content).map(|c| c.get(1).unwrap().as_str().to_string())
}

fn extract_int(content: &str, key: &str) -> Option<i32> {
    let pattern = format!(r#"["']{}["']\s*:\s*(\d+)"#, key);
    let re = Regex::new(&pattern).ok()?;
    re.captures(content).and_then(|c| c.get(1).unwrap().as_str().parse().ok())
}

fn extract_list(content: &str, key: &str) -> Option<Vec<String>> {
    let pattern = format!(r#"["']{}["']\s*:\s*\[([^\]]*)\]"#, key);
    let re = Regex::new(&pattern).ok()?;
    let caps = re.captures(content)?;
    let list_content = caps.get(1)?.as_str();

    let item_re = Regex::new(r#"["']([^"']+)["']"#).ok()?;
    let items: Vec<String> = item_re
        .captures_iter(list_content)
        .filter_map(|c| c.get(1).map(|m| m.as_str().to_string()))
        .collect();

    Some(items)
}

/// Extract the module-level docstring (problem definition)
pub fn extract_docstring(content: &str) -> String {
    let re = Regex::new(r#"^"""([\s\S]*?)""""#).ok();
    if let Some(re) = re {
        if let Some(caps) = re.captures(content) {
            return caps.get(1).map(|m| m.as_str().trim().to_string()).unwrap_or_default();
        }
    }

    // Try single quotes
    let re = Regex::new(r#"^'''([\s\S]*?)'''"#).ok();
    if let Some(re) = re {
        if let Some(caps) = re.captures(content) {
            return caps.get(1).map(|m| m.as_str().trim().to_string()).unwrap_or_default();
        }
    }

    String::new()
}

/// Extract Key Insights section from README.md
pub fn extract_hints(readme: &str) -> Vec<String> {
    // Find the Key Insights section
    let section_re = Regex::new(r#"(?i)##\s*Key\s*Insights?\s*\n([\s\S]*?)(?:\n##|$)"#).ok();

    if let Some(re) = section_re {
        if let Some(caps) = re.captures(readme) {
            let section = caps.get(1).map(|m| m.as_str()).unwrap_or("");

            // Extract bullet points
            let bullet_re = Regex::new(r#"[-*]\s+(.+)"#).ok();
            if let Some(bullet_re) = bullet_re {
                return bullet_re
                    .captures_iter(section)
                    .filter_map(|c| c.get(1).map(|m| m.as_str().trim().to_string()))
                    .collect();
            }
        }
    }

    Vec::new()
}

/// Extract Approaches section from README.md
pub fn extract_explanation(readme: &str) -> String {
    let section_re = Regex::new(r#"(?i)##\s*Approach(?:es)?\s*\n([\s\S]*?)(?:\n##|$)"#).ok();

    if let Some(re) = section_re {
        if let Some(caps) = re.captures(readme) {
            return caps.get(1).map(|m| m.as_str().trim().to_string()).unwrap_or_default();
        }
    }

    String::new()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_metadata() {
        let content = r#"
PROBLEM_METADATA = {
    "number": 26,
    "name": "Remove Duplicates from Sorted Array",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Two Pointers'],
    "url": "https://leetcode.com/problems/remove-duplicates-from-sorted-array/",
    "companies": ['Amazon'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
"#;
        let metadata = parse_metadata(content).unwrap();
        assert_eq!(metadata.number, 26);
        assert_eq!(metadata.name, "Remove Duplicates from Sorted Array");
        assert_eq!(metadata.difficulty, "Easy");
    }
}
