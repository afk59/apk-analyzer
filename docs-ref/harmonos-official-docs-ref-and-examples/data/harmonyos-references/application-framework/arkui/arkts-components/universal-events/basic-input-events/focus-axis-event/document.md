# Focus Axis Event

A focus axis event is an event triggered by interacting with a game controller through the directional pad or joystick. This type of event is dispatched to the component that currently has focus and is then passed back to the application. Components that are focusable by default, such as **Button**, do not require additional attributes to handle focus axis events. For components that are not focusable by default, such as **Text** and **Image**, you can enable focus axis events by setting the **focusable** attribute to **true**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/HkVsbzmYQEuOxN9nI_5JXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5BCB8DE204CFD9AD1D416A608D32EFF01279990ED89B808102B0B74B4E9A25B)

The focus axis event is supported since API version 15. Updates will be marked with a superscript to indicate their earliest API version.

#### onFocusAxisEvent

onFocusAxisEvent(event: Callback<FocusAxisEvent>): T

Binds a focus axis event callback to the component. Triggered when any operation is performed with the game controller's directional pad or joystick on the bound component.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | Callback<[FocusAxisEvent](#focusaxisevent)\> | Yes | Focus axis event callback. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### FocusAxisEvent

Describes the focus axis event object. Inherits from [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| axisMap | Map<[AxisModel](../../../common-definitions/enums/document.md#axismodel15), number> | No | No | Axis value table of the focus axis event. |
| stopPropagation | Callback<void> | No | No | Blocks [event bubbling](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) propagation. |

#### Example

This example demonstrates how to set up a focus axis event on a button. When the button gains focus, operating the game controller's directional pad or joystick will trigger the **onFocusAxisEvent** callback.

// xxx.ets
@Entry
@Component
struct FocusAxisEventExample {
  @State text: string = ''
  @State axisValue: string = ''

  aboutToAppear(): void {
    this.getUIContext().getFocusController().activate(true)
  }

  aboutToDisappear(): void {
    this.getUIContext().getFocusController().activate(false)
  }

  build() {
    Column() {
      Button('FocusAxisEvent')
        .defaultFocus(true)
        .onFocusAxisEvent((event: FocusAxisEvent) => {
          let absX = event.axisMap.get(AxisModel.ABS\_X);
          let absY = event.axisMap.get(AxisModel.ABS\_Y);
          let absZ = event.axisMap.get(AxisModel.ABS\_Z);
          let absRz = event.axisMap.get(AxisModel.ABS\_RZ);
          let absGas = event.axisMap.get(AxisModel.ABS\_GAS);
          let absBrake = event.axisMap.get(AxisModel.ABS\_BRAKE);
          let absHat0X = event.axisMap.get(AxisModel.ABS\_HAT0X);
          let absHat0Y = event.axisMap.get(AxisModel.ABS\_HAT0Y);
          this.axisValue =
            'absX: ' + absX + '; absY: ' + absY + '; absZ: ' + absZ + '; absRz: ' + absRz + '; absGas: ' + absGas +
              '; absBrake: ' + absBrake + '; absHat0X: ' + absHat0X + '; absHat0Y: ' + absHat0Y;
          this.text = JSON.stringify(event);
        })
      Text(this.axisValue).padding(15)
      Text(this.text).padding(15)
    }.height(300).width('100%').padding(35)
  }
}

The figure below shows the result when the game controller's joystick is moved.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ZC7h8DjjQXWw3t7dsol_kQ/en-us_image_0000002568765103.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F572E672B04460A8D5A94E5B858A1F9F00EEF13CFCD39B87E8EB3F82D7379622)
