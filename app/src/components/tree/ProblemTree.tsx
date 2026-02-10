import { useCallback, useRef, useEffect } from "react";
import { useProblemStore } from "@/store";
import { TreeNode as TreeNodeType } from "@/types";
import { TreeNode } from "./TreeNode";

export function ProblemTree() {
  const tree = useProblemStore((state) => state.tree);
  const loading = useProblemStore((state) => state.loading);
  const error = useProblemStore((state) => state.error);
  const focusedNodeId = useProblemStore((state) => state.focusedNodeId);
  const focusNextNode = useProblemStore((state) => state.focusNextNode);
  const focusPrevNode = useProblemStore((state) => state.focusPrevNode);
  const focusFirstNode = useProblemStore((state) => state.focusFirstNode);
  const focusLastNode = useProblemStore((state) => state.focusLastNode);
  const expandFocusedNode = useProblemStore((state) => state.expandFocusedNode);
  const collapseFocusedNode = useProblemStore((state) => state.collapseFocusedNode);
  const activateFocusedNode = useProblemStore((state) => state.activateFocusedNode);

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
