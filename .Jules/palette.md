## 2024-05-14 - Keyboard Accessibility Standard
**Learning:** This codebase uses standard tailwind `focus-visible` utilities across inputs and select dropdowns, but the base `Button` component was missing them. The standard focus ring pattern for dark mode here is `focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-foreground/30`.
**Action:** When creating or modifying interactive components, consistently apply this standard `focus-visible` pattern to ensure keyboard navigation visibility is maintained without breaking mouse click aesthetics.
