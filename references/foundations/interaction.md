# Interaction across input modalities

Read when changing controls, navigation, selection, shortcuts, gestures, or focus. Pair with [accessibility](accessibility.md) for numeric baselines and requirement levels; [states and recovery](states-and-recovery.md) for action outcomes; [editors and canvas](../patterns/editors-and-canvas.md) for direct manipulation. [Fitts's Law](../principles/fitts-law.md) informs targeting, and [Jakob's Law](../principles/jakob-law.md) informs familiar interaction conventions. Search terms: pointer, touch, keyboard, switch, gamepad, remote, XR, focus, selection.

## Model intent independently from the input device

Identify the semantic operation first: choose an item, move it, preview content, edit a value, confirm an action, cancel, or undo. Expose one operation through the modalities the product supports. Shared commands should share validation and outcome handling; duplicated event-specific business logic creates inconsistent behavior. Input equivalence means a user can achieve the same meaningful outcome, not that every device performs identical gestures.

Determine actual devices and use context from project evidence. A desktop UI may have a touchscreen; a mobile UI may have an external keyboard, voice control, or switch input. Hardware detection cannot establish a user's abilities or exclude other concurrent devices. Maintain stable content and selection when input mode changes. Use visual affordances that teach capabilities without blocking expert operation.

## Modality decisions

| Modality | Design and implementation check | Typical failure |
|---|---|---|
| Mouse / trackpad / pen | Provide a clear hit region, predictable activation, cancellation before commitment, and discoverable context actions. Distinguish pen drawing from selection when relevant. | Hover is the only route to an action; a context menu has no alternative. |
| Touch | Support coarse aiming, thumb reach, scrolling, and on-screen keyboard changes. Measure the hit area using platform guidance. Provide alternatives to hidden gestures and precision dragging. | Invisible hit areas overlap; an action fires as scrolling starts. |
| Keyboard | Define traversal order, activation, composite navigation, escape behavior, and shortcuts. Keep focus visible and meaningful. | Selection color is mistaken for focus; a rerender loses focus. |
| Switch / scanning / voice | Expose stable names, grouped controls, and actionable semantics. Keep controls in a logical order and avoid time-sensitive discovery. | Repeated “Edit” names cannot identify a row; a scanning user must hit a fleeting toast. |
| Gamepad / remote | Define directional focus, initial focus, edge behavior, back, confirm, and text-entry route. Test held-key repeats and disconnection. | Directional navigation reaches an offscreen item or traps the user in a grid. |
| XR / spatial input | Verify platform selection model, comfortable placement, focus cues, alternative inputs, and motion settings. Test viewing distance, occlusion, posture, and repeated interaction. | A precise pinch is mandatory for a common operation; a status appears outside the current view. |

These are implementation heuristics; platform-specific exceptions and specialized drawing or gameplay should be documented rather than forced into a conventional form interaction.

## Focus, selection, and mode

Keep three concepts separate: focus receives input, selection identifies the current object or set, and mode changes what an action does. A file row may be selected while its rename field owns focus. A canvas tool may remain active while a properties control owns keyboard focus. Explain modes through persistent affordances and offer a clear exit. Do not use focus movement to silently select or execute a destructive action.

For web composites, follow the relevant [APG keyboard pattern](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/): the page's tab sequence and a widget's internal arrow navigation serve different purposes. Choose a coherent pattern that matches semantics, rather than assigning every child a tab stop by default. Native applications should use their platform focus system and conventions. If an item disappears after deletion, move focus to its logical successor, predecessor, or collection control; preserve context instead of dropping focus to an unrelated root.

Prevent shortcuts from hijacking typing, composition, browser, operating-system, or assistive-technology commands. Show available shortcuts through menus or discoverable help. Treat user-configurable shortcuts as a product choice when justified, not a mandatory feature of every application. Test single-key commands against accessibility requirements and avoid activation while text input owns focus.

## Continuous input and action commitment

During dragging, preview the intended result, identify valid destinations, and allow cancellation. On release, validate the current destination and commit through the same operation used by the alternative control. Separate preview state from saved state; repeated intermediate updates should not produce repeated server mutations unless the task explicitly needs continuous control.

For live controls, distinguish values that may update continuously from consequential triggers. A presentation application's brightness slider can preview immediately; “Go live” needs an unambiguous action boundary and visible current output. Do not place stop and start where changing touch posture makes accidental activation likely. Do not delay emergency stop for aesthetic transitions.

Press-and-hold, double-click, swipe, dwell, or shaking can be useful accelerators. They need an equivalent discoverable route when the task or applicable accessibility requirement calls for one. Avoid adding confirmation to every routine reversible action: undo can preserve flow while protecting against errors. For irreversible or expensive operations, name the exact object and consequence before commitment.

## Acceptance scenario

For a reorderable playlist, verify that pointer drag, keyboard “Move up/down,” and touch controls all use the same ordering operation. Canceled drag leaves order unchanged. Moving an item preserves its identity and focus, announces the resulting position appropriately, and does not scroll it out of reach. A controller user can reach move controls and return to the playlist. After a viewport resize or device change, the current selection and order remain understandable.

Evaluate the interaction with realistic task data and the actual build. A simulated pointer test does not verify touch scrolling; dispatching key events does not prove a screen reader recognizes the widget. Record which modalities were exercised and which remain untested. Consult [Android accessibility guidance](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views), [Windows touch guidance](https://learn.microsoft.com/en-us/windows/apps/develop/input/touch-interactions), and [Apple HIG accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) for platform implementation boundaries. Sources consulted 2026-10-04.
