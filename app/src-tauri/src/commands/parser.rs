use regex::Regex;
use once_cell::sync::Lazy;
use crate::models::ProblemMetadata;

// ============================================================================
// PRE-COMPILED REGEX PATTERNS
// These are compiled once at startup, eliminating per-call regex compilation
// which was causing 10+ regex compilations per file read.
// ============================================================================

// Metadata extraction patterns
static RE_METADATA: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"PROBLEM_METADATA\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}"#).unwrap()
});
static RE_LIST_ITEM: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"["']([^"']+)["']"#).unwrap()
});

// Docstring extraction patterns
static RE_DOCSTRING_DOUBLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"^"""([\s\S]*?)""""#).unwrap()
});
static RE_DOCSTRING_SINGLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"^'''([\s\S]*?)'''"#).unwrap()
});

// README section patterns
static RE_KEY_INSIGHTS: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"(?i)##\s*Key\s*Insights?\s*\n([\s\S]*?)(?:\n##|$)"#).unwrap()
});
static RE_BULLET: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"[-*]\s+(.+)"#).unwrap()
});
static RE_APPROACHES: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"(?i)##\s*Approach(?:es)?\s*\n([\s\S]*?)(?:\n##|$)"#).unwrap()
});

// Code stripping patterns
static RE_MODULE_DOCSTRING_DOUBLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"^"""[\s\S]*?"""\s*\n?"#).unwrap()
});
static RE_MODULE_DOCSTRING_SINGLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"^'''[\s\S]*?'''\s*\n?"#).unwrap()
});
static RE_METADATA_WITH_COMMENT: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"\n*#?\s*Metadata.*\n?PROBLEM_METADATA\s*=\s*\{[\s\S]*?\}\s*\n?"#).unwrap()
});
static RE_METADATA_PLAIN: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"\n*PROBLEM_METADATA\s*=\s*\{[\s\S]*?\}\s*\n?"#).unwrap()
});
static RE_CLASS_DOCSTRING_DOUBLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"(class\s+\w+.*?:\s*\n)\s*"""[\s\S]*?"""\s*\n"#).unwrap()
});
static RE_CLASS_DOCSTRING_SINGLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"(class\s+\w+.*?:\s*\n)\s*'''[\s\S]*?'''\s*\n"#).unwrap()
});
static RE_METHOD_DOCSTRING_DOUBLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"(def\s+\w+\s*\([^)]*\)[^:]*:\s*\n)\s*"""[\s\S]*?"""\s*\n"#).unwrap()
});
static RE_METHOD_DOCSTRING_SINGLE: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"(def\s+\w+\s*\([^)]*\)[^:]*:\s*\n)\s*'''[\s\S]*?'''\s*\n"#).unwrap()
});
static RE_STANDALONE_COMMENT: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"(?m)^\s*#.*\n"#).unwrap()
});
static RE_MULTIPLE_NEWLINES: Lazy<Regex> = Lazy::new(|| {
    Regex::new(r#"\n{3,}"#).unwrap()
});

// Dynamic pattern builders (cached per key)
fn build_string_pattern(key: &str) -> Regex {
    Regex::new(&format!(r#"["']{}["']\s*:\s*["']([^"']+)["']"#, key)).unwrap()
}

fn build_int_pattern(key: &str) -> Regex {
    Regex::new(&format!(r#"["']{}["']\s*:\s*(\d+)"#, key)).unwrap()
}

fn build_list_pattern(key: &str) -> Regex {
    Regex::new(&format!(r#"["']{}["']\s*:\s*\[([^\]]*)\]"#, key)).unwrap()
}

// ============================================================================
// PUBLIC API
// ============================================================================

/// Parse PROBLEM_METADATA from solution.py content
pub fn parse_metadata(content: &str) -> Option<ProblemMetadata> {
    let caps = RE_METADATA.captures(content)?;
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
    let re = build_string_pattern(key);
    re.captures(content).map(|c| c.get(1).unwrap().as_str().to_string())
}

fn extract_int(content: &str, key: &str) -> Option<i32> {
    let re = build_int_pattern(key);
    re.captures(content).and_then(|c| c.get(1).unwrap().as_str().parse().ok())
}

fn extract_list(content: &str, key: &str) -> Option<Vec<String>> {
    let re = build_list_pattern(key);
    let caps = re.captures(content)?;
    let list_content = caps.get(1)?.as_str();

    let items: Vec<String> = RE_LIST_ITEM
        .captures_iter(list_content)
        .filter_map(|c| c.get(1).map(|m| m.as_str().to_string()))
        .collect();

    Some(items)
}

/// Extract the module-level docstring (problem definition)
pub fn extract_docstring(content: &str) -> String {
    if let Some(caps) = RE_DOCSTRING_DOUBLE.captures(content) {
        return caps.get(1).map(|m| m.as_str().trim().to_string()).unwrap_or_default();
    }

    if let Some(caps) = RE_DOCSTRING_SINGLE.captures(content) {
        return caps.get(1).map(|m| m.as_str().trim().to_string()).unwrap_or_default();
    }

    String::new()
}

/// Extract Key Insights section from README.md
pub fn extract_hints(readme: &str) -> Vec<String> {
    if let Some(caps) = RE_KEY_INSIGHTS.captures(readme) {
        let section = caps.get(1).map(|m| m.as_str()).unwrap_or("");
        return RE_BULLET
            .captures_iter(section)
            .filter_map(|c| c.get(1).map(|m| m.as_str().trim().to_string()))
            .collect();
    }

    Vec::new()
}

/// Extract Approaches section from README.md
pub fn extract_explanation(readme: &str) -> String {
    if let Some(caps) = RE_APPROACHES.captures(readme) {
        return caps.get(1).map(|m| m.as_str().trim().to_string()).unwrap_or_default();
    }

    String::new()
}

/// Strip comments, docstrings, and metadata from code for a clean editor display
pub fn strip_code_for_editor(content: &str) -> String {
    let mut result = content.to_string();

    // Remove module-level docstring (at the start of file)
    result = RE_MODULE_DOCSTRING_DOUBLE.replace(&result, "").to_string();
    result = RE_MODULE_DOCSTRING_SINGLE.replace(&result, "").to_string();

    // Remove PROBLEM_METADATA dict
    result = RE_METADATA_WITH_COMMENT.replace(&result, "").to_string();
    result = RE_METADATA_PLAIN.replace(&result, "").to_string();

    // Remove class docstrings
    result = RE_CLASS_DOCSTRING_DOUBLE.replace_all(&result, "$1").to_string();
    result = RE_CLASS_DOCSTRING_SINGLE.replace_all(&result, "$1").to_string();

    // Remove method docstrings
    result = RE_METHOD_DOCSTRING_DOUBLE.replace_all(&result, "$1").to_string();
    result = RE_METHOD_DOCSTRING_SINGLE.replace_all(&result, "$1").to_string();

    // Remove standalone comment blocks
    result = RE_STANDALONE_COMMENT.replace_all(&result, "").to_string();

    // Clean up multiple consecutive blank lines
    result = RE_MULTIPLE_NEWLINES.replace_all(&result, "\n\n").to_string();

    result.trim().to_string()
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
