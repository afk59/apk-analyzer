# Configuring a Component Without a Primary Button

#### Use Case

The function of configuring a component without a primary button is available since version 6.0.0(20) Beta1.

The [HdsActionBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsactionbar) component supports the multi-button style. If your app requires multiple buttons without any primary button or the effect to expand or collapse buttons, you can just configure the settings for the buttons on the left and right.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/6XuIZeI7T8-0dUdHhLj9LQ/en-us_image_0000002532144167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FF4851553892AC3D16670B1AAA581ABB83B6D16B64401BB455C9290111EB066)

#### Development Procedure

1.  Import required modules.
    
    import { HdsActionBar, ActionBarButton } from '@kit.UIDesignKit'
    
2.  Create **startButtons** (array of the buttons on the left of the primary button) and **endButtons** (array of the buttons on the right of the primary button), without any primary button or the effect to expand or collapse buttons.
    
    @Entry
    @ComponentV2
    struct TestNoPrimaryButton {
    
      build() {
        Column() {
          HdsActionBar({
            startButtons: \[new ActionBarButton({
              baseIcon: $r('sys.symbol.stopwatch\_fill')
            }), new ActionBarButton({
              baseIcon: $r('sys.symbol.stopwatch\_fill')
            })\],
            endButtons: \[new ActionBarButton({
              baseIcon: $r('sys.symbol.mic\_fill')
            })\]
          })
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xF1F3F5)
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
      }
    }
