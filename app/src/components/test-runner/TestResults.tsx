import { useState } from "react";
import { CheckCircle, XCircle, ChevronDown, ChevronRight } from "lucide-react";
import type { TestRunResult } from "@/types";
import { cn } from "@/lib/utils";

interface TestResultsProps {
  results: TestRunResult;
}

export function TestResults({ results }: TestResultsProps) {
  const [showRaw, setShowRaw] = useState(false);

  return (
    <div className="space-y-2">
      {/* Individual test results */}
      {results.results.map((test, index) => (
        <div
          key={index}
          className={cn(
            "flex items-start gap-2 p-2 rounded text-sm",
            test.passed ? "bg-green-500/10" : "bg-red-500/10"
          )}
        >
          {test.passed ? (
            <CheckCircle className="h-4 w-4 text-green-500 shrink-0 mt-0.5" />
          ) : (
            <XCircle className="h-4 w-4 text-red-500 shrink-0 mt-0.5" />
          )}
          <div className="flex-1 min-w-0">
            <span
              className={cn(
                "font-mono text-xs",
                test.passed ? "text-green-400" : "text-red-400"
              )}
            >
              {test.testName}
            </span>
            {test.error && (
              <pre className="mt-1 text-xs text-red-400 whitespace-pre-wrap">
                {test.error}
              </pre>
            )}
          </div>
        </div>
      ))}

      {/* Raw output toggle */}
      <button
        onClick={() => setShowRaw(!showRaw)}
        className="flex items-center gap-1 text-xs text-muted-foreground hover:text-foreground transition-colors mt-4"
      >
        {showRaw ? (
          <ChevronDown className="h-3 w-3" />
        ) : (
          <ChevronRight className="h-3 w-3" />
        )}
        Raw output
      </button>

      {showRaw && (
        <pre className="p-3 bg-secondary rounded text-xs font-mono overflow-x-auto whitespace-pre-wrap">
          {results.rawOutput}
        </pre>
      )}
    </div>
  );
}
