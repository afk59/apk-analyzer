# Toolbar Configuration

You can configure the toolbar for a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/H_mS_XaaTEyTcWsNQ8Nshw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73CCC900A0BC12B142445DD7371D2CAA758DFD3C1B96705214E398ACB5B032C9)

-   The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This toolbar is a universal attribute for components. Note the distinction from the toolbar attribute of the [Navigation](../../../navigation-and-switching/navigation/document.md) component.
    

#### toolbar

toolbar(value: CustomBuilder): T

Creates a toolbar (consisting of [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md) components) for the bound component in the window's top title bar section. The toolbar's position corresponds to the bound component's position in the layout. The [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) must consist of [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md) components for the toolbar to take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Mb-VDkbgTTyvggfB-2vavw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE61D29CAC9BADEFBE892272154AEE293192B0ACAE9D9970DC3FD237AA26889E)

This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Custom toolbar of the CustomBuilder type for the current component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/A7CbsAV-RVKDgxABo0U72A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F36FE34575606E213D81FEB42840780E36059D1AA1852C88163D4C75DA5274B5)

1.  Only fixed title bars are supported; floating title bars in three-button navigation mode are not supported.
    
2.  You can customize the toolbar layout and place it on the left or right side. However, if the number of elements exceeds the available space, layout truncation or focus frame overlap may occur, rendering some actions invisible or causing interaction conflicts. There is no automatic shrinking, so keep the number of elements reasonable.
    
3.  The toolbar only supports single-line layouts, so avoid putting multi-line elements in it.
    
4.  The toolbar only works when [NavigationMode](../../../navigation-and-switching/navigation/document.md#navigationmode9) is set to **Split**. It does not work when [NavigationMode](../../../navigation-and-switching/navigation/document.md#navigationmode9) is set to **Stack** or **Auto**.
    
5.  The title bar height dynamically adjusts based on the [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md) components on the toolbar:
    
    -   There is a default 4 vp margin between the [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md) components and the title bar.
    -   If the tallest [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md) component is less than or equal to 48 vp, the title bar height will adjust to 56 vp. This setting is suitable for universal components such as title bars, toolbars, and search bars.
    -   If the tallest [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md) component is between 48 vp and 56 vp, the title bar height will adjust to 64 vp. This setting is suitable for toolbars that display both icons and text.
    -   If the tallest [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md) component exceeds 56 vp, the title bar height will adjust to 72 vp. If it exceeds 64 vp, the title bar height will remain at 72 vp, and any excess area will be clipped.

#### Example

This example demonstrates how to: 1. Bind the universal **toolbar** attribute to a [Button](../../../buttons-and-selections/button/document.md) component under [Navigation](../../../navigation-and-switching/navigation/document.md), adding two button toolbar items at the start of the **Navbar** section in the title bar. 2. Bind the **toolbar** attribute to a [Text](../../../text-and-input/text/document.md) component under [NavDestination](../../../navigation-and-switching/navdestination/document.md) to add a slider and a search bar component as toolbar items at the end of the **NavDestination** section in the title bar.

// xxx.ets
@Entry
@Component
struct SideBarContainerExample {
  normalIcon: Resource = $r("app.media.startIcon")
  selectedIcon: Resource = $r("app.media.startIcon")
  @State arr: number\[\] = \[1, 2, 3\]
  @State current: number = 1
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack()

  @Builder
  MyToolBar() {
    ToolBarItem({ placement: ToolBarItemPlacement.TOP\_BAR\_LEADING }) {
      Button("left").height("30vp")
    }

    ToolBarItem({ placement: ToolBarItemPlacement.TOP\_BAR\_LEADING }) {
      Button("right").height("30vp")
    }
  }

  @Builder
  MyToolbarNavDest() {
    ToolBarItem({ placement: ToolBarItemPlacement.TOP\_BAR\_TRAILING }) {
      Slider().width("120vp")
    }

    ToolBarItem({ placement: ToolBarItemPlacement.TOP\_BAR\_TRAILING }) {
      Search().width("120vp")
    }
  }

  @Builder
  PageNavDest(name: string) {
    NavDestination() {
      Column() {
        Text("add toolbar")
          .fontSize(30)
          .toolbar(this.MyToolbarNavDest())
      }
      .backgroundColor(Color.Grey)
    }
  }

  build() {
    SideBarContainer(SideBarContainerType.Embed) {
      Column() {
        ForEach(this.arr, (item: number) => {
          Column({ space: 5 }) {
            Image(this.current === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
            Text("Index0" + item)
              .fontSize(25)
              .fontColor(this.current === item ? '#0A59F7' : '#999')
              .fontFamily('source-sans-pro,cursive,sans-serif')
          }
          .onClick(() => {
            this.current = item
          })
        }, (item: number) => item.toString())
      }.width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)
      .backgroundColor('#19000000')

      Navigation(this.navPathStack) {
        Column() {
          Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
            .width('20%')
            .height(40)
            .margin(20)
            .toolbar(this.MyToolBar)
          Button('showNavDest', { stateEffect: true, type: ButtonType.Capsule })
            .width('20%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.navPathStack.pushPath({ name: "1" })
            })
        }
        .width('100%')
        .height('100%')
      }
      .navBarPosition(NavBarPosition.Start)
      .navBarWidth("50%")
      .navBarWidthRange(\["25%", "70%"\])
      .hideBackButton(true)
      .navDestination(this.PageNavDest)
      .height('100%')
      .title('Navigation')
    }
    .sideBarWidth(150)
    .minSideBarWidth(50)
    .maxSideBarWidth(300)
    .minContentWidth(0)
    .onChange((value: boolean) => {
      console.info('status:' + value)
    })
    .divider({
      strokeWidth: '1vp',
      color: Color.Gray,
      startMargin: '4vp',
      endMargin: '4vp'
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/zLAIuxinSh-z0qGmyE4DYw/en-us_image_0000002568765213.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=887A8586330ACFA2B26427B502F22D47AC2EE72ADC8E68CF6FCA5B372B6221B9)
