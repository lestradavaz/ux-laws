# Working Memory

## Principle and evidence

Holding and manipulating temporary information requires limited cognitive resources. Let the interface retain task context and support recognition instead of unnecessary recall.

Working memory is a cognitive construct with multiple models. The catalog presents capacity and duration estimates as explanatory shorthand; they are not universal limits or countdowns for interface design. Task complexity, familiarity, ability, interference, and external aids change demands.

## Observable triggers

- Users compare values by navigating back and forth.
- Instructions disappear before the required action.
- Interruptions or session changes erase context and force reconstruction.

## Implementation actions

1. Map which facts a user needs at each decision. Keep relevant earlier choices, object identity, units, and constraints visible or readily inspectable when they become necessary.
2. Use side-by-side comparison, selected-item summaries, history, and breadcrumbs where they support the task. Present differences explicitly rather than asking users to mentally compute them.
3. Carry verified values across steps and preserve drafts, filters, and selection according to product expectations. Show which information was retained and what needs reconfirmation.
4. Support clipboard and lookup workflows without arbitrary re-entry. Handle sensitive values with appropriate visibility and persistence rules rather than retaining everything indiscriminately.
5. Test realistic interruptions and return paths. Observe reconstruction effort, mistaken comparisons, forgotten conditions, and repeated navigation; choose the smallest support that removes the actual burden.

## Example

A procurement flow keeps selected products in a comparison table with identical attribute ordering and highlighted differences. Returning from a product detail preserves the shortlist and filters. The final review includes quantity, unit price, and delivery constraints so approval does not depend on remembering separate pages.

## Counterexample

A configuration tool splits mutually dependent values into separate wizard steps and removes the previous selection from view. Users repeatedly go back to check a value, lose edits, and make inconsistent choices.

## Limits and conflicts

Making all context persistent can create distraction and privacy exposure. Retain what is needed, organize it meaningfully, and provide control over saved state. Recognition works only when labels and representations are comprehensible. Dense professional workflows may need multiple values visible at once; minimalism can worsen memory burden. Do not use a capacity estimate to cap visible content.

## Acceptance checks

- Task-critical facts remain available at the decisions that require them.
- Returning after interruption restores enough context to continue safely.
- Comparison does not depend on retaining values from separate screens.
- Persistence avoids exposing sensitive information and clearly signals stale or reconfirmed data.

## Sources and related guidance

Primary scholarly material, consulted 2026-10-04: [Cowan (2001), reconsideration of storage capacity (author-hosted PDF)](https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf), distinguishes constrained capacity estimates from tasks using additional strategies and memory sources. [Miller (1956), original paper reproduced by York University](https://psychclassics.yorku.ca/Miller/), provides historical context for meaningful recoding. These accounts support investigating memory demands; interface guidance here is a contextual application, not a direct experimental result.

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/working-memory/), [Spanish](https://lawsofux.com/es/la-memoria-de-trabajo/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Miller’s law](miller-law.md) · [Chunking](chunking.md) · [Cognitive load](cognitive-load.md) · [Accessibility](../foundations/accessibility.md).
