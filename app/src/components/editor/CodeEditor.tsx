import { useEffect } from "react";
import Editor, { OnMount } from "@monaco-editor/react";
import { useProblemStore, useEditorStore } from "@/store";
import { EditorToolbar } from "./EditorToolbar";

export function CodeEditor() {
  const solutionCode = useProblemStore((state) => state.solutionCode);
  const setSolutionCode = useProblemStore((state) => state.setSolutionCode);
  const setEditorInstance = useEditorStore((state) => state.setEditorInstance);

  const handleEditorChange = (value: string | undefined) => {
    setSolutionCode(value ?? "");
  };

  const handleEditorMount: OnMount = (editor) => {
    setEditorInstance(editor);
  };

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
      </div>
    </div>
  );
}
