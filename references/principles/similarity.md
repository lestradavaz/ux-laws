# Law of Similarity

## Principle and evidence

Elements that share visual traits can appear related or equivalent. Use consistent appearance for consistent roles and deliberate differentiation for meaningful differences.

Similarity is a perceptual grouping principle. Shape, size, orientation, color, and other traits can contribute, but the resulting interpretation depends on context. Shared styling alone does not establish semantic equivalence or accessibility.

## Observable triggers

- A link looks like ordinary text or decoration looks actionable.
- Different control types share an identical appearance but behave differently.
- Equivalent statuses or actions receive inconsistent styles across the product.

## Implementation actions

1. Inventory styles by role and state, not by screen. Reuse the project's tokens and components for the same behavior; define variants only for an intentional difference.
2. Make interaction affordances recognizable. Links, buttons, selected items, focus, and disabled controls should expose their role and state through more than an unexplained color.
3. Reserve status encodings for stable meanings. Pair colors with text or symbols when state carries information, and keep those meanings consistent in legends and detailed views.
4. Distinguish consequential actions without making every control visually loud. Differences should help users understand role, priority, or risk rather than reflect arbitrary component authorship.
5. Test mixed views with realistic content and all relevant states. Check that a reused style does not falsely imply identical scope, permissions, or results.

## Example

A monitoring app uses the same warning icon, label treatment, and meaning in its overview, detail panel, and alert log. Acknowledge and Resolve differ in name and appearance because acknowledgment does not fix the underlying condition. The app keeps both discoverable without implying that they have the same effect.

## Counterexample

A promotional badge uses the same filled shape as primary buttons, but it is not interactive. Meanwhile, an actual text link has no recognizable interaction cue. Users click the badge and miss the navigation.

## Limits and conflicts

Similarity can be overridden by proximity, region, and learned conventions. Differentiation must be available to users with different sensory capabilities; color-only meaning is insufficient. A design system does not guarantee consistency if the same component is assigned different roles. Validate semantics and behavior as well as screenshots.

## Acceptance checks

- Equivalent roles and statuses use consistent names, encodings, and behavior.
- Interactive elements are distinguishable from noninteractive content.
- Selection, focus, disabled, pending, and error states remain identifiable.
- Any visual difference corresponds to a documented, useful role or state distinction.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/law-of-similarity/), [Spanish](https://lawsofux.com/es/ley-de-la-semejanza/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Von Restorff](von-restorff-effect.md) · [Proximity](proximity.md) · [Jakob’s law](jakob-law.md) · [Accessibility](../foundations/accessibility.md).

