import { useEffect, useRef, useCallback } from "react";

interface UseAutoSaveOptions {
  delay?: number;
}

/**
 * Hook for auto-saving content with debounce.
 * @param saveFunction - The function to call to save (e.g., store.saveSolution)
 * @param isDirty - Whether there are unsaved changes
 * @param options - Configuration options
 */
export function useAutoSave(
  saveFunction: () => Promise<void>,
  isDirty: boolean,
  options: UseAutoSaveOptions = {}
) {
  const { delay = 1500 } = options;

  const timeoutRef = useRef<NodeJS.Timeout | null>(null);
  const saveFunctionRef = useRef(saveFunction);

  // Keep save function ref up to date without causing effect re-runs
  saveFunctionRef.current = saveFunction;

  useEffect(() => {
    if (!isDirty) {
      return;
    }

    // Clear existing timeout
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }

    // Set new timeout
    timeoutRef.current = setTimeout(() => {
      saveFunctionRef.current();
    }, delay);

    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, [isDirty, delay]);

  const saveNow = useCallback(() => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    return saveFunctionRef.current();
  }, []);

  return { saveNow };
}
