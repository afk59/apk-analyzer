# HdsNavigation

This module provides the navigation component capability, supporting dynamic blur styles of the title bar that activate with content scrolling. After API version 6.0.0(20), you are advised to use [bindToScrollable](#section14512122441412) or [bindToNestedScrollable](#section1375318442179) to bind the navigation component to a scrollable container component. This allows you to utilize the navigation component's scrolling functions to implement features like dynamic blur effects triggered by scrolling and the title bar dynamically appearing or disappearing as content scrolls, ultimately providing a superior UI experience.

The **HdsNavigation** component is the root view container for navigation. It typically functions as the root container of pages and includes a title bar, content area, and toolbar. By default, the content area switches between the home page content (child components of **HdsNavigation**) and non-home page content (child components of [HdsNavDestination](../hdsnavdestination/document.md)) through routing.

**Start version**: 5.1.0(18)

#### Modules to Import

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/C-A27GEGRX-xlWyJ5LiFwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=376CD4D941D5613CD022CB6F5AAC78CC08F8C2E72A0A86B4375E4A69E5972234)

-   **HdsNavigationAttribute** is essential for configuring the **HdsNavigation** component. In version 6.0.1(21) and earlier, you must manually import **HdsNavigationAttribute** after importing the **HdsNavigation** component. Otherwise, a compilation error is reported. However, starting from version 6.0.2(22), the compilation toolchain automatically imports **HdsNavigationAttribute** when it detects the **HdsNavigation** component, so manual import is no longer necessary.
-   If you manually import **HdsNavigationAttribute**, DevEco Studio shows it as disabled (grayed out). In version 6.0.1(21) and earlier, removing this import causes a compilation error. But from version 6.0.2(22) onward, removing it does not affect the functionality.

Version 6.0.1(21) and earlier:

import { HdsNavigation, HdsNavigationAttribute } from '@kit.UIDesignKit';

Version 6.0.2(22) and later:

import { HdsNavigation } from '@kit.UIDesignKit';

#### Child Components

Child components are supported. Use [NavPathStack](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navpathstack10) together with various attribute settings of the [HdsNavDestination](../hdsnavdestination/document.md) component for navigation jumps.

#### API

HdsNavigation(pathInfos?: NavPathStack)

Binds a navigation stack to the **HdsNavigation** component.

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

pathInfos

 | 

[NavPathStack](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navpathstack10)

 | 

No

 | 

Navigation stack information.

 |

#### Attributes

In addition to [universal attributes](../../../arkui/arkts-components/universal-attributes/document.md), the following attributes are supported.

#### \[h2\]titleBar

titleBar(options?: HdsNavigationTitleBarOptions)

Sets the styles and content of the **titleBar** area (including the return icon area, title area, menu area, and background) of the **HdsNavigation** component.

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

