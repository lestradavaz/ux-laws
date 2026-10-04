# Law of Uniform Connectedness

## Principle and evidence

Visible connections can make separate elements appear to share a relationship. Draw connections only when they reflect actual structure, sequence, dependency, or ownership.

Uniform connectedness is a perceptual grouping principle. Its application to UI helps explain diagrams and connected controls, but a visual line is not self-explanatory: direction, meaning, and valid endpoints must be understood in context.

## Observable triggers

- Users cannot determine which output belongs to which source.
- A workflow or dependency diagram uses crossing or ambiguous lines.
- Decorative connectors imply a sequence or relationship the system does not enforce.

## Implementation actions

1. Define the relationship before choosing its encoding. Distinguish sequence, data transfer, dependency, and group membership using clear labels or a legend when necessary.
2. Attach lines to unambiguous endpoints. Use direction cues when order matters and preserve them while moving, zooming, selecting, or updating nodes.
3. Use connected styling for linked controls only when their values or behavior are actually linked. Explain how linking can be changed and what happens when it is removed.
4. Provide a structured text or table representation for important relationships. Make connection creation, selection, and deletion available through suitable alternatives to precise dragging.
5. Handle invalid, hidden, collapsed, and off-screen endpoints explicitly. Keep relationship identity stable during layout recalculation so users can follow the same connection.

## Example

An automation editor connects a trigger to actions with directed, labeled edges. Selecting an edge exposes its condition and offers Delete connection, distinct from deleting a node. A relationship list identifies source, destination, and condition, allowing keyboard review and operation without tracing the visual graph.

## Counterexample

A timeline draws a continuous line through optional setup tasks. Users assume each task must be completed in order, though the product supports independent execution and skipping several tasks.

## Limits and conflicts

Connections can dominate proximity and create misleading grouping. Dense graphs may need filtering, bundling, or alternate views, but hidden edges must not conceal material dependencies. Visual readability does not prove workflow correctness. For a process with branching or failure, represent those states honestly rather than simplifying them into one unqualified success path.

## Acceptance checks

- Users can explain each important connection's meaning and direction.
- Moving, zooming, collapsing, and updating preserve correct endpoints.
- Important relationships are available through an accessible structured alternative.
- Removing or changing a connection has an explicit scope and recoverable outcome where feasible.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/law-of-uniform-connectedness/), [Spanish](https://lawsofux.com/es/ley-de-conectividad-uniforme/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Common region](common-region.md) · [Prägnanz](pragnanz.md) · [Mental models](mental-model.md) · [Accessibility](../foundations/accessibility.md).

