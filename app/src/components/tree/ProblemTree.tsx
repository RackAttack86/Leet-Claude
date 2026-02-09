import { useProblemStore } from "@/store";
import { TreeNode as TreeNodeType } from "@/types";
import { TreeNode } from "./TreeNode";

export function ProblemTree() {
  const tree = useProblemStore((state) => state.tree);
  const loading = useProblemStore((state) => state.loading);
  const error = useProblemStore((state) => state.error);

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
    <div className="py-2">
      {tree.map((node: TreeNodeType) => (
        <TreeNode key={node.id} node={node} level={0} />
      ))}
    </div>
  );
}
