import { create } from "zustand";
import type { Problem, ProblemContent, TreeNode } from "@/types";
import {
  getProblemTree,
  getProblemContent,
  writeSolution,
  getProblemsDir,
} from "@/lib/tauri-commands";

interface ProblemState {
  // Tree data
  tree: TreeNode[];
  loading: boolean;
  error: string | null;

  // Current selection
  selectedProblem: Problem | null;
  problemContent: ProblemContent | null;

  // Editor state
  solutionCode: string;
  originalCode: string;
  isDirty: boolean;
  isSaving: boolean;
  lastSaved: Date | null;

  // Actions
  loadProblems: () => Promise<void>;
  selectProblem: (problem: Problem) => Promise<void>;
  setSolutionCode: (code: string) => void;
  saveSolution: () => Promise<void>;
  resetToOriginal: () => void;
  toggleNode: (nodeId: string) => void;
}

export const useProblemStore = create<ProblemState>((set, get) => ({
  tree: [],
  loading: true,
  error: null,
  selectedProblem: null,
  problemContent: null,
  solutionCode: "",
  originalCode: "",
  isDirty: false,
  isSaving: false,
  lastSaved: null,

  loadProblems: async () => {
    try {
      set({ loading: true, error: null });
      const problemsDir = await getProblemsDir();
      const tree = await getProblemTree(problemsDir);
      set({ tree, loading: false });
    } catch (err) {
      set({ error: String(err), loading: false });
    }
  },

  selectProblem: async (problem: Problem) => {
    try {
      set({ loading: true, error: null });
      const content = await getProblemContent(problem.path);
      set({
        selectedProblem: problem,
        problemContent: content,
        solutionCode: content.solution,
        originalCode: content.solution,
        isDirty: false,
        loading: false,
      });
    } catch (err) {
      set({ error: String(err), loading: false });
    }
  },

  setSolutionCode: (code: string) => {
    const { originalCode } = get();
    set({
      solutionCode: code,
      isDirty: code !== originalCode,
    });
  },

  saveSolution: async () => {
    const { selectedProblem, solutionCode } = get();
    if (!selectedProblem) return;

    try {
      set({ isSaving: true });
      // Use backslash for Windows path - save to starter.py (user's work)
      const starterPath = `${selectedProblem.path}\\starter.py`;
      await writeSolution(starterPath, solutionCode);
      set({
        isSaving: false,
        isDirty: false,
        originalCode: solutionCode,
        lastSaved: new Date(),
      });
    } catch (err) {
      set({ isSaving: false, error: String(err) });
    }
  },

  resetToOriginal: () => {
    const { originalCode } = get();
    set({
      solutionCode: originalCode,
      isDirty: false,
    });
  },

  toggleNode: (nodeId: string) => {
    const { tree } = get();
    const toggleInTree = (nodes: TreeNode[]): TreeNode[] => {
      return nodes.map((node) => {
        if (node.id === nodeId) {
          return { ...node, expanded: !node.expanded };
        }
        if (node.children) {
          return { ...node, children: toggleInTree(node.children) };
        }
        return node;
      });
    };
    set({ tree: toggleInTree(tree) });
  },
}));
