# Specialized, constrained, and spatial interfaces

Use when ordinary web/mobile/desktop assumptions do not describe the environment: kiosks, game HUDs, spatial interfaces, embedded displays, and constrained professional tools. Start by recording audience, task, hardware, physical conditions, supported inputs, operating limits, and failure consequences. Reuse only relevant patterns. A general UX principle does not override a device constraint or domain requirement.

## Shared adaptation method

Identify how people perceive state, issue commands, confirm outcomes, and recover. Determine whether use is public/private, seated/standing, novice/expert, interrupted/continuous, or shared/personal. Inspect actual hardware and runtime accessibility capabilities. Do not assume a touch target measured in web CSS pixels applies unchanged to a physical kiosk, VR angular geometry, or embedded panel.

Keep essential controls operable through supported alternatives where feasible. State unsupported tasks accurately and surface documented product limits; an alternative display is useful only if it preserves the necessary information and operations. WCAG2ICT provides informative adaptation guidance for non-web ICT, including considerations for closed functionality. It does not establish universal compliance for constrained hardware. [WCAG2ICT](https://www.w3.org/TR/wcag2ict/). Use [accessibility](../foundations/accessibility.md) for applicability and numeric provenance.

## Kiosks and shared terminals

Make the starting task clear and recovery available without relying on prior account familiarity. Accommodate realistic reach, viewing angle, glare, ambient noise, and privacy. Keep a visible language/help route where the product supports it. Confirm which assistive inputs are physically available; a software-only keyboard route cannot help a kiosk that provides no usable keyboard access.

Separate session reset from task completion. Explain an applicable inactivity warning and preserve or discard sensitive data according to the product's privacy rules. Web kiosk content still needs the web criteria's timing analysis and exceptions. Avoid inventing persistent draft storage on a shared terminal. Example: a ticket kiosk keeps the current itinerary visible and identifies the payment's unknown outcome before allowing another payment. Counterexample: inactivity returns to Welcome during payment and the next user sees the prior traveler details.

## Games and heads-up displays

Prioritize information needed for the next play decision without making menus and settings inaccessible. Consider readable text, distinguishable objects, configurable input, subtitle placement, motion, and focus across controller/keyboard/pointer transitions. Microsoft's Xbox Accessibility Guidelines are best-practice guidance organized by game features; their input guidance extends beyond remapping to alternatives for demanding input patterns. [XAG overview](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines) and [XAG 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107).

Preserve intentional challenge while separating it from accidental interface barriers. A cooldown indicator can use shape/text as well as color; essential menu navigation should not require simultaneous stick clicks if a supported alternative can accomplish the task. Test in play conditions, with realistic visual load and configured controls. Do not infer menu accessibility from gameplay input support or vice versa.

## XR and spatial interaction

Consider field of view, comfortable reading, depth, occlusion, motion, reach, fatigue, and environmental awareness. Keep task content stable enough to understand and allow an appropriate exit/recenter route. Apple guidance recommends limiting excessive peripheral motion and repetitive large gestures in visionOS; its vision-and-motion session discusses perceptual comfort. These are platform recommendations, not universal distances or angular dimensions. [Apple HIG accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) and [vision/motion considerations](https://developer.apple.com/videos/play/wwdc2023/10078/).

Example: a spatial inspection tool exposes a readable panel and a supported selection alternative, rather than requiring precise sustained arm pointing for every step. Counterexample: critical text follows the head incessantly, rapid peripheral motion demands attention, and exit depends on a hidden gesture. Validate on target hardware with representative users; a desktop simulation cannot establish comfort.

## Embedded and professional constraints

For small panels, gloved use, vibration, low-power displays, or regulated workflows, prioritize authoritative state, mode visibility, signal freshness, and recovery. Preserve justified information density and learned operator conventions. Map preparation, requested command, acknowledgment, and actual effect as in [live operations](../patterns/live-and-critical-operations.md). Do not label stale telemetry "Normal" or assume touchscreen feedback means equipment applied a command.

Related principles: [Fitts's Law](../principles/fitts-law.md), [mental models](../principles/mental-model.md), [working memory](../principles/working-memory.md), [cognitive load](../principles/cognitive-load.md), and [Jakob's Law](../principles/jakob-law.md).

## Acceptance checks

- Test essential tasks on target hardware with realistic posture, environment, and supported input modes.
- Verify mode/target identity, freshness, acknowledgment, interruption, and recovery under relevant failures.
- Check public-session privacy, timeout handling, motion/comfort, or game input alternatives where applicable.
- Record actual accessibility capabilities and gaps. Separate observed usability from untested assumptions or certification claims.

Sources consulted: 2026-10-04. Specialized guidance supplements task/domain requirements; it does not replace them.
