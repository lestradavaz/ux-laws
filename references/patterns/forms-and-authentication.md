# Forms and authentication

Use for data entry, account access, verification, submissions, and editing records. Start by identifying what information the task actually needs, what the service accepts, and what must remain exact. Read [content and localization](../foundations/content-and-localization.md) before assuming universal name, address, telephone, or date formats.

## Reduce avoidable effort

Give fields persistent labels, useful examples, and constraints before the user commits. Placeholder text is not a substitute for a label. Group related inputs by task meaning; do not split a simple form into screens solely to make each screen look sparse. A multistep flow is useful when grouping reflects work stages or conditional questions. Preserve completed input when moving backward.

Use appropriate platform input types and autofill support where available. Let password managers and paste work. Web WCAG 2.2 Accessible Authentication (Minimum), Level AA, limits authentication steps that require cognitive-function tests unless its specified alternatives or assistance conditions apply; inspect the exact criterion and exceptions rather than treating all verification as prohibited. [W3C authentication explanation](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html).

Do not invent broad normalization. Trimming accidental surrounding whitespace may be safe for some fields; stripping punctuation from legal identifiers, rewriting names, or altering passwords may corrupt intent. [Postel's Law](../principles/postels-law.md) should inform tolerant parsing only where domain semantics remain intact. Preserve the entered value and explain the accepted interpretation when ambiguity matters.

## Separate validation from submission

Distinguish editing, validation, pending submission, rejection, and completion. Delay intrusive error messages while the user is still constructing a valid value; validate earlier when it prevents costly work, and again at submission. Server validation remains necessary even if local validation succeeds. WAI guidance supports clear error identification, correction suggestions, and error summaries linked to affected fields. [WAI form validation](https://www.w3.org/WAI/tutorials/forms/validation/).

```text
editing -> submitting(submission_id)
submitting -> rejected(field_errors, form_error) | accepted(receipt)
transport_unknown -> check_existing_submission | safe_retry
```

A transport timeout does not prove rejection. For payments, orders, invitations, or other consequential submissions, use the existing service's deduplication or status mechanism if available; never invent a successful receipt or blindly retry. Retain non-sensitive input on recoverable failure. Handle sensitive fields according to the product's security policy, and explain when re-entry is needed.

Errors should say what happened, identify the field or action, and give an achievable next step. For authentication, do not disclose account existence or other sensitive details beyond the established service policy. A generic credential error can still offer usable recovery without identifying which credential was wrong. Recovery links need visible names and coherent return paths.

Do not disable Submit merely because a pristine form is incomplete if that hides why completion is impossible. When a disabled control is appropriate, explain unmet prerequisites independently. On submit failure, place focus at an error summary or suitable field according to the form's size and existing behavior; routine validation should not repeatedly steal focus during typing.

## Example and counterexample

A reservation form explains its date format, preserves passenger details after a seat becomes unavailable, and lets the user choose another seat before retrying. The final confirmation shows a reservation identifier from the service. Counterexample: one invalid phone field clears the entire form, paste is blocked in verification, and a spinner becomes "Booked" after a local timer despite no acknowledgment.

Related principles: [cognitive load](../principles/cognitive-load.md), [working memory](../principles/working-memory.md), [Tesler's Law](../principles/teslers-law.md), [mental models](../principles/mental-model.md), and [Hick's Law](../principles/hick-law.md). Read [states and recovery](../foundations/states-and-recovery.md) for interruption handling.

## Acceptance checks

- Complete the form with keyboard, relevant assistive technology, autofill, and paste.
- Verify error-to-field association, focus after rejection, and preservation of useful input.
- Test invalid values, expired verification, offline submission, timeout with an unknown outcome, and repeated activation.
- Check international examples and long errors; no unsupported format assumption becomes a hidden requirement.
- Confirm success requires the appropriate service acknowledgment and that recovery follows the actual product contract.

Sources consulted: 2026-10-04. Apply exact normative requirements through [accessibility](../foundations/accessibility.md); WAI tutorials and Understanding pages explain implementation but are not themselves conformance criteria.
