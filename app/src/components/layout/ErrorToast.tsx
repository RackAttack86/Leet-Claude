import { useProblemStore } from "@/store";
import { Toast, ToastContainer } from "@/components/ui";

export function ErrorToast() {
  const error = useProblemStore((state) => state.error);
  const clearError = useProblemStore((state) => state.clearError);

  if (!error) return null;

  return (
    <ToastContainer>
      <Toast message={error} type="error" onClose={clearError} />
    </ToastContainer>
  );
}
