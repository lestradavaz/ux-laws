# Goal-Gradient Effect

## Principle and evidence

Perceived proximity to a meaningful goal can influence motivation. Make actual progress and remaining work understandable so users can decide whether to continue.

The catalog describes a motivational effect and examples of endowed progress. Its application depends on the goal and context. Treat any expected completion improvement as a hypothesis; progress visibility is a design recommendation, not a guarantee of faster or better work.

## Observable triggers

- Users cannot tell how much remains in a multi-step process.
- A progress indicator changes its denominator unexpectedly.
- The interface declares an almost-finished task while important mandatory work remains.

## Implementation actions

1. Define the goal from the user's perspective and distinguish required, optional, and already completed work. Reveal material effort or prerequisites before the user commits.
2. Represent progress using truthful units: completed steps, processed items, or known phases. If duration is variable, name the phase instead of inventing a precise percentage.
3. When prefilled data counts as completed work, label it honestly and allow verification. Explain conditional steps when they arise; do not conceal them to create apparent momentum.
4. Preserve completion when returning or recovering. Explain why a step needs correction rather than silently reducing progress or resetting the whole task.
5. Provide pause, back, and exit routes appropriate to the task. Celebrate useful completion proportionally and avoid guilt, manufactured urgency, or pressure to perform optional actions.

## Example

A workspace setup checklist shows Organization details complete because verified account information is already available. Invite teammates is optional and excluded from the required completion count. A conditional security check appears with an explanation before final activation. The user can save the draft and return to the remaining required work.

## Counterexample

A setup bar starts near completion even though the user has supplied nothing. After each action it introduces another hidden requirement. The reassuring graphic increases continuation while making the actual commitment harder to assess.

## Limits and conflicts

Step count is not elapsed-time progress when steps have different costs. A task can be complete for the user even when optional product adoption goals remain. Balance motivation with honest state and user control. Avoid applying the effect to encourage unsafe spending, compulsive engagement, or consent obtained through misleading completion framing.

## Acceptance checks

- Progress has a defensible denominator or is explicitly indeterminate.
- Users can describe what remains and distinguish optional work.
- Returning after interruption preserves verified completion and exposes corrections.
- Completion means the promised user outcome is achieved, not merely that an animation finished.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/goal-gradient-effect/), [Spanish](https://lawsofux.com/es/efecto-de-tendencia-a-la-meta/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Doherty threshold](doherty-threshold.md) · [Zeigarnik effect](zeigarnik-effect.md) · [Peak–end rule](peak-end-rule.md) · [Accessibility](../foundations/accessibility.md).

