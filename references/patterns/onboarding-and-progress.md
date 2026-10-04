# Onboarding and progress

Use for first use, setup, guided workflows, prerequisites, checkpoints, and long operations. Identify what the user is trying to accomplish now; onboarding is useful only when it helps that task. Read [content and localization](../foundations/content-and-localization.md) for instruction clarity and [states and recovery](../foundations/states-and-recovery.md) for interruptions.

## Teach at the point of need

Introduce the minimum concept required for the next meaningful action. Prefer a useful initial state, example data clearly labeled as examples, and contextual guidance over a forced tour of every feature. A professional tool may need discoverable help and a sample task without delaying repeat users. Allow dismissal and later access where instruction is optional.

Distinguish required setup from education and optional preferences. Explain why a permission or external connection is needed before requesting it; avoid soliciting unrelated permissions during first launch. If a prerequisite is unavailable, show the supported route around it or an accurate limit. Do not present an optional integration as an unavoidable step.

Use [mental models](../principles/mental-model.md) to connect new concepts to the user's task vocabulary. [Cognitive load](../principles/cognitive-load.md) suggests staging information; it does not justify hiding consequential details. [Tesler's Law](../principles/teslers-law.md) suggests doing work the system can reliably handle instead of making the user repeat it.

## Represent progress truthfully

Show steps when a workflow has meaningful stages. Keep completed answers available, identify the current stage, and explain remaining work. If branches change the total, use stage labels or disclose the updated count rather than showing a falsely fixed denominator. WAI's multi-page form guidance describes progress and navigation techniques; apply those techniques to the actual workflow rather than splitting every form. [WAI multi-page forms](https://www.w3.org/WAI/tutorials/forms/multi-page/).

For system operations, separate known work progress from uncertain duration:

```text
queued -> running(known units completed/total OR unknown total)
running -> completed(receipt) | failed(reason) | cancellation_requested
cancellation_requested -> cancelled | completed | cancellation_failed
```

Use a percentage only when it represents a defensible measurement. An operation that has uploaded all bytes but is still processing is not fully complete; label its stages. When duration is unknown, use an indeterminate status plus the current activity and supported controls. A cancellation request should not instantly claim cancellation if the operation can still finish remotely.

[Goal-Gradient Effect](../principles/goal-gradient-effect.md) can guide visible milestones, but does not justify fake progress or fabricated accomplishments. [Zeigarnik Effect](../principles/zeigarnik-effect.md) can guide resume cues; do not turn unfinished tasks into coercive nagging. Let users understand and intentionally leave a workflow. A final summary can support closure by showing the actual outcome and relevant next step.

Time-limited flows need special attention. Web WCAG Timing Adjustable contains conditions and exceptions for time limits, including real-time and essential situations; inspect applicability before adopting a universal timeout rule. [W3C timing explanation](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html). Preserve drafts and provide warning or extension behavior when required and supported. Shared-device privacy may constrain durable draft storage; respect the product's policy.

## Example and counterexample

A document import shows "Uploading", then "Checking contents", then a receipt with imported and rejected item counts. A setup checklist distinguishes required device pairing from optional tutorial content and supports resuming. Counterexample: a timer drives progress to 99%, the UI forces unrelated notification permissions, and closing the window silently discards completed setup answers.

## Acceptance checks

- New users can reach a useful result; returning users can bypass optional instruction and reopen help.
- Verify backtracking, branching, interruption, resume, and inaccessible prerequisites with realistic data.
- Confirm stage/count/percentage meaning against actual operation signals; no local timer invents success.
- Test cancellation races, partial completion, failure, and applicable timeout behavior.
- Check announcement cadence and reduced-motion behavior through [accessibility](../foundations/accessibility.md). Progress must inform without overwhelming.

Sources consulted: 2026-10-04. Workflow/state recommendations are non-normative; WAI materials explain web implementation and criterion applicability.
