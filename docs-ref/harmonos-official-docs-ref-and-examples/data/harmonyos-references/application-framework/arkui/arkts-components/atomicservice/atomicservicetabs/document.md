# AtomicServiceTabs

**AtomicServiceTabs** is an advanced component designed to streamline the use of the **Tabs** component by limiting customization options. It restricts the display to a maximum of five tabs, with fixed styles, positions, and sizes for the tabs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Fz0LHH07RiWCVgzPOM55vQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AEAA26E75AFCAD04B442B67B18D85EDA5BE16D0B73E944227689DC5DBFA20B6)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### AtomicServiceTabs

AtomicServiceTabs({
   tabContents?: \[ TabContentBuilder?,
                    TabContentBuilder?,
                  TabContentBuilder?,
                  TabContentBuilder?,
                  TabContentBuilder?
                \],
   tabBarOptionsArray: \[ TabBarOptions,
                        TabBarOptions,
                        TabBarOptions?,
                        TabBarOptions?,
                        TabBarOptions?
                      \],
   tabBarPosition?: TabBarPosition,
   layoutMode?: LayoutMode,
   barBackgroundColor?: ResourceColor,
   index?: number,
   barOverlap?: boolean,
   controller?: TabsController,
   onChange?: Callback<number>,
   onTabBarClick?: Callback<number>,
   onContentWillChange?: OnContentWillChangeCallback,
})

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| tabContents | \[[TabContentBuilder?](#tabcontentbuilder),[TabContentBuilder?](#tabcontentbuilder), [TabContentBuilder?](#tabcontentbuilder),[TabContentBuilder?](#tabcontentbuilder), [TabContentBuilder?](#tabcontentbuilder)\] | No | @BuilderParam | 
Array of content view containers. The default value is empty.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| tabBarOptionsArray | \[[TabBarOptions](#tabbaroptions),[TabBarOptions](#tabbaroptions), [TabBarOptions?](#tabbaroptions),[TabBarOptions?](#tabbaroptions), [TabBarOptions?](#tabbaroptions)\] | Yes | @Prop | 

Array of tab bar container configurations.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| tabBarPosition | [TabBarPosition](#tabbarposition) | No | @Prop | 

Position of the tab bar. The default value is **TabBarPosition.Bottom**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| layoutMode18+ | [LayoutMode](../../navigation-and-switching/tabcontent/document.md#layoutmode10) | No | @Prop | 

Layout mode of the images and text on the bottom tab. The default value is **LayoutMode.VERTICAL**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| barBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | @Prop | 

Background color of the tab bar. The default value is transparent.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| index | number | No | @Prop | 

Index of the currently displayed tab. The index is zero-based.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| barOverlap | boolean | No | @Prop | 

Whether the tab bar overlaps the **TabContent** component with a blurred background effect. **true** means that the tab bar overlaps the **TabContent** component with a blurred background effect. Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| controller | [TabsController](../../navigation-and-switching/tabs/document.md#tabscontroller) | No | \- | 

Tab controller, which is used to control switching of tabs.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onChange | Callback<number> | No | \- | 

Callback invoked when a tab is switched.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onTabBarClick | Callback<number> | No | \- | 

Callback invoked when a tab is clicked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onContentWillChange | [OnContentWillChangeCallback](#oncontentwillchangecallback) | No | \- | 

Callback invoked when a new page is about to be displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### TabContentBuilder

type TabContentBuilder = () => void

Defines the content view container.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### TabBarOptions

#### \[h2\]constructor

constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr, unselectedColor?: ResourceColor, selectedColor?: ResourceColor)

A constructor used to create a **TabBarOptions** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [TabBarSymbol](../../navigation-and-switching/tabcontent/document.md#tabbarsymbol12) | Yes | Image for the tab. |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | Text of the tab. |
| unselectedColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | 
Color of the tab when it is not selected.

Default value: **#99182431**

 |
| selectedColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | 

Color of the tab when it is selected.

Default value: **#FF007DFF**

 |

#### TabBarPosition

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LEFT | 0 | The tab bar is on the left side of the screen. |
| BOTTOM | 1 | The tab bar is at the bottom of the screen. |

#### OnContentWillChangeCallback

type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean

Defines the callback function triggered when the page content changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| currentIndex | number | Yes | Index of the current tab. |
| comingIndex | number | Yes | Index of the tab to be switched to. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true**: Callback execution is successful. **false**: Callback execution failed. |

#### Example

## Example 1: Pure Text Style

// Index.ets
import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Home';
  @State onClickNumber: number = 0;
  @State currentIndex: number = 0;
  @State comingIndex: number = 0;
  onContentWillChangeCallBack:  OnContentWillChangeCallback = (currentIndex: number, comingIndex: number): boolean => {
    this.currentIndex = currentIndex;
    this.comingIndex = comingIndex;
    console.info('OnContentWillChangeCallback')
     return true;
  }
  onTabClick: Callback<number> = (index:number)=>{
    this.onClickNumber ++;
    console.info('onTabClick');
  }
  @Builder
  tabContent1() {
    Column().width('100%').height('100%').alignItems(HorizontalAlign.Center).backgroundColor('#00CB87')
  }

  @Builder
  tabContent2() {
    Column().width('100%').height('100%').backgroundColor('#007DFF')
  }

  @Builder
  tabContent3() {
    Column().width('100%').height('100%').backgroundColor('#FFBF00')
  }

  build() {
    Stack() {
    AtomicServiceTabs({
      tabContents: \[
        () => {
          this.tabContent1()
        },
        () => {
          this.tabContent2()
        },
        () => {
          this.tabContent3()
        }
      \],
      tabBarOptionsArray: \[
        new TabBarOptions('', 'Green', Color.Black, Color.Green),
        new TabBarOptions('', 'Blue', Color.Black, Color.Blue),
        new TabBarOptions('', 'Yellow', Color.Black, Color.Yellow),
      \],
      tabBarPosition: TabBarPosition.BOTTOM,
      barBackgroundColor: $r('sys.color.ohos\_id\_color\_bottom\_tab\_bg'),
      onTabBarClick:this.onTabClick,
      onContentWillChange: this.onContentWillChangeCallBack,
    })
    Column() {
      Text("onchange callback times:" + this.onClickNumber)
      Text("comingIndex = " + this.comingIndex + ", currentIndex = " + this.currentIndex)
    }.margin({top:500})
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/JWxZK5KtSNGxjtM8sog0QQ/en-us_image_0000002537765950.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDF98296DBDD747073FE6D4A093819F8C9F5B79F4D58F7367C50DB5BFC5BB0C8)

## Example 2: Pure Icon Style

// Index.ets
import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Home';
  @State onClickNumber: number = 0;
  @State currentIndex: number = 0;
  @State comingIndex: number = 0;
  onContentWillChangeCallBack: OnContentWillChangeCallback = (currentIndex: number, comingIndex: number): boolean => {
    this.currentIndex = currentIndex;
    this.comingIndex = comingIndex;
    console.info('OnContentWillChangeCallback');
    return true;
  }
  onTabClick: Callback<number> = (index:number)=>{
    this.onClickNumber ++;
    console.info('onTabClick');
  }
  @Builder
  tabContent1() {
    Column().width('100%').height('100%').alignItems(HorizontalAlign.Center).backgroundColor('#00CB87')
  }

  @Builder
  tabContent2() {
    Column().width('100%').height('100%').backgroundColor('#007DFF')
  }

  @Builder
  tabContent3() {
    Column().width('100%').height('100%').backgroundColor('#FFBF00')
  }

  build() {
    Stack() {
    AtomicServiceTabs({
      tabContents: \[
        () => {
          this.tabContent1()
        },
        () => {
          this.tabContent2()
        },
        () => {
          this.tabContent3()
        }
      \],
      tabBarOptionsArray: \[
        new TabBarOptions($r('sys.media.ohos\_ic\_public\_phone'), '', Color.Black, Color.Blue),
        new TabBarOptions($r('sys.media.ohos\_ic\_public\_location'), '', Color.Black, Color.Blue),
        new TabBarOptions($r('sys.media.ohos\_ic\_public\_more'), '', Color.Black, Color.Blue),
      \],
      tabBarPosition: TabBarPosition.BOTTOM,
      barBackgroundColor: $r('sys.color.ohos\_id\_color\_bottom\_tab\_bg'),
      onTabBarClick:this.onTabClick,
      onContentWillChange: this.onContentWillChangeCallBack,
    })
    Column() {
      Text("onchange callback times:" + this.onClickNumber)
      Text("comingIndex = " + this.comingIndex + ", currentIndex = " + this.currentIndex)
    }.margin({top:500})
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-EKJDeKmSeW-9058iZuNuA/en-us_image_0000002537925890.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=024CDAB470FE57A5ECE6C11D77938C669CF041D25778CF7BF9A891B19228C8B3)

## Example 3: Custom Layout with Text and Icons

// Index.ets
import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';

@Entry
@Component
struct AtomicserviceTabs  {
  @State flag: boolean = false;
  @State message: string = 'Home';
  @State onClickNumber: number = 0;
  @State currentIndex: number = 0;
  @State comingIndex: number = 0;
  @State layoutMode: LayoutMode = LayoutMode.VERTICAL;
  onContentWillChangeCallBack: OnContentWillChangeCallback = (currentIndex: number, comingIndex: number): boolean => {
    this.currentIndex = currentIndex;
    this.comingIndex = comingIndex;
    console.info('OnContentWillChangeCallback');
    return true;
  }
  onTabClick: Callback<number> = (index: number) => {
    this.onClickNumber++;
    console.info('onTabClick');
  }
  onChange: Callback<number, void> = (Index: number) => {
    console.info('onChange');
    console.info('onChange2');
  }

  @Builder
  tabContent1() {
    Column().width('100%').height('100%').alignItems(HorizontalAlign.Center).backgroundColor('#00CB87')
  }

  @Builder
  tabContent2() {
    Column().width('100%').height('100%').backgroundColor(Color.Blue)
  }

  @Builder
  tabContent3() {
    Column().width('100%').height('100%').backgroundColor('#FFBF00')
  }

  build() {
    Stack() {
      AtomicServiceTabs({
        tabContents: \[
          () => {
            this.tabContent1()
          },
          () => {
            this.tabContent2()
          },
          () => {
            this.tabContent3()
          },
        \],
        tabBarOptionsArray: \[
        new TabBarOptions($r('sys.media.ohos\_ic\_public\_phone'), 'Green', Color.Black, Color.Blue),
        new TabBarOptions($r('sys.media.ohos\_ic\_public\_location'), 'Blue', Color.Black, Color.Blue),
        new TabBarOptions($r('sys.media.ohos\_ic\_public\_more'), 'Yellow', Color.Black, Color.Blue),
        \],
        tabBarPosition: TabBarPosition.BOTTOM,
        barBackgroundColor: $r('sys.color.ohos\_id\_color\_bottom\_tab\_bg'),
        onTabBarClick: this.onTabClick,
        onContentWillChange: this.onContentWillChangeCallBack,
        onChange: this.onChange,
        layoutMode: this.layoutMode,
      })

      Column() {
        Button("Vertical Layout")
          .width('30%')
          .height(50)
          .margin({ top: 5 })
          .onClick((event?: ClickEvent) => {
            this.layoutMode = LayoutMode.VERTICAL;
          })
        Button("Horizontal Layout")
          .width('30%')
          .height(50)
          .margin({ top: 5 })
          .onClick((event?: ClickEvent) => {
            this.layoutMode = LayoutMode.HORIZONTAL;
          })
      }.margin({ top: 10 })
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/4Kbxf2GuTJ6QcZYGFY6dLw/en-us_image_0000002568685667.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A29165EAA518F0C98E715D4899F1EA8120048399F2E53B38156D575A90802B93)
