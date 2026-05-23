## 2026-05-23 - Added keyboard focus styles to base Button component
**Learning:** The base UI component library (shadcn/ui-like) lacked global keyboard focus indications on its primary button component, making navigation unclear for keyboard-only users. Applying `focus-visible:ring-1` globally to the `cva` buttonVariants resolved this universally.
**Action:** Always check the root base components (e.g., button, input, select) for accessible focus states when adopting new UI libraries, as they often require manual configuration for accessibility.
