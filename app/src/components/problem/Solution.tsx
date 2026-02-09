interface SolutionProps {
  content: string;
}

export function Solution({ content }: SolutionProps) {
  if (!content) {
    return (
      <p className="text-muted-foreground text-sm">
        No solution available.
      </p>
    );
  }

  return (
    <pre className="bg-secondary p-4 rounded-md overflow-x-auto">
      <code className="text-xs font-mono text-foreground whitespace-pre">
        {content}
      </code>
    </pre>
  );
}
