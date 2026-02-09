import { useState } from "react";
import { ChevronLeft, ChevronRight, FolderTree } from "lucide-react";
import { ProblemTree } from "@/components/tree/ProblemTree";
import { cn } from "@/lib/utils";

export function TreeSidebar() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div
      className={cn(
        "h-full bg-secondary/30 border-r border-border flex flex-col transition-all duration-200",
        collapsed ? "w-12" : "w-72"
      )}
    >
      {/* Header */}
      <div className="flex items-center justify-between p-3 border-b border-border">
        {!collapsed && (
          <div className="flex items-center gap-2">
            <FolderTree className="h-4 w-4 text-muted-foreground" />
            <span className="font-medium text-sm">Problems</span>
          </div>
        )}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="p-1 hover:bg-accent rounded transition-colors"
          title={collapsed ? "Expand sidebar" : "Collapse sidebar"}
        >
          {collapsed ? (
            <ChevronRight className="h-4 w-4" />
          ) : (
            <ChevronLeft className="h-4 w-4" />
          )}
        </button>
      </div>

      {/* Tree content */}
      {!collapsed && (
        <div className="flex-1 overflow-auto">
          <ProblemTree />
        </div>
      )}

      {/* Collapsed icon */}
      {collapsed && (
        <div className="flex-1 flex items-start justify-center pt-4">
          <FolderTree className="h-5 w-5 text-muted-foreground" />
        </div>
      )}
    </div>
  );
}
