import { Panel, PanelGroup, PanelResizeHandle } from "react-resizable-panels";
import { useProblemStore } from "@/store";
import { CodeEditor } from "@/components/editor/CodeEditor";
import { TestRunner } from "@/components/test-runner/TestRunner";

export function RightPanel() {
  const selectedProblem = useProblemStore((state) => state.selectedProblem);

  if (!selectedProblem) {
    return (
      <div className="h-full flex items-center justify-center bg-background">
        <div className="text-center text-muted-foreground">
          <p className="text-lg mb-2">Editor</p>
          <p className="text-sm">Select a problem to start coding</p>
        </div>
      </div>
    );
  }

  return (
    <PanelGroup direction="vertical" className="h-full">
      <Panel defaultSize={70} minSize={30}>
        <CodeEditor />
      </Panel>
      <PanelResizeHandle className="h-1.5 bg-border hover:bg-primary/50 transition-colors" />
      <Panel defaultSize={30} minSize={15}>
        <TestRunner />
      </Panel>
    </PanelGroup>
  );
}
