# Implement a scoped UX improvement

Use for features, fixes, or refinements in an existing interface. Start from the requested task, not from a desire to apply every principle. Route to relevant patterns and platforms using [the entrypoint](../../SKILL.md).

## Ground the change

Inspect the actual component, state ownership, async operations, error handling, available semantic controls, existing conventions, and verification tools. Trace the affected journey into adjacent states that can change the outcome. Backend invariants and authorization still govern visible behavior.

Identify the observed problem, its user consequence, and the smallest responsible layer. Changing a misleading label may be enough; duplicate submission may require an operation guard below the view. Do not merely disable a button if keyboard shortcuts or another view can still trigger the same action.

Done: the change has a specific user outcome and its dependencies are understood. Report a proposed scope expansion separately if fixing the root cause would alter unrelated behavior.

## Translate principles into implementation

Choose relevant cards from the [principle index](../principles/index.md) and state the behavior they imply. For example:

| Problem | Reasoning | Implementation consequence |
| --- | --- | --- |
| Retry clears valid data | Working memory and Postel | Preserve known-safe entries and attach actionable field errors |
| Pending request looks complete | Doherty and mental model | Acknowledge input promptly; show pending until operation acknowledgment |
| Repeated settings feel unrelated | Similarity and proximity | Reuse labels, control semantics, and meaningful grouping |
| Advanced workflow requires repeated pointer travel | Fitts and flow | Add discoverable scoped shortcuts while retaining pointer access |

Preserve design tokens, components, domain language, and valid expert workflows. Use existing accessible native controls before adding custom interaction infrastructure. Validate platform advice for the actual implementation; HTML patterns are not native API contracts.

## Account for the affected state transitions

Use [states and recovery](../foundations/states-and-recovery.md) to identify transitions actually relevant to the change. A read-only label fix does not need an offline state machine. A multi-step save does need explicit pending, failure, completion, and recoverability behavior.

Example operation ownership:

```text
on_request(command):
    if operation_for(command.resource) is already pending:
        expose current operation instead of starting a duplicate
    else:
        record operation identity
        dispatch command

on_result(operation_id, result):
    apply only to the matching operation and resource
    display acknowledged outcome
    preserve retry context on recoverable failure
```

This is illustrative logic. Select the real cancellation, idempotency, and concurrency policy from the application's contracts. A disabled visual state does not prove backend idempotency.

Apply [content/localization](../foundations/content-and-localization.md) for new copy and [interaction](../foundations/interaction.md) for changed focus or input behavior. Review [accessibility](../foundations/accessibility.md) for affected controls and presentation.

## Verify and stop

Choose checks proportional to risk using [evaluation](../foundations/evaluation-and-metrics.md). Reproduce the reported problem; exercise the modified behavior and nearby consequential failure states. Use meaningful automated coverage for logic and manual runtime checks for interaction. Reuse existing checks before adding tooling.

For visual-only changes, inspect relevant sizes, themes, text lengths, and focus states. For consequential actions, verify acknowledgement, duplicates, errors, cancellation races, and recovery as applicable. Record checks that were unavailable; do not substitute a successful build for runtime UX verification.

Completion: requested behavior works with evidence, appropriate existing checks pass, necessary unverified items are explicit, and no unrelated redesign has been introduced. Summarize outcome, relevant reasoning, evidence, and limits. Use [a decision record](../../assets/templates/decision-record.md) only when persistent documentation is requested.
