import { memo, useCallback, useMemo } from "react";
import { ChevronRight, ChevronDown, Folder, FolderOpen, FileCode } from "lucide-react";
import { useProblemStore } from "@/store";
import { TreeNode as TreeNodeType } from "@/types";
import { cn, getDifficultyColor } from "@/lib/utils";

interface TreeNodeProps {
  node: TreeNodeType;
  level: number;
}

export const TreeNode = memo(function TreeNode({ node, level }: TreeNodeProps) {
  const toggleNode = useProblemStore((state) => state.toggleNode);
  const selectProblem = useProblemStore((state) => state.selectProblem);
  const selectedProblemNumber = useProblemStore((state) => state.selectedProblem?.number);
  const focusedNodeId = useProblemStore((state) => state.focusedNodeId);
  const setFocusedNodeId = useProblemStore((state) => state.setFocusedNodeId);

  const hasChildren = node.children && node.children.length > 0;
  const isExpanded = node.expanded;
  const isSelected = node.data && selectedProblemNumber === node.data.number;
  const isFocused = focusedNodeId === node.id;

  const handleClick = useCallback(() => {
    setFocusedNodeId(node.id);
    if (node.type === "problem" && node.data) {
      selectProblem(node.data);
    } else if (hasChildren) {
      toggleNode(node.id);
    }
  }, [node.type, node.data, node.id, hasChildren, selectProblem, toggleNode, setFocusedNodeId]);

  const icon = useMemo(() => {
    if (node.type === "problem") {
      return <FileCode className="h-4 w-4 text-muted-foreground" />;
    }
    if (isExpanded) {
      return <FolderOpen className="h-4 w-4 text-yellow-500" />;
    }
    return <Folder className="h-4 w-4 text-yellow-500" />;
  }, [node.type, isExpanded]);

  const paddingLeft = useMemo(() => ({ paddingLeft: `${level * 12 + 8}px` }), [level]);

  return (
    <div role="treeitem" aria-expanded={hasChildren ? isExpanded : undefined} data-node-id={node.id}>
      <button
        onClick={handleClick}
        className={cn(
          "w-full flex items-center gap-1 px-2 py-1 text-left text-sm hover:bg-accent/50 transition-colors",
          isSelected && "bg-accent",
          isFocused && "ring-1 ring-primary ring-inset"
        )}
        style={paddingLeft}
        tabIndex={-1}
      >
        {/* Expand/collapse chevron */}
        {hasChildren ? (
          isExpanded ? (
            <ChevronDown className="h-4 w-4 shrink-0" />
          ) : (
            <ChevronRight className="h-4 w-4 shrink-0" />
          )
        ) : (
          <span className="w-4 shrink-0" />
        )}

        {/* Icon */}
        {icon}

        {/* Label */}
        <span
          className={cn(
            "truncate",
            node.type === "difficulty" && getDifficultyColor(node.label)
          )}
        >
          {node.label}
        </span>

        {/* Problem difficulty badge */}
        {node.type === "problem" && node.data && (
          <span
            className={cn(
              "ml-auto text-xs px-1.5 py-0.5 rounded",
              getDifficultyColor(node.data.difficulty)
            )}
          >
            {node.data.difficulty.charAt(0)}
          </span>
        )}
      </button>

      {/* Children */}
      {hasChildren && isExpanded && (
        <div>
          {node.children!.map((child) => (
            <TreeNode key={child.id} node={child} level={level + 1} />
          ))}
        </div>
      )}
    </div>
  );
});
