# Miller’s Law

## Principle and evidence

Immediate memory is constrained, and meaningful grouping changes how information can be retained. Reduce unnecessary recall and organize material around recognizable units.

The catalog discusses Miller's historic memory work and warns against using its famous number as a design limit. A laboratory memory-span result is not a maximum for navigation items, table rows, form fields, or visible options. Modern capacity estimates and task conditions differ; do not turn any one estimate into a universal UI quota.

## Observable triggers

- A design decision is justified solely by a maximum menu-item count.
- Users must remember several values, instructions, or choices between views.
- An unstructured sequence is difficult to retain or repeat correctly.

## Implementation actions

1. Identify whether the task requires recall at all. Visible alternatives, familiar categories, and searchable content differ from retaining an unfamiliar sequence in memory.
2. Externalize relevant information: persistent summaries, selected-item lists, comparison tables, or contextual instructions. Keep information visible when it is needed, not only when it was first entered.
3. Create chunks that match domain knowledge. Validate the grouping with the audience; arbitrary boxes or evenly sized sections do not create meaningful cognitive units.
4. Support paste, lookup, and transfer rather than forcing manual re-entry. Preserve exact data where normalization could alter meaning.
5. Evaluate the complete task with realistic interruption and expertise levels. Choose menu depth, grouping, and density from search and completion evidence instead of the historic number.

## Example

A configuration wizard initially asks users to remember a server address and several identifiers from a prior screen. Keep a summary panel visible, copy validated values forward, and provide a review page. Do not reduce the visible server list to a supposedly correct count when searchable access to all servers supports recognition.

## Counterexample

A settings menu is split into several vague submenus solely to keep every level below a magic number. Users now remember the path, open the wrong branch, and lose the context needed to choose.

## Limits and conflicts

Memory burden is affected by familiarity, meaningfulness, modality, interruption, and the work performed on the retained information. A visible long list may be easier than a short hidden hierarchy. Pair memory considerations with Hick and task analysis rather than treating them as interchangeable explanations. Retained sensitive information also needs appropriate privacy controls.

## Acceptance checks

- No option-count restriction is justified solely by the historic memory number.
- Task-critical information remains available across navigation and interruption.
- Groups reflect audience-recognizable meaning rather than arbitrary counts.
- Users can complete the task without unnecessary memorization or re-entry.

## Sources and related guidance

Primary scholarly material, consulted 2026-10-04: [Miller (1956), original paper reproduced by York University](https://psychclassics.yorku.ca/Miller/), separates absolute judgment from immediate memory and discusses recoding into chunks. [Cowan (2001), reconsideration of storage capacity (author-hosted PDF)](https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf), emphasizes carefully defined experimental conditions and the identification of independent chunks. Neither source sets a quota for visible menu items.

Laws of UX publisher guidance, consulted 2026-10-04: [English](https://lawsofux.com/millers-law/), [Spanish](https://lawsofux.com/es/ley-de-miller/). The summary above is a conceptual synthesis; implementation actions and examples are contextual recommendations, not empirical effect-size claims.

[Working memory](working-memory.md) · [Chunking](chunking.md) · [Hick’s law](hick-law.md) · [Accessibility](../foundations/accessibility.md).
