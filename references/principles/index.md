# Principle catalog

Use this index when an observed UI problem needs a behavioral explanation or implementation direction. The catalog covers all 30 concepts listed in the [Spanish Laws of UX collection](https://lawsofux.com/es/), checked against the publisher's English pages on 2026-10-04. Each card links both language versions.

## How to use a card

1. Start with the user's task, affected audience, supported input modes, current behavior, and actual evidence. Identify a symptom below.
2. Read the smallest relevant set of cards, including their limits. Select actions and acceptance checks proportionally to the requested change; not every listed action is needed for every use.
3. Treat a card's explanation as a hypothesis about the local interface. Record the observed trigger, proposed change, expected outcome, and the check that could disconfirm it.
4. Use participants only when available and authorized. Without participant evidence, label inferred mental models and expected behavioral benefits as hypotheses. Perform feasible inspection or scenario checks, then propose appropriate follow-up; a small fix need not wait for a research program.
5. Resolve conflicts through task consequences, accessibility, informed control, and prevention of serious errors. Then consider effort, efficiency, established conventions, and appearance. Explain any deliberate tradeoff.
6. Verify behavior on representative content, relevant states, and input modes. Report what was checked and what remains uncertain; a principle label alone is not proof.

These concepts are descriptive models, psychological constructs, or design heuristics. They are not legal requirements, universal numerical limits, or substitutes for domain expertise. Normative accessibility requirements and their scope belong in [Accessibility](../foundations/accessibility.md).

## Route by observed problem

| Observed problem | Start here | Add when relevant |
| --- | --- | --- |
| People hesitate among similar options | [Choice overload](choice-overload.md) | [Hick](hick-law.md), [Cognitive load](cognitive-load.md) |
| Tiny controls, long pointer travel, accidental activation | [Fitts](fitts-law.md) | [Proximity](proximity.md), [Jakob](jakob-law.md) |
| Users cannot tell what belongs together | [Proximity](proximity.md) | [Common region](common-region.md), [Chunking](chunking.md) |
| Appearance implies the wrong behavior or status | [Similarity](similarity.md) | [Jakob](jakob-law.md), [Mental model](mental-model.md) |
| A graph, workflow, or icon has ambiguous meaning | [Uniform connectedness](uniform-connectedness.md) | [Prägnanz](pragnanz.md), [Mental model](mental-model.md) |
| Important warnings or changes go unnoticed | [Selective attention](selective-attention.md) | [Von Restorff](von-restorff-effect.md), [Cognitive load](cognitive-load.md) |
| Users remember or re-enter values across views | [Working memory](working-memory.md) | [Miller](miller-law.md), [Chunking](chunking.md) |
| Familiar controls or consequences surprise users | [Mental model](mental-model.md) | [Jakob](jakob-law.md), [Active user](active-user-paradox.md) |
| Users begin immediately and miss help | [Active user](active-user-paradox.md) | [Flow](flow.md), [Cognitive load](cognitive-load.md) |
| Work is interrupted, slow, or loses context | [Flow](flow.md) | [Doherty](doherty-threshold.md), [Working memory](working-memory.md) |
| Progress or remaining effort is unclear | [Goal gradient](goal-gradient-effect.md) | [Doherty](doherty-threshold.md), [Zeigarnik](zeigarnik-effect.md) |
| Abandoned or interrupted work cannot be resumed | [Zeigarnik](zeigarnik-effect.md) | [Working memory](working-memory.md), [Flow](flow.md) |
| Required work expands into needless steps | [Parkinson](parkinsons-law.md) | [Occam](occams-razor.md), [Tesler](teslers-law.md) |
| Harmless input variation causes errors | [Postel](postels-law.md) | [Tesler](teslers-law.md), [Mental model](mental-model.md) |
| Simplification hides assumptions or creates workarounds | [Tesler](teslers-law.md) | [Occam](occams-razor.md), [Cognitive load](cognitive-load.md) |
| Instructions or sequences are hard to follow | [Serial position](serial-position-effect.md) | [Chunking](chunking.md), [Working memory](working-memory.md) |
| Strong opinions or attractive visuals obscure failures | [Cognitive bias](cognitive-bias.md) | [Aesthetic–usability](aesthetic-usability-effect.md), [Pareto](pareto-principle.md) |
| Success, cancellation, or failure lacks closure | [Peak–end](peak-end-rule.md) | [Doherty](doherty-threshold.md), [Zeigarnik](zeigarnik-effect.md) |
| Many improvements compete for limited effort | [Pareto](pareto-principle.md) | [Cognitive bias](cognitive-bias.md), [Occam](occams-razor.md) |

## Complete catalog by family

### Decision and complexity

- [Choice Overload](choice-overload.md): support narrowing and meaningful comparison.
- [Hick's Law](hick-law.md): reduce interpretation cost in decisions.
- [Cognitive Load](cognitive-load.md): distinguish necessary effort from interface-induced work.
- [Tesler's Law](teslers-law.md): allocate necessary complexity with visibility and control.
- [Occam's Razor](occams-razor.md): compare adequate solutions by their assumptions.
- [Pareto Principle](pareto-principle.md): prioritize measured impact while protecting essential needs.
- [Parkinson's Law](parkinsons-law.md): prevent unnecessary task expansion without arbitrary pressure.
- [Postel's Law](postels-law.md): bound input flexibility and preserve secure meaning.

### Learning and expectations

- [Jakob's Law](jakob-law.md): use audience and platform conventions.
- [Mental Model](mental-model.md): make objects, scope, and consequences predictable.
- [Paradox of the Active User](active-user-paradox.md): support doing, contextual learning, and reference.

### Memory and information organization

- [Chunking](chunking.md): build meaningful units for scanning and understanding.
- [Miller's Law](miller-law.md): reduce recall burden without a universal menu quota.
- [Working Memory](working-memory.md): externalize relevant context and comparisons.
- [Serial Position Effect](serial-position-effect.md): organize sequences without memory-dependent safeguards.

### Perception and relationships

- [Law of Common Region](common-region.md): communicate group and action scope.
- [Law of Proximity](proximity.md): express ownership through spacing.
- [Law of Prägnanz](pragnanz.md): reduce ambiguity while preserving useful distinctions.
- [Law of Similarity](similarity.md): align appearance with equivalent roles and states.
- [Law of Uniform Connectedness](uniform-connectedness.md): communicate real connections and dependencies.
- [Von Restorff Effect](von-restorff-effect.md): reserve salience for meaningful priority.
- [Selective Attention](selective-attention.md): place relevant signals in the task's attention path.

### Interaction and continuity

- [Fitts's Law](fitts-law.md): inspect actual hit targets and travel for each modality.
- [Doherty Threshold](doherty-threshold.md): provide responsive, truthful feedback.
- [Flow](flow.md): protect focused work while supporting safe interruption and exit.

### Motivation and evaluation

- [Goal-Gradient Effect](goal-gradient-effect.md): show honest progress and remaining effort.
- [Zeigarnik Effect](zeigarnik-effect.md): support resumption, abandonment, and closure.
- [Peak–End Rule](peak-end-rule.md): improve stressful moments and factual endings.
- [Aesthetic–Usability Effect](aesthetic-usability-effect.md): separate perceived ease from task performance.
- [Cognitive Bias](cognitive-bias.md): examine framing and disconfirm design assumptions.

## Guard against common misapplications

- A memory estimate is not a maximum navigation count. Use recognition, meaningful grouping, and task evidence.
- A historical responsiveness threshold is not a universal latency promise. Define interaction-specific budgets and measure them.
- Progress must reflect actual work. Use phases or indeterminate feedback when exact completion is unknown; return completed results promptly.
- Forgiving human input must follow documented meaning-preserving rules. Ambiguous dates, identifiers, secrets, permissions, money, and machine protocols require explicit domain contracts.
- Frequency and conversion are not the whole user outcome. Consider excluded users, rare serious failures, understanding, and recovery.
- Minimalism and polish must preserve labels, state, scope, necessary comparisons, and control.
