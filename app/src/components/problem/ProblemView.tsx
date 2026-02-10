import { useState } from "react";
import { ExternalLink, Loader2 } from "lucide-react";
import { useProblemStore } from "@/store";
import { Collapsible, CollapsibleTrigger, CollapsibleContent } from "@/components/ui/Collapsible";
import { ProblemDefinition } from "./ProblemDefinition";
import { Hints } from "./Hints";
import { Solution } from "./Solution";
import { Explanation } from "./Explanation";
import { cn, getDifficultyBadgeClasses } from "@/lib/utils";

function LoadingSkeleton() {
  return (
    <div className="h-full flex flex-col animate-pulse">
      <div className="p-4 border-b border-border">
        <div className="h-6 w-48 bg-muted rounded mb-3" />
        <div className="flex gap-2">
          <div className="h-5 w-16 bg-muted rounded" />
          <div className="h-5 w-24 bg-muted rounded" />
        </div>
      </div>
      <div className="p-4 space-y-4">
        <div className="h-4 w-full bg-muted rounded" />
        <div className="h-4 w-5/6 bg-muted rounded" />
        <div className="h-4 w-4/6 bg-muted rounded" />
        <div className="h-32 w-full bg-muted rounded mt-6" />
      </div>
    </div>
  );
}

function EmptyState() {
  return (
    <div className="h-full flex items-center justify-center text-muted-foreground">
      <p className="text-sm">Select a problem to get started</p>
    </div>
  );
}

export function ProblemView() {
  const selectedProblem = useProblemStore((state) => state.selectedProblem);
  const problemContent = useProblemStore((state) => state.problemContent);
  const loading = useProblemStore((state) => state.loading);

  // Section open states - definition is open by default
  const [definitionOpen, setDefinitionOpen] = useState(true);
  const [hintsOpen, setHintsOpen] = useState(false);
  const [solutionOpen, setSolutionOpen] = useState(false);
  const [explanationOpen, setExplanationOpen] = useState(false);

  // Show loading skeleton when loading a problem
  if (loading && selectedProblem) {
    return <LoadingSkeleton />;
  }

  // Show empty state when no problem selected
  if (!selectedProblem || !problemContent) {
    return <EmptyState />;
  }

  return (
    <div className="h-full flex flex-col">
      {/* Problem Header */}
      <div className="p-4 border-b border-border">
        <div className="flex items-start justify-between gap-4">
          <div>
            <h1 className="text-lg font-semibold">
              {selectedProblem.number}. {selectedProblem.name}
            </h1>
            <div className="flex items-center gap-2 mt-2">
              <span
                className={cn(
                  "px-2 py-0.5 text-xs font-medium rounded border",
                  getDifficultyBadgeClasses(selectedProblem.difficulty)
                )}
              >
                {selectedProblem.difficulty}
              </span>
              <span className="text-xs text-muted-foreground">
                {selectedProblem.pattern}
              </span>
            </div>
          </div>
          {selectedProblem.url && (
            <a
              href={selectedProblem.url}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-1 text-xs text-muted-foreground hover:text-primary transition-colors"
            >
              <ExternalLink className="h-3 w-3" />
              LeetCode
            </a>
          )}
        </div>

        {/* Topics */}
        {selectedProblem.topics.length > 0 && (
          <div className="flex flex-wrap gap-1 mt-3">
            {selectedProblem.topics.map((topic) => (
              <span
                key={topic}
                className="px-2 py-0.5 text-xs bg-secondary rounded"
              >
                {topic}
              </span>
            ))}
          </div>
        )}

        {/* Complexity */}
        {(selectedProblem.timeComplexity || selectedProblem.spaceComplexity) && (
          <div className="flex gap-4 mt-3 text-xs text-muted-foreground">
            {selectedProblem.timeComplexity && (
              <span>Time: {selectedProblem.timeComplexity}</span>
            )}
            {selectedProblem.spaceComplexity && (
              <span>Space: {selectedProblem.spaceComplexity}</span>
            )}
          </div>
        )}
      </div>

      {/* Collapsible Sections */}
      <div className="flex-1 overflow-auto">
        {/* Problem Definition - Default OPEN */}
        <Collapsible open={definitionOpen} onOpenChange={setDefinitionOpen}>
          <CollapsibleTrigger isOpen={definitionOpen}>
            Problem Definition
          </CollapsibleTrigger>
          <CollapsibleContent>
            <ProblemDefinition content={problemContent.definition} />
          </CollapsibleContent>
        </Collapsible>

        {/* Hints - Default CLOSED */}
        <Collapsible open={hintsOpen} onOpenChange={setHintsOpen}>
          <CollapsibleTrigger isOpen={hintsOpen}>
            Hints ({problemContent.hints.length})
          </CollapsibleTrigger>
          <CollapsibleContent>
            <Hints hints={problemContent.hints} />
          </CollapsibleContent>
        </Collapsible>

        {/* Solution - Default CLOSED */}
        <Collapsible open={solutionOpen} onOpenChange={setSolutionOpen}>
          <CollapsibleTrigger isOpen={solutionOpen}>
            Full Solution
          </CollapsibleTrigger>
          <CollapsibleContent>
            <Solution content={problemContent.solution} />
          </CollapsibleContent>
        </Collapsible>

        {/* Explanation - Default CLOSED */}
        <Collapsible open={explanationOpen} onOpenChange={setExplanationOpen}>
          <CollapsibleTrigger isOpen={explanationOpen}>
            Explanation
          </CollapsibleTrigger>
          <CollapsibleContent>
            <Explanation content={problemContent.explanation} />
          </CollapsibleContent>
        </Collapsible>
      </div>
    </div>
  );
}
