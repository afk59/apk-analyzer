# Configuring the Custom Area

#### Use Case

The navigation component supports setting the [stackBuilder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section156391311175017) and [bottomBuilder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section156391311175017) attributes for the title bar since version 6.0.0(20) Beta1.

When you need to add custom nodes to the title bar, such as inserting segmented buttons in the upper title bar region, or adding search boxes and tabs in the bottom title bar area, you can leverage the title bar custom area configuration capability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/oeHO2dIrQaeYiySQvrO3mQ/en-us_image_0000002532304109.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0506C7DD239BD690E01FEBC1D5422AF3BD2B1F90D37490D5E0F3ED63A07BDE8B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Ukr1oTRPRA2a1airZ25oRQ/en-us_image_0000002500304224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=902F4FD1F821D8E36E090169B6501481C022CB25F7DD00B01073E3256F5508D0 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
    import { HdsNavigation, BottomBuilderShowType, HdsNavigationAttribute } from '@kit.UIDesignKit';
    
2.  Create a level-1 navigation component. Then set the **stackBuilder** and **bottomBuilder** attributes of the **content** attribute in **titleBar** to use the custom area configuration function of the navigation component.
    
    @Entry
    @Component
    struct Index {
      @Builder
      StackBuilder() { // Customize the **StackBuilder** component.
        Column() {
          Button("Hello")
        }
        .height(56)
        .justifyContent(FlexAlign.Center)
      }
    
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
          content: { // Set the content area of the **HdsNavigation** component.
            title: { mainTitle: 'MainTitle', subTitle: 'SubTitle' },
            // Configure the **StackBuilder** area of the **HdsNavigation** component.
            stackBuilder: (): void => this.StackBuilder(),
            // Configure the **BottomBuilder** area of the **HdsNavigation** component, including the area height and display type.
            bottomBuilder: {
              builder: (): void => this.BottomBuilder(),
              height: 56,
              showType: BottomBuilderShowType.DIRECTLY\_SHOW
            }
          }
        })
      }
    }
