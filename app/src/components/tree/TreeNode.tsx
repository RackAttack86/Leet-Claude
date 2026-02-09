import { ChevronRight, ChevronDown, Folder, FolderOpen, FileCode } from "lucide-react";
import { useProblemStore } from "@/store";
import { TreeNode as TreeNodeType, Problem } from "@/types";
import { cn } from "@/lib/utils";

interface TreeNodeProps {
  node: TreeNodeType;
  level: number;
}

export function TreeNode({ node, level }: TreeNodeProps) {
  const toggleNode = useProblemStore((state) => state.toggleNode);
  const selectProblem = useProblemStore((state) => state.selectProblem);
  const selectedProblem = useProblemStore((state) => state.selectedProblem);

  const hasChildren = node.children && node.children.length > 0;
  const isExpanded = node.expanded;
  const isSelected = node.data && selectedProblem?.number === node.data.number;

  const handleClick = () => {
    if (node.type === "problem" && node.data) {
      selectProblem(node.data);
    } else if (hasChildren) {
      toggleNode(node.id);
    }
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty.toLowerCase()) {
      case "easy":
        return "text-green-500";
      case "medium":
        return "text-yellow-500";
      case "hard":
        return "text-red-500";
      default:
        return "text-muted-foreground";
    }
  };

  const getIcon = () => {
    if (node.type === "problem") {
      return <FileCode className="h-4 w-4 text-muted-foreground" />;
    }
    if (isExpanded) {
      return <FolderOpen className="h-4 w-4 text-yellow-500" />;
    }
    return <Folder className="h-4 w-4 text-yellow-500" />;
  };

  return (
    <div>
      <button
        onClick={handleClick}
        className={cn(
          "w-full flex items-center gap-1 px-2 py-1 text-left text-sm hover:bg-accent/50 transition-colors",
          isSelected && "bg-accent"
        )}
        style={{ paddingLeft: `${level * 12 + 8}px` }}
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
        {getIcon()}

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
}
