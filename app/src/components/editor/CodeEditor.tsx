import Editor from "@monaco-editor/react";
import { useProblemStore } from "@/store";
import { useAutoSave } from "@/hooks";
import { EditorToolbar } from "./EditorToolbar";

export function CodeEditor() {
  const solutionCode = useProblemStore((state) => state.solutionCode);
  const setSolutionCode = useProblemStore((state) => state.setSolutionCode);
  const saveSolution = useProblemStore((state) => state.saveSolution);
  const isDirty = useProblemStore((state) => state.isDirty);

  // Auto-save with debounce using the shared hook
  useAutoSave(saveSolution, isDirty);

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
