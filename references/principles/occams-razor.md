# Occam’s Razor

## Principle and evidence

When plausible approaches serve the task equally well, prefer the one requiring fewer assumptions. Remove unnecessary complexity while preserving the information and controls needed for correct use.

Occam's razor is a reasoning principle, not an empirical usability law or an instruction to minimize pixels, clicks, or features. The important condition is comparable explanatory or functional adequacy; a simpler-looking solution may demand more inference from users.

## Observable triggers

- Several competing mechanisms solve the same interaction problem.
- An interface accumulates redundant status widgets, settings, or confirmation steps.
- A proposal relies on hidden assumptions about what users know or intend.

## Implementation actions

1. State the task and success conditions before comparing solutions. Include accessibility, errors, recovery, and required specialist use rather than judging only a default screenshot.
2. List assumptions for each approach: remembered values, inferred icon meanings, unstated defaults, automatic behavior, or platform dependencies.
3. Remove duplication and ornamental controls whose purpose is unsupported. Consolidate equivalent mechanisms when their scope and behavior are truly equivalent.
4. Retain necessary labels, explanations, and safeguards. Test the leaner solution with realistic content and failure states; fewer visible elements must not shift work into guessing.
5. Prefer the simplest implementation that meets the observed need and established project conventions. Record why retained complexity is necessary instead of adding speculative configurability.

## Example

A file upload screen has separate indicators for selecting, transferring, processing, and completion, plus a permanent spinner. Replace redundant indicators with one coherent status region that names the current phase and offers relevant recovery. Keep file-level errors and cancellation because users need them to understand partial failure.

## Counterexample

A designer removes labels and field errors to achieve a clean form. Users must guess formats, infer icon meanings, and retry blind submissions. The visual reduction adds assumptions rather than removing them.

## Limits and conflicts

Domain complexity and high-consequence decisions may require substantial visible detail. A single automatic action can hide more complexity than explicit controls. Pair with Tesler to determine who carries the remaining work. Existing conventions and compatibility can justify a less visually spare solution; preserving a learned workflow may be simpler for users than replacing it.

## Acceptance checks

- The chosen approach meets the same documented task and recovery requirements.
- Removed elements have no necessary informational or operational role.
- Users need fewer assumptions or fewer redundant actions after the change.
- Retained complexity has a concrete reason tied to use, safety, or compatibility.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/occams-razor/), [Spanish](https://lawsofux.com/es/la-navaja-de-occam/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Tesler’s law](teslers-law.md) · [Prägnanz](pragnanz.md) · [Cognitive load](cognitive-load.md) · [Accessibility](../foundations/accessibility.md).

