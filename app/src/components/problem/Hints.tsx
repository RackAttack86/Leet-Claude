import { Lightbulb } from "lucide-react";

interface HintsProps {
  hints: string[];
}

export function Hints({ hints }: HintsProps) {
  if (hints.length === 0) {
    return (
      <p className="text-muted-foreground text-sm">
        No hints available for this problem.
      </p>
    );
  }

  return (
    <ul className="space-y-3">
      {hints.map((hint, index) => (
        <li key={index} className="flex items-start gap-3">
          <Lightbulb className="h-4 w-4 text-yellow-500 shrink-0 mt-0.5" />
          <span className="text-sm">{hint}</span>
        </li>
      ))}
    </ul>
  );
}
