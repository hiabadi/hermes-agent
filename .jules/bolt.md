## 2024-06-26 — Memoize SidebarNavLink to fix 10s polling render tax
**Where:** `web/src/App.tsx` (`SidebarNavLink`)
**Symptom:** ~17 components (the entire navigation list) in the app sidebar re-rendering every 10 seconds and on every route change.
**Root cause:** `App.tsx` calls `useSidebarStatus()`, which polls the backend every 10s. The status update causes `App.tsx` to re-render. Since `SidebarNavLink` was un-memoized and mapped inline, React forcefully re-rendered all 17 instances despite their props (`item`, `t`, `closeMobile`, etc.) being referentially stable. This also affected every `useLocation` route change.
**Resolution:** fixed. Wrapped `SidebarNavLink` in `React.memo()`. As the props passed down were already referentially stable, this prevented the 17+ re-renders from executing the component tree on each tick.
**Next time:** Look for expensive un-memoized lists inside app shells or providers that re-render periodically due to polling hooks or global state context changes.
