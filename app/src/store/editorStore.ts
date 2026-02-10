import { create } from "zustand";
import type { editor } from "monaco-editor";

type MonacoEditor = editor.IStandaloneCodeEditor;

interface EditorState {
  // Editor instance
  editorInstance: MonacoEditor | null;

  // Actions
  setEditorInstance: (editor: MonacoEditor | null) => void;
  focus: () => void;
  goToLine: (line: number, column?: number) => void;
  getCursorPosition: () => { line: number; column: number } | null;
  setCursorPosition: (line: number, column: number) => void;
  getSelectedText: () => string | null;
  insertText: (text: string) => void;
}

export const useEditorStore = create<EditorState>((set, get) => ({
  editorInstance: null,

  setEditorInstance: (editor) => {
    set({ editorInstance: editor });
  },

  focus: () => {
    const { editorInstance } = get();
    editorInstance?.focus();
  },

  goToLine: (line, column = 1) => {
    const { editorInstance } = get();
    if (!editorInstance) return;

    editorInstance.setPosition({ lineNumber: line, column });
    editorInstance.revealLineInCenter(line);
    editorInstance.focus();
  },

  getCursorPosition: () => {
    const { editorInstance } = get();
    if (!editorInstance) return null;

    const position = editorInstance.getPosition();
    if (!position) return null;

    return { line: position.lineNumber, column: position.column };
  },

  setCursorPosition: (line, column) => {
    const { editorInstance } = get();
    if (!editorInstance) return;

    editorInstance.setPosition({ lineNumber: line, column });
    editorInstance.focus();
  },

  getSelectedText: () => {
    const { editorInstance } = get();
    if (!editorInstance) return null;

    const selection = editorInstance.getSelection();
    if (!selection) return null;

    return editorInstance.getModel()?.getValueInRange(selection) ?? null;
  },

  insertText: (text) => {
    const { editorInstance } = get();
    if (!editorInstance) return;

    const selection = editorInstance.getSelection();
    if (!selection) return;

    editorInstance.executeEdits("insert", [
      {
        range: selection,
        text,
        forceMoveMarkers: true,
      },
    ]);
    editorInstance.focus();
  },
}));
