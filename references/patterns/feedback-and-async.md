# Feedback and asynchronous work

Use when a control initiates work that outlives the input event: saving, loading, connecting, sending, processing, or synchronizing. Read [states and recovery](../foundations/states-and-recovery.md) for the shared failure model. Keep feedback proportional to outcome importance; an ordinary background refresh should not interrupt a person completing a form.

## Distinguish intent from outcome

Represent accepted input, pending work, and acknowledged completion separately. Immediate local feedback can show that a button was activated; it cannot establish that a remote operation succeeded. Establish which layer supplies the authoritative outcome: service receipt, durable write, device acknowledgment, or another existing contract.

```text
idle -> requested(operation_id) -> pending
pending -> acknowledged(result) | rejected(reason) | outcome_unknown
outcome_unknown -> status_check | supported_recovery
```

Do not collapse an unknown outcome into failure when duplicate execution could matter. Coordinate retry with the operation's deduplication or status semantics. If those semantics are absent, present the uncertainty and avoid claiming a retry is harmless. Handle older responses by request identity or revision so that a delayed success cannot overwrite newer work.

Optimistic UI can suit reversible, low-cost actions when rollback is understandable. Show a failed favorite toggle's real state and a recovery route. For costly actions, persistent state should follow acknowledgment. Avoid hiding ambiguity behind a transient success toast. If the user leaves the view, determine whether work continues, cancels, or remains available elsewhere according to existing behavior.

## Choose feedback location and urgency

Use local inline feedback for a field or action, persistent banners for ongoing service conditions, and an outcome area or history when users need to revisit results. Use transient messages for low-stakes information that does not require action or later retrieval. A critical failure should survive long enough to be understood and acted on. An alert dialog is appropriate only when interruption is needed for a decision, not as the default error container.

On the web, qualifying status messages must be programmatically available without receiving focus under WCAG 2.2 SC 4.1.3, Level AA. Use appropriate status semantics and verify actual announcements; repeatedly announcing every incremental update can overwhelm users. [W3C status-message explanation](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html). Native applications need corresponding accessibility APIs and runtime checks; ARIA attributes do not apply to a native scene graph.

Avoid reflow that moves the triggering control unexpectedly, especially during repeated actions. Reserve space for predictable status or place feedback nearby without covering essential controls. Do not turn every success into a modal or move focus merely to make an announcement happen. If a completion changes context, such as opening a new result view, manage that context transition deliberately.

[Doherty Threshold](../principles/doherty-threshold.md) can prompt attention to responsiveness, but is not a universal network SLA. Measure response segments that affect the task. [Flow](../principles/flow.md) supports keeping attention on work. [Working memory](../principles/working-memory.md) supports attaching feedback to the object and action rather than requiring users to recall what an unlabeled "Done" meant.

## Example and counterexample

An upload list keeps each file's queued, uploading, processing, complete, or failed state beside its name. A failed file can be retried without restarting completed files. Counterexample: one page-level spinner hides all files, "Success" disappears before the user reads it, and reconnect resends every upload without checking prior outcomes.

## Acceptance checks

- Verify immediate input feedback and authoritative completion independently under delay.
- Test rejection, connection loss, timeout, duplicate activation, stale responses, cancellation, and navigation away where relevant.
- Check persistence and discoverability of consequential outcomes after a transient message disappears.
- Test announcements with the target assistive technology; routine progress does not seize focus or speak continuously.
- Compare requested, displayed, and acknowledged values after rollback or partial completion. Use [evaluation and metrics](../foundations/evaluation-and-metrics.md) for task-appropriate performance evidence.

Sources consulted: 2026-10-04. The W3C page is informative explanation of a normative web criterion; this operation model is an illustrative implementation recommendation.
