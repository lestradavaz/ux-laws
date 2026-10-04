# Postel’s Law

## Principle and evidence

Support reasonable variation in human input while producing clear, predictable outcomes. Define accepted input explicitly; tolerance is not permission to guess security-sensitive meaning.

The catalog adapts a networking robustness maxim to interfaces. That adaptation is a heuristic. Modern IAB guidance documents hazards of overly permissive interpretation in protocols; distinguish human-friendly input handling from strict authorization, protocol validation, and data-integrity requirements.

## Observable triggers

- A form rejects harmless spacing or familiar input formats.
- An import silently changes ambiguous values.
- Client-side tolerance differs from server interpretation or identifier matching.

## Implementation actions

1. Define supported variations by field and context. Normalize only transformations that preserve intended meaning under the domain contract; keep the original input available when correction or audit requires it.
2. Explain expected formats before entry and give actionable errors near the affected field. Preserve entered data when validation fails.
3. Ask for clarification when interpretation is ambiguous, such as locale-dependent dates or decimal separators. Show a parsed preview for imports and consequential normalized values.
4. Keep credentials, authorization scope, account identity, payment amounts, signatures, and machine protocols subject to their explicit rules. Do not apply broad trimming, case-folding, truncation, or fallback interpretation without an established contract.
5. Align client and server validation, document canonical output, and test malformed, oversized, conflicting, and unsupported input. Flexibility should be a supported feature with bounded behavior.

## Example

A date import accepts an explicitly chosen source format and previews parsed dates before committing. It does not guess whether 03/04 means March 4 or April 3. A human-readable phone input accepts supported separators, while account identifiers and secrets follow their separate exact-match contracts.

## Counterexample

A login implementation strips spaces, lowercases every credential, and truncates long values to make input forgiving. Users can no longer rely on their entered secret, and different layers may identify different accounts.

## Limits and conflicts

Silently accepting malformed machine input can create inconsistent implementations and security failures. Domain-specific identity and locale rules matter. Helpful recovery may mean rejecting input clearly rather than accepting it. Accessibility also requires perceivable validation and correction support. Keep normalization decisions explicit, testable, and shared across trusted layers.

## Acceptance checks

- Every normalization rule preserves meaning under a documented field contract.
- Ambiguous input requests clarification rather than silently guessing.
- Client and server agree on accepted values and canonical output.
- Security-sensitive fields, malformed input, and boundary cases have been checked separately.

## Sources and related guidance

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/postels-law/), [Spanish](https://lawsofux.com/es/ley-de-postel/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

Additional primary guidance: [IAB RFC 9413 — Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413.html), an informational protocol document; use its caution contextually rather than treating it as a form-design standard.

[Tesler’s law](teslers-law.md) · [Mental models](mental-model.md) · [Cognitive load](cognitive-load.md) · [Accessibility](../foundations/accessibility.md).

