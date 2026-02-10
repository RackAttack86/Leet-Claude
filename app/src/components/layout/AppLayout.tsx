import { Panel, PanelGroup, PanelResizeHandle } from "react-resizable-panels";
import { TreeSidebar } from "./TreeSidebar";
import { LeftPanel } from "./LeftPanel";
import { RightPanel } from "./RightPanel";
import { ErrorToast } from "./ErrorToast";

export function AppLayout() {
  return (
    <div className="h-screen flex bg-background">
      {/* Tree sidebar */}
      <TreeSidebar />

      {/* Main content area with resizable panels */}
      <PanelGroup direction="horizontal" className="flex-1">
        <Panel defaultSize={40} minSize={25}>
          <LeftPanel />
        </Panel>
        <PanelResizeHandle className="w-1.5 bg-border hover:bg-primary/50 transition-colors" />
        <Panel defaultSize={60} minSize={30}>
          <RightPanel />
        </Panel>
      </PanelGroup>

      {/* Error notifications */}
      <ErrorToast />
    </div>
  );
}
