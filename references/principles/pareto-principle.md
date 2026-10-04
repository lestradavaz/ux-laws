# Pareto Principle

## Principle and evidence

Contribution is often uneven: some tasks, defects, or interactions account for a disproportionate share of impact. Use evidence to prioritize work while protecting essential needs.

Pareto is a prioritization heuristic, not a universal numerical distribution. The catalog's familiar ratio illustrates imbalance. Measure the actual product and population rather than assuming that a fixed minority of features produces a fixed majority of value.

## Observable triggers

- A team has many possible UX changes with limited time.
- A small cluster of errors dominates support or abandonment.
- Low-frequency workflows are proposed for removal because aggregate usage is small.

## Implementation actions

1. Define impact in terms of user outcomes: completion, error severity, time, accessibility barriers, or recovery cost. Include exposure and consequence rather than clicks alone.
2. Segment findings by role, ability, device, context, and lifecycle stage where evidence supports it. An aggregate can hide a severe barrier for a smaller group.
3. Prioritize high-impact, well-supported improvements, but separately retain safety, accessibility, contractual, and essential specialist needs as constraints.
4. Choose bounded improvements that address the responsible cause. Check whether a highly visible issue originates in shared validation, state handling, or terminology before patching many screens.
5. After release, compare relevant outcomes and watch for displaced effort or regressions in less common tasks. Revise priorities when new evidence changes the distribution.

## Example

Most support requests concern failed imports, so the team improves format guidance and file-level recovery first. It also fixes a keyboard barrier affecting a less frequently used administration flow because that barrier prevents an entire user group from completing an essential task. Prioritization includes both reach and severity.

## Counterexample

An export format used by few customers is removed under an assumed ratio. Those customers require the format for regulatory delivery, so a low aggregate count conceals a mission-critical capability.

## Limits and conflicts

Recorded usage reflects what the interface makes possible and discoverable. An inaccessible feature may appear unimportant because people cannot use it. Rare events can have large consequences. Business revenue, task frequency, and user value are different signals; report which one informs the decision. Avoid treating population size as permission to exclude.

## Acceptance checks

- Priorities cite observed distribution, impact, and confidence rather than an assumed ratio.
- Accessibility and high-consequence rare workflows are explicitly considered.
- A proposed removal has evidence about affected users and alternatives.
- Post-change checks include user outcomes and regression in protected workflows.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/pareto-principle/), [Spanish](https://lawsofux.com/es/principio-de-pareto/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Cognitive bias](cognitive-bias.md) · [Tesler’s law](teslers-law.md) · [Occam’s razor](occams-razor.md) · [Accessibility](../foundations/accessibility.md).

