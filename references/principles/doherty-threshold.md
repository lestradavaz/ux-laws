# Doherty Threshold

## Principle and evidence

Responsive feedback helps people maintain a productive interaction rhythm. Separate acknowledgment of an action from completion of the underlying work.

The catalog's historical response-time threshold describes a particular research framing, not a universal service-level target. Modern tasks vary: dragging, typing, remote submissions, and background exports need different budgets. Establish budgets from the interaction and measure them on representative devices.

## Observable triggers

- A control seems inactive, so users click repeatedly.
- Typing, dragging, or preview updates stall behind background work.
- Loading indicators disappear without a clear success, failure, or partial result.

## Implementation actions

1. Measure input-to-visible-feedback, completion time, and responsiveness during work separately. Investigate slow tails and poor devices, not just average server duration.
2. Acknowledge accepted input promptly with a meaningful pressed, pending, or preview state. Keep the event loop and rendering responsive; offload costly work when supported by the platform.
3. Use progress only when it corresponds to known work. Show phases or an indeterminate status when the denominator is unknown; distinguish queued, processing, saving, and completed.
4. Use optimistic updates only for reversible operations with a defined rollback or conflict path. Preserve user input and identify the failed item if the server rejects it.
5. Provide cancellation, retry, and safe duplicate handling where applicable. Return the real result as soon as it is ready; do not add delay to create an impression of importance.

## Example

A large presentation export immediately shows Export queued, then Rendering slides with the completed slide count, then Saving file. The editor remains usable. Cancellation communicates whether the job was actually stopped, and completion supplies the file location. A fast export goes straight to completion without waiting for an animation to finish.

## Counterexample

A spinner always runs for several seconds to make an analysis feel thorough. Its progress reaches completion before the request returns, and the UI claims success even when saving subsequently fails.

## Limits and conflicts

Feedback cannot substitute for completing work quickly. Avoid decorative motion that delays interaction or causes discomfort. Instant apparent success is unsafe for uncertain consequential operations. Screen-reader announcements must convey meaningful changes without flooding users with every progress tick. Validate timing targets against real usage rather than adopting the catalog number as a blanket requirement.

## Acceptance checks

- Repeated activation cannot create unintended duplicate work.
- Slow, failed, canceled, offline, and out-of-order responses leave understandable states.
- Displayed progress reflects actual known work and completion reflects confirmed outcome.
- Users receive the result immediately when available and can continue supported work during processing.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/doherty-threshold/), [Spanish](https://lawsofux.com/es/umbral-de-doherty/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Flow](flow.md) · [Goal gradient](goal-gradient-effect.md) · [Selective attention](selective-attention.md) · [Accessibility](../foundations/accessibility.md).

