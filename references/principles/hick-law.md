# Hick’s Law

## Principle and evidence

Choice and interpretation take time. Improve time-sensitive decisions by making alternatives distinct, organized, and relevant to the current task.

The Hick–Hyman relationship originated in controlled choice-reaction work. Applying it to complex navigation is a heuristic, not a formula predicting every interface decision. Familiarity, search, task knowledge, option probability, and label quality affect performance.

## Observable triggers

- Users hesitate among equally emphasized actions.
- A menu mixes unrelated commands with unclear names.
- An operator must interpret a large set of possible actions during urgent work.

## Implementation actions

1. Identify the decision being made and which alternatives are genuinely available in that state. Remove irrelevant actions from the immediate decision while keeping supported capabilities discoverable.
2. Use concrete labels that distinguish outcomes. Organize options by task or domain, with consistent ordering that users can learn.
3. Highlight a primary action only when it is justified by the current workflow. Explain recommended defaults and retain a practical route to alternatives.
4. Provide direct access for known targets through search, shortcuts, or a command palette. Avoid forcing experts through a branching wizard for repeated actions.
5. Measure end-to-end decision and completion time, errors, and backtracking. Compare a grouped menu with a flat searchable list using realistic tasks before choosing depth.

## Example

A live presentation control panel separates preparation commands from actions affecting current output. Start, Pause, and End have distinct labels and state-specific availability. Advanced setup remains searchable elsewhere. An operator can find the safe next action quickly without navigating several levels during a live session.

## Counterexample

A navigation bar is reduced to three vague icons. The smaller option count looks compliant with the law, but users must open each icon to discover its meaning and then retrace their path.

## Limits and conflicts

Fewer choices can increase the number of steps, memory demands, or uncertainty. The law does not imply a universal menu size, nor that every task should become a wizard. Safety may require a deliberate checkpoint even when speed is desirable. Preserve meaningful expert options and distinguish choosing among alternatives from locating an already known item.

## Acceptance checks

- Users understand the outcome of each immediately relevant action.
- Urgent workflows expose the safe next action with stable labels and placement.
- Known-target users have a direct route where the task warrants one.
- Any option reduction improves overall task performance without removing required capability.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/hicks-law/), [Spanish](https://lawsofux.com/es/ley-de-hick/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Choice overload](choice-overload.md) · [Miller’s law](miller-law.md) · [Fitts’s law](fitts-law.md) · [Accessibility](../foundations/accessibility.md).

