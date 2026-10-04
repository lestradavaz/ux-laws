# Navigation and search

Use when people must locate a destination, recover their place, or retrieve an item from a collection. Start with tasks and vocabulary: a known-item lookup, exploratory browsing, and jumping to a command require different affordances. Read [interaction](../foundations/interaction.md) for input behavior and [content and localization](../foundations/content-and-localization.md) for labels.

## Decide the navigation model

Identify what stays stable: top-level destinations, hierarchy, recently visited items, and the current workspace. Preserve established labels and placement unless observed task failures justify change. A sidebar may be appropriate for a dense professional tool; a short primary navigation may suit a small public site. Do not apply an arbitrary item cap from [Miller's Law](../principles/miller-law.md). Meaningful grouping supports recognition without hiding needed destinations.

Use links for destinations and buttons for actions. Site navigation usually needs ordinary links with disclosure buttons for nested sections, rather than an application menubar with its more elaborate interaction model. APG distinguishes the menubar widget from typical site navigation; choose semantics from behavior, not visual appearance. [APG menubar guidance](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/).

Represent current location through a visible selected state, a page title, and hierarchy where relevant. Web landmarks help users find major page regions; name repeated navigation landmarks when they have different purposes. [WAI page regions](https://www.w3.org/WAI/tutorials/page-structure/regions/). For application routing, preserve useful query/filter state across Back, item-detail visits, and reload when consistent with the product's existing persistence policy. Do not introduce new durable storage merely to fix a navigation label.

## Make search states explicit

Keep query text, active filters, selected suggestion, results, and request status separate. A small state model can prevent stale responses:

```text
query_changed -> request(query, sequence)
response(sequence): apply only if sequence == latest_request
states: idle | searching | results | no_matches | unavailable
```

This illustrates behavior, not a required architecture. Cancel stale requests when supported; ignoring stale results still matters if cancellation races. Retain the last usable result set during refresh when it helps orientation, but mark it as updating. A blank area should not ambiguously mean loading, no matches, permission denied, or failure.

For suggestions, decide whether arbitrary text is allowed or a listed entity is required. Preserve typing and standard text editing. A web combobox requires a coherent popup, focus, and selection model; copying only ARIA roles cannot supply its interactions. [APG combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/). Do not commit the first suggestion just because a delayed response arrived. Let a visible result identify the matched item and any disambiguating context.

No-results guidance should expose useful recovery: remove an active filter, revise the query, or browse another category. Avoid suggesting unavailable actions. Show result scope, especially when search excludes archived content or other workspaces. Searching commands should state whether activating a result navigates, previews, or immediately executes.

## Example and counterexample

An inventory tool keeps category and sort position when a user opens an item and returns. Search for "adapter" identifies name, connector type, and warehouse; empty results explain that an "In stock" filter is active. Counterexample: every return resets to the first row, the selected category exists only as color, and a delayed response for "ad" overwrites results for "adapter".

Relevant principles: [Jakob's Law](../principles/jakob-law.md), [mental models](../principles/mental-model.md), [Hick's Law](../principles/hick-law.md), [working memory](../principles/working-memory.md), and [cognitive load](../principles/cognitive-load.md).

## Acceptance checks

- Complete a known-item lookup and an exploratory task without memorizing hidden categories.
- Verify location, selected filters, and return behavior with keyboard and the target assistive technology.
- Test reversed response order, slow search, no matches, and service failure; the active query remains authoritative.
- Check long labels, narrow layouts, and duplicate item names. Scope and identity remain understandable.
- Measure lookup success or recovery effort against the task baseline; fewer clicks alone do not establish improvement. Use [evaluation and metrics](../foundations/evaluation-and-metrics.md).

Sources consulted: 2026-10-04. APG and WAI tutorials provide informative web implementation guidance; apply normative requirements through [accessibility](../foundations/accessibility.md).
