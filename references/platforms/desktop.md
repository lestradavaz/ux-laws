# Desktop and professional applications

Use for installed desktop software, multi-window tools, keyboard-heavy applications, and professional workspaces. Inspect the supported operating systems, UI toolkit/version, integration layer, window model, document lifecycle, and current conventions. Read [interaction](../foundations/interaction.md), [editors and canvas](../patterns/editors-and-canvas.md), or [live operations](../patterns/live-and-critical-operations.md) when relevant.

## Preserve efficient work

Support recurring tasks through visible commands plus discoverable shortcuts. Distinguish focus navigation from command acceleration; a shortcut list does not make inaccessible controls keyboard operable. Keep platform text editing, clipboard, Undo, and menu conventions coherent. Windows guidance emphasizes predictable focus navigation, context-sensitive keyboard behavior, and shortcuts for frequently used commands. Those recommendations describe Windows patterns; inspect the corresponding conventions for other operating systems. [Windows keyboard interactions](https://learn.microsoft.com/en-us/windows/apps/develop/input/keyboard-interactions).

Make focus, selection, active document, and active window distinct. A selected row should not implicitly own every global command. Route destructive commands to the intended document or object, and avoid processing the same keystroke through multiple handlers. Text entry, IME composition, menus, and dialogs need explicit precedence appropriate to the toolkit. Explain commands that act on all documents or remote targets.

Preserve professional density when it supports actual work: side-by-side comparisons, persistent status, sortable tables, compact toolbars, and resizable panes may reduce memory and navigation burden. [Cognitive load](../principles/cognitive-load.md) is not synonymous with low information density. Improve grouping, hierarchy, labels, and irrelevant interruptions before hiding expert tools. [Flow](../principles/flow.md) supports efficient continuity; [Jakob's Law](../principles/jakob-law.md) supports familiar platform behavior.

## Handle windows, files, and state

Show dirty, saving, saved, read-only, and failed states according to the actual persistence model. Distinguish saving a document from exporting an artifact. Do not treat writing to a temporary buffer as a durable save. Inspect existing autosave and recovery behavior before adding storage or prompts. Use [states and recovery](../foundations/states-and-recovery.md) for unknown outcomes and interruptions.

Test resizing, display scaling, monitor changes, and window restoration. Ensure an essential dialog cannot reopen permanently offscreen after a monitor disappears. Resize or scroll controls without silently dropping functionality. Multi-window tools should identify document and output ownership so a command in one window does not unexpectedly affect another.

Accessibility depends on more than native-looking visuals. Windows accessibility guidance describes UI Automation support and the properties exposed by framework controls; custom controls require additional work. [Windows accessibility overview](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview). For each toolkit and integration, inspect the current bridge to the operating system's accessibility API, names/states, focus, and supported actions. Validate in the actual shipped runtime and record gaps.

WCAG2ICT provides informative guidance for adapting WCAG concepts to non-web software; it is not itself a separate native-software conformance standard. Use the applicable product requirements and platform guidance alongside it. [WCAG2ICT](https://www.w3.org/TR/wcag2ict/). Keep normative web units and platform recommendations separate through [accessibility](../foundations/accessibility.md).

## Rust/egui example and counterexample

A Rust/egui presenter keeps preparation state, output commands, and acknowledgment outside frame drawing. A render reads state and emits an intentional action once. Text input owns typing, while a verified contextual shortcut issues Take only in the correct context. Preview and Live labels persist, and actual output is observed during runtime verification. Counterexample: every redraw resends the selected slide, the Space key advances output while entering a title, and the local preview is assumed to prove audience display.

This example prescribes no egui API and promises no automatic screen-reader support. Inspect the installed version and integration. Its detailed behavioral checks live in [live operations](../patterns/live-and-critical-operations.md).

## Acceptance checks

- Complete affected recurring tasks with keyboard only and through named controls.
- Verify input precedence, focus/selection distinction, shortcuts, Undo scope, and dialog exit/return.
- Test save failure, unsaved close, read-only content, resizing, scale changes, and monitor loss where relevant.
- Inspect and exercise the accessibility tree with target operating-system tools and assistive technology.
- Evaluate expert task time and error recovery, preserving established conventions unless evidence supports change.

Sources consulted: 2026-10-04. Microsoft guidance is platform-specific; WCAG2ICT is informative. Report verification scope rather than a blanket native accessibility claim.
