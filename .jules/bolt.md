## 2024-05-18 - React.memo Arrays Ref Equality
**Learning:** Adding React.memo() to a component is useless if one of the props passed to it is generated with an array method like `.split()` during render, as it creates a new reference.
**Action:** When adding React.memo() to a component, check the parent components that use it to ensure they are not passing dynamically created array or object references as props. Wrap dynamically created props in `useMemo` in the parent.
