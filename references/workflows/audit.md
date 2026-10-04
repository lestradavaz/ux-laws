# Audit a defined interface or journey

Use for an explicitly requested usability review. This mode produces findings; it does not authorize changes. Define the surfaces, tasks, roles, platforms, modalities, and evidence available before assessing them. For a full product, inventory journeys first; for a single flow, stay within that flow and its necessary dependencies.

## Gather observable evidence

Exercise representative tasks when a runtime is available. Otherwise inspect code, supplied screenshots, recordings, or specifications and state the evidence boundary. Code inspection can reveal missing error handling; a screenshot can reveal grouping; neither demonstrates a working screen-reader journey.

Map entry, critical decision, work in progress, result, and recovery. Use the [principle index](../principles/index.md) and relevant [patterns](../../SKILL.md) to inspect likely problems, rather than producing a checklist comment for every law. For a comprehensive audit, consider every family and record exclusions by journey or modality; irrelevant laws need no fabricated finding.

Cover applicable [accessibility](../foundations/accessibility.md), [interaction](../foundations/interaction.md), [states](../foundations/states-and-recovery.md), and [content](../foundations/content-and-localization.md). Treat valid professional density and deliberate safety friction as potential requirements, not defects by default.

## Write actionable findings

Each finding should contain:

- **Location and trigger:** affected screen/control and starting conditions.
- **Evidence:** reproducible steps, observed output, or code/specification evidence; label hypotheses.
- **User consequence:** who is affected, task impact, frequency if known, and recovery cost.
- **Reasoning:** relevant principle and applicable requirement, with a primary citation where needed.
- **Remedy:** specific behavior, preserving intended scope and domain constraints.
- **Verification:** how to establish the remedy works; note unavailable evidence.

Example: “After an export fails, all options reset. An operator must reconstruct a destination and quality settings before retrying. Preserve valid options and attach the failure to the operation. Test a failed transfer followed by retry to the same destination.” This is stronger than “violates Miller's Law.”

## Prioritize by consequence

| Severity | Observable consequence |
| --- | --- |
| Critical | Serious harm, consequential data loss, unintended live output, or a blocked essential task with no usable alternative |
| High | Core task failure, inaccessible required action, or costly repeated errors with difficult recovery |
| Moderate | Recoverable confusion, avoidable delay, or friction on a meaningful task |
| Low | Minor clarity or consistency issue with limited task impact |

Adjust priority using affected users, exposure, confidence, and dependencies. Distinguish severity from ease of implementation. A low-frequency accessibility barrier can still be high severity. A cosmetic defect does not become critical merely because a principle applies.

Consolidate findings that share a root cause. Avoid double-counting one misgrouped control under three Gestalt principles. Separate measured facts from predictions about cognition or conversion.

## Deliver a bounded result

Lead with the most consequential findings and the audited boundary. Include practical next actions, evidence limits, and proposed validation. If a pass finds no issues, say what was inspected and what remains unknown; a clean partial review is not proof of universal usability or accessibility conformance.

Use [evaluation and metrics](../foundations/evaluation-and-metrics.md) to design follow-up checks. Save an [audit report](../../assets/templates/audit-report.md) only when requested; otherwise return findings directly. Completion means the defined scope was examined using available evidence and findings can be acted on without guessing their trigger, impact, or intended remedy.
