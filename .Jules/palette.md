## 2024-05-24 - Accessibility for Icon-only Clear Search Buttons
**Learning:** Icon-only buttons used for clearing search inputs across different pages (e.g., SkillsPage, ConfigPage, SessionsPage) were missing both tooltips (`title`) and screen reader labels (`aria-label`).
**Action:** When adding icon-only buttons, especially for repetitive actions like clearing search, ensure they have proper ARIA labels using localized translation keys (e.g., `t.common.clear`) for accessibility and tooltips for better visual feedback.
