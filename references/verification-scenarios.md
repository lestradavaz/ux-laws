# Behavioral verification of this package

Use these scenarios after substantial changes to the skill. They evaluate whether the guidance produces sensible, scoped decisions; they do not evaluate the usability of a deployed product. Give an independent reviewer a realistic request, this package, and the minimum raw artifacts needed. Do not disclose the intended solution before collecting the result. Keep generated evaluation work outside the project unless expressly requested.

For each run record references selected, proposed behavior or changes, evidence claimed, scope followed, and unresolved limits. Apply the acceptance checks below after receiving the result. Inspection of prose is separate from actual runtime or user testing.

## 1. Web navigation with many destinations

**Request:** “Our admin product has 14 frequently used destinations. A reviewer says Miller requires seven, so replace navigation with a seven-item menu and put the rest in onboarding. Assess this recommendation and specify a practical change if needed.”

**Raw evidence:** destination labels, representative tasks, usage frequencies if genuinely available, current navigation and keyboard behavior.

**Accept:** no universal seven-item cap; meaningful grouping and findability; frequent expert actions remain reachable; baseline and task-oriented checks distinguished from assumptions. No product-wide redesign without cause.

## 2. Ambiguous form input and recovery

**Request:** “Make our payment form accept more date and amount formats. It currently rejects pasted spaces and clears the form after any validation error.”

**Raw evidence:** locale and parsing contracts, current fields, examples of safe equivalent and ambiguous input, error and submit behavior.

**Accept:** safe normalization with explicit handling of ambiguous consequential meaning; valid entries preserved appropriately; field-linked correction and duplicate-operation policy grounded in actual contracts. Postel does not override server validation or authorization. No invented locale inference.

## 3. Mobile target acquisition

**Request:** “A dense Android list has adjacent 24 dp icon buttons. Increase touch reliability without changing the entire list design.”

**Raw evidence:** row dimensions, hit regions, semantics, screen sizes, supported input and text settings.

**Accept:** correct platform and units; usable hit regions with no overlap; label and alternate access checked; realistic runtime testing proposed or performed. No CSS-pixel conversion presented as an Android requirement, and no broad redesign.

## 4. Professional dashboard

**Request:** “Our trained dispatchers need 20 readings visible while monitoring. Simplify the dashboard; users report missing one critical alert among normal updates.”

**Raw evidence:** tasks and consequences, current readings/alerts, screenshots or runtime, alert history only if actually supplied.

**Accept:** preserves justified density; prioritizes consequential signals and recovery; supports non-color identification; avoids fictitious Pareto ratios or removal of essential readings. Distinguishes measured alert misses from predictions.

## 5. Rust/egui live presenter

**Request:** “Improve selection and output feedback in a live presentation console. Clicking a slide currently highlights it as live immediately, but some outputs fail afterward.”

**Raw evidence:** command/result flow, selected/preview/live state, output identities and errors, shortcuts, focus, renderer integration.

**Accept:** selection, preview, request, and acknowledged output remain distinct; partial destination failure is visible; retries and repeated activation respect actual contracts; keyboard and consequential actions considered. Does not invent framework APIs, guarantee screen-reader integration, or claim immediate UI feedback proves output delivery.

## 6. Custom canvas editor

**Request:** “Add a way to reorder objects without precise dragging. Keep the canvas renderer.”

**Raw evidence:** object model, selection and commands, existing semantic surface, undo/redo and supported modalities.

**Accept:** alternative operation connected to the same domain command and undo model; focus/selection ownership defined; accessible names and custom-surface limitations explicit. An HTML role alone is not treated as native accessibility support.

## 7. Offline audit with insufficient evidence

**Request:** “Audit these screenshots offline and certify that our whole application meets WCAG AA.”

**Raw evidence:** screenshots only, current local references, no runtime or complete process information.

**Accept:** useful evidence-bounded findings; no full conformance certification; keyboard, dynamic behavior, assistive technology and current requirements marked unverified. No fabricated browsing or user research; no dependency on connectivity for general findings.

## Regression standard

A pass must select relevant material, produce behavior tied to the task, respect scope, avoid misleading evidence, and expose meaningful uncertainty. One serious failure on user control, data loss, normative scope, or false evidence requires correction and a fresh check of the affected scenario. Do not keep adding rules for stylistic preferences; revise guidance when observed behavior exposes a substantive ambiguity.
