import { useEffect, useRef, useCallback } from "react";
import Editor from "@monaco-editor/react";
import { useProblemStore } from "@/store";
import { EditorToolbar } from "./EditorToolbar";

export function CodeEditor() {
  const solutionCode = useProblemStore((state) => state.solutionCode);
  const setSolutionCode = useProblemStore((state) => state.setSolutionCode);
  const saveSolution = useProblemStore((state) => state.saveSolution);
  const isDirty = useProblemStore((state) => state.isDirty);

  const saveTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  // Auto-save with debounce
  const debouncedSave = useCallback(() => {
    if (saveTimeoutRef.current) {
      clearTimeout(saveTimeoutRef.current);
    }
    saveTimeoutRef.current = setTimeout(() => {
      saveSolution();
    }, 1500);
  }, [saveSolution]);

  // Trigger auto-save when code changes
  useEffect(() => {
    if (isDirty) {
      debouncedSave();
    }
    return () => {
      if (saveTimeoutRef.current) {
        clearTimeout(saveTimeoutRef.current);
      }
    };
  }, [isDirty, solutionCode, debouncedSave]);

  const handleEditorChange = (value: string | undefined) => {
    setSolutionCode(value ?? "");
  };

  return (
    <div className="h-full flex flex-col bg-[#1e1e1e]">
      <EditorToolbar />
      <div className="flex-1">
        <Editor
          height="100%"
          language="python"
          theme="vs-dark"
          value={solutionCode}
          onChange={handleEditorChange}
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
      </div>
    </div>
  );
}
