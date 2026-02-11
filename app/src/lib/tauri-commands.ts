import { invoke } from "@tauri-apps/api/tauri";
import type { TreeNode, ProblemContent, TestRunResult } from "@/types";

// Get the problem tree structure for navigation
export async function getProblemTree(problemsDir: string): Promise<TreeNode[]> {
  return invoke<TreeNode[]>("get_problem_tree", { problemsDir });
}

// Get full content for a selected problem
export async function getProblemContent(
  problemPath: string
): Promise<ProblemContent> {
  return invoke<ProblemContent>("get_problem_content", { problemPath });
}

// Read solution.py content
export async function readSolution(path: string): Promise<string> {
  return invoke<string>("read_solution", { path });
}

// Run pytest for a problem with code from editor
export async function runTests(problemPath: string, code: string): Promise<TestRunResult> {
  return invoke<TestRunResult>("run_tests", { problemPath, code });
}

// Get the problems directory path
export async function getProblemsDir(): Promise<string> {
  return invoke<string>("get_problems_dir");
}
