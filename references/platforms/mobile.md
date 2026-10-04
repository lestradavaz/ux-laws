# Mobile and touch interfaces

Use for native or hybrid phone/tablet applications and touch-centered responsive UI. Identify actual device classes, input modes, platform conventions, orientation constraints, and network/interruption conditions. A touch screen may also use a keyboard, pointer, stylus, voice, switch, or screen reader. Read [interaction](../foundations/interaction.md) and [accessibility](../foundations/accessibility.md); keep platform units and recommendation status intact.

## Design for the task and platform

Adapt navigation and controls to the host platform rather than scaling down a desktop view. Maintain recognizable back behavior, selection, sheets/dialogs, and native editing conventions. Apple's iOS guidance recommends emphasizing primary tasks, accommodating device configuration changes, and considering comfortable reach. These are platform design recommendations, not universal rules for every screen or user. [Apple HIG: designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios).

Arrange frequent actions so they can be reached and understood under realistic holding conditions. Avoid placing a dangerous action where a routine gesture or hand repositioning commonly lands. Evaluate hit areas and separation, not merely visible icon size; authoritative target values and units belong in [accessibility](../foundations/accessibility.md). [Fitts's Law](../principles/fitts-law.md) helps reason about acquisition effort but does not determine one universal control dimension.

Gestures may accelerate a discoverable action; provide an accessible route to essential tasks rather than relying exclusively on swipe, long press, or multi-finger input. Android's accessibility guidance explicitly recommends alternatives to gestures and testing with TalkBack and Switch Access. [Android mobile accessibility](https://developer.android.com/design/ui/mobile/guides/foundations/accessibility).

## Preserve meaning through adaptation

Use system text-scaling support and test large sizes without clipping labels, losing context, or making actions unreachable. Apple's Dynamic Type guidance describes adapting layout as text grows; merely multiplying fonts in fixed-height containers is insufficient. [Apple Dynamic Type session](https://developer.apple.com/videos/play/wwdc2024/10074/). Reorganize comparison content carefully: stacking a table into cards must preserve labels, units, and the comparisons needed for the task. Tablet layouts may benefit from concurrent panes and external keyboard support rather than phone-sized content stretched across the screen.

Provide semantic names, roles, states, and actions through the actual runtime. In Android Compose, semantics convey component meaning to accessibility services and tests; built-in components supply useful defaults, while custom drawing and grouping require inspection. [Compose semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics). Do not apply web ARIA attributes to a native view and assume they work. Hybrid web content follows its web contract as well as host integration requirements.

Treat interruption as ordinary use: keyboard appearance, backgrounding, incoming calls, permission prompts, transient offline periods, and process recreation where relevant. Retain useful task state according to the app's existing storage and privacy rules. A locally displayed toggle is not proof that a remote setting persisted. Make pending and failed synchronization intelligible; see [feedback and asynchronous work](../patterns/feedback-and-async.md).

## Example and counterexample

A mobile inspection app exposes a visible "Add photo" control, clearly requests camera permission when needed, preserves the draft after backgrounding, and marks attachments pending upload until acknowledgment. The same flow is operable with TalkBack. Counterexample: adding photos requires an undocumented shake gesture, enlarged text hides Submit beneath the keyboard, and offline drafts are labeled "Submitted".

Related principles: [mental models](../principles/mental-model.md), [Jakob's Law](../principles/jakob-law.md), [working memory](../principles/working-memory.md), [cognitive load](../principles/cognitive-load.md), and [Tesler's Law](../principles/teslers-law.md).

## Acceptance checks

- Complete the affected task on representative physical device sizes and actual supported input modes.
- Check hit areas, accidental activation, orientation, system bars, keyboard occlusion, and large text.
- Verify screen-reader naming/order/actions and a relevant alternative input route; a semantics snapshot alone does not establish usability.
- Test interruption, denied permission, offline work, and reconnection without losing or falsely completing the task.
- Preserve justified expert workflows on tablets or field devices; evaluate density through task evidence rather than imposing a universal sparse layout.

Sources consulted: 2026-10-04. Apple and Android guidance here is platform-specific and recommendatory. Web criteria apply directly to web content; native requirements need the applicable platform and policy context.
