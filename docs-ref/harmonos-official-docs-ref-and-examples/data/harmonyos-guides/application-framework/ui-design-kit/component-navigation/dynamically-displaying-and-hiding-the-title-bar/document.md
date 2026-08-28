# Dynamically Displaying and Hiding the Title Bar

#### Use Case

The navigation component supports dynamically displaying and hiding the title bar and setting the display/hide types since version 6.0.0(20) Beta1.

If you want to dynamically hide the title bar, set the [dynamicHideTitleBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section96017217517) attribute. Note that the status bar can be hidden only after the title area is hidden.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/9izJj6l7RFuayg_RqVGb8Q/en-us_image_0000002532144139.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEA37AAF82D6E049E0ABF4FB5FDD7F9E364BF4CD0ADF4A2E9774ADC88A36B7EE "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
    import { HdsNavigation, BottomBuilderShowType, HideMode, HdsNavigationAttribute } from '@kit.UIDesignKit';
    
2.  Create a level-1 navigation component and set the **dynamicHideTitleBar** attribute to configure the hiding of the status bar, title area, and **BottomBuilder**.
    
    @Entry
    @Component
    struct Index {
      @Builder
      BottomBuilder() { // Customize the **BottomBuilder** component.
        Column() {
          Search()
        }
        .width('100%')
        .height(56)
        .backgroundColor(Color.Orange)
      }
    
      build() {
        HdsNavigation() { // Create the **HdsNavigation** component.
        }.titleBar({
          content: {
            title: { mainTitle: 'MainTitle', subTitle: 'SubTitle' },
            // Configure the **BottomBuilder** area of the **HdsNavigation** component, including the area height and display type.
            bottomBuilder: { builder: (): void => this.BottomBuilder(), height: 56, showType: BottomBuilderShowType.DIRECTLY\_SHOW }
          }
        })
        // Configure the dynamic display/hiding settings of the title bar for the **HdsNavigation** component, including whether to hide the title area, **bottomBuilder** area, and status bar area dynamically, hiding type, and minimum scrolling distance needed for the hiding to activate.
        .dynamicHideTitleBar({ hideTitleArea:true, hideBottomBuilder: true, hideStatusBar: false, mode: HideMode.SCROLL\_UP\_TO, hideOffset: 10 })
      }
    }
