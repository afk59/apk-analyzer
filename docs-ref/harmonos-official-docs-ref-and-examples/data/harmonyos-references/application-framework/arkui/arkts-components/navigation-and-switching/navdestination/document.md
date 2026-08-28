# NavDestination

**NavDestination** is the root container of a destination page and represents the content area of the [Navigation](../navigation/document.md) component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/21WORpUfRau0zstWqjNQHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95BA489A808AAFC59F48E26250B3EEE56FCEFB2FAB78DBB95C67FF7B01E3BA96)

-   This component is supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Since API version 11, this component supports the safe area attribute by default, with the default attribute value being **expandSafeArea(\[SafeAreaType.SYSTEM\], \[SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM\])**. You can override this attribute to change the default behavior. In earlier versions, you need to use the [expandSafeArea](../../universal-attributes/layout-and-borders/safe-area/document.md) attribute to implement the safe area feature.
    
-   The **NavDestination** component must be used in conjunction with the **Navigation** component to act as the root node for the navigation destination page. When used alone, it can only function as a standard container component and does not possess any routing-related attributes or capabilities.
    
-   If the lifecycle of an intermediate page in the routing stack changes, the lifecycle callbacks (**onWillShow**, **onShown**, **onHidden**, **onWillDisappear**) of the top **NavDestination** in the stack both before and after the navigation will be triggered last in the sequence.
    
-   If no main title or subtitle is set for **NavDestination** and there is no back button, the title bar is not displayed.
    
-   Avoid setting layout-related attributes such as the position and size. They may result in display issues on the page. For example, do not apply the [zIndex](../../universal-attributes/basic-attributes/z-order-control/document.md#zindex) attribute to a **NavDestination** component. This will override the system-defined stacking order and may cause display anomalies.
    

#### Child Components

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/3O1Nto7RSra5JHRjRQUpKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B63179461638938902E3FFB42ABC62491EE70D869618AF46057324AC7E8E0CA)

-   Allowed child component types: built-in and custom components, including rendering control types ([if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), and [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)).
-   Number of child components: multiple.

#### APIs

NavDestination()

Creates the root container for a subpage in [Navigation](../navigation/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are supported.

#### \[h2\]title

title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource, options?: NavigationTitleOptions)

