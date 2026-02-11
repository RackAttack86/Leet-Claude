import { create } from "zustand";
import type { Problem, ProblemContent, TreeNode } from "@/types";
import {
  getProblemTree,
  getProblemContent,
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

  // Keyboard navigation
  focusedNodeId: string | null;

  // Editor state (ephemeral - not saved)
  solutionCode: string;
  originalCode: string;

  // Actions
  loadProblems: () => Promise<void>;
  selectProblem: (problem: Problem) => Promise<void>;
  setSolutionCode: (code: string) => void;
  resetToOriginal: () => void;
  toggleNode: (nodeId: string) => void;
  clearError: () => void;
  setFocusedNodeId: (nodeId: string | null) => void;
  getVisibleNodes: () => TreeNode[];
  focusNextNode: () => void;
  focusPrevNode: () => void;
  focusFirstNode: () => void;
  focusLastNode: () => void;
  expandFocusedNode: () => void;
  collapseFocusedNode: () => void;
  activateFocusedNode: () => void;
}

// Helper to flatten visible nodes (expanded folders + all their visible children)
function flattenVisibleNodes(nodes: TreeNode[]): TreeNode[] {
  const result: TreeNode[] = [];
  for (const node of nodes) {
    result.push(node);
    if (node.children && node.expanded) {
      result.push(...flattenVisibleNodes(node.children));
    }
  }
  return result;
}

// Helper to find a node by ID in the tree
function findNodeById(nodes: TreeNode[], id: string): TreeNode | null {
  for (const node of nodes) {
    if (node.id === id) return node;
    if (node.children) {
      const found = findNodeById(node.children, id);
      if (found) return found;
    }
  }
  return null;
}

// Helper to find parent of a node
function findParentNode(nodes: TreeNode[], targetId: string, parent: TreeNode | null = null): TreeNode | null {
  for (const node of nodes) {
    if (node.id === targetId) return parent;
    if (node.children) {
      const found = findParentNode(node.children, targetId, node);
      if (found !== null) return found;
    }
  }
  return null;
}

export const useProblemStore = create<ProblemState>((set, get) => ({
  tree: [],
  loading: true,
  error: null,
  selectedProblem: null,
  problemContent: null,
  focusedNodeId: null,
  solutionCode: "",
  originalCode: "",

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
      // content.starterCode contains the template for the editor
      // content.solution contains the full solution for the Full Solution panel
      set({
        selectedProblem: problem,
        problemContent: content,
        solutionCode: content.starterCode,
        originalCode: content.starterCode,
        loading: false,
      });
    } catch (err) {
      set({ error: String(err), loading: false });
    }
  },

  setSolutionCode: (code: string) => {
    set({ solutionCode: code });
  },

  resetToOriginal: () => {
    const { originalCode } = get();
    set({ solutionCode: originalCode });
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

  clearError: () => {
    set({ error: null });
  },

  setFocusedNodeId: (nodeId) => {
    set({ focusedNodeId: nodeId });
  },

  getVisibleNodes: () => {
    const { tree } = get();
    return flattenVisibleNodes(tree);
  },

  focusNextNode: () => {
    const { focusedNodeId, tree } = get();
    const visible = flattenVisibleNodes(tree);
    if (visible.length === 0) return;

    if (!focusedNodeId) {
      set({ focusedNodeId: visible[0].id });
      return;
    }

    const currentIndex = visible.findIndex((n) => n.id === focusedNodeId);
    if (currentIndex < visible.length - 1) {
      set({ focusedNodeId: visible[currentIndex + 1].id });
    }
  },

  focusPrevNode: () => {
    const { focusedNodeId, tree } = get();
    const visible = flattenVisibleNodes(tree);
    if (visible.length === 0) return;

    if (!focusedNodeId) {
      set({ focusedNodeId: visible[visible.length - 1].id });
      return;
    }

    const currentIndex = visible.findIndex((n) => n.id === focusedNodeId);
    if (currentIndex > 0) {
      set({ focusedNodeId: visible[currentIndex - 1].id });
    }
  },

  focusFirstNode: () => {
    const { tree } = get();
    const visible = flattenVisibleNodes(tree);
    if (visible.length > 0) {
      set({ focusedNodeId: visible[0].id });
    }
  },

  focusLastNode: () => {
    const { tree } = get();
    const visible = flattenVisibleNodes(tree);
    if (visible.length > 0) {
      set({ focusedNodeId: visible[visible.length - 1].id });
    }
  },

  expandFocusedNode: () => {
    const { focusedNodeId, tree, toggleNode } = get();
    if (!focusedNodeId) return;

    const node = findNodeById(tree, focusedNodeId);
    if (!node) return;

    // If it's a folder and collapsed, expand it
    if (node.children && node.children.length > 0 && !node.expanded) {
      toggleNode(focusedNodeId);
    }
    // If it's expanded or a leaf, move to first child
    else if (node.children && node.children.length > 0 && node.expanded) {
      set({ focusedNodeId: node.children[0].id });
    }
  },

  collapseFocusedNode: () => {
    const { focusedNodeId, tree, toggleNode } = get();
    if (!focusedNodeId) return;

    const node = findNodeById(tree, focusedNodeId);
    if (!node) return;

    // If it's a folder and expanded, collapse it
    if (node.children && node.children.length > 0 && node.expanded) {
      toggleNode(focusedNodeId);
    }
    // Otherwise, move to parent
    else {
      const parent = findParentNode(tree, focusedNodeId);
      if (parent) {
        set({ focusedNodeId: parent.id });
      }
    }
  },

  activateFocusedNode: () => {
    const { focusedNodeId, tree, selectProblem, toggleNode } = get();
    if (!focusedNodeId) return;

    const node = findNodeById(tree, focusedNodeId);
    if (!node) return;

    if (node.type === "problem" && node.data) {
      selectProblem(node.data);
    } else if (node.children && node.children.length > 0) {
      toggleNode(focusedNodeId);
    }
  },
}));
