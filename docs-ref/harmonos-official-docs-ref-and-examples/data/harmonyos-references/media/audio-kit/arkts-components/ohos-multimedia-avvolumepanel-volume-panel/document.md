# @ohos.multimedia.avVolumePanel (Volume Panel)

The module provides the capability of displaying the system volume panel for users to adjust the volume.

An application cannot directly adjust the system volume. However, it can invoke the system volume panel for users to adjust the volume. When the user adjusts the volume, a volume prompt UI is displayed to explicitly notify the user that the system volume changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/I30aeioTRBScB0X1vD9d_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F70D03E69475C81012B6F55EB6358B935F6F494EC88DA8D9BF969AD86F240DB2)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The sample effect is subject to the real device in use. Currently, DevEco Studio Previewer cannot display the actual volume or adjust the volume.
-   **Device restrictions**
    -   On wearable devices, the module can be used to adjust the system volume, but no UI is displayed. You need to design the UI by yourself.
    -   The APIs of this module are not supported on TVs.

#### Modules to Import

import { AVVolumePanel } from '@kit.AudioKit';

#### Properties

The [universal properties](../../../../application-framework/arkui/arkts-components/universal-attributes/document.md) are supported.

#### AVVolumePanel

AVVolumePanel({volumeLevel?: number, volumeParameter?: AVVolumePanelParameter})

Volume panel, which can be used to display the volume adjustment panel in your application.

**Decorator**: [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Volume

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| volumeLevel | number | No | @Prop | 
Target volume.

The value must be between the minimum volume and the maximum volume supported by the device.

If the value is greater than the maximum volume supported, the maximum volume is used.

If the value is less than the minimum volume supported, the minimum volume is used.

For details about how to obtain the maximum value, minimum value, and current value, see [AudioVolumeGroupManager](../../arkts-apis/ohos-multimedia-audio-audio-management/interface-audiovolumegroupmanager/document.md).

 |
| volumeParameter | [AVVolumePanelParameter](#avvolumepanelparameter) | No | @Prop | 

Custom parameter of the volume panel.

If this parameter is not set, the volume bar appears at the system default location.

 |

#### AVVolumePanelParameter

Describes the volume panel parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Volume

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| position | [Position](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#position) | No | Yes | 
Position of the volume panel.

If this parameter is not set, the volume bar appears at the system default location.

If this parameter is set to a position within the screen, the volume bar appears at the specified location.

If this parameter is set to a position outside the screen, such as (-1, -1), the system volume bar is not displayed. In this case, you should consider implementing a custom volume bar.

 |

#### Events

The [universal events](../../../../application-framework/arkui/arkts-components/universal-events/document.md) are supported.

#### How to Use

1.  When implementing the custom volume bar, you are advised to use the volume change listening API of the audio framework. The application can determine whether to process the current data and display the custom volume bar based on the volume type (**volumeEvent.volumeType**), volume level (**volumeEvent.volume**), and whether to display the volume bar (**volumeEvent.updateUi**) in the API callback. For details, see [on('streamVolumeChange')](../../arkts-apis/ohos-multimedia-audio-audio-management/interface-audiovolumemanager/document.md#onstreamvolumechange20).
2.  To ensure users are aware of volume changes, applications are not allowed to adjust the volume in the background. The system will take corresponding control measures.

#### Example

To see how the volume panel works, refer to the sample code below. To experience the volume adjustment, you'll need to change the **volume** value or press the volume buttons.

import { AVVolumePanel } from '@kit.AudioKit';

@Entry
@Component
struct Index {

  @State volume: number = 0;

  build() {
    Row() {
      Column() {
        AVVolumePanel({
          volumeLevel: this.volume,
          volumeParameter: {
            position: {
              x: 100,
              y: 200
            }
          }
        })
      }
    }.width('50%').height('50%')
  }
}
