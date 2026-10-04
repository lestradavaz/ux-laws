# Law of Proximity

## Principle and evidence

Nearby elements tend to be perceived as related. Use spacing to express relationships without forcing users to infer ownership.

Proximity is a perceptual grouping principle. Its interface application depends on layout, language, content, and competing cues. There is no universal spacing scale in the principle; use the project's design system and validate the resulting relationships.

## Observable triggers

- A label appears closer to the wrong field.
- Status, error, or action placement leaves its owning item unclear.
- Responsive wrapping changes which pieces appear grouped.

## Implementation actions

1. List the relationships that must be visible: label–input, hint–input, value–unit, item–action, or heading–section. Keep each related set together in the layout.
2. Establish a spacing hierarchy in which separation between groups exceeds ordinary separation within a group. Use shared layout primitives rather than unrelated margin adjustments.
3. Attach validation messages to their field and keep summaries linked to the affected input. Place instructions before the action they guide, close enough to be encountered in task flow.
4. Use consistent alignment and semantic ordering. Test wrap behavior with long localized labels, missing content, and narrow viewports.
5. Where space cannot make a relationship clear, add an explicit heading, boundary, or connection rather than squeezing content or assuming color will solve ownership.

## Example

A desktop property inspector shows Width with its numeric field and unit on the same row. The hint about aspect ratio stays beside the linked Width and Height controls. At a narrow width, each label precedes its own control and errors remain within that field group, avoiding accidental association with the next property.

## Counterexample

A form uses identical spacing above and below every input. A multiline help message lands halfway between two fields, and people apply its format instructions to the wrong field.

## Limits and conflicts

Grouping through proximity must survive reading order and assistive access; physical distance is unavailable in a linear reading experience. Very tight placement can conflict with target acquisition. Dense tables and canvases may need additional structures because meaningful relations are not always spatially adjacent. RTL layout requires checking the actual relationships, not blindly mirroring margins.

## Acceptance checks

- Labels, units, hints, errors, and actions have unambiguous ownership.
- Grouping remains clear when text wraps or content is absent.
- Supported interaction areas maintain adequate separation while associated content stays coherent.
- Linear reading and keyboard order preserve the same relationships as the visual layout.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/law-of-proximity/), [Spanish](https://lawsofux.com/es/ley-de-proximidad/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Common region](common-region.md) · [Fitts’s law](fitts-law.md) · [Similarity](similarity.md) · [Accessibility](../foundations/accessibility.md).

