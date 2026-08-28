# Point-Light Effect

#### Use Case

The [point-light effect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdseffect#section285511175574) is supported since version 6.0.0(20) Beta1.

You can call the point light API to set a component's emission and illumination effects, making the component interaction experience more immersive.

#### Restrictions

A component can be illuminated by a maximum of 12 light sources at the same time.

#### Development Procedure

1.  Import the required module.
    
    import { hdsEffect } from '@kit.UIDesignKit';
    
2.  Create a point-light effect. To configure the emission and illumination effects for a component, set the **sourceType** and **illuminatedType** attributes, respectively.
    
    The following code indicates that when the button in the center is tapped, a point-light effect is triggered, with repeated taps triggering different point-light effects.
    
    @Entry
    @Component
    struct Index {
      @State bloomValue: number = 0;
      @State index: number = 0;
      @State illuminatedType: hdsEffect.PointLightIlluminatedType = hdsEffect.PointLightIlluminatedType.NONE;
      @State button\_gradient\_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
      @State lightIntensity: number = 10;
      @State types: hdsEffect.PointLightIlluminatedType\[\] =
        \[hdsEffect.PointLightIlluminatedType.NONE, hdsEffect.PointLightIlluminatedType.BORDER,
          hdsEffect.PointLightIlluminatedType.CONTENT, hdsEffect.PointLightIlluminatedType.BORDER\_CONTENT,
          hdsEffect.PointLightIlluminatedType.DEFAULT\_FEATHERING\_BORDER\];
    
      build() {
        Flex({
          direction: FlexDirection.Column,
          justifyContent: FlexAlign.Center,
          alignItems: ItemAlign.Center,
        }) {
          // Vertical circulation.
          ForEach(Array<number>(4).fill(0), (row: number) => {
            Flex({
              direction: FlexDirection.Row,
              justifyContent: FlexAlign.Center,
              alignItems: ItemAlign.Center,
            }) {
              // Horizontal circulation.
              ForEach(Array<number>(4).fill(0), (col: number) => {
                Flex()
                  .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
                    illuminatedType: this.illuminatedType,
                  }).buildEffect())
                  .backgroundColor(0x808080)
                  .size({ width: 60, height: 60 })
                  .borderRadius(50)
                  .margin({ top: 20, right: 10, left: 10 }) // Add margins.
              })
            }
            .width('100%') // Set the width of the **Row** component to 100%.
          })
    
          Flex({
            direction: FlexDirection.Row,
            justifyContent: FlexAlign.Center, // Use **SpaceBetween** to evenly distribute spacing.
            alignItems: ItemAlign.Center,
          }) {
            Flex()
              .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
                illuminatedType: this.illuminatedType,
              }).buildEffect())
              .backgroundColor(0x808080)
              .size({ width: 60, height: 60 })
              .borderRadius(50)
              .margin({ top: 20, right: 10, left: 10 })
    
            Button('Tap to glow')
              .size({ width: 140, height: 60 })
              .backgroundColor(0x808080)
              .fontColor(0xADD8E6)
              .visualEffect(new hdsEffect.HdsEffectBuilder()
                .pressShadow(this.button\_gradient\_state)
                .pointLight({
                  options: {
                    color: Color.White,
                    intensity: this.lightIntensity,
                    height: 150
                  }
                })
                .pressShadow(this.button\_gradient\_state)
                .buildEffect())
              .onClick(() => {
                if (this.index <= 3) {
                  this.index++;
                  this.illuminatedType = this.types\[this.index\];
                  this.button\_gradient\_state = hdsEffect.PressShadowType.BLEND\_GRADIENT;
                }
                let message = 'NONE';
                if (this.illuminatedType == 1) {
                  message = 'BORDER';
                } else if (this.illuminatedType == 2) {
                  message = 'CONTENT';
                } else if (this.illuminatedType == 3) {
                  message = 'BORDER\_CONTENT';
                } else {
                  message = 'DEFAULT\_FEATHERING\_BORDER';
                }
                this.getUIContext().getPromptAction().showToast({
                  message: message,
                  duration: 2000,
                  bottom: '80%'
                });
              })
              .margin({ top: 20, right: 10, left: 10 })
    
            Flex()
              .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
                illuminatedType: this.illuminatedType,
              }).buildEffect())
              .backgroundColor(0x808080)
              .size({ width: 60, height: 60 })
              .borderRadius(50)
              .margin({ top: 20, right: 10, left: 10 })
          }
          .width('100%') // Set the width of the **Row** component to 100%.
    
          ForEach(Array<number>(4).fill(0), (row: number) => {
            Flex({
              direction: FlexDirection.Row,
              justifyContent: FlexAlign.Center,
              alignItems: ItemAlign.Center,
            }) {
              // Horizontal circulation.
              ForEach(Array<number>(4).fill(0), (col: number) => {
                Flex()
                  .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
                    illuminatedType: this.illuminatedType,
                  }).buildEffect())
                  .backgroundColor(0x808080)
                  .size({ width: 60, height: 60 })
                  .borderRadius(50)
                  .margin({ top: 20, right: 10, left: 10 })
              })
            }
            .width('100%') // Set the width of the **Row** component to 100%.
          })
        }
        .backgroundColor(Color.Black)
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ds_ygJAPRgyMGxKD1oV_Qg/en-us_image_0000002532144145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADF6C5AF7B312D616E944541ABD129080D5DCB2C0CAE0276F11216A9285A1906 "Click to enlarge")
