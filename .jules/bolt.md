## 2024-05-14 - React Frontend Search Performance

**Learning:** When performing text searches on long lists of Markdown content (like chat sessions), the `React.memo` boundaries are easily broken if inline arrays/objects or string functions (`toLowerCase`) are run on every render keystroke. This causes heavy markdown parser re-runs on un-targeted messages.

**Action:** Before optimizing complex logic, ensure the prop dependencies flowing into heavy components (like `Markdown.tsx`) are stable by memoizing calculations in the parent (`MessageBubble`), and wrap the heavy components themselves in `React.memo()`. Always verify backend deps aren't accidentally touched.
