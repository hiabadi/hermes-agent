## 2026-06-16 — Shadcn form component id passthrough
**Type:** a11y
**Insight:** Shadcn components like `Switch` and `Select` require explicit prop passthrough of the `id` attribute down to the actual interactive element (e.g. `<button role="switch">`), rather than leaving it on wrapper `div`s, to ensure `<Label htmlFor="id">` properly focuses and toggles the element upon click.
**Where:** `web/src/components/ui/select.tsx`, `web/src/components/ui/switch.tsx`, `web/src/components/AutoField.tsx`
**Action next time:** Ensure when adopting custom interactive components that they accept and correctly apply `id` props to the semantics element that handles the focus state.
