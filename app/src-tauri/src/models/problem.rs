use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ProblemMetadata {
    pub number: i32,
    pub name: String,
    pub difficulty: String,
    pub pattern: String,
    pub topics: Vec<String>,
    pub url: String,
    pub companies: Vec<String>,
    pub time_complexity: String,
    pub space_complexity: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Problem {
    pub number: i32,
    pub name: String,
    pub slug: String,
    pub difficulty: String,
    pub pattern: String,
    pub topics: Vec<String>,
    pub url: String,
    pub companies: Vec<String>,
    pub time_complexity: String,
    pub space_complexity: String,
    pub path: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ProblemContent {
    pub definition: String,
    pub hints: Vec<String>,
    pub solution: String,
    pub starter_code: String,
    pub explanation: String,
    pub readme: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct TreeNode {
    pub id: String,
    pub label: String,
    #[serde(rename = "type")]
    pub node_type: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub children: Option<Vec<TreeNode>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub data: Option<Problem>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub expanded: Option<bool>,
}
