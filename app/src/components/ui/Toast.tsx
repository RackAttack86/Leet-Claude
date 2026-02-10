import { useEffect } from "react";
import { X, AlertCircle, CheckCircle, Info } from "lucide-react";
import { cn } from "@/lib/utils";

export type ToastType = "error" | "success" | "info";

interface ToastProps {
  message: string;
  type?: ToastType;
  onClose: () => void;
  duration?: number;
}

export function Toast({ message, type = "error", onClose, duration = 5000 }: ToastProps) {
  useEffect(() => {
    if (duration > 0) {
      const timer = setTimeout(onClose, duration);
      return () => clearTimeout(timer);
    }
  }, [duration, onClose]);

  const icons = {
    error: <AlertCircle className="h-4 w-4" />,
    success: <CheckCircle className="h-4 w-4" />,
    info: <Info className="h-4 w-4" />,
  };

  const styles = {
    error: "bg-red-950 border-red-800 text-red-200",
    success: "bg-green-950 border-green-800 text-green-200",
    info: "bg-blue-950 border-blue-800 text-blue-200",
  };

  return (
    <div
      className={cn(
        "flex items-start gap-3 p-4 rounded-lg border shadow-lg max-w-md animate-in slide-in-from-right-full duration-300",
        styles[type]
      )}
      role="alert"
    >
      <span className="shrink-0 mt-0.5">{icons[type]}</span>
      <p className="text-sm flex-1 break-words">{message}</p>
      <button
        onClick={onClose}
        className="shrink-0 p-1 hover:bg-white/10 rounded transition-colors"
        aria-label="Dismiss"
      >
        <X className="h-4 w-4" />
      </button>
    </div>
  );
}

interface ToastContainerProps {
  children: React.ReactNode;
}

export function ToastContainer({ children }: ToastContainerProps) {
  return (
    <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2">
      {children}
    </div>
  );
}
