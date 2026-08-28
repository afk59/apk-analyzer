# Configuring a Component with a Primary Button

#### Use Case

The function of configuring a component with a primary button is available since version 6.0.0(20) Beta1.

The [HdsActionBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsactionbar) component supports the multi-button style. If your app requires multiple buttons that expand from and collapse into a primary button, you can configure the primary button's settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/zXrdmiJ0RD2wZbPq2mAguQ/en-us_image_0000002500424074.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47204CDD964FA50D69D72D892DB90ED747325110FF48E3811E1687FFE8EF23BB)

#### Development Procedure

1.  Import required modules.
    
    import { HdsActionBar, ActionBarButton, ActionBarStyle } from '@kit.UIDesignKit'
    
2.  Create **startButtons** (array of the buttons on the left of the primary button), **endButtons** (array of the buttons on the right of the primary button), and **primaryButton** (primary button). Then set the initial value of **isExpand** to **true**, indicating that the **HdsActionBar** is expanded initially. Tapping the primary button will collapse the other buttons, and tapping it again will expand them.
    
    @Entry
    @ComponentV2
    struct TestActionBar {
      @Local isExpand: boolean = true;
    
      @Local isPrimaryIconChanged: boolean = false;
    
      @Local primaryHoverTips: ResourceStr = 'Start';
    
      build() {
        Column() {
          HdsActionBar({
            startButtons: \[new ActionBarButton({
              baseIcon: $r('sys.symbol.stopwatch\_fill')
            })\],
            endButtons: \[new ActionBarButton({
              baseIcon: $r('sys.symbol.mic\_fill')
            })\],
            primaryButton: new ActionBarButton({
              baseIcon: $r('sys.symbol.plus'),
              altIcon: $r('sys.symbol.play\_fill'),
              onClick: () => {
                this.isExpand = !this.isExpand;
                this.isPrimaryIconChanged = !this.isPrimaryIconChanged;
                if (this.isPrimaryIconChanged) {
                  this.primaryHoverTips = 'Pause';
                } else {
                  this.primaryHoverTips = 'Start';
                }
              },
              hoverTips: this.primaryHoverTips
            }),
            actionBarStyle: new ActionBarStyle({
              isPrimaryIconChanged: this.isPrimaryIconChanged
            }),
            isExpand: this.isExpand!!
          })
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xF1F3F5)
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
      }
    }
