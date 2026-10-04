# Law of Prägnanz

## Principle and evidence

People tend to organize ambiguous visual material into coherent, economical forms. Reduce avoidable ambiguity while preserving distinctions needed for the task.

Prägnanz is a broad Gestalt account of perceptual organization. Its use in UI is a design heuristic. It does not prove that the visually simplest screen is the most usable or that every icon will be interpreted as intended.

## Observable triggers

- An icon or diagram has several plausible interpretations.
- Overlapping shapes, decorative layers, or inconsistent geometry obscure structure.
- A sparse interface requires users to infer hidden controls or state.

## Implementation actions

1. Identify the object, action, and state each visual element must communicate. Remove ornamental features only when they do not carry necessary meaning.
2. Use consistent shapes, alignment, and hierarchy to clarify structure. Pair unfamiliar or consequential symbols with explicit text rather than relying on a designer's interpretation.
3. Separate interactive surfaces from decoration and background. Ensure overlays, shadows, and cropping do not suggest false boundaries or connections.
4. Inspect the view as a whole and in relevant states: selection, disabled, empty, error, and loading. A simplified default view can become ambiguous when states overlap.
5. Evaluate comprehension with realistic tasks. Ask users what a diagram or control means before explaining it, and revise ambiguous cues rather than treating disagreement as a training problem.

## Example

A network configuration diagram uses consistent node shapes and clearly named directed links. Selected nodes have a stable outline, while errors include an icon and label. Decorative background lines are removed so they cannot be mistaken for data connections. A textual relationship view supplies equivalent information.

## Counterexample

A toolbar replaces explicit action names with minimalist abstract glyphs. The screen looks cleaner, but users repeatedly confuse duplicate, split, and detach, and the simplified appearance hides consequential differences.

## Limits and conflicts

Perceptual economy is not functional minimalism. Expert visualization can require rich detail and several encodings. Preserve information that supports interpretation and safety. Pair with mental-model research because a coherent visual form can still describe the wrong system. Simplicity should reduce ambiguity rather than make the user construct missing information.

## Acceptance checks

- Representative users correctly interpret important controls and diagram relationships.
- Visual simplification retains object identity, state, scope, and consequential distinctions.
- Overlapping and exceptional states remain understandable.
- Essential meaning is available beyond appearance alone, including labels or an equivalent structured view.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/law-of-pr%C3%A4gnanz/), [Spanish](https://lawsofux.com/es/ley-de-pr%C3%A4gnanz/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Occam’s razor](occams-razor.md) · [Mental models](mental-model.md) · [Uniform connectedness](uniform-connectedness.md) · [Accessibility](../foundations/accessibility.md).

