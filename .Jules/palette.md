## 2024-03-24 - Accessibility on Search Clear Icons
**Learning:** Icon-only clear search buttons (using X icon) in ConfigPage, SkillsPage, and SessionsPage lacked aria-labels, making them inaccessible to screen readers.
**Action:** Always ensure any icon-only button, especially common ones like clear search (X) or pagination arrows, has an aria-label using the i18n translation system with a fallback.
