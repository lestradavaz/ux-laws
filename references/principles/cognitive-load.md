# Cognitive Load

## Principle and evidence

An interface consumes mental effort through understanding, remembering, deciding, and coordinating actions. Reduce effort that does not contribute to the user's goal while supporting the task's necessary complexity.

Cognitive load comes from psychological and instructional research. Its use here is an implementation heuristic. A crowded screenshot or an arbitrary element count does not measure workload; expertise, task difficulty, interruptions, and information quality all matter.

## Observable triggers

- Users must mentally calculate, translate terminology, or remember values across screens.
- Many independent status changes compete during one task.
- A streamlined interface has fewer controls but requires more inference or navigation.

## Implementation actions

1. Map the task's decisions and information dependencies. Distinguish work intrinsic to the domain from work caused by presentation, hidden state, or unnecessary repetition.
2. Keep context available: units, current object, selected scope, prior choices, and consequences. Let the system perform reliable calculations and show inputs or assumptions that users must verify.
3. Replace internal terminology with domain language, clear labels, and examples near unfamiliar inputs. Use progressive disclosure for infrequent details when the primary task stays understandable.
4. Group related information, remove competing decoration, and make current status explicit. Preserve comparison layouts for workflows that require several values at once.
5. Observe representative tasks with realistic interruptions. Track backtracking, errors, help requests, and perceived effort; investigate their cause before redesigning broadly.

## Example

A scheduling UI asks users to calculate whether several jobs fit before a deadline. Show a timeline with duration, dependencies, remaining capacity, and conflicts. Let users adjust the assumptions and retain a textual list of the same information. The improvement is reduced mental arithmetic and more visible consequences, not simply fewer rows.

## Counterexample

A control room hides all detailed readings behind individual popovers to make the dashboard look calm. Operators must memorize values across popovers to diagnose a fault, increasing actual workload.

## Limits and conflicts

Useful density is not automatically overload. Experts can benefit from persistent, information-rich interfaces. Automation may shift cognitive work into checking uncertain results. Resolve conflicts with Tesler by retaining control and explanations where decisions require judgment; prefer evidence from real tasks over aesthetic preference.

## Acceptance checks

- Users can identify current scope, state, and next action without reconstructing them.
- Necessary comparisons and calculations are visible or supported by the system.
- Reduced visual density does not increase backtracking or memory requirements.
- Observed workload findings distinguish task difficulty from interface-induced effort.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/cognitive-load/), [Spanish](https://lawsofux.com/es/carga-cognitiva/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Tesler’s law](teslers-law.md) · [Working memory](working-memory.md) · [Chunking](chunking.md) · [Accessibility](../foundations/accessibility.md).

