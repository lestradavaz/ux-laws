# Content, semantics, and localization

Read when changing labels, instructions, validation, dates, quantities, navigation vocabulary, or layouts that support multiple languages. Pair with [forms and authentication](../patterns/forms-and-authentication.md), [navigation and search](../patterns/navigation-and-search.md), and [accessibility](accessibility.md). Use [Postel's Law](../principles/postels-law.md) cautiously when accepting varied input: tolerance must not silently change meaning. Search terms: labels, plural, RTL, dates, currency, numbers, names, translation.

## Write for the user's decision

Use the product's established vocabulary for objects and actions. “Save draft,” “Send invitation,” and “Delete recording” reveal different consequences; “Continue” may be sufficient inside a clearly explained step but hides scope at a commitment point. Identify what the user needs to know before acting, what they can see after acting, and what can be deferred to help. Do not make internal architecture or implementation errors part of routine product copy.

Keep labels stable and match visible and accessible names. Distinguish neighboring commands with meaningful words, not icon shape alone. Write descriptions around the task and consequence; a settings toggle needs enough context to understand what enabled means. Avoid unexplained acronyms unless the audience and project evidence justify them; expert applications may use precise domain terms that a generic “simplification” would damage.

Errors should state the problem and actionable correction when known. “Choose an end date after the start date” is more useful than “Invalid.” If the service failed, say what was retained and how to recover. Avoid humor or celebratory copy around destructive actions, serious failure, billing, or access denial. Tone is contextual; clarity and truthful expectations take priority.

## Localize messages, not fragments

Use the project's localization system. Store complete meaningful messages with named variables and translator context. Avoid constructing sentences by joining translated fragments; grammar, agreement, and word order change by language. Handle plural categories using locale-aware rules rather than a universal singular/plural test. Labels, accessible names, errors, help, placeholders, notifications, and exported user-facing content belong in the same localization review.

Identify which elements are deliberately untranslated: identifiers, product names, protocol tokens, domain-specific symbols, or user content. Do not translate data values merely because surrounding UI is localized. Keep interpolation safe without destroying meaningful user text. Provide examples that demonstrate the expected format without replacing persistent labels.

Allow real text growth and shrinkage. Favor wrapping and flexible layout before arbitrary abbreviation. Check longest plausible labels, multiline errors, narrow windows, enlarged text, and scripts with different shaping or line-breaking behavior. Pseudolocalization catches layout assumptions but cannot prove that a translation is meaningful or culturally appropriate; use language review for that claim.

## Locale is not identity or timezone

Language, region, timezone, currency, measurement system, and date interpretation can differ. Establish which values come from user preference, task context, or device settings. Do not infer citizenship from language or location from a phone number. Preserve existing product policy unless the requested change includes it.

Format display using locale-aware libraries and typed values. Parse using an explicit input contract. A value such as `03/04/2026` is ambiguous without context; show an unambiguous format or a locale-aware date control with clear interpretation. For scheduling across regions, display the relevant timezone and distinguish an instant from a local calendar date. Test daylight-saving transitions and boundary dates when scheduling behavior is in scope. Avoid converting a date-only birthday into a timestamp and shifting its day across zones.

For numbers, specify decimal/grouping interpretation, units, precision, and rounding where the decision needs them. Distinguish display formatting from storage and calculation. Never silently reinterpret an ambiguous monetary amount. Show currency identity when multiple currencies can appear. For percentages, rates, and measurements, label the basis so a familiar numeral does not communicate the wrong quantity.

Support realistic names and addresses: spaces, diacritics, non-Latin scripts, differing order, and optional components. Ask only for fields the task needs. A single global address schema or restrictive ASCII name validation can reject legitimate users; a particular jurisdiction or delivery integration may justify constraints if clearly explained. Validate downstream limitations before promising broader support.

## Direction and cultural conventions

For web RTL content, set semantic direction with `dir`, separately from `lang`; use logical layout properties for content whose arrangement should follow direction. Isolate inserted mixed-direction names or identifiers as appropriate. W3C's [structural RTL guidance](https://www.w3.org/International/questions/qa-html-dir) and [bidi markup guidance](https://www.w3.org/International/questions/qa-bidi-controls) explain these boundaries. Native UIs need their equivalent platform direction and text-shaping support.

Mirror directional navigation when the meaning follows reading direction; do not blindly mirror logos, media playback symbols, physical diagrams, or domain charts. Test whether a timeline represents time, language progression, or physical movement before choosing its orientation. Check punctuation around embedded email addresses, codes, numbers, and user-generated text. Rendering and copy/paste should preserve correct identifiers, not merely look plausible.

Colors, gestures, icons, imagery, humor, and form conventions are not universally interpreted. Use established platform and local product conventions, and verify high-consequence differences with relevant users or specialists. Avoid inventing cultural generalizations from a language code. Preserve recognizability while allowing local context to change examples or wording.

## Acceptance example

A booking form displays local dates and the venue's timezone, accepts supported names with diacritics, keeps entered values after validation, and communicates the exact payment currency before confirmation. German labels wrap without hiding actions; Arabic layout and mixed-direction reservation codes remain readable; a screen reader receives the correct language and field names. The same stored booking yields consistent results when reopened under another locale. Tests distinguish translation quality, rendering correctness, and date/currency business rules rather than claiming one proves all three.

Sources consulted 2026-10-04. This guidance supplies implementation decisions; exact locale and jurisdiction requirements remain product-specific.
