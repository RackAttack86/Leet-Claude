import { create } from "zustand";
import type { TestRunResult } from "@/types";
import { runTests } from "@/lib/tauri-commands";

interface TestState {
  isRunning: boolean;
  results: TestRunResult | null;
  error: string | null;

  runTests: (problemPath: string, code: string) => Promise<void>;
  clearResults: () => void;
}

export const useTestStore = create<TestState>((set) => ({
  isRunning: false,
  results: null,
  error: null,

  runTests: async (problemPath: string, code: string) => {
    set({ isRunning: true, results: null, error: null });
    try {
      const results = await runTests(problemPath, code);
      set({ results, isRunning: false });
    } catch (err) {
      set({ isRunning: false, error: String(err) });
    }
  },

  clearResults: () => {
    set({ results: null, error: null });
  },
}));
