# Shadow Effect upon a Press

#### Use Case

The [shadow effect upon a press](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdseffect#section132615713716) is supported since version 6.0.0(20) Beta1.

Your app can call the API that implements the shadow effect upon a press to configure the background color change effect of a component when it is pressed.

#### Development Procedure

1.  Import the required module.
    
    import { hdsEffect } from '@kit.UIDesignKit';
    
2.  Create the shadow effect that takes effect upon a press.
    
    @Entry
    @Component
    struct PressShadowExample {
      @State button\_blend\_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
      @State button\_gradient\_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
    
      build() {
        NavDestination() {
          Column({ space: 50 }) {
            Button("BLEND\_WHITE", { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
              .visualEffect(new hdsEffect.HdsEffectBuilder()
                .pressShadow(this.button\_blend\_state)
                .buildEffect())
              .onTouch((event: TouchEvent) => {
                if (event.type === TouchType.Down) {
                  this.button\_blend\_state =  hdsEffect.PressShadowType.BLEND\_WHITE;
                } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
                  this.button\_blend\_state =  hdsEffect.PressShadowType.NONE;
                }
              })
    
            Button("GRADIENT", { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
              .visualEffect(new hdsEffect.HdsEffectBuilder()
                .pressShadow(this.button\_gradient\_state)
                .buildEffect())
              .onTouch((event: TouchEvent) => {
                if (event.type === TouchType.Down) {
                  this.button\_gradient\_state =  hdsEffect.PressShadowType.BLEND\_GRADIENT;
                } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
                  this.button\_gradient\_state =  hdsEffect.PressShadowType.NONE;
                }
              })
          }
          .height('70%')
          .justifyContent(FlexAlign.Center)
        }
        .width('100%')
        .height('100%')
        .title('Button example')
        .backgroundColor('#040404')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/MkDtYSYjQHKDmvc2N1oR7A/en-us_image_0000002532304095.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39DE2E742DE95C7932913884C96EE0C35459A1A605023A5F8140C2D0F1793FC7)
