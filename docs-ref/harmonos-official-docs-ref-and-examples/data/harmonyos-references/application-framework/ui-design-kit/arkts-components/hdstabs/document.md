# HdsTabs

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/oXj0C1oaTrq-KBv7NdvRoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A67C7CF34B600AB30BA39DD60734CBDAE43C165836ED1AB10EB6D5E560DDBC2)

This component is not supported for TVs.

This module provides the divider style, blur style, and half-screen center-aligned sidebar style of the **Tabs** container component.

The **HdsTabs** component is the root view container, which is generally used as the root container of pages. The **HdsTabs** component consists of the content area and tab bar. By default, the content on the first tab is displayed in the content area. Users can swipe or tap tabs to switch the content.

**Start version**: 6.0.0(20)

#### Modules to Import

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/1SyP-3IcQFWtLFEjz9MLcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B879F0FD609CCD087B6EBE78889A2B7231392889EDC17DB6EDF97AEE80B4499D)

-   **HdsTabsAttribute** is essential for configuring the **HdsTabs** component. In version 6.0.1(21) and earlier, you must manually import **HdsTabsAttribute** after importing the **HdsTabs** component. Otherwise, a compilation error is reported. However, starting from version 6.0.2(22), the compilation toolchain automatically imports **HdsTabsAttribute** when it detects the **HdsTabs** component, so manual import is no longer necessary.
-   If you manually import **HdsTabsAttribute**, DevEco Studio shows it as disabled (grayed out). In version 6.0.1(21) and earlier, removing this import causes a compilation error. But from version 6.0.2(22) onward, removing it does not affect the functionality.

Version 6.0.1(21) and earlier:

import { HdsTabs, HdsTabsController, HdsTabsAttribute } from '@kit.UIDesignKit';

Version 6.0.2(22) and later:

import { HdsTabs, HdsTabsController } from '@kit.UIDesignKit';

#### Child Components

The involved child component is [TabContent](../../../arkui/arkts-components/navigation-and-switching/tabcontent/document.md).

**Device behavior**: This API has no effect on TVs and works on other devices.

#### API

HdsTabs(options?: HdsTabsOptions)

