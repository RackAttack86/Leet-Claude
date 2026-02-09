import { useEffect } from "react";
import { useProblemStore, useTestStore } from "@/store";

export function useKeyboardShortcuts() {
  const saveSolution = useProblemStore((state) => state.saveSolution);
  const selectedProblem = useProblemStore((state) => state.selectedProblem);
  const runTests = useTestStore((state) => state.runTests);
  const isRunning = useTestStore((state) => state.isRunning);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Ctrl+S or Cmd+S - Save
      if ((e.ctrlKey || e.metaKey) && e.key === "s") {
        e.preventDefault();
        saveSolution();
      }

      // Ctrl+Enter or Cmd+Enter - Run tests
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        e.preventDefault();
        if (selectedProblem && !isRunning) {
          runTests(selectedProblem.path);
        }
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [saveSolution, selectedProblem, runTests, isRunning]);
}
