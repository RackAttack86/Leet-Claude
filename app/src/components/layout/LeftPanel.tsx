import { useProblemStore } from "@/store";
import { ProblemView } from "@/components/problem/ProblemView";
import { ErrorBoundary } from "@/components/ui";

export function LeftPanel() {
  const selectedProblem = useProblemStore((state) => state.selectedProblem);
  const loading = useProblemStore((state) => state.loading);

  if (loading) {
    return (
      <div className="h-full flex items-center justify-center bg-background">
        <div className="text-muted-foreground">Loading...</div>
      </div>
    );
  }

  if (!selectedProblem) {
    return (
      <div className="h-full flex items-center justify-center bg-background">
        <div className="text-center text-muted-foreground">
          <p className="text-lg mb-2">No problem selected</p>
          <p className="text-sm">Select a problem from the tree to get started</p>
        </div>
      </div>
    );
  }

  return (
    <div className="h-full overflow-auto bg-background">
      <ErrorBoundary name="ProblemView">
        <ProblemView />
      </ErrorBoundary>
    </div>
  );
}
