# Configuring the Sheet Style

#### Use Case

The navigation component supports the sheet style and can blur the title bar under this style since version 6.0.0(20) Beta1.

This is suitable for the scenario of using the navigation component in a sheet. You can set [HdsNavigationTitleMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section26841314155317) to **MODAL** to make this happen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/rIiGB8peR0GTp8OPVUe0qA/en-us_image_0000002532304101.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12C129BECACD524A1C0CD68944098C55948F94CBA4F21B6EB21419E951FBCCA0 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
    import { HdsNavigation, HdsNavigationTitleMode, HdsNavigationAttribute } from '@kit.UIDesignKit';
    
2.  Create a level-1 navigation component and set **titleMode** to **HdsNavigationTitleMode.MODAL** to implement the sheet style for the title bar.
    
    @Entry
    @Component
    struct Index {
      build() {
        HdsNavigation() { // Create the **HdsNavigation** component.
        }
        .titleBar({
          content: {
            title: {mainTitle: 'MainTitle', subTitle: 'SubTitle'},
          }
        })
        .titleMode(HdsNavigationTitleMode.MODAL) // Implement the sheet style for the title bar of the **HdsNavigation** component.
      }
    }
