import { Play, RotateCcw, Loader2 } from "lucide-react";
import { useProblemStore, useTestStore } from "@/store";
import { cn } from "@/lib/utils";

export function EditorToolbar() {
  const selectedProblem = useProblemStore((state) => state.selectedProblem);
  const solutionCode = useProblemStore((state) => state.solutionCode);
  const originalCode = useProblemStore((state) => state.originalCode);
  const resetToOriginal = useProblemStore((state) => state.resetToOriginal);

  const runTests = useTestStore((state) => state.runTests);
  const isRunning = useTestStore((state) => state.isRunning);

  // Check if code differs from original (for Reset button)
  const hasChanges = solutionCode !== originalCode;

  const handleRunTests = () => {
    if (selectedProblem && solutionCode) {
      runTests(selectedProblem.path, solutionCode);
    }
  };

  const handleReset = () => {
    if (confirm("Reset to starter template? Your changes will be lost.")) {
      resetToOriginal();
    }
  };

  return (
    <div className="flex items-center justify-between px-3 py-2 border-b border-border bg-background">
      <div className="flex items-center gap-2">
        {/* Run Tests */}
        <button
          onClick={handleRunTests}
          disabled={isRunning || !solutionCode}
          className={cn(
            "flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded transition-colors",
            "bg-green-600 hover:bg-green-700 text-white",
            (isRunning || !solutionCode) && "opacity-50 cursor-not-allowed"
          )}
        >
          {isRunning ? (
            <Loader2 className="h-4 w-4 animate-spin" />
          ) : (
            <Play className="h-4 w-4" />
          )}
          Run Tests
        </button>

        {/* Reset */}
        <button
          onClick={handleReset}
          disabled={!hasChanges}
          className={cn(
            "flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded transition-colors",
            "bg-secondary hover:bg-secondary/80 text-foreground",
            !hasChanges && "opacity-50 cursor-not-allowed"
          )}
          title="Reset to starter template"
        >
          <RotateCcw className="h-4 w-4" />
          Reset
        </button>
      </div>

      {/* Status indicator */}
      <div className="text-xs text-muted-foreground">
        {hasChanges && (
          <span className="text-yellow-500">Modified</span>
        )}
      </div>
    </div>
  );
}
