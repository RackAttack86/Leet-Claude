import { useEffect, Suspense, lazy, useCallback } from "react";
import type { OnMount } from "@monaco-editor/react";
import { useProblemStore, useEditorStore } from "@/store";
import { EditorToolbar } from "./EditorToolbar";
import { shallow } from "zustand/shallow";

// Lazy load Monaco Editor (~6MB) for better initial bundle size
const Editor = lazy(() => import("@monaco-editor/react").then(mod => ({ default: mod.Editor })));

function EditorLoadingFallback() {
  return (
    <div className="h-full flex items-center justify-center bg-[#1e1e1e] text-gray-400">
      <div className="flex flex-col items-center gap-2">
        <div className="w-6 h-6 border-2 border-gray-400 border-t-transparent rounded-full animate-spin" />
        <span>Loading editor...</span>
      </div>
    </div>
  );
}

export function CodeEditor() {
  // Batch store subscriptions to reduce re-renders
  const { solutionCode, setSolutionCode } = useProblemStore(
    (state) => ({ solutionCode: state.solutionCode, setSolutionCode: state.setSolutionCode }),
    shallow
  );
  const setEditorInstance = useEditorStore((state) => state.setEditorInstance);

  const handleEditorChange = useCallback((value: string | undefined) => {
    setSolutionCode(value ?? "");
  }, [setSolutionCode]);

  const handleEditorMount: OnMount = useCallback((editor) => {
    setEditorInstance(editor);
  }, [setEditorInstance]);

  // Cleanup editor instance on unmount
  useEffect(() => {
    return () => {
      setEditorInstance(null);
    };
  }, [setEditorInstance]);

  return (
    <div className="h-full flex flex-col bg-[#1e1e1e]">
      <EditorToolbar />
      <div className="flex-1">
        <Suspense fallback={<EditorLoadingFallback />}>
          <Editor
            height="100%"
            language="python"
            theme="vs-dark"
            value={solutionCode}
            onChange={handleEditorChange}
            onMount={handleEditorMount}
            options={{
              minimap: { enabled: false },
              fontSize: 14,
              lineNumbers: "on",
              automaticLayout: true,
              scrollBeyondLastLine: false,
              wordWrap: "on",
              tabSize: 4,
              insertSpaces: true,
              formatOnPaste: true,
              formatOnType: true,
              renderWhitespace: "selection",
              bracketPairColorization: { enabled: true },
              guides: {
                indentation: true,
                bracketPairs: true,
              },
              padding: { top: 8, bottom: 8 },
            }}
          />
        </Suspense>
      </div>
    </div>
  );
}
