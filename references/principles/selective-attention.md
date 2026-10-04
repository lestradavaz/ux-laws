# Selective Attention

## Principle and evidence

People attend to information relevant to their current goal and may miss competing or apparently irrelevant content. Put important signals where the task naturally directs attention.

Selective attention encompasses several psychological accounts and observed phenomena. The catalog highlights banner blindness and change blindness. An individual missed signal can have many causes; test salience, relevance, timing, and accessibility rather than assuming one mechanism.

## Observable triggers

- Users overlook a warning outside their work region.
- Background updates change content without being noticed.
- Many badges, animations, and notifications compete for the same attention.

## Implementation actions

1. Locate the user's focus during the task: selected item, input, pointer target, or live output region. Place related status and consequences near that focus while retaining a persistent record where needed.
2. Rank signals by urgency, consequence, and required response. Give critical information distinct, clear treatment; keep routine updates calm and avoid making every status an alert.
3. Use specific labels and more than color to communicate changes. Preserve stable positions and selection so updates do not make users lose their place.
4. Announce meaningful asynchronous changes through the appropriate platform channel. Batch or summarize high-frequency updates so assistive feedback and visual status remain usable.
5. Check combinations: validation arriving during typing, collaborator edits, background completion, or several alerts. Test whether the necessary signal is noticed without hijacking unrelated work.

## Example

A live operator changes a source while several asset downloads finish in the background. The current output panel clearly shows the selected source and any failure affecting live display. Download completions stay in a status list rather than replacing the operator's focus. A critical output failure remains visible until addressed and includes a clear recovery action.

## Counterexample

A banner-shaped warning above a dense editor says a destructive operation will affect all slides. It resembles a promotion and sits far from the action. The button label itself communicates no scope, so users proceed without noticing the warning.

## Limits and conflicts

More flashing or louder alerts can increase distraction and desensitization. Avoid motion-dependent meaning and provide user control where appropriate. Critical alerts may justify interruption, but the decision must follow consequence and domain requirements. Recognition cannot rely on visual salience alone; reading order and assistive announcements must communicate the same important state.

## Acceptance checks

- Important signals are encountered at the relevant decision point.
- Critical and routine updates have clearly differentiated treatment.
- Concurrent updates preserve active input, focus, selection, and spatial context.
- Meaningful state changes are available through appropriate nonvisual channels without announcement floods.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/selective-attention/), [Spanish](https://lawsofux.com/es/atenci%C3%B3n-selectiva/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Von Restorff](von-restorff-effect.md) · [Flow](flow.md) · [Cognitive load](cognitive-load.md) · [Accessibility](../foundations/accessibility.md).

