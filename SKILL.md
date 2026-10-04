---
name: ux-laws
description: Apply Laws of UX when designing or implementing visible interface behavior, or auditing usability, in web, mobile, desktop, and specialized software. Translate relevant principles into scoped changes and verifiable acceptance criteria. Use for interaction, navigation, forms, feedback, information hierarchy, and recovery; backend-only work does not require this skill.
---

# UX Laws

Turn observable usability problems into implementable behavior. Use the 30 concepts in [Laws of UX](https://lawsofux.com/es/) as a reasoning framework, supported by platform guidance and accessibility standards. They are neither a universal checklist nor proof that a particular design will work.

## Start with the actual task

1. Identify the requested outcome and affected user journey. Inspect existing screens, interaction code, state handling, terminology, design conventions, and available tests. Separate observed behavior from assumptions.
2. Establish users and expertise, environment, input modalities, platform, consequential actions, and constraints. Use repository evidence first; ask only about decisions that materially affect the work. Record unresolved assumptions without inventing research.
3. Choose a mode below. Load its workflow, the relevant platform reference, and the pattern matching the affected journey. Use the [principle index](references/principles/index.md) to select relevant cards; avoid loading the whole library.
4. Translate each selected principle into a specific behavior and an acceptance check. Explain the problem before naming the principle. If no concrete consequence follows from a principle, omit it from the change justification.
5. Implement or propose the requested work, then check affected states and modalities. Finish with the compact evidence format below. Broaden scope only when the request or a necessary dependency warrants it.

Completion means the requested outcome is addressed, affected consequential states are accounted for, checks have evidence, and unverified assumptions or limitations are visible.

## Modes

| Request | Read | Result |
| --- | --- | --- |
| New experience, flow, component, or interaction specification | [Design](references/workflows/design.md) | Task model, behavior, alternatives where meaningful, and acceptance criteria |
| Feature, fix, or improvement in an existing interface | [Implementation](references/workflows/implementation.md) | Scoped changes that fit the codebase, plus evidence |
| Review or audit of a defined interface or journey | [Audit](references/workflows/audit.md) | Prioritized findings with evidence, impact, proposed remedy, and validation |
| Validation of existing work | [Evaluation](references/foundations/evaluation-and-metrics.md) | Results for defined acceptance criteria; scope stays fixed unless evidence requires a correction |

An audit does not authorize implementation. A small UI change does not require a full-product audit. Use existing project tools; this package adds no runtime framework or network requirement.

## Select references by the problem

| Observable problem or task | Pattern |
| --- | --- |
| Users cannot find a destination or recover their place | [Navigation and search](references/patterns/navigation-and-search.md) |
| Too many choices, unclear defaults, difficult settings | [Choices and settings](references/patterns/choices-and-settings.md) |
| Data entry, validation, authentication, submission | [Forms and authentication](references/patterns/forms-and-authentication.md) |
| Dense information, tables, charts, monitoring | [Data and dashboards](references/patterns/data-and-dashboards.md) |
| Selection, manipulation, custom surfaces, authoring | [Editors and canvas](references/patterns/editors-and-canvas.md) |
| First use, resumption, steps, task completion | [Onboarding and progress](references/patterns/onboarding-and-progress.md) |
| Waiting, network operations, cancellation, status | [Feedback and asynchronous work](references/patterns/feedback-and-async.md) |
| Live output, hazardous actions, operator controls | [Live and critical operations](references/patterns/live-and-critical-operations.md) |

Choose the actual platform: [web](references/platforms/web.md), [mobile](references/platforms/mobile.md), [desktop](references/platforms/desktop.md), or [specialized](references/platforms/specialized.md). Hybrid products may need more than one reference. Preserve differences between CSS pixels, points, density-independent pixels, and physical geometry.

Read foundations when their trigger applies:

- [Accessibility](references/foundations/accessibility.md): changed controls, structure, visual presentation, announcements, timing, or input. This is the source of numeric accessibility guidance in this package.
- [Interaction](references/foundations/interaction.md): focus, keyboard, touch, pointer, gestures, shortcuts, gamepad, remote, or spatial selection.
- [States and recovery](references/foundations/states-and-recovery.md): asynchronous work, data loss, empty/error/partial states, offline behavior, cancellation, or consequential actions.
- [Content and localization](references/foundations/content-and-localization.md): labels, help, errors, dates, quantities, bidirectional layout, or unfamiliar domain concepts.
- [Evaluation and metrics](references/foundations/evaluation-and-metrics.md): acceptance checks, measurement, instrumentation, user evaluation, and evidence limits.

## Resolve tradeoffs explicitly

- Give accessibility, user control, and prevention of serious errors priority over decorative polish, engagement, and small speed gains.
- Preserve useful domain conventions and expert efficiency. Compare task time, error cost, discoverability, and recoverability before replacing a dense professional interface with a novice flow.
- Separate necessary domain complexity from presentation complexity. Move work to the system only when defaults, inference, and automation remain understandable and correctable.
- Use honest progress, actual completion states, and proportional interruption. A motivational effect is not permission for pressure, false urgency, fabricated completion, or undisclosed waiting.
- Treat numbers attached to cognitive principles as contextual observations. Miller is not a menu cap; Doherty is not a promise that every operation finishes within a fixed time.
- Accept safe equivalent formats without guessing consequential meaning. Postel does not override security validation, authorization, or explicit confirmation of ambiguity.
- Preserve the user's requested product and authorized scope. State any proposed expansion separately; do not silently redesign unrelated UI or create persistent reports.

## Evidence and source discipline

Distinguish four things: a principle's explanation, this package's implementation recommendation, a platform recommendation, and a normative requirement. Consult the [source registry](references/sources.md) when a citation, numeric rule, or current requirement matters. Local guidance supports offline work; verify changing requirements against the applicable official source when connectivity is available. If verification is unavailable, disclose the dated guidance and uncertainty, and proceed only where the missing fact is not essential to correctness.

Do not claim user validation without participants, accessibility conformance from partial checks, or measured performance from visual inspection. Mark checks as observed, automated, manually exercised, proposed, or unavailable. A screenshot can support a visual finding; it cannot establish keyboard or assistive-technology behavior.

## Deliver the result

Keep the final explanation proportional to the change:

1. **Outcome:** what changed or what the audit found, and which task it helps.
2. **Reasoning:** relevant principles, concrete tradeoffs, and authoritative requirements when applicable.
3. **Evidence:** checks actually performed, environment and meaningful results.
4. **Limits:** unresolved assumptions, unavailable checks, and next validation needed.

For a one-control fix, a few sentences can cover this. For an audit, use severity and evidence per finding. Produce project files for UX documentation only when requested or already required by the project. Optional assets: [brief](assets/templates/ux-brief.md), [decision record](assets/templates/decision-record.md), [audit](assets/templates/audit-report.md), [verification plan](assets/templates/verification-plan.md).

## Maintain this package

Keep each substantive rule in one authoritative reference and link to it from related material. Preserve source provenance and review dates when updating guidance. Add references only when they change implementation decisions.

Run the offline structural check from any directory:

```sh
python3 /path/to/ux-laws/scripts/validate_skill.py /path/to/ux-laws
```

It checks packaging and routing, not usability or conformance. After material changes, use the [behavioral verification scenarios](references/verification-scenarios.md) for an independent, scoped evaluation.