Sets the page title. When the title string is too long: (1) if no subtitle is set, the string is scaled down, wrapped in two lines, and then clipped with an ellipsis (...); (2) if a subtitle is set, the title string is scaled down and then clipped with an ellipsis (...).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/QhgJa4ViRyy8swp2glOlsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFD0331B60A183FE6F6A49E5B1B2C7E977C187EC6EA07D9E4BDB776F1E6C1816)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | [NavDestinationCommonTitle](#navdestinationcommontitle) | [NavDestinationCustomTitle](#navdestinationcustomtitle) | [Resource14+](../../common-definitions/basic-types/document.md#resource) | Yes | Page title. |
| options12+ | [NavigationTitleOptions](../navigation/document.md#navigationtitleoptions11) | No | Title bar options. |

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

Default value: **false**

**true**: Hide the title bar.

**false**: Show the title bar.

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

Default value: **false**

**true**: Hide the title bar.

**false**: Show the title bar.

 |
| animated | boolean | Yes | 

Whether to animate the visibility change of the title bar.

Default value: **false**

**true**: Animate the visibility change of the title bar.

**false**: Do not animate the visibility change of the title bar.

 |

#### \[h2\]toolbarConfiguration13+

toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

Sets the content of the toolbar. If this API is not called, the toolbar remains hidden.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/WeleKbrfSgCGO7iFkg1peA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C03F8DEAB12F6506DAF846D79FB1EB6791A012AACB857C80D5C0D7276889E6E)

-   This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.
    
-   The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.
    

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| toolbarParam | Array<[ToolbarItem](../navigation/document.md#toolbaritem10)\> | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | 
Content of the toolbar.

When configured with Array<[ToolbarItem](../navigation/document.md#toolbaritem10)\>, the toolbar follows the rules below:

\- Toolbar items are evenly distributed on the bottom toolbar, with text and icons evenly spaced in each content area.

\- In portrait mode, the toolbar shows a maximum of five icons, with any additional icons placed under an automatically generated **More** icon. In landscape mode, the behavior of the toolbar is determined by the display mode: (1) If the display mode is [Split](../navigation/document.md#navigationmode9), the display will remain the same as in portrait mode. (2) If the display mode is [Stack](../navigation/document.md#navigationmode9), the toolbar must be used together with Array<[NavigationMenuItem](../navigation/document.md#navigationmenuitem)\> of the [menus](#menus12) attribute; in this configuration, the bottom toolbar is automatically hidden, and all items on the toolbar are relocated to the menu in the upper right corner of the screen.

When configured with [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8), the toolbar does not follow the above rules.

 |
| options | [NavigationToolbarOptions](../navigation/document.md#navigationtoolbaroptions11) | No | Toolbar options. Toolbar options include the background color, background blur style and blur option, background properties, and layout mode of the toolbar, as well as whether to hide the toolbar text, and options for the toolbar's more button menu. |

#### \[h2\]hideToolBar13+

hideToolBar(hide: boolean, animated?: boolean)

Specifies whether to hide the toolbar.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hide | boolean | Yes | 
Whether to hide the toolbar.

Default value: **false**

**true**: Hide the toolbar.

**false**: Show the toolbar.

 |
| animated | boolean | No | 

Whether to animate the visibility change of the toolbar.

Default value: **false**

**true**: Animate the visibility change of the toolbar.

**false**: Do not animate the visibility change of the toolbar.

 |

#### \[h2\]mode11+

mode(value: NavDestinationMode)

Sets the mode of the **NavDestination** component. Dynamic modification is not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/rjbUg-FHRSGWmawvGRvrJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B66DFA1A16E72B0DBB432ED1E71DF9E95E7DFFED37C897AA0AD0469ABA426302)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NavDestinationMode](#navdestinationmode11) | Yes | 
Mode of the **NavDestination** component.

Default value: **NavDestinationMode.STANDARD**

 |

#### \[h2\]backButtonIcon11+

backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier)

Sets the icon of the back button on the title bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/CZ9ttjeuQOer5e0ovvFIBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=004E64EECAA26844DC02C772DED7F5DDE893F63A94953F6F959095CC1F4BD616)

-   This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.
    
-   The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [SymbolGlyphModifier12+](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | Yes | Icon of the back button on the title bar. |

#### \[h2\]backButtonIcon19+

backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier, accessibilityText?: ResourceStr)

Sets the icon and accessibility text for the back button on the title bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/ToaM1DBZRJWvKTVEv-UhvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E169A13C885BFA9C3DEEDA08F37DA5ADE6B273646900312A02BAAE4702F2F78D)

-   This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    
-   The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.
    

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | Yes | Icon of the back button on the title bar. |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | 
Accessibility text for the back button.

Default value: **back** when the system language is English.

 |

#### \[h2\]menus12+

menus(value: Array<NavigationMenuItem> | CustomBuilder)

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. When the value type is Array<[NavigationMenuItem](../navigation/document.md#navigationmenuitem)\>, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/DmZG3a6mSy-MM98GgcaANQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A42EB68835643F86CCE7479B99BF445E91323DDBAC5D5FF523F0A990DC2C0657)

-   This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 14.
    
-   The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[NavigationMenuItem](../navigation/document.md#navigationmenuitem)\> | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Menu items in the upper right corner of the page. |

#### \[h2\]menus19+

menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. Compared with [menus](#menus12), this API adds menu options. When the value type is Array<[NavigationMenuItem](../navigation/document.md#navigationmenuitem)\>, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/CLxmbo6OS_G0Zl1dGSqqkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D665E0E6718A3AD0190338A71BD1DBE91633349D5794CA5C25C9B43312A28A2)

-   This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    
-   The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or changing the animation effect type through the **symbolEffect** attribute.
    

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | Array<[NavigationMenuItem](../navigation/document.md#navigationmenuitem)\> | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Menu items in the upper right corner of the page. |
| options | [NavigationMenuOptions](../navigation/document.md#navigationmenuoptions19) | No | Optional settings for menu items in the upper right corner of the page. |

#### \[h2\]ignoreLayoutSafeArea12+

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

Ignores the layout safe area by allowing the component to extend into the non-safe areas of the screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/U04hoXXUT2yqU9Bh1PQeYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC10454B5BC0229DD815EE8B0F75D8ADFDCE8EFD07F2F46A626F02043376BCC4)

-   Prerequisites for the **ignoreLayoutSafeArea** attribute to take effect:
    
    When **LayoutSafeAreaType.SYSTEM** is set, the component can extend into the non-safe area if its boundaries overlap with the non-safe area.
    
-   If the component extends into the non-safe area, events triggered within that area (such as click events) might be intercepted by the system. This allows the system to prioritize responses to system components such as the status bar.
    
-   To allow a component to extend into non-safe areas, the title bar and toolbar must be hidden or set to [STACK](../navigation/document.md#barstyle12) mode.
    

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

Sets the style of the system status bar when this **NavDestination** page is displayed in the **Navigation** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/QgjYOQhARB2ZbqkhlWWpjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DAAEDA6C1752C35DDE552A18AC1F5240C0FB504542F86E19B974DF345300F0B)

-   The setting takes effect only when the **NavDestination** component is used in conjunction with the **Navigation** component.
    
-   For other usage restrictions, see the description of [systemBarStyle](../navigation/document.md#systembarstyle12) for the **Navigation** component.
    
-   This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[SystemBarStyle](../../../arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#systembarstyle12)\> | Yes | Style of the system status bar. |

#### \[h2\]systemTransition14+

systemTransition(type: NavigationSystemTransitionType)

Sets the system transition animation of the **NavDestination** component. System transition animations for the title bar and content area can be configured separately.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [NavigationSystemTransitionType](#navigationsystemtransitiontype14) | Yes | 
Type of the system transition animation.

Default value: **NavigationSystemTransitionType.DEFAULT**

 |

#### \[h2\]recoverable14+

recoverable(recoverable: Optional<boolean>)

Sets whether the **NavDestination** component is recoverable. If set to recoverable, when the application process exits unexpectedly and restarts, the **NavDestination** component will be automatically re-created. To use this feature, ensure that the [recoverable](../navigation/document.md#recoverable14) attribute is set for the **Navigation** component associated with the **NavDestination** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/CDzHH27zR6yo_VGhgTBXnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A41BB346D86B40C244D8589889646F7CF7790BEAC0BA4397D8CEDD72E619233)

This API must be used together with the [recoverable](../navigation/document.md#recoverable14) API of **Navigation**.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recoverable | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether the **NavDestination** component is recoverable. By default, it is not recoverable.

Default value: **false**

**true**: The **NavDestination** component is recoverable.

**false**: The **NavDestination** component is not recoverable.

 |

#### \[h2\]bindToScrollable14+

bindToScrollable(scrollers: Array<Scroller>)

Binds the **NavDestination** component with a scrollable container, which can be a [List](../../scroll-and-swipe/list/document.md), [Scroll](../../scroll-and-swipe/scroll/document.md), [Grid](../../scroll-and-swipe/grid/document.md), or [WaterFlow](../../scroll-and-swipe/waterflow/document.md) component. This way, scrolling in the scrollable container triggers the display and hide animations of the title bar and toolbar of all **NavDestination** components that are bound to it – scrolling up triggers the hide animation, and scrolling down triggers the show animation. A single **NavDestination** component can be bound to multiple scrollable containers, and a single scrollable container can be bound to multiple **NavDestination** components. For details, see [Example 1](#example-1-linking-the-title-bar-and-toolbar-with-scrollable-components).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/EksfpIaJSqq8W6szs_kuYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4919777C532F52977D51456C658A22D4EF42723C73CD317A4171C55102B5D33)

-   The connection between the scrolling actions and the animations for showing or hiding the title bar and toolbar of the **NavDestination** component takes effect only when the title bar or toolbar is visible.
    
-   If a **NavDestination** component is bound to multiple scrollable containers, scrolling in any of these containers triggers the display or hiding animations of the title bar and toolbar. Specifically, when any scrollable container reaches either the bottom or the top, the display animation for the title bar and toolbar is triggered without delay. As such, to ensure the optimal user experience, avoid triggering scroll events of multiple scrollable containers simultaneously.
    
-   This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 22.
    

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scrollers | Array<[Scroller](../../scroll-and-swipe/scroll/document.md#scroller)\> | Yes | Controller of the target scrollable container. |

#### \[h2\]bindToNestedScrollable14+

bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo>)

Binds the **NavDestination** component with a nested scrollable container, which can be a [List](../../scroll-and-swipe/list/document.md), [Scroll](../../scroll-and-swipe/scroll/document.md), [Grid](../../scroll-and-swipe/grid/document.md), or [WaterFlow](../../scroll-and-swipe/waterflow/document.md) component. This way, scrolling in the scrollable container triggers the display and hide animations of the title bar and toolbar of all **NavDestination** components that are bound to it – scrolling up triggers the hide animation, and scrolling down triggers the show animation. A single **NavDestination** component can be bound to multiple nested scrollable containers, and a single nested scrollable container can be bound to multiple **NavDestination** components. For details, see [Example 1](#example-1-linking-the-title-bar-and-toolbar-with-scrollable-components).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/jBsUNkE3Q0mutXjs3HU9-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8854DFEE14F5434640A93EA7CBD907A78D2ED08BD8206CC498EEC66546880FDA)

-   The connection between the scrolling actions and the animations for showing or hiding the title bar and toolbar of the **NavDestination** component takes effect only when the title bar or toolbar is visible.
    
-   If a **NavDestination** component is bound to multiple scrollable containers, scrolling in any of these containers triggers the display or hiding animations of the title bar and toolbar. Specifically, when any scrollable container reaches either the bottom or the top, the display animation for the title bar and toolbar is triggered without delay. As such, to ensure the optimal user experience, avoid triggering scroll events of multiple scrollable containers simultaneously.
    
-   This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 22.
    

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scrollInfos | Array<[NestedScrollInfo](#nestedscrollinfo14)\> | Yes | Controller of the target nested scrollable containers. |

#### \[h2\]hideBackButton15+

hideBackButton(hide: Optional<boolean>)

Sets whether to hide the back button in the title bar.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hide | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to hide the back button in the title bar.

Default value: **false**

**true**: Hide the back button in the title bar.

**false**: Show the back button in the title bar.

 |

#### \[h2\]customTransition15+

customTransition(delegate: NavDestinationTransitionDelegate)

Sets a custom transition animation for the **NavDestination** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/jognRKjWSd-bz7pbCw6O_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5E06E74FC0D9FDB0365068D0DD762B50F7AC2E4FB4AA1399BCC5B6004EF3ED0)

-   This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    
-   If both this attribute and [systemTransition](#systemtransition14) are set, whichever is set later takes effect.
    

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| delegate | [NavDestinationTransitionDelegate](#navdestinationtransitiondelegate15) | Yes | Delegate function for custom animations of the **NavDestination** component. |

#### \[h2\]preferredOrientation19+

preferredOrientation(orientation: Optional<Orientation>)

Sets the display orientation for the **NavDestination** component. After the transition to the NavDestination, the system also switches the application's main window to the specified display orientation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/6C1VwX0oTzGlhKLgLEkWtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDBE6BC5F5ED9CF543725CF11A4BD72F806A56CFFF6E77ECE7B62B972F9DC680)

-   This attribute is effective only if the following conditions are all met:
    
    1.  The **NavDestination** component belongs to the application's main window page, and the main window is a full-screen window.
    2.  The **Navigation** container containing the **NavDestination** component occupies the entire application page area.
    3.  The type of **NavDestination** is [NavDestinationMode](#navdestinationmode11).STANDARD.
-   The actual effect of setting the display orientation depends on the specific device support. For details, see [setPreferredOrientation](../../../arkts-api/window-manager/ohos-window-window/interface-window/document.md#setpreferredorientation9-1).
    

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| orientation | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Orientation](#orientation19)\> | Yes | Display orientation to set. |

#### \[h2\]enableStatusBar19+

enableStatusBar(enabled: Optional<boolean>, animated?: boolean)

Sets whether to show or hide the system status bar when entering this **NavDestination** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/X6XBtDZ7QDKVxMaBvBSIwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0ABF507AF9A2B468AA94002B0E9E0A4317FED496511C4134932E7C31E4CB609D)

-   This attribute is effective only if the following conditions are all met:
    
    1.  The **NavDestination** component belongs to the application's main window page, and the main window is a full-screen window.
    2.  The **Navigation** container containing the **NavDestination** component occupies the entire page area.
    3.  The **NavDestination** component occupies the entire **Navigation** container.
    4.  The type of **NavDestination** is [NavDestinationMode](#navdestinationmode11).STANDARD.
-   The actual effect of setting the system status bar depends on the specific device support. For details, see [setSpecificSystemBarEnabled](../../../arkts-api/window-manager/ohos-window-window/interface-window/document.md#setspecificsystembarenabled11).
    

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to show or hide the system status bar when entering the current **NavDestination** component.

**true**: Show the system status bar.

**false**: Hide the system status bar.

 |
| animated | boolean | No | 

Whether to animate the visibility change of the system status bar. Default value: **false**.

**true**: Animate the visibility change of the system status bar.

**false**: Do not animate the visibility change of the system status bar.

 |

#### \[h2\]enableNavigationIndicator19+

enableNavigationIndicator(enabled: Optional<boolean>)

Sets whether to show or hide the system navigation bar when entering this **NavDestination** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/5rpYMPneSh6JLYhnFguJFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9873C9F721B85644F455526E747857F9DBF58AEEA1E2598F6F21EC4F30A089AE)

This attribute is effective only if the following conditions are all met:

1.  The **NavDestination** component belongs to the application's main window page, and the main window is a full-screen window.
2.  The **Navigation** container containing the **NavDestination** component occupies the entire page area.
3.  The **NavDestination** component occupies the entire **Navigation** container.
4.  The type of **NavDestination** is [NavDestinationMode](#navdestinationmode11).STANDARD.

The actual effect of setting the system navigation bar depends on the specific device support. For details, see [setSpecificSystemBarEnabled](../../../arkts-api/window-manager/ohos-window-window/interface-window/document.md#setspecificsystembarenabled11).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to show or hide the system navigation bar when entering the current **NavDestination** component.

**true**: Show the system navigation bar.

**false**: Hide the system navigation bar.

 |

#### NavDestinationMode11+

Mode of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| STANDARD | 0 | Standard mode. |
| DIALOG | 1 | 
The navigation destination is transparent by default. Stack operations do not affect the visibility of underlying **NavDestination** components (lifecycle methods like **onShown** and **onHidden** remain unchanged). Only the **onActive** and **onInactive** lifecycle methods are triggered.

Before API version 13, no system transition animation is available by default. System transition animations are supported since API version 13.

 |

#### NavigationSystemTransitionType14+

Type of the system transition animation.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | 
Default system transition animation.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| NONE | 1 | 

No system transition animation.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| TITLE | 2 | 

System transition animation of the title bar.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| CONTENT | 3 | 

System transition animation of the content area.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| FADE15+ | 4 | 

Fade-type system transition animation.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| EXPLODE15+ | 5 | 

Center-scale type system transition animation.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| SLIDE\_RIGHT15+ | 6 | 

Right-slide type system transition animation.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| SLIDE\_BOTTOM15+ | 7 | 

Bottom-slide type system transition animation.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/xRY2KCimQkeGnD99bMZ4fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1DB978C30E28902E0958C2C440AACC290D53279751588C0E75E195E7B510CEA)

System transition animations for the title bar and content area can be configured separately.

The system transition animation of the title bar is only available for the push and pop animations of navigation destination pages in STANDARD mode, with the following constraints:

1.  When **NavigationSystemTransitionType** is set to **TITLE**, only the system transition animation of the title bar is displayed.
2.  When **NavigationSystemTransitionType** is set to **CONTENT**, only the system transition animation of the content area is displayed.

When **NONE** or **TITLE** is set, no system transition animation is displayed. When **CONTENT** or **DEFAULT** is set, the system transition animation is displayed by default.

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onShown10+

onShown(callback: Callback<VisibilityChangeReason>)

Triggered when the navigation destination page is displayed. Starting from API version 21, the callback includes a **VisibilityChangeReason** parameter indicating the cause of the visibility change.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[VisibilityChangeReason](#visibilitychangereason21)\>21+ | Yes | 
Triggered when the navigation destination page is displayed.

In versions earlier than API version 21, the callback is a basic callback without parameters.

Since API version 21, the callback includes a **VisibilityChangeReason** parameter describing the trigger cause.

 |

#### \[h2\]onHidden10+

onHidden(callback: Callback<VisibilityChangeReason>)

Triggered when the navigation destination page is hidden. Starting from API version 21, the callback includes a **VisibilityChangeReason** parameter indicating the cause of the visibility change.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[VisibilityChangeReason](#visibilitychangereason21)\>21+ | Yes | 
Triggered when the navigation destination page is hidden.

In versions earlier than API version 21, the callback is a basic callback without parameters.

Since API version 21, the callback includes a **VisibilityChangeReason** parameter describing the trigger cause.

 |

#### \[h2\]onWillAppear12+

onWillAppear(callback: Callback<void>)

Called when the **NavDestination** component is about to be mounted. The routing stack can be modified in the callback, and the modification takes effect in the current frame.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/uvliLS8MQqeIBs8TRURBkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=811E414BA2B31046058773B7A96BE00DEBBFFC465F6652C921F08D1A131901D6)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | Yes | Called when the **NavDestination** component is about to be mounted. The routing stack can be modified in the callback, and the modification takes effect in the current frame. |

#### \[h2\]onWillShow12+

onWillShow(callback: Callback<void>)

Called when the **NavDestination** component is about to display.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/bsenahlaTtuxQUbDIymYQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22780727B3A577BE1E41B803F3BA04B7CF844762BA04E2CBFCFCF5AF1C46FD03)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | Yes | Called when the **NavDestination** component is about to display. |

#### \[h2\]onWillHide12+

onWillHide(callback: Callback<void>)

Called when the **NavDestination** component is about to be hidden.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/gbQViUobRKmTEFd4Cbjsmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD94B0505DEEAD10301FBABAC08C16219A98BAF8466CEAD51220C35970478715)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | Yes | Called when the **NavDestination** component is about to be hidden. |

#### \[h2\]onWillDisappear12+

onWillDisappear(callback: Callback<void>)

Called when the the **NavDestination** component is about to be unmounted (or when the transition animation, if any, is about to start).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/tmi0hxyTRYyoqhQI4PDADQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=796072DFC9363C56435706E84A08D8F0D36A6E71F4A81E25CF2493296DD23A79)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | Yes | Called when the the **NavDestination** component is about to be unmounted (or when the transition animation, if any, is about to start). |

#### \[h2\]onBackPressed10+

onBackPressed(callback: () => boolean)

This callback takes effect when content exists in the navigation controller bound to the **Navigation** component. Triggered when the back button is pressed.

The value **true** means that the back button logic is overridden, and **false** means that the previous page is displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => boolean | Yes | This callback takes effect when content exists in the navigation controller bound to the **Navigation** component. Triggered when the back button is pressed. |

#### \[h2\]onReady11+

onReady(callback: [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[NavDestinationContext](#navdestinationcontext11)\>)

Triggered when the **NavDestination** component is about to build a child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/wShz-b0FR1C4_QsWUPOfKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE25A47FDC555470FA5C75549A690231A89E88D86B00A3870DC8B19FCD2B3DB8)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[NavDestinationContext](#navdestinationcontext11)\> | Yes | Triggered when the **NavDestination** component is about to build a child component. |

#### \[h2\]onResult15+

onResult(callback: Optional<Callback<ESObject>>)

Triggered when the **NavDestination** component returns.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/skXpli6gR8e5oECpJwGBiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=537EA412D6B74F53CCC98ECD9D94C0159FDAFA37B7F3E3A60E5E27BC632163DE)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<ESObject>> | Yes | Callback for page returning, with the parameter being the **result** parameter passed by the [pop](../navigation/document.md#pop11), [popToName](../navigation/document.md#poptoname11), or [popToIndex](../navigation/document.md#poptoindex11) API. If this parameter is not passed, the input is **undefined**. |

#### \[h2\]onActive17+

onActive(callback: Optional<Callback<NavDestinationActiveReason>>)

Triggered when the **NavDestination** component becomes active (on top of the stack and operable, with no special components blocking it). For details, see [Example 5](#example-5-handling-navdestination-onactive-and-oninactive-lifecycle-events).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/4F6BgSEzTwOYDz7x96wYgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36505339F4A75C2EDD0FC3C54A9192F7AFCCF335F513FCC95E9F99DBAEB13AD6)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[NavDestinationActiveReason](#navdestinationactivereason17)\>> | Yes | Reason why the **NavDestination** component switches from inactive to active. |

#### \[h2\]onInactive17+

onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)

Triggered when the **NavDestination** component becomes inactive (not on top of the stack and inoperable, or on top but blocked by special components). For details, see [Example 5](#example-5-handling-navdestination-onactive-and-oninactive-lifecycle-events).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/cQ6sLWvwSFSc2c0LzWmCdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A240901F4835B0A7ED9489FB3CBFFFFFC6AF8D6469684CBDC9BAE2FDAC1F3E7)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[NavDestinationActiveReason](#navdestinationactivereason17)\>> | Yes | Reason why the **NavDestination** component switches from active to inactive. |

#### \[h2\]onNewParam19+

onNewParam(callback: Optional<Callback<ESObject>>)

Triggered when a **NavDestination** page that already exists in the stack is moved to the top using [launchMode.MOVE\_TO\_TOP\_SINGLETON](../navigation/document.md#launchmode12) or [launchMode.POP\_TO\_SINGLETON](../navigation/document.md#launchmode12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/agz10EWSSKuIYvNi3cCrnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE85B05F8A60C590804FC952FFE349DB7A3A8FA9B7D1819097EA07757714DB29)

-   This callback is not triggered by [replacePath](../navigation/document.md#replacepath11) or [replaceDestination](../navigation/document.md#replacedestination18).
    
-   This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 22.
    

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<ESObject>> | Yes | Callback triggered by **onNewParam**, with the parameter being the data passed to the target page during navigation. |

#### NavDestinationCommonTitle

Defines a general title for the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| main | string | [Resource14+](../../common-definitions/basic-types/document.md#resource) | No | No | Main title. |
| sub | string | [Resource14+](../../common-definitions/basic-types/document.md#resource) | No | No | Subtitle. |

#### NavDestinationCustomTitle

Defines a custom title for the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| builder | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | No | Content of the title bar. |
| height | [TitleHeight](../../common-definitions/enums/document.md#titleheight9) | [Length](../../common-definitions/basic-types/document.md#length) | No | No | 
Height of the title bar.

Value range: \[0, +∞)

 |

#### NavDestinationContext11+

Defines the context information for the **NavDestination** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pathInfo | [NavPathInfo](../navigation/document.md#navpathinfo10) | No | No | 
Path information of the navigation destination page.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| pathStack | [NavPathStack](../navigation/document.md#navpathstack10) | No | No | 

Navigation controller of the current **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| navDestinationId12+ | string | No | Yes | 

Unique ID of the current navigation destination page, which is automatically generated by the system and is irrelevant to the universal attribute **id** of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mode22+ | [NavDestinationMode](#navdestinationmode11) | No | Yes | 

Type of the current **NavDestination**.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### \[h2\]getConfigInRouteMap12+

getConfigInRouteMap(): RouteMapConfig | undefined

Obtains the routing configuration of the current **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [RouteMapConfig](#routemapconfig12) | undefined | 
Routing configuration of the current page.

**undefined** is returned when the page is not configured through the route table.

 |

#### RouteMapConfig12+

Defines the routing configuration.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Page name. |
| pageSourceFile | string | No | No | Path of the page in the current package. |
| data | Object | No | No | Custom data of the page. |

#### NestedScrollInfo14+

Provides the information about the nested scrollable containers.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| parent | [Scroller](../../scroll-and-swipe/scroll/document.md#scroller) | No | No | Controller of the target scrollable container. |
| child | [Scroller](../../scroll-and-swipe/scroll/document.md#scroller) | No | No | Controller of the scrollable container nested within the target scrollable container. This scrollable container is a child component of the target scrollable container. |

#### \[h2\]NavDestinationActiveReason17+

Enumerates reasons for the activation state changes of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TRANSITION | 0 | Activation state changes due to page navigation. |
| CONTENT\_COVER | 1 | Activation state changes due to the opening or closing of a modal page. |
| SHEET | 2 | Activation state changes due to the opening or closing of a sheet. |
| DIALOG | 3 | Activation state changes due to the opening or closing of a custom dialog box. |
| OVERLAY | 4 | Activation state changes due to the opening or closing of an overlay using **OverlayManager**. |
| APP\_STATE | 5 | Activation state changes due to switching between foreground and background states of the application. |

#### \[h2\]VisibilityChangeReason21+

Enumerates reasons for **NavDestination** visibility changes.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TRANSITION | 0 | Visibility changes due to page navigation. |
| CONTENT\_COVER | 1 | Visibility changes due to the opening or closing of a modal page. |
| APP\_STATE | 2 | Visibility changes due to switching between the foreground and background states. |

#### NavDestinationTransition15+

Defines a custom transition animation for the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onTransitionEnd | Callback<void> | No | Yes | Callback triggered when the transition animation ends. |
| duration | number | No | Yes | 
Duration of the transition animation.

Default value: **1000** (in milliseconds)

 |
| curve | [Curve](../../common-definitions/enums/document.md#curve) | No | Yes | 

Curve type of the animation.

Default value: [Curve.EaseInOut](../../common-definitions/enums/document.md#curve)

 |
| delay | number | No | Yes | 

Delay of the transition animation.

Default value: **0** (in milliseconds)

 |
| event | Callback<void> | No | No | Closure function specifying the transition animation. The system generates the corresponding transition animation based on the modifications to the component's UI state within the closure. For details, see **event** in [animateTo](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#animateto). |

#### NavDestinationTransitionDelegate15+

type NavDestinationTransitionDelegate = (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined

Defines the delegate function for custom transition animations of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| operation | [NavigationOperation](../navigation/document.md#navigationoperation11) | Yes | Type of navigation operation for the current page transition. |
| isEnter | boolean | Yes | 
Whether the current page is an entry page.

**true**: The current page is an entry page.

**false**: The current page is not an entry page.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[NavDestinationTransition](#navdestinationtransition15)\> | undefined | Array of custom animations for the **NavDestination** page. If **undefined** is returned, the default system animation is used. |

#### Orientation19+

type Orientation = Orientation

Defines an instance object of the Orientation type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 19.

| Type | Description |
| :-- | :-- |
| [Orientation](../../../arkts-api/window-manager/ohos-window-window/enums/document.md#orientation9) | **Orientation** instance. |

#### Example

## Example 1: Linking the Title Bar and Toolbar with Scrollable Components

This example shows how to bind a **NavDestination** component to scrollable containers so that scrolling in the scrollable containers triggers the animations for showing or hiding the title bar and toolbar of the **NavDestination** component.

import { SymbolGlyphModifier } from '@kit.ArkUI';

@Component
struct MyPageOne {
  private listScroller: Scroller = new Scroller();
  private scrollScroller: Scroller = new Scroller();
  private arr: number\[\] = \[\];

  aboutToAppear(): void {
    for (let i = 0; i < 30; i++) {
      this.arr.push(i);
    }
  }

  build() {
    NavDestination() {
      Scroll(this.scrollScroller) {
        Column() {
          List({ space: 0, initialIndex: 0, scroller: this.listScroller }) {
            ForEach(this.arr, (item: number, index: number) => {
              ListItem() {
                Text('' + item)
                  .height(100)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .width('90%')
                  .margin({ left: '5%' })
                  .borderRadius(10)
                  .backgroundColor(Color.Gray)
              }
            }, (item: string) => item);
          }.width('100%').height('80%').scrollBar(BarState.Off)
          .nestedScroll({ scrollForward: NestedScrollMode.SELF\_FIRST, scrollBackward: NestedScrollMode.SELF\_FIRST })

          ForEach(this.arr, (item: number, index: number) => {
            ListItem() {
              Text('' + item)
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .width('90%')
                .margin({ top: '5%' })
                .borderRadius(10)
                .backgroundColor(Color.Pink)
            }
          }, (item: string) => item);
        }
      }
      .width('100%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Vertical)
      .edgeEffect(EdgeEffect.Spring)
    }
    .title('PageOne', { backgroundColor: Color.Yellow, barStyle: BarStyle.STACK })
    .toolbarConfiguration(\[
      {
        // Replace $r('sys.symbol.phone\_badge\_star') with the resource file you use.
        value: 'item1',
        symbolIcon: new SymbolGlyphModifier($r('sys.symbol.phone\_badge\_star'))
      }
    \], { backgroundColor: Color.Orange, barStyle: BarStyle.STACK })
    // Bind the component to nested scrollable containers.
    .bindToNestedScrollable(\[{ parent: this.scrollScroller, child: this.listScroller }\])
  }
}

@Component
struct MyPageTwo {
  private listScroller: Scroller = new Scroller();
  private arr: number\[\] = \[\];

  aboutToAppear(): void {
    for (let i = 0; i < 30; i++) {
      this.arr.push(i);
    }
  }

  build() {
    NavDestination() {
      List({ scroller: this.listScroller }) {
        ForEach(this.arr, (item: number, index: number) => {
          ListItem() {
            Text('' + item)
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .width('90%')
              .margin({ left: '5%' })
              .borderRadius(10)
              .backgroundColor(Color.Gray)
          }
        }, (item: string) => item);
      }.width('100%')
    }
    .title('PageTwo', { backgroundColor: Color.Yellow, barStyle: BarStyle.STACK })
    .toolbarConfiguration(\[
      {
        // Replace $r('sys.symbol.phone\_badge\_star') with the resource file you use.
        value: 'item1',
        symbolIcon: new SymbolGlyphModifier($r('sys.symbol.phone\_badge\_star'))
      }
    \], { backgroundColor: Color.Orange, barStyle: BarStyle.STACK })
    // Bind the component to a scrollable container.
    .bindToScrollable(\[this.listScroller\])
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  MyPageMap(name: string) {
    if (name === 'myPageOne') {
      MyPageOne();
    } else {
      MyPageTwo();
    }
  }

  build() {
    Navigation(this.stack) {
      Column() {
        Button('push PageOne').onClick(() => {
          this.stack.pushPath({ name: 'myPageOne' });
        })
        Button('push PageTwo').onClick(() => {
          this.stack.pushPath({ name: 'myPageTwo' });
        })
      }.height('40%').justifyContent(FlexAlign.SpaceAround)
    }.width('100%')
    .height('100%')
    .title({ main: 'MainTitle', sub: 'subTitle' })
    .navDestination(this.MyPageMap)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/H8uNO7tXTVOIEYfhjcvMAw/en-us_image_0000002537925514.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15B93EA72114DF60372C362A72B58B6AAF0BE9C400E5A53B7CC47F1FCAE00DF9)

## Example 2: Setting a Custom Transitions for the NavDestination Component

The following example demonstrates how to set a custom transition animation for the **NavDestination** component using [customTransition](#customtransition15).

@Entry
@Component
struct NavDestinationCustomTransition {
  stack: NavPathStack = new NavPathStack();

  @Builder
  pageMap(name: string) {
    if (name) {
      NavDest();
    }
  }

  aboutToAppear(): void {
    this.stack.pushPath({name: 'dest0'});
  }

  build() {
    Navigation(this.stack) {
      // empty
    }
    .navDestination(this.pageMap)
    .hideNavBar(true)
    .title('Main Page')
    .titleMode(NavigationTitleMode.Mini)
  }
}

declare type voidFunc = () => void;

@Component
struct NavDest {
  @State name: string = 'NA';
  @State destWidth: string = '100%';
  stack: NavPathStack = new NavPathStack();
  @State translateY: string = '0';

  @Builder
  titleBuilder() {
    Text(this.name)
      .fontSize(20)
      .height(55)
      .fontWeight(FontWeight.Bold)
      .width('100%')
      .padding({ left: 16, right: 16 })
  }

  build() {
    NavDestination() {
      Column() {
        Button('push next page', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.stack.pushPath({ name: this.name == 'PageOne' ? "PageTwo" : "PageOne" });
          })
      }
      .size({ width: '100%', height: '100%' })
    }
    .title(this.titleBuilder)
    .translate({ y: this.translateY })
    .onReady((context) => {
      this.name = context.pathInfo.name;
      this.stack = context.pathStack;
    })
    .backgroundColor(this.name == 'PageOne' ? '#F1F3F5' : '#ff11dee5')
    .customTransition(
      (op: NavigationOperation, isEnter: boolean)
        : Array<NavDestinationTransition> | undefined => {
        console.info('\[NavDestinationTransition\]', 'reached delegate in frontend, op: ' + op + ', isEnter: ' + isEnter);

        let transitionOneEvent: voidFunc = () => { console.info('\[NavDestinationTransition\]', 'reached transitionOne, empty now!'); }
        let transitionOneFinishEvent: voidFunc = () => { console.info('\[NavDestinationTransition\]', 'reached transitionOneFinish, empty now!'); }
        let transitionOneDuration: number = 500;
        if (op === NavigationOperation.PUSH) {
          if (isEnter) {
            // ENTER\_PUSH
            this.translateY = '100%';
            transitionOneEvent = () => {
              console.info('\[NavDestinationTransition\]', 'transitionOne, push & isEnter');
              this.translateY = '0';
            }
          } else {
            // EXIT\_PUSH
            this.translateY = '0';
            transitionOneEvent = () => {
              console.info('\[NavDestinationTransition\]', 'transitionOne, push & !isEnter');
              this.translateY = '0';
            }
            transitionOneDuration = 450;
          }
        } else if (op === NavigationOperation.POP) {
          if (isEnter) {
            // ENTER\_POP
            this.translateY = '0';
            transitionOneEvent = () => {
              console.info('\[NavDestinationTransition\]', 'transitionOne, pop & isEnter');
              this.translateY = '0';
            }
          } else {
            // EXIT\_POP
            this.translateY = '0';
            transitionOneEvent = () => {
              console.info('\[NavDestinationTransition\]', 'transitionOne, pop & !isEnter');
              this.translateY = '100%';
            }
          }
        }

        let transitionOne: NavDestinationTransition = {
          duration: transitionOneDuration,
          delay: 0,
          curve: Curve.Friction,
          event: transitionOneEvent,
          onTransitionEnd: transitionOneFinishEvent
        };

        let transitionTwoEvent: voidFunc = () => { console.info('\[NavDestinationTransition\]', 'reached transitionTwo, empty now!'); }
        let transitionTwo: NavDestinationTransition = {
          duration: 1000,
          delay: 0,
          curve: Curve.EaseInOut,
          event: transitionTwoEvent,
          onTransitionEnd: () => { console.info('\[NavDestinationTransition\]', 'reached Two\\'s finish'); }
        };

        return \[
          transitionOne,
          transitionTwo,
        \];
      })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/3PozTJUUTxiPfu272FFr9g/en-us_image_0000002568685291.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C34ECFAA9CC70E5703AD520AD0D234A0E50506EF97A9ECDC6F6A894F01E7F57D)

## Example 3: Setting System Transition Animations for the NavDestination Component

The following example demonstrates how to set system transition animations using [systemTransition](#systemtransition14) with **Fade**, **Explode**, **SlideBottom**, and **SlideRight** effects.

@Entry
@Component
struct NavDestinationSystemTransition {
  @Provide stack: NavPathStack = new NavPathStack()
  @Provide homePageTransitionType: NavigationSystemTransitionType = NavigationSystemTransitionType.DEFAULT;

  @Builder
  pageMap(name: string) {
    if (name === 'Fade') {
      Fade();
    } else if (name === 'Explode') {
      Explode();
    } else if (name === 'SlideRight') {
      SlideRight();
    } else if (name === 'SlideBottom') {
      SlideBottom();
    } else {
      Dest();
    }
  }

  aboutToAppear(): void {
    this.stack.pushPath({name: 'Dest'});
  }

  build() {
    Navigation(this.stack) {
      // empty
    }
    .navDestination(this.pageMap)
    .hideNavBar(true)
  }
}

@Component
struct Dest {
  @Consume stack: NavPathStack;
  @Consume homePageTransitionType: NavigationSystemTransitionType;
  @State name: string = 'NA';

  build() {
    NavDestination() {
      HomeBody();
    }
    .title('Navigation System Animation')
    .onReady((context) => {
      this.name = context.pathInfo.name;
    })
    .systemTransition(this.homePageTransitionType)
  }
}

@Component
struct Fade {
  @Consume stack: NavPathStack;
  @State name: string = 'NA';

  build() {
    NavDestination() {
      DestBody({
        name: this.name
      })
    }
    .title(this.name)
    .onReady((context) => {
      this.name = context.pathInfo.name;
    })
    .systemTransition(NavigationSystemTransitionType.FADE)
  }
}

@Component
struct Explode {
  @Consume stack: NavPathStack;
  @State name: string = 'NA';

  build() {
    NavDestination() {
      DestBody({
        name: this.name
      })
    }
    .title(this.name)
    .onReady((context) => {
      this.name = context.pathInfo.name;
    })
    .systemTransition(NavigationSystemTransitionType.EXPLODE)
  }
}

@Component
struct SlideRight {
  @Consume stack: NavPathStack;
  @State name: string = 'NA';

  build() {
    NavDestination() {
      DestBody({
        name: this.name
      })
    }
    .title(this.name)
    .onReady((context) => {
      this.name = context.pathInfo.name;
    })
    .systemTransition(NavigationSystemTransitionType.SLIDE\_RIGHT)
  }
}

@Component
struct SlideBottom {
  @Consume stack: NavPathStack;
  @State name: string = 'NA';

  build() {
    NavDestination() {
      DestBody({
        name: this.name
      })
    }
    .title(this.name)
    .onReady((context) => {
      this.name = context.pathInfo.name;
    })
    .systemTransition(NavigationSystemTransitionType.SLIDE\_BOTTOM)
  }
}

@Component
struct DestBody {
  name: string = 'NA';

  columnTextSize: number = 22;
  columnTextFontWeight: FontWeight = FontWeight.Bolder;
  columnWidth: string = '65%';
  columnPadding: number = 22;
  columnMargin: number = 10;
  columnBorderRadius: number = 10;

  build() {
    Column() {
      Column()
        .width('85')
        .height(50)
        .backgroundColor(Color.White)
      Column() {
        Text(this.name)
          .fontSize(this.columnTextSize)
          .fontWeight(this.columnTextFontWeight)
      }
      .width(this.columnWidth)
      .padding(this.columnPadding)
      .margin(this.columnMargin)
      .borderRadius(this.columnBorderRadius)
      .shadow(ShadowStyle.OUTER\_DEFAULT\_LG)
    }
  }
}

@Component
struct HomeBody {
  @Consume stack: NavPathStack;
  @Consume homePageTransitionType: NavigationSystemTransitionType;

  columnTextSize: number = 22;
  columnTextFontWeight: FontWeight = FontWeight.Bolder;
  columnWidth: string = '85%';
  columnPadding: number = 22;
  columnMargin: number = 10;
  columnBorderRadius: number = 10;
  columnShadow: ShadowStyle = ShadowStyle.OUTER\_DEFAULT\_MD;

  build() {
    Column() {
      Search({ value: 'Search' })
        .width(this.columnWidth)

      Column() {
        Text('fade')
          .fontSize(this.columnTextSize)
          .fontWeight(this.columnTextFontWeight)
      }
      .width(this.columnWidth)
      .padding(this.columnPadding)
      .margin(this.columnMargin)
      .borderRadius(this.columnBorderRadius)
      .shadow(this.columnShadow)
      .onClick(() => {
        this.homePageTransitionType = NavigationSystemTransitionType.FADE;
        this.stack.pushPath({name: 'Fade'});
      })

      Column() {
        Text('explode')
          .fontSize(this.columnTextSize)
          .fontWeight(this.columnTextFontWeight)
      }
      .width(this.columnWidth)
      .padding(this.columnPadding)
      .margin(this.columnMargin)
      .borderRadius(this.columnBorderRadius)
      .shadow(this.columnShadow)
      .onClick(() => {
        this.homePageTransitionType = NavigationSystemTransitionType.EXPLODE;
        this.stack.pushPath({name: 'Explode'});
      })

      Column() {
        Text('slide right')
          .fontSize(this.columnTextSize)
          .fontWeight(this.columnTextFontWeight)
      }
      .width(this.columnWidth)
      .padding(this.columnPadding)
      .margin(this.columnMargin)
      .borderRadius(this.columnBorderRadius)
      .shadow(this.columnShadow)
      .onClick(() => {
        this.homePageTransitionType = NavigationSystemTransitionType.SLIDE\_RIGHT;
        this.stack.pushPath({name: 'SlideRight'});
      })

      Column() {
        Text('slide bottom')
          .fontSize(this.columnTextSize)
          .fontWeight(this.columnTextFontWeight)
      }
      .width(this.columnWidth)
      .padding(this.columnPadding)
      .margin(this.columnMargin)
      .borderRadius(this.columnBorderRadius)
      .shadow(this.columnShadow)
      .onClick(() => {
        this.homePageTransitionType = NavigationSystemTransitionType.SLIDE\_BOTTOM;
        this.stack.pushPath({name: 'SlideBottom'});
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/_lQqDlMORICfI9rUx5JNkA/en-us_image_0000002568765301.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7F0B8A2DBFF76ACE07215FE5B66F67459A1FC99EB9599FA1CB428AFE930189C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lNFyUO-6QfCKV92-bNbORg/en-us_image_0000002537765576.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B7FAF5A0C0AFC77A8941EB828733BC5B91EFF61CE02194690108F3F3DB0F264)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/7yjAJRpWSV-9NcC-D-h9bA/en-us_image_0000002537925516.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A57C533613793BFC20F3AC87FD2360D7CC46A71C9E2BCF1D807BFDB14C60F1B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/jOhAFF8kQGWp9ReuhaMWIg/en-us_image_0000002568685293.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FEFB6AD369334D16D1DD8871E775C4745D360A5B6FD9C74E69B3A784DD5367A)

## Example 4: Configuring Display Orientation and Status Bar and Navigation Bar Visibility

This example demonstrates how to configure each **NavDestination** component with specific display orientations and control the visibility of the status bar and navigation bar.

import { window } from '@kit.ArkUI';

@Component
struct PortraitPage {
  @State info: string = '';
  private stack: NavPathStack | undefined = undefined;
  build() {
    NavDestination() {
      Stack({alignContent: Alignment.Center}) {
        Button('push LANDSCAPE page').onClick(() => {
          this.stack?.pushPath({name: 'landscape'});
        })
      }.width('100%').height('100%')
    }
    .width('100%').height('100%')
    .title('PortraitPage')
    .preferredOrientation(window.Orientation.PORTRAIT) // Portrait orientation.
    .enableStatusBar (true) // Show the status bar.
    .enableNavigationIndicator(true) // Show the navigation bar.
    .backgroundColor('#ffbaece9')
    .onResult((result: ESObject)=>{
      this.info = result as string;
    })
    .onReady((ctx: NavDestinationContext) => {
      this.stack = ctx.pathStack;
    })
  }
}

@Component
struct LandscapePage {
  private stack: NavPathStack | undefined = undefined;
  build() {
    NavDestination() {
      Stack({alignContent: Alignment.Center}) {
        Button('push PORTRAIT page').onClick(() => {
          this.stack?.pushPath({name: 'portrait'});
        })
      }.width('100%').height('100%')
    }
    .width('100%').height('100%')
    .title('LandscapePage')
    .preferredOrientation(window.Orientation.LANDSCAPE) // Landscape orientation.
    .enableStatusBar(false) // Hide the status bar.
    .enableNavigationIndicator(false) // Hide the navigation bar.
    .backgroundColor('#ffecb8b8')
    .ignoreLayoutSafeArea(\[LayoutSafeAreaType.SYSTEM\], \[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM\])
    .onReady((ctx: NavDestinationContext) => {
      this.stack = ctx.pathStack;
    })
  }
}

@Entry
@Component
struct ExamplePage {
  private stack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.stack.pushPath({name: "portrait"});
  }

  @Builder
  MyPageMap(name: string) {
    if (name === 'portrait') {
      PortraitPage();
    } else {
      LandscapePage();
    }
  }

  build() {
    Navigation(this.stack) {
    }
    .width('100%')
    .height('100%')
    .hideNavBar(true)
    .navDestination(this.MyPageMap)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/IrADugNYTJC-Uok1eZBW4Q/en-us_image_0000002568765303.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14E67DE765EFBC2A21B94A43241BA6615B93717E6E661D124ED1A79D734217C0)

## Example 5: Handling NavDestination onActive and onInActive Lifecycle Events

Starting from API version 17, the **NavDestination** component includes the [onActive](#onactive17) and [onInactive](#oninactive17) lifecycle events. This example demonstrates various triggering scenarios for the **onActive** and **onInactive** lifecycle callbacks.

import { promptAction, ComponentContent, OverlayManager } from '@kit.ArkUI';

class Params {
  text: string = "";
  offset: Position;

  constructor(text: string, offset: Position) {
    this.text = text;
    this.offset = offset;
  }
}

let overlayShownTag: boolean = false;

@Builder
function builderText(params: Params) {
  Column() {
    Text('I am ' + params.text)
      .fontWeight(FontWeight.Bolder)
      .align(Alignment.Center)
      .fontSize(25)
      .offset({ y: '10%' })
  }
  .backgroundColor(params.text === 'overlay' ? '#ffc' : '#ccf')
  .width('100%')
  .height('100%')
  .offset(params.offset)
}

@Entry
@Component
struct Index {
  stack: NavPathStack = new NavPathStack();

  @Builder
  pageMap(name: string) {
    if (name === 'standard' || name === 'Home') {
      NavDest({
        name: name
      })
    }
    else if (name === 'dialog') {
      NavDest({
        name: name,
        mode: NavDestinationMode.DIALOG,
        positionY: '40%'
      })
    }
  }

  aboutToAppear(): void {
    this.stack.pushPath({name: 'Home'});
  }

  build() {
    Navigation(this.stack) {

    }
    .hideNavBar(true)
    .navDestination(this.pageMap)
  }
}

@Component
struct NavDest {
  @State positionY: string = '0%';
  name: string = 'NA';
  mode: NavDestinationMode = NavDestinationMode.STANDARD;

  build() {
    NavDestination() {
      NavBody()
    }
    .backgroundColor(this.mode === NavDestinationMode.DIALOG ? Color.Pink : undefined)
    .height(this.mode === NavDestinationMode.DIALOG ? '65%' : '100%')
    .mode(this.mode)
    .title(this.name)
    .position({ y: this.positionY })
    .onActive((reason: NavDestinationActiveReason) => {
      let onActiveMsg: string = \`\[activeTest\] ${this.name} onActive, reason: ${reason}\`;
      console.info(onActiveMsg);
      // Use promptAction.showToast for API version 17, and promptAction.openToast for API version 18 or later.
      promptAction.openToast({ message: onActiveMsg }).catch(() => {
        console.info('open toast failed');
      });
    })
    .onInactive((reason: NavDestinationActiveReason) => {
      let onInActiveMsg: string = \`\[activeTest\] ${this.name} onInactive, reason: ${reason}\`;
      console.info(onInActiveMsg);
      // Use promptAction.showToast for API version 17, and promptAction.openToast for API version 18 or later.
      promptAction.openToast({ message: onInActiveMsg }).catch(() => {
        console.info('open toast failed');
      });
    })
    .onBackPressed(() => {
      if (overlayShownTag) {
        overlayShownTag = false;
        this.getUIContext().getOverlayManager().hideAllComponentContents();
        return true;
      }
      return false;
    })
  }
}

@Component
struct NavBody {
  @State isShow: boolean = false;
  @State isBindSheetShow: boolean = false;
  stack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.stack = this.queryNavigationInfo()?.pathStack!;
  }

  @Builder
  myBuilder(id: string) {
    Column() {
      Text('I am ' + id)
        .fontWeight(FontWeight.Bolder)
        .align(Alignment.Center)
        .fontSize(25)
        .offset({ y: '10%' })
    }
    .width('100%')
    .height('100%')
  }

  build() {
    Column() {
      Row() {
        Button('pushPath standard')
          .margin(5)
          .onClick(() => {
            this.stack.pushPath({name: 'standard'});
          })
        Button('pushPath dialog')
          .margin(5)
          .onClick(() => {
            this.stack.pushPath({name: 'dialog'});
          })
      }
      Column() {
        Row() {
          Button("open Modal")
            .onClick(() => {
              this.isShow = true;
            })
            .fontColor(Color.Black)
            .backgroundColor('#ccc')
            .margin(5)
            .bindContentCover(
              this.isShow,
              this.myBuilder('modal'), {
                backgroundColor: '#fcf',
                onDisappear: () => {
                  this.isShow = false;
                }
              })
          Button("open BindSheet")
            .onClick(() => {
              this.isBindSheetShow = true;
            })
            .fontColor(Color.Black)
            .backgroundColor('#ccc')
            .margin(5)
            .bindSheet($$this.isBindSheetShow, this.myBuilder('bindSheet'), {
              height: '60%',
              backgroundColor: '#cfc'
            })
        }
        Row() {
          Button("open Dialog")
            .onClick(() => {
              let componentContent = new ComponentContent(
                this.getUIContext(), wrapBuilder<\[Params\]>(builderText),
                new Params('dialog', {y: '10%'}));
              this.getUIContext().getPromptAction().openCustomDialog(componentContent)
                .then(() => {
                  console.info('\[activeTest\] open custom dialog success');
                })
                .catch(() => {
                  console.info('\[activeTest\] open custom dialog failed');
                })
            })
            .fontColor(Color.Black)
            .backgroundColor('#ccc')
            .margin(5)
          Button("open Overlay")
            .onClick(() => {
              let componentContent = new ComponentContent(
                this.getUIContext(), wrapBuilder<\[Params\]>(builderText),
                new Params('overlay', {y: '10%'}));
              this.getUIContext().getOverlayManager().addComponentContent(componentContent);
              this.getUIContext().getOverlayManager().showComponentContent(componentContent);
              overlayShownTag = true;
            })
            .fontColor(Color.Black)
            .backgroundColor('#ccc')
            .margin(5)
        }
      }
      .width('95%')
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/XNNSAFMaSvOoWjGzxe9VfQ/en-us_image_0000002537765578.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=721E12DCE6A5B1A12EEB669EDD06038DE837EDE9538F355267A1073A8BDE888C)

For more usage of the **NavDestination** component, see [Example in Navigation](../navigation/document.md#example).
