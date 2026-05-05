## 2024-05-18 - Missing clear search accessibility
**Learning:** Found an accessibility issue pattern across multiple search inputs where the 'clear search' (X) button lacked `aria-label` and `title` attributes. Since these were icon-only buttons, they were completely invisible to screen readers and lacked tooltips.
**Action:** When implementing icon-only buttons (like clear buttons or simple toggles), always ensure they have localized `title` and `aria-label` attributes.
