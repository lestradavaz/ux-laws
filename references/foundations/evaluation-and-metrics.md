# Evaluation, evidence, and metrics

Read when deciding whether a proposed UX change helps, selecting acceptance checks, auditing a flow, or interpreting measurements. Pair with the relevant pattern and [accessibility](accessibility.md). Read [cognitive bias](../principles/cognitive-bias.md) when an interpretation favors an expected result, and [data and dashboards](../patterns/data-and-dashboards.md) when measurement itself appears in the UI. Search terms: hypothesis, observed, task success, error, time, research, guardrail, audit, telemetry.

## Make the claim testable

State the user's task, relevant audience and context, current friction, proposed behavior, and expected outcome. A UX principle is a reason to investigate, not evidence that the proposed design works. “Grouping these filters should reduce search mistakes” is a hypothesis. “In the tested build, keyboard users cannot reach the filter reset button” is an observed finding. Keep that distinction in findings and implementation reports.

Choose acceptance conditions observable in the scoped product: a task can be completed, an error can be corrected, focus remains usable, values retain their meaning, or feedback accurately reflects completion. Avoid universal targets for clicks, duration, conversion, or number of options. An expert editor may benefit from dense controls; a time limit can be harmful in an accessible form. Use task evidence, consequences, and project constraints to decide what counts as improvement.

## Select proportional evidence

| Question | Suitable method | Limit |
|---|---|---|
| Does the implementation preserve a state invariant? | Focused component, integration, or state-transition test | Passing assertions may miss confusing content or unsupported input. |
| Can a supported input mode complete the task? | Manual task walkthrough in the actual build | One configuration does not establish all devices or abilities. |
| Is there an obvious standards failure? | Automated checks plus targeted manual accessibility review | Tools cannot assess every criterion or real task comprehension. |
| Do users understand choices and recover from mistakes? | Representative task-based usability sessions | Small samples reveal problems; they do not establish population rates. |
| Did behavior change after release? | Suitable instrumentation and comparison | Correlation, selection effects, seasonality, and technical changes can distort interpretation. |
| Does a treatment cause a measurable outcome difference? | Controlled experiment when feasible and justified | Sample size, exposure, validity, harm, and guardrails need deliberate design. |

Do not prescribe an experiment or broad research study for a low-impact reversible change. Existing evidence and a focused walkthrough may be enough. For a major uncertain decision, inspect whether representative research is available and identify the remaining uncertainty instead of manufacturing certainty from a heuristic score.

## Build realistic tasks

Use representative data volume, labels, permissions, history, and device constraints. Exercise the happy path and the failures most likely to affect completion or cause harm. Include novice and experienced needs when both audiences matter; avoid defining expert efficiency only through a first-use session.

Write a task prompt around an outcome rather than telling participants which control to use. “Find next week's unpaid invoices and export them” tests navigation and interpretation; “Click the Filters button, choose Unpaid, then click Export” tests compliance with directions. Use non-sensitive fixture data and avoid recording credentials or personal material. Capture observations with consent and established retention practices where user research is authorized.

For accessibility evaluation, inspect actual semantics and complete tasks with relevant assistive technologies. [WAI's evaluation overview](https://www.w3.org/WAI/test-evaluate/) recommends a combination of approaches; [involving users](https://www.w3.org/WAI/test-evaluate/involving-users/) adds evidence that standards review alone does not supply. User sessions complement conformance evaluation rather than replacing it. A participant successfully completing a task does not prove all applicable criteria pass.

## Choose metrics around the outcome

Define numerator, denominator, eligible population, start/end events, exclusions, and observation window before interpreting a rate. Task success should represent the intended result, not merely button activation. Count retries and abandoned attempts according to the same task definition, and distinguish technical failures from user corrections. For long or asynchronous work, measure accepted, completed, and discovered-result stages separately when needed.

Useful candidates include completion rate, harmful error rate, recovery success, task duration, repeated attempts, abandonment point, help use, and qualitative confidence. Each is contextual. Faster completion can come from skipping important verification; lower help use can mean help became unreachable; higher conversion can come from coercion. Select guardrails that prevent the proposed improvement from hiding harm, such as accidental commitments, accessibility regression, data loss, or increased support burden.

Inspect latency distributions and long-tail failures where delays matter, rather than treating an average as every user's experience. Segment only when useful and privacy-compatible: input mode, task complexity, supported device class, or new/returning users may reveal meaningful differences. Avoid small-cell reporting that exposes individuals or creates misleading conclusions. Do not collect entered content to diagnose a generic validation event when a safe error category will answer the question.

## Prioritize and report honestly

Use severity based on task impact, consequence, affected users, frequency, and recovery—not on how many laws a finding cites. A rare irreversible loss can outrank a frequent cosmetic inconsistency. Include reproducible context, observed behavior, proposed correction, and a proportionate acceptance check. If incidence is unknown, mark it unknown; do not invent a frequency or attach a numerical severity formula for apparent precision.

After implementation, list checks performed, result, material gaps, and remaining hypotheses. Keep automated/static checks distinct from runtime observation and user evidence. Explain a deliberate exception through the user's task and available evidence. Do not write a report file unless requested or already part of the project's workflow; concise delivery notes can carry verification results.

## Acceptance example

For redesigned filters: a manual keyboard and touch walkthrough confirms that users can apply, inspect, and reset criteria without losing focus or selected values. Integration tests cover stale responses and retained filters on failure. Existing telemetry can compare successful result discovery and repeated filter changes if its event definitions are adequate. A claim about clearer terminology remains a hypothesis until supported by relevant user evidence. The release check names tested configurations and avoids declaring whole-product accessibility conformance from the changed flow.

Sources consulted 2026-10-04. Metric candidates and prioritization guidance are original practical recommendations, not validated universal thresholds or a replacement for a research protocol.
