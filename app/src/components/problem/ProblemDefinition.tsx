import { memo } from "react";
import ReactMarkdown from "react-markdown";
import { markdownComponents } from "./markdownComponents";

interface ProblemDefinitionProps {
  content: string;
}

export const ProblemDefinition = memo(function ProblemDefinition({ content }: ProblemDefinitionProps) {
  if (!content) {
    return (
      <p className="text-muted-foreground text-sm">
        No problem definition available.
      </p>
    );
  }

  return (
    <div className="prose prose-sm prose-invert max-w-none">
      <ReactMarkdown components={markdownComponents}>
        {content}
      </ReactMarkdown>
    </div>
  );
});
