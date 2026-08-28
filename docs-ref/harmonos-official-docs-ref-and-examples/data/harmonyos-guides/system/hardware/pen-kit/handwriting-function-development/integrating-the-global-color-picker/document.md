# Integrating the Global Color Picker

After the global color picker is integrated, users can use their finger or stylus to pick up an onscreen color after they lift the finger or stylus. The image information corresponding to the color value is generated.

#### Use Case

Use the global color picker in the app. The effect is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/z0OjkRV8RQuD_EzGMqQGNQ/en-us_image_0000002535422317.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8B8BAEF268C2C1D7E906D5415B8DB980F6C3367F545F148A0F8B19A739138EE "Click to enlarge")

The color value and color gamut of the selected position on the screen can be obtained.

#### Restrictions

The global color picker capability supports tablets and PCs/2-in-1 devices. Starting from version 5.1.1(19), phones are also supported.

#### API Description

| 
Class

 | 

API

 | 

Description

 |
| :-- | :-- | :-- |
| 

[imageFeaturePicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-imagefeaturepicker)

 | 

[pickForResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-imagefeaturepicker#section759192934316)

 | 

Starts the global color picker. This API is used to start the color picker. The color value is not displayed when the color picker is moved.

 |

#### Development Procedure

1\. Import required modules.

import { imageFeaturePicker } from '@kit.Penkit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Construct the Color picker capability.

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Column() {
        Row() {
          Button() {
            Text('Call GlobalColorPicker from ets side')
              .fontSize(18)
              .fontWeight(FontWeight.Normal)
          }
          .width('50%')
          .height('60vp')
          .align(Alignment.Center)
          .onClick((event) => {
            imageFeaturePicker.pickForResult(event.displayX, event.displayY)
              .then((colorInfo: imageFeaturePicker.PickedColorInfo) => {
                if (colorInfo) {
                  console.info('colorInfo=' + JSON.stringify(colorInfo));
                }
              }).catch((err: BusinessError) => {
              console.error(\`pickForResult failed. Code is ${err.code}, message is ${err.message}\`)
            })
          })
        }
      }
      .align(Alignment.Center)
    }
    .width('100%')
    .height('100%')
  }
}
