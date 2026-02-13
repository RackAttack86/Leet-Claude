import { useCallback, useRef, useEffect } from "react";
import { useProblemStore } from "@/store";
import { shallow } from "zustand/shallow";
import { TreeNode as TreeNodeType } from "@/types";
import { TreeNode } from "./TreeNode";

export function ProblemTree() {
  // Batch state subscriptions to reduce re-renders
  const { tree, loading, error, focusedNodeId } = useProblemStore(
    (state) => ({
      tree: state.tree,
      loading: state.loading,
      error: state.error,
      focusedNodeId: state.focusedNodeId,
    }),
    shallow
  );

  // Batch action subscriptions (these are stable references from Zustand)
  const {
    focusNextNode,
    focusPrevNode,
    focusFirstNode,
    focusLastNode,
    expandFocusedNode,
    collapseFocusedNode,
    activateFocusedNode,
  } = useProblemStore(
    (state) => ({
      focusNextNode: state.focusNextNode,
      focusPrevNode: state.focusPrevNode,
      focusFirstNode: state.focusFirstNode,
      focusLastNode: state.focusLastNode,
      expandFocusedNode: state.expandFocusedNode,
      collapseFocusedNode: state.collapseFocusedNode,
      activateFocusedNode: state.activateFocusedNode,
    }),
    shallow
  );

  const containerRef = useRef<HTMLDivElement>(null);

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      switch (e.key) {
        case "ArrowDown":
          e.preventDefault();
          focusNextNode();
          break;
        case "ArrowUp":
          e.preventDefault();
          focusPrevNode();
          break;
        case "ArrowRight":
          e.preventDefault();
          expandFocusedNode();
          break;
        case "ArrowLeft":
          e.preventDefault();
          collapseFocusedNode();
          break;
        case "Enter":
        case " ":
          e.preventDefault();
          activateFocusedNode();
          break;
        case "Home":
          e.preventDefault();
          focusFirstNode();
          break;
        case "End":
          e.preventDefault();
          focusLastNode();
          break;
      }
    },
    [focusNextNode, focusPrevNode, expandFocusedNode, collapseFocusedNode, activateFocusedNode, focusFirstNode, focusLastNode]
  );

  // Scroll focused node into view
  useEffect(() => {
    if (focusedNodeId && containerRef.current) {
      const focusedElement = containerRef.current.querySelector(`[data-node-id="${focusedNodeId}"]`);
      focusedElement?.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  }, [focusedNodeId]);

  if (loading) {
    return (
      <div className="p-4 text-sm text-muted-foreground">
        Loading problems...
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-4 text-sm text-destructive">
        Error: {error}
      </div>
    );
  }

  if (tree.length === 0) {
    return (
      <div className="p-4 text-sm text-muted-foreground">
        No problems found
      </div>
    );
  }

  return (
    <div
      ref={containerRef}
      className="py-2 outline-none"
      tabIndex={0}
      role="tree"
      aria-label="Problem navigation"
      onKeyDown={handleKeyDown}
    >
      {tree.map((node: TreeNodeType) => (
        <TreeNode key={node.id} node={node} level={0} />
      ))}
    </div>
  );
}
