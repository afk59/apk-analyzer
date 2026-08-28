# HdsSideBar

This module provides a sidebar container that can be displayed or hidden, allowing you to customize the sidebar and content area.

**Start version**: 6.0.0(20)

#### Modules to Import

import { HdsSideBar } from '@kit.UIDesignKit';

#### API

HdsSideBar({contentAreaMask?: boolean, isShowSideBar?: boolean, $isShowSideBar?: Callback<boolean>, minSideBarWidth?: Length, maxSideBarWidth?: Length, minContentWidth?: Length, sideBarColor?: ResourceColor, contentColor?: ResourceColor, sideBarWidth?: Length, autoHide?: boolean, isSideBarBlur?: boolean, sideBarPosition?: sideBarPosition, onChange?: Callback<boolean>, sideBarPanelBuilder: CustomBuilder, contentPanelBuilder: CustomBuilder, sideBarContainerType?: SideBarContainerType})

**Decorator type**: @ComponentV2

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

contentAreaMask

 | 

boolean

 | 

No

 | 

@Param

 | 

Indicates whether to add an overlay to the content area when the sidebar of the **HdsSideBar** component is displayed in a floating manner.

**true**: yes **false**: no

The default value is **true**.

 |
| 

isShowSideBar

 | 

boolean

 | 

No

 | 

@Param

 | 

Indicates whether to display the sidebar of the **HdsSideBar** component.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

$isShowSideBar

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<boolean>

 | 

No

 | 

@Event

 | 

Callback for whether to display the sidebar after a sidebar control button of the **HdsSideBar** component is tapped.

 |
| 

minSideBarWidth

 | 

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

No

 | 

@Param

 | 

Minimum sidebar width of the **HdsSideBar** component.

The default value is 200 vp.

 |
| 

maxSideBarWidth

 | 

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

No

 | 

@Param

 | 

Maximum sidebar width of the **HdsSideBar** component.

The default value is 280 vp.

 |
| 

minContentWidth

 | 

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

No

 | 

@Param

 | 

Minimum content area width of the **HdsSideBar** component.

The default value is 360 vp.

 |
| 

sideBarColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

@Param

 | 

Sidebar background color of the **HdsSideBar** component.

The default value is **Color.Transparent**.

 |
| 

contentColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

@Param

 | 

Content area background color of the **HdsSideBar** component.

The default value is **Color.Transparent**.

 |
| 

sideBarWidth

 | 

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

No

 | 

@Param

 | 

Sidebar width of the **HdsSideBar** component.

The default value is 240 vp.

 |
| 

autoHide

 | 

boolean

 | 

No

 | 

@Param

 | 

Indicates whether to automatically hide the sidebar of the **HdsSideBar** component when it is dragged to be smaller than the minimum width.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

isSideBarBlur

 | 

boolean

 | 

No

 | 

@Param

 | 

Indicates whether to apply a blur effect to the sidebar of the **HdsSideBar** component when the window gains focus.

**true**: yes. The sidebar is blurred only when the window gains focus.

**false**: no

The default value is **true**.

 |
| 

sideBarPosition

 | 

[SideBarPosition](../../../arkui/arkts-components/grid-and-column-layout/sidebarcontainer/document.md#sidebarposition9)

 | 

No

 | 

@Param

 | 

Sidebar position of the **HdsSideBar** component.

The default value is **SideBarPosition.Start**, indicating that the sidebar is on the left side of the container.

 |
| 

onChange

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<boolean>

 | 

No

 | 

@Param

 | 

Triggered when the status of the sidebar of the **HdsSideBar** component switches between visible and hidden.

Callback trigger conditions:

1.  The value of the **isShowSideBar** attribute changes.
2.  The adaptation of the **isShowSideBar** attribute changes.
3.  **autoHide** is triggered upon divider dragging.

The options are **true** (visible) and **false** (hidden).

 |
| 

sideBarPanelBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

Yes

 | 

@Require

@BuilderParam

 | 

Sidebar child component of the **HdsSideBar** component.

 |
| 

contentPanelBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

Yes

 | 

@Require

@BuilderParam

 | 

Content area child component of the **HdsSideBar** component.

 |
| 

sideBarContainerType

 | 

[SideBarContainerType](../../../arkui/arkts-components/grid-and-column-layout/sidebarcontainer/document.md#sidebarcontainertype)

 | 

No

 | 

@Param

 | 

Sidebar display type of the **HdsSideBar** component.

The default value is **SideBarContainerType.AUTO**, indicating that the sidebar is nested in the component and displayed side by side with the content area.

 |

#### build

build(): void

Default constructor of a struct. This method cannot be directly called.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### Example

The **HdsSideBar** component provides a sidebar container that can be displayed or hidden, allowing you to customize the sidebar and content area.

import { HdsSideBar } from '@kit.UIDesignKit';

@Entry
@ComponentV2
struct Index {
  @Local isShowSidebar: boolean = true;

  // Sidebar area on the left.
  @Builder
  SideBarPanelBuilder() {
    Column() {
      Text('Sidebar area on the left')
    }
    .width('100%')
    .height('100%')
    .margin(40)
  }

  // Content area on the right.
  @Builder
  ContentPanelBuilder() {
    Text('Content area on the right')
      .margin(40)
  }

  @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
  @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder

  @Builder
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Button() {
        SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open\_sidebar') : $r('sys.symbol.close\_sidebar'))
          .fontWeight(FontWeight.Normal)
          .fontSize($r('sys.float.ohos\_id\_text\_size\_headline7'))
          .fontColor(\[$r('sys.color.ohos\_id\_color\_titlebar\_icon')\])
          .hitTestBehavior(HitTestMode.None)
      }
      .id('side\_bar\_button')
      .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
      .height(30)
      .width(30)
      .onClick(() => {
        this.isShowSidebar = !this.isShowSidebar;
      })
      .zIndex(1)
      .margin({ top: 10, left: 10 })

      HdsSideBar({
        sideBarPanelBuilder: (): void => {
          this.sideBarBuilder()
        },
        contentPanelBuilder: (): void => {
          this.contentBuilder()
        },
        sideBarContainerType: SideBarContainerType.Overlay,
        maxSideBarWidth: 100,
        isShowSideBar: this.isShowSidebar,
        $isShowSideBar: (isShowSidebar: boolean) => {
          this.isShowSidebar = !isShowSidebar
        },
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/q5RFFYvMSueV8IwJdZpcvQ/en-us_image_0000002532144163.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1FE7853D539204E1F28BD8A39F21E434C07D9EAC90BE45AE759DB40EB9762A6)
