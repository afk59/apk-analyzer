# Configuring the Sidebar Half-Screen-based Center-Aligned Style

#### Use Case

The function of configuring the sidebar half-screen-based center-aligned style is available since version 6.0.0(20) Beta1.

The [HdsTabs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdstabs) container component supports a half-screen-based center-aligned sidebar layout. If tabs are arranged horizontally and the tab bar height is not defined, the default height 48 vp is used. If tabs are arranged vertically, the default width of the tab bar is 96 vp. Setting **barHeight** to a fixed value prevents the tab bar from extending beyond the bottom safe area. When **bottom** is set to **0** or is not explicitly set under **safeAreaPadding**, the tab bar is allowed to extend beyond the bottom safe area.

-   Half-screen-based center alignment

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/AV9YuY62Q02TgpY0WZmqVg/en-us_image_0000002500424098.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A94AC36380C5CF618C7BE8F95538A7327B469203DF05E74EB82387EA6CEC9CE "Click to enlarge")

-   Default widths of horizontal and vertical arrangements

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/E5Z-6ZU1RBmIFWGL2AcQsA/en-us_image_0000002500424096.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A116301D20555AF86A39A46EC4553AE4484DBD030A50DF762F6C6C647E09701 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vZmQJmmOQLWDy_iAnDK2bA/en-us_image_0000002500304246.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6F05226983E51A62632F54C7D99E2AE16795FB9C98AAF4E3243F4C45C88A4B2 "Click to enlarge")

#### Constraints

1.  The tab bar has been placed at the sidebar of the container and **vertical** is set to **true**.
2.  The tab bar uses **BottomTabBarStyle**.

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
    import { HdsTabs, ExtendBarMode, HdsTabsAttribute } from '@kit.UIDesignKit';
    
2.  Create a level-1 container component. Then set **barMode** to **ExtendBarMode.HALF\_SCREEN\_FIXED** for the **HdsTabs** component, and configure that the total height of all tabs is one fourth of the height of the **HdsTabs** component and the tabs are in the middle of a half screen.
    
    @Entry
    @Component
    struct Index {
      @State isVertical: boolean = false;
    
      build() {
        Column() {
          Column() {
            Row() {
              Button('verticalChange')
                .onClick(() => {
                  this.isVertical = !this.isVertical;
                })
            }
          }
          .margin({ top: 20 })
          .width('100%')
          .height('10%')
          HdsTabs({ barPosition: BarPosition.End }) {
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Yellow)
            }
            .tabBar(new BottomTabBarStyle($r('sys.media.ohos\_app\_icon'), 'Yellow'))
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Blue)
            }
            .tabBar(new BottomTabBarStyle($r('sys.media.ohos\_app\_icon'), 'Blue'))
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Pink)
            }
            .tabBar(new BottomTabBarStyle($r('sys.media.ohos\_app\_icon'), 'Pink'))
          }
          .vertical(this.isVertical)
          .barMode(ExtendBarMode.HALF\_SCREEN\_FIXED)
          .width('100%')
          .height('90%')
        }
      }
    }
