# Arc Button (ArcButton)

Supported since API version 18, the **ArcButton** component represents an arc button specifically designed for circular screens. It offers various button styles, such as emphasized, normal, and warning, tailored for watch UIs. For details, see [ArcButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton).

#### Creating a Button

To create an **ArcButton** component, use the following:

ArcButton({
  options: new ArcButtonOptions({
    label: 'OK',
    position: ArcButtonPosition.TOP\_EDGE,
    styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
  // ···
  })
})

[label](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions): sets the text displayed on the button.

[position](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions): sets the type of the button.

[styleMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions): sets the style mode of the button.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/GzJrZwOZSweTqREmJfPSMQ/en-us_image_0000002568764431.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76646E53CEC7CF2F8F703F3FDC5A7091990909E49C68755F84BB402B8D0FCF78)

#### Setting the Button Type

The **ArcButton** component offers two types: top arc button and bottom arc button. Use the [position](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions) attribute to set the type.

-   Lower arc button (default type)
    
    Set [position](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions) to **ArcButtonPosition.BOTTOM\_EDGE**.
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        position: ArcButtonPosition.BOTTOM\_EDGE,
        styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
      // ···
      })
    
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/HnCBmCC4TnGFYi2FeVjDwQ/en-us_image_0000002537764706.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F761C7C379D1F8F34AB586C87DB8B24AB965601A1C361508A34F53F170639038)
    
-   Upper arc button
    
    Set [position](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions) to **ArcButtonPosition.TOP\_EDGE**.
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        position: ArcButtonPosition.TOP\_EDGE,
        styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
      // ···
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/P7c6W0J2R3-4iaO7jv20Cg/en-us_image_0000002537924646.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD159EE43990BD4E833C8BAD142DA21FEDDC694E0E0EC566D8A2C9DDFD6F3AEF)
    

#### Customizing the Style

-   Setting the background color
    
    Use the [backgroundColor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions) attribute to set the background color of the button.
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        styleMode: ArcButtonStyleMode.CUSTOM,
        backgroundColor: ColorMetrics.resourceColor('#707070')
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/N8GxYx_PRMStvTGO5LBjhg/en-us_image_0000002568684423.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0098059178BBABDE63B1A309CAAFEF5DA6A0841C27AA50D6DDEBDF57DFE42DA8)
    
-   Setting the font color
    
    Use the [fontColor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions) attribute to set the font color of the button.
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        styleMode: ArcButtonStyleMode.CUSTOM,
        backgroundColor: ColorMetrics.resourceColor('#E84026'),
        fontColor: ColorMetrics.resourceColor('#707070')
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/LL3Ii-kZQQGO3w0R1LI4hw/en-us_image_0000002568764433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56BED27A91BCD20F101413AAFC428A6C17FB376556CEE4C1DC41D125BD85F691)
    
-   Setting the shadow color
    
    Enable the button shadow using the [shadowEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions) attribute and set the shadow color using the [shadowColor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions) attribute.
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        shadowEnabled: true,
        shadowColor: ColorMetrics.resourceColor('#ffec1022')
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/LXdb2XfOQJesHQqv4DL_oQ/en-us_image_0000002537764708.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0C20F694E2B302258E32803F6A369C2F199BC2229DE3C142E9E8B53C1EE5A7A)
    

#### Adding Events

-   Bind the **onClick** event to define custom behavior to be executed when the button is clicked.
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
      // ···
        onClick: () => {
          hilog.info(DOMAIN, TAG, 'ArcButton onClick');
        },
      })
    })
    
-   Bind the **onTouch** event to define custom behavior to be executed when the button is touched.
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
      // ···
        onTouch: (event: TouchEvent) => {
          hilog.info(DOMAIN, TAG, 'ArcButton onTouch');
        }
      })
    
    })
    

#### Example

This example demonstrates a brightness settings screen where a slider displays the current brightness level at 30%. When the reset button is clicked, the brightness value is reset to the default value of 50%.

To run this sample code, wearable device support is required. In the project configuration file [module.json5](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) located in the **src/main** directory, configure **wearable** under [devicetypes](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#devicetypes).

"module": {
  // ···
  "deviceTypes": \[
    "wearable"
  \],
  // ···
}

import { LengthMetrics, LengthUnit, ArcButton, ArcButtonOptions, ArcButtonStyleMode } from '@kit.ArkUI';

const BRIGHT\_NESS\_VALUE = 30;
const BRIGHT\_NESS\_VALUE\_DEFAULT = 50;

@Entry
@ComponentV2
struct BrightnessPage {
  @Local brightnessValue: number = BRIGHT\_NESS\_VALUE;
  private defaultBrightnessValue: number = BRIGHT\_NESS\_VALUE\_DEFAULT;

  build() {
    RelativeContainer() {
      // Replace $r('app.string.Brightness') with the actual resource file. In this example, the value in the resource file is "Set brightness."
      Text($r('app.string.Brightness'))
        .fontColor(Color.White)
        .id('id\_brightness\_set\_text')
        .fontSize(24)
        .margin({ top: 16 })
        .alignRules({
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })

      Text(\`${this.brightnessValue} %\`)
        .fontColor(Color.White)
        .id('id\_brightness\_min\_text')
        .margin({ left: 16 })
        .alignRules({
          start: { anchor: '\_\_container\_\_', align: HorizontalAlign.Start },
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center }
        })

      Slider({
        value: this.brightnessValue,
        min: 0,
        max: 100,
        style: SliderStyle.InSet
      })
        .blockColor('#191970')
        .trackColor('#ADD8E6')
        .selectedColor('#4169E1')
        .width(150)
        .id('id\_brightness\_slider')
        .margin({ left: 16, right: 16 })
        .onChange((value: number, mode: SliderChangeMode) => {
          this.brightnessValue = value;
        })
        .alignRules({
          center: { anchor: 'id\_brightness\_min\_text', align: VerticalAlign.Center },
          start: { anchor: 'id\_brightness\_min\_text', align: HorizontalAlign.End }
        })

      ArcButton({
        options: new ArcButtonOptions({
          // Replace $r('app.string.Reset') with the actual resource file. In this example, the value in the resource file is "Reset."
          label: $r('app.string.Reset'),
          styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
          fontSize: new LengthMetrics(19, LengthUnit.FP),
          onClick: () => {
            this.brightnessValue = this.defaultBrightnessValue;
          }
        })
      })
        .alignRules({
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center },
          bottom: { anchor: '\_\_container\_\_', align: VerticalAlign.Bottom }
        })
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Black)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/OnDG48mySuKhXKT-9bqwAw/en-us_image_0000002537924648.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6777099FFF12BB17CE98B82EA12F67D53634F899B8C86258636B5CEFA5808F3B)
