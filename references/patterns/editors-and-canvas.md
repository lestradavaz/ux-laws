# Editors and canvas

Use for text editors, drawing surfaces, node tools, slide composition, timelines, maps, and other direct-manipulation workspaces. First establish the editable object model, selection behavior, operation scope, and persistence contract. Read [desktop](../platforms/desktop.md) or [specialized platforms](../platforms/specialized.md) when the interaction exceeds ordinary document UI.

## Keep interaction modes legible

Separate selected objects, active tool, keyboard focus, viewport, and document state. A selected shape need not own keyboard focus; panning the viewport should not dirty the document. Show an active tool through more than color, and expose what the next gesture will do. Avoid modes whose exit or consequence depends on remembering a hidden key.

```text
document: objects + revision
selection: object identities
interaction: tool + active gesture + focused region
viewport: pan + zoom
history: semantic operations, independent of redraws
```

This is an illustrative separation, not a prescribed framework. Render from state; route an input event to one intended command. A redraw must not duplicate an edit. Commit undoable operations at meaningful task boundaries: moving one shape should not require undoing every intermediate pointer sample. For collaborative editors, inspect the actual conflict and history model rather than assuming local Undo can reverse remote changes.

Capture the pre-gesture order and relevant revision before pointer samples change anything. Prefer a preview separate from committed document state; on release, validate and commit one before/after operation. Cancel discards the preview and leaves document/history unchanged. If the existing renderer mutates order during a gesture, retain the original order for cancellation and Undo; a snapshot captured only after completion cannot reconstruct the prior order. Reconcile intervening edits through the actual revision model rather than restoring a stale snapshot over newer work.

Make selection, zoom level, and snapping understandable. Offer appropriate precision controls when a task needs exact positioning or dimensions; dragging alone is insufficient for that work. Provide non-dragging routes such as Move up/down, destination choice, or numeric properties where applicable. Web WCAG 2.2 Dragging Movements, Level AA, requires an alternative single-pointer operation without dragging unless its essential or user-agent exceptions apply; keyboard alternatives remain separately important. [W3C dragging explanation](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html).

## Support commands across modalities

Expose common actions through named controls or menus as well as shortcuts. Preserve platform text-editing and clipboard behavior. Keep shortcuts contextual so typing in a field does not delete objects or advance slides. For web single-character shortcuts, inspect the criterion's options for disabling, remapping, or limiting activation to focus. [W3C character key shortcuts](https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html).

A web toolbar can reduce repeated Tab stops through an appropriate composite interaction, but then it must implement the associated keyboard model. Do not add `role="toolbar"` to a visual row without checking behavior. [APG toolbar guidance](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/). Canvas objects need meaningful identification and a usable route to essential operations. An accessible object list or property editor can complement spatial editing; confirm that it covers actual tasks, rather than treating its existence as proof of equivalence.

Persistence feedback should distinguish locally changed, saving, saved, failed, and externally changed states. If autosave fails, retain work and provide the supported retry or export route. Display unresolved conflicts before replacing content. See [states and recovery](../foundations/states-and-recovery.md).

## Example and counterexample

A slide editor supports selecting a text box on canvas or through a named object list. Its properties expose coordinates and alignment; Undo reverses one completed move; export reports its own outcome independently of save. Counterexample: dragging is the sole ordering mechanism, Delete removes a shape while a text field has focus, and "Saved" appears whenever the render loop completes.

Related principles: [Fitts's Law](../principles/fitts-law.md), [mental models](../principles/mental-model.md), [Jakob's Law](../principles/jakob-law.md), [working memory](../principles/working-memory.md), and [flow](../principles/flow.md). Efficient expert shortcuts can support flow without eliminating visible, discoverable commands.

## Acceptance checks

- Complete creation, selection, precision edit, reorder, Undo, and save without relying on dragging alone.
- Verify keyboard focus, input capture, command scope, and shortcut behavior while typing, using IME composition, and opening menus.
- Test zoomed views, overlapping objects, pointer cancellation, save failures, and revision conflicts where supported.
- Inspect accessibility semantics and equivalent task routes with the target runtime. Record unsupported operations explicitly.
- Check document changes against expected history entries; viewport-only actions do not create edit operations.

Sources consulted: 2026-10-04. W3C Understanding pages explain web criteria; APG is informative. Native and spatial implementations need their own verified platform contracts.
