# Live and critical operations

Use when UI controls affect an audience, equipment, shared environment, or an outcome costly to reverse. Examples include presentation output, broadcast control, industrial monitoring, and live event software. This reference supports UX implementation; it does not establish a safety certification or replace a domain's applicable engineering requirements. Read [states and recovery](../foundations/states-and-recovery.md) and [desktop](../platforms/desktop.md).

## Make effect scope unmistakable

Separate preparation from applied state. Previewing a slide, staging a command, and sending it to the output are distinct actions. Label the relevant surface and target visibly; do not rely on green/red alone. Keep the currently applied content or value understandable beside the prepared next action. Keyboard focus, selection, and live identity must not be conflated. Preserve an established click-to-take trigger when it is intentional; separating state does not itself require another confirmation or preparation step.

Place frequent safe actions for efficient use, while separating destructive or high-impact commands sufficiently to prevent common slips. Use confirmation when it helps prevent a consequential mistake; avoid repeated confirmations on every routine action when they encourage automatic dismissal. For rapidly recoverable presenter navigation, a reliable Previous or Undo may be more useful than a blocking dialog. Domain-specific interlocks require the actual product contract, not an invented UX rule.

## Model acknowledgment and degraded states

Represent command intent, dispatch, acknowledgment, and observation separately:

```text
prepared(item_id)
Take -> outputs[output_id].pending(command_id, item_id)
confirmed effect(command_id, output_id) ->
    outputs[output_id].last_confirmed(item_id, acknowledged_at)
failure(command_id, output_id) ->
    outputs[output_id].failed(error, last_confirmed_item)
timeout/disconnect(output_id) ->
    outputs[output_id].outcome_unknown(last_confirmed_item)
```

Keep command identity, pending work, confirmed content, and failure/unknown state per output. If HDMI confirms while NDI fails, show the split result and each target's last confirmed content. An aggregate success label requires every requested target to confirm the intended result at the stated acknowledgment level; one successful target cannot turn partial output into global success. A late acknowledgment must not replace newer confirmed state; reconcile competing or unknown commands through the actual output contract.

An acknowledgment should mean what the underlying system guarantees. A command accepted by a queue may not prove that the target rendered it; name that distinction. If only dispatch can be observed, say "Sent" or "Awaiting confirmation" rather than "Live". Use an output monitor or actual runtime observation for verification when available. Reconnection should reconcile state before replaying commands whose effect may already have occurred.

Show freshness and degraded connectivity without replacing the last known state with a reassuring default. A "Freeze" control for display inspection should not imply that the remote process paused. Alerts need priority tied to the task, a useful action, and an acknowledgment policy when the domain requires one. Avoid decorative flashing and continuous alarm saturation; follow applicable motion accessibility guidance and test with operators.

## Rust/egui presenter example

For a Rust presenter using egui, keep domain state outside frame drawing: prepared slide identity and each output's last confirmed live identity, connection, pending commands, and operation errors. The UI reads a snapshot and emits intentional commands; a frame redraw never sends Take again. Record only one command for one activation, whether it arrives through a button or shortcut. This is an architectural example, not a claim about a particular egui API.

Route shortcuts through the active input context. Editing a slide title must not advance the audience display. Present Preview and Live as persistent labels with distinct borders or shapes; keep explicit Take, Previous, and any supported blackout control reachable through named UI actions as well as verified shortcuts. Opening a second monitor window is not proof of audience output. Test the actual installed runtime, display routing, disconnect/reconnect, and rendered audience surface.

Inspect the selected egui integration's current keyboard and accessibility support. Do not assume screen-reader support because controls look native or because an accessibility backend exists. Verify focus traversal, names, states, and essential operations with the target operating system and assistive technology; document any missing capability. See [accessibility](../foundations/accessibility.md).

Related principles: [mental models](../principles/mental-model.md), [Fitts's Law](../principles/fitts-law.md), [working memory](../principles/working-memory.md), [Jakob's Law](../principles/jakob-law.md), and [cognitive load](../principles/cognitive-load.md). Preserve justified operator density when it supports monitoring and rapid recovery.

## Acceptance checks

- Verify Preview edits never affect Live until the intended command is issued.
- Exercise one activation across several redraws; only one command is dispatched.
- Test late acknowledgment, unknown outcome, wrong output target, disconnect, reconnect, and emergency recovery behavior supported by the product.
- Observe actual output rather than inferring it from local button feedback.
- Verify shortcuts while typing and keyboard-only operation; record runtime accessibility limits.
- Simulate common slips with representative operators and compare recovery effort through [evaluation and metrics](../foundations/evaluation-and-metrics.md).

Guidance status: original implementation recommendations, reviewed 2026-10-04. Use the platform references for sourced accessibility guidance and applicable domain specifications for operational requirements.
