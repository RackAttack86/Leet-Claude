import { useEffect } from "react";
import { useProblemStore, useTestStore } from "@/store";

export function useKeyboardShortcuts() {
  const selectedProblem = useProblemStore((state) => state.selectedProblem);
  const solutionCode = useProblemStore((state) => state.solutionCode);
  const runTests = useTestStore((state) => state.runTests);
  const isRunning = useTestStore((state) => state.isRunning);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Ctrl+Enter or Cmd+Enter - Run tests
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        e.preventDefault();
        if (selectedProblem && !isRunning) {
          runTests(selectedProblem.path, solutionCode);
        }
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [selectedProblem, solutionCode, runTests, isRunning]);
}
