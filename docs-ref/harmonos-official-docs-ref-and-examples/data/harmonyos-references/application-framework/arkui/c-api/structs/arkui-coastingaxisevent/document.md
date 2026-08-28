# ArkUI\_CoastingAxisEvent

typedef struct ArkUI\_CoastingAxisEvent ArkUI\_CoastingAxisEvent

#### Overview

Defines the coasting axis event.

When the user performs a two-finger swipe on the touchpad, the system constructs a swipe event based on the finger lift speed, following a specific attenuation curve. You can listen for this event to handle the flick effect immediately after processing regular axis events.

This event is only dispatched if two conditions are met: 1. The user executes a two-finger swipe on the touchpad. 2. A component registered for the [NODE\_ON\_COASTING\_AXIS\_EVENT](../../header-files/native-node-h/document.md#arkui_nodeeventtype) event (via [registerNodeEvent](../arkui-nativenodeapi-1/document.md#registernodeevent)) exists at the pointer's position.

**Since**: 22

**Related module**: [ArkUI\_EventModule](../../modules/arkui-eventmodule/document.md)

**Header file**: [ui\_input\_event.h](../../header-files/ui-input-event-h/document.md)