[HdsNavigationTitleBarOptions](#section1867665412513)

 | 

No

 | 

Title bar settings.

 |

#### \[h2\]titleMode

titleMode(value: HdsNavigationTitleMode)

Sets the display mode of the page title bar.

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

[HdsNavigationTitleMode](#section26841314155317)

 | 

Yes

 | 

Display mode of the page title bar.

The default value is **HdsNavigationTitleMode.FREE**.

 |

#### \[h2\]toolbarConfiguration

toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/02-u2plGRe-eeYc4HfeoTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF800B6B5C8B9119231DF6DD7D2AF4D0E809845B1C5E089F690F2FCF3000E769)

The following are not allowed: modify the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, change the animation effects through the **effectStrategy** attribute, or change the type of animation effects through the **symbolEffect** attribute.

Sets the content of the toolbar. If this parameter is not set, no toolbar is displayed.

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

Array<[ToolbarItem](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#toolbaritem10)\> | [CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

Yes

 | 

Content of the toolbar. When configured with Array<[ToolbarItem](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#toolbaritem10)\>, the toolbar follows the rules below:

-   Toolbar items, with their icons and text, are evenly distributed on the bottom toolbar.

-   If any item contains overlong text and there are fewer than five items, the toolbar will: (1) Increase the item width to accommodate the text until the toolbar spans the screen width; (2) Reduce the text size progressively; (3) Wrap the text into two lines and truncate the exceeding text.

-   In portrait mode, the toolbar shows a maximum of five icons, with any additional icons placed under an automatically generated **More** icon. In landscape mode: (1) If the display mode is [Split](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9), the toolbar follows the same rules as in portrait mode. (2) If the display mode is [Stack](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9), the toolbar cannot be merged into the menu bar.

When configured with [CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8), the toolbar does not follow the above rules, except for evenly distributing items at the bottom toolbar.

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

Sets whether to hide the back button on the title bar. The back button is available only when [titleMode](#section0266105514213) is set to **HdsNavigationTitleMode.MINI**.

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

#### \[h2\]navBarWidth

navBarWidth(value: Length)

Sets the width of the navigation bar. This parameter takes effect only when the **HdsNavigation** component is split.

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

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

Yes

 | 

Width of the navigation bar.

The default value is **240**.

The unit is vp.

**undefined**: No action is taken, and the navigation bar width remains consistent with the default value.

 |

#### \[h2\]navBarPosition

navBarPosition(value: NavBarPosition)

Sets the position of the navigation bar. This parameter takes effect only when the **HdsNavigation** component is split.

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

[NavBarPosition](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navbarposition9)

 | 

Yes

 | 

Position of the navigation bar.

The default value is **NavBarPosition.Start**.

 |

#### \[h2\]mode

mode(value: NavigationMode)

Sets the display mode of the navigation bar. Available options are **Stack**, **Split**, and **Auto**.

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

[NavigationMode](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9)

 | 

Yes

 | 

Display mode of the navigation bar.

The default value is **NavigationMode.Auto**.

At the default settings, the component adapts to a single column or two columns based on the component width.

 |

#### \[h2\]hideNavBar

hideNavBar(value: boolean)

Sets whether to hide the navigation bar.

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

Indicates whether to hide the navigation bar. If this parameter is set to **false**, the navigation bar is not hidden. If this parameter is set to **true**, the navigation bar, including the title bar, content area, and toolbar, is hidden. In this case, if an **HdsNavDestination** page is in the navigation stack, it is moved to the top of the stack and displayed. Otherwise, a blank page is displayed.

The default value is **false**.

 |

#### \[h2\]navDestination

navDestination(builder: NavDestinationBuilder)

Creates an **HdsNavDestination** component. The **builder** function is used, with the **name** and **pageInfos** parameters passed in. The builder can contain only one root node. In the builder, a parent custom component can be added for the **HdsNavDestination** component. However, no parameters or events can be set for the custom component. Otherwise, only a blank component is displayed.

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

builder

 | 

[NavDestinationBuilder](#section147171747131910)

 | 

Yes

 | 

Builder used to create an **HdsNavDestination** component.

 |

#### \[h2\]navBarWidthRange

navBarWidthRange(value: NavBarWidthRangeOptions)

Sets the minimum and maximum widths of the navigation bar (effective in dual-column mode).

For details about the priority rules, see the parameter description of [minContentWidth](#section03511461273).

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

[NavBarWidthRangeOptions](#section6345424102713)

 | 

Yes

 | 

Minimum and maximum widths of the navigation bar.

 |

#### \[h2\]minContentWidth

minContentWidth(value: Dimension)

Sets the minimum width of the navigation bar content area (effective in dual-column mode).

For details about the priority rules, see **NOTE** below.

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

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

Yes

 | 

Minimum width of the navigation bar content area.

The default value is **360**.

The unit is vp.

**undefined**: No action is taken, and the minimum width of the navigation bar content area remains consistent with the default value.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/yhR1pNToRVaJb0SQFEOsHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E46E98D3293D8536C28753C40DFA5471822C0AEA4588BA136A20773903497750)

1.  If only **navBarWidth** is set, no divider in the **HdsNavigation** component can be dragged.
2.  **navBarWidthRange** specifies the range within which the divider can be dragged. If it is not set, the default value is used. The dragging of the divider is subject to both **navBarWidthRange** and **minContentWidth**.
3.  If the size of the **HdsNavigation** component decreases, it carries out the following steps in sequence: a. Scale down the content area. If **minContentWidth** is not set, the content area can be scaled down to **0**. Otherwise, the content area can be scaled down to as small as the value specified by **minContentWidth**. b. Scale down the navigation bar until its width reaches the value defined by **navBarRange**. c. Clip the displayed content.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/WlLg46KhSr2hFQQ4g8X9Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BA3375326FDBA0C09D60FE1EB5E0210C4E1063597F583A501D912EECFD6ECA2)

After **LayoutSafeArea** is set:

When **LayoutSafeAreaType.SYSTEM** is used, the component can extend into the non-safe areas if its boundaries overlap with them. For example, if the device's top status bar is 100 high, the component can extend into the non-safe areas only when there is an absolute vertical offset between 0 and 100.

If the component extends into the non-safe areas, events triggered within those areas (such as tap events) might be blocked by the system. This allows the system to prioritize responses to system components such as the status bar.

#### \[h2\]systemBarStyle

systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>)

Sets the style of the system status bar when the home page of the **HdsNavigation** component is displayed.

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

Dynamic style of the system status bar after the final dynamic style of the **HdsNavigation** component takes effect. If the **systemBarStyle** attribute is not set, the font color of the main title bar is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/V_dYmu8WQVOQRKdwNO6rnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CED9FC7D6C8787037D13ED5AFC6D9FA480ABC644BC68A765EFF22D8D0B76126)

1.  Avoid using the **systemBarStyle** attribute in conjunction with the status bar style APIs in the **Window** module, such as [setWindowSystemBarProperties](../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#setwindowsystembarproperties9).
2.  For the **HdsNavigation** component that uses the [Split](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9) mode, if there is no **HdsNavDestination** in the content area, the settings of the **HdsNavigation** home page will apply. Otherwise, the settings of the top **HdsNavDestination** page on the navigation stack will apply.
3.  The **systemBarStyle** attribute is effective only for the main page of the main window.
4.  When different styles are set for pages, the new style takes effect at the start of the page transition.
5.  The status bar style set by **HdsNavigation** or **HdsNavDestination** does not apply in non-full-screen windows.

#### \[h2\]recoverable

recoverable(recoverable: Optional<boolean>)

Sets whether the **HdsNavigation** component is recoverable. If set to recoverable, when the app process exits unexpectedly and restarts, the **HdsNavigation** component will be automatically recreated, and the navigation stack will be restored to the state at the time of the unexpected exit.

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

Indicates whether the **HdsNavigation** component is recoverable. By default, it is not recoverable.

The default value is **false**.

**true**: yes

**false**: no

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/_Voex7etS12DYEtPjO82Xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0626F67EA25FF6139A30D1C9D4606DF8BD85A2121EE8E0383C34A1368E9E2B73)

For this API to work properly, you must first set the [id attribute](../../../arkui/arkts-components/universal-attributes/basic-attributes/component-id/document.md#id) of the **HdsNavigation** component.

This API must be used together with the [recoverable](../hdsnavdestination/document.md#section814571810599) API of **HdsNavDestination**.

Non-serializable information, such as non-serializable parameters and custom **onPop**, is deprecated and cannot be restored during the recovery process.

#### \[h2\]dynamicHideTitleBar

dynamicHideTitleBar(value: DynamicHideParams)

Sets whether to dynamically trigger the display or hiding animation of the title bar as the content area scrolls. You are advised to call this API together with [bindToScrollable](#section14512122441412)/[bindToNestedScrollable](#section1375318442179) to achieve a better scrolling effect.

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

[DynamicHideParams](#section453532817500)

 | 

Yes

 | 

Indicates whether to dynamically trigger the display or hiding animation of the title bar as the content area scrolls.

If the title bar mode is **HdsNavigationTitleMode.MODAL**, settings made through this API do not take effect.

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

Array<[NestedScrollInfo](#section28581254125712)\>

 | 

Yes

 | 

Controller of the target nested scrollable container.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/tlBLTaODTH-kYu5Ym-ha8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4241D5D1536904D3F21F6DCC404C1C63D4D0BECD79E2E5E91DE8B14A1089EF0C)

If a navigation component is bound to multiple scrollable containers, scrolling in any of these containers triggers the display or hiding animation of the title bar. Specifically, when any scrollable container reaches either the bottom or the top, the display animation for the title bar is triggered without delay. As such, to ensure the optimal user experience, avoid triggering scroll events of multiple scrollable containers simultaneously.

#### \[h2\]enableDragBar

enableDragBar(isEnabled: Optional<boolean>)

Sets whether to display a drag bar in split-column scenarios.

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

isEnabled

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<boolean>

 | 

Yes

 | 

Indicates whether to enable the drag bar. By default, there is no drag bar.

The default value is **false**.

**true**: yes

**false**: no

 |

#### \[h2\]enableModeChangeAnimation

enableModeChangeAnimation(isEnabled: Optional<boolean>)

Sets whether to enable the animation for switching between single and double column modes for [NavigationMode](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9).

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

isEnabled

 | 

[Optional](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt12)<boolean>

 | 

Yes

 | 

Indicates whether to enable the animation for switching between single and double column modes.

The default value is **true**.

**true**: yes

**false**: no

 |

#### Events

#### \[h2\]onNavBarStateChange

onNavBarStateChange(callback: Callback<boolean>)

Triggered when the navigation bar visibility status changes.

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

callBack

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<boolean>

 | 

Yes

 | 

Returns whether the navigation bar is displayed. The options are **true** (yes) and **false** (no).

 |

#### \[h2\]onNavigationModeChange

onNavigationModeChange(callback: Callback<NavigationMode>)

Triggered when the **HdsNavigation** component is displayed for the first time or its display mode switches between single-column and dual-column.

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<[NavigationMode](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationmode9%E6%9E%9A%E4%B8%BE%E8%AF%B4%E6%98%8E)\>

 | 

Yes

 | 

-   **NavigationMode.Split**: The **HdsNavigation** component is displayed in two columns.

-   **NavigationMode.Stack**: The **HdsNavigation** component is displayed in a single column.

 |

#### \[h2\]onTitleModeChange

onTitleModeChange(callback: Callback<HdsNavigationTitleMode>)

Triggered when **titleMode** is set to **HdsNavigationTitleMode.FREE** and the title bar mode changes as content scrolls.

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

callback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<[HdsNavigationTitleMode](#section26841314155317)\>

 | 

Yes

 | 

Triggered upon a title mode change, with the title mode as a parameter.

 |

#### \[h2\]customNavContentTransition

customNavContentTransition(delegate: CustomTransitionDelegate)

Callback of the custom transition animation.

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

[CustomTransitionDelegate](#section357932612138)

 | 

Yes

 | 

Callback method of the custom transition animation.

 |

#### ScrollEffectType

Defines the enumeration of the title bar blur style.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

COMMON\_BLUR

 | 

0

 | 

Blur style of the title bar: common type.

Using this style, the background of the title bar can also be uniformly blurred with consistent intensity and sharp boundaries, emphasizing the hierarchical division between controls and content.

As content slides into or out of the title bar area, the blurred background and divider line will gradually fade in or out. This style is applicable to non-immersive scenarios.

 |
| 

GRADUAL\_BLUR

 | 

1

 | 

Blur style of the title bar: transition blur.

Using this style, the background of the title bar can also be uniformly blurred with consistent intensity and sharp boundaries, emphasizing the hierarchical division between controls and content.

As content scrolls, the title bar undergoes color and state changes, which linearly animate synchronously with the scrolling motion. This style is only applicable for scenarios involving transitions between immersive and non-immersive modes.

**Start version**: 6.0.0(20)

 |
| 

GRADIENT\_BLUR

 | 

2

 | 

Blur style of the title bar: gradient blur.

This blur effect gradually intensifies or lessens across the screen, featuring soft, seamless edges to create a more immersive page experience.

-   When **ScrollEffectOptions.enableScrollEffect** is set to **true**, gradient blur takes effect in a gradual mode. In this case, as content scrolls, the title bar undergoes color/state changes, which linearly animate synchronously with the scrolling motion.
-   When **ScrollEffectOptions.enableScrollEffect** is set to **false**, gradient blur takes effect directly.

**Start version**: 6.0.0(20)

 |

#### HdsNavigationTitleMode

Defines the enumeration of the display mode for the title bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

FREE

 | 

0

 | 

The title shrinks as the content scrolls down (the subtitle fades out with its size remaining unchanged) and restores as the content scrolls up to the top.

In the non-scrolling state, the height of the title bar is the same as in **FULL** mode; in the scrolling state, the minimum height of the title bar is the same as in **MINI** mode.

You are advised to also call [bindToScrollable](#section14512122441412)/[bindToNestedScrollable](#section1375318442179) in this mode to achieve a better linkage experience.

 |
| 

FULL

 | 

1

 | 

The title is fixed at full mode.

If there is only a main title, the title bar height is 112 vp; if there is both a main title and a subtitle, the title bar height is 138 vp.

 |
| 

MINI

 | 

2

 | 

The title is fixed at mini mode. The title bar height is 56 vp.

 |
| 

MODAL

 | 

3

 | 

The title is fixed at sheet mode.

-   When a first-level page only has a main title, the background height of the title area is 64 vp, with the title bar height being 56 vp and top padding being 8 vp.
-   When a first-level page has both a main title and subtitle, the background height of the title area is 80 vp, with the title bar height being 72 vp and top padding being 8 vp.

**Start version**: 6.0.0(20)

 |

#### DividerShowType

Defines the enumeration of the divider display type.

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

OFF

 | 

0

 | 

The divider is always hidden.

 |
| 

ON

 | 

1

 | 

The divider is always visible.

 |
| 

AUTO

 | 

2

 | 

The divider is visible or hidden with the scrolling motion of the content area.

 |

#### TextStyleMode

Defines the enumeration of the text icon mode.

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

NORMAL

 | 

200

 | 

Common text mode.

This mode indicates a capsule button, with a corner radius specified by **sys.float.corner\_radius\_level10**.

 |
| 

SINGLE\_CHARACTER

 | 

201

 | 

Single-character mode.

This mode indicates a round button.

 |

#### BottomBuilderShowType

Defines the enumeration of the display type for the **bottomBuilder**.

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

DIRECTLY\_SHOW

 | 

0

 | 

The bottomBuilder is directly displayed.

 |
| 

OVERDRAG\_SHOW

 | 

1

 | 

The **bottomBuilder** is displayed upon over-scrolling.

 |

#### HideMode

Defines the enumeration of the dynamic display/hiding mode for the title bar.

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

SCROLL\_UP\_TO

 | 

0

 | 

The title bar is hidden on downward scroll to a fixed position and displayed on upward scroll to a fixed position.

 |
| 

SCROLL\_UP

 | 

1

 | 

The title bar is hidden on any downward scroll and displayed on any upward scroll.

 |
| 

SCROLL\_DOWN

 | 

2

 | 

The title bar is displayed on any downward scroll and hidden on any upward scroll. This setting takes effect only when the title bar mode is **HdsNavigationTitleMode.MINI** or **HdsNavDestinationTitleMode.MINI**.

 |
| 

SCROLL\_UP\_TO\_BLEND\_SCROLL\_UP

 | 

3

 | 

The title bar is displayed in hybrid mode. The **bottomBuilder** uses the **SCROLL\_UP\_TO** mode, and the title bar uses the **SCROLL\_UP** mode.

 |

#### IconStyleMode

Defines the enumeration of the image icon mode.

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

SMALL

 | 

100

 | 

Small image icon mode. The default icon size is 18 x 18 vp.

 |
| 

NORMAL

 | 

101

 | 

Common-size image icon mode. The default icon size is 24 x 24 vp.

 |
| 

LARGE

 | 

102

 | 

Large image icon mode. The default icon size is 40 x 40 vp.

 |

#### BlurStrategy

Defines the enumeration of the blur effect.

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

ENABLE

 | 

0

 | 

The blur effect is enabled.

 |
| 

DISABLE

 | 

1

 | 

The blur effect is disabled.

 |
| 

ADAPTIVE

 | 

2

 | 

The blur effect policy is adjusted based on the system policy. Three distinct system style policy ranks are supported: exquisite, gentle, and smooth. Blur effects can take effect only for the exquisite rank.

The system style policy is configured by each device manufacturer based on device performance, with the exquisite rank executed by default if not configured.

 |

#### NavDestinationBuilder

type NavDestinationBuilder = (name: string, pageInfos: Object) => void

Constructs the **HdsNavDestination** component based on **name** and **pageInfos**.

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

name

 | 

string

 | 

Yes

 | 

Name of the created **HdsNavDestination** page.

 |
| 

pageInfos

 | 

Object

 | 

Yes

 | 

Parameters of the **HdsNavDestination** page.

 |

#### CustomTransitionDelegate

type CustomTransitionDelegate = (from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined

Callback method of the custom transition animation.

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

from

 | 

[NavContentInfo](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navcontentinfo11)

 | 

Yes

 | 

Page to exit.

 |
| 

to

 | 

[NavContentInfo](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navcontentinfo11)

 | 

Yes

 | 

Page to access.

 |
| 

operation

 | 

[NavigationOperation](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationoperation11)

 | 

Yes

 | 

Navigation type.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[NavigationAnimatedTransition](../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navigationanimatedtransition11) | undefined

 | 

Custom transition animation agreement.

**undefined**: The default transition effect is executed.

 |

#### IconType

type IconType = ResourceStr | SymbolGlyphModifier | PixelMap

Defines the image resource type supported by a single icon-type menu item on the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

Character string type.

 |
| 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

Symbol resource type.

 |
| 

[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Image pixel type.

**Start version**: 6.0.0(20)

 |

#### HdsNavigationMenuItemOptions

type HdsNavigationMenuItemOptions = HdsNavigationBadgeIconOptions

Defines the menu items of the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsNavigationBadgeIconOptions](#section7349101217489)

 | 

Icon settings, including the reminder badge.

 |

#### HdsNavigationBackButtonItemOptions

type HdsNavigationBackButtonItemOptions = HdsNavigationIconOptions

Defines the back button settings of the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsNavigationIconOptions](#section74312125454)

 | 

Icon settings.

 |

#### HdsNavigationBackgroundStyle

Defines the title bar background style of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

backgroundColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of the title bar.

Default value:

-   When the **COMMON\_BLUR** blur type is used, the default background color is transparent.
-   When the **GRADUAL\_BLUR** blur type is used, the default background color is transparent.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **false**, the default gradient color takes effect for the blur overlay.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **true**, the blur overlay is transparent before the dynamic style takes effect and changes to the default gradient color after the dynamic style takes effect.

Among the default parameters for the blur overlay gradient, the array defining the colors and their corresponding percentage stops is **\[\["#99000000",0\],\["#8F000000",0.15\],\["#66000000",0.5\],\["#40000000",0.65\],\["#26000000",0.75\],\["#12000000",0.85\], \["#00000000",1\]\]**, with the gradient applied in the direction [GradientDirection](../../../arkui/arkts-components/common-definitions/enums/document.md#gradientdirection).Bottom.

 |
| 

maskExtraHeight

 | 

number

 | 

No

 | 

Yes

 | 

Additional height that the blur overlay extends beyond the title bar. This setting takes effect only for the **GRADIENT\_BLUR** blur type. The unit is vp.

The default value is **32**.

**Start version**: 6.0.0(20)

 |

#### HdsNavigationTitleStyle

Defines the title style for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

mainTitleColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Main title color of the title bar.

Default value:

-   When the **COMMON\_BLUR** blur type is used, the default color of the main title is **$r('sys.color.font\_primary')**.
-   When the **GRADUAL\_BLUR** blur type is used, the default color of the main title is **$r('sys.color.font\_on\_primary')** before the dynamic style takes effect and is **$r('sys.color.font\_primary')** after the dynamic style takes effect.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **false**, the default color of the main title is **$r('sys.color.font\_on\_primary')**.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **true**, the default color of the main title is **$r('sys.color.font\_primary')** before the dynamic style takes effect and is **$r('sys.color.font\_on\_primary')** after the dynamic style takes effect.

 |
| 

subTitleColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Subtitle color of the title bar.

Default value:

-   When the **COMMON\_BLUR** blur type is used, the default color of the subtitle is **$r('sys.color.font\_secondary')**.
-   When the **GRADUAL\_BLUR** blur type is used, the default color of the subtitle is **$r('sys.color.font\_on\_secondary')** before the dynamic style takes effect and is **$r('sys.color.font\_secondary')** after the dynamic style takes effect.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **false**, the default color of the subtitle is **$r('sys.color.font\_on\_secondary')**.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **true**, the default color of the subtitle is **$r('sys.color.font\_secondary')** before the dynamic style takes effect and is **$r('sys.color.font\_on\_secondary')** after the dynamic style takes effect.

 |

#### HdsNavigationIconItemStyle

Defines the icon style for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

backgroundColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of an icon on the title bar.

Default value:

-   When the **COMMON\_BLUR** blur type is used, the default background color of an icon is **$r('sys.color.comp\_background\_tertiary')**.
-   When the **GRADUAL\_BLUR** blur type is used, the default background color of an icon is transparent and the darkening and brightening style also takes effect.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **false**, the default background color of an icon is transparent and the darkening and brightening style also takes effect.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **true**, the default background color of an icon is **$r('sys.color.comp\_background\_tertiary')** before the dynamic style takes effect and is transparent after the dynamic style takes effect, with the brightening and darkening style enabled.

 |
| 

iconColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Color of an icon on the title bar. This setting takes effect when the icon mode is set to [IconStyleMode](#section172403812484).

Default value:

-   When the **COMMON\_BLUR** blur type is used, the default color of an icon is **$r('sys.color.icon\_primary')**.
-   When the **GRADUAL\_BLUR** blur type is used, the default color of an icon is **$r('sys.color.icon\_on\_primary')** before the dynamic style takes effect and is **$r('sys.color.icon\_primary')** after the dynamic style takes effect.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **false**, the default color of an icon is **$r('sys.color.icon\_on\_primary')**.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **true**, the default color of an icon is **$r('sys.color.icon\_primary')** before the dynamic style takes effect and is **$r('sys.color.icon\_on\_primary')** after the dynamic style takes effect.

 |
| 

textColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Font color of an icon on the title bar. This setting takes effect when the icon mode is set to [TextStyleMode](#section1563041134414).

Default value:

-   When the **COMMON\_BLUR** blur type is used, the default font color of an icon is **$r('sys.color.font\_primary')**.
-   When the **GRADUAL\_BLUR** blur type is used, the default font color of an icon is **$r('sys.color.font\_on\_primary')** before the dynamic style takes effect and is **$r('sys.color.font\_primary')** after the dynamic style takes effect.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **false**, the default font color of an icon is **$r('sys.color.font\_on\_primary')**.
-   When the **GRADIENT\_BLUR** blur type is used and **ScrollEffectOptions.enableScrollEffect** is set to **true**, the default font color of an icon is **$r('sys.color.font\_primary')** before the dynamic style takes effect and is **$r('sys.color.font\_on\_primary')** after the dynamic style takes effect.

**Start version**: 6.0.0(20)

 |

#### HdsNavigationDividerStyle

Defines the divider style for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

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

dividerColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Color of the divider on the title bar.

Default value: **$r('sys.color.comp\_divider')**

 |

#### HdsTitleBarContentStyle

Defines the content area style for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

titleStyle

 | 

[HdsNavigationTitleStyle](#section18445141914017)

 | 

No

 | 

Yes

 | 

Title style of the title bar content area.

 |
| 

menuStyle

 | 

[HdsNavigationIconItemStyle](#section1132015774014)

 | 

No

 | 

Yes

 | 

Menu bar style of the title bar content area.

 |
| 

backIconStyle

 | 

[HdsNavigationIconItemStyle](#section1132015774014)

 | 

No

 | 

Yes

 | 

Back button icon style of the title bar content area.

 |
| 

subIconStyle

 | 

[HdsNavigationIconItemStyle](#section1132015774014)

 | 

No

 | 

Yes

 | 

Sub-icon style of the title bar content area.

**Start version**: 6.0.0(20)

 |
| 

dividerStyle

 | 

[HdsNavigationDividerStyle](#section1967916431016)

 | 

No

 | 

Yes

 | 

Divider style of the title bar content area.

**Start version**: 6.0.0(20)

 |

#### HdsNavigationTitleBarStyle

Defines the title bar style of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

backgroundStyle

 | 

[HdsNavigationBackgroundStyle](#section6828845123712)

 | 

No

 | 

Yes

 | 

Title bar background style of the **HdsNavigation** component.

 |
| 

contentStyle

 | 

[HdsTitleBarContentStyle](#section8553559194113)

 | 

No

 | 

Yes

 | 

Content area style for the title bar of the **HdsNavigation** component.

 |

#### ScrollEffectOptions

Defines the dynamic blur style settings for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

enableScrollEffect

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the blur styles of the title take effect when scrolling with the content area dynamically.

The default value is **true**.

**true**: yes

**false**: no

 |
| 

scrollEffectType

 | 

[ScrollEffectType](#section21731754221)

 | 

No

 | 

Yes

 | 

Blur style type of the title bar.

The default value is **ScrollEffectType.COMMON\_BLUR**.

 |
| 

blurEffectiveStartOffset

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Lower threshold of the scrolling distance of the content area for making the dynamic style of the title bar effective during scrolling.

The default value is **LengthMetric.vp(0)**.

When the title bar no longer reduces in size as the content area scrolls, the scrolling distance starts to be calculated.

 |
| 

blurEffectiveEndOffset

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Upper threshold of the scrolling distance in the content area when the dynamic style takes effect. Between the lower threshold and the upper threshold, the dynamic style changes linearly with the scrolling distance.

Default value:

-   If the title bar blur style type is **ScrollEffectType.COMMON\_BLUR** or **ScrollEffectType.GRADIENT\_BLUR**, the default value is **LengthMetric.vp(8)**.
-   If the title bar blur style type is **ScrollEffectType.GRADUAL\_BLUR**, the default value is **LengthMetric.vp(56)**.

When the title bar no longer reduces in size as the content area scrolls, the scrolling distance starts to be calculated.

 |

#### TitleBarStyleOptions

Defines the style settings for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

scrollEffectOpts

 | 

[ScrollEffectOptions](#section646561734417)

 | 

No

 | 

Yes

 | 

Dynamic blur style settings for the title bar of the **HdsNavigation** component.

 |
| 

originalStyle

 | 

[HdsNavigationTitleBarStyle](#section2462651174318)

 | 

No

 | 

Yes

 | 

Initial style of the title bar before the dynamic style takes effect.

 |
| 

scrollEffectStyle

 | 

[HdsNavigationTitleBarStyle](#section2462651174318)

 | 

No

 | 

Yes

 | 

Final style of the title bar after the dynamic style takes effect.

If the blur effect settings do not match the blur type, the default style settings corresponding to the current blur type take effect.

 |
| 

blurStrategy

 | 

[BlurStrategy](#section1086755971212)

 | 

No

 | 

Yes

 | 

Effective strategy for the blur type of the title bar.

The default value is **BlurStrategy.ADAPTIVE**.

**Start version**: 6.0.0(20)

 |

#### HdsNavigationBadgeOptions

Defines the message reminder badge settings of the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

count

 | 

number

 | 

No

 | 

Yes

 | 

Message quantity displayed on the reminder badge. If the number is greater than 99, **99+** is displayed.

Value range: \[-2147483648,2147483647\]. If the value is out of the range, **4294967296** is added or subtracted so that the value is within the range. If the value is not an integer, it is rounded off to the nearest integer.

The default value is **–1**.

If this parameter is set to a value less than or equal to 0, no reminder badge is displayed.

 |
| 

value

 | 

string

 | 

No

 | 

Yes

 | 

Text string of the reminder content.

-   If both **value** and **count** are set, the setting of **value** is displayed preferentially.
-   If this parameter is not set, the reminder display is subject to the setting of **count**.
-   If this parameter is set to an empty string, the reminder badge displays as a small red dot.

 |
| 

accessibilityText

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility text of the message reminder badge on the title bar.

If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

**Start version**: 6.0.0(20)

 |

#### HdsNavigationIconOptions

Defines icon settings for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

icon

 | 

[IconType](#section2930111714251)

 | 

No

 | 

Yes

 | 

Image resource type supported by a single menu item of the icon type on the title bar.

If this parameter is not set, a blank icon is displayed.

 |
| 

label

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Text of an icon-type menu item.

Default value: **""**

 |
| 

isEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Specifies whether to enable an icon.

The default value is **true**.

**true**: yes

**false**: no

 |
| 

action

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

No

 | 

Yes

 | 

Callback triggered when a menu item is selected.

 |
| 

componentId

 | 

string

 | 

No

 | 

Yes

 | 

Unique ID you assigned to a component.

Default value: **""**

**Start version**: 6.0.0(20)

 |
| 

type

 | 

[IconStyleMode](#section172403812484) | [TextStyleMode](#section1563041134414)

 | 

No

 | 

Yes

 | 

Icon type of the title bar. If the icon type is set to **TextStyleMode.NORMAL**, the icon does not support the **badge** attribute.

The default value is **IconStyleMode.NORMAL**.

**Start version**: 6.0.0(20)

 |

#### HdsNavigationBadgeIconOptions

Defines the settings of icon-type menu items with a reminder badge for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

content

 | 

[HdsNavigationIconOptions](#section74312125454)

 | 

No

 | 

Yes

 | 

Icon settings.

 |
| 

badge

 | 

[HdsNavigationBadgeOptions](#section9994192913455)

 | 

No

 | 

Yes

 | 

Badge settings.

 |

#### HdsNavigationMenuContentOptions

Defines the content settings of the menu area for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

value

 | 

Array<[HdsNavigationMenuItemOptions](#section16350125562818)\>

 | 

No

 | 

Yes

 | 

Icon settings of the menu bar.

 |
| 

maxCount

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of icons that can be displayed on the menu bar. By default, a maximum of three icons can be displayed. Other icons will be added to the **More** option that is automatically generated.

 |
| 

multiWindowEntryInAPPMenu

 | 

[MultiWindowEntryInAPPMenuParams](#section34012132713)

 | 

No

 | 

Yes

 | 

Menu bar settings for the in-app multi-window effect.

NOTE:

This capability is applicable only when the current device and its screen state support the multitask view. Currently, the following device types support the multitask view:

-   Bi-fold phones in unfolded state
-   Tri-fold phones in Dual screen mode or Triple screen mode (in landscape mode)
-   Tablets in landscape mode

For other device types or states, this component will not respond to any taps on the in-app multi-window icon.

**Start version**: 6.0.0(20)

 |

#### MultiWindowEntryInAPPMenuParams

Defines the in-app multi-window settings of the menu area for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

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

want

 | 

[Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)

 | 

No

 | 

No

 | 

Parameters for starting multiple windows. The requirements are as follows:

-   The **abilityName**, **moduleName**, and **bundleName** fields are mandatory.
-   App restrictions: All the specified fields (including **abilityName**, **moduleName**, and **bundleName**) must belong to the current app.
-   Cross-app restrictions: The multi-windows function does not support cross-app capabilities.

 |

#### HdsNavigationTitle

Defines title resource configuration for the title bar of the **HdsNavigation** component. When the title string is too long: (1) If no subtitle is set, the string is scaled down, wrapped in two lines, and then clipped if the text is still overlong. (2) If a subtitle is set, the subtitle is scaled down and then clipped with an ellipsis (...) if the text is still overlong.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

mainTitle

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

No

 | 

Main title of the title bar.

 |
| 

subTitle

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Subtitle of the title bar. If this parameter is not set, no subtitle is displayed.

 |
| 

subTitleBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Yes

 | 

Custom area at the bottom of the title bar. This setting takes effect only when the title bar mode is set to **HdsNavigationTitleMode.MODAL** or **HdsNavDestinationTitleMode.MODAL**.

**Start version**: 6.0.0(20)

 |
| 

subTitleComponent

 | 

[ComponentContent](../../../arkui/arkts-api/ui/arkui/componentcontent/document.md)

 | 

No

 | 

Yes

 | 

Custom area at the bottom of the title bar. This setting takes effect only when the title bar mode is set to **HdsNavigationTitleMode.MODAL** or **HdsNavDestinationTitleMode.MODAL**.

If both **subTitleBuilder** and **subTitleComponent** are set, only **subTitleComponent** takes effect.

**Start version**: 6.0.1(21)

 |
| 

mainTitleId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the component to which the main title belongs.

Default value: **""**

**Start version**: 6.0.0(20)

 |
| 

subTitleId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the component to which the subtitle belongs.

Default value: **""**

**Start version**: 6.0.0(20)

 |

#### BottomBuilderParams

Defines the custom area settings at the bottom of the title bar for the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

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

builder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

No

 | 

Content in the custom area at the bottom of the title bar.

 |
| 

builderComponent

 | 

[ComponentContent](../../../arkui/arkts-api/ui/arkui/componentcontent/document.md)

 | 

No

 | 

Yes

 | 

Content in the custom area at the bottom of the title bar.

If both **builder** and **builderComponent** are set, only **builderComponent** takes effect.

**Start version**: 6.0.1(21)

 |
| 

height

 | 

[Length](../../../arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

No

 | 

Yes

 | 

Height of the custom area at the bottom of the title bar. The value cannot be a percentage.

The default value is 56 vp.

 |
| 

showType

 | 

[BottomBuilderShowType](#section1621712719586)

 | 

No

 | 

Yes

 | 

Display type of the custom area at the bottom of the title bar. This parameter takes effect only when **HideMode** is set to **HideMode.SCROLL\_UP\_TO**.

The default value is **BottomBuilderShowType.DIRECTLY\_SHOW**.

 |

#### HdsNavigationDividerParams

Defines the title bar divider parameter for the **HdsNavigation** component. The parameter cannot be changed dynamically.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

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

showType

 | 

[DividerShowType](#section1759271114393)

 | 

No

 | 

Yes

 | 

Display type of the divider on the title bar.

The default value is **DividerShowType.AUTO**.

 |

#### TitleBarContentOptions

Defines content area settings for the title bar of the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

title

 | 

[HdsNavigationTitle](#section59501489496)

 | 

No

 | 

Yes

 | 

Title content of the title bar.

 |
| 

menu

 | 

[HdsNavigationMenuContentOptions](#section158052224917)

 | 

No

 | 

Yes

 | 

Menu content of the title bar.

 |
| 

backIcon

 | 

[HdsNavigationBackButtonItemOptions](#section1931715301301)

 | 

No

 | 

Yes

 | 

Content of the back button on the title bar.

 |
| 

stackBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Yes

 | 

Custom area at the top of the title bar.

**Start version**: 6.0.0(20)

 |
| 

stackBuilderComponent

 | 

[ComponentContent](../../../arkui/arkts-api/ui/arkui/componentcontent/document.md)

 | 

No

 | 

Yes

 | 

Custom area at the top of the title bar.

If both **stackBuilder** and **stackBuilderComponent** are set, only **stackBuilderComponent** takes effect.

**Start version**: 6.0.1(21)

 |
| 

bottomBuilder

 | 

[BottomBuilderParams](#section022717175435)

 | 

No

 | 

Yes

 | 

Custom area at the bottom of the title bar.

**Start version**: 6.0.0(20)

 |
| 

divider

 | 

[HdsNavigationDividerParams](#section102561040192912)

 | 

No

 | 

Yes

 | 

Divider settings of the title bar.

**Start version**: 6.0.0(20)

 |
| 

subIcon

 | 

[HdsNavigationBadgeIconOptions](#section7349101217489)

 | 

No

 | 

Yes

 | 

Sub-icon content of the title bar.

**Start version**: 6.0.0(20)

 |

#### PaddingOptions

Defines the padding settings of the title bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

start

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Padding at the start of the title bar.

Default value: 16 vp for pages with a width less than 600 vp; 32 vp for pages with a width greater than or equal to 840 vp; 24 vp for other page widths.

 |
| 

end

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Padding at the end of the title bar.

Default value: 16 vp for pages with a width less than 600 vp; 32 vp for pages with a width greater than or equal to 800 vp; 24 vp for other page widths.

 |

#### NavBarWidthRangeOptions

Defines the maximum and minimum widths of the navigation bar.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

minWidth

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Minimum width of the navigation bar.

The default value is 240 vp.

 |
| 

maxWidth

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Maximum width of the navigation bar.

The default value is 40% of the component width, in vp. If this value is greater than 432, 432 vp is used.

 |

#### HdsNavigationTitleBarOptions

Defines the title bar settings for the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 5.1.0(18)

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

padding

 | 

[PaddingOptions](#section14824153495010)

 | 

No

 | 

Yes

 | 

Padding settings of the title bar.

 |
| 

style

 | 

[TitleBarStyleOptions](#section4190244154420)

 | 

No

 | 

Yes

 | 

Style settings of the title bar.

 |
| 

content

 | 

[TitleBarContentOptions](#section156391311175017)

 | 

No

 | 

Yes

 | 

Content area settings of the title bar.

 |
| 

enableHoverMode

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the hover mode.

The usage restrictions of this mode are as follows:

1\. The mode can take effect only when the **HdsNavigation** component is in full screen.

2\. If the title bar mode is **HdsNavigationTitleMode.FREE**, settings made through this API do not take effect.

The default value is **false**.

**true**: yes

**false**: no

**Start version**: 6.0.0(20)

 |
| 

avoidLayoutSafeArea

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the title bar needs to avoid the safe area.

The default value is **false**.

**true**: yes

**false**: no

**Start version**: 6.0.0(20)

 |
| 

enableComponentSafeArea

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to configure the title bar as a [component-level safe area](../../../arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#safeareapadding14).

The default value is **false**.

**true**: yes

**false**: no

**Start version**: 6.0.0(20)

 |

#### DynamicHideParams

Defines the dynamic display/hide mode of the title bar for the **HdsNavigation** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

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

hideTitleArea

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to hide the title area.

The default value is **false**.

**true**: yes

**false**: no

 |
| 

hideBottomBuilder

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to hide the custom area at the bottom of the title bar.

The default value is **false**.

**true**: yes

**false**: no

 |
| 

hideStatusBar

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to hide the status bar area. Hiding the status bar area can take effect only when the title area is hidden.

The default value is **false**.

**true**: yes

**false**: no

 |
| 

mode

 | 

[HideMode](#section1576811571633)

 | 

No

 | 

Yes

 | 

Dynamic hiding mode of the title bar.

The default value is **HideMode.SCROLL\_UP\_TO**.

 |
| 

hideOffset

 | 

number

 | 

No

 | 

Yes

 | 

Scrolling distance at which the title bar starts to hide. This parameter takes effect only when **HideMode** is set to **SCROLL\_UP\_TO**.

The unit is vp.

The default value is **0**.

 |
| 

hideRatio

 | 

number

 | 

No

 | 

Yes

 | 

Ratio of the content area scrolling distance to title bar hide distance. The value range is \[1.0,3.0\].

For every 1 vp the content area scrolls, the title bar hides by 1/**hideRatio** vp.

If the value is out of the range, the default value is used.

The default value is **2.0**.

 |

#### NestedScrollInfo

Defines the information about the nested scrollable containers.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

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

parent

 | 

[Scroller](../../../arkui/arkts-components/scroll-and-swipe/scroll/document.md#scroller)

 | 

No

 | 

No

 | 

Controller of the target scrollable container.

 |
| 

child

 | 

[Scroller](../../../arkui/arkts-components/scroll-and-swipe/scroll/document.md#scroller)

 | 

No

 | 

No

 | 

Controller of the scrollable container nested within the target scrollable container. This scrollable container is a child component of the target scrollable container.

 |

#### Example

#### \[h2\]Setting the Dynamic Blur Style

In the following code, the **titleBar** attribute is used to customize the dynamic blur style of the title bar when it scrolls with the content area.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { HdsNavigation, HdsNavigationAttribute, ScrollEffectType, HdsNavigationTitleMode } from '@kit.UIDesignKit';
import { LengthMetrics } from '@kit.ArkUI';

const  TITLE\_BAR\_HEIGHT\_FREE: number = 138;
@Entry
@Component
struct Index {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  scroller: Scroller = new Scroller();
  @State blankHeight: number = TITLE\_BAR\_HEIGHT\_FREE;
  @State isHideBackButton: boolean = false;
  @State titleMode: HdsNavigationTitleMode = HdsNavigationTitleMode.FREE;
  @State subTitle: string = 'Sub'

  build() {
    HdsNavigation(this.pageInfos) {
      Column() {
        Stack() {
          Scroll(this.scroller) {
            Column() {
              Blank().height(this.blankHeight)
              Image($r('app.media.scenery')).width('100%') // **scenery** is a custom resource. You need to replace it with your local resource.
            }
          }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
        }
      }
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
        }, scrollEffectStyle: {
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
          mainTitle: 'Main',
          subTitle: this.subTitle
        },
        menu: {
          value: \[{
            content: {
              label: 'menu1',
              icon: $r('sys.symbol.ohos\_wifi'),
              isEnabled: true,
              action: () => {
                console.info("HdsNavigation menu1");
              }
            }
          }, {
            content: {
              label: 'menu2',
              icon: $r('sys.symbol.plus'),
              isEnabled: true,
            }
          }, {
            content: {
              label: 'menu3',
              icon: $r('sys.symbol.lock'),
            }
          }, {
            content: {
              label: 'menu4',
              icon: $r('sys.symbol.trunk'),
            }
          }\]
        },
        backIcon: {
          label: 'backButton',
          icon: $r('sys.symbol.trunk'),
          isEnabled: true,
        }
      }
    })
    .systemBarStyle({ statusBarContentColor: '#0A59F7' }, { statusBarContentColor: '#C7C7CD' })
    .titleMode(this.titleMode)
    .hideBackButton(this.isHideBackButton)
    .hideTitleBar(false)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/bSg2togoQP673z340rXn9A/en-us_image_0000002500304242.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D74DD5508D36A2A4E081B6EF02B07918622CA12E3BA23AE54C180B818DEDE41 "Click to enlarge")

#### \[h2\]Setting the Menu Message Reminder

You can add a message reminder badge to the upper right corner of a menu item by configuring the **badge** attribute in menu item settings of the title bar.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { HdsNavigation, HdsNavigationAttribute } from '@kit.UIDesignKit';

const  TITLE\_BAR\_HEIGHT\_FREE: number = 138;
@Entry
@Component
struct Index {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  @State blankHeight: number = TITLE\_BAR\_HEIGHT\_FREE;
  @State subTitle: string = 'Sub';

  build() {
    HdsNavigation(this.pageInfos) {
      Column() {
        Stack() {
          Column() {
            Blank().height(this.blankHeight)
            Image($r('app.media.background1')) // **background1** is a custom resource. You need to replace it with your local resource.
              .width('100%')
          }
        }
      }
    }
    .titleBar({
      content: {
        title: {
          mainTitle: "Main",
          subTitle: this.subTitle
        },
        menu: {
          value: \[{
            content: {
              label: 'menu1',
              icon: $r('sys.symbol.plus'),
              isEnabled: true,
            },
            badge: {
              count: 1,
            }
          }, {
            content: {
              label: 'menu2',
              icon: $r('sys.symbol.trunk'),
              isEnabled: true,
            },
            badge: {
              count: 100,
            }
          }\]
        },
      }
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/gXg6c06-RfaxOD8yKgD7Lg/en-us_image_0000002532144149.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FFEE1A092A3EAB736D0BA7AD478B56D866102F76772C1009D081353893CCF37 "Click to enlarge")

#### \[h2\]Configuring the Custom Area

You can set the **stackBuilder** and **bottomBuilder** attributes under **titleBar** to configure the custom area of the title bar.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { HdsNavigation, HdsNavigationAttribute, ScrollEffectType } from '@kit.UIDesignKit';
import { LengthMetrics } from '@kit.ArkUI';

const  TITLE\_BAR\_HEIGHT\_FREE: number = 138;
const BOTTOM\_BUILDER\_HEIGHT: number = 56;
@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  @State blankHeight: number = TITLE\_BAR\_HEIGHT\_FREE + BOTTOM\_BUILDER\_HEIGHT;

  @Builder
  StackBuilder() {
    Column() {
      Button("HdsNavigation")
    }
    .height(56)
    .justifyContent(FlexAlign.Center)
  }

  @Builder
  BottomBuilder() {
    Column() {
      Search()
    }
    .width('100%')
    .height(56)
  }

  build() {
    Column() {
      HdsNavigation() {
        Scroll(this.scroller) {
          Column() {
            Blank().height(this.blankHeight).width('100%')
            Image($r('app.media.scenery')).width('100%') // **scenery** is a custom resource. You need to replace it with your local resource.
          }
        }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
      }
      .titleBar({
        style: {
          scrollEffectOpts: {
            enableScrollEffect: true,
            scrollEffectType: ScrollEffectType.GRADIENT\_BLUR,
            blurEffectiveStartOffset: LengthMetrics.vp(0),
            blurEffectiveEndOffset: LengthMetrics.vp(20)
          },
          scrollEffectStyle: {
            backgroundStyle: { maskExtraHeight: 56.0 },
          }
        },
        content: {
          title: {
            mainTitle: 'MainTitle',
            subTitle: 'SubTitle'
          },
          stackBuilder: (): void => this.StackBuilder(),
          bottomBuilder: { builder: (): void => this.BottomBuilder() },
          menu: {
            value: \[{
              content: {
                label: 'menu1',
                icon: $r('sys.symbol.plus'),
              },
            }, {
              content: {
                label: 'menu2',
                icon: $r('sys.symbol.lock'),
              }
            }\]
          }
        }
      })
      .bindToScrollable(\[this.scroller\])
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/dsJLUZV8QT-1SZgArd6Png/en-us_image_0000002500424092.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DE56C20FE6FEEDCFE228C561CD8BBFCD10F26DF889951B45F475EA3990DAD42 "Click to enlarge")

#### \[h2\]Dynamically Displaying and Hiding the Title Bar

You can set the **dynamicHideTitleBar** attribute to dynamically display or hide the title bar as the content area scrolls.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { HdsNavigation, HdsNavigationAttribute, HideMode } from '@kit.UIDesignKit';

const TITLE\_BAR\_HEIGHT\_FREE: number = 138;
const BOTTOM\_BUILDER\_HEIGHT: number = 56;
@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  @State blankHeight: number = TITLE\_BAR\_HEIGHT\_FREE + BOTTOM\_BUILDER\_HEIGHT;

  @Builder
  BottomBuilder() {
    Column() {
      Search()
    }
    .width('100%')
    .height(56)
  }

  build() {
    Column() {
      HdsNavigation() {
        Scroll(this.scroller) {
          Column() {
            Blank().height(this.blankHeight).width('100%')
            Image($r('app.media.scenery')).width('100%') // **scenery** is a custom resource. You need to replace it with your local resource.
          }
        }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
      }
      .titleBar({
        content: {
          title: {
            mainTitle: 'MainTitle',
            subTitle: 'SubTitle'
          },
          bottomBuilder: { builder: (): void => this.BottomBuilder() },
          menu: {
            value: \[{
              content: {
                label: 'menu1',
                icon: $r('sys.symbol.plus'),
              },
            }\]
          }
        }
      })
      .bindToScrollable(\[this.scroller\])
      .dynamicHideTitleBar({hideTitleArea: true, hideBottomBuilder: true, hideStatusBar: false, mode: HideMode.SCROLL\_UP\_TO})
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/rUG-1UsyRZKfpDxR5CdXOw/en-us_image_0000002532304127.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04EC83E9FC2C91F3B783A5302CBB1DAE6E78270775795AE6E78FCDC368309304 "Click to enlarge")

#### \[h2\]Setting the Icon Style for the Title Bar

You can set the **type** attribute in **HdsNavigationIconOptions** to configure the icon type as text or image.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { 
  HdsNavigation,
  HdsNavigationAttribute,
  HdsNavigationTitleMode,
  IconStyleMode,
  TextStyleMode,
  DividerShowType } from '@kit.UIDesignKit';

const TITLE\_BAR\_HEIGHT\_MINI: number = 56;
@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  @State blankHeight: number = TITLE\_BAR\_HEIGHT\_MINI;

  build() {
    Column() {
      HdsNavigation() {
        Scroll(this.scroller) {
          Column() {
            Blank().height(this.blankHeight).width('100%')
            Image($r('app.media.background1')).width('100%')
          }
        }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
      }
      .titleMode(HdsNavigationTitleMode.MINI)
      .titleBar({
        content: {
          title: {
            mainTitle: 'Main',
            subTitle: 'Sub'
          },
          menu: {
            value: \[{
              content: {
                label: 'CAPSULE',
                type: TextStyleMode.NORMAL,
              }
            }, {
              content: {
                label: '5',
                type: TextStyleMode.SINGLE\_CHARACTER,
              }
            }, {
              content: {
                label: 'smallIcon',
                icon: $r('sys.symbol.plus'),
                type: IconStyleMode.LARGE,
              }
            }\]
          },
          subIcon: {
            content: {
              label: 'headIcon',
              icon: $r('sys.symbol.lock'),
              type: IconStyleMode.SMALL,
            }
          },
          divider: { showType: DividerShowType.ON },
        }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/aZhgxzfUTpGQUwbB_TDgsA/en-us_image_0000002500304234.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A801F0DFC25C3BB57E12EB71D18B1BBF4D6E98FF5EEB49C1E20A2329895F10CB "Click to enlarge")

#### \[h2\]Title Bar Sheet Style

You can use **titleMode** to set the sheet style for the title bar. In this mode, you can use **subTitleBuilder** to customize the content on the right side of **subTitle**. In the sheet style, if the icon type is set to **IconStyleMode.SMALL** and no icon resource is passed, a close icon is displayed by default.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode, IconStyleMode } from '@kit.UIDesignKit';

const TITLE\_BAR\_HEIGHT\_MODAL: number = 80;
@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;
  @State blankHeight: number = TITLE\_BAR\_HEIGHT\_MODAL;
  scroller: Scroller = new Scroller();
  @Builder
  SubTitleBuilder() {
    Text("click to share")
      .fontColor(Color.Blue)
      .maxFontScale(1)
      .lineHeight(\`${14\*1.49}vp\`)
      .fontSize(14)
      .onClick(() => {
        console.info("click to share");
      })
  }

  // Create content to be displayed in sheet style.
  @Builder
  myBuilder() {
    Column() {
      HdsNavigation() {
        Scroll(this.scroller) {
          Column() {
            Blank().height(this.blankHeight).width('100%')
            Image($r('app.media.background1')) // **background1** is a custom resource. You need to replace it with your local resource.
              .width('100%')
          }
        }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
      }
      .titleMode(HdsNavigationTitleMode.MODAL) // Configure the display mode of the **HdsNavigation** component as the sheet style.
      .titleBar({
        content: {
          title: {
            mainTitle: 'MainTitle',
            subTitle: 'SubTitle',
            subTitleBuilder: this.SubTitleBuilder.bind(this), // Custom subtitle area.
          },
          menu: {
            value: \[{
              content: {
                label: 'modal\_cancel',
                isEnabled: true,
                type: IconStyleMode.SMALL,
                action: () => {
                  console.info("model cancel");
                }
              }
            }\]
          },
          subIcon: {
            content: {
              label: 'leftIcon',
              icon:  $r('sys.symbol.ohos\_wifi'),
              isEnabled: true,
            }
          },
        }
      })
    }
  }

  build() {
    Column() {
      Button("transition modal")
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {showClose: false}) // Bind the sheet page.
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/gJKBlEerRpeK1LttbpPxaA/en-us_image_0000002500304230.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF2810ABD2EC1B4E772B752F6A69429E2848888FD92479AF6ACE65F658AB75EA "Click to enlarge")

#### \[h2\]Binding a Custom Menu to an Icon

You can set the **componentId** attribute under **HdsNavigationIconOptions** and then call the **promptAction.openMenu** method to set the **Id** attribute in **TargetInfo** to the value of **componentId**, so that a custom menu can be displayed from a specific icon.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
import { ComponentContent, LengthMetrics, Prompt  } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

const TITLE\_BAR\_HEIGHT\_FULL: number = 138;
@Builder
function menuComponent() {
  Menu() {
    MenuItem({ content: "copy" }).onClick(() => {
      Prompt.showToast({ message: 'on click' })
    })
    MenuItem({ content: "paste" }).enabled(false)
  }
  .width(224).menuItemDivider({ strokeWidth: LengthMetrics.px(1), color: $r('sys.color.comp\_divider') })
}
@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  @State blankHeight: number = TITLE\_BAR\_HEIGHT\_FULL;
  private targetId: string = 'bindMenu'
  build() {
    Column() {
      HdsNavigation() {
        Scroll(this.scroller) {
          Column() {
            Blank().height(this.blankHeight).width('100%')
            Image($r('app.media.background1'))
              .width('100%')
          }
        }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
      }
      .titleMode(HdsNavigationTitleMode.FULL)
      .titleBar({
        content: {
          title: {
            mainTitle: 'MainTitle',
            subTitle: 'SubTitle'
          },
          menu: {
            value: \[{
              content: {
                label: 'menu1',
                icon: $r('sys.symbol.plus'),
                isEnabled: true,
                componentId: this.targetId,
                action: () => {
                  let uiContext = this.getUIContext();
                  let promptAction = uiContext.getPromptAction();
                  let contentNode = new ComponentContent(uiContext, wrapBuilder(menuComponent));
                  try {
                    promptAction.openMenu(
                      contentNode,
                      { id: this.targetId },
                      { backgroundColor: Color.Yellow })
                  } catch (error) {
                    let message = (error as BusinessError).message;
                    let code = (error as BusinessError).code;
                    console.error(\`openMenu args error code is ${code}, message is ${message}\`);
                  }
                  console.info("model cancel");
                }
              }
            }, {
              content: {
                label: 'menu2',
                icon: $r('sys.symbol.ohos\_wifi'),
              }
            }\]
          },
        }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/6hjiNhiHS-KZUL8lkJS-Jg/en-us_image_0000002532304119.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9B320E54288E98385F67D80E218AAD21FA119C91A78187569E3566E1D1E6885 "Click to enlarge")

#### \[h2\]Configuring the In-App Multi-Window Icon

Create a level-1 navigation component. Then set the **multiWindowEntryInAPPMenu** attribute under **menu** in **titleBar** to configure the in-app multi-window icon.

// Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
import { HdsNavigation, HdsNavigationAttribute, HdsNavigationMenuContentOptions } from '@kit.UIDesignKit';
import { Want } from '@kit.AbilityKit';

@Entry
@Component
struct MultiWindowEntryInAPPTest {
  private want: Want = {
    // Replace the values of **bundleName**, **moduleName**, and **abilityName** with those of your app to start the **UIAbility** in the app.
    bundleName: "com.example.myapplication",
    moduleName: "entry",
    abilityName: "FuncAbility",
  }
  @State menuContent: HdsNavigationMenuContentOptions = {
    multiWindowEntryInAPPMenu: {
      want: this.want,
    },
    maxCount: 3,
    value: \[
      { content: { label: 'menu1', icon: $r('sys.symbol.search\_things'), } },
      { content: { label: 'menu2', icon: $r('sys.symbol.plus'), } }
    \]
  }

  build() {
    HdsNavigation() {
      Stack() {
        Text("Page1")
      }.alignContent(Alignment.Center)
      .width("100%")
      .height("100%")
    }
    .hideToolBar(false)
    .navBarWidth('100%')
    .titleBar({
      content: {
        title: {
          mainTitle: "Index"
        },
        menu: this.menuContent
      }
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/FEN6weN1QGeMSDdCvCOSWA/en-us_image_0000002532144155.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2094F71F68C0179C31ED74A2501FFD09B4D9F890673FFAAFCC35CC8CCECD064E "Click to enlarge")
