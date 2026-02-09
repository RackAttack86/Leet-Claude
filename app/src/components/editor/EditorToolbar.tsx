import { Play, RotateCcw, Save, Check, Loader2 } from "lucide-react";
import { useProblemStore, useTestStore } from "@/store";
import { cn } from "@/lib/utils";

export function EditorToolbar() {
  const selectedProblem = useProblemStore((state) => state.selectedProblem);
  const isDirty = useProblemStore((state) => state.isDirty);
  const isSaving = useProblemStore((state) => state.isSaving);
  const lastSaved = useProblemStore((state) => state.lastSaved);
  const saveSolution = useProblemStore((state) => state.saveSolution);
  const resetToOriginal = useProblemStore((state) => state.resetToOriginal);

  const runTests = useTestStore((state) => state.runTests);
  const isRunning = useTestStore((state) => state.isRunning);

  const handleRunTests = () => {
    if (selectedProblem) {
      runTests(selectedProblem.path);
    }
  };

  const handleSave = () => {
    saveSolution();
  };

  const handleReset = () => {
    if (confirm("Reset to original solution? Your changes will be lost.")) {
      resetToOriginal();
    }
  };

  const formatLastSaved = (date: Date | null) => {
    if (!date) return null;
    return date.toLocaleTimeString();
  };

  return (
    <div className="flex items-center justify-between px-3 py-2 border-b border-border bg-background">
      <div className="flex items-center gap-2">
        {/* Run Tests */}
        <button
          onClick={handleRunTests}
          disabled={isRunning}
          className={cn(
            "flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded transition-colors",
            "bg-green-600 hover:bg-green-700 text-white",
            isRunning && "opacity-50 cursor-not-allowed"
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
          disabled={!isDirty}
          className={cn(
            "flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded transition-colors",
            "bg-secondary hover:bg-secondary/80 text-foreground",
            !isDirty && "opacity-50 cursor-not-allowed"
          )}
          title="Reset to original solution"
        >
          <RotateCcw className="h-4 w-4" />
          Reset
        </button>

        {/* Manual Save */}
        <button
          onClick={handleSave}
          disabled={!isDirty || isSaving}
          className={cn(
            "flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded transition-colors",
            "bg-secondary hover:bg-secondary/80 text-foreground",
            (!isDirty || isSaving) && "opacity-50 cursor-not-allowed"
          )}
          title="Save (auto-saves after 1.5s)"
        >
          <Save className="h-4 w-4" />
          Save
        </button>
      </div>

      {/* Save status */}
      <div className="flex items-center gap-2 text-xs text-muted-foreground">
        {isSaving && (
          <span className="flex items-center gap-1">
            <Loader2 className="h-3 w-3 animate-spin" />
            Saving...
          </span>
        )}
        {!isSaving && isDirty && (
          <span className="text-yellow-500">Unsaved changes</span>
        )}
        {!isSaving && !isDirty && lastSaved && (
          <span className="flex items-center gap-1 text-green-500">
            <Check className="h-3 w-3" />
            Saved at {formatLastSaved(lastSaved)}
          </span>
        )}
      </div>
    </div>
  );
}
