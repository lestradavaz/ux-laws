# Mental Model

## Principle and evidence

People act using an internal account of how a system works. Make the interface's concepts, state, and consequences understandable in the terms relevant to their tasks.

Mental models are a cognitive concept. The catalog recommends aligning system presentation with user expectations, but there is no single universal model for an audience. Developers' architecture and users' understanding often differ; investigate that difference through observation and prediction.

## Observable triggers

- Users cannot predict what saving, deleting, syncing, or publishing will affect.
- The UI exposes backend entities or process names instead of task concepts.
- Different people use the same label to mean different objects or scopes.

## Implementation actions

1. Ask representative users to describe the task and predict important action results. Inspect support evidence and existing workflows rather than inventing a persona's assumptions.
2. Map user concepts to the domain model. Establish vocabulary for objects, scope, lifecycle, ownership, and relationships; hide internal plumbing unless users need it to act.
3. Make uncertain or asynchronous state explicit. Distinguish local draft, saved record, synchronized copy, and live output when those differences affect decisions.
4. Use familiar metaphors only as far as they fit. When the system diverges, explain the boundary at the decision point rather than allowing a misleading metaphor to imply guarantees.
5. Verify predictions after changes. Test recovery and edge states, because a model that works only on the happy path leaves users unable to reason about failure.

## Example

A presentation controller distinguishes Preview from Live output. Editing a slide changes Preview, while Take live explicitly changes the audience display. Status shows which version is currently live and whether a newer draft exists. The vocabulary lets an operator reason about the consequence before activating output.

## Counterexample

The interface uses Save for both local draft persistence and public deployment depending on hidden state. Users learn that Save is safe in one screen and accidentally expose unfinished work in another.

## Limits and conflicts

Alignment does not require implementing a technically false belief. Explain consequential differences and gradually help users build a more accurate understanding. Novices and experts may need different detail levels. Architecture can guide implementation, but its vocabulary must earn a place through user usefulness. Test the actual domain instead of assuming a consumer metaphor fits specialist work.

## Acceptance checks

- Users correctly predict scope and outcome of consequential actions.
- Core objects and lifecycle states have consistent, understandable names.
- Draft, pending, confirmed, and failed states support a coherent account of the system.
- Edge-case explanations help users recover without requiring internal implementation knowledge.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/mental-model/), [Spanish](https://lawsofux.com/es/modelo-mental/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Jakob’s law](jakob-law.md) · [Tesler’s law](teslers-law.md) · [Working memory](working-memory.md) · [Accessibility](../foundations/accessibility.md).

