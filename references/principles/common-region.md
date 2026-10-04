# Law of Common Region

## Principle and evidence

A visible boundary or shared surface can make elements appear to belong together. Use containers to communicate true scope and relationship.

Common region is a perceptual grouping principle. Its interface application is a recommendation about visual organization, not a mandate to place every group inside a card. Actual interpretation depends on surrounding cues and content.

## Observable triggers

- Users are unsure which controls modify a particular item or section.
- A page contains several independent records with similar actions.
- An error or status appears visually associated with the wrong group.

## Implementation actions

1. Identify which elements share an object, decision, or scope. Place only those elements inside the same visual region and give the region a specific heading.
2. Make group boundaries legible through appropriate spacing, background, border, or elevation without adding unnecessary visual layers.
3. Keep group-specific actions and status inside or clearly attached to their region. Put page-level actions outside item regions and label their broader scope.
4. Pair the visual grouping with semantic structure and names. On the web, use appropriate headings, fieldsets, sections, or landmarks according to content; in native UI, expose corresponding grouping through the platform.
5. Check nesting, narrow widths, enlarged text, and empty/error states. A missing value or wrapped button must not blur which group owns the interaction.

## Example

An account page separates Billing address from Delivery address. Each region includes its own Edit action and status. A page-wide Save all changes action names its broader scope and sits outside both regions. Assistive navigation exposes the group headings rather than only a sequence of anonymous text boxes.

## Counterexample

A large decorative card wraps three unrelated settings panels and one destructive account action. Its boundary implies that the action belongs to the currently edited settings even though it affects the whole account.

## Limits and conflicts

Containers add visual weight and consume space. Dense professional tables may communicate relationships more effectively with alignment and headers. Shared region can conflict with proximity or similarity, so inspect the combined interpretation. A border alone creates no meaningful accessible group and does not explain scope to users who cannot see it.

## Acceptance checks

- Users can identify which object each action and status affects.
- Visual regions match semantic grouping and reading order.
- Responsive and enlarged layouts preserve ownership of labels, errors, and controls.
- Every prominent container communicates a useful relationship rather than decoration alone.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/law-of-common-region/), [Spanish](https://lawsofux.com/es/ley-de-regi%C3%B3n-com%C3%BAn/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Proximity](proximity.md) · [Uniform connectedness](uniform-connectedness.md) · [Chunking](chunking.md) · [Accessibility](../foundations/accessibility.md).

