# Setting the Tab Bar Blur Style

#### Use Case

The function of setting the tab bar blur style is available since version 6.0.0(20) Beta1.

The [HdsTabs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdstabs) container component supports setting the direct blur and gradient blur effects for the tab bar.

-   Direct blur

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/gkofOf7tSYi8aG-bulf4kQ/en-us_image_0000002500424066.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=958A07F4FD9EB7C0CD9B580297E8B974CAD43222FCB22F3F4A9AFDABA934C61C "Click to enlarge")

-   Gradient blur

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/24jNZbSqSjOzPavPXsKcOg/en-us_image_0000002532144135.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D650D373424CE9A141E7941FD1D22E80B7D25096B54D01A2A59BA500C33B2ADB "Click to enlarge")

#### Constraints

1.  The tab bar has been placed at the bottom of the container by setting **barPosition** to **BarPosition.End** and **vertical** to **false**.
2.  The **TabBar** is overlaid on top of the **TabContent** by setting **barOverlap** to **true**.
3.  The value of **barBackgroundBlurStyle** for the **TabBar** is set to **BlurStyle.NONE**.

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
    import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';
    
2.  Create a level-1 container component. Then set the **barBackgroundStyle** attribute for the **HdsTabs** component to customize the color and height of the blur to implement gradient blur.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/yBhImy5JRW2CP4zrRUktgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=814C7427CB3F55B6057D4E5F5F7E66592BAE3AAA7152F8A6E1823187540AB7B1)
    
    1.  If you use the **barBackgroundBlurStyle** attribute of the **Tabs** component to set the blur effect, the default blur effect of the **HdsTabs** component does not take effect.
    2.  If you use the **barBackgroundEffect** attribute of the **Tabs** component to set the blur effect, the default blur effect of the **HdsTabs** component does not take effect.
    3.  If you use the **barBackgroundColor** attribute of the **Tabs** component to set the background color, the default blur effect of the **HdsTabs** component applies only to the blur radius (80 vp).
    
    @Entry
    @Component
    struct Index {
      private controller: HdsTabsController = new HdsTabsController();
    
      build() {
        Column() {
          HdsTabs({ controller: this.controller }) {
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Pink)
            }
            .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar 1' })
    
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Blue)
            }
            .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar2' })
          }
          .barOverlap(true)
          .barPosition(BarPosition.End)
          .vertical(false)
          .barBackgroundStyle({
            maskColor: Color.Yellow,
            maskHeight: 80
          })
        }
      }
    }
