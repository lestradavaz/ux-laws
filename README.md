# UX Laws

**Turn UX principles into practical interface behavior, scoped implementation changes, and observable acceptance criteria.**

`ux-laws` is a reusable skill for development projects with a visible UI: websites, mobile applications, desktop tools, dashboards, editors, kiosks, games, spatial interfaces, and professional control software. It supports new design, implementation, audits, and verification.

The package covers all **30 concepts from [Laws of UX](https://lawsofux.com/es/)** through original implementation guidance, supported by accessibility standards and official platform documentation. Each principle has observable triggers, practical actions, an example, a counterexample, limits, acceptance checks, and exact source links.

Repository: [lestradavaz/ux-laws](https://github.com/lestradavaz/ux-laws). Skill identifier: **`ux-laws`**. Documentation language: **English**. License: **[MIT](LICENSE)**.

## Contents

- [Install](#install)
- [Start using the skill](#start-using-the-skill)
- [Choose a working mode](#choose-a-working-mode)
- [How the workflow works](#how-the-workflow-works)
- [Prompt recipes](#prompt-recipes)
- [What a useful result contains](#what-a-useful-result-contains)
- [Reference library](#reference-library)
- [Complete principle catalog](#complete-principle-catalog)
- [Platform coverage](#platform-coverage)
- [Evidence, accessibility, and source policy](#evidence-accessibility-and-source-policy)
- [Templates](#templates)
- [Validate this package](#validate-this-package)
- [Publishing and skills.sh discovery](#publishing-and-skillssh-discovery)
- [Troubleshooting](#troubleshooting)
- [Maintenance and contributions](#maintenance-and-contributions)
- [License and source provenance](#license-and-source-provenance)

## Install

### Requirements

For installation with `npx`, have Node.js, npm/npx, and Git available, with connectivity to the public repository. The tested `skills` CLI version is **1.7.0**, whose package declares **Node.js 22.20.0 or newer**. Check the [current CLI package](https://www.npmjs.com/package/skills) when using a newer release; its requirements can change.

The skill itself is Markdown and supporting resources. It adds no application runtime, UI framework, package manager configuration, or network service. Python 3 is needed only to run its optional structural validator.

### Inspect available skills first

```sh
npx skills add lestradavaz/ux-laws --list
```

The output should include **`ux-laws`**. `--list` discovers available skills without installing them into destination environments. This is a discovery check, not an installation or usability test.

### Install into a project

Run from the development project where you want to use the skill:

```sh
npx skills add lestradavaz/ux-laws --skill ux-laws
```

Project scope is the default. Select the appropriate destination when prompted; the CLI's behavior also depends on the environment in which it is executed. The repository source is `lestradavaz/ux-laws`; the skill name selected by `--skill` is `ux-laws`.

### Install across projects

```sh
npx skills add lestradavaz/ux-laws --skill ux-laws --global
```

Use global scope when you want availability across your projects. Installation paths, target selection, and loading behavior depend on the destination environment. See the [official CLI reference](https://skills.sh/docs/cli) and [CLI installation documentation](https://github.com/vercel-labs/skills#installation).

### Check, update, or remove

```sh
npx skills list
```

To check for global installation, use `npx skills list --global`. To update this skill, run `npx skills update ux-laws` and select the appropriate scope if requested. To remove a project installation, run `npx skills remove ux-laws`; add `--global` for global scope.

Keep the full skill directory: `SKILL.md`, `references/`, `assets/`, and `scripts/`. A download containing only `SKILL.md` loses the linked guidance this package depends on.

## Start using the skill

In an environment supporting named skill invocation, use **`$ux-laws`** with a concrete task. Otherwise explicitly request the installed `ux-laws` workflow or point to its [SKILL.md](SKILL.md). Invocation syntax and automatic selection vary by environment.

```text
Use $ux-laws to improve the export dialog in this project.
Inspect its current implementation and conventions first.
Preserve the supported export formats and the rest of the editor.
Make pending, failed, canceled, and completed outcomes understandable.
Implement the scoped improvement and report checks actually performed.
```

The skill's description makes it eligible for selection on UI design, interaction implementation, and usability reviews in environments that support automatic discovery. It does not force activation in every environment. For a predictable first use, name it explicitly and state the requested mode and boundary.

Useful context includes the user task, affected journey, platform, expertise, input modes, screenshots or runtime access, and known constraints. Provide what is not discoverable from the project. Repository inspection should resolve implementation facts before questions about product preferences.

You can ask for a response in another language while retaining the English reference library. Specify the language of user-facing product copy separately from the language of the development discussion.

Backend-only work does not need this skill unless the requested change affects visible behavior. A small UI fix should use a small relevant subset of the library.

## Choose a working mode

| Mode | When to use it | Expected result |
| --- | --- | --- |
| [Design](references/workflows/design.md) | Define a new flow, component, interaction, or experience | Task model, selected behavior, meaningful tradeoffs, states, and acceptance criteria |
| [Implementation](references/workflows/implementation.md) | Build a feature or fix an existing interface | Changes fitting the codebase, affected-state handling, and proportionate verification |
| [Audit](references/workflows/audit.md) | Review a defined interface or user journey | Prioritized findings with evidence, consequence, proposed remedy, and checks |
| [Verification](references/foundations/evaluation-and-metrics.md) | Assess whether existing work meets its goals | Observable results for defined criteria, with evidence limits |

An audit request produces findings; it does not authorize code changes. An implementation request can include the inspection necessary for the fix without becoming a whole-product redesign. Verification keeps its agreed scope unless a demonstrated problem warrants correction.

## How the workflow works

1. **Inspect the current task.** Read the actual interface, domain language, state handling, interaction conventions, constraints, and available checks. Separate observed facts from assumptions.
2. **Choose the mode and relevant platform.** Decide whether the result is a specification, implementation, audit, or verification. Hybrid products may need more than one platform reference.
3. **Route by the observable problem.** Select the matching pattern and a small set of principle cards. For example, missed alerts suggest attention and salience; forgotten values suggest working memory; tiny targets suggest Fitts.
4. **Translate reasoning into behavior.** A useful decision names what changes, what user consequence it addresses, and how to check it. Naming a law alone is insufficient.
5. **Resolve tradeoffs.** Consider accessibility, informed control, serious error prevention, domain constraints, expertise, efficiency, and established conventions. Preserve useful professional density.
6. **Implement or propose within scope.** Handle relevant success, failure, interruption, recovery, focus, and input behavior. Use existing project tools and components where appropriate.
7. **Verify and report.** Record checks performed, results, and unavailable evidence. Distinguish proposed checks from observed outcomes.

### Progressive reference loading

The short entrypoint routes to deeper material only when needed. Ordinary work does not require reading every principle, pattern, and platform guide. The [principle index](references/principles/index.md) maps symptoms to relevant cards; the entrypoint maps tasks to patterns and foundations.

This structure gives a one-control fix a narrow path while supporting detailed review of complex products. The README is a human-facing guide, not required reading for each UI change.

## Prompt recipes

Use these as starting points. Replace the task-specific description with your actual feature or journey; scope and evidence matter more than the number of principles cited.

### New interaction design

```text
Use $ux-laws in design mode for a multi-step import flow.
Identify necessary decisions and meaningful groups before choosing screens.
Define preview, validation, partial failure, retry, cancellation, and completion.
Include labels, focus behavior, and observable acceptance criteria.
State assumptions that need product input or user research.
```

### Fix a form without expanding scope

```text
Use $ux-laws to implement a correction in the payment form.
Preserve valid nonsecret entries after validation failures.
Accept only meaning-preserving input variations supported by the service contract.
Do not guess ambiguous dates or amounts, or change credential semantics.
Inspect duplicate submission and unknown timeout outcomes.
Keep unrelated checkout screens unchanged.
```

### Review dense professional information

```text
Use $ux-laws to review this monitoring dashboard for trained operators.
All 20 readings are required during the task; preserve their availability.
Investigate missed alerts, competing visual emphasis, freshness, and recovery.
Provide prioritized findings and concrete acceptance checks.
Separate screenshot observations from hypotheses requiring runtime or user evidence.
```

### Improve a desktop application with live output

```text
Use $ux-laws to improve feedback in our Rust/egui presentation console.
Keep established deliberate activation conventions.
Distinguish selection, dispatched commands, and confirmed output per destination.
Account for one output succeeding while another fails.
Check shortcut ownership during text entry and command emission across redraws.
Do not assume toolkit accessibility support without inspecting integration.
```

### Make a custom canvas operable without precise dragging

```text
Use $ux-laws to add non-drag object reordering while keeping the renderer.
Inspect object identity, ordering, selection, and Undo contracts.
Provide named operations for relevant input modes through the same domain command.
Preserve selection and capture pre-gesture state for cancellation and history.
Apply web-specific requirements only if this is a web implementation.
```

### Audit with limited evidence

```text
Use $ux-laws in audit mode for the supplied screenshots.
Make no code changes.
Report observable clarity, hierarchy, and state risks.
Mark keyboard, dynamic behavior, accessibility semantics, and whole-process checks
as unverified when screenshots cannot establish them.
Use local guidance if sources are unavailable and disclose its review date.
```

### Verify a completed change

```text
Use $ux-laws to verify the updated export dialog against its acceptance criteria.
Exercise relevant input modes and success, failure, and recovery transitions.
Use existing automated checks where they verify meaningful behavior.
Report passed, failed, unavailable, and deferred checks.
Expand no other UI unless evidence shows a necessary dependency.
```

## What a useful result contains

A result should make the conclusion assessable without requiring the full library:

- **Outcome:** changed behavior or principal findings, tied to the affected task.
- **Reasoning:** relevant principles and concrete tradeoffs; applicable requirements are distinguished from recommendations.
- **Evidence:** actual inspection, automated checks, manual runtime exercises, or participant evidence, with meaningful results.
- **Limits:** unresolved assumptions, unavailable configurations, and further validation needed.

For an audit, each finding should also identify location/trigger, user consequence, severity, proposed remedy, and verification. Severity follows task impact and recovery cost, not the count of cited laws.

For example: “A failed export now retains the selected destination and quality settings. A pending operation stays pending until the export service confirms its result. The retry-state test passed; keyboard traversal and output discovery still need a runtime walkthrough.” This clearly separates implementation evidence from checks not yet performed.

Persistent reports and decision records are created only when requested or already required by the project. A short explanation can be sufficient for a small reversible change.

## Reference library

| Area | Coverage and entrypoints |
| --- | --- |
| Principles | [30 individual cards and symptom router](references/principles/index.md) |
| Foundations | [Accessibility](references/foundations/accessibility.md), [interaction](references/foundations/interaction.md), [states/recovery](references/foundations/states-and-recovery.md), [content/localization](references/foundations/content-and-localization.md), [evaluation/metrics](references/foundations/evaluation-and-metrics.md) |
| Navigation and decisions | [Navigation/search](references/patterns/navigation-and-search.md), [choices/settings](references/patterns/choices-and-settings.md) |
| Entry and interpretation | [Forms/authentication](references/patterns/forms-and-authentication.md), [data/dashboards](references/patterns/data-and-dashboards.md) |
| Authoring and continuity | [Editors/canvas](references/patterns/editors-and-canvas.md), [onboarding/progress](references/patterns/onboarding-and-progress.md) |
| Outcomes and operations | [Asynchronous feedback](references/patterns/feedback-and-async.md), [live/critical operations](references/patterns/live-and-critical-operations.md) |
| Workflows | [Design](references/workflows/design.md), [implementation](references/workflows/implementation.md), [audit](references/workflows/audit.md), shared evaluation foundation |
| Maintenance | [Source registry](references/sources.md), [behavioral verification scenarios](references/verification-scenarios.md), [structural validator](scripts/validate_skill.py) |

### Repository layout

```text
ux-laws/
├── README.md
├── LICENSE
├── SKILL.md
├── references/
│   ├── principles/             30 cards and one index
│   ├── foundations/            5 references
│   ├── patterns/               8 references
│   ├── platforms/              4 references
│   ├── workflows/              3 workflows
│   ├── sources.md
│   └── verification-scenarios.md
├── assets/
│   └── templates/              4 optional document templates
└── scripts/
    └── validate_skill.py
```

The root `SKILL.md` exposes one installable skill. Supporting cards are reference material, not separately installable skills.

## Complete principle catalog

Each card uses the same practical structure: principle/evidence, observable triggers, implementation actions, example, counterexample, limits/conflicts, acceptance checks, and sources/related guidance. Select applicable actions proportionally.

| Family | Concepts |
| --- | --- |
| Decisions and complexity | [Choice Overload](references/principles/choice-overload.md), [Hick's Law](references/principles/hick-law.md), [Cognitive Load](references/principles/cognitive-load.md), [Tesler's Law](references/principles/teslers-law.md), [Occam's Razor](references/principles/occams-razor.md), [Pareto Principle](references/principles/pareto-principle.md), [Parkinson's Law](references/principles/parkinsons-law.md), [Postel's Law](references/principles/postels-law.md) |
| Learning and expectations | [Jakob's Law](references/principles/jakob-law.md), [Mental Model](references/principles/mental-model.md), [Paradox of the Active User](references/principles/active-user-paradox.md) |
| Memory and organization | [Chunking](references/principles/chunking.md), [Miller's Law](references/principles/miller-law.md), [Working Memory](references/principles/working-memory.md), [Serial Position Effect](references/principles/serial-position-effect.md) |
| Perception and relationships | [Common Region](references/principles/common-region.md), [Proximity](references/principles/proximity.md), [Prägnanz](references/principles/pragnanz.md), [Similarity](references/principles/similarity.md), [Uniform Connectedness](references/principles/uniform-connectedness.md), [Von Restorff Effect](references/principles/von-restorff-effect.md), [Selective Attention](references/principles/selective-attention.md) |
| Interaction and continuity | [Fitts's Law](references/principles/fitts-law.md), [Doherty Threshold](references/principles/doherty-threshold.md), [Flow](references/principles/flow.md) |
| Motivation and evaluation | [Goal-Gradient Effect](references/principles/goal-gradient-effect.md), [Zeigarnik Effect](references/principles/zeigarnik-effect.md), [Peak-End Rule](references/principles/peak-end-rule.md), [Aesthetic-Usability Effect](references/principles/aesthetic-usability-effect.md), [Cognitive Bias](references/principles/cognitive-bias.md) |

The term “law” spans perceptual relationships, cognitive concepts, effects, and practical heuristics. The cards identify their limits and distinguish contextual recommendations from empirical guarantees.

## Platform coverage

| Platform | Adaptations |
| --- | --- |
| [Web](references/platforms/web.md) | Native HTML behavior, semantic controls, custom-widget responsibilities, browser navigation, focus, responsive layout, and async state |
| [Mobile](references/platforms/mobile.md) | Actual hit regions, text scaling, gestures and alternatives, native semantics, interruptions, permission and connectivity states |
| [Desktop](references/platforms/desktop.md) | Keyboard-heavy workflows, expert density, window/document ownership, save/export state, monitors, and accessibility integration |
| [Specialized](references/platforms/specialized.md) | Kiosks/shared sessions, game HUDs, spatial comfort, constrained hardware, professional monitoring, and domain-specific operational limits |

Rust/egui is an illustrative desktop case. No particular framework is required. Web patterns are adapted to native or specialized UI through actual platform semantics, input behavior, and product contracts.

## Evidence, accessibility, and source policy

The library is self-contained for general practice. Its [source registry](references/sources.md) records provenance and consultation dates; exact links also appear alongside relevant claims. Local guidance was reviewed on **2026-10-04**. Standards, platform recommendations, and APIs can change, so verify current official sources when a changing fact materially affects correctness.

Accessibility values and their scopes are centralized in [the accessibility foundation](references/foundations/accessibility.md). It separates web criteria, native recommendations, levels, units, and exceptions. A partial check of a changed component does not establish whole-application conformance.

Important interpretation boundaries include:

- **Miller:** memory experiments do not impose a universal seven-option menu limit.
- **Doherty:** responsiveness needs task-specific measurement; feedback does not establish completion or justify artificial delay.
- **Postel:** input tolerance follows explicit meaning-preserving contracts; it does not authorize guesses about credentials, money, dates, permissions, or machine protocols.
- **Goal gradient and Zeigarnik:** progress and resumable work should be honest and controllable; optional adoption goals do not redefine task completion.
- **Pareto:** prioritize using evidence while preserving essential access and rare consequential needs; an assumed ratio is insufficient.
- **Aesthetics and minimalism:** preserve labels, comparisons, scope, state, and justified expert efficiency.

Verification is proportional to the change. Automated checks, code inspection, runtime walkthroughs, assistive-technology exercises, and participant research provide different kinds of evidence. An unavailable method is recorded as a limitation rather than replaced with an unsupported claim. Participant research requires actual availability and authorization.

## Templates

Four templates are available when persistent documentation is requested:

| Template | Use |
| --- | --- |
| [UX brief](assets/templates/ux-brief.md) | Outcome, users, constraints, journey, proposed behavior, acceptance, and open questions |
| [Decision record](assets/templates/decision-record.md) | Selected behavior, evidence, tradeoff, consequences, and revisit conditions |
| [Audit report](assets/templates/audit-report.md) | Review boundary, prioritized findings, proposed order, and validation needs |
| [Verification plan](assets/templates/verification-plan.md) | Starting conditions, observable expectations, methods, evidence, and limits |

Populate templates with facts, supported hypotheses, or explicit unknowns. Remove irrelevant prompts. Their presence does not require creating four documents for every task.

## Validate this package

From the repository root:

```sh
python3 scripts/validate_skill.py
```

Or point the validator at a skill directory from another working directory:

```sh
python3 ux-laws/scripts/validate_skill.py ux-laws
```

The validator checks required metadata, naming, local document links and heading anchors, reading routes, the complete 30-card catalog, bilingual concept-source links, code fences, and unfinished scaffold markers. It uses Python's standard library, performs no network requests, and does not install anything. Keep the checked package directory named `ux-laws`, matching its declared skill name.

It does not prove external URLs are current, validate every possible YAML/Markdown construct, assess deployed interface usability, or certify accessibility. Review the [behavioral verification scenarios](references/verification-scenarios.md) for meaningful guidance checks: navigation, ambiguous input, mobile targeting, dense dashboards, live output, canvas reordering, and offline audits.

For a reproducible discovery check using the CLI version tested for this package:

```sh
DISABLE_TELEMETRY=1 npx --yes skills@1.7.0 add . --list
```

Here, `--yes` belongs to `npx` and accepts downloading the CLI package. The skill command still uses `--list`, so no destination skill installation occurs. `DISABLE_TELEMETRY=1` applies to this diagnostic invocation only.

## Publishing and skills.sh discovery

The public repository has `SKILL.md` at its root, with the required `name` and `description`. Its name is `ux-laws`; it is not marked internal. The root layout is a supported discovery path, and the README accompanies the full reference package. No package manifest, build step, or application deployment is needed for this layout.

According to the [skills.sh FAQ](https://skills.sh/docs/faq), directory visibility is populated through recorded installations using the CLI. Public GitHub hosting enables discovery; `--list` confirms it. A real `npx skills add lestradavaz/ux-laws --skill ux-laws` installation is the next step for installation-based directory tracking. This package does not promise an immediate listing, ranking, audit status, or indexing time.

The [official telemetry documentation](https://skills.sh/docs/cli#telemetry) explains recording and opt-out. Diagnostics here disable telemetry. An installation with telemetry disabled should not be relied on to register an installation-based listing.

For future updates: publish the complete package to the public branch, validate locally, confirm public `--list` discovery, and let users update through the CLI. Directory appearance remains a separate service outcome from a successful package validation or install.

## Troubleshooting

| Symptom | Check or next action |
| --- | --- |
| `No skills found` | Run public `--list`; confirm `SKILL.md` is committed on the fetched branch with valid required frontmatter and exact filename case. |
| CLI fails before discovery | Check Node.js against the current CLI package requirements, npm/npx availability, Git, and access to the public repository. |
| Listed but unavailable in the project | Check `npx skills list`, selected destination and scope, installation location, and the environment's loading/reload behavior. |
| Works in one project only | Project scope is local to that project; choose global scope when appropriate. |
| References cannot be opened | Check that the complete skill directory was installed, preserving relative paths; avoid single-file downloads. |
| Local validator reports folder mismatch | Check a directory named `ux-laws`, or clone the repository using its default directory name. |
| Sources cannot be reached | Use dated local references for supported general practice; record uncertainty for requirements needing current verification. |
| Expected benefit has no measurements | Treat the behavioral benefit as a hypothesis; choose proportionate runtime or participant checks. |
| Not visible on skills.sh after publishing | Verify public discovery and an actual recorded install; `--list`, disabled telemetry, and a README alone do not establish listing. |

For reproducible package problems, use the [repository issues](https://github.com/lestradavaz/ux-laws/issues). Include the command, CLI/runtime version, relevant platform, expected result, actual result, and non-sensitive reproduction details. Report an invocation or package issue separately from uncertainty about a product's own requirements.

## Maintenance and contributions

Keep the entrypoint focused on shared decisions and routing. Put deeper guidance in the relevant reference, preserve one authoritative location for substantive rules, and link rather than duplicate numerical requirements.

When proposing a change, identify the concrete task it improves, provide primary sources for factual or normative claims, distinguish source guidance from original recommendations, and preserve platform scope. Update consultation dates only for sources actually checked. Changes to the catalog should be intentional and accompanied by updates to its index and validator expectations.

Run structural validation after document changes. For substantive behavioral changes, evaluate relevant scenarios independently and revise only where results support a correction. New scripts need meaningful success/failure checks. Stylistic preferences alone do not justify additional universal rules.

## License and source provenance

The original documentation, examples, templates, and validator in this repository are distributed under the [MIT License](LICENSE).

Linked external works retain their own ownership and terms. This package contains original applications and short conceptual syntheses; it is not a republication of the full source website or official standards, and it claims no endorsement by their authors. See [sources and provenance](references/sources.md) for the organizing framework, research, accessibility standards, and platform guidance.
