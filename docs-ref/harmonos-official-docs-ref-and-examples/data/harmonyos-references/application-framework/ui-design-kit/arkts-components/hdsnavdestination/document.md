# HdsNavDestination

The **HdsNavDestination** component functions as the subpage root container for displaying the content area of the [HdsNavigation](../hdsnavigation/document.md) component. By default, it supports dynamic blur styles of the title bar that scrolls with the content area. After version 6.0.0(20), you are advised to use [bindToScrollable](#section14512122441412) or [bindToNestedScrollable](#section1375318442179) to bind the navigation component to a scrollable container component. This allows you to utilize the navigation component's scrolling functions to implement features like dynamic blur effects triggered by scrolling and the title bar dynamically appearing or disappearing as content scrolls, ultimately providing a superior UI experience.

**Start version**: 5.1.0(18)

#### Modules to Import

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/4dkvhbz_RSuBDMXGohuINw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C63B4A75CA75C013D6B3B51F08A4A31D1E0847A755A9EB25FB790D260672734)

-   **HdsNavDestinationAttribute** is essential for configuring the **HdsNavigation** component. In version 6.0.1(21) and earlier, you must manually import **HdsNavDestinationAttribute** after importing the **HdsNavDestination** component. Otherwise, a compilation error is reported. However, starting from version 6.0.2(22), the compilation toolchain automatically imports **HdsNavDestinationAttribute** when it detects the **HdsNavigation** component, so manual import is no longer necessary.
-   If you manually import **HdsNavDestinationAttribute**, DevEco Studio shows it as disabled (grayed out). In version 6.0.1(21) and earlier, removing this import causes a compilation error. But from version 6.0.2(22) onward, removing it does not affect the functionality.

Version 6.0.1(21) and earlier:

import { HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';

Version 6.0.2(22) and later:

import { HdsNavDestination } from '@kit.UIDesignKit';

#### Child Components

-   Child component types: built-in components and custom components, with support for [if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), and [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach) rendering control.
-   Number of child components: multiple.

#### API

HdsNavDestination()

Creates the root container for child pages of the [HdsNavigation](../hdsnavigation/document.md) component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

#### Attributes

[Universal attributes](../../../arkui/arkts-components/universal-attributes/document.md) are supported.

Avoid setting layout-related attributes such as the position and size. They may result in display issues on the page.

#### \[h2\]titleBar

titleBar(options?: HdsNavigationTitleBarOptions)

Sets the style and content of the **titleBar** area (including the return icon area, title area, menu area, and background) of the **HdsNavDestination** component.

When the title string is too long: (1) If no subtitle is set, the string is scaled down and wrapped in two lines. Any content exceeding this will be truncated with an ellipsis (...); (2) If a subtitle is set, the subtitle is scaled down and then truncated with an ellipsis (...) if it is still overlong.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

[HdsNavigationTitleBarOptions](../hdsnavigation/document.md#section1867665412513)

 | 

No

 | 

Title bar settings.

 |

#### \[h2\]hideTitleBar

hideTitleBar(hide: boolean, animated?: boolean)

Sets whether to hide the title bar and whether to animate the visibility change.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

hide

 | 

boolean

 | 

Yes

 | 

Indicates whether to hide the title bar.

The default value is **false**.

**true**: yes

**false**: no

 |
| 

animated

 | 

boolean

 | 

No

 | 

Indicates whether to animate the visibility change.

The default value is **false**.

**true**: yes

**false**: no

 |

#### \[h2\]hideBackButton

hideBackButton(value: boolean)

Sets whether to hide the back button on the title bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

Indicates whether to hide the back button on the title bar.

The default value is **false**.

**true**: yes

**false**: no

 |

#### \[h2\]mode

mode(value: NavDestinationMode)

Sets the type of the **HdsNavDestination** component. Its value cannot be changed dynamically.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

[NavDestinationMode](../../../arkui/arkts-components/navigation-and-switching/navdestination/document.md#navdestinationmode11)

 | 

Yes

 | 

**HdsNavDestination** component type.

The default value is **NavDestinationMode.STANDARD**.

 |

#### \[h2\]toolbarConfiguration

toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

Sets the content of the toolbar. If this API is not called, the toolbar remains hidden.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

toolbarParam

 | 

Array<[ToolbarItem](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#toolbaritem10)\> | [CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

Yes

 | 

Content of the toolbar.

When configured with Array<[ToolbarItem](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#toolbaritem10)\>, the toolbar follows the rules below:

-   Toolbar items, with their icons and text, are evenly distributed on the bottom toolbar.

-   If any item contains overlong text and there are fewer than five items, the toolbar will: (1) Increase the item width to accommodate the text until the toolbar spans the screen width; (2) Reduce the text size progressively; (3) Wrap the text into two lines and truncate the exceeding text.

-   In portrait mode, the toolbar shows a maximum of five icons, with any additional icons placed under an automatically generated **More** icon. In landscape mode: (1) If the display mode is [Split](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9), the toolbar follows the same rules as in portrait mode. (2) If the display mode is [Stack](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9), the toolbar cannot be merged into the menu bar.

When configured with [CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8), the toolbar only supports evenly distributing items at its bottom.

 |
| 

options

 | 

[NavigationToolbarOptions](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationtoolbaroptions11)

 | 

No

 | 

Toolbar items.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/B9wQMi9BRVGTKicijDsUsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D5C81B3B2A166752FB6FB748DC3C3BE13D90F646BE9FEF193262EE14C37709C)

The following are not allowed: modify the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, change the animation effects through the **effectStrategy** attribute, or change the type of animation effects through the **symbolEffect** attribute.

#### \[h2\]hideToolBar

hideToolBar(hide: boolean, animated?: boolean)

Sets whether to hide the toolbar and whether to animate the visibility change.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

hide

 | 

boolean

 | 

Yes

 | 

Indicates whether to hide the toolbar.

The default value is **false**.

**true**: yes

**false**: no

 |
| 

animated

 | 

boolean

 | 

No

 | 

Indicates whether to animate the visibility change.

The default value is **false**.

**true**: yes

**false**: no

 |

#### \[h2\]ignoreLayoutSafeArea

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

Ignores the layout safe area by allowing the component to extend into the non-safe areas of the screen.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

types

 | 

Array <[LayoutSafeAreaType](../../../arkui/arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#layoutsafeareatype12)\>

 | 

No

 | 

Types of non-safe areas to extend into.

The default value is **\[LayoutSafeAreaType.SYSTEM\]**.

 |
| 

edges

 | 

Array <[LayoutSafeAreaEdge](../../../arkui/arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#layoutsafeareaedge12)\>

 | 

No

 | 

Edges for expanding the safe area.

Default value: \[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM\]

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Zoj7p4yaQ_mp7uKCRP9Tqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F6EB22134BAC3D8501CD6C1CBC89C0F7692F16D92ACEC6D8CD1AAC5460F6614)

After **LayoutSafeArea** is set:

When **LayoutSafeAreaType.SYSTEM** is used, the component can extend into the non-safe areas if its boundaries overlap with them. For example, if the device's top status bar is 100 high, the component can extend into the non-safe areas only when there is an absolute vertical offset between 0 and 100.

If the component extends into the non-safe areas, events triggered within those areas (such as tap events) might be blocked by the system. This allows the system to prioritize responses to system components such as the status bar.

#### \[h2\]systemBarStyle

systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>)

Sets the style of the system status bar when the home page of the **HdsNavDestination** component is displayed.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

originalStyle

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<[SystemBarStyle](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#systembarstyle12)\>

 | 

Yes

 | 

Initial style of the system status bar. If the **systemBarStyle** attribute is not set, the font color of the main title bar is used.

 |
| 

scrollEffectStyle

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<[SystemBarStyle](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#systembarstyle12)\>

 | 

Yes

 | 

Dynamic style of the system status bar after the dynamic style of the **HdsNavDestination** component takes effect. If the **systemBarStyle** attribute is not set, the font color of the main title bar is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/oJSyUwFpQ1e1dXq7huClcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0EDBE44C4E847FA762CD0F98AB71412FC28F8AB3870DE538704AF050F796B2A)

1.  The setting takes effect only when the **HdsNavigation** component is used as the root node of the **HdsNavDestination** component.
2.  For other restrictions, please refer to [systemBarStyle](../hdsnavigation/document.md#section122478710329) of the **HdsNavigation** component.

#### \[h2\]recoverable

recoverable(recoverable: Optional<boolean>)

Sets whether the **HdsNavDestination** component is recoverable. If set to recoverable, when the app process exits unexpectedly and restarts, the **HdsNavDestination** component will be automatically recreated. To use this feature, ensure that the **recoverable** attribute is set for the **HdsNavigation** component associated with the **HdsNavDestination** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

recoverable

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<boolean>

 | 

Yes

 | 

Indicates whether the **HdsNavDestination** component is recoverable. By default, it is not recoverable.

The default value is **false**.

**true**: yes

**false**: no

 |

#### \[h2\]dynamicHideTitleBar

dynamicHideTitleBar(value: DynamicHideParams)

Sets whether to dynamically trigger the display or hiding animation of the title bar as the content area scrolls. You are advised to call this API together with [bindToScrollable](../hdsnavigation/document.md#section14512122441412)/[bindToNestedScrollable](../hdsnavigation/document.md#section1375318442179) to achieve a better scrolling effect.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

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

[DynamicHideParams](../hdsnavigation/document.md#section453532817500)

 | 

Yes

 | 

Indicates whether to dynamically trigger the display or hiding animation of the title bar as the content area scrolls.

If yes, the title bar mode cannot be dynamically switched.

If the title bar mode is **HdsNavDestinationTitleMode.MODAL**, settings made through this API do not take effect.

Attributes cannot be dynamically changed during the display and hiding process.

 |

#### \[h2\]bindToScrollable

bindToScrollable(scrollers: Array<Scroller>)

Binds the navigation component and scrollable container component to achieve the function of displaying/hiding the title area, status bar, and bottom custom area, delivering a better dynamic display and hiding experience.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

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

scrollers

 | 

Array<[Scroller](../../../arkui/arkts-components/scroll-and-swipe/scroll/document.md#scroller)\>

 | 

Yes

 | 

Controller of the target scrollable container.

 |

#### \[h2\]bindToNestedScrollable

bindToNestedScrollable(scrollers: Array<NestedScrollInfo>)

Binds the navigation component and nested scrollable container component to achieve the function of displaying/hiding the title area, status bar, and bottom custom area, delivering a better dynamic display and hiding experience.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

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

scrollers

 | 

Array<[NestedScrollInfo](../hdsnavigation/document.md#section28581254125712)\>

 | 

Yes

 | 

Controller of the target nested scrollable container.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/ndmZy41mRnu_5O3iVmGsQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2803D19FC5D1926F48AD5F964E41275CBF761D57D515613E1113EDC1994FD725)

If a navigation component is bound to multiple scrollable containers, scrolling in any of these containers triggers the display or hiding animation of the title bar. Specifically, when any scrollable container reaches either the bottom or the top, the display animation for the title bar is triggered without delay. As such, to ensure the optimal user experience, avoid triggering scroll events of multiple scrollable containers simultaneously.

#### \[h2\]systemTransition

systemTransition(type: NavigationSystemTransitionType)

Sets the system transition animation of the **HdsNavDestination** component. System transition animations for the title bar and content area can be configured separately.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

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

type

 | 

[NavigationSystemTransitionType](../../../arkui/arkts-components/navigation-and-switching/navdestination/document.md#navigationsystemtransitiontype14)

 | 

Yes

 | 

Type of the system transition animation.

The default value is **NavigationSystemTransitionType.DEFAULT**.

 |

#### \[h2\]customTransition

customTransition(delegate: NavDestinationTransitionDelegate)

Sets a custom transition animation for the **HdsNavDestination** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

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

delegate

 | 

[NavDestinationTransitionDelegate](../../../arkui/arkts-components/navigation-and-switching/navdestination/document.md#navdestinationtransitiondelegate15)

 | 

Yes

 | 

Delegation function for custom animations of the **HdsNavDestination** component.

 |

#### \[h2\]titleMode

titleMode(value: HdsNavDestinationTitleMode)

Sets the display mode of the page title bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

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

[HdsNavDestinationTitleMode](#section195465713522)

 | 

Yes

 | 

Display mode of the page title bar. The default value is **HdsNavDestinationTitleMode.MINI**.

 |

#### Events

#### \[h2\]onShown

onShown(callback: Callback<void>)

Triggered when an **HdsNavDestination** page is displayed.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

Yes

 | 

Triggered when an **HdsNavDestination** page is displayed.

 |

#### \[h2\]onHidden

onHidden(callback: Callback<void>)

Triggered when an **HdsNavDestination** page is hidden.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

Yes

 | 

Triggered when an **HdsNavDestination** page is hidden.

 |

#### \[h2\]onReady

onReady(callback: Callback<NavDestinationContext>)

Triggered when the **HdsNavDestination** component is about to build a child component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<[NavDestinationContext](../../../arkui/arkts-components/navigation-and-switching/navdestination/document.md#navdestinationcontext11)\>

 | 

Yes

 | 

Triggered when the **HdsNavDestination** component is about to build a child component.

 |

#### \[h2\]onWillAppear

onWillAppear(callback: Callback<void>)

Triggered when the **HdsNavDestination** component is about to be mounted. The page stack can be modified in the callback and the modification takes effect in the current frame.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

Yes

 | 

Triggered when the **HdsNavDestination** component is about to be mounted.

 |

#### \[h2\]onWillDisappear

onWillDisappear(callback: Callback<void>)

Triggered when the **HdsNavDestination** component is about to be unmounted (or when the transition animation, if any, is about to start).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

Yes

 | 

Triggered when the **HdsNavDestination** component is about to be unmounted (or when the transition animation, if any, is about to start).

 |

#### \[h2\]onWillShow

onWillShow(callback: Callback<void>)

Triggered when the **HdsNavDestination** component is about to be displayed.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

Yes

 | 

Triggered when the **HdsNavDestination** component is about to be displayed.

 |

#### \[h2\]onWillHide

onWillHide(callback: Callback<void>)

Triggered when the **HdsNavDestination** component is about to be hidden.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

Yes

 | 

Triggered when the **HdsNavDestination** component is about to be hidden.

 |

#### \[h2\]onBackPressed

onBackPressed(callback: Callback<void, boolean>)

Triggered when the back button is tapped. This callback takes effect only when page stack bound to the **HdsNavigation** component contains content.

The value **true** means that the back button logic is overridden, and **false** means that the previous page is displayed. You are advised not to set the back button custom event and the **onBackPressed** callback simultaneously.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void, boolean>

 | 

Yes

 | 

Triggered when the back button is tapped and the page stack bound to the **HdsNavigation** component contains content.

 |

#### \[h2\]onActive

onActive(callback: Optional<Callback<NavDestinationActiveReason>>)

Triggered when the **HdsNavDestination** component becomes active (on top of the stack and operable, with no special components blocking it).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.1(21)

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

callback

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<[NavDestinationActiveReason](../../../arkui/arkts-components/navigation-and-switching/navdestination/document.md#navdestinationactivereason17)\>>

 | 

Yes

 | 

Reason why the **HdsNavDestination** component switches from inactive to active.

 |

#### \[h2\]onlnactive

onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)

Triggered when the **HdsNavDestination** component becomes inactive (not on top of the stack and inoperable, or on top but blocked by special components).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.1(21)

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

callback

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<[NavDestinationActiveReason](../../../arkui/arkts-components/navigation-and-switching/navdestination/document.md#navdestinationactivereason17)\>>

 | 

Yes

 | 

Reason why the **HdsNavDestination** component switches from active to inactive.

 |

#### HdsNavDestinationTitleMode

Defines the enumeration of the display mode for the title bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

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

MINI

 | 

100

 | 

The title is fixed at mini mode. The title bar height is 56 vp.

 |
| 

MODAL

 | 

101

 | 

The title is fixed at sheet mode. The background height is 64 vp, the title bar height is 56 vp, and the top padding height is 8 vp.

 |

#### Example

In the following code, the **titleBar** attribute is used to customize the dynamic blur style of the title bar when it scrolls with the content area.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavDestinationAttribute. For details, refer to the "Modules to Import" section of the HdsNavDestination reference document.
import { HdsNavDestination, HdsNavDestinationAttribute, ScrollEffectType } from '@kit.UIDesignKit';
import { LengthMetrics } from '@kit.ArkUI';

const  TITLE\_BAR\_HEIGHT\_MINI: number = 56;

@Entry
@Component
struct PageOne {
  scroller: Scroller = new Scroller()

  build() {
    HdsNavDestination() {
      Scroll(this.scroller) {
        Column() {
          Blank().height(TITLE\_BAR\_HEIGHT\_MINI)
          Image($r('app.media.scenery')).width('100%') // **scenery** is a custom resource. You need to replace it with your local resource.
        }
      }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
    }
    .titleBar({
      padding: {
        start: LengthMetrics.vp(2),
        end: LengthMetrics.vp(2)
      },
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON\_BLUR,
          blurEffectiveStartOffset: LengthMetrics.vp(0),
          blurEffectiveEndOffset: LengthMetrics.vp(20)
        },
        originalStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos\_id\_color\_background'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font\_primary'), subTitleColor: $r('sys.color.font\_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp\_background\_tertiary'), iconColor: $r('sys.color.icon\_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp\_background\_tertiary'), iconColor: $r('sys.color.icon\_primary') }
          }
        },
        scrollEffectStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos\_id\_color\_background\_transparent'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font\_primary'), subTitleColor: $r('sys.color.font\_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp\_background\_tertiary'), iconColor: $r('sys.color.icon\_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp\_background\_tertiary'), iconColor: $r('sys.color.icon\_primary') }
          }
        }
      },
      content: {
        title: {
          mainTitle: "PageOne",
        },
        menu: {
          value: \[{
            content: {
              label: 'menu1',
              icon: 'resources/base/media/startIcon.png',
              isEnabled: true,
              action: () => {
                console.info("HdsNavDestination menu1");
              }
            }
          }, {
            content: {
              label: 'menu2',
              icon: 'resources/base/media/startIcon.png',
              isEnabled: true,
              action: () => {
                console.info("HdsNavDestination menu2");
              }
            }
          }\]
        },
      }
    })
    .systemBarStyle({ statusBarContentColor: '#0A59F7' }, { statusBarContentColor: '#C7C7CD' })
    .hideBackButton(false)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/tPiwx_W8SnyRNYwiWdTODg/en-us_image_0000002500304212.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AA26AA628079C4B08646D1576A08A5806231725E23BCAB6B6476A0167D17F0B "Click to enlarge")

For more samples regarding the **HdsNavDestination** component, please refer to the [sample code](../hdsnavigation/document.md#section86814120266).
