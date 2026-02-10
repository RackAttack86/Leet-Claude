import { memo } from "react";
import ReactMarkdown from "react-markdown";

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
      <ReactMarkdown
        components={{
          pre: ({ children }) => (
            <pre className="bg-secondary p-3 rounded-md overflow-x-auto text-xs">
              {children}
            </pre>
          ),
          code: ({ children, className }) => {
            const isInline = !className;
            return isInline ? (
              <code className="bg-secondary px-1 py-0.5 rounded text-xs">
                {children}
              </code>
            ) : (
              <code className="text-xs">{children}</code>
            );
          },
          p: ({ children }) => (
            <p className="mb-3 text-sm leading-relaxed">{children}</p>
          ),
          ul: ({ children }) => (
            <ul className="list-disc list-inside mb-3 text-sm">{children}</ul>
          ),
          ol: ({ children }) => (
            <ol className="list-decimal list-inside mb-3 text-sm">{children}</ol>
          ),
          li: ({ children }) => <li className="mb-1">{children}</li>,
          h1: ({ children }) => (
            <h1 className="text-lg font-bold mb-2">{children}</h1>
          ),
          h2: ({ children }) => (
            <h2 className="text-base font-semibold mb-2">{children}</h2>
          ),
          h3: ({ children }) => (
            <h3 className="text-sm font-semibold mb-2">{children}</h3>
          ),
          strong: ({ children }) => (
            <strong className="font-semibold text-primary">{children}</strong>
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
});
