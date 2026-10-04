# States, asynchronous feedback, and recovery

Read when an action loads data, saves work, depends on connectivity, changes permissions, or can fail. Pair with [feedback and asynchronous operations](../patterns/feedback-and-async.md), [live operations](../patterns/live-and-critical-operations.md), and [accessibility](accessibility.md). Search terms: pending, partial, stale, offline, retry, cancel, undo, duplicate.

## Define the state model before polishing feedback

Describe what the user knows and can safely do in each relevant state. Do not require an elaborate state machine for a simple control; do require explicit behavior where concurrent work, data loss, or uncertain outcomes are possible. Separate the state of fetched data, user edits, connection, and operations. “Offline with saved data” and “offline with unsent edits” need different information.

| State | Information and action to provide | Implementation question |
|---|---|---|
| Idle / ready | Current value, scope, and available action | Is the action enabled because its prerequisites are met? |
| Pending | Acknowledgment, truthful progress if known, remaining useful actions | Can the operation be repeated, canceled, or left running? |
| Success | What completed and where the result is available | Does success mean accepted, persisted, delivered, or merely queued? |
| Empty | Why nothing is shown and a relevant next step | Is this first use, an empty query, missing access, or an empty dataset? |
| Error | User-relevant failure, retained work, recovery route | Is retry safe; what is known about the previous attempt? |
| Partial | Completed and failed portions separately | Will retry affect only failures or repeat successes? |
| Stale | Age or freshness limitation and a refresh path | Which decisions are unsafe with this data? |
| Offline | Connectivity state, local capability, unsent work | Are updates queued, blocked, or already persisted locally? |
| Canceled | What stopped and what remains | Did local cancellation also stop remote work? |

Do not display all these states everywhere. Choose those that can occur in the scoped flow, and test transitions rather than screenshots alone.

## Honest feedback and concurrency

Acknowledge activation promptly with the smallest useful cue: pressed state, changed button label, inline status, or task indicator. Keep user input responsive while work runs. A percentage requires measurable progress with a defensible denominator; otherwise show indeterminate progress and useful stage information. Do not add a fabricated percentage or a minimum artificial wait to imply trustworthiness.

Consider the operation's identity. Rapid repeat clicks, retries after a network timeout, and multiple tabs can create duplicates. Disable a trigger while the same non-repeatable request is pending only when that matches the operation; also use appropriate server-side safeguards when the backend is in scope. UI disabling alone does not establish exactly-once execution. A canceled request or disconnected client may leave remote work running. When outcome is unknown, show uncertainty and provide reconciliation before encouraging a risky retry.

Ignore or reconcile stale asynchronous responses: an earlier search response must not replace a newer query's results. Decide whether optimistic changes can be rolled back safely. If another update may have occurred, offer reconciliation instead of restoring a blind snapshot that overwrites newer work. For partial bulk operations, preserve item identities and report per-item outcomes; a general “failed” message should not imply that nothing changed.

## Recovery proportional to consequence

Preserve entries, selections, and context through validation and transient failure. Focus or link to actionable errors, and explain the correction using the field's language. Separate user-correctable input from service, permission, and connectivity failures. Do not blame the user for a server error or show internal stack traces as the recovery instruction.

Prefer undo for routine reversible operations where reversal is reliable. Show irreversible consequences before commitment, using the actual object and scope. If undo has a real time or storage limit, disclose it; do not promise undo after external delivery or permanent deletion when the system cannot supply it. Avoid generic modal confirmation that users can learn to dismiss without understanding the consequence.

For long operations, define leaving the view, browser refresh, application restart, and reconnect behavior. Restore enough status to tell the user whether work continues, completed, or needs action. Local draft persistence has privacy and security implications: avoid saving secrets or sensitive content by default; use the product's existing policy and capabilities.

## Accessible and non-disruptive status

Use persistent inline information when the user needs to reference it. A toast can acknowledge a minor event but should not be the only place to recover important work. Background success should usually preserve focus; a dialog is appropriate only when the user must make a decision before proceeding. [WCAG Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) explains programmatic exposure without focus changes. [APG alerts](https://www.w3.org/WAI/ARIA/apg/patterns/alert/) are informative guidance for important brief messages, not a reason to mark every update urgent.

For screen readers, announce meaningful transitions and summarize bursty updates. Do not repeatedly announce a ticking counter, every log line, or every preview frame. Keep error messages associated with affected fields and expose expanded, selected, invalid, and busy states accurately. Native applications must verify corresponding native accessibility behavior; ARIA attributes cannot repair a native canvas.

## Acceptance scenario and observation

For a multi-file export: pending state names the operation; cancel indicates which files already completed; a failed file does not erase successful results; retry targets failed items without silently overwriting existing files. Disconnect after submission produces an honest unknown/queued state until reconciled. Returning to the view restores the operation's status. Keyboard and assistive-technology users can find the output, error, and retry action without receiving an announcement flood.

Observe latency, failure classes, retry outcomes, abandonment, and duplicate attempts only when useful to the task. Prefer event categories and coarse durations over recording entered text, file contents, personal identifiers, or credentials. Describe the event schema and retention within existing privacy practices. Counts alone do not explain why users failed; combine them with reproducible technical evidence or consented user research. Never infer success from a click when completion occurs later.

Sources consulted 2026-10-04. The state matrix and implementation checks are practical guidance, not a new normative standard.
