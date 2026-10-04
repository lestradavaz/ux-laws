# Choices and settings

Use when users choose a value, compare alternatives, configure behavior, or manage preferences. Read [interaction](../foundations/interaction.md) for control semantics and [states and recovery](../foundations/states-and-recovery.md) for persistence failures.

## Match the choice to the decision

Determine whether the user selects one value, several values, a continuous amount, or an immediate command. Select a control that exposes that meaning. A row of radio options can make short, consequential alternatives comparable; a select can conserve space for a familiar long list; searchable selection can help a large known vocabulary. Do not replace a comprehensible native control with a custom widget for appearance alone.

[Hick's Law](../principles/hick-law.md) suggests reducing decision difficulty through grouping and meaningful differences, not deleting expert options. Keep advanced controls available when they serve real tasks. Move infrequent choices into a clearly named section only when discovery cost is acceptable. [Miller's Law](../principles/miller-law.md) supplies no universal maximum number of options. A short list of nearly identical labels may be harder than a larger organized list.

Comparison content should answer what changes, what it costs, who it fits, and whether the choice can be reversed. Put essential constraints near each option. Avoid a visually dominant recommendation with hidden disadvantages. Keep recommendations explainable through a relevant criterion, such as compatibility with an existing device, rather than an unqualified "Best" badge.

For web switches, use stable naming and expose the current binary state. Changing the label from "Enable alerts" to "Disable alerts" can make the name and state confusing. APG distinguishes a switch's on/off semantics from checkboxes; the chosen widget should preserve that meaning. [APG switch pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch/).

## Define when changes take effect

Choose between immediate application and explicit Save according to existing conventions, reversibility, and effect scope. Display that policy near consequential controls. Avoid mixed behavior where some fields save instantly and others silently wait for a button.

```text
persisted_value != draft_value -> unsaved
Save -> saving -> saved | error(draft retained)
Cancel -> restore persisted_value
```

An immediate-save control still needs a request state and recovery. Do not display a successful saved state based solely on the local toggle. If optimistic display is appropriate, make a failed persistence operation recoverable and disclose the effective value. Keep the requested value and acknowledged value distinguishable for settings that affect remote devices or other users.

Clarify scope: this document, this device, this account, or the whole team. Permission limitations should explain who can change a locked setting or what prerequisite is missing. A tooltip-only explanation on a disabled control excludes some input modes; prefer nearby help that can be reached independently. Show inherited values separately from explicit overrides when the product already supports inheritance.

Avoid unnecessary settings by choosing sensible defaults, but do not remove agency for accessibility preferences or expert workflows. [Tesler's Law](../principles/teslers-law.md) encourages handling avoidable complexity in the system; it does not permit hiding consequential policy decisions.

## Example and counterexample

An export dialog groups format, destination, and optional metadata. Each format explains compatibility; an existing project default is preselected; Export shows the effective result. Counterexample: formats appear as unexplained icons, the recommended option quietly changes the destination, and closing the dialog loses edits without indicating whether anything was saved.

Related principles: [cognitive load](../principles/cognitive-load.md), [mental models](../principles/mental-model.md), [Jakob's Law](../principles/jakob-law.md), and [Postel's Law](../principles/postels-law.md). Be tolerant of safe input variations while retaining exact values when normalization could change meaning.

## Acceptance checks

- Users can state the active choice, its consequence, scope, and when it becomes effective.
- Verify single/multiple selection, accessible names, keyboard operation, and visible focus using [accessibility](../foundations/accessibility.md).
- Test save failure, rapid changes, Cancel, closing, and concurrent remote updates where supported. Requested and effective values never silently diverge.
- Check unavailable choices, long localized labels, and inherited settings with realistic content.
- Validate that expert users can still reach recurring options without repetitive disclosure overhead.

Sources consulted: 2026-10-04. APG is informative web widget guidance. The state model and selection criteria are implementation recommendations, not universal standards.
