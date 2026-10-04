# Jakob’s Law

## Principle and evidence

People transfer expectations from products and environments they already know. Use established interaction conventions when they fit the audience and task; explain necessary departures.

Jakob's law is a usability heuristic about transferred expectations, not a statistical claim that all users know the same products. Familiarity depends on platform, culture, domain, experience, and assistive technology.

## Observable triggers

- A familiar-looking control behaves differently from its apparent role.
- Common actions use novel labels, gestures, or shortcuts without a clear benefit.
- A redesign changes navigation and workflow while preserving the old visual cues.

## Implementation actions

1. Inspect the project's existing conventions, platform patterns, and domain tools used by the intended audience. Record which expectations matter to the requested task.
2. Match labels, placement, feedback, and recovery behavior to those expectations where appropriate. Reuse established components when their semantics and input support fit.
3. Make mode changes and novel consequences explicit. A button that affects live output must communicate that scope rather than resembling an ordinary local preview control.
4. Introduce major departures with clear signifiers, migration guidance, and a reversible learning path when feasible. Keep shortcuts and saved workflows compatible unless a concrete requirement warrants change.
5. Test first use and learned use separately. Ask users to predict a control's result before activation, then observe whether the actual behavior matches.

## Example

A desktop editor uses standard selection, undo, and copy conventions. Its Publish command is domain-specific, so it names the destination and shows the live consequence before commitment. A redesign keeps keyboard shortcuts stable while improving discoverability through a command palette.

## Counterexample

A mobile close icon saves and sends a draft because the team wants a novel one-tap workflow. Users expect it to dismiss the view and discover the transmission only afterward.

## Limits and conflicts

Familiar patterns can also be inaccessible, misleading, or unsuitable for a new task. Convention supports predictability rather than copying every visual detail. Experts may expect specialized behavior that differs from consumer software. Resolve conflicts by grounding in the actual audience and domain, then document and test deliberate deviations.

## Acceptance checks

- Common controls produce the expected result on supported platforms.
- Novel or consequential behavior has a visible, understandable signifier before activation.
- Existing learned shortcuts and workflows have been checked for regression.
- First-use evaluation identifies prediction errors and their consequences.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/jakobs-law/), [Spanish](https://lawsofux.com/es/ley-de-jakob/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Mental models](mental-model.md) · [Active user](active-user-paradox.md) · [Similarity](similarity.md) · [Accessibility](../foundations/accessibility.md).

