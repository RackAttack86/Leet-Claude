import { Terminal, CheckCircle, XCircle, Loader2 } from "lucide-react";
import { useTestStore } from "@/store";
import { TestResults } from "./TestResults";


export function TestRunner() {
  const isRunning = useTestStore((state) => state.isRunning);
  const results = useTestStore((state) => state.results);
  const error = useTestStore((state) => state.error);

  return (
    <div className="h-full flex flex-col bg-background border-t border-border">
      {/* Header */}
      <div className="flex items-center justify-between px-3 py-2 border-b border-border bg-secondary/30">
        <div className="flex items-center gap-2">
          <Terminal className="h-4 w-4 text-muted-foreground" />
          <span className="text-sm font-medium">Test Results</span>
        </div>

        {/* Summary */}
        {results && !isRunning && (
          <div className="flex items-center gap-3 text-xs">
            <span className="flex items-center gap-1 text-green-500">
              <CheckCircle className="h-3 w-3" />
              {results.passed} passed
            </span>
            {results.failed > 0 && (
              <span className="flex items-center gap-1 text-red-500">
                <XCircle className="h-3 w-3" />
                {results.failed} failed
              </span>
            )}
            <span className="text-muted-foreground">
              {results.total} total
            </span>
          </div>
        )}

        {isRunning && (
          <span className="flex items-center gap-1 text-xs text-muted-foreground">
            <Loader2 className="h-3 w-3 animate-spin" />
            Running tests...
          </span>
        )}
      </div>

      {/* Content */}
      <div className="flex-1 overflow-auto p-3">
        {isRunning && (
          <div className="flex items-center justify-center h-full">
            <div className="flex items-center gap-2 text-muted-foreground">
              <Loader2 className="h-5 w-5 animate-spin" />
              <span>Running tests...</span>
            </div>
          </div>
        )}

        {error && !isRunning && (
          <div className="p-3 bg-red-500/10 border border-red-500/30 rounded">
            <p className="text-sm text-red-500">Error: {error}</p>
          </div>
        )}

        {results && !isRunning && (
          <TestResults results={results} />
        )}

        {!results && !isRunning && !error && (
          <div className="flex items-center justify-center h-full text-muted-foreground text-sm">
            Click "Run Tests" to execute the test suite
          </div>
        )}
      </div>
    </div>
  );
}
