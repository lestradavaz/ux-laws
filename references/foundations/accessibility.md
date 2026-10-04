# Accessibility: requirements, platform guidance, and verification

Read for every changed user journey; investigate the affected controls and states rather than claiming a whole-product audit. Pair with [interaction](interaction.md), [states and recovery](states-and-recovery.md), and [evaluation](evaluation-and-metrics.md). Search terms: semantics, focus, targets, contrast, reflow, timing, authentication, canvas.

## Choose the applicable baseline

For web content, use the project's stated WCAG version and level. If absent, propose WCAG 2.2 AA as an engineering baseline and record it as a default, not an inferred legal obligation. AA includes A requirements. Procurement, contractual, and jurisdiction-specific obligations need their own verified scope. Native software needs its platform accessibility APIs and applicable requirements; HTML techniques are not native implementation instructions.

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) supplies normative success criteria. [WCAG2ICT](https://www.w3.org/TR/wcag2ict/) is informative guidance for applying WCAG concepts to non-web documents and software, not a separate conformance standard. [APG](https://www.w3.org/WAI/ARIA/apg/) supplies informative web-widget patterns. None of these makes a passing automated scan a conformance claim. A scoped change review leaves untested criteria, pages, processes, platforms, and assistive-technology combinations unassessed.

## Numeric reference: keep units, levels, and exceptions

Values below were consulted on 2026-10-04. Recheck the official source for an updated platform or formal assessment. CSS px, pt, dp, and epx are different coordinate systems; do not substitute physical screen pixels or treat their numbers as interchangeable.

| Context | Value and status | Important boundary and source |
|---|---|---|
| Web pointer targets | At least 24 × 24 CSS px, WCAG 2.2 AA, SC 2.5.8 | Exceptions: qualifying spacing, equivalent control, inline content, unmodified user-agent sizing, essential presentation. Spacing test uses 24 CSS px diameter circles centered on undersized target bounding boxes; circles must avoid other targets and other undersized-target circles. [Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). |
| Web enhanced targets | At least 44 × 44 CSS px, AAA, SC 2.5.5 | Equivalent, inline, user-agent, and essential exceptions; does not inherit the AA spacing exception. [Target Size Enhanced](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html). |
| Android | 48 × 48 dp interactive target recommendation | Visible icon may be smaller; measure actual accessible hit area, avoiding overlap. [Android accessibility](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views). |
| Windows | Touchable: 40 × 40 epx, or 32 epx high when at least 120 epx wide; touch-optimized recommendation: 44 × 44 epx with at least 4 epx visible separation | These are platform guidance, not WCAG CSS units. [Windows touch interactions](https://learn.microsoft.com/en-us/windows/apps/develop/input/touch-interactions). |
| Apple iOS / iPadOS | Default 44 × 44 pt; minimum 28 × 28 pt | Current HIG distinguishes default and minimum; use defaults as the normal design starting point and assess spacing, consequence, and input context before smaller controls. [HIG accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). |
| Apple macOS | Default 28 × 28 pt; minimum 20 × 20 pt | Same HIG guidance and distinction. |
| Apple tvOS | Default 66 × 66 pt; minimum 56 × 56 pt | Same HIG guidance; directional focus still needs testing. |
| Apple visionOS | Default 60 × 60 pt; minimum 28 × 28 pt | Same HIG guidance; spatial distance and indirect selection need platform-specific validation. |
| Apple watchOS | Default 44 × 44 pt; minimum 28 × 28 pt | Same HIG guidance; screen constraints do not prove small targets usable. |
| Web text contrast | AA: 4.5:1 normal text; 3:1 large text, SC 1.4.3 | Large text: at least 18 pt, or 14 pt bold, or equivalent. Exceptions include incidental text and logotypes. Ratios are thresholds, not rounded estimates. [Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). |
| Web meaningful non-text information | AA: 3:1 against adjacent colors, SC 1.4.11 | Applies to required control/state cues and meaningful graphics, with inactive, unmodified user-agent, and essential-graphic exceptions. Not every decorative border needs the ratio. [Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). |
| Web text resize | AA: up to 200% without loss of content/function, SC 1.4.4 | Captions and images of text have criterion-specific exceptions. [Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html). |
| Web reflow | AA: no loss or two-dimensional scrolling at a width equivalent to 320 CSS px, or height 256 CSS px for vertically written content, SC 1.4.10 | Parts requiring two-dimensional layout are excepted; this does not excuse inaccessible surrounding controls. [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html). |

## Semantics before decoration

Inspect actual accessibility output, not component names. A button-shaped object needs an exposed name, role, state, and action; include the visible label in its accessible name so voice users can address it. [Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html). Prefer native controls and native associations. Adding a role does not implement keyboard behavior, focus, validation, or state updates; [APG's introduction](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) explains this implementation responsibility.

For a chart, provide a useful summary and an equivalent way to inspect values. For a canvas editor, map selectable objects, properties, and operations into navigable accessible controls. A raster screenshot or an offscreen list with no actionable relation to selection is insufficient. For immediate-mode frameworks such as egui, verify the actual accessibility bridge, supported build features, platform integration, and stable identities. Do not assume repeated drawing creates a usable accessibility tree. Test a real built application with the intended assistive technology; record unavailable support as a limitation and offer a workable equivalent route.

## Operability and perception checklist

- Complete the task with keyboard alone; preserve visible, logical focus and an exit from composite widgets and dialogs. Distinguish focus from selection. Under AA SC 2.4.11, author-created content must not entirely obscure a control when it receives keyboard focus; consult its notes for user-repositioned and user-opened content. Fully unobscured focus is stronger practice, with AAA SC 2.4.12 separately assessed. [Focus Minimum](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html), [Focus Enhanced](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-enhanced.html).
- Test enlarged text, narrow layout, text spacing overrides, high-contrast settings, and reduced motion. Check labels, error hints, overlays, keyboard appearance, and dynamic content, not only the initial page.
- Communicate errors, selected state, series identity, and connection status through more than hue. Inspect contrast in each meaningful state and theme. Do not rely on decorative animation to communicate completion.
- For applicable web dragging interactions, AA SC 2.5.7 needs a single-pointer alternative without dragging, apart from essential or unmodified user-agent behavior; keyboard support alone does not supply that pointer alternative. [Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html). Verify hit areas after zoom, transform, clipping, and overlays.
- Announce relevant background status without stealing focus; use appropriate native notifications or web status semantics. Avoid announcing every live value. [Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html).

## Time, motion, and authentication

Separate motion concerns: interaction-triggered motion animation can be disabled unless essential under AAA SC 2.3.3; reduced-motion support is a useful implementation approach. Automatically moving/blinking/scrolling content lasting more than five seconds alongside other content has pause/stop/hide obligations under A SC 2.2.2 unless essential. Auto-updating information has its own pause/stop/hide or frequency-control condition. Flashing hazards have separate criteria; reduced motion does not prove flash safety. [Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html), [Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html).

For time limits, examine turn-off, adjustment, extension, and criterion exceptions before relying on a timeout. Warn in an actionable way and preserve entered work where feasible; time-sensitive events and essential timing need explicit reasoning. [Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html).

Authentication must support completion without an unsupported cognitive test. Password managers and paste can provide an assisting mechanism; check the entire flow including one-time codes and recovery. SC 3.3.8 AA permits specified alternatives, assisting mechanisms, object recognition, or personal-content recognition; AAA SC 3.3.9 differs. Do not call every CAPTCHA universally prohibited or disable security checks indiscriminately. [Accessible Authentication Minimum](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html).

## Acceptance example and reporting

For an export dialog: keyboard opens it, focus enters predictably, every setting has a name and state, validation connects errors to fields, pending export announces status without moving focus, failure keeps settings, dismissal returns to the invoker or a sensible successor. At enlarged text, the primary action remains reachable; touch targets meet the applicable platform baseline without overlapping neighboring actions.

Report tested task, build, platforms, input modes, assistive technologies, findings, and untested areas. State “affected dialog checks passed on these configurations,” rather than “application is compliant.” User testing can expose needs beyond standards; standards checks can expose barriers a small participant sample misses.
