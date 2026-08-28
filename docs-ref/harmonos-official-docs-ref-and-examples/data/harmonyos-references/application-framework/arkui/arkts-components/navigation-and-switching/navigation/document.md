# Navigation

The **Navigation** component is the root view container for navigation. It typically functions as the root container of a page and includes a title bar, content area, and toolbar. The content area switches between the home page content (child components of **Navigation**) and non-home page content (child components of [NavDestination](../navdestination/document.md)) through routing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/tgA8j-oIR9KzDGWQj8NX0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6E98875818B39922A81152AFB8AB3697878462D3F17DB35B1113DC4E0E35102)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Since API version 11, this component supports the safe area attribute by default, with the default attribute value being **expandSafeArea(\[SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT\], \[SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM\])**. You can override this attribute to change the default behavior. In earlier versions, you need to use the [expandSafeArea](../../universal-attributes/layout-and-borders/safe-area/document.md#expandsafearea) attribute to implement the safe area feature.
    
-   When [NavBar](#navbar12) is nested within a **Navigation** component, the lifecycle of the inner **NavDestination** component does not synchronize with the outer **NavDestination** component or the lifecycle of a [modal](../../universal-attributes/transition/modal-transition/document.md).
    
-   If the [title](#title) and [subTitle](#subtitledeprecated) are not set and [hideBackButton](#hidebackbutton) is set to **true**, the title bar is not displayed.
    
-   During subpage navigation within **Navigation**, the new page actively requests focus.
    
-   You are not advised to use stack operations in [aboutToAppear](../../custom-components/custom-component-lifecycle/document.md#abouttoappear), as the page has not yet finished building at this stage, which may lead to issues such as white screens or navigation failures.
    

#### Child Components

Supported

Since API version 9, it is recommended that this component be used together with the [NavRouter](../../components-and-apis-no-longer-maintained/navrouter/document.md) component.

Since API version 10, it is recommended that this component be used together with the [NavPathStack](#navpathstack10) component and [navDestination](#navdestination10) attribute for page routing.

#### APIs

#### \[h2\]Navigation

Navigation()

Creates a root view container for route navigation, suitable for page routing using the [NavRouter](../../components-and-apis-no-longer-maintained/navrouter/document.md) component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Navigation10+

Navigation(pathInfos: NavPathStack)

Binds a navigation controller to the **Navigation** component, suitable for page routing using [NavPathStack](#navpathstack10) with the [navDestination](#navdestination10) attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pathInfos | [NavPathStack](#navpathstack10) | Yes | Navigation controller object. |

#### \[h2\]Navigation20+

Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)

Binds a routing stack to the **Navigation** component and specifies a **NavDestination** component as the navigation page (home page) for **Navigation**. This is suitable for page routing using [NavPathStack](#navpathstack10) with the [navDestination](#navdestination10) attribute or the system routing table. For the usage example, see [Example 16: Using NavDestination as a Navigation Page in Navigation](#example-16-using-navdestination-as-a-navigation-page-in-navigation).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pathInfos | [NavPathStack](#navpathstack10) | Yes | Information about the routing stack. |
| homeDestination | [HomePathInfo](#homepathinfo20) | Yes | Home page **NavDestination** information. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/pi4UuUkKT6W-Yx2mpkx9lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70E51CE50416C767833B5095E3B312AFB0BF5FC8DD6CD485794F58547EF6D74E)

When using a home page **NavDestination**, the **Navigation** component will behave with the following key changes:

-   Any content you define directly inside the **Navigation** component will not be created.
    
-   For the various attributes configured on the **Navigation** component: if the home page NavDestination has corresponding functional attributes, the attributes set on the **Navigation** component will be overridden and fail to take effect.
    

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]title

title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle, options?: NavigationTitleOptions)

Sets the page title.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Hrfc1ybSRuu6Iok5C0v9Sw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFBD865CF097E8487EF254AC466A1FADB8B89B73A67711D37937AEAF2A1F4A3D)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)10+ | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | [NavigationCommonTitle](#navigationcommontitle9)9+ | [NavigationCustomTitle](#navigationcustomtitle9)9+ | Yes | 
Page title. When the NavigationCustomTitle type is used to set the height, [titleMode](#titlemode) does not take effect.

When the title string is too long:

\- If no subtitle is set, the string is scaled down, wrapped in two lines, and then clipped.

\- If a subtitle is set, the subtitle is scaled down and then clipped.

 |
| options11+ | [NavigationTitleOptions](#navigationtitleoptions11) | No | Defines the title bar options. Title bar options include the background color, background blur style, blur options, background properties, layout style, and padding at the start and end of the title bar, as well as main title attribute modifier, subtitle attribute modifier, and whether to respond when the device is in semi-folded mode. |

#### \[h2\]menus

menus(value: Array<NavigationMenuItem> | CustomBuilder)

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. When the value type is Array<[NavigationMenuItem](#navigationmenuitem)\>, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/JrFC8eh7Sv2RTgj6KQFwXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CE97D6C5E473E8EB1D724F0491773812F115EC514463470D1803FB05FB23F2F)

The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[NavigationMenuItem](#navigationmenuitem)\> | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Menu items in the upper right corner of the page. |

#### \[h2\]menus19+

menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. Compared with [menus](#menus), this API adds menu options. When the value type is Array<[NavigationMenuItem](#navigationmenuitem)\>, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ADiglKFUQ9yxEFFdaP_LAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14219C1E0A1AF5420B3832375B4CF479BF18EBED19687FEC304CF403D49C43A3)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | Array<[NavigationMenuItem](#navigationmenuitem)\> | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Menu items in the upper right corner of the page. |
| options | [NavigationMenuOptions](#navigationmenuoptions19) | No | Configuration options for menu items in the upper right corner of the page. |

#### \[h2\]titleMode

titleMode(value: NavigationTitleMode)

Sets the display mode of the page title bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NavigationTitleMode](#navigationtitlemode) | Yes | 
Display mode of the page title bar.

Default value: **NavigationTitleMode.Free**

 |

#### \[h2\]toolbarConfiguration10+

toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

Sets the content of the toolbar. If this attribute is not set, no toolbar is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/8A007jMNQ3aJ5BAbhDt4fA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0BC4A05693651838EF1B72434E43E11E217FC26C256AD1EA30E131A3FE2BCB2)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[ToolbarItem](#toolbaritem10)\> | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | 
Content of the toolbar. When configured with Array<[ToolbarItem](#toolbaritem10)\>, the toolbar follows the rules below:

Toolbar items are evenly distributed on the bottom toolbar, with text and icons evenly spaced in each content area.

In portrait mode, the toolbar shows a maximum of five icons, with any additional icons placed into an automatically generated **More** icon. In landscape mode, toolbar behavior depends on the display mode:

\- If the display mode is [Split](#navigationmode9), the toolbar maintains the portrait mode.

\- If the display mode is [Stack](#navigationmode9), the toolbar must be used together with Array<[NavigationMenuItem](#navigationmenuitem)\> of the **menus** attribute; in this configuration, the bottom toolbar is automatically hidden, and all items on the toolbar are relocated to the menu in the upper right corner of the screen.

When configured with [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8), the toolbar does not follow the above rules.

 |
| options11+ | [NavigationToolbarOptions](#navigationtoolbaroptions11) | No | Toolbar options. Toolbar options include the background color, background blur style and blur option, background properties, and layout mode of the toolbar, as well as whether to hide the toolbar text, and options for the toolbar's more button menu. |

#### \[h2\]hideToolBar

hideToolBar(value: boolean)

Specifies whether to hide the toolbar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to hide the toolbar.

**true**: Hide the toolbar.

**false**: Display the toolbar.

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]hideToolBar13+

hideToolBar(hide: boolean, animated: boolean)

Specifies whether to hide the toolbar. Compared with [hideToolBar](#hidetoolbar), this API adds the capability to control whether to animate the visibility change of the toolbar.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hide | boolean | Yes | 
Whether to hide the toolbar.

**true**: Hide the toolbar.

**false**: Display the toolbar.

If the input parameter is invalid, the value **false** is used.

 |
| animated | boolean | Yes | 

Whether to animate the visibility change.

**true**: yes

**false**: no

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]hideTitleBar

hideTitleBar(value: boolean)

Specifies whether to hide the title bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to hide the title bar.

**true**: yes

**false**: no

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]hideTitleBar13+

hideTitleBar(hide: boolean, animated: boolean)

Specifies whether to hide the title bar. Compared with [hideTitleBar](#hidetitlebar), this API adds the capability to control whether to animate the visibility change of the title bar.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hide | boolean | Yes | 
Whether to hide the title bar.

**true**: yes

**false**: no

If the input parameter is invalid, the value **false** is used.

 |
| animated | boolean | Yes | 

Whether to animate the visibility change.

**true**: yes

**false**: no

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]hideBackButton

hideBackButton(value: boolean)

Sets whether to hide the back button in the title bar. The back button takes effect only when [titleMode](#titlemode) is set to **NavigationTitleMode.Mini**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to hide the back button in the title bar.

**true**: Hide the back button in the title bar.

**false**: Show the back button in the title bar.

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]navBarWidth9+

navBarWidth(value: Length)

Set the width of the navigation page. It takes effect only when [mode](#mode9) is set to **NavigationMode.Auto** or **NavigationMode.Split**.

Since API version 18, this attribute supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Width of the navigation page.

Default value: **240**

Unit: vp

**undefined**: No action is taken, and the navigation page width remains consistent with the default value.

 |

#### \[h2\]navBarPosition9+

navBarPosition(value: NavBarPosition)

Sets the position of the navigation page. It takes effect only when [mode](#mode9) is set to **NavigationMode.Auto** or **NavigationMode.Split**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NavBarPosition](#navbarposition9) | Yes | 
Position of the navigation page.

Default value: **NavBarPosition.Start**

 |

#### \[h2\]mode9+

mode(value: NavigationMode)

Sets the display mode of the navigation page.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NavigationMode](#navigationmode9) | Yes | 
Display mode of the navigation page.

Default value: **NavigationMode.Auto**

At the default settings, the component adapts to a single column or two columns based on the component width.

 |

#### \[h2\]backButtonIcon9+

backButtonIcon(value: string | PixelMap | Resource | SymbolGlyphModifier)

Sets the icon of the back button in the title bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/N21KGkaiQ8eWiFe6OlSrcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D1D9BA2927E9015FF4C8C9F8BCEE995C99A03AC4578B8EA9886261F66E847E2)

The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../common-definitions/basic-types/document.md#resource) | [SymbolGlyphModifier12+](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | Yes | Icon of the back button in the title bar. |

#### \[h2\]backButtonIcon19+

backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier, accessibilityText?: ResourceStr)

Sets the icon and accessibility text for the back button on the title bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/eq80K9IASFmZ1-CiCjJpyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0902E724A64F779829EAB94B163013A9338796A5C62EE3A638C04280C9939DCD)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| icon | string | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../common-definitions/basic-types/document.md#resource) | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | Yes | Icon of the back button in the title bar. |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | 
Accessibility text for the back button.

Default value: **back** when the system language is English.

 |

#### \[h2\]hideNavBar9+

hideNavBar(value: boolean)

Sets whether to hide the navigation page. If the value is set to **true**, the navigation bar, including the title bar, content area, and toolbar, will be hidden. In this case, if the navigation destination page is in the routing stack, it is moved to the top of the stack and displayed. Otherwise, a blank page is displayed.

From API version 9 to API version 10, this attribute takes effect only in split-column mode. Since API version 11, this attribute takes effect in all display modes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to hide the navigation page.

**true**: yes

**false**: no

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]navDestination10+

navDestination(builder: (name: string, param: unknown) => void)

Creates a **NavDestination** component. The builder receives the **name** and **param** parameters for constructing the **NavDestination** component. The builder must return a single root node. The builder can have only one root node. In the builder, a layer of custom components can wrap the **NavDestination** component. However, no attributes or events can be set for these custom components. Otherwise, only blank content is displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | (name: string, param: unknown) => void | Yes | Builder for a **NavDestination** component. **name**: name of the **NavDestination** page. **param**: detailed parameters for the custom **NavDestination** page. The **unknown** type can be replaced with a user-defined type. |

#### \[h2\]navBarWidthRange10+

navBarWidthRange(value: \[Dimension, Dimension\])

Sets the minimum and maximum widths of the navigation page (effective in split-column mode). When this API is not used, the minimum width defaults to 240 vp, and the maximum width defaults to 40% of the component width (not exceeding 432 vp). When dragging the divider changes the navigation page width, the content area will be compressed.

Divider dragging range:

| Condition | Dragging Range |
| :-- | :-- |
| Both **navBarWidthRange** and **minContentWidth** are set. | Range set by **navBarWidthRange** if the value set by **minContentWidth** is satisfied |
| Neither **navBarWidthRange** nor **minContentWidth** is set. | Default minimum and maximum ranges of **navBarWidthRange** |
| Only the **navBarWidthRange** attribute is set. | Range set by **navBarWidthRange**, where the maximum dragging range cannot exceed the default value of **minContentWidth** |
| Only the **minContentWidth** attribute is set. | Default minimum and maximum ranges of **navBarWidthRange** |
| Only the **navBarWidth** attribute is set. | Dragging not supported |

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | \[[Dimension](../../common-definitions/basic-types/document.md#dimension10), [Dimension](../../common-definitions/basic-types/document.md#dimension10)\] | Yes | Minimum and maximum widths of the navigation page. If an invalid value is set, the default value is used. |

#### \[h2\]minContentWidth10+

minContentWidth(value: Dimension)

Minimum width of the navigation bar content area (effective in split-column mode).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | Yes | 
Minimum width of the content area on the navigation page.

Default value: **360**

Unit: vp

**undefined**: No action is taken, and the minimum width of the navigation page remains consistent with the default value.

Breakpoint calculation in Auto mode: default 600 vp = minNavBarWidth (240 vp) + minContentWidth (360 vp)

 |

#### \[h2\]ignoreLayoutSafeArea12+

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

Ignores the layout safe area by allowing the component to extend into the non-safe areas of the screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/d0RwY-DpSqO1SHKRfyQyMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F4D7739D7BF59F0EAF6BA3D624E29BED253F0B306FA69EBEFADD1AA61E796BE)

-   Prerequisites for the **ignoreLayoutSafeArea** attribute to take effect:
    
    When **LayoutSafeAreaType.SYSTEM** is set, the component can extend into the non-safe area if its boundaries overlap with it.
    
-   If the component extends into the non-safe area, events triggered within that area (such as click events) might be intercepted by the system. This allows the system to prioritize responses to system components such as the status bar.
    
-   To allow a component to extend into non-safe areas, the title bar and toolbar must be hidden or set to [STACK](#barstyle12) mode.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| types | Array <[LayoutSafeAreaType](../../universal-attributes/layout-and-borders/safe-area/document.md#layoutsafeareatype12)\> | No | 
Types of non-safe areas to extend into.

Default value:

\[LayoutSafeAreaType.SYSTEM\]

 |
| edges | Array <[LayoutSafeAreaEdge](../../universal-attributes/layout-and-borders/safe-area/document.md#layoutsafeareaedge12)\> | No | 

Edges for expanding the safe area.

Default value:

\[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM\]

 |

#### \[h2\]systemBarStyle12+

systemBarStyle(style: Optional<SystemBarStyle>)

Sets the style of the system status bar when the home page of the **Navigation** component is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/mC1Jl7MjTWmwRauFPzidaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78469AB1296B7E65B1EDA9FAC87473A25F410CE545C09782900F88C56BA7B08B)

1.  Avoid using the **systemBarStyle** attribute in conjunction with the status bar style APIs in the **Window** module, such as [setWindowSystemBarProperties](../../../arkts-api/window-manager/ohos-window-window/interface-window/document.md#setwindowsystembarproperties9).
2.  When you first set the **systemBarStyle** attribute for a **Navigation** or **NavDestination** component, the current status bar style is saved for potential future restoration.
3.  **Navigation** always uses the status bar style defined by the home page (when no **NavDestination** exists in the routing stack) or the top **NavDestination** in the stack.
4.  If the home page or any top **NavDestination** page has a valid **systemBarStyle** set, that style will be used. If no style is set, and there is a previously saved style available, the saved style will be used. If no style has been set or saved, no changes will be made.
5.  In [Split](#navigationmode9) mode, if there is no **NavDestination** in the content area, the settings of the **Navigation** home page will apply. Otherwise, the settings of the top **NavDestination** page on the routing stack will apply.
6.  The **systemBarStyle** attribute is effective only for the main page of the main window.
7.  The set style will only take effect if the **Navigation** component spans the entire page. If it does not, and there is a previously saved style available, the saved style will be used instead.
8.  When different styles are set for pages, the new style takes effect at the start of the page transition.
9.  The status bar style set by **Navigation** or **NavDestination** does not apply in non-fullscreen windows.

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[SystemBarStyle](../../../arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#systembarstyle12)\> | Yes | Style of the system status bar. |

#### \[h2\]recoverable14+

recoverable(recoverable: Optional<boolean>)

Sets whether the **Navigation** component is recoverable. If set to recoverable, when the application process exits unexpectedly and restarts, the **Navigation** component can be automatically re-created and its routing stack restored to the state at the time of the unexpected exit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/T2qR4bm2RuSkjpzx7rkF0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=392FB4445275DC480FB4309A8390F4152FC599C1BD0912D3FC799AD68592971C)

1.  For this API to work properly, you must first set the universal attribute [id](../../universal-attributes/basic-attributes/component-id/document.md#id) of the **Navigation** component.
2.  This API must be used together with the [recoverable](../navdestination/document.md#recoverable14) API of **NavDestination**.
3.  Non-serializable information, such as non-serializable parameters and custom **onPop**, is discarded and cannot be restored during the recovery process.
4.  If an application is terminated due to insufficient system resources after it is switched to the background, any page configured as recoverable will be automatically restored when the application is revived to the foreground. For details, see [UIAbility Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-recover-guideline). For the usage example, see [Example 18: Setting Navigation as Recoverable](#example-18-setting-navigation-as-recoverable).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recoverable | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether the **Navigation** component is recoverable. By default, it is not recoverable.

**true**: yes

**false**: no

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]enableDragBar14+

enableDragBar(isEnabled: Optional<boolean>)

Sets whether to display a drag bar in split-column scenarios. This attribute has no effect on PCs/2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable the drag bar. By default, there is no drag bar.

**true**: yes; **false**: no

If the input parameter is invalid, the value **false** is used.

 |

#### \[h2\]enableModeChangeAnimation15+

enableModeChangeAnimation(isEnabled: Optional<boolean>)

Sets whether to enable the animation for switching between single- and split-column modes.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable the animation for switching between single- and split-column modes.

**true**: yes; **false**: no

If the input parameter is invalid, the value **true** is used.

 |

#### \[h2\]enableToolBarAdaptation19+

enableToolBarAdaptation(enable: Optional<boolean>)

Sets whether to enable toolbar adaptation ([toolbarConfiguration](#toolbarconfiguration10)) for the **Navigation** and **NavDestination** components. If this feature is disabled, the bottom toolbar ([toolbarConfiguration](#toolbarconfiguration10)) will no longer be moved into the menu in the upper right corner of the page. This API does not apply to custom menus; using it requires defining the [menu](#menus) via the [NavigationMenuItem](#navigationmenuitem) API.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | Optional<boolean> | Yes | 
Whether to enable toolbar adaptation.

Default value: **true**

**true**: Enable toolbar adaptation.

**false**: Disable toolbar adaptation.

 |

#### \[h2\]splitPlaceholder20+

splitPlaceholder(placeholder: ComponentContent)

Sets a default placeholder page for the right column in the **Navigation** component's split-column mode. The placeholder page is for UI display only and cannot receive focus or respond to events.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| placeholder | [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1) | Yes | Default placeholder page for the right column in the **Navigation** component's split-column mode. |

#### \[h2\]enableVisibilityLifecycleWithContentCover21+

enableVisibilityLifecycleWithContentCover(isEnabled: Optional<boolean>)

Sets whether to enable the linkage between the [onShown](../navdestination/document.md#onshown10) and [onHidden](../navdestination/document.md#onhidden10) lifecycle callbacks of the [NavDestination](../navdestination/document.md) page and the full-modal triggering.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | Optional<boolean> | Yes | 
Whether to enable the linkage between the **onShown** and **onHidden** lifecycle callbacks of the NavDestination page and the full-modal triggering.

Default value: **true**

**true**: When a full-modal page is shown, the current **NavDestination** page triggers **onHidden**. When the full-modal pages is dismissed, the page triggers **onShown**.

**false**: The **onShown** and **onHidden** callbacks of the **NavDestination** page are not triggered by the showing or dismissing of a full-modal page.

 |

#### \[h2\]subTitle(deprecated)

subTitle(value: string)

Sets the page subtitle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/9eIDwJrZTcq_3ycAaP8CHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C284B0C71D45A1807AB701087E0C10C37D5A4DA406FEF3C39358D064B59FF431)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [title](#title) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Page subtitle. |

#### \[h2\]toolBar(deprecated)

toolBar(value: object | CustomBuilder)

Sets the content of the toolbar. If this attribute is not set, no toolbar is displayed. Toolbar items are evenly distributed on the bottom toolbar, with text and icons evenly spaced in each content area. If any item contains overlong text and there are fewer than five items, the toolbar will reduce the text size progressively, wrap the text over two lines if necessary, and then clip the text to fit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Rs9NIKO8TkWFz7GK3dZTOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3894FE6C13135BF354002F67F3A95DDD68D7094BED73DF60FC2580DD0FD16013)

This API is supported since API version 8 and deprecated since API version 10. You are advised to use [toolbarConfiguration](#toolbarconfiguration10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | object | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Content of the toolbar. |

**object**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text of the toolbar item. |
| icon | string | No | Icon path of the toolbar item. |
| action | () => void | No | Callback invoked when the toolbar item is selected. |

#### Events

#### \[h2\]onTitleModeChange

onTitleModeChange(callback: (titleMode: NavigationTitleMode) => void)

Triggered when [titleMode](#titlemode) is set to **NavigationTitleMode.Free** and the title bar mode changes as content scrolls.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| titleMode | [NavigationTitleMode](#navigationtitlemode) | Yes | Title mode. |

#### \[h2\]onNavBarStateChange9+

onNavBarStateChange(callback: (isVisible: boolean) => void)

Callback invoked when the navigation page visibility status changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isVisible | boolean | Yes | Whether the navigation bar is visible. The value **true** means that the navigation bar is visible, and **false** means the opposite. |

#### \[h2\]onNavigationModeChange11+

onNavigationModeChange(callback: (mode: NavigationMode) => void)

Triggered when the **Navigation** component is displayed for the first time or its display mode switches between single-column and split-column.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [NavigationMode](#navigationmode9) | Yes | 
**NavigationMode.Split**: The component is displayed in split-column mode.

**NavigationMode.Stack**: The component is displayed in single-column mode.

 |

#### \[h2\]customNavContentTransition11+

customNavContentTransition(delegate:(from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined)

Defines the callback of the custom transition animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/W20DaRxpSRajwBQBor6hlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4EC0420260D4998B9D78075FC7FB90A42D2B7EE8379D911DA150C53F6546CB3)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [NavContentInfo](#navcontentinfo11) | Yes | Destination page to exit. |
| to | [NavContentInfo](#navcontentinfo11) | Yes | Destination page to enter. |
| operation | [NavigationOperation](#navigationoperation11) | Yes | Transition type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NavigationAnimatedTransition](#navigationanimatedtransition11) | undefined | 
**NavigationAnimatedTransition**: protocol object for custom transition animations.

**undefined**: undefined, executing the default transition animation effect.

 |

#### NavPathStack10+

A navigation controller that manages all child pages in the **Navigation** component with a stack data structure and provides stack operation methods for controlling page transitions.

Starting from API version 12, **NavPathStack** is inheritable. Objects of a derived class can replace those of the base class. For details, see [Example 10](#example-10-defining-a-derived-class-of-navpathstack).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/XXOry4mWThm-mOyJ_KSXnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=591D18E6823D292014C533F8DEA5682AF874B88585DF71718317980568C8E044)

1.  When multiple navigation controller operations are triggered in succession, the intermediate states are bypassed, and only the final result of the operations is rendered.
    
    For example, if a Page1 is popped and then immediately pushed back, the system considers that the states before and after these operations are identical, leading to no actual change in the stack. To ensure that a new instance of Page1 is pushed onto the stack despite the consecutive operations, use the **NEW\_INSTANCE** mode.
    
2.  Avoid relying on lifecycle event listeners as a means to manage the navigation controller.
    
3.  When the application is in the background, calling stack operation APIs of **NavPathStack** will trigger a refresh upon the application's return to the foreground.
    

#### \[h2\]constructor

constructor()

Creates a **NavPathStack** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]pushPath10+

pushPath(info: NavPathInfo, animated?: boolean): void

Pushes the navigation destination page specified by **info** onto the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | Yes | Information about the navigation destination page. |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

If the input parameter is invalid, the value **true** is used.

 |

#### \[h2\]pushPath12+

pushPath(info: NavPathInfo, options?: NavigationOptions): void

Pushes the navigation destination page specified by **info** onto the routing stack. Depending on the [LaunchMode](#launchmode12) specified in the **options** parameter, different behaviors will be implemented.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | Yes | Information about the navigation destination page. |
| options | [NavigationOptions](#navigationoptions12) | No | Routing stack operation options. |

#### \[h2\]pushPathByName10+

pushPathByName(name: string, param: unknown, animated?: boolean): void

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| param | unknown | Yes | Detailed parameters for the custom **NavDestination** page. The **unknown** type can be replaced with a user-defined type. |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]pushPathByName11+

pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack. This API uses the **onPop** callback to receive the result returned when the page is popped out of the stack.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| param | Object | Yes | Detailed parameters for the custom **NavDestination** page. |
| onPop | Callback<[PopInfo](#popinfo11)\> | Yes | Callback used to receive the result. It is triggered only when the **result** parameter is set in [pop](#pop11), [popToName](#poptoname11), or [popToIndex](#poptoindex11). |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]pushDestination11+

pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>

Pushes the navigation destination page specified by **info** onto the routing stack. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/QxC-zm_1S_mVIjbaRsmlXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21086F1A1A96E9A5A50E0EB30AA74A0B7577889230EC2C9A86EED88CD2B365A6)

You are not advised to use stack operations in [aboutToAppear](../../custom-components/custom-component-lifecycle/document.md#abouttoappear), as the page has not yet finished building at this stage, which may lead to issues such as white screens or navigation failures.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | Yes | Information about the navigation destination page. |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

#### \[h2\]pushDestination12+

pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>

Pushes the navigation destination page specified by **info** onto the routing stack. This API uses a promise to return the result. Depending on the [LaunchMode](#launchmode12) specified in the **options** parameter, different behaviors will be implemented.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/tp4Kg0UBTyCCoyQGflm_CQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85643B660AB2A5A504010D36CFBB5CF88B17E44050EC568ABE8E927C03C87EFD)

You are not advised to use stack operations in [aboutToAppear](../../custom-components/custom-component-lifecycle/document.md#abouttoappear), as the page has not yet finished building at this stage, which may lead to issues such as white screens or navigation failures.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | Yes | Information about the navigation destination page. |
| options | [NavigationOptions](#navigationoptions12) | No | Routing stack operation options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

#### \[h2\]pushDestinationByName11+

pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/6snruLM-SEGAmXuJyjFdTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7C7BFDF646554C3DE6F4E3ABEB8745370BA3875F9BFF6A37E47F27D53A97559)

You are not advised to use stack operations in [aboutToAppear](../../custom-components/custom-component-lifecycle/document.md#abouttoappear), as the page has not yet finished building at this stage, which may lead to issues such as white screens or navigation failures.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| param | Object | Yes | Detailed parameters for the custom **NavDestination** page. |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

#### \[h2\]pushDestinationByName11+

pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack. This API uses the **onPop** callback to handle the result returned when the page is popped out of the stack. It uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/HvS4kws_SR6IHYkk_rLdNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=128F14C2C9F2E583F8AF04EA09BB06C566500E8F37F164E87286D0C0C727D2C7)

You are not advised to use stack operations in [aboutToAppear](../../custom-components/custom-component-lifecycle/document.md#abouttoappear), as the page has not yet finished building at this stage, which may lead to issues such as white screens or navigation failures.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| param | Object | Yes | Detailed parameters for the custom **NavDestination** page. |
| onPop | Callback<[PopInfo](#popinfo11)\> | Yes | Callback used to handle the result returned when the page is popped out of the stack. It is triggered only when the **result** parameter is set in [pop](#pop11), [popToName](#poptoname11), or [popToIndex](#poptoindex11). |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

#### \[h2\]replacePath11+

replacePath(info: NavPathInfo, animated?: boolean): void

Replaces the top of the routing stack with the navigation destination page specified by **info**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | Yes | Parameters for the new top page of the routing stack. |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]replacePath12+

replacePath(info: NavPathInfo, options?: NavigationOptions): void

Replaces the top page on the routing stack. Depending on the [LaunchMode](#launchmode12) specified in the **options** parameter, different behaviors will be implemented.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | Yes | Parameters for the new top page of the routing stack. |
| options | [NavigationOptions](#navigationoptions12) | No | Routing stack operation options. |

#### \[h2\]replacePathByName11+

replacePathByName(name: string, param: Object, animated?: boolean): void

Replaces the top of the routing stack with the page specified by **name**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| param | Object | Yes | Detailed parameters for the custom **NavDestination** page. |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]replaceDestination18+

replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>

Performs a replacement operation on the routing stack. This API uses a promise to return the result. Its behavior varies depending on the value of [LaunchMode](#launchmode12) specified in **options**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | Yes | Information about the navigation destination page. |
| options | [NavigationOptions](#navigationoptions12) | No | Routing stack operation options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |

#### \[h2\]removeByIndexes11+

removeByIndexes(indexes: Array<number>): number

Removes the navigation destination pages specified by **indexes** from the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| indexes | Array<number> | Yes | Array of indexes of the navigation destination pages to remove. The index is zero-based. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of the navigation destination pages removed. |

#### \[h2\]removeByName11+

removeByName(name: string): number

Removes the navigation destination page specified by **name** from the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of the navigation destination pages removed. |

#### \[h2\]removeByNavDestinationId12+

removeByNavDestinationId(navDestinationId: string): boolean

Removes the navigation destination page specified by **navDestinationId** from the routing stack. **navDestinationId** can be obtained from the [onReady](../navdestination/document.md#onready11) callback of **NavDestination** or from [NavDestinationInfo](../../../arkts-api/ui/ohos-arkui-observer-observer/document.md#navdestinationinfo).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| navDestinationId | string | Yes | Unique ID of the navigation destination page to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the page is removed successfully.

**true**: Removal succeeded.

**false**: Removal failed.

 |

#### \[h2\]pop10+

pop(animated?: boolean): NavPathInfo | undefined

Pops the top element out of the routing stack.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/iJ1pTltHQXi-xYX2mU_ZXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEEEB04623D0C2E988AC56E0BE0D00BAD24F06F2A83E2B4077545F9B11355272)

When multiple navigation controller methods are called consecutively, any pages popped during the sequence are cached. If a page with the same name is later pushed, the system reuses the cached instance instead of instantiating a new page.

Example:

pathStack: NavPathStack = new NavPathStack()

//The initial page stack is \[A\].

pathStack.pop()

pathStack.pushPath(A)

pathStack.pushPath(B)

// The page stack after the operation is \[A B\].

In this case, page A is reused, and the new creation process is not performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NavPathInfo](#navpathinfo10) | undefined | 
**NavPathInfo**: information about the navigation destination page at the top of the stack.

**undefined**: the routing stack is empty.

 |

#### \[h2\]pop11+

pop(result: Object, animated?: boolean): NavPathInfo | undefined

Pops the top element out of the routing stack and invokes the **onPop** callback to pass the page processing result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/gOQS8PKEQYSI36imAggIyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=676D2BCBCE978DA4F8BDE0DE08313038FEABF220BCFD59823D9CFD64B1985375)

When multiple navigation controller methods are called consecutively, any pages popped during the sequence are cached. If a page with the same name is later pushed, the system reuses the cached instance instead of instantiating a new page.

Example:

pathStack: NavPathStack = new NavPathStack()

//The initial page stack is \[A\].

pathStack.pop()

pathStack.pushPath(A)

pathStack.pushPath(B)

// The page stack after the operation is \[A B\].

In this case, page A is reused, and the new creation process is not performed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | Object | Yes | Custom processing result on the page. The boolean type is not supported. |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NavPathInfo](#navpathinfo10) | undefined | 
**NavPathInfo**: information about the navigation destination page at the top of the stack.

**undefined**: the routing stack is empty.

 |

#### \[h2\]popToName10+

popToName(name: string, animated?: boolean): number

Pops pages until the first navigation destination page that matches **name** from the bottom of the routing stack is at the top of the stack.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns the index of the first navigation destination page that matches **name** from the bottom of the routing stack; returns **\-1** if such a page does not exist. |

#### \[h2\]popToName11+

popToName(name: string, result: Object, animated?: boolean): number

Pops pages until the first navigation destination page that matches **name** from the bottom of the routing stack is at the top of the stack. This API uses the **onPop** callback to pass in the page processing result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| result | Object | Yes | Custom processing result on the page. The boolean type is not supported. |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns the index of the first navigation destination page that matches **name** from the bottom of the routing stack; returns **\-1** if such a page does not exist. |

#### \[h2\]popToIndex10+

popToIndex(index: number, animated?: boolean): void

Returns the routing stack to the page specified by **index**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the navigation destination page. The index is zero-based. |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]popToIndex11+

popToIndex(index: number, result: Object, animated?: boolean): void

Returns the routing stack to the page specified by **index** and invokes the **onPop** callback to pass the page processing result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the navigation destination page. The index is zero-based. |
| result | Object | Yes | Custom processing result on the page. The boolean type is not supported. |
| animated | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]moveToTop10+

moveToTop(name: string, animated?: boolean): number

Moves the first navigation destination page that matches **name** from the bottom of the routing stack to the top of the stack.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns the index of the first navigation destination page that matches **name** from the bottom of the routing stack; returns **\-1** if such a page does not exist. |

#### \[h2\]moveIndexToTop10+

moveIndexToTop(index: number, animated?: boolean): void

Moves to the top of the routing stack the navigation destination page specified by **index**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the navigation destination page. The index is zero-based. |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]clear10+

clear(animated?: boolean): void

Clears the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| animated11+ | boolean | No | 
Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### \[h2\]getAllPathName10+

getAllPathName(): Array<string>

Obtains the names of all navigation destination pages in the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Names of all navigation destination pages in the routing stack. |

#### \[h2\]getParamByIndex10+

getParamByIndex(index: number): unknown | undefined

Obtains the parameter information of the navigation destination page specified by **index**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the navigation destination page. The index is zero-based. |

**Return value**

| Type | Description |
| :-- | :-- |
| unknown | undefined | 
**unknown**: parameter information of the corresponding navigation destination page. **unknown** can represent a user-defined type.

**undefined**: an invalid index is provided.

 |

#### \[h2\]getParamByName10+

getParamByName(name: string): Array<unknown>

Obtains the parameter information of all **NavDestination** pages with the specified name, and sorts the information in ascending order by page index.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<unknown> | Parameter information of all **NavDestination** pages with the specified name. **unknown** can represent a user-defined type. |

#### \[h2\]getIndexByName10+

getIndexByName(name: string): Array<number>

Obtains the indexes of all the navigation destination pages that match **name**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the navigation destination page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Indexes of all the matching navigation destination pages. If no pages with the specified name exist in the routing stack, an empty array is returned. The index range is \[0, routing stack size - 1\]. |

#### \[h2\]size10+

size(): number

Obtains the stack size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Stack size.

Value range: \[0, +∞)

 |

#### \[h2\]disableAnimation11+

disableAnimation(value: boolean): void

Disables or enables the transition animation in the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to disable the transition animation.

Default value: **false**

**true**: Disable the transition animation.

**false**: Enable the transition animation.

 |

#### \[h2\]getParent11+

getParent(): NavPathStack | null

Obtains the parent navigation path stack.

When a **Navigation** component is nested (directly or indirectly) inside another **Navigation** component, the **NavPathStack** of the inner component can obtain the **NavPathStack** of the outer component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [NavPathStack](#navpathstack10) | null | Navigation path stack of the outer **Navigation** component in which the current **Navigation** component is nested. If **NavPathStack** cannot be obtained, **null** is returned. |

#### \[h2\]setInterception12+

setInterception(interception: NavigationInterception): void

Sets the interception callback for navigation page redirection.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interception | [NavigationInterception](#navigationinterception12) | Yes | Object to be intercepted during navigation redirection. |

#### \[h2\]getPathStack19+

getPathStack(): Array<NavPathInfo>

Obtains the array of route page information from this routing stack.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[NavPathInfo](#navpathinfo10)\> | Array of route page information in the current routing stack. |

#### \[h2\]setPathStack19+

setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void

Updates the array of route page information in this routing stack to the specified content and performs route transitions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/27Go22pWSZa1dztueckiPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0B5B296E4447720BEB9BC5C0BDDE2A4219F00E0D16C53C376829A5FF6EDB193)

1.  You can add or remove pages in batches based on the existing stack. Among the pages added in batches, only the visible pages will trigger creation; other pages, although added to the stack, will not be created immediately. They will only be created when they become visible.
2.  For routing stacks updated through the batch push functionality, the lifecycle events of each page are triggered from the top to the bottom of the stack. This differs from the triggering order of other push APIs, which are triggered from the bottom to the top of the stack.
3.  You can operate existing pages using **navDestinationId** (unique ID) in [NavPathInfo](#navpathinfo10). This ID is system-generated and globally unique (it can be obtained using the [getPathStack](#getpathstack19) API and should not be manually reassigned). If the specified ID does not exist in the current routing stack, it indicates a new page. If it exists and the corresponding name is the same, it indicates reuse of an existing page.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pathStack | Array<[NavPathInfo](#navpathinfo10)\> | Yes | 
Array of route page information in the current routing stack.

**NOTE**

The array length is not limited.

 |
| animated | boolean | No | 

Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### NavPathInfo10+

Provides the navigation page information.

#### \[h2\]constructor

constructor(name: string, param: unknown, onPop?: Callback<PopInfo>, isEntry?: boolean)

Creates a **NavPathInfo** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | 
Name of the navigation destination page. The name matches the name in the following route tables:

1\. Custom route table, which is passed via the [navDestination](#navdestination10) method.

2\. System route table, which is set by **name** in **routerMap**. For details, please refer to [Example 2: Using NavPathStack APIs](#example-2-using-navpathstack-apis).

 |
| param | unknown | Yes | Detailed parameters for the custom **NavDestination** page. The **unknown** type can be replaced with a user-defined type. |
| onPop11+ | Callback<[PopInfo](#popinfo11)\> | No | Callback returned when [pop](#pop11), [popToName](#poptoname11), or [popToIndex](#poptoindex11) is called on the navigation destination page. It is triggered only when the **result** parameter is set in [pop](#pop11), [popToName](#poptoname11), or [popToIndex](#poptoindex11). |
| isEntry12+ | boolean | No | 

Whether the navigation destination page is the entry page.

**true**: yes; **false**: no

Default value: **false**

The value of this parameter is reviewed or reset under the following conditions:

1\. A global return event is triggered on the current navigation destination page.

2\. The application is switched to the background.

**NOTE**

The navigation destination page serving as an entry does not respond to the in-app global back events; instead, it directly triggers the global back event between applications.

 |

#### \[h2\]Properties

Provides parameters of **NavPathInfo**.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | 
Name of the navigation destination page. The name matches the name in the following route tables:

1\. Custom route table, which is passed via the [navDestination](#navdestination10) method.

2\. System route table, which is set by **name** in **routerMap**. For details, please refer to [Example 2: Using NavPathStack APIs](#example-2-using-navpathstack-apis).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| param | unknown | No | Yes | 

Detailed parameters for the custom **NavDestination** page. The **unknown** type can be replaced with a user-defined type.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onPop11+ | Callback<[PopInfo](#popinfo11)\> | No | Yes | 

Callback returned when [pop](#pop11), [popToName](#poptoname11), or [popToIndex](#poptoindex11) is called on the navigation destination page. It is triggered only when the **result** parameter is set in [pop](#pop11), [popToName](#poptoname11), or [popToIndex](#poptoindex11).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isEntry12+ | boolean | No | Yes | 

Whether the navigation destination page is the entry page.

**true**: yes; **false**: no

Default value: **false**

The value of this parameter is reviewed or reset under the following conditions:

1\. A global back event is triggered on the current navigation destination page.

2\. The application is switched to the background.

**NOTE**

The navigation destination page serving as an entry does not respond to the in-app global back events; instead, it directly triggers the global back event between applications.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| navDestinationId19+ | string | No | Yes | 

Unique ID of the navigation destination page. This ID is system-generated and globally unique. It can be obtained using the [getPathStack](#getpathstack19) API and should not be manually reassigned.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### PopInfo11+

Provides the callback information returned when a page is popped out of the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| info | [NavPathInfo](#navpathinfo10) | No | No | Information about the current page when a back action is performed. The value is automatically obtained by the system. |
| result | Object | No | No | Result returned when a back action is performed. You must customize the object. |

#### NavContentInfo11+

Provides the destination information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | Yes | Name of the navigation destination. If the view is a root view (**NavBar**), the return value is **undefined**. |
| index | number | No | No | 
Index of the navigation destination in the routing stack. If the view is a root view (**NavBar**), the return value is **\-1**.

Value range: \[-1, +∞)

 |
| mode | [NavDestinationMode](../navdestination/document.md#navdestinationmode11) | No | Yes | Mode of the navigation destination. If the view is a root view (**NavBar**), the return value is **undefined**. |
| param12+ | Object | No | Yes | Parameters loaded on the navigation destination page. |
| navDestinationId12+ | string | No | Yes | Unique identifier of the navigation destination page. |

#### NavigationAnimatedTransition11+

Defines the custom transition animation protocol. You need to implement this protocol to define the redirection animation of the navigation route.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timeout | number | No | Yes | 
Animation timeout time.

Unit: ms

Value range: \[0, +∞)

Default value: no default value for interactive animations; 1000 ms for non-interactive animations.

 |
| transition | (transitionProxy:[NavigationTransitionProxy](#navigationtransitionproxy-11)) => void | No | No | 

Callback for executing the custom transition animation.

**transitionProxy**: proxy for the custom transition animation.

 |
| onTransitionEnd | (success:boolean) => void | No | Yes | 

Callback invoked when the transition is complete.

**success**: whether the transition is successful.

 |
| isInteractive12+ | boolean | No | Yes | 

Whether the transition animation is interactive.

**true**: yes; **false**: no

Default value: **false**

 |

#### NavigationTransitionProxy 11+

Implements a custom transition animation proxy.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

Provides parameters of **NavigationTransitionProxy**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| from | [NavContentInfo](#navcontentinfo11) | No | No | Information about the exit page. |
| to | [NavContentInfo](#navcontentinfo11) | No | No | Information about the enter page. |
| isInteractive12+ | boolean | No | Yes | 
Whether the transition animation is interactive.

Default value: **false**

**true**: The transition animation is interactive.

**false**: The transition animation is not interactive.

 |

#### \[h2\]finishTransition

finishTransition(): void;

Finishes this custom transition animation. This API must be manually called to end the animation. Otherwise, the system ends the animation when the timeout expires.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]cancelTransition12+

cancelTransition?(): void;

Cancels this interactive transition animation, restoring the routing stack to its state before page redirection. (Non-interactive transition animations cannot be canceled.)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]updateTransition12+

updateTransition?(progress: number): void;

Updates the progress of this interactive transition animation. (Non-interactive animations do not support setting the animation progress).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/dTW0an1TQj-FiASShv3knA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3585733D32ABDA5BE011DED24AEA2977B6029E3619179BEC87AE552141E60FD6)

You are not advised to use stack operations in [aboutToAppear](../../custom-components/custom-component-lifecycle/document.md#abouttoappear), as the page has not yet finished building at this stage, which may lead to issues such as white screens or navigation failures.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | number | Yes | Progress percentage of the interactive transition animation. Value range: \[0, 1\]. |

#### NavigationInterception12+

Describes the object to be intercepted during navigation redirection.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| willShow | [InterceptionShowCallback](#interceptionshowcallback12) | No | Yes | 
Callback invoked before a page transition, allowing for stack operations, which take effect immediately for the current transition. The intercepted page will be created.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| didShow | [InterceptionShowCallback](#interceptionshowcallback12) | No | Yes | 

Callback after page redirection. The setting takes effect in the next redirection.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| modeChange | [InterceptionModeCallback](#interceptionmodecallback12) | No | Yes | 

Callback invoked when the display mode of the **Navigation** component switches between single-column and split-column.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| interception22+ | [InterceptionCallback](#interceptioncallback22) | No | Yes | 

Callback invoked before a page transition, allowing for stack operations, which take effect immediately for the current transition. The intercepted page will not be created.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### \[h2\]InterceptionShowCallback12+

type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void

Represents the interception callback invoked before and after page redirection.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [NavDestinationContext](../navdestination/document.md#navdestinationcontext11) | [NavBar](#navbar12) | Yes | Information about the top page in the routing stack before page redirection. The value **navBar** indicates that the top page is the home page. |
| to | [NavDestinationContext](../navdestination/document.md#navdestinationcontext11) | [NavBar](#navbar12) | Yes | Information about the top page in the routing stack after page redirection. The value **navBar** indicates that the top page is the home page. |
| operation | [NavigationOperation](#navigationoperation11) | Yes | Current page redirection type. |
| isAnimated | boolean | Yes | 
Whether to enable the transition animation.

**true**: Enable the transition animation.

**false**: Disable the transition animation.

 |

#### \[h2\]InterceptionModeCallback12+

type InterceptionModeCallback = (mode: NavigationMode) => void

Implements an interception callback invoked when the display mode of the **Navigation** component switches between single-column and split-column.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [NavigationMode](#navigationmode9) | Yes | Display mode of the navigation page. |

#### \[h2\]InterceptionCallback22+

type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void

Defines the callback triggered before a navigation page is redirected.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [NavPathInfo](#navpathinfo10) |[NavBar](#navbar12) | Yes | Information about the exit page. The value **navBar** indicates that the top page is the home page. |
| to | [NavPathInfo](#navpathinfo10) |[NavBar](#navbar12) | Yes | Information about the enter page. The value **navBar** indicates that the top page is the home page. |
| pathStack | [NavPathStack](#navpathstack10) | Yes | Page stack. |
| operation | [NavigationOperation](#navigationoperation11) | Yes | Current page redirection type. |
| isAnimated | boolean | Yes | 
Whether to enable the transition animation.

**true**: Enable the transition animation.

**false**: Disable the transition animation.

 |

#### NavBar12+

type NavBar = 'navBar'

Defines the name of the navigation home page.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| 'navBar' | Navigation home page. |

#### NavigationMenuItem

Defines the navigation menu item, including the menu icon and menu information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | string | [Resource14+](../../common-definitions/basic-types/document.md#resource) | No | No | 
Text of the menu item. Its visibility varies by the API version.

API version 9: visible.

Since API version 10: invisible.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | string | [Resource14+](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Icon path of the menu item.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isEnabled12+ | boolean | No | Yes | 

Enabled status. **true** (default): enabled. **false**: disabled.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| action | () => void | No | Yes | 

Callback invoked when the menu item is selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolIcon12+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon for a single option on the menu bar. It has higher priority than **icon**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ToolbarItem10+

Provides customizable parameters of the toolbar.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | ResourceStr | No | No | 
Text of the toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | ResourceStr | No | Yes | 

Icon path of the toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action | () => void | No | Yes | 

Callback invoked when the menu item is selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| status | [ToolbarItemStatus](#toolbaritemstatus10) | No | Yes | 

Status of a toolbar item.

Default value: **ToolbarItemStatus.NORMAL**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| activeIcon | ResourceStr | No | Yes | 

Icon path of the toolbar item in the active state.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolIcon12+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon for a single option on the toolbar. It has higher priority than **icon**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| activeSymbolIcon12+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon for a single option on the menu bar when it is in active state. It has higher priority than **activeIcon**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ToolbarItemStatus10+

Enumerates the toolbar item states.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Normal state. In this state, the toolbar item takes on the default style and can switch to another state-specific style by responding to the hover, press, and focus events. |
| DISABLED | 1 | Disabled state. In this state, the toolbar item is disabled and does not allow for user interactions. |
| ACTIVE | 2 | Active state. In this state, the toolbar item can update its icon to the one specified by **activeIcon** by responding to a click event. |

#### NavigationTitleMode

Enumerates the display modes of the title bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Free | 0 | 
When the content is more than one screen in a scrollable component, the main title shrinks as the content scrolls down (the subtitle fades out with its size remaining unchanged) and restores as the content scrolls up to the top.

**NOTE**

The effect where the main title's size changes in response to content scrolling is effective only when **title** is set to **ResourceStr** or **NavigationCommonTitle**. If **title** is set to any other value type, the main title changes in mere location when pulled down.

For this effect to work when the content is less than one screen in a scrollable component, set the **options** parameter of the scrollable component's [edgeEffect](../../scroll-and-swipe/list/document.md#edgeeffect) attribute to **true**. In the non-scrolling state, the height of the title bar is the same as in **Full** mode; in the scrolling state, the minimum height of the title bar is the same as in **Mini** mode.

 |
| Full | 1 | 

The title is fixed at full mode.

Default value: If there is only a main title, the title bar height is 112 vp; if there is both a main title and a subtitle, the title bar height is 138 vp.

 |
| Mini | 2 | 

The title is fixed at mini mode.

Default value:

In versions earlier than API version 12, if there is only a main title, the title bar height is 56 vp; if there is both a main title and a subtitle, the title bar height is 82 vp.

Since API version 12, the title bar height is 56 vp.

 |

#### NavigationCommonTitle9+

Defines a general title for the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| main | string | [Resource14+](../../common-definitions/basic-types/document.md#resource) | No | No | Main title. |
| sub | string | [Resource14+](../../common-definitions/basic-types/document.md#resource) | No | No | Subtitle. |

#### NavigationCustomTitle9+

Defines a custom title for the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| builder | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | No | Content of the title bar. |
| height | [TitleHeight](../../common-definitions/enums/document.md#titleheight9) | [Length](../../common-definitions/basic-types/document.md#length) | No | No | Height of the title bar. |

#### NavBarPosition9+

Position of the navigation page.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Start | When two columns are displayed, the main column is at the start of the main axis. |
| End | When two columns are displayed, the main column is at the end of the main axis. |

#### NavigationMode9+

Display mode of the navigation page. When **Navigation** is displayed in split-column mode, a divider is displayed between the navigation page and the content area.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Stack | 0 | The navigation page and content area are displayed independently of each other, which are equivalent to two pages. |
| Split | 1 | 
The navigation page and content area are displayed in different columns.

**1.** Table 1 describes the relationship between the actual resulting **navBarWidth** and the value set by you.

**2.** When the component size is decreased, the content area is shrunk until its width reaches the value defined by **minContentWidth**, and then the navigation page is shrunk until its width reaches the value defined by **minNavBarWidth**. If the component size is further decreased, the content area is further shrunk until it disappears, and then the navigation page is shrunk.

**3.** When the navigation page is set to a fixed size and the component size is continuously decreased, the navigation page is shrunk.

**4.** If only **navBarWidth** is set, the width of the navigation page is fixed at the value of **navBarWidth**, and the divider cannot be dragged.

**5.** The touch target of the divider is 2 vp on each side (left and right). Therefore, it is recommended that you keep a minimum distance of 4 vp from this area to avoid unintended interactions.

**6.** In Split mode, if there is only one page in the content area, the back button will not be displayed in the upper left corner of the page.

 |
| Auto | 2 | 

In API version 9 and earlier versions: If the window width is greater than or equal to 520 vp, the Split mode is used; otherwise, the Stack mode is used.

In API version 10 and later versions: If the window width is greater than or equal to 600 vp, the Split mode is used; otherwise, the Stack mode is used. 600 vp = minNavBarWidth (240 vp) + minContentWidth (360 vp).

 |

**Table 1** Relationship between actual navBarWidth and the developer-defined value

| Developer-defined navBarWidth | calcNavBarWidth Value | Actual navBarWidth |
| :-- | :-- | :-- |
| navBarWidth < minNavBarWidth | NA | minNavBarWidth |
| navBarWidth > maxNavBarWidth | calcNavBarWidth > maxNavBarWidth | maxNavBarWidth |
| navBarWidth > maxNavBarWidth | calcNavBarWidth < minNavBarWidth | minNavBarWidth |
| navBarWidth > maxNavBarWidth | minNavBarWidth ≤ calcNavBarWidth ≤ maxNavBarWidth | calcNavBarWidth |
| minNavBarWidth ≤ navBarWidth ≤ maxNavBarWidth | calcNavBarWidth ≤ minNavBarWidth | minNavBarWidth |
| minNavBarWidth ≤ navBarWidth ≤ maxNavBarWidth | minNavBarWidth < calcNavBarWidth <= navBarWidth | calcNavBarWidth |
| minNavBarWidth ≤ navBarWidth ≤ maxNavBarWidth | calcNavBarWidth > navBarWidth | navBarWidth |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/VO4-2I6MS-2uhMo7afs5Yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=529FF6B5708C16A555C7F815BD1E018B3ADD6916A56897E80CA4E9B3E79023F3)

For simplicity, **calcNavBarWidth** is defined as follows: Component width – minContentWidth – Divider width (1 px)

#### NavigationOperation11+

Enumerates the page redirection types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| PUSH | 1 | The transition is enter transition. |
| POP | 2 | The transition is exit transition. |
| REPLACE | 3 | The transition is page replacement. |

#### BarStyle12+

Enumerates the layout styles of the title bar and toolbar. Note that this API is not supported for the toolbar in **NavDestination**.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| STANDARD | 0 | 
In this mode, the title bar or toolbar is laid out above the content area.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STACK | 1 | 

In this mode, the title bar or toolbar is overlaid on top of the content area.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SAFE\_AREA\_PADDING14+ | 2 | 

In this mode, the title bar or toolbar is configured to respect the [component-level safe area](../../universal-attributes/layout-and-borders/sizing/document.md#safeareapadding14).

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### NavigationTitleOptions11+

Defines the title bar options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Background color of the title bar. If this parameter is not set, the default color is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the title bar. If this parameter is not set, the background blur effect is disabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 

Options for the title bar background blur style.

**NOTE**

This parameter is only effective when **backgroundBlurStyle** is set.

Avoid using this API in conjunction with **backgroundEffect**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Title bar background properties, including blur radius, brightness, saturation, and color.

**NOTE**

Avoid using this API in conjunction with **backgroundBlurStyleOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| barStyle12+ | [BarStyle](#barstyle12) | No | Yes | 

Layout style of the title bar.

Default value: **BarStyle.STANDARD**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| paddingStart12+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Padding at the start of the title bar.

Only supported in one of the following scenarios:

1\. Displaying the back icon, that is, [hideBackButton](#hidebackbutton) is **false**

2\. Using a non-custom title, that is, the [title value](#title) type is **ResourceStr** or **NavigationCommonTitle**

Default value:

LengthMetrics.resource(**$r('sys.float.margin\_left')**)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| paddingEnd12+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Padding at the end of the title bar.

Only supported in one of the following scenarios:

1\. Using a non-custom menu, that is, the [menu value](#menus) is Array<NavigationMenuItem>

2\. Using a non-custom menu without a menu in the upper right corner, that is, the [title value](#title) type is **ResourceStr** or **NavigationCommonTitle**

Default value:

LengthMetrics.resource($r('sys.float.margin\_right'))

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mainTitleModifier13+ | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | No | Yes | 

Main title attribute modifier.

1\. Attribute settings configured by this modifier will override the system's default attribute settings. For example, if the modifier is used to set font size attributes, such as **fontSize**, **maxFontSize**, and **minFontSize**, the settings will take precedence over the system's default settings for size-related attributes.

2\. If no modifier is used or an invalid value is set, the system reverts to its default settings.

3\. In [Free](#navigationtitlemode) mode, setting the font size will disable the effect where the main title's size changes in response to content scrolling.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| subTitleModifier13+ | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | No | Yes | 

Subtitle attribute modifier.

1\. Attribute settings configured by this modifier will override the system's default attribute settings. For example, if the modifier is used to set font size attributes, such as **fontSize**, **maxFontSize**, and **minFontSize**, the settings will take precedence over the system's default settings for size-related attributes.

2\. If no modifier is used or an invalid value is set, the system reverts to its default settings.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| enableHoverMode13+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode.

Observe the following when using this API:

1\. Make sure the **Navigation** component is in full screen.

2\. When the title bar is in [Free](#navigationtitlemode) display mode or in [STANDARD](#barstyle12) layout style, this API has no effect.

**true**: yes; **false**: no

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

#### NavigationToolbarOptions11+

Defines the toolbar options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Background color of the toolbar. If this parameter is not set, the default color is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the toolbar. If this parameter is not set, the background blur effect is disabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 

Options for the toolbar background blur style.

**NOTE**

This parameter is only effective when **backgroundBlurStyle** is set.

Avoid using this API in conjunction with **backgroundEffect**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Toolbar background properties, including blur radius, brightness, saturation, and color.

**NOTE**

Avoid using this API in conjunction with **backgroundBlurStyleOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| barStyle14+ | [BarStyle](#barstyle12) | No | Yes | 

Layout style of the toolbar.

Default value: **BarStyle.STANDARD**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hideItemValue19+ | boolean | No | Yes | 

Whether to hide the toolbar text.

Default value: **false**

**true**: yes; **false**: no

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| moreButtonOptions19+ | [MoreButtonOptions](#morebuttonoptions19) | No | Yes | 

Options for the toolbar's more button menu.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### NavigationMenuOptions19+

Defines options for menu items in the upper right corner of the page.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| moreButtonOptions | [MoreButtonOptions](#morebuttonoptions19) | No | Yes | Options for the more button menu. |

#### LaunchMode12+

Enumerates the operation modes for the routing stack.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| STANDARD | 0 | 
Default routing stack operation mode.

In this mode, push operations add the specified **NavDestination** page to the stack; replace operations replace the current top **NavDestination** page.

 |
| MOVE\_TO\_TOP\_SINGLETON | 1 | This mode searches from the bottom to the top of the routing stack. If a **NavDestination** page with the specified name exists, it moves that page to the top of the stack (for a replace operation, it replaces the last top **NavDestination** page with the specified one); otherwise, it behaves like **STANDARD**. |
| POP\_TO\_SINGLETON | 2 | This mode searches from the bottom to the top of the routing stack. If a **NavDestination** page with the specified name exists, it removes all **NavDestination** pages above it(for a replace operation, it replaces the last top **NavDestination** page with the specified one); otherwise, it behaves like **STANDARD**. |
| NEW\_INSTANCE | 3 | This mode creates an instance of **NavDestination**. Compared with **STANDARD**, this mode does not reuse the instance with the same name in the stack. When this mode is specified, the newly created page will execute the push animation effect by default. |

#### NavigationOptions12+

Defines the routing stack operation options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| launchMode | [LaunchMode](#launchmode12) | No | Yes | 
Operation mode of the routing stack.

Default value: **LaunchMode.STANDARD**

 |
| animated | boolean | No | Yes | 

Whether to enable the transition animation.

**true**: yes; **false**: no

Default value: **true**

 |

#### MoreButtonOptions19+

Defines the options for the more button menu.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | Background blur style of the more button menu. If this parameter is not set, background blur is disabled. |
| backgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 
Background blur style options of the more button menu.

**NOTE**

This parameter is only effective when **backgroundBlurStyle** is set.

Avoid using this API in conjunction with **backgroundEffect**.

 |
| backgroundEffect | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Background properties of the more button menu, including blur radius, brightness, saturation, and color.

**NOTE**

Avoid using this parameter in conjunction with **backgroundBlurStyleOptions**.

 |

#### SystemBarStyle12+

type SystemBarStyle = SystemBarStyle

Describes the properties of the status bar. These properties are valid for the page-level status bar.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [SystemBarStyle](../../../arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#systembarstyle12) | 
Color of the text on the status bar.

Default value: **'#0xE5FFFFFF'**

 |

#### HomePathInfo20+

Defines the home page **NavDestination** information.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the home page **NavDestination**. |
| param | Object | No | Yes | Detailed parameters of the home page **NavDestination**. |

#### Example

The outcome of the sample code may vary depending on the actual device used. The system routing table does not work with DevEco Studio Previewer or emulators.

## Example 1: Implementing a Navigation Page Layout

This example demonstrates the layout of a navigation page, including the title bar ([title](#title)), menu bar ([menus](#menus)), content area, and toolbar ([toolbarConfiguration](#toolbarconfiguration10)).

// xxx.ets

@Entry
@Component
struct NavigationExample {
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];

  @Builder
  NavigationTitle() {
    Column() {
      Text('Title')
        .fontColor('#182431')
        .fontSize(30)
        .lineHeight(41)
        .fontWeight(700)
      Text('subtitle')
        .fontColor('#182431')
        .fontSize(14)
        .lineHeight(19)
        .opacity(0.4)
        .margin({ top: 2, bottom: 20 })
    }.alignItems(HorizontalAlign.Start)
  }

  @Builder
  NavigationMenus() {
    Row() {
      // Replace 'resources/base/media/ic\_public\_add.svg' with the resource file you use.
      Image('resources/base/media/ic\_public\_add.svg')
        .width(24)
        .height(24)
      // Replace 'resources/base/media/ic\_public\_add.svg' with the resource file you use.
      Image('resources/base/media/ic\_public\_add.svg')
        .width(24)
        .height(24)
        .margin({ left: 24 })
      // Replace 'resources/base/media/ic\_public\_more.svg' with the image resource file you use.
      Image('resources/base/media/ic\_public\_more.svg')
        .width(24)
        .height(24)
        .margin({ left: 24 })
    }
  }

  build() {
    Column() {
      Navigation() {
        TextInput({ placeholder: 'search...' })
          .width('90%')
          .height(40)
          .backgroundColor('#FFFFFF')
          .margin({ top: 8 })

        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('90%')
                .height(72)
                .backgroundColor('#FFFFFF')
                .borderRadius(24)
                .fontSize(16)
                .fontWeight(500)
                .textAlign(TextAlign.Center)
            }
          }, (item: number) => item.toString())
        }
        .height(324)
        .width('100%')
        .margin({ top: 12, left: '10%' })
      }
      .title(this.NavigationTitle)
      .menus(this.NavigationMenus)
      .titleMode(NavigationTitleMode.Full)
      .toolbarConfiguration(\[
        {
          // Replace $r("app.string.navigation\_toolbar\_add") and $r("app.media.ic\_public\_highlights\_ed") with the image resource file you use.
          value: $r("app.string.navigation\_toolbar\_add"),
          icon: $r("app.media.ic\_public\_highlights\_ed")
        },
        {
          // Replace $r("app.string.navigation\_toolbar\_app") and $r("app.media.ic\_public\_highlights") with the image resource file you use.
          value: $r("app.string.navigation\_toolbar\_app"),
          icon: $r("app.media.ic\_public\_highlights")
        },
        {
          // Replace $r("app.string.navigation\_toolbar\_collect") and $r("app.media.ic\_public\_highlights") with the image resource file you use.
          value: $r("app.string.navigation\_toolbar\_collect"),
          icon: $r("app.media.ic\_public\_highlights")
        }
      \])
      .hideTitleBar(false)
      .hideToolBar(false)
      .onTitleModeChange((titleModel: NavigationTitleMode) => {
        console.info('titleMode' + titleModel)
      })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/oVk-P8O1S2StCXNCA1-z3Q/en-us_image_0000002568765291.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=992BA63230C6D513497FFE7BE78F575E366C30F6966C2E1C0D8754C7459BFFD6)

## Example 2: Using NavPathStack APIs

This example demonstrates the use of methods in [NavPathStack](#navpathstack10) and route interception.

// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfos: NavPathStack = new NavPathStack();
  isUseInterception: boolean = false;

  registerInterception() {
    this.pageInfos.setInterception({
      // Interception before page redirection, allowing for stack operations. The setting takes effect in the current redirection.
      willShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
        operation: NavigationOperation, animated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof to === "string") {
          console.info("target page is navigation home");
          return;
        }
        // Redirect the target page from pageTwo to pageOne.
        let target: NavDestinationContext = to as NavDestinationContext;
        if (target.pathInfo.name === 'pageTwo') {
          target.pathStack.pop();
          target.pathStack.pushPathByName('pageOne', null);
        }
      },
      // Callback invoked after the page is navigated. Stack operations in this callback are effective in the next navigation.
      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
        operation: NavigationOperation, isAnimated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof from === "string") {
          console.info("current transition is from navigation home");
        } else {
          console.info(\`current transition is from  ${(from as NavDestinationContext).pathInfo.name}\`);
        }
        if (typeof to === "string") {
          console.info("current transition to is navBar");
        } else {
          console.info(\`current transition is to ${(to as NavDestinationContext).pathInfo.name}\`);
        }
      },
      // Callback invoked when the display mode of the Navigation component switches between single-column and split-column.
      modeChange: (mode: NavigationMode) => {
        if (!this.isUseInterception) {
          return;
        }
        console.info(\`current navigation mode is ${mode}\`);
      }
    })
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' }); // Push the navigation destination page specified by name to the stack.
          })
        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.isUseInterception = !this.isUseInterception;
            if (this.isUseInterception) {
              this.registerInterception();
            } else {
              this.pageInfos.setInterception(undefined);
            }
          })
      }
    }.title('NavIndex')
  }
}

// PageOne.ets
class TmpClass {
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfos.pushPathByName('pageTwo', tmp); // Push the navigation destination page specified by name, with the data specified by param, to the stack.
          })
        Button('singletonLaunchMode', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' },
              { launchMode: LaunchMode.MOVE\_TO\_TOP\_SINGLETON }); // Search from the bottom to the top of the stack. If the page with the specified name exists, move that page to the top of the stack.
          })
        Button('popToname', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToName('pageTwo'); // Pop the first navigation destination page that matches the value of name to the top of the routing stack.
            console.info(\`popToName ${JSON.stringify(this.pageInfos)},\` +
              \`Return value ${JSON.stringify(this.pageInfos.popToName('pageTwo'))}\`);
          })
        Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToIndex(1); // Return the routing stack to the navigation destination page that matches the value of index.
            console.info(\`popToIndex ${JSON.stringify(this.pageInfos)}\`);
          })
        Button('moveToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveToTop('pageTwo'); // Move to the top of the routing stack the first navigation destination page that matches the value of name.
            console.info(\`moveToTop ${JSON.stringify(this.pageInfos)},\` +
              \`Return value ${JSON.stringify(this.pageInfos.popToName('pageTwo'))}\`);
          })
        Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveIndexToTop(1); // Move to the top of the routing stack the navigation destination page that matches the value of index.
            console.info(\`moveIndexToTop ${JSON.stringify(this.pageInfos)}\`);
          })
        Button('clear', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.clear(); // Clear the routing stack.
          })
        Button('get', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            console.info('-------------------');
            console.info(\`Obtain names of all NavDestination pages in the stack ${JSON.stringify(this.pageInfos.getAllPathName())}\`);
            console.info(\`Obtained parameter information of the navigation destination page specified by index ${JSON.stringify(this.pageInfos.getParamByIndex(1))}\`);
            console.info(\`Obtained parameter information of all the navigation destination pages specified by name ${JSON.stringify(this.pageInfos.getParamByName('pageTwo'))}\`);
            console.info(\`Obtained the index information of all the navigation destination pages specified by name ${JSON.stringify(this.pageInfos.getIndexByName('pageOne'))}\`);
            console.info(\`Obtain the stack size ${JSON.stringify(this.pageInfos.size())}\`);
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      const popDestinationInfo = this.pageInfos.pop(); // Pop the top element out of the routing stack.
      console.info(\`pop return value ${JSON.stringify(popDestinationInfo)}\`);
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
  }
}

// PageTwo.ets
@Builder
export function PageTwoBuilder(name: string, param: Object) {
  PageTwo()
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();
  private menuItems: Array<NavigationMenuItem> = \[
    {
      // Replace 'resources/base/media/undo.svg' with the image resource file you use.
      value: "1",
      icon: 'resources/base/media/undo.svg',
    },
    {
      // Replace 'resources/base/media/redo.svg' with the image resource file you use.
      value: "2",
      icon: 'resources/base/media/redo.svg',
      isEnabled: false,
    },
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: "3",
      icon: 'resources/base/media/ic\_public\_ok.svg',
      isEnabled: true,
    }
  \];

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pushPathByName('pageOne', null);
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .menus(this.menuItems)
    .onBackPressed(() => {
      this.pathStack.pop();
      return true;
    })
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
      console.info(\`current page config info is ${JSON.stringify(context.getConfigInRouteMap())}\`);
    })
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/FE7Bi306SpeQQGNFfPfhEA/en-us_image_0000002537765566.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C656099FB053E80E7DB2F8AF07B61A7E37EC54F4B78A6A100DC456DDA138262)

## Example 3: Setting an Interactive Transition Animation

This sample demonstrates how to set a custom transition animation and an interactive transition animation for each [NavDestination](../navdestination/document.md) page.

// Index.ets
import { CustomTransition, AnimateCallback } from './CustomNavigationUtils'

@Entry
@Component
struct NavigationExample {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear() {
    if (this.pageInfos === undefined) {
      this.pageInfos = new NavPathStack();
    }
    this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
  }

  build() {
    Navigation(this.pageInfos) {
    }
    .title('NavIndex')
    .hideNavBar(true)
    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
      if (from.mode == NavDestinationMode.DIALOG || to.mode == NavDestinationMode.DIALOG) {
        return undefined;
      }

      // No custom animation for the home page
      if (from.index === -1 || to.index === -1) {
        return undefined;
      }

      CustomTransition.getInstance().operation = operation;
      if (CustomTransition.getInstance().interactive) {
        let customAnimation: NavigationAnimatedTransition = {
          onTransitionEnd: (isSuccess: boolean) => {
            console.info("===== current transition is " + isSuccess);
            CustomTransition.getInstance().recoverState();
            CustomTransition.getInstance().proxy = undefined;
          },
          transition: (transitionProxy: NavigationTransitionProxy) => {
            CustomTransition.getInstance().proxy = transitionProxy;
            let targetIndex: string | undefined = operation == NavigationOperation.PUSH ?
              (to.navDestinationId) : (from.navDestinationId);
            if (targetIndex) {
              CustomTransition.getInstance().fireInteractiveAnimation(targetIndex, operation);
            }
          },
          isInteractive: CustomTransition.getInstance().interactive
        }
        return customAnimation;
      }
      let customAnimation: NavigationAnimatedTransition = {
        onTransitionEnd: (isSuccess: boolean) => {
          console.info(\`current transition result is ${isSuccess}\`);
        },
        timeout: 7000,
        // Called when transition starts. The transition context proxy object is passed in.
        transition: (transitionProxy: NavigationTransitionProxy) => {
          if (!from.navDestinationId || !to.navDestinationId) {
            return;
          }
          // Obtain the corresponding transition animation callback from the CustomTransition class by subpage ID.
          let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);
          let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);
          if (operation == NavigationOperation.PUSH) {
            if (toParam.start) {
              toParam.start(true, false);
            }
            this.getUIContext()?.animateTo({
              duration: 500, onFinish: () => {
                transitionProxy.finishTransition();
              }
            }, () => {
              if (toParam.finish) {
                toParam.finish(true, false);
              }
            })
          } else {
            if (fromParam.start) {
              fromParam.start(true, true);
            }
            this.getUIContext()?.animateTo({
              duration: 500, onFinish: () => {
                transitionProxy.finishTransition();
              }
            }, () => {
              if (fromParam.finish) {
                fromParam.finish(true, true);
              }
            })
          }
        }
      };
      return customAnimation;
    })
  }
}

// PageOne.ets
import { CustomTransition } from './CustomNavigationUtils';

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();
  @State translateX: string = '0';
  pageId: string = '';
  rectWidth: number = 0;
  interactive: boolean = false;

  registerCallback() {
    CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '100%';
      } else {
        this.translateX = '0';
      }
    }, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '0';
      } else {
        this.translateX = '100%';
      }
    }, (isPush: boolean, isExit: boolean) => {
      this.translateX = '0';
    }, (operation: NavigationOperation) => {
      if (operation == NavigationOperation.PUSH) {
        this.translateX = '100%';
        this.getUIContext()?.animateTo({
          duration: 1000,
          onFinish: () => {
            this.translateX = '0';
          }
        }, () => {
          this.translateX = '0';
        })
      } else {
        this.translateX = '0';
        this.getUIContext()?.animateTo({
          duration: 1000,
          onFinish: () => {
            this.translateX = '0';
          }
        }, () => {
          this.translateX = '100%';
        })
      }
    }, 200);
  }

  build() {
    NavDestination() {
      Column() {
        Button(\`setInteractive\`)
          .onClick(() => {
            CustomTransition.getInstance().interactive = !CustomTransition.getInstance().interactive;
            this.interactive = CustomTransition.getInstance().interactive;
          })

        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            // Push the navigation destination page specified by name, with the data specified by param, to the routing stack.
            this.pageInfos.pushDestinationByName('pageTwo', CustomTransition.getInstance().getAnimationId());
          })
      }
      .size({ width: '100%', height: '100%' })
    }
    .title('pageOne')
    .onDisAppear(() => {
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      if (context.navDestinationId) {
        this.pageId = context.navDestinationId;
        this.registerCallback();
      }
    })
    .translate({ x: this.translateX })
    .backgroundColor('#F1F3F5')
    .gesture(PanGesture()
      .onActionStart((event: GestureEvent) => {
        this.rectWidth = event.target.area.width as number;
        if (event.offsetX < 0) {
          this.pageInfos.pushPath({ name: 'pageTwo', param: CustomTransition.getInstance().getAnimationId() });
        } else {
          this.pageInfos.pop();
        }
      })
      .onActionUpdate((event: GestureEvent) => {
        let rate = event.fingerList\[0\].localX / this.rectWidth;
        CustomTransition.getInstance().updateProgress(rate);
      })
      .onActionEnd((event: GestureEvent) => {
        let rate: number = event.fingerList\[0\].localX / this.rectWidth;
        CustomTransition.getInstance().finishInteractiveAnimation(rate);
      }))
  }
}

// PageTwo.ets
import { CustomTransition } from './CustomNavigationUtils'

@Builder
export function PageTwoBuilder(name: string, param: Object) {
  PageTwo({ param: param as number })
}

@Component
export struct PageTwo {
  pageInfos: NavPathStack = new NavPathStack();
  @State translateX: string = '0';
  pageId: string = '';
  rectWidth: number = 0;
  param: number = 0;

  registerCallback() {
    CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '100%'
      } else {
        this.translateX = '0';
      }
    }, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '0';
      } else {
        this.translateX = '100%';
      }
    }, (isPush: boolean, isExit: boolean) => {
      this.translateX = '0';
    }, (operation: NavigationOperation) => {
      if (operation == NavigationOperation.PUSH) {
        this.translateX = '100%';
        this.getUIContext()?.animateTo({
          duration: 500, onFinish: () => {
            this.translateX = '0';
          }
        }, () => {
          this.translateX = '0';
        })
      } else {
        this.translateX = '0';
        this.getUIContext()?.animateTo({
          duration: 500, onFinish: () => {
            this.translateX = "0";
          }
        }, () => {
          this.translateX = '100%';
        })
      }
    }, 2000)
  }

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            // Push the navigation destination page specified by name, with the data specified by param, to the routing stack.
            this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
          })
      }
      .size({ width: '100%', height: '100%' })
    }
    .title('pageTwo')
    .gesture(PanGesture()
      .onActionStart((event: GestureEvent) => {
        this.rectWidth = event.target.area.width as number;
        if (event.offsetX < 0) {
          this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
        } else {
          this.pageInfos.pop();
        }
      })
      .onActionUpdate((event: GestureEvent) => {
        let rate = event.fingerList\[0\].localX / this.rectWidth;
        CustomTransition.getInstance().updateProgress(rate);
      })
      .onActionEnd((event: GestureEvent) => {
        let rate = event.fingerList\[0\].localX / this.rectWidth;
        CustomTransition.getInstance().finishInteractiveAnimation(rate);
      }))
    .onAppear(() => {
      this.registerCallback();
    })
    .onDisAppear(() => {
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      if (context.navDestinationId) {
        this.pageId = context.navDestinationId;
        this.registerCallback();
      }
    })
    .translate({ x: this.translateX })
    .backgroundColor(Color.Yellow)
  }
}

// src/main/pages/CustomNavigationUtils.ets
// Custom API to save the transition animation callback and parameters related to a page.

export interface AnimateCallback {
  finish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  start: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  onFinish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  interactive: ((operation: NavigationOperation) => void | undefined) | undefined;
  timeout: (number | undefined) | undefined;
}

const customTransitionMap: Map<string, AnimateCallback> = new Map();

export class CustomTransition {
  static delegate = new CustomTransition();
  interactive: boolean = false;
  proxy: NavigationTransitionProxy | undefined = undefined;
  private animationId: number = 0;
  operation: NavigationOperation = NavigationOperation.PUSH;

  static getInstance() {
    return CustomTransition.delegate;
  }

  /\* Register animation callbacks for a page.
   \* name: unique ID of the target page
   \* startCallback: used to set the page state at the start of the animation.
   \* endCallback: used to set the page state at the end of the animation.
   \* onFinish: used to perform other operations after the animation ends.
   \* interactiveCallback: used to handle the interactive part of the transition.
   \* timeout: timeout for ending the transition.
   \*/
  registerNavParam(name: string, startCallback: (operation: boolean, isExit: boolean) => void,
    endCallback: (operation: boolean, isExit: boolean) => void,
    onFinish: (operation: boolean, isExit: boolean) => void,
    interactiveCallback: (operation: NavigationOperation) => void,
    timeout: number): void {
    if (customTransitionMap.has(name)) {
      let param = customTransitionMap.get(name);
      if (param != undefined) {
        param.start = startCallback;
        param.finish = endCallback;
        param.timeout = timeout;
        param.onFinish = onFinish;
        param.interactive = interactiveCallback;
        return;
      }
    }
    let params: AnimateCallback = {
      timeout: timeout,
      start: startCallback,
      finish: endCallback,
      onFinish: onFinish,
      interactive: interactiveCallback
    };
    customTransitionMap.set(name, params);
  }

  getAnimationId() {
    return Date.now();
  }

  unRegisterNavParam(name: string): void {
    customTransitionMap.delete(name);
  }

  fireInteractiveAnimation(id: string, operation: NavigationOperation) {
    let animation = customTransitionMap.get(id)?.interactive;
    if (!animation) {
      return;
    }
    animation(operation);
  }

  updateProgress(progress: number) {
    if (!this.proxy?.updateTransition) {
      return;
    }
    progress = this.operation == NavigationOperation.PUSH ? 1 - progress : progress;
    this.proxy?.updateTransition(progress);
  }

  cancelTransition() {
    if (this.proxy?.cancelTransition) {
      this.proxy.cancelTransition();
    }
  }

  recoverState() {
    if (!this.proxy?.from.navDestinationId || !this.proxy?.to.navDestinationId) {
      return;
    }
    let fromParam = customTransitionMap.get(this.proxy.from.navDestinationId);
    if (fromParam?.onFinish) {
      fromParam.onFinish(false, false);
    }
    let toParam = customTransitionMap.get(this.proxy?.to.navDestinationId);
    if (toParam?.onFinish) {
      toParam.onFinish(true, true);
    }
  }

  finishTransition() {
    this.proxy?.finishTransition();
  }

  finishInteractiveAnimation(rate: number) {
    if (this.operation == NavigationOperation.PUSH) {
      if (rate > 0.5) {
        if (this.proxy?.cancelTransition) {
          this.proxy.cancelTransition();
        }
      } else {
        this.proxy?.finishTransition();
      }
    } else {
      if (rate > 0.5) {
        this.proxy?.finishTransition();
      } else {
        if (this.proxy?.cancelTransition) {
          this.proxy.cancelTransition();
        }
      }
    }
  }

  getAnimateParam(name: string): AnimateCallback {
    let result: AnimateCallback = {
      start: customTransitionMap.get(name)?.start,
      finish: customTransitionMap.get(name)?.finish,
      timeout: customTransitionMap.get(name)?.timeout,
      onFinish: customTransitionMap.get(name)?.onFinish,
      interactive: customTransitionMap.get(name)?.interactive,
    };
    return result;
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/wvqLLuQPRWOnGxT4_iW5OQ/en-us_image_0000002537925506.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55FD6031E93EF33688680A28564F7A35761D650E342C18B2AC46034B96B843BD)

## Example 4: Implementing a Navigation Component with Parameter Returning

This example demonstrates how to use the APIs in [NavPathStack](#navpathstack10) to pass parameters back to the previous page.

// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'pageOne' }); // Push the navigation destination page specified by name to the routing stack.
          })
      }
    }.title('NavIndex')
  }
}

// PageOne.ets
import { BusinessError } from '@kit.BasicServicesKit';

class TmpClass {
  count: number = 10;
}

class ParamWithOp {
  operation: number = 1;
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();
  @State message: string = 'Hello World';

  build() {
    NavDestination() {
      Column() {
        Text(this.message)
          .width('80%')
          .height(50)
          .margin(10)

        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            this.pageInfo.pushPath({
              name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
                this.message =
                  \`\[pushPath\]last page is: ${popInfo.info.name},result: ${JSON.stringify(popInfo.result)}\`;
              }
            }); // Push the navigation destination page specified by name, with the data specified by param, to the routing stack. Use the onPop callback to receive the page processing result.
          })

        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfo.pushPathByName('pageTwo', tmp, (popInfo) => {
              this.message =
                \`\[pushPathByName\]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}\`;
            }); // Push the navigation destination page specified by name, with the data specified by param, to the routing stack. Use the onPop callback to receive the page processing result.
          })

        Button('pushDestination', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // Push the navigation destination page specified by name, with the data specified by param, to the routing stack. Use the onPop callback to receive the page processing result.
            this.pageInfo.pushDestination({
              name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
                this.message =
                  \`\[pushDestination\]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}\`;
              }
            }).catch((error: BusinessError) => {
              console.error(\`\[pushDestination\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.error('\[pushDestination\]success.');
            });
          })

        Button('pushDestinationByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // Push the navigation destination page specified by name, with the data specified by param, to the routing stack. Use the onPop callback to receive the page processing result.
            this.pageInfo.pushDestinationByName('pageTwo', tmp, (popInfo) => {
              this.message =
                \`\[pushDestinationByName\]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}\`;
            }).catch((error: BusinessError) => {
              console.error(\`\[pushDestinationByName\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
            }).then(() => {
              console.error('\[pushDestinationByName\]success.');
            });
          })

        Button('pushPathWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'pageTwo', param: new ParamWithOp() }); // Push the navigation destination page specified by name to the routing stack.
          })

        Button('pushPathByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfo.pushPathByName('pageTwo', tmp); // Push the navigation destination page specified by name, with the data specified by param, to the routing stack.
          })

        Button('pushDestinationWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // Push the navigation destination page specified by name, with the data specified by param, to the routing stack. Use the onPop callback to receive the page processing result.
            this.pageInfo.pushDestination({ name: 'pageTwo', param: new ParamWithOp() })
              .catch((error: BusinessError) => {
                console.error(\`\[pushDestinationWithoutOnPop\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
              }).then(() => {
              console.error('\[pushDestinationWithoutOnPop\]success.');
            });
          })

        Button('pushDestinationByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // Push the navigation destination page specified by name, with the data specified by param, to the routing stack.
            this.pageInfo.pushDestinationByName('pageTwo', tmp)
              .catch((error: BusinessError) => {
                console.error(\`\[pushDestinationByNameWithoutOnPop\]failed, error code = ${error.code}, error.message = ${error.message}.\`);
              }).then(() => {
              console.error('\[pushDestinationByNameWithoutOnPop\]success.');
            });
          })

        Button('clear', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            this.pageInfo.clear(); // Clear the routing stack.
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      this.pageInfo.pop({ number: 1 }); // Pop the top element out of the routing stack.
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}

// PageTwo.ets
class resultClass {
  constructor(count: number) {
    this.count = count;
  }

  count: number = 10;
}

@Builder
export function PageTwoBuilder() {
  PageTwo();
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pop(new resultClass(1)); // Return to the previous page and pass in the processing result to the onPop callback of push.
          })

        Button('popToName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToName('pageOne',
              new resultClass(11)); // Move the first navigation destination page that matches name to the top of the routing stack, and pass in the processing result to the onPop callback of push.
          })

        Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToIndex(0, new resultClass(111)); // Move the navigation destination page specified by index to the top of the routing stack, and pass in the processing result to the onPop callback of push.
          })

        Button('popWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pop();
          })

        Button('popToNameWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToName('pageOne');
          })

        Button('popToIndexWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToIndex(0);
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onBackPressed(() => {
      this.pathStack.pop(new resultClass(0)); // Return to the previous page and pass in the processing result to the onPop callback of push.
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    })
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/XCQGrJCMS8SvK-7RDtUt8Q/en-us_image_0000002568685283.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C70E658FCABFABC41AB01DC65DCA2A55D22EC5743B74978453C0FEFF4344EA04)

## Example 5: Setting the Background Color and Blur Effect

This example demonstrates how to set the background color and background blur effect for the title bar of the home page in **Navigation**, as well as for the toolbar and the title bars on the [NavDestination](../navdestination/document.md) pages.

// Index
import {
  COLOR1,
  COLOR2,
  BLUR\_STYLE\_1,
  BLUR\_STYLE\_2,
  BLUR\_STYLE\_OPTION\_1,
  BLUR\_STYLE\_OPTION\_2,
} from './Utils';

@Entry
@Component
struct Index {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
  @State useColor1: boolean = true;
  @State useBlur1: boolean = true;
  @State useBlurOption1: boolean = true;

  build() {
    Navigation(this.navPathStack) {
      Stack({ alignContent: Alignment.Center }) {
        BackComponent()
          .width('100%')
          .height('100%')
        Column() {
          Stack({ alignContent: Alignment.Center }) {
            Button("switch color")
              .onClick(() => {
                this.useColor1 = !this.useColor1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch blur")
              .onClick(() => {
                this.useBlur1 = !this.useBlur1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch blurOption")
              .onClick(() => {
                this.useBlurOption1 = !this.useBlurOption1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("push page")
              .onClick(() => {
                this.navPathStack.pushPathByName('NavigationMenu', null);
              })
          }
          .width('100%')
          .layoutWeight(1)
        }
        .width('100%')
        .height('80%')
      }.width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    // You can set the background color and background blur style of the title bar.
    .title("NavTitle", {
      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
      backgroundBlurStyle: this.useBlur1 ? BLUR\_STYLE\_1 : BLUR\_STYLE\_2,
      barStyle: BarStyle.STACK,
      backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR\_STYLE\_OPTION\_1 : BLUR\_STYLE\_OPTION\_2,
    })
    // You can set the background color and background blur style for the menu
    .menus(\[
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
    \], {
      moreButtonOptions: {
        backgroundBlurStyle: this.useBlur1 ? BLUR\_STYLE\_1 : BLUR\_STYLE\_2,
        backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR\_STYLE\_OPTION\_1 : BLUR\_STYLE\_OPTION\_2,
      }
    })
    // You can set the background color and background blur style of the toolbar.
    .toolbarConfiguration(\[
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
      { value: "E" },
      { value: "F" }
    \], {
      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
      backgroundBlurStyle: this.useBlur1 ? BLUR\_STYLE\_1 : BLUR\_STYLE\_2,
      // You can set the background color and background blur style for the menu in the toolbar.
      moreButtonOptions: {
        backgroundBlurStyle: this.useBlur1 ? BLUR\_STYLE\_1 : BLUR\_STYLE\_2,
        backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR\_STYLE\_OPTION\_1 : BLUR\_STYLE\_OPTION\_2,
      }
    })
  }
}

@Component
export struct BackComponent {
  build() {
    Row() {
      Column() {
      }
      .height('100%')
      .backgroundColor("#3D9DB4")
      .layoutWeight(9)

      Column() {
      }
      .height('100%')
      .backgroundColor("#17A98D")
      .layoutWeight(9)

      Column() {
      }
      .height('100%')
      .backgroundColor("#FFC000")
      .layoutWeight(9)
    }
    .height('100%')
    .width('100%')
  }
}

// PageOne.ets
import {
  COLOR1,
  COLOR2,
  BLUR\_STYLE\_1,
  BLUR\_STYLE\_2,
  EFFECT\_OPTION\_1,
  EFFECT\_OPTION\_2
} from './Utils';
import { BackComponent } from './Index';

@Builder
export function PageBuilder(name: string, param?: Object) {
  ColorAndBlur();
}

@Component
struct ColorAndBlur {
  @State useColor1: boolean = true;
  @State useBlur1: boolean = true;
  @State useEffect1: boolean = true;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        BackComponent()
          .width('100%')
          .height('100%')
        Column() {
          Stack({ alignContent: Alignment.Center }) {
            Button("switch color")
              .onClick(() => {
                this.useColor1 = !this.useColor1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch blur")
              .onClick(() => {
                this.useBlur1 = !this.useBlur1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch effect")
              .onClick(() => {
                this.useEffect1 = !this.useEffect1;
              })
          }
          .width('100%')
          .layoutWeight(1)
        }
        .width('100%')
        .height('100%')
      }.width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    // You can set the background color and background blur style of the title bar.
    .title("Destination Title", {
      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
      backgroundBlurStyle: this.useBlur1 ? BLUR\_STYLE\_1 : BLUR\_STYLE\_2,
      barStyle: BarStyle.STACK,
      backgroundEffect: this.useEffect1 ? EFFECT\_OPTION\_1 : EFFECT\_OPTION\_2,
    })
    // You can set the background color and background blur style for the menu
    .menus(\[
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
    \], {
      moreButtonOptions: {
        backgroundEffect: this.useEffect1 ? EFFECT\_OPTION\_1 : EFFECT\_OPTION\_2,
      }
    })
    // You can set the background color and background blur style of the toolbar.
    .toolbarConfiguration(\[
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
      { value: "E" },
      { value: "F" }
    \], {
      backgroundEffect: this.useEffect1 ? EFFECT\_OPTION\_1 : EFFECT\_OPTION\_2,
      // You can set the background color and background blur style for the menu in the toolbar.
      moreButtonOptions: {
        backgroundEffect: this.useEffect1 ? EFFECT\_OPTION\_1 : EFFECT\_OPTION\_2,
      }
    })
  }
}

// Utils.ets
export const COLOR1: string = "#80004AAF";
export const COLOR2: string = "#802787D9";
export const BLUR\_STYLE\_1: BlurStyle = BlurStyle.BACKGROUND\_THIN;
export const BLUR\_STYLE\_2: BlurStyle = BlurStyle.BACKGROUND\_THICK;
export const BLUR\_STYLE\_OPTION\_1: BackgroundBlurStyleOptions = {
  colorMode: ThemeColorMode.DARK,
  adaptiveColor: AdaptiveColor.DEFAULT,
  blurOptions: { grayscale: \[20, 20\] },
  scale: 1
};
export const BLUR\_STYLE\_OPTION\_2: BackgroundBlurStyleOptions = {
  colorMode: ThemeColorMode.LIGHT,
  adaptiveColor: AdaptiveColor.AVERAGE,
  blurOptions: { grayscale: \[20, 20\] },
  scale: 1
};
export const EFFECT\_OPTION\_1: BackgroundEffectOptions = {
  radius: 20,
  saturation: 10,
  brightness: 0,
  color: '#66FFFFFF',
  adaptiveColor: AdaptiveColor.DEFAULT,
  blurOptions: { grayscale: \[0, 0\] },
};
export const EFFECT\_OPTION\_2: BackgroundEffectOptions = {
  radius: 60,
  saturation: 40,
  brightness: 1,
  color: '#661A1A1A',
  adaptiveColor: AdaptiveColor.AVERAGE,
  blurOptions: { grayscale: \[20, 20\] },
};

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "NavigationMenu",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Y1_MMpMzSkmbacnlCxQx7w/en-us_image_0000002568765293.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E4D5E0AC050B8FD452EA95FFEB9AE6067123B60492D6E63F02B84B4254FE49D)

## Example 6: Obtaining the Outer Stack for a Nested Navigation Component

This example shows how to obtain the parent [NavPathStack](#navpathstack10) for a nested **Navigation** component.

@Entry
@Component
struct NavigationExample1 {
  @State childNavStack: NavPathStack = new NavPathStack();

  build() {
    Navigation() {
      Stack({ alignContent: Alignment.Center }) {
        Navigation(this.childNavStack) {
          Button('push Path to parent Navigation', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              // The parent navigation path stack can be obtained.
              let parentStack = this.childNavStack.getParent();
              parentStack?.pushPath({ name: "pageOne" });
            })
        }
        .clip(true)
        .backgroundColor(Color.Orange)
        .width('80%')
        .height('80%')
        .title('ChildNavigation')
      }
      .width('100%')
      .height('100%')
    }
    .backgroundColor(Color.Green)
    .width('100%')
    .height('100%')
    .title('ParentNavigation')
  }
}

// PageOne.ets
@Builder
export function PageOneBuilder(name: string) {
  NavDestination() {
    Text("this is " + name)
  }
  .title(name)
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/ghPngPsuSS-UtswB-O7x_Q/en-us_image_0000002537765568.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6444582389B966AA20992166B5347ABD88993C5DD66D3EAFB3288A6CAB26CCB3)

## Example 7: Obtaining the Stack Through onReady

This example demonstrates the following:

1.  The routing stack operation can be conducted even when [NavPathStack](#navpathstack10) is not declared as a state variable.
    
2.  [NavDestination](../navdestination/document.md) can obtain the corresponding [NavPathInfo](#navpathinfo10) and its belonging [NavPathStack](#navpathstack10) via the [onReady](../navdestination/document.md#onready11) event.
    

class PageParam {
  constructor(num\_: number) {
    this.num = num\_;
  }

  num: number = 0;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne();
}

@Component
struct PageOne {
  private stack: NavPathStack | null = null;
  private name: string = "";
  private paramNum: number = 0;

  build() {
    NavDestination() {
      Column() {
        Text("NavPathInfo: name: " + this.name + ", paramNum: " + this.paramNum)
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            if (this.stack) {
              let p = new PageParam(this.paramNum + 1);
              this.stack.pushPath({ name: "pageOne", param: p });
            }
          })
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.stack?.pop();
          })
      }
      .width('100%')
      .height('100%')
    }
    .title('pageOne')
    .onReady((ctx: NavDestinationContext) => {
      // The passed NavPathInfo and the owning NavPathStack objects can be obtained for <NavDestination>.
      try {
        this.name = ctx?.pathInfo?.name;
        this.paramNum = (ctx?.pathInfo?.param as PageParam)?.num;
        this.stack = ctx.pathStack;
      } catch (e) {
        console.error(\`testTag onReady catch exception: ${JSON.stringify(e)}\`);
      }
    })
  }
}

@Entry
@Component
struct NavigationExample2 {
  private stack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.stack) {
      Stack({ alignContent: Alignment.Center }) {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            let p = new PageParam(1);
            this.stack.pushPath({ name: "pageOne", param: p });
          })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .title('Navigation')
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/-JU6k_H3QnG33VKzbC-YcA/en-us_image_0000002537925508.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4306C42799865E5EC244679A77117385D6DEDA99831A44D4EDDFE59C5B954BF)

## Example 8: Using NavDestination Lifecycle Callbacks

This example demonstrates the timing of the [NavDestination](../navdestination/document.md) component lifecycle callbacks: [onAppear](../../universal-events/component-change-events/show-hide-event/document.md#onappear), [onDisAppear](../../universal-events/component-change-events/show-hide-event/document.md#ondisappear), [onShown](../navdestination/document.md#onshown10), [onHidden](../navdestination/document.md#onhidden10), [onWillAppear](../navdestination/document.md#onwillappear12), [onWillDisappear](../navdestination/document.md#onwilldisappear12), [onWillShow](../navdestination/document.md#onwillshow12), and [onWillHide](../navdestination/document.md#onwillhide12).

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOneComponent();
}

@Component
struct PageOneComponent {
  private stack: NavPathStack | null = null;
  @State eventStr: string = "";

  build() {
    NavDestination() {
      Column() {
        Text("event: " + this.eventStr)
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            if (this.stack) {
              this.stack.pushPath({ name: "pageOne" });
            }
          })
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.stack?.pop();
          })
      }
      .width('100%')
      .height('100%')
    }
    .title('pageOne')
    .onAppear(() => {
      this.eventStr += "<onAppear>";
    })
    .onDisAppear(() => {
      this.eventStr += "<onDisAppear>";
    })
    .onShown(() => {
      this.eventStr += "<onShown>";
    })
    .onHidden(() => {
      this.eventStr += "<onHidden>";
    })
    .onWillAppear(() => {
      this.eventStr += "<onWillAppear>";
    })
    .onWillDisappear(() => {
      this.eventStr += "<onWillDisappear>";
    })
    .onWillShow(() => {
      this.eventStr += "<onWillShow>";
    })
    .onWillHide(() => {
      this.eventStr += "<onWillHide>";
    })
    // onReady is called before onAppear.
    .onReady((ctx: NavDestinationContext) => {
      try {
        this.eventStr += "<onReady>";
        this.stack = ctx.pathStack;
      } catch (e) {
        console.error(\`testTag onReady catch exception: ${JSON.stringify(e)}\`);
      }
    })
  }
}

@Entry
@Component
struct NavigationExample3 {
  private stack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.stack) {
      Stack({ alignContent: Alignment.Center }) {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.stack.pushPath({ name: "pageOne" });
          })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .title('Navigation')
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/y0T6u9TMR-esGiL7I5y9iQ/en-us_image_0000002568685285.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA252F95B5E6DD668F46EF0C6E339007868EC889AB4F44226AFF354DB5F39F06)

## Example 9: Configuring the Title Bar Stack Layout

This example demonstrates the stack layout of the title bar in the **Navigation** component.

@Entry
@Component
struct NavigationExample {
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\];
  private scrollerForScroll: Scroller = new Scroller();
  @State barStyle: BarStyle = BarStyle.STANDARD;

  build() {
    Column() {
      Navigation() {
        Column() {
          Scroll(this.scrollerForScroll) {
            Column() {
              // Replace $r('app.media.image\_1') with the resource file you use.
              Image($r('app.media.image\_1'))// Set the height to be the same as that of the title bar to observe the STACK effect.
                .height(138)
                .width('100%')
              Button('BarStyle.STANDARD')
                .height('50vp')
                .onClick(() => {
                  this.barStyle = BarStyle.STANDARD;
                })
              Button('BarStyle.STACK')
                .height('50vp')
                .margin({ top: 12 })
                .onClick(() => {
                  this.barStyle = BarStyle.STACK;
                })

              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('' + item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(Color.Orange)
                    .margin({ top: 12 })
                }
              }, (item: number) => item.toString())
            }
          }
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xDCDCDC)
      }
      .title(
        {
          main: 'NavTitle',
          sub: 'subtitle'
        },
        {
          backgroundBlurStyle: BlurStyle.COMPONENT\_THICK,
          barStyle: this.barStyle,
        }
      )
      .titleMode(NavigationTitleMode.Free)
      .hideTitleBar(false)
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/i-XR6WX_TBauu47ocY4fkQ/en-us_image_0000002568765295.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E34D8AE20B834D4A5B88997B85CE75B43B7C1813F6ED85E5BE138E26044E926)

## Example 10: Defining a Derived Class of NavPathStack

This example demonstrates how to define a derived class of [NavPathStack](#navpathstack10) and the basic usage of the derived class in **Navigation**.

// Index.ets
import { DerivedNavPathStack, NewParam } from './Utils';

@Entry
@Component
struct Index {
  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();

  aboutToAppear(): void {
    this.derivedStack.setId('origin stack');
  }
  
  build() {
    Navigation(this.derivedStack) {
      Button('to Page One').margin(20).onClick(() => {
        this.derivedStack.pushPath({
          name: 'pageOne',
          param: new NewParam('push pageOne in homePage when stack size: ' + this.derivedStack.size())
        });
      })
    }
    .title('Home Page')
  }
}

// PageOne.ets
import { DerivedNavPathStack, NewParam } from './Utils';

@Builder
export function pageMap(name: string) {
  PageOne();
}

@Component
struct PageOne {
  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();
  curStringifyParam: string = "NA";

  build() {
    NavDestination() {
      Column() {
        Text(this.derivedStack.getInfo())
          .margin(10)
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Start)
        Text('current page param info:')
          .margin(10)
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Start)
        Text(this.curStringifyParam)
          .margin(20)
          .fontSize(20)
          .textAlign(TextAlign.Start)
      }.backgroundColor(Color.Pink)

      Button('to Page One').margin(20).onClick(() => {
        this.derivedStack.pushPath({
          name: 'pageOne',
          param: new NewParam('push pageOne in pageOne when stack size: ' + this.derivedStack.size())
        });
      })
    }.title('Page One')
    .onReady((context: NavDestinationContext) => {
      console.info('\[derive-test\] reached PageOne\\'s onReady');
      // Obtain the derived stack from navdestinationContext.
      this.derivedStack = context.pathStack as DerivedNavPathStack;
      console.info('\[derive-test\] -- got derivedStack: ' + this.derivedStack.id);
      this.curStringifyParam = JSON.stringify(context.pathInfo.param);
      console.info('\[derive-test\] -- got param: ' + this.curStringifyParam);
    })
  }
}

// Utils.ets
export class DerivedNavPathStack extends NavPathStack {
  // Set the custom unique ID.
  id: string = "\_\_default\_\_";

  // Custom method for the derived class.
  setId(id: string) {
    this.id = id;
  }

  // Custom method for the derived class.
  getInfo(): string {
    return "this page used Derived NavPathStack, id: " + this.id;
  }

  // Overload the method inherited from the NavPathStack base class.
  pushPath(info: NavPathInfo, animated?: boolean): void
  pushPath(info: NavPathInfo, options?: NavigationOptions): void
  pushPath(info: NavPathInfo, secArg?: boolean | NavigationOptions): void {
    console.info('\[derive-test\] reached DerivedNavPathStack\\'s pushPath');
    if (typeof secArg === 'boolean') {
      super.pushPath(info, secArg);
    } else {
      super.pushPath(info, secArg);
    }
  }

  // Override and overload the method inherited from the NavPathStack base class.
  pop(animated?: boolean | undefined): NavPathInfo | undefined
  pop(result: Object, animated?: boolean | undefined): NavPathInfo | undefined
  pop(result?: Object, animated?: boolean | undefined): NavPathInfo | undefined {
    console.info('\[derive-test\] reached DerivedNavPathStack\\'s pop');
    return super.pop(result, animated);
  }

  // Remaining methods inherited from the base class
}

export class NewParam {
  info: string = "\_\_default\_param\_\_";

  constructor(info: string) {
    this.info = info;
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "pageMap",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/1dk4FG2JTGW2njwBDOkEgA/en-us_image_0000002537765570.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8369AF4240C2EC459B849C356AFAA788299EF98DC168EF38973B7E6E8C52BF7A)

## Example 11: Using Symbol Icons

This example demonstrates how to use the **Symbol** components in **Navigation** and **[NavDestination](../navdestination/document.md)**.

// Index.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct NavigationExample {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
  @State menuItems: Array<NavigationMenuItem> = \[
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: 'menuItem1',
      icon: 'resources/base/media/ic\_public\_ok.svg' // Icon resource path.
    },
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: 'menuItem2',
      icon: 'resources/base/media/ic\_public\_ok.svg', // Icon resource path.
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus')).fontColor(\[Color.Red, Color.Green\])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR),
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
    },
  \];
  @State toolItems: Array<ToolbarItem> = \[
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: 'toolItem1',
      icon: 'resources/base/media/ic\_public\_ok.svg', // Icon resource path.
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus')).fontColor(\[Color.Red,
        Color.Green\]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR),
      action: () => {
      }
    },
    {
      // Replace 'resources/base/media/ic\_public\_more.svg' with the image resource file you use.
      value: 'toolItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeIcon: 'resources/base/media/ic\_public\_more.svg', // Icon resource path.
      action: () => {
      }
    },
    {
      value: 'toolItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
      action: () => {
      }
    }
  \];

  build() {
    Navigation(this.navPathStack) {
      Column() {
        Button('Go').onClick(() => {
          this.navPathStack.pushPathByName('NavigationMenu', null);
        })
      }
    }
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi')))
    .titleMode(NavigationTitleMode.Mini)
    .menus(this.menuItems)
    .toolbarConfiguration(this.toolItems)
    .title('Level-1 page')
  }
}

// PageOne.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Builder
export function myRouter(name: string, param?: Object) {
  NavigationMenu();
}

@Component
export struct NavigationMenu {
  @Consume('navPathStack') navPathStack: NavPathStack;
  @State menuItems: Array<NavigationMenuItem> = \[
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: 'menuItem1',
      icon: 'resources/base/media/ic\_public\_ok.svg', // Icon resource path.
      action: () => {
      }
    },
    {
      value: 'menuItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus')).fontColor(\[Color.Red, Color.Green\])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR),
      action: () => {
      }
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat\_1')),
      action: () => {
      }
    },
  \];

  build() {
    NavDestination() {
      Row() {
        Column() {
        }
        .width('100%')
      }
      .height('100%')
    }
    .hideTitleBar(false)
    .title('NavDestination title')
    .backgroundColor($r('sys.color.ohos\_id\_color\_titlebar\_sub\_bg'))
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos\_star'))
      .fontColor(\[Color.Blue\]))
    .menus(this.menuItems)
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "NavigationMenu",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "myRouter",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/jDQHwlkhTl2oh-5424FkEg/en-us_image_0000002537925510.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA5949940F98131007C3559A7A8A118CD16297EB690BA64C6870C1873315691A)

## Example 12: Setting the Custom Title Bar Margin

This example demonstrates how to set custom title bar padding in **Navigation** and [NavDestination](../navdestination/document.md), and how to modify the main title and subtitle text styles through **TextModifier**.

// Index.ets
import { LengthMetrics } from '@kit.ArkUI';
import { MainTitleTextModifier, SubTitleTextModifier } from './Utils';

@Entry
@Component
struct NavigationExample {
  private navPathStack: NavPathStack = new NavPathStack();
  // Assign an initial padding at the start of the title bar.
  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);
  // Assign an initial padding at the end of the title bar.
  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);
  // Main title attribute modifier.
  @State mainTitleModifier: MainTitleTextModifier = new MainTitleTextModifier();
  // Subtitle attribute modifier.
  @State subTitleModifier: SubTitleTextModifier = new SubTitleTextModifier();
  @State applyModifier: boolean = false;
  @State useStyle1: boolean = true;

  build() {
    Navigation(this.navPathStack) {
      Column() {
        // Switch between padding values for the title bar.
        Button('apply padding 32vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(32);
            this.paddingEnd = LengthMetrics.vp(32);
          })
          .margin({ top: 70 })
          .width(180)
        Button('apply padding 20vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(20);
            this.paddingEnd = LengthMetrics.vp(20);
          })
          .margin({ top: 40 })
          .width(180)
        Button('pushPage')
          .onClick(() => {
            this.navPathStack.pushPath({ name: 'NavDestinationExample' });
          })
          .margin({ top: 40 })
          .width(180)
        Row() {
          Text(\`apply Modifier\`)
          Toggle({ isOn: this.applyModifier, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.applyModifier = isOn;
          })
        }
        .padding({ top: 95, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)

        Row() {
          Text(\`use Style1\`)
          Toggle({ isOn: this.useStyle1, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.mainTitleModifier.useStyle1 = isOn;
            this.subTitleModifier.useStyle1 = isOn;
            this.useStyle1 = isOn;
          })
        }
        .padding({ top: 40, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)
      }
      .width('100%')
      .height('100%')
    }
    .titleMode(NavigationTitleMode.Full)
    .title(
      { main: "Title", sub: "subTitle" },
      this.applyModifier ?
        {
          paddingStart: this.paddingStart,
          paddingEnd: this.paddingEnd,
          mainTitleModifier: this.mainTitleModifier,
          subTitleModifier: this.subTitleModifier,
        } : {
        paddingStart: this.paddingStart,
        paddingEnd: this.paddingEnd
      })
  }
}

// PageOne.ets
import { LengthMetrics } from '@kit.ArkUI';
import { MainTitleTextModifier, SubTitleTextModifier } from './Utils';

@Builder
export function myRouter(name: string, param?: Object) {
  NavDestinationExample();
}
@Component
export struct NavDestinationExample {
  @State menuItems: Array<NavigationMenuItem> = \[
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: 'menuItem1',
      icon: 'resources/base/media/ic\_public\_ok.svg', // Icon resource path.
      action: () => {
      }
    }
  \];
  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);
  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);
  // Main title attribute modifier.
  @State mainTitleModifier: MainTitleTextModifier = new MainTitleTextModifier();
  // Subtitle attribute modifier.
  @State subTitleModifier: SubTitleTextModifier = new SubTitleTextModifier();
  @State applyModifier: boolean = false;
  @State useStyle1: boolean = true;

  build() {
    NavDestination() {
      Column() {
        // Switch between padding values for the title bar.
        Button('apply padding 32vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(32);
            this.paddingEnd = LengthMetrics.vp(32);
          })
          .margin({ top: 150 })
          .width(180)
        Button('apply padding 20vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(20);
            this.paddingEnd = LengthMetrics.vp(20);
          })
          .margin({ top: 40 })
          .width(180)
        Row() {
          Text(\`apply Modifier\`)
          Toggle({ isOn: this.applyModifier, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.applyModifier = isOn;
          })
        }
        .padding({ top: 95, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)

        Row() {
          Text(\`use Style1\`)
          Toggle({ isOn: this.useStyle1, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.mainTitleModifier.useStyle1 = isOn;
            this.subTitleModifier.useStyle1 = isOn;
            this.useStyle1 = isOn;
          })
        }
        .padding({ top: 40, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)
      }
      .width('100%')
      .height('90%')
    }
    .hideTitleBar(false)
    .title(
      { main: "Title", sub: "subTitle" },
      this.applyModifier ?
        {
          paddingStart: this.paddingStart,
          paddingEnd: this.paddingEnd,
          mainTitleModifier: this.mainTitleModifier,
          subTitleModifier: this.subTitleModifier,
        } : {
        paddingStart: this.paddingStart,
        paddingEnd: this.paddingEnd
      })
    .menus(this.menuItems)
  }
}

// Utils.ets
import { TextModifier } from '@kit.ArkUI';

export class MainTitleTextModifier extends TextModifier {
  useStyle1: boolean = true;

  applyNormalAttribute(instance: TextModifier): void {
    if (this.useStyle1) {
      console.info(\`testTag mainTitle use style1\`);
      instance.fontColor('#FFFFC000');
      instance.fontSize(35);
      instance.fontWeight(FontWeight.Bolder);
      instance.fontStyle(FontStyle.Normal);
      instance.textShadow({ radius: 5, offsetX: 9 });
    } else {
      console.info(\`testTag mainTitle use style2\`);
      instance.fontColor('#FF23A98D');
      instance.fontSize(20);
      instance.heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST);
      instance.fontWeight(FontWeight.Lighter);
      instance.fontStyle(FontStyle.Italic);
      instance.textShadow({ radius: 3, offsetX: 3 });
    }
  }
}

export class SubTitleTextModifier extends TextModifier {
  useStyle1: boolean = true;

  applyNormalAttribute(instance: TextModifier): void {
    if (this.useStyle1) {
      console.info(\`testTag subTitle use style1\`);
      instance.fontColor('#FFFFC000');
      instance.fontSize(15);
      instance.fontWeight(FontWeight.Bolder);
      instance.fontStyle(FontStyle.Normal);
      instance.textShadow({ radius: 5, offsetX: 9 });
    } else {
      console.info(\`testTag subTitle use style2\`);
      instance.fontColor('#FF23A98D');
      instance.fontSize(10);
      instance.fontWeight(FontWeight.Lighter);
      instance.fontStyle(FontStyle.Italic);
      instance.textShadow({ radius: 3, offsetX: 3 });
    }
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "NavDestinationExample",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "myRouter",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/s2Mnf5DvQMi_aByTvTdxjQ/en-us_image_0000002568685287.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D42C127765C7EC038D2E8F7E99A1B8B02088188C142E70490F6A656C8BAC271)

## Example 13: Implementing a Custom Transition Animation

This example shows how to implement a custom transition animation for navigation between pages.

// Index.ets
import { AnimateCallback, CustomTransition } from './CustomTransitionUtils'

@Entry
@Component
struct NavigationCustomTransitionExample {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear() {
    this.pageInfos.pushPath({ name: 'PageOne' }, false);
  }

  build() {
    Navigation(this.pageInfos) {
    }
    .hideNavBar(true)
    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
      // No custom animation for the home page
      if (from.index === -1 || to.index === -1) {
        return undefined;
      }

      let customAnimation: NavigationAnimatedTransition = {
        timeout: 2000,
        // Called when transition starts. The transition context proxy object is passed in.
        transition: (transitionProxy: NavigationTransitionProxy) => {
          if (!from.navDestinationId || !to.navDestinationId) {
            return;
          }
          // Obtain the corresponding transition animation callback from the CustomTransition class by subpage ID.
          let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);
          let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);
          // Push animation
          if (operation == NavigationOperation.PUSH) {
            if (fromParam.start && toParam.start) {
              // Set the animation start for both pages in the push transition.
              fromParam.start(true, true);
              toParam.start(true, false);
            }
            this.getUIContext()?.animateTo({
              duration: 500, curve: Curve.Friction, onFinish: () => {
                // Manually call the finishTransition API after the animation ends. Otherwise, the system will automatically call the API after the specified timeout period.
                transitionProxy.finishTransition();
              }
            }, () => {
              if (fromParam.finish && toParam.finish) {
                // Set the animation end for both pages in the push transition.
                fromParam.finish(true, true);
                toParam.finish(true, false);
              }

            })
          } else if (operation == NavigationOperation.POP) {
            // Pop animation
            if (fromParam.start && toParam.start) {
              // Set the animation start for both pages in the pop transition.
              fromParam.start(false, true);
              toParam.start(false, false);
            }
            this.getUIContext()?.animateTo({
              duration: 500, curve: Curve.Friction, onFinish: () => {
                // Manually call the finishTransition API after the animation ends. Otherwise, the system will automatically call the API after the specified timeout period.
                transitionProxy.finishTransition();
              }
            }, () => {
              if (fromParam.finish && toParam.finish) {
                // Set the animation end for both pages in the pop transition.
                fromParam.finish(false, true);
                toParam.finish(false, false);
              }
            })
          } else {
            // No animation for the replacement operation
          }
        }
      };
      return customAnimation;
    })
  }
}

// PageOne
@Builder
export function PageOneBuilder() {
  PageContainer({ title: "PageOne" });
}

// PageTwo
@Builder
export function PageTwoBuilder() {
  PageContainer({ title: "PageTwo" });
}

@Component
export struct PageContainer {
  pageInfos: NavPathStack = new NavPathStack();
  @State translateY: string = '0';
  pageId: string = '';
  title: string = ''

  registerCallback() {
    CustomTransition.getInstance().registerNavParam(this.pageId,
      // Set the start point of the transition animation based on the transition type.
      (isPush: boolean, isExit: boolean) => {
        if (isPush) {
          if (isExit) {
            this.translateY = '0';
          } else {
            this.translateY = '100%';
          }
        } else {
          if (isExit) {
            this.translateY = '0';
          } else {
            this.translateY = '0';
          }
        }
      },
      // Set the end point of the transition animation based on the transition type.
      (isPush: boolean, isExit: boolean) => {
        if (isPush) {
          if (isExit) {
            this.translateY = '0';
          } else {
            this.translateY = '0';
          }
        } else {
          if (isExit) {
            this.translateY = '100%';
          } else {
            this.translateY = '0';
          }
        }
      });
  }

  build() {
    NavDestination() {
      Column() {
        Button('push next page', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: this.title == 'PageOne' ? "PageTwo" : "PageOne" });
          })
      }
      .size({ width: '100%', height: '100%' })
    }
    .title(this.title)
    .onDisAppear(() => {
      // Unregister the custom transition animation parameters when the page is destroyed.
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      if (context.navDestinationId) {
        this.pageId = context.navDestinationId;
        // Register the custom transition animation parameters when the page is created.
        this.registerCallback();
      }
    })
    .translate({ y: this.translateY })
    .backgroundColor(this.title == 'PageOne' ? '#F1F3F5' : '#ff11dee5')
  }
}

// The src/main/pages/CustomTransitionUtils.ts file defines a utility class for managing custom animation parameters for different pages.
// Custom API to save the transition animation callback and parameters related to a page.
export interface AnimateCallback {
  start: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  finish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
}

const customTransitionMap: Map<string, AnimateCallback> = new Map();

export class CustomTransition {
  static delegate = new CustomTransition();

  static getInstance() {
    return CustomTransition.delegate;
  }

  /\* Register animation callbacks for a page.
   \* name: unique ID of the target page
   \* startCallback: used to set the page state at the start of the animation.
   \* endCallback: used to set the page state at the end of the animation.
   \*/
  registerNavParam(name: string, startCallback: (isPush: boolean, isExit: boolean) => void,
    endCallback: (isPush: boolean, isExit: boolean) => void): void {
    if (customTransitionMap.has(name)) {
      let param = customTransitionMap.get(name);
      if (param != undefined) {
        param.start = startCallback;
        param.finish = endCallback;
        return;
      }
    }
    let params: AnimateCallback = { start: startCallback, finish: endCallback };
    customTransitionMap.set(name, params);
  }

  unRegisterNavParam(name: string): void {
    customTransitionMap.delete(name);
  }

  getAnimateParam(name: string): AnimateCallback {
    let result: AnimateCallback = {
      start: customTransitionMap.get(name)?.start,
      finish: customTransitionMap.get(name)?.finish
    };
    return result;
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "PageTwo",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageTwoBuilder"
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/4i2fBgB5TXayxJTApQ1ZOQ/en-us_image_0000002568765297.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC89CAC88149273B93639E7FFFEC33786ACBCADCB1A47FE5C81E7B3EA0D05CC6)

## Example 14: Setting the Navigation Split-Column Mode

This example demonstrates a **Navigation** component in split-column mode, where the right pane shows a default placeholder page. It also uses [navBarWidthRange](#navbarwidthrange10) to set the minimum and maximum width of the navigation page.

Before running this example, you need to set **orientation** to **auto\_rotation** in the **abilities** field of the project configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file).

import { ComponentContent } from '@kit.ArkUI';

@Builder function PlaceholderPage() {
  Column() {
    Text("Split-column mode placeholder page")
      .fontSize(28)
      .fontWeight(700)
      .margin({ top: 200 })
  }.width("100%")
  .height("100%")
}

@Entry
@Component
struct NavigationExample {
  @State minNavBarWidth: Dimension | undefined = undefined;
  @State maxNavBarWidth: Dimension | undefined = undefined;
  @State minContentWidth: Dimension|undefined = undefined;
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
  @State currentIndex: number = 0;
  placeholder = new ComponentContent(this.getUIContext(), wrapBuilder(PlaceholderPage))

  @Builder
  NavigationTitle() {
    Column() {
      Text('Title')
        .fontColor('#182431')
        .fontSize(30)
        .lineHeight(41)
        .fontWeight(700)
      Text('subtitle')
        .fontColor('#182431')
        .fontSize(14)
        .lineHeight(19)
        .opacity(0.4)
        .margin({ top: 2, bottom: 20 })
    }.alignItems(HorizontalAlign.Start)
  }

  @Builder
  NavigationMenus() {
    Row() {
      // Replace $r('sys.media.ohos\_ic\_public\_add') with the resource file you use.
      Image($r('sys.media.ohos\_ic\_public\_add'))
        .width(24)
        .height(24)
      // Replace $r('sys.media.ohos\_ic\_public\_add') with the resource file you use.
      Image($r('sys.media.ohos\_ic\_public\_add'))
        .width(24)
        .height(24)
        .margin({ left: 24 })
      // Replace $r('sys.media.ohos\_ic\_public\_more') with the resource file you use.
      Image($r('sys.media.ohos\_ic\_public\_more'))
        .width(24)
        .height(24)
        .margin({ left: 24 })
    }.margin({ top: 30 })
  }

  build() {
    Column() {
      Navigation() {
        TextInput({ placeholder: 'search...' })
          .width('90%')
          .height(40)
          .backgroundColor('#FFFFFF')
          .margin({ top: 8 })

        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('90%')
                .height(72)
                .backgroundColor('#FFFFFF')
                .borderRadius(24)
                .fontSize(16)
                .fontWeight(500)
                .textAlign(TextAlign.Center)
            }
          }, (item: number) => item.toString())
        }
        .height(324)
        .width('100%')
        .margin({ top: 12, left: '10%' })
      }
      .title(this.NavigationTitle)
      .padding({ left: 12 })
      .menus(this.NavigationMenus)
      .titleMode(NavigationTitleMode.Full)
      .toolbarConfiguration(\[
        {
          // Replace $r("app.string.navigation\_toolbar\_add") and $r("app.media.startIcon") with the image resource file you use.
          value: $r("app.string.navigation\_toolbar\_add"),
          icon: $r("app.media.startIcon")
        },
        {
          // Replace $r("app.string.navigation\_toolbar\_app") and $r("app.media.startIcon") with the image resource file you use.
          value: $r("app.string.navigation\_toolbar\_app"),
          icon: $r("app.media.startIcon")
        },
        {
          // Replace $r("app.string.navigation\_toolbar\_collect") and $r("app.media.startIcon") with the image resource file you use.
          value: $r("app.string.navigation\_toolbar\_collect"),
          icon: $r("app.media.startIcon")
        }
      \])
      .mode(NavigationMode.Split) // Set the navigation mode to Split.
      .navBarWidthRange(\[this.minNavBarWidth, this.maxNavBarWidth\]) // Set the navigation page width range: \[minimum width, maximum width\].
      .minContentWidth(this.minContentWidth)
      .hideTitleBar(false)
      .hideToolBar(false)
      .onTitleModeChange((titleModel: NavigationTitleMode) => {
        console.info('titleMode' + titleModel)
      })
      .splitPlaceholder(this.placeholder)
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/CiDnS3e9TpW9X36tpONdZQ/en-us_image_0000002537765572.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7866CD151CD26FFF9640C2B9976A54EBF0D613CB4C309175639B2C4A344FFE83)

## Example 15: Enabling and Disabling Navigation Toolbar Adaptation

This example demonstrates how to enable and disable the toolbar adaptation capability of **Navigation**.

In the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file, set **orientation** to **landscape** in the **abilities** field. (This configuration is used only to demonstrate the toolbar adaptation capability of **Navigation** in landscape mode. You can set orientation to **auto\_rotation** as required.)

import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct NavigationExample {
  @Provide('navPathStack') navPathStack:NavPathStack = new NavPathStack();
  @State enable: boolean = false
  @State menuItems:Array<NavigationMenuItem> = \[
    {
      value:'menuItem1',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.card\_writer')),
    },
    {
      value:'menuItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus'))
    },
    {
      value:'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
    },
  \]

  @State toolItems:Array<ToolbarItem> = \[
    {
      value:'toolItem1',
      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
      action:()=>{}
    },
    {
      value:'toolItem2',
      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.card\_migration')),
      action:()=>{}
    },
    {
      value:'toolItem3',
      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos\_star')),
      action:()=>{}
    }
  \]

  build() {
    Navigation(this.navPathStack) {
      Column() {
        Button('Enable/Disable Adaptation').onClick(()=> {
          this.enable = !this.enable;
        })
        Text("Toolbar adaptation enabled:" + this.enable)
      }
    }
    .mode(NavigationMode.Stack)
    .enableToolBarAdaptation(this.enable) // Specify whether to enable toolbar adaptation.
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi')))
    .titleMode(NavigationTitleMode.Mini)
    .menus(this.menuItems)
    .toolbarConfiguration(this.toolItems)
    .title('Level-1 page')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/ZNe8_oC4R-KGW5bSh2fGVA/en-us_image_0000002537925512.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BDC71D5812F7C50956745F6B1EE6310A9817CBFFFF836D96D5CB427FDD413A3)

## Example 16: Using NavDestination as a Navigation Page in Navigation

This example demonstrates that **Navigation** can use [NavDestination](../navdestination/document.md) as the navigation page (home page).

@Component
struct PageHome {
  private stack: NavPathStack | undefined = undefined;

  build() {
    NavDestination() {
      Stack({alignContent: Alignment.Center}) {
        Button('push PageOne').onClick(() => {
          this.stack?.pushPath({name: 'PageOne'});
        })
      }.width('100%').height('100%')
    }.title('PageHome')
    .onReady((ctx: NavDestinationContext) => {
      this.stack = ctx.pathStack;
    })
  }
}

@Builder
function PageHomeBuilder() {
  PageHome()
}

@Component
struct PageOne {
  build() {
    NavDestination() {
      Stack({alignContent: Alignment.Center}) {
        Text('PageOne')
      }.width('100%').height('100%')
    }.title('PageOne')
  }
}

@Builder
function PageOneBuilder() {
  PageOne()
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  build() {
    // Configure home page NavDestination information here.
    Navigation(this.stack, { name: 'PageHome' }) {
    }
    .width('100%').height('100%')
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. The following is an example of **router\_map.json**:

{
  "routerMap": \[
    {
      "name": "PageHome",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageHomeBuilder",
      "data": {
        "description": "this is PageHome"
      }
    },
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is PageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/qkhwsMNYQlaXWT6l9zPPRg/en-us_image_0000002568685289.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=668B89A8029B0E3AD741DDDF1F94DCC2624D98AC5A1B6CD492BF5AD2FF0408B8)

## Example 17: Using New Navigation Controller APIs

This example demonstrates how to implement route interception by setting the [setInterception](#setinterception12) method and obtain **mode** using the [NavDestinationContext](../navdestination/document.md#navdestinationcontext11) object.

The **interception** API is added to the [NavigationInterception](#navigationinterception12) parameter type of **setInterception** since API version 22.

// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfos: NavPathStack = new NavPathStack();
  isUseInterception: boolean = false;

  registerInterception() {
    this.pageInfos.setInterception({
      // Intercept navigation behavior before page creation. Stack operations take effect for the current navigation process.
      interception: (from: NavPathInfo | "navBar", to: NavPathInfo | NavBar, navStack: NavPathStack,
        operation: NavigationOperation, animated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof to === "string") {
          return;
        }
        // Redirect the target page from pageTwo to pageOne.
        let target: NavPathInfo = to as NavPathInfo;
        let navStacktarget: NavPathStack = navStack as NavPathStack;
        if (target.name === 'pageTwo') {
          navStacktarget.pop();
          navStacktarget.pushPathByName('pageOne', null);
        }
      },
      // Callback invoked after the page is navigated. Stack operations in this callback are effective in the next navigation.
      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
        operation: NavigationOperation, isAnimated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof from === "string") {
          console.info("current transition is from navigation home");
        } else {
          console.info(\`current transition is from  ${(from as NavDestinationContext).pathInfo.name}\`);
          console.info(\`current transition mode is to ${(to as NavDestinationContext).mode?.toString()}\`);
        }
        if (typeof to === "string") {
          console.info("current transition to is navBar");
        } else {
          console.info(\`current transition is to ${(to as NavDestinationContext).pathInfo.name}\`);
          console.info(\`current transition mode is to ${(to as NavDestinationContext).mode?.toString()}\`);
        }
      },
      // Callback invoked when the display mode of the Navigation component switches between single-column and split-column.
      modeChange: (mode: NavigationMode) => {
        if (!this.isUseInterception) {
          return;
        }
        console.info(\`current navigation mode is ${mode}\`);
      }
    })
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' }); // Push the navigation destination page specified by name to the navigation stack.
          })
        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.isUseInterception = !this.isUseInterception;
            if (this.isUseInterception) {
              this.registerInterception();
            } else {
              this.pageInfos.setInterception(undefined);
            }
          })
      }
    }.title('NavIndex')
  }
}

// PageOne.ets
class TmpClass {
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfos.pushPathByName('pageTwo', tmp); // Push the navigation destination page specified by name, with the data specified by param, to the routing stack.
          })
        Button('singletonLaunchMode', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' },
              { launchMode: LaunchMode.MOVE\_TO\_TOP\_SINGLETON }); // Search from the bottom to the top of the stack. If the page with the specified name exists, move that page to the top of the stack.
          })
        Button('popToname', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToName('pageTwo'); // Pop the first navigation destination page that matches the value of name to the top of the routing stack.
            console.info('popToName' + JSON.stringify(this.pageInfos),
              'Return value' + JSON.stringify(this.pageInfos.popToName('pageTwo')));
          })
        Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToIndex(1); // Return the routing stack to the navigation destination page that matches the value of index.
            console.info('popToIndex' + JSON.stringify(this.pageInfos));
          })
        Button('moveToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveToTop('pageTwo'); // Move to the top of the routing stack the first navigation destination page that matches the value of name.
            console.info('moveToTop' + JSON.stringify(this.pageInfos),
              'Return value' + JSON.stringify(this.pageInfos.moveToTop('pageTwo')));
          })
        Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveIndexToTop(1); // Move to the top of the routing stack the navigation destination page that matches the value of index.
            console.info('moveIndexToTop' + JSON.stringify(this.pageInfos));
          })
        Button('clear', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.clear(); // Clear the routing stack.
          })
        Button('get', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            console.info('-------------------');
            console.info('Obtain names of all NavDestination pages in the stack', JSON.stringify(this.pageInfos.getAllPathName()));
            console.info('Obtain parameter information of the NavDestination page at the specified index',
              JSON.stringify(this.pageInfos.getParamByIndex(1)));
            console.info('Obtain the parameter information of all NavDestination pages with the specified name',
              JSON.stringify(this.pageInfos.getParamByName('pageTwo')));
            console.info('Obtain the position indexes of all NavDestination pages with the specified name',
              JSON.stringify(this.pageInfos.getIndexByName('pageOne')));
            console.info('Obtain the stack size', JSON.stringify(this.pageInfos.size()));
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      const popDestinationInfo = this.pageInfos.pop(); // Pop the top element out of the routing stack.
      console.info('pop' + 'return value' + JSON.stringify(popDestinationInfo));
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
  }
}

// PageTwo.ets
@Builder
export function PageTwoBuilder(name: string, param: Object) {
  PageTwo()
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();
  private menuItems: Array<NavigationMenuItem> = \[
    {
      value: "1",
      icon: 'resources/base/media/undo.svg',
    },
    {
      value: "2",
      icon: 'resources/base/media/redo.svg',
      isEnabled: false,
    },
    {
      value: "3",
      icon: 'resources/base/media/ic\_public\_ok.svg',
      isEnabled: true,
    }
  \];

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pushPathByName('pageOne', null);
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .menus(this.menuItems)
    .onBackPressed(() => {
      this.pathStack.pop();
      return true;
    })
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
      console.info("current page config info is " + JSON.stringify(context.getConfigInRouteMap()));
    })
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the project configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory.

// src/main/resources/base/profile/router\_map.json
{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/4FwFCgJSRt69-dRCtsMi-g/en-us_image_0000002568765299.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=071B2BCF6487CAAB8B4339F4ACBF1AF62103322A06CEBB93D4CF758E517072E6)

## Example 18: Setting Navigation as Recoverable

This example demonstrates how to set **Navigation** as recoverable by using the [recoverable](#recoverable14) API. You need to enable the [UIAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) backup and restore function during module initialization. For details, see [UIAbility Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-recover-guideline).

The recoverable API is supported since API version 14.

// Index.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct NavigationExample {
  navPathStack: NavPathStack = new NavPathStack();
  @State menuItems: Array<NavigationMenuItem> = \[
    {
      // Replace 'resources/base/media/startIcon.png' with the resource file you use.
      value: 'menuItem1',
      icon: 'resources/base/media/startIcon.png' // Icon resource path.
    },
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: 'menuItem2',
      icon: 'resources/base/media/ic\_public\_ok.svg', // Icon resource path.
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus')).fontColor(\[Color.Red, Color.Green\])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR),
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
    },
  \];
  @State toolItems: Array<ToolbarItem> = \[
    {
      // Replace 'resources/base/media/ic\_public\_ok.svg' with the image resource file you use.
      value: 'toolItem1',
      icon: 'resources/base/media/ic\_public\_ok.svg', // Icon resource path.
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus')).fontColor(\[Color.Red,
        Color.Green\]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR),
      action: () => {
      }
    },
    {
      // Replace 'resources/base/media/startIcon.png' with the resource file you use.
      value: 'toolItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeIcon: 'resources/base/media/startIcon.png', // Icon resource path.
      action: () => {
      }
    },
    {
      value: 'toolItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')),
      action: () => {
      }
    }
  \];

  build() {
    Navigation(this.navPathStack) {
      Column() {
        Button('Go').onClick(() => {
          this.navPathStack.pushPathByName('NavigationMenu', null);
        })
      }
    }
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi')))
    .titleMode(NavigationTitleMode.Mini)
    .menus(this.menuItems)
    .toolbarConfiguration(this.toolItems)
    .title('Level-1 page')
    .id('test')
    .recoverable(true)
  }
}

// PageOne.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Builder
export function myRouter(name: string, param?: Object) {
  NavigationMenu();
}

@Component
export struct NavigationMenu {
  navPathStack: NavPathStack = new NavPathStack();
  @State menuItems: Array<NavigationMenuItem> = \[
    {
      // Replace 'resources/base/media/startIcon.png' with the resource file you use.
      value: 'menuItem1',
      icon: 'resources/base/media/startIcon.png', // Icon resource path.
      action: () => {
      }
    },
    {
      value: 'menuItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus')).fontColor(\[Color.Red, Color.Green\])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR),
      action: () => {
      }
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat\_1')),
      action: () => {
      }
    },
  \];

  build() {
    NavDestination() {
      Row() {
        Column() {
        }
        .width('100%')
      }
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.navPathStack = context.pathStack;
    })
    .hideTitleBar(false)
    .title('NavDestination title')
    .backgroundColor($r('sys.color.ohos\_id\_color\_titlebar\_sub\_bg'))
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos\_star'))
    .fontColor(\[Color.Blue\]))
    .menus(this.menuItems)
    .recoverable(true)
  }
}

Configure **"routerMap": "$profile:router\_map"** in the **module** field of the configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, and add the **router\_map.json** file to the **src/main/resources/base/profile** directory. Example:

{
  "routerMap": \[
    {
      "name": "NavigationMenu",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "myRouter",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/oez2ypg6Rca57QpCOp4a7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE9387B713434B04BAE52A810560BAD8199F81E8A913A996C889AAFF71BCC9AB)

To simulate the scenario where a process exits unexpectedly and is cold started again, perform the following steps:

1.  After the project is successfully executed, click the jump button.
    
2.  Swipe up the app to return to the background and open the CLI.
    
3.  Run **hdc shell**, and then run **pidof \[/topic/body/section/note/ol/li/p/b/package\_name {""}) (package\_name\]** to query the value of **pid**.
    
4.  Run the **aa force-stop Project name -p Value of pid -r RESOURCE\_CONTROL** command to simulate the scenario where the app exits due to improper resource usage.
    
5.  Click the application. The displayed page is still the page after the jump button is clicked.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/rjSj2d_7T_OPIG4f_onEEg/en-us_image_0000002537765574.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5C00E08BCD95EE073D57AADDD21F7EA5FA55963CC08A68CB1A41C54799F92CC)
