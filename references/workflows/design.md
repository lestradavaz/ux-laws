# Design a usable interaction

Use when the requested result is a new flow, interface specification, or prototype. Inspect constraints and existing domain conventions before choosing presentation. Read the relevant pattern and platform through [the entrypoint](../../SKILL.md).

## Establish the task model

Define the user, goal, starting state, information available, necessary decisions, success state, and cost of failure. Include expertise, frequency, environment, and modalities when they alter behavior. A professional operator under time pressure and an occasional visitor may need different paths to the same result.

Describe the task in domain language before drawing screens. Separate domain invariants from design preferences: a purchase total must be correct; a wizard is one possible presentation. Use known research if supplied. Otherwise label the task model as a hypothesis based on repository evidence and the brief.

Done: the primary journey has an observable success state and its consequential failure/recovery paths are named.

## Choose the smallest useful structure

Map necessary information and actions onto the journey. Group by meaningful relationships; expose enough context to make decisions; put rare detail behind discoverable paths. Do not reduce choices by burying a frequent action or force a wizard solely because a list is long.

Select principles through the [index](../principles/index.md). Each selection must answer an actual design question: Fitts for acquisition of a target; Tesler for ownership of complexity; mental model for predictability. A principle's name alone is not a rationale.

If alternatives materially change the task, compare them by error cost, efficiency, learnability, accessibility, implementation constraints, and user control. Choose one and preserve the rejected alternative only when it explains an important tradeoff. For a routine control, use the established pattern without manufacturing an alternatives report.

Done: layout and interactions have concrete reasons, and the implementer does not have to guess which behavior was selected.

## Specify behavior, not just the happy screenshot

Define entry and exit, state transitions, labels, focus movement, selection, validation, feedback, cancellation, resumption, and completion. Use [states and recovery](../foundations/states-and-recovery.md) for applicable branches. Decide what is visible and actionable during work; distinguish acknowledgment from actual completion.

Example specification for an export control:

```text
ready -> export requested -> preparing -> transferring -> completed
                                  |             |
                                  +-> failed <--+
preparing or transferring -> cancellation requested -> canceled/finished
```

Preserve the selected destination and options after a retryable error. While transferring, expose real progress if measurable; otherwise state that export is running. Show the destination at completion. If cancellation races with completion, display the result the operation actually reached. Whether cancellation is supported depends on the underlying operation, not the desired animation.

Use [accessibility](../foundations/accessibility.md) and [interaction](../foundations/interaction.md) to make the specification operable through required modalities. If the custom-rendered surface lacks semantic support, document that dependency explicitly rather than calling the prototype accessible.

## Accept and hand off

Write observable criteria: given a starting state and input, specify the result and recovery. Include representative normal, boundary, failure, and modality cases. “Feels intuitive” is not an acceptance criterion. Define measurements only when their targets follow from user needs or a known baseline.

A specification is complete when a builder can implement the behavior, a reviewer can exercise the criteria, and unresolved research or platform constraints are visible. A design proposal does not establish usability with real users.

Optional requested deliverables: [brief template](../../assets/templates/ux-brief.md), [decision record](../../assets/templates/decision-record.md), [verification plan](../../assets/templates/verification-plan.md).
