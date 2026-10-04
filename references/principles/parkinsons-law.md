# Parkinson’s Law

## Principle and evidence

Open-ended tasks and unnecessary process can expand effort. Give work a clear purpose, completion condition, and efficient path while respecting the user's pace.

Parkinson's law began as a satirical organizational observation, not a controlled UI-performance model. Its interface use is a heuristic for preventing needless task expansion. It does not justify imposing arbitrary time limits or pressuring people to finish faster.

## Observable triggers

- A simple task includes excessive setup or optional decisions.
- Users cannot tell when they have done enough.
- Repeated manual entry or unnecessary confirmation adds effort without improving outcome.

## Implementation actions

1. Define the minimum sufficient user outcome and distinguish its required steps from optional enrichment. Explain when the task is complete.
2. Remove redundant collection and repeated input. Offer reliable autofill or reuse with clear provenance and a correction path rather than silently assuming old data is current.
3. Provide useful defaults when the effect is understood and reversible. Leave consequential or ambiguous decisions to the user with enough information to decide.
4. Measure real completion and correction time across relevant abilities and contexts. Compare gains from reduced work rather than celebrating a countdown-driven speed increase.
5. For genuine expiry or resource constraints, explain the reason, preserve work where possible, and apply the relevant accessibility guidance. Use user-controlled reminders or estimates instead of fabricated urgency.

## Example

An event registration asks only for attendance details required to reserve a place. Optional profile enrichment is offered after confirmation. Known contact information is visible for verification, and the user can save and resume. The process ends with a clear reservation result rather than another mandatory promotional step.

## Counterexample

A form shows a short countdown to force decisions, despite no actual capacity or security constraint. Slower readers lose entered information and must restart, so apparent urgency increases workload and exclusion.

## Limits and conflicts

Some tasks need deliberate review, deliberation, or mandatory steps. The objective is sufficient effort with control, not minimum duration at any cost. Defaults can introduce bias or stale-data errors. A simpler path must retain informed decisions and safe recovery. Do not infer organizational theory from one usability session.

## Acceptance checks

- The required outcome and completion condition are explicit.
- Optional work can be deferred without blocking the promised result.
- Reused or default data can be inspected and corrected.
- Any enforced time constraint has a real basis and appropriate warning, extension, or recovery.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/parkinsons-law/), [Spanish](https://lawsofux.com/es/ley-de-parkinson/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Goal gradient](goal-gradient-effect.md) · [Cognitive bias](cognitive-bias.md) · [Occam’s razor](occams-razor.md) · [Accessibility](../foundations/accessibility.md).

