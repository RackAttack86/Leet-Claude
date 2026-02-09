import { useEffect, useRef, useCallback } from "react";
import { writeSolution } from "@/lib/tauri-commands";

interface UseAutoSaveOptions {
  delay?: number;
  onSaveStart?: () => void;
  onSaveComplete?: () => void;
  onSaveError?: (error: string) => void;
}

export function useAutoSave(
  path: string | undefined,
  content: string,
  enabled: boolean,
  options: UseAutoSaveOptions = {}
) {
  const {
    delay = 1500,
    onSaveStart,
    onSaveComplete,
    onSaveError,
  } = options;

  const timeoutRef = useRef<NodeJS.Timeout | null>(null);
  const lastSavedContentRef = useRef<string>("");

  const save = useCallback(async () => {
    if (!path || content === lastSavedContentRef.current) {
      return;
    }

    onSaveStart?.();

    try {
      await writeSolution(path, content);
      lastSavedContentRef.current = content;
      onSaveComplete?.();
    } catch (err) {
      onSaveError?.(String(err));
    }
  }, [path, content, onSaveStart, onSaveComplete, onSaveError]);

  useEffect(() => {
    if (!enabled || !path) {
      return;
    }

    // Clear existing timeout
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }

    // Set new timeout
    timeoutRef.current = setTimeout(save, delay);

    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, [enabled, path, content, delay, save]);

  // Reset last saved content when path changes
  useEffect(() => {
    lastSavedContentRef.current = content;
  }, [path]);

  return { save };
}
