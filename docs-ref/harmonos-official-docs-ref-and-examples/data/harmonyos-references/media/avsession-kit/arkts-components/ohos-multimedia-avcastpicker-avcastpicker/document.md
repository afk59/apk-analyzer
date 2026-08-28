# @ohos.multimedia.avCastPicker (AVCastPicker)

The module provides the functionality to create an **AVCastPicker** component, which offers a unified entry for device discovery and connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/23ioADpUSVu9fWTjrli9KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99BA8961CD8788764646B2B9D78F4DA35A5BF6F18F267E59CB0E8DDBD281CC2B)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The Preview in DevEco Studio does not support actual casting. To see the real effect, test on a real device.

#### Modules to Import

import { AVCastPicker } from '@kit.AVSessionKit';

#### Properties

The [universal properties](../../../../application-framework/arkui/arkts-components/universal-attributes/document.md) are supported.

#### AVCastPicker

AVCastPicker({
  normalColor?: Color | number | string;
  activeColor?: Color | number | string;
  pickerStyle?: AVCastPickerStyle;
  colorMode?: AVCastPickerColorMode;
  sessionType?: string;
  customPicker?: CustomBuilder;
  onStateChange?: (state: AVCastPickerState) => void;
})

Implements an **AVCastPicker** component, which can be used to cast audio and video onto other devices.

This component is a custom component. Some basic knowledge of [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component) will be helpful in using the component.

**Decorator**: [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| normalColor11+ | Color | number | string | No | @Prop | 
Color of the component in normal state.

If this parameter is left unspecified, the color setting in **colorMode** is used.

 |
| activeColor11+ | Color | number | string | No | @Prop | Color of the component when audio and video are successfully cast to another device. If this parameter is left unspecified, the system preferentially matches the color based on **normalColor**. If **normalColor** is also left unspecified, the color setting in **colorMode** is used. |
| pickerStyle12+ | [AVCastPickerStyle](../../arkts-apis/ohos-multimedia-avcastpickerparam-avcastpicker-parameters/document.md#avcastpickerstyle12) | No | @Prop | 

Style of the component.

\- When **sessionType** is set to **audio** or **video**, the default value is **STYLE\_PANEL**.

\- When **sessionType** is set to **voice\_call** or **video\_call**, the default value is **STYLE\_MENU** and the value cannot be changed to **STYLE\_PANEL**.

 |
| colorMode12+ | [AVCastPickerColorMode](../../arkts-apis/ohos-multimedia-avcastpickerparam-avcastpicker-parameters/document.md#avcastpickercolormode12) | No | @Prop | 

Display mode. The default value is **AUTO**.

\- When **colorMode** is set to **AUTO**, the default system color in dark/light color mode is used.

\- When **colorMode** is set to **DARK** or **LIGHT**, the preset system color of the corresponding mode is used.

 |
| sessionType12+ | string | No | @Prop | Session type. For details, see [AVSessionType](../../arkts-apis/ohos-multimedia-avsession-avsession-management/types/document.md#avsessiontype10). The default value is **AVSessionType** created by the application. |
| customPicker12+ | [CustomBuilder](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8) | No | @Prop | Custom style. You are advised to customize a component style so that the component can be displayed quickly. |
| onStateChange11+ | (state: [AVCastPickerState](../../arkts-apis/ohos-multimedia-avcastpickerparam-avcastpicker-parameters/document.md)) => void | No | \- | Callback invoked when the casting state changes. |

#### Events

The [universal events](../../../../application-framework/arkui/arkts-components/universal-events/document.md) are supported.

#### Example

The following is an example of using **AVCastPicker**:

To experience complete functions, see [AVCastPicker Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/distributed-playback-guide) and [Using the Call Device Switching Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-switch-call-devices).

import { AVCastPickerState, AVCastPicker } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {

  @State pickerImage: ResourceStr = $r('app.media.castPicker'); // Custom resources.

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
        AVCastPicker({
          normalColor: Color.Red,
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
