# @ohos.multimedia.avInputCastPicker (AVInputCastPicker)

The module provides the functionality to create an **AVInputCastPicker** component, which offers a unified entry for discovering and connecting recording devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/JyPrqNHFRoGlYR_r8rp8Fw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4990D4F5FECCD6DFC3C3324E57EC12D8A1DDA0A1ED2B8CDED1D678F24666EED0)

-   The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The Preview in DevEco Studio does not support actual recording device selection. To see the real effect, test on a real device.

#### Modules to Import

import { AVInputCastPicker } from '@kit.AVSessionKit';

#### Properties

The [universal properties](../../../../application-framework/arkui/arkts-components/universal-attributes/document.md) are supported.

#### AVInputCastPicker

AVInputCastPicker({
  customPicker?: CustomBuilder;
  onStateChange?: OnPickerStateCallback;
})

Implements an **AVInputCastPicker** component, which can be used to switch audio input devices.

This component is a custom component. Some basic knowledge of [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component) will be helpful in using the component.

**Decorator**: [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component)

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.AVInputCast

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| customPicker | [CustomBuilder](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8) | No | @Prop | Custom style. You are advised to customize a component style for higher component rendering performance. |
| onStateChange | [OnPickerStateCallback](#onpickerstatecallback) | No | \- | Callback invoked when the device list state changes. |

#### OnPickerStateCallback

type OnPickerStateCallback = (state: AVCastPickerState) => void

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.AVInputCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AVCastPickerState](../../arkts-apis/ohos-multimedia-avcastpickerparam-avcastpicker-parameters/document.md#avcastpickerstate) | Yes | Device list state. |

#### Events

The [universal events](../../../../application-framework/arkui/arkts-components/universal-events/document.md) are supported.

#### Example

The following is an example of using **AVCastPicker**:

import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {

  @State pickerImage: ResourceStr = $r('app.media.layered\_image'); // Custom resources.

  private onStateChange(state: AVCastPickerState) {
    if (state == AVCastPickerState.STATE\_APPEARING) {
      console.info('The picker starts showing.');
    } else if (state == AVCastPickerState.STATE\_DISAPPEARING) {
      console.info('The picker finishes presenting.');
    }
  }

  @Builder
  customPickerBuilder() {
    Image(this.pickerImage)
      .width('100%')
      .height('100%')
      .fillColor(Color.Black)
  }

  build() {
    Row() {
      Column() {
        AVInputCastPicker({
          customPicker: () => this.customPickerBuilder(),
          onStateChange: this.onStateChange
        })
          .width('40vp')
          .height('40vp')
          .border({ width: 1, color: Color.Red })
      }.height('50%')
    }.width('50%')
  }
}
