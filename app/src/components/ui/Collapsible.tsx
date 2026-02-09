import * as React from "react";
import * as CollapsiblePrimitive from "@radix-ui/react-collapsible";
import { ChevronRight } from "lucide-react";
import { cn } from "@/lib/utils";

const Collapsible = CollapsiblePrimitive.Root;

const CollapsibleTrigger = React.forwardRef<
  React.ElementRef<typeof CollapsiblePrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof CollapsiblePrimitive.Trigger> & {
    isOpen?: boolean;
  }
>(({ className, children, isOpen, ...props }, ref) => (
  <CollapsiblePrimitive.Trigger
    ref={ref}
    className={cn(
      "flex items-center gap-2 w-full p-3 text-left font-medium hover:bg-accent/50 transition-colors border-b border-border",
      className
    )}
    {...props}
  >
    <ChevronRight
      className={cn(
        "h-4 w-4 shrink-0 transition-transform duration-200",
        isOpen && "rotate-90"
      )}
    />
    {children}
  </CollapsiblePrimitive.Trigger>
));
CollapsibleTrigger.displayName = "CollapsibleTrigger";

const CollapsibleContent = React.forwardRef<
  React.ElementRef<typeof CollapsiblePrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof CollapsiblePrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <CollapsiblePrimitive.Content
    ref={ref}
    className={cn(
      "overflow-hidden data-[state=closed]:animate-collapse-up data-[state=open]:animate-collapse-down",
      className
    )}
    {...props}
  >
    <div className="p-4 border-b border-border">{children}</div>
  </CollapsiblePrimitive.Content>
));
CollapsibleContent.displayName = "CollapsibleContent";

export { Collapsible, CollapsibleTrigger, CollapsibleContent };
