import { useCallback, useMemo, useState } from "react";

type SectionState<T extends string> = Record<T, boolean>;

interface UseCollapsibleSectionsReturn<T extends string> {
  sections: SectionState<T>;
  isOpen: (section: T) => boolean;
  toggle: (section: T) => void;
  open: (section: T) => void;
  close: (section: T) => void;
  openAll: () => void;
  closeAll: () => void;
}

export function useCollapsibleSections<T extends string>(
  sectionNames: readonly T[],
  defaultOpen: T[] = []
): UseCollapsibleSectionsReturn<T> {
  const initialState = useMemo(() => {
    const state = {} as SectionState<T>;
    for (const name of sectionNames) {
      state[name] = defaultOpen.includes(name);
    }
    return state;
  }, []); // Only compute once on mount

  const [sections, setSections] = useState<SectionState<T>>(initialState);

  const isOpen = useCallback((section: T) => sections[section], [sections]);

  const toggle = useCallback((section: T) => {
    setSections((prev) => ({ ...prev, [section]: !prev[section] }));
  }, []);

  const open = useCallback((section: T) => {
    setSections((prev) => ({ ...prev, [section]: true }));
  }, []);

  const close = useCallback((section: T) => {
    setSections((prev) => ({ ...prev, [section]: false }));
  }, []);

  const openAll = useCallback(() => {
    setSections((prev) => {
      const next = { ...prev };
      for (const key of Object.keys(next) as T[]) {
        next[key] = true;
      }
      return next;
    });
  }, []);

  const closeAll = useCallback(() => {
    setSections((prev) => {
      const next = { ...prev };
      for (const key of Object.keys(next) as T[]) {
        next[key] = false;
      }
      return next;
    });
  }, []);

  return { sections, isOpen, toggle, open, close, openAll, closeAll };
}
