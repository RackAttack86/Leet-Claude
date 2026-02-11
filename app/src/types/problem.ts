// Core problem metadata structure
export interface ProblemMetadata {
  number: number;
  name: string;
  difficulty: "Easy" | "Medium" | "Hard";
  pattern: string;
  topics: string[];
  url: string;
  companies: string[];
  timeComplexity: string;
  spaceComplexity: string;
}

// Full problem with path info
export interface Problem extends ProblemMetadata {
  slug: string;
  path: string;
}

// Problem content loaded when selected
export interface ProblemContent {
  definition: string;
  hints: string[];
  solution: string;      // Full solution for display
  starterCode: string;   // Template/starter for editor
  explanation: string;
  readme: string;
}

// Tree node for navigation
export interface TreeNode {
  id: string;
  label: string;
  type: "pattern" | "difficulty" | "problem";
  children?: TreeNode[];
  data?: Problem;
  expanded?: boolean;
}

// Test execution results
export interface TestResult {
  passed: boolean;
  testName: string;
  output: string;
  error?: string;
  duration: number;
}

export interface TestRunResult {
  success: boolean;
  total: number;
  passed: number;
  failed: number;
  results: TestResult[];
  rawOutput: string;
}
