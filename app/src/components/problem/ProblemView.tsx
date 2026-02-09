import { useState } from "react";
import { ExternalLink } from "lucide-react";
import { useProblemStore } from "@/store";
import { Collapsible, CollapsibleTrigger, CollapsibleContent } from "@/components/ui/Collapsible";
import { ProblemDefinition } from "./ProblemDefinition";
import { Hints } from "./Hints";
import { Solution } from "./Solution";
import { Explanation } from "./Explanation";
import { cn } from "@/lib/utils";

export function ProblemView() {
  const selectedProblem = useProblemStore((state) => state.selectedProblem);
  const problemContent = useProblemStore((state) => state.problemContent);

  // Section open states - definition is open by default
  const [definitionOpen, setDefinitionOpen] = useState(true);
  const [hintsOpen, setHintsOpen] = useState(false);
  const [solutionOpen, setSolutionOpen] = useState(false);
  const [explanationOpen, setExplanationOpen] = useState(false);

  if (!selectedProblem || !problemContent) {
    return null;
  }

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty.toLowerCase()) {
      case "easy":
        return "bg-green-500/20 text-green-500 border-green-500/30";
      case "medium":
        return "bg-yellow-500/20 text-yellow-500 border-yellow-500/30";
      case "hard":
        return "bg-red-500/20 text-red-500 border-red-500/30";
      default:
        return "bg-muted text-muted-foreground";
    }
  };

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
                  getDifficultyColor(selectedProblem.difficulty)
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
