# Sources, provenance, and maintenance

Consulted: **2026-10-04**. This is a review date, not a claim that every source was published or revised on that date. External pages can change independently of this package.

## Source hierarchy

| Material | Role | Authority and boundary |
| --- | --- | --- |
| [Laws of UX, Spanish](https://lawsofux.com/es/) and [English](https://lawsofux.com/) | Requested organizing framework: 30 concepts | Explanations and recommendations; not a universal specification or proof of a design's usability |
| Individual concept pages | Concept origin, interpretation, caveats | Each local [principle card](principles/index.md) links its exact Spanish and English pages |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Web accessibility success criteria | Distinguish normative criteria, levels, exceptions, and conformance scope from implementation advice |
| [WCAG2ICT](https://www.w3.org/TR/wcag2ict/) | Applying accessibility concepts beyond web | Informative guidance for non-web software and documents; does not itself create new requirements |
| [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) and [Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) | Web widget behavior and semantics | Informative patterns; implementing an example still needs interoperability and task testing |
| [WAI tutorials](https://www.w3.org/WAI/tutorials/) | Practical accessibility implementation | Supporting techniques, not a substitute for the applicable criterion or runtime evidence |
| [Apple HIG accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) | Apple platform recommendations | Check the actual platform and distinguish default from minimum values; source can require JavaScript |
| [Apple HIG documentation data](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/accessibility.json) | Official structured representation of the HIG page | Useful when the presentation layer is unavailable; endpoint format may change |
| [Windows accessibility overview](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview) | Windows implementation guidance | Framework-provided support does not establish a complete application's accessibility |
| [Windows touch interactions](https://learn.microsoft.com/en-us/windows/apps/develop/input/touch-interactions) | Touch and hybrid input recommendations | Preserve platform units and context; do not transplant values as universal geometry |
| [Android Compose accessibility defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults) and [Views guidance](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views) | Android implementation guidance | Framework defaults, semantics, and target recommendations still require checking real task behavior |
| [Miller's original paper](https://psychclassics.yorku.ca/Miller/) | Historical cognitive research | Distinguish experimental memory/identification tasks from the number of visible interface choices |
| [Cowan 2001](https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf) and [Cowan 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/) | Memory-capacity interpretation | Findings depend on conditions and chunking; they are not universal menu-size limits |
| [egui documentation](https://docs.rs/egui/latest/egui/) | Framework capabilities and limitations | Illustrative desktop case only; verify the project's installed version, integration, and runtime behavior |

Use linked individual criteria and official implementation pages in the relevant reference for a precise claim. The registry provides provenance and routing; numerical accessibility advice is centralized in [accessibility](foundations/accessibility.md).

## Reading the local recommendations

The cards and examples contain original applications of the principles to development tasks. They are not translations of the full website and do not imply that their authors endorse this package. A brief conceptual synthesis describes the source; implementation actions, counterexamples, and acceptance checks describe the proposed practice.

When guidance differs from a site's suggestion, retain traceability and explain the choice. In particular, artificial progress, unnecessary waiting, or pressure to finish a task are not defaults here. Prefer verifiable progress, useful feedback, resumption, and user control.

The source site uses “laws” for a mix of perceptual principles, cognitive concepts, effects, and practical heuristics. Their explanatory scope varies. Apply the principle to a concrete task, consider confounders, and test the resulting behavior. Distinguish this from a normative accessibility requirement.

## Update and offline policy

1. For ordinary task reasoning, use local references without requiring connectivity.
2. When a changing platform requirement, numeric value, API, or source quote matters to correctness, inspect the applicable official page and the installed project version. Prefer a current published standard over a draft unless the task explicitly targets the draft.
3. Record the source, version or publication date when available, consultation date, applicability, and whether the guidance is normative or advisory. A lookup failure does not establish that a source is obsolete.
4. If a source cannot be reached, identify the dated local guidance and resulting uncertainty. Continue with well-supported general practice; leave dependent requirements unverified rather than inventing an update.
5. If sources disagree, compare scope, date, definitions, and authority. Preserve the difference when it cannot be resolved. For example, a general design tip does not automatically override a platform-specific HIG table.

Review the 30-concept catalog against both indexes when updating it. Do not infer general translation quality or freshness from a single differing page. Preserve exact concept-page links even when local filenames are shorter than the site's URLs.

After updates, run the [structural validator](../scripts/validate_skill.py), then exercise affected [behavioral scenarios](verification-scenarios.md). Structural success is not an editorial fact check or a usability study.
