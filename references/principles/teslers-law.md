# Tesler’s Law

## Principle and evidence

Some complexity belongs to the domain and must be handled somewhere. Move reliable mechanical work into the system while leaving users informed and in control of meaningful decisions.

Tesler's law is a design maxim about allocating complexity, not a physical conservation equation. A product may remove unnecessary requirements or change the underlying process. Use the principle to inspect where remaining work, uncertainty, and recovery responsibility go.

## Observable triggers

- A simple interface conceals unpredictable automation.
- Users repeat calculations, data transfer, or reconciliation that software could handle.
- A redesign removes controls but shifts effort into workarounds or support.

## Implementation actions

1. Map the task's unavoidable decisions, rules, dependencies, and failure modes. Identify what can be automated reliably and what requires judgment or domain accountability.
2. Implement dependable mechanical support: calculations, validation, data carry-forward, and compatible defaults. Expose assumptions and source information when users need to verify them.
3. Preserve meaningful override, correction, and undo where possible. For uncertain automation, show the proposed result and confidence or limitations rather than silently committing.
4. Give complex professional tasks an appropriate advanced path. Progressive disclosure should reduce beginner effort without making expert capability inaccessible or context-free.
5. Account for complexity beyond the screen: backend state, permissions, migrations, error recovery, maintenance, and accessibility. Evaluate the whole workflow rather than the number of exposed settings.

## Example

A shipping form calculates supported delivery options from destination and package information. It shows the assumptions and lets users correct the package dimensions. A specialist can choose a supported alternative service. When the carrier lookup fails, the form preserves input and explains which part remains unresolved.

## Counterexample

A scheduling tool has one Auto-plan button but silently chooses priorities, deadlines, and resource conflicts. Users must export data to understand its choices and cannot revise one constraint without rerunning everything.

## Limits and conflicts

Automation can create errors at scale and demand more difficult verification. Some domains require explicit approval or traceability. Complexity is not always undesirable: experts need meaningful controls, and meaningful learning can improve long-term efficiency. Pair with Occam to remove redundant process before deciding who should carry necessary work.

## Acceptance checks

- Mechanical work is handled reliably without concealing consequential assumptions.
- Users can inspect, correct, or override results where the domain permits.
- Errors preserve work and explain remaining responsibility.
- The simplified path and expert path both complete required tasks without external workarounds.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/teslers-law/), [Spanish](https://lawsofux.com/es/ley-de-tesler/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Occam’s razor](occams-razor.md) · [Cognitive load](cognitive-load.md) · [Postel’s law](postels-law.md) · [Accessibility](../foundations/accessibility.md).

