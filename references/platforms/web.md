# Web interfaces

Use for websites, browser applications, embedded web views, and web portions of hybrid products. Inspect the current rendering framework, router, component library, accessibility behavior, and supported browsers before prescribing changes. Read [accessibility](../foundations/accessibility.md) for exact levels, units, exceptions, and the difference between normative criteria and implementation guidance.

## Use browser contracts deliberately

Prefer native semantic controls when they fit the task. Links navigate; buttons act; form controls expose names and values. HTML semantics provide behavior that must otherwise be implemented and tested. ARIA can describe a custom widget but does not add its keyboard interaction. APG emphasizes that adding a role creates obligations to implement expected behavior and that inappropriate ARIA can damage accessibility. [APG read-me-first guidance](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/).

Inspect existing components before building replacements. A library's accessibility claim is not evidence for the configured application. Check rendered markup, names, states, focus, and target assistive technology. Use the specific APG pattern when implementing custom composites; do not copy a menu, grid, or tab role because the layout resembles one visually.

Respect browser capabilities: Back/Forward, opening links in another tab, text selection, zoom, find, autofill, and standard text editing. Preserve real link destinations. Avoid intercepting every key globally or turning a clickable container into a destination with no native link. For client-side navigation, manage page title, location, and focus intentionally; neither scrolling to the top nor focusing every render constitutes a complete route-transition policy. Test the actual router behavior, including direct entry and history navigation.

## Adapt layout without changing task meaning

Use content-driven layout and responsive behavior appropriate to the task. Allow text enlargement and reflow while preserving usable controls and reading order. Data tables, maps, and other intrinsically two-dimensional content need examination under the applicable criterion rather than a blanket prohibition on horizontal scrolling. WCAG 2.2 defines web success criteria and conformance requirements; a responsive screenshot does not establish conformance. [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

Do not let visual rearrangement silently change reading or keyboard order. Sticky headers and overlays must not obscure focused controls or essential information. Check long localized strings, user text-size settings, browser zoom, narrow windows, orientation, and on-screen keyboards. Hover interactions need reachable keyboard and touch behavior where they convey essential information.

Separate view state from network state. A framework rerender should not resubmit data, restart a consequential action, or move focus out of an active field. For asynchronous content, preserve query identity, disclose loading and stale data, and verify actual outcomes. Use [feedback and asynchronous work](../patterns/feedback-and-async.md) and [navigation and search](../patterns/navigation-and-search.md).

## Example and counterexample

A product settings page uses labeled native controls, keeps draft edits during a recoverable save failure, and returns focus coherently after closing a confirmation dialog. Its compact layout wraps descriptions without hiding them. Counterexample: a styled `div` serves as a button, keyboard focus disappears behind a fixed footer, and every route change replaces the browser history entry so Back cannot restore a search.

Relevant principles: [Jakob's Law](../principles/jakob-law.md), [Fitts's Law](../principles/fitts-law.md), [mental models](../principles/mental-model.md), [Hick's Law](../principles/hick-law.md), and [cognitive load](../principles/cognitive-load.md). Preserve familiar browser and product conventions unless task evidence supports a departure.

## Acceptance checks

- Complete the affected task with pointer, keyboard, and a representative browser/assistive-technology pairing.
- Verify links, focus order, widget roles/states, dialog escape/return behavior, and route transitions where changed.
- Check layout under text expansion, zoom, reduced motion, and applicable narrow/reflow conditions from the foundation.
- Exercise direct URL entry, reload, Back/Forward, slow responses, and failure for relevant paths.
- Run existing automated checks and inspect the changed behavior manually. Report checked scope and outstanding issues; do not infer whole-site conformance from a component pass.

Sources consulted: 2026-10-04. APG is informative implementation guidance; WCAG's normative text controls criterion interpretation. Preserve the project's established support matrix and change only the requested UI scope.