Creates an **HdsTabs** container.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[HdsTabsOptions](#section194091491257)

 | 

No

 | 

Parameters of the **HdsTabs** component.

 |

#### HdsTabsOptions

Inherits from [TabsOptions](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#tabsoptions15) and defines parameters of the **HdsTabs** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

controller

 | 

[HdsTabsController](#section13103111423616)

 | 

No

 | 

Yes

 | 

**HdsTabs** controller.

The default value is **undefined**.

 |

#### HdsTabsController

Controller of the **HdsTabs** component, which is used to control switching of tabs and inherits [TabsController](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#tabscontroller). One **HdsTabsController** cannot control multiple **HdsTabs** components.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

#### \[h2\]bindScroller

bindScroller(value: number, scroller: Scroller, parentScroller?: Scroller): void

Binds the scrollable component of the content area to the **HdsTabs** controller.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

number

 | 

Yes

 | 

Index of a tab. The index starts from 0.

 |
| 

scroller

 | 

[Scroller](../../../arkui/arkts-components/scroll-and-swipe/scroll/document.md#scroller)

 | 

Yes

 | 

Controller of the scrollable component.

 |
| 

parentScroller

 | 

[Scroller](../../../arkui/arkts-components/scroll-and-swipe/scroll/document.md#scroller)

 | 

No

 | 

Parent controller of the scrollable component.

 |

#### \[h2\]unbindScroller

unbindScroller(scroller: Scroller): void

Unbinds the scrollable component of the content area from the **HdsTabs** controller.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

scroller

 | 

[Scroller](../../../arkui/arkts-components/scroll-and-swipe/scroll/document.md#scroller)

 | 

Yes

 | 

Controller of the scrollable component.

 |

#### Attributes

In addition to [universal attributes](../../../arkui/arkts-components/universal-attributes/document.md), the following attributes are supported.

#### \[h2\]vertical

vertical(value: boolean)

Sets whether to use vertical tabs.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

boolean

 | 

Yes

 | 

Indicates whether to use vertical tabs.

The options are **true** (vertical) and **false** (horizontal).

The default value is **false**.

If set to have an **auto** height, horizontal tabs auto-adapt the height to child components, which is calculated as follows: Tab bar height + Divider width + Tab content height + Top and bottom paddings + Top and bottom border widths.

If set to have an **auto** width, vertical tabs auto-adapt the width to child components, which is calculated as follows: Tab bar width + Divider width + Tab content width + Left and right paddings + Left and right border widths.

To avoid animation jitter when switching between tabs, maintain a consistent size for child components on each tab.

 |

#### \[h2\]barPosition

barPosition(value: BarPosition)

Sets the position of the **Tabs** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[BarPosition](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#barposition)

 | 

Yes

 | 

Position of the **Tabs** component.

The default value is **BarPosition.Start**.

 |

#### \[h2\]scrollable

scrollable(value: boolean)

Sets whether the tabs can be switched via swipe gestures.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

boolean

 | 

Yes

 | 

Indicates whether the tabs can be switched via swipe gestures.

The options are **true** (yes) and **false** (no).

The default value is **true**.

 |

#### \[h2\]barWidth

barWidth(value: Length)

Sets the width of the tab bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

Yes

 | 

Width of the tab bar, in vp. If the specified value is less than 0 or greater than the width of the **Tabs** component, the default value is used.

Default value:

-   If the tab bar has the **vertical** attribute set to **false** and does not have [SubTabBarStyle](../../../arkui/arkts-components/navigation-and-switching/tabcontent/document.md#subtabbarstyle9) or [BottomTabBarStyle](../../../arkui/arkts-components/navigation-and-switching/tabcontent/document.md#bottomtabbarstyle9) specified, the default value is the width of the **Tabs** component.
-   If the tab bar has the **vertical** attribute set to **true** and does not have **SubTabBarStyle** or **BottomTabBarStyle** specified, the default value is 56 vp.
-   If **SubTabBarStyle** is set and the **vertical** attribute is **false**, the default value is the width of the **Tabs** component.
-   If **SubTabBarStyle** is set and the **vertical** attribute is **true**, the default value is 56 vp.
-   If **BottomTabBarStyle** is set and the **vertical** attribute is **true**, the default value is 96 vp.
-   If **BottomTabBarStyle** is set and the **vertical** attribute is **false**, the default value is the width of the **Tabs** component.

 |

#### \[h2\]barHeight

barHeight(value: Length)

Sets the height of the tab bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

Yes

 | 

Height of the tab bar. The unit is vp. If this parameter is set to **'auto'**, which takes effect only when tabs are arranged horizontally, the tab bar adapts to the height of its child components. If the specified value is less than 0 or greater than the height of the **Tabs** component, the default value is used.

Default value:

-   If the tab bar has the **vertical** attribute set to **false** and does not have a style specified, the default value is 48 vp.
-   If the tab bar has the **vertical** attribute set to **true** and does not have a style specified, the default value is the height of the **Tabs** component.
-   If [SubTabBarStyle](../../../arkui/arkts-components/navigation-and-switching/tabcontent/document.md#subtabbarstyle9) is set and the **vertical** attribute is **false**, the default value is 48 vp. If **SubTabBarStyle** is set and the **vertical** attribute is **true**, the default value is the height of the **Tabs** component.
-   If [BottomTabBarStyle](../../../arkui/arkts-components/navigation-and-switching/tabcontent/document.md#bottomtabbarstyle9) is set and the **vertical** attribute is **true**, the default value is the height of the **Tabs** component.
-   If **BottomTabBarStyle** is set and the **vertical** attribute is **false**, the default value is 48 vp.

 |

#### \[h2\]animationDuration

animationDuration(value: number)

Sets the animation duration for tab switching initiated by tapping a specific tab or by calling the **changeIndex** API of **HdsTabsController**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

number

 | 

Yes

 | 

Time required to complete the tab switching animation, which is initiated by tapping a specific tab or by calling the **changeIndex** API of **TabsController**.

Default value:

-   If this parameter is set to an invalid value or not set when a tab bar with **BottomTabBarStyle** set exists, the default value is **0**.
-   If no tab bar is set with **BottomTabBarStyle**, the default value is **300**.

Unit: millisecond

Value range: \[0, +∞)

 |

#### \[h2\]barOverlap

barOverlap(value: boolean)

Sets whether the tab bar overlaps the **TabContent** component with a blurred background effect.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

boolean

 | 

Yes

 | 

Indicates whether the tab bar overlaps the **TabContent** component with a blurred background effect.

**true**: The tab bar overlaps the **TabContent** component with a blurred background effect, and the default blur style of the tab bar is set to **'BlurStyle.COMPONENT\_THICK'**.

**false**: The style does not take effect.

The default value is **false**.

 |

#### \[h2\]barBackgroundColor

barBackgroundColor(value: ResourceColor)

Sets the background color of the tab bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

Yes

 | 

Background color of the tab bar.

The default value is **Color.Transparent**.

 |

#### \[h2\]barBackgroundBlurStyle

barBackgroundBlurStyle(style: BlurStyle, options?: BackgroundBlurStyleOptions)

Defines the blur style to apply between the background and content of the tab bar. It encapsulates various blur radius, overlay color, overlay opacity, saturation, and brightness options through enum values.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

style

 | 

[BlurStyle](../../../arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#blurstyle9)

 | 

Yes

 | 

Background blur style.

 |
| 

options

 | 

[BackgroundBlurStyleOptions](../../../arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10)

 | 

No

 | 

Background blur style options.

 |

#### \[h2\]barBackgroundEffect

barBackgroundEffect(options: BackgroundEffectOptions)

Sets the background effect of the tab bar, including the blur radius, brightness, saturation, and color.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[BackgroundEffectOptions](../../../arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11)

 | 

Yes

 | 

Background effect of the tab bar, including the blur radius, brightness, saturation, and color.

 |

#### \[h2\]barMode

barMode(value: HdsBarMode, options?: ScrollableBarModeOptions)

Sets the tab bar layout mode.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[HdsBarMode](#section880135003119)

 | 

Yes

 | 

The width of each tab bar is determined by the actual layout. When this parameter is set to **BarMode.Scrollable**, the tabs are scrollable in the following case: In horizontal layout, the total width exceeds the tab bar width; in vertical layout, the total height exceeds the tab bar height. When this parameter is set to **HALF\_SCREEN\_FIXED**, the total height of all tabs is one fourth of the height of the **HdsTabs** component and the tabs are in the middle of a half screen.

NOTE:

Prerequisites for using **HALF\_SCREEN\_FIXED**:

1.  The tab bar is placed at the sidebar of the container and **vertical** is set to **true**.
2.  The tab bar uses **BottomTabBarStyle**.

 |
| 

options

 | 

[ScrollableBarModeOptions](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#scrollablebarmodeoptions10)

 | 

No

 | 

Layout style of the tab bar in scrollable mode.

NOTE:

This parameter takes effect only when tabs are arranged horizontally (**vertical** set to **false**).

 |

#### \[h2\]divider

divider(value: Optional<HdsDividerStyle>)

Sets the divider between the **TabBar** and **TabContent** components.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<[HdsDividerStyle](#section9535642152319)\>

 | 

Yes

 | 

Divider style. By default, the divider displays/hides with scrolling motion.

**mode**: divider mode, including always visible, always hidden, and visible/hidden with scrolling motion (when the content area extends beyond the tab bar).

**style**: divider style.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ZBojifrYSUKWhPwI0c3ziQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AAA18BAC9AB914B29C92AFDFAE08BDECCEB9AAB43952084C4149534EA3677CC)

1\. To use this setting, the tab bar should be placed at the bottom of the container by setting **barPosition** to **BarPosition.End** and **vertical** to **false**.

2\. The effect of displaying/hiding the divider with scrolling motion is available only to components that use common APIs for scrolling. For other types of components, you need to implement this functionality by yourself.

3\. To support the effect of display/hiding with scrolling motion, the corresponding list scrolling controller needs to be bound to the **HdsTabs** controller.

#### \[h2\]barBackgroundStyle

barBackgroundStyle(backgroundStyle: Optional<HdsTabsBackgroundStyle>)

Sets the blur style to gradient blur.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

backgroundStyle

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<[HdsTabsBackgroundStyle](#section86661977269)\>

 | 

Yes

 | 

Color and height of the blur effect. The blur effect does not take effect by default.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/0VDMyv2mQKaiOyjYgB2Fxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27B8B9B628816A2B0DBD53C12650E2029A13985A655DA3BB9266C26222E862A2)

1\. To use this setting, the tab bar should be placed at the bottom of the container by setting **barPosition** to **BarPosition.End** and **vertical** to **false**.

2\. The **TabBar** is overlaid on top of the **TabContent** by setting **barOverlap** to **true**.

3\. The default value of **barBackgroundBlurStyle** for the **TabBar** is changed to **BlurStyle.NONE**.

#### \[h2\]blurStrategy

blurStrategy(value: BlurStrategy)

Sets the effective strategy for the blur type of the tab bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[BlurStrategy](../hdsnavigation/document.md#section1086755971212)

 | 

Yes

 | 

Effective strategy for the blur type of the tab bar.

The default value is **BlurStrategy.ADAPTIVE**.

 |

#### HdsDividerStyle

Sets the tab bar divider.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

mode

 | 

[DividerMode](#section186781730153111)

 | 

No

 | 

No

 | 

Display mode of the tab bar divider.

The default value is **DividerMode.FOLLOW\_SCROLL**.

 |
| 

style

 | 

[DividerStyle](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#dividerstyle10)

 | 

No

 | 

Yes

 | 

Tab bar divider style.

Default value:

{strokeWidth: '1px', color: '#33000000'}

 |

#### HdsTabsBackgroundStyle

Defines the gradient blur style.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maskColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Gradient blur color.

The default value is **#CCFFFFFF**.

 |
| 

maskHeight

 | 

number

 | 

No

 | 

Yes

 | 

Gradient blur height.

Default value: component height (including the tab bar height at the bottom) + 32 vp

 |

#### Events

#### \[h2\]onChange

onChange(event: Callback<number>)

Triggered when tabs at the bottom are switched.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

event

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<number>

 | 

Yes

 | 

Triggered when tabs at the bottom are switched, which will be used to obtain the tab subscript after switching.

 |

#### \[h2\]onAnimationStart

onAnimationStart(handler: OnTabsAnimationStartCallback)

Triggered when the switching animation starts. This event is not triggered when [animationDuration](#section13511122142) is set to **0**, which effectively disables the animation.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

handler

 | 

[OnTabsAnimationStartCallback](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#ontabsanimationstartcallback18)

 | 

Yes

 | 

Triggered when the switching animation starts.

 |

#### \[h2\]onContentWillChange

onContentWillChange(handler: OnTabsContentWillChangeCallback)

Triggered when a new tab page is about to be displayed.

This event is triggered when any of the following occurs:

1\. When the user swipes through the **TabContent** to switch to a new page.

2\. When **TabsController.changeIndex** is called to switch to a new page.

3\. When the **index** attribute is changed to switch to a new page.

4\. When the user taps a tab on the tab bar to switch to a new page.

5\. When the user presses the left or right arrow key on the keyboard to switch to a new page while the tab bar has focus.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

handler

 | 

[OnTabsContentWillChangeCallback](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#ontabscontentwillchangecallback18)

 | 

Yes

 | 

Handler triggered when a new tab page is about to be displayed.

 |

#### \[h2\]onTabBarClick

onTabBarClick(event: Callback<number>)

Triggered when a tab is tapped.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

Parameters:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

event

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<number>

 | 

Yes

 | 

Index of the tapped tab. The index starts from 0.

 |

#### ExtendBarMode

Enumerates layout modes of the tab bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

HALF\_SCREEN\_FIXED

 | 

100

 | 

Half-screen, center-aligned sidebar layout.

 |

#### DividerMode

Enumerates display modes of the tab bar divider.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

VISIBLE

 | 

0

 | 

Display mode of the tab bar divider: always visible.

 |
| 

NONE

 | 

1

 | 

Display mode of the tab bar divider: always hidden.

 |
| 

FOLLOW\_SCROLL

 | 

2

 | 

Display mode of the tab bar divider: visible/hidden with scrolling motion.

 |

#### HdsBarMode

type HdsBarMode= ExtendBarMode | BarMode

Sets the layout mode and extension mode of the tab bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ExtendBarMode](#section15758214103115)

 | 

Extension mode of the tab bar.

 |
| 

[BarMode](../../../arkui/arkts-components/navigation-and-switching/tabs/document.md#barmode)

 | 

Layout mode of the tab bar.

 |

#### bleedIconStyle

bleedIconStyle(builder: CustomTabBuilder): void

Customizes the tab icon bleed style for the **TabsContent** component.

**Decorator type**: @Builder

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

builder

 | 

[CustomTabBuilder](#section1434192490)

 | 

Yes

 | 

Bleed style of a custom component.

 |

#### CustomTabBuilder

type CustomTabBuilder= () => void

Defines a custom component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 6.0.0(20)

#### Example

#### \[h2\]Displaying/Hiding the Tab Bar Divider

You can set the tab bar divider style to support display modes, including always visible, always hidden, and visible/hidden with scrolling motion.

**Device behavior**: This API has no effect on TVs and works on other devices.

// Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
import { 
  HdsTabs,
  HdsTabsAttribute,
  HdsTabsController,
  DividerMode } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  private controller: HdsTabsController = new HdsTabsController();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8\];
  @State mode: DividerMode = DividerMode.FOLLOW\_SCROLL;
  listScroller0: ListScroller = new ListScroller();
  listScroller1: ListScroller = new ListScroller();

  aboutToAppear(): void {
    this.controller.bindScroller(0, this.listScroller0);
    this.controller.bindScroller(1, this.listScroller1);
  }

  aboutToDisappear(): void {
    this.controller.unbindScroller(this.listScroller0);
    this.controller.unbindScroller(this.listScroller1);
  }

  build() {
    Column() {
      Column() {
        Row() {
          Text('Show divider:')
            .width('25%')
          Button('Visible')
            .onClick(() => {
              this.mode = DividerMode.VISIBLE; // Set the divider to be always visible.
            })
          Button('None')
            .onClick(() => {
              this.mode = DividerMode.NONE; // Set the divider to be always hidden.
            })
          Button('Follow Scroll')
            .onClick(() => {
              this.mode = DividerMode.FOLLOW\_SCROLL;  // Set the divider to be always visible/hidden with scrolling motion.
            })
        }
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('10%')

      HdsTabs({ controller: this.controller }) {
        TabContent() {
          this.ContentBuilder(this.listScroller0)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar 1' })

        TabContent() {
          this.ContentBuilder(this.listScroller1)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar2' })
      }
      .barOverlap(true)
      .barPosition(BarPosition.End)
      .vertical(false)
      .divider({
        mode: this.mode,
        style: {
          color: Color.Black,
          strokeWidth: 1,
          startMargin: 0,
          endMargin: 0
        }
      })
      .width('100%')
      .height('90%')
    }
  }

  @Builder
  ContentBuilder(listScroller: Scroller) {
    List({ scroller: listScroller }) {
      ForEach(this.arr, (item: number) => {
        ListItem() {
          Text("item" + item)
            .height(96)
            .width('100%')
            .backgroundColor(item % 2 === 0 ? Color.Pink : Color.Yellow)
            .textAlign(TextAlign.Center)
        }
      }, (item: string) => item)
    }
    .width('100%')
    .height('100%')
  }
}

**Table 1** Display effect
| 
Always Visible

 | 

Always Hidden

 | 

Visible/Hidden with Scrolling Motion

 |
| :-- | :-- | :-- |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WHt1Br_JSDa9BeFpsrrI9A/en-us_image_0000002500304208.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F0EC5641EA1B1DA8B763C294099F2B686520F81DE0B4C31A0BDA3905C32CE2A "Click to enlarge")

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/mirnwixxRgC83nF-YGDg0w/en-us_image_0000002532144129.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E84C3295BDBD6F3B1E8AA2B328FD83B23BAF22ABB80041C43316B530EB957D1 "Click to enlarge")

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/6zhgijxRRiy1_MunDH5GsQ/en-us_image_0000002532144127.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5AAA2D6E0A609E1F8A148D4D7F1C716997B9C083FE7393F3BC7FEEDCBDC186B "Click to enlarge")

 |

#### \[h2\]Supporting Gradient Blur

Set **barBackgroundStyle** for the **HdsTabs** component to customize the color and height of the blur to implement gradient blur.

**Device behavior**: This API has no effect on TVs and works on other devices.

// Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  private controller: HdsTabsController = new HdsTabsController();

  build() {
    Column() {
      HdsTabs({ controller: this.controller }) {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.White)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar 1' })

        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.White)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar2' })
      }
      .barOverlap(true)
      .barPosition(BarPosition.End)
      .vertical(false)
      .barBackgroundStyle({
        maskColor: Color.Orange,
        maskHeight: 80
      })
    }
  }
}

Display effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/C-gyv5dmQVqb47O895lp_A/en-us_image_0000002532304103.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F02D2911AA2C1D3D18E73C123E6055EAAB6241DC14A54B844E1886905B82198 "Click to enlarge")

#### \[h2\]Supporting the Bleed Style

You can set the tab bar style for the **TabContent** child component of the **HdsTabs** component to implement the bleed style.

**Device behavior**: This API has no effect on TVs and works on other devices.

// Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
import { HdsTabs, HdsTabsAttribute, bleedIconStyle } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
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

Display effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/dl3mRMJDQaCqoYFzFt7ObA/en-us_image_0000002500424070.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D8DF212E3BA14A9B584B42834B4AC6279B38E905D8E7CC180788AA2C4DE4B17)

#### \[h2\]Supporting Half-Screen-based Center Alignment

You can set **barMode** to **ExtendBarMode.HALF\_SCREEN\_FIXED** for the **HdsTabs** component, and configure that the total height of all tabs is one fourth of the height of the **HdsTabs** component and the tabs are in the middle of a half screen.

**Device behavior**: This API has no effect on TVs and works on other devices.

// Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
import { HdsTabs, HdsTabsAttribute, ExtendBarMode } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  @State isVertical: boolean = true;

  build() {
    Column(){
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
      .height('100%')
    }
  }
}

Display effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/mGh9WaT8QWeQByy7Y_NSqQ/en-us_image_0000002500304222.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=927001947C57EAF7E5BFAFBBE4C9EF692C39BAFE9F726025ACAA71728126053D "Click to enlarge")
