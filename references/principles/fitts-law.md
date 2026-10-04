# Fitts’s Law

## Principle and evidence

Acquiring a pointing target becomes harder when it is smaller or farther away. Design the actual interactive area and travel path for the input modality and task.

Fitts's law is a motor-performance model with task-dependent parameters. It supports examining target size and distance, but it does not prescribe one button size for all devices. Keyboard, switch, voice, touch, pointer, stylus, and spatial input require their own interaction analysis.

## Observable triggers

- Small icons are frequently missed or the adjacent destructive action is activated.
- A repeated action requires long pointer or thumb travel.
- Drag handles, resize edges, or transient menus are difficult to acquire.

## Implementation actions

1. Inspect hit areas rather than icon artwork alone. Give actionable rows, labels, and controls sufficient interactive space without overlapping neighboring targets.
2. Place related actions near their object or the normal work region. Keep high-frequency controls stable; avoid moving a target as the pointer approaches.
3. Separate conflicting actions, especially irreversible ones, with clear names and deliberate activation. Provide undo or confirmation proportional to consequence rather than enlarging a dangerous control indiscriminately.
4. Provide alternative operation for dragging and fine pointing where applicable. Preserve visible focus and meaningful control names for keyboard or assistive navigation.
5. Use the applicable platform and accessibility target guidance from the foundation reference, preserving its units and exceptions. Validate real touch reach and pointer acquisition on supported layouts.

## Example

A mobile media list initially uses tiny play icons beside delete icons. Make each play button's hit area larger, move deletion into a clearly labeled item menu, and offer an accessible alternative to swipe actions. On desktop, keep selection and playback distinct so clicking an item does not unexpectedly start output.

## Counterexample

Expanding every icon's invisible hit area makes neighboring controls overlap. A tap visually centered on one control triggers the other, while the design review incorrectly judges success from the artwork dimensions.

## Limits and conflicts

Screen edges can help pointer acquisition only when the actual target reaches the relevant boundary and the environment supports that behavior. Touch reach, occlusion, zoom, and motor ability change the problem. Bigger targets can increase scrolling and travel; balance density using measured workflow needs. Minimum conformance alone does not prove comfortable operation.

## Acceptance checks

- All relevant controls can be acquired reliably with supported modalities.
- Interactive bounds do not overlap or differ misleadingly from visible affordances.
- Repeated actions remain stable and reachable across responsive and zoomed layouts.
- Dragging and precise pointing have usable alternatives where required; adjacent errors have been checked.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/fittss-law/), [Spanish](https://lawsofux.com/es/ley-de-fitts/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Proximity](proximity.md) · [Hick’s law](hick-law.md) · [Jakob’s law](jakob-law.md) · [Accessibility](../foundations/accessibility.md).

