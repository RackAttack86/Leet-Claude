import { useEffect } from "react";
import { useProblemStore } from "@/store";
import { AppLayout } from "@/components/layout/AppLayout";
import { useKeyboardShortcuts } from "@/hooks";

function App() {
  const loadProblems = useProblemStore((state) => state.loadProblems);

  // Initialize keyboard shortcuts
  useKeyboardShortcuts();

  useEffect(() => {
    loadProblems();
  }, [loadProblems]);

  return <AppLayout />;
}

export default App;
