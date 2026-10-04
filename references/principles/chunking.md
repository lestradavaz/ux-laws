# Chunking

## Principle and evidence

Organize information into meaningful units so people can recognize relationships and process a task in manageable parts. A chunk is meaningful to its audience, not merely a box drawn around items.

Chunking is a cognitive concept related to memory research. The catalog applies it to information structure. Neither that application nor the historic memory literature supplies a fixed number of sections, fields, tabs, or cards for every interface.

## Observable triggers

- A long form mixes identity, delivery, payment, and preferences without structure.
- Instructions contain several unrelated actions in one dense paragraph.
- Users scan back and forth to identify which values or controls belong together.

## Implementation actions

1. Group by task, subject, or decision using the vocabulary users already understand. Confirm the grouping against actual workflows and representative content.
2. Give each group a specific heading and keep its labels, hints, errors, and actions together. Prefer semantic sections to repeated anonymous containers.
3. Use an intentional spacing hierarchy: related items are closer than separate groups. Add boundaries when proximity alone becomes ambiguous.
4. Split across steps only when the task benefits from sequencing. Carry essential context and provide a review or back path; keep comparison-heavy material together.
5. Treat formatted identifiers separately from stored values. Support paste and copy without unexpected separators or destructive normalization.

## Example

An equipment registration form groups serial number and model under Equipment, and location and installation date under Installation. Field-level hints remain attached to their input. The summary displays both groups together before submission, allowing a technician to verify the whole record without remembering the previous screen.

## Counterexample

Every field becomes an individual card with a large title. The interface is longer, related values are visually separated, and technicians must scroll repeatedly to compare the model with the serial label.

## Limits and conflicts

A novice's meaningful unit can differ from an expert's. Visual segmentation that improves scanning may harm comparison or keyboard flow when implemented as unnecessary dialogs. Balance with proximity and working memory. Preserve semantic order and readable names when responsive layouts rearrange groups.

## Acceptance checks

- A user can locate a required group using its heading without scanning every field.
- The same relationships remain clear at narrow widths and enlarged text.
- Reading and focus order follow the task; a group boundary does not cause unexpected navigation.
- Splitting the task does not force users to memorize values needed in the next step.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/chunking/), [Spanish](https://lawsofux.com/es/fragmentaci%C3%B3n/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Miller’s law](miller-law.md) · [Proximity](proximity.md) · [Working memory](working-memory.md) · [Accessibility](../foundations/accessibility.md).

