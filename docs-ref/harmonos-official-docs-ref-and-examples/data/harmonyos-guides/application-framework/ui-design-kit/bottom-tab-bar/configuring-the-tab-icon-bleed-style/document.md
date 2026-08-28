# Configuring the Tab Icon Bleed Style

#### Use Case

The function of configuring the tab icon bleed style is available since version 6.0.0(20) Beta1.

The [HdsTabs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdstabs) container component can be extended to support the tab icon bleed style. You can achieve a tab height that extends beyond the **tabBar** by setting the tab's attributes and adding a custom component with a bleed effect. A tab icon can extend beyond the container by a maximum height of 4 vp.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/DGaeaSaLTWagYayVR_npHA/en-us_image_0000002500304248.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09FCCF14A21EB3084F6897A248D11F3D5CA017F1270BF0F2A86BA3C68C3B6E75 "Click to enlarge")

#### Constraints

The tab bar has been placed at the bottom of the container by setting **barPosition** to **BarPosition.End** and **vertical** to **false**.

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
    import { HdsTabs, HdsTabsAttribute } from '@kit.UIDesignKit';
    import { bleedIconStyle } from '@hms.hds.HdsStyle';
    
2.  Create a level-1 container component. Then set the tab bar style for the **TabContent** child component of the **HdsTabs** component.
    
    @Entry
    @Component
    struct Index {
      build() {
        Stack() {
          HdsTabs() {
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Yellow)
            }
            .tabBar(bleedIconStyle(() => {
              this.tabBuilder()
            }))
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Blue)
            }
            .tabBar(this.tabBuilder())
          }
          .vertical(false)
          .barPosition(BarPosition.End)
        }
      }
    
      @Builder
      tabBuilder() {
        Column() {
          Image($r('app.media.startIcon'))
            .width(48)
            .height(48)
            .borderRadius(24)
        }
      }
    }
