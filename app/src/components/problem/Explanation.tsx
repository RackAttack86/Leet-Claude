import { memo } from "react";
import ReactMarkdown from "react-markdown";
import { markdownComponents } from "./markdownComponents";

interface ExplanationProps {
  content: string;
}

export const Explanation = memo(function Explanation({ content }: ExplanationProps) {
  if (!content) {
    return (
      <p className="text-muted-foreground text-sm">
        No explanation available. Check the README.md file for more details.
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
