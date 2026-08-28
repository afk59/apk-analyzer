# Menu Control

A context menu – a vertical list of items – can be bound to a component and displayed by long-pressing, clicking, or right-clicking the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ULV3Wp_kRiKex2tamtImDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=940B730697B5B47040E674DDF282DBD1D0D591B34D416428F47EBBCC2069F787)

-   The feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Multi-level menus cannot be displayed using **bindMenu** and **bindContextMenu** in **CustomBuilder**. Use the [Menu](../../../menus/menu/document.md) component instead.
    
-   The text in the context menu cannot be selected by long-pressing.
    
-   When the window size changes or the menu content area is tapped, the menu is automatically hidden.
    
-   If the component bound to the menu is a draggable node and **preview** is not specified for **bindContextMenu**, the drag preview will be displayed when the menu is displayed, and the menu options and preview will not avoid each other. You can set preview or set the target node to be non-draggable based on the application scenario.
    
-   Since API version 12, menus allow users to display a submenu with a 500 ms long press, with the pressed state following the movement of the finger.
    
    1.  This feature is only available in scenarios where the [Menu](../../../menus/menu/document.md) component is used and the child components include [MenuItem](../../../menus/menuitem/document.md) or [MenuItemGroup](../../../menus/menuitemgroup/document.md).
        
    2.  This feature is only available for menus with [MenuPreviewMode](#menupreviewmode11) set to **NONE**.
        
-   The maximum width of a menu is limited by the grids occupied by the device. Even if the width is set to 100%, the menu does not occupy the entire screen.
    
-   When the component object bound to the menu is destroyed, the menu disappears.
    
-   [bindContextMenu](#bindcontextmenu8) can be displayed only in the subwindow. [bindMenu](#bindmenu) can be configured to display in subwindows by setting the **showInSubWindow** property in [MenuOptions](#menuoptions10).
    

#### bindMenu

bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T

Binds a menu to this component, which is displayed when the user clicks the component. The displayed menu items support icon+text arrangement and component customization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/QuMcY8XkRTuHOuAfFSWazg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82E9B3ACFACFE41B51DAF9AC3D4AE12B31D42E03ABE4087CA68CED3F01B44A69)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20 only if the input parameter type of **content** is Array<MenuElement>.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| content | Array<[MenuElement](#menuelement)\> | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Array of menu item icons and text, or custom component. |
| options | [MenuOptions](#menuoptions10) | No | Parameters of the context menu. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### bindMenu11+

bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T

Binds a menu to a component. **isShow** specifies whether to display a menu. The displayed menu items support icon+text arrangement and component customization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/_oe67X9ZT2mM49nmUPIngg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3145A73245576F9C67CABA219A105846C25114B688567EC47512CCABED11E85)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20 only if the input parameter type of **content** is Array<MenuElement>.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isShow | boolean | Yes | 
Menu visibility. The menu can be displayed only after the entire page is fully constructed. Setting this parameter to **true** during page construction will cause incorrect positioning and layout. Since API version 18, this parameter supports two-way binding through the [!! syntax](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**true**: Display the menu. **false**: Close the menu.

Default value: **false**

 |
| content | Array<[MenuElement](#menuelement)\> | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Array of menu item icons and text, or custom component. |
| options | [MenuOptions](#menuoptions10) | No | Parameters of the context menu. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### bindContextMenu8+

bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T

Binds a menu to a component. The display or hiding of the menu is triggered via long press or right-click, with custom menu items. To use the code logic to control the display and hiding of menus, use [bindContextMenu12+](#bindcontextmenu12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/KxI4u-FgToGEUcyD9qHgmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18DE14D9F905AF5F309E6FE87586CBB76F10143721BB01541B79EFDCBF33DF74)

-   **bindContextMenu** (implemented in subwindows by default) is not supported in input method windows. For details, see the constraints in [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1) of the input method framework documentation.
    
-   This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| content | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Builder of the custom menu content. |
| responseType | [ResponseType](../../../common-definitions/enums/document.md#responsetype8) | Yes | How the context menu is triggered, which can be long-press or right-click. Long pressing with a mouse device is not supported. |
| options | [ContextMenuOptions](#contextmenuoptions10) | No | Parameters of the context menu. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### bindContextMenu12+

bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T

Binds a menu to a component. **isShown** specifies whether to display a menu.

When **isShown** is **true**, the menu is displayed. When **isShown** is **false**, the menu is hidden. Menu items can be customized.

The menu display position is determined only by the **placement** setting, regardless of the click position.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/SDAA23xPTbuFFvtxG-xEag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC61E5F76737BBB9E29DEED4961DB2CB2934278F9C57872FE017302E8D07156C)

-   **bindContextMenu** (implemented in subwindows by default) is not supported in input method windows. For details, see the constraints in [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1) of the input method framework documentation.
    
-   This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isShown | boolean | Yes | 
Menu visibility. The menu can be displayed properly only when the related page has been constructed. If this parameter is set to **true** before the construction is complete, display issues, such as misplacement, distortion, or failure to pop up, may occur. To trigger dragging by long presses is not supported. Since API version 18, this parameter supports two-way binding through the [!! syntax](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**true**: Display the menu. **false**: Close the menu.

Default value: **false**

 |
| content | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Builder of the custom menu content. |
| options | [ContextMenuOptions](#contextmenuoptions10) | No | Parameters of the context menu. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### MenuElement

Configures icon, text, and interaction information of a menu item.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Menu item text.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon10+ | [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Menu item icon.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enabled11+ | boolean | No | Yes | 

Whether to enable interactions with the menu item.

**true**: yes; **false**: no

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| action | () => void | No | No | 

Action triggered when a menu item is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolIcon12+ | [SymbolGlyphModifier](../../../text-and-input/text-box-component-common-apis/document.md#symbolglyphmodifier12) | No | Yes | 

Icon of a menu item. You can configure the menu item icon using **Modifier**. If both **symbolIcon** and **icon** are configured, the icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### MenuOptions10+

Configues menu item information, which is inherited from [ContextMenuOptions](#contextmenuoptions10).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Menu title.

**NOTE**

This parameter is effective only when **content** is set to Array<[MenuElement](#menuelement)\>.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showInSubWindow11+ | boolean | No | Yes | 

Whether to show the menu in a subwindow.

**true**: yes; **false**: no

Default value: **true** for 2-in-1 devices and **false** for other devices

**NOTE**

This parameter takes effect only for 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ContextMenuOptions10+

Configures menu item information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offset | [Position](../../../common-definitions/basic-types/document.md#position) | No | Yes | 
Offset for showing the context menu, which should not cause the menu to extend beyond the screen.

Default value: **{ x: 0, y: 0 }**. Percentage values are not supported.

**NOTE**

When the menu is displayed relative to the parent component area, the width or height of the area is automatically counted into the offset based on the **placement** attribute of the menu.

Table 1 describes the relationship between the final **offset** value and the **placement** value.

If this parameter is not set, or set to an abnormal value or **undefined**, the default value **{ x: 0, y: 0 }** is used. If the offset exceeds the screen range, it will be constrained to the nearest point within the screen range.

If the display position of the menu is adjusted (different from the main direction of the initial **placement** value), the offset value is invalid.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| placement | [Placement](../../../common-definitions/enums/document.md#placement8) | No | Yes | 

Preferred position of the context menu. If the set position is insufficient for holding the component, it will be automatically adjusted.

**NOTE**

Setting **placement** to **undefined** or **null** is equivalent to not setting it at all. In this case, if [bindMenu](#bindmenu11) is used, the default value of **placement** is **Placement.BottomLeft**; if [bindContextMenu8+](#bindcontextmenu8) is used, the menu is displayed at the touched position; if [bindContextMenu12+](#bindcontextmenu12) is used, the default value is **Placement.BottomLeft**..

 |
| enableArrow | boolean | No | Yes | 

Whether to display an arrow. If the size and position of the context menu are insufficient for holding an arrow, no arrow is displayed.

Default value: **false**, indicating that no arrow is displayed.

**NOTE**

When **enableArrow** is set to **true** and **placement** is not set or set to an invalid value, the arrow is displayed above the target object by default. (For details about the relationship between the default menu position and the API, see Table 3.) Otherwise, the arrow is displayed based on the position specified by **placement**. If the position is insufficient for holding the arrow, it is automatically adjusted. When **enableArrow** is **undefined**, no arrow is displayed. This API is supported in **bindContextMenu** since API version 10 and **bindMenu** since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enableHoverMode18+ | boolean | No | Yes | 

Whether to respond when the device is in hover mode (semi-folded state), that is, whether it triggers avoidance of the crease area in hover mode.

Default value: **false** (**true** for 2-in-1 devices by default) If this parameter is not set or set to an invalid value, the default value is used.

**NOTE**

1\. If the menu display position is within the crease area in hover mode, it will not respond in hover mode.

2\. This parameter is supported on 2-in-1 devices since API version 20.

3\. This parameter only takes effect in window waterfall mode for 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| arrowOffset | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Offset of the arrow relative to the context menu. The offset settings take effect only when the value is valid, can be converted to a number greater than 0, and does not cause the arrow to extend beyond the safe area of the context menu.

Default value: **0**

Unit: vp

**NOTE**

The safe distance of the arrow from the four sides of the menu is the sum of the menu's corner radius and half the width of the arrow.

The value of **placement** determines whether the offset is horizontal or vertical.

When the arrow is in the horizontal direction of the menu, the offset is the distance from the arrow to the leftmost arrow's safe distance. When the arrow is in the vertical direction of the menu, the offset is the distance from the arrow to the topmost arrow's safe distance.

The default position where the arrow is displayed varies with the value of **placement**:

Table 2 describes the relationship between the final position of the arrow and the value of **placement** in cases where the menu does not trigger repositioning.

This API is supported in **bindContextMenu** since API version 10 and **bindMenu** since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| preview11+ | [MenuPreviewMode](#menupreviewmode11) | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | 

Preview displayed when the context menu is triggered by a long-press or by calling [bindContextMenu12+](#bindcontextmenu12). It can be a screenshot of the target component or custom content.

Default value: **MenuPreviewMode.NONE**, indicating no preview.

**NOTE**

\- This parameter has no effect when **responseType** is set to **ResponseType.RightClick**.

\- If **preview** is set to **MenuPreviewMode.NONE** or is not set, the **enableArrow** parameter is effective.

\- If **preview** is set to **MenuPreviewMode.IMAGE** or **CustomBuilder**, no arrow will be displayed even when **enableArrow** is **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| previewAnimationOptions11+ | [ContextMenuAnimationOptions](#contextmenuanimationoptions11) | No | Yes | 

Display effect of the long-press preview.

Default value: **{ scale: \[0.95, 1.1\], transition: undefined, hoverScale: undefined }**

**NOTE**

If the value is less than or equal to **0**, this parameter does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| previewBorderRadius19+ | [BorderRadiusType](#borderradiustype19) | No | Yes | 

Border corner radius for the preview image.

Default value: **16vp**

**NOTE**

If the sum of the two corner radii in the horizontal direction exceeds the width of the preview image, or the sum of the two corner radii in the vertical direction exceeds the height of the preview image, the maximum allowable radius should be used.

A larger corner radius results in a faster animation change for the corners.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| layoutRegionMargin13+ | [Margin](../../../common-definitions/basic-types/document.md#margin) | No | Yes | 

Minimum margin between the preview and menu layout for top, bottom, left, and right edges.

**NOTE**

Only vp, px, fp, lpx, and percentage units are supported.

Any abnormal or negative values will be treated as the default values.

If **preview** is set to **CustomBuilder**, setting **margin.left** or **margin.right** will remove the maximum grid width restriction for the preview.

Be cautious not to set excessively large margins that are too large, which could reduce the layout area and affect the proper layout of the preview and menu.

If the sum of horizontal margins exceeds the maximum layout width, **margin.left** and **margin.right** will be ignored and default values will be applied.

If the sum of vertical margins exceeds the maximum layout width, **margin.top** and **margin.bottom** will be ignored and default values will be applied.

The default margin values are 16 vp for the left and right, 16 vp for top, and 4 vp for bottom.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| previewScaleMode20+ | [PreviewScaleMode](#previewscalemode20) | No | Yes | 

Preview image scaling mode.

Default value: **PreviewScaleMode.AUTO**

**NOTE**

This parameter applies to the scenarios where the layout space is insufficient. If this parameter is not set or is set to **undefined**, the value **PreviewScaleMode.AUTO** will be used. When this parameter is set to **PreviewScaleMode.CONSTANT**, if the preview image is too large and the remaining space is insufficient for placing the menu, the menu is displayed under the preview image.

The maximum width and height of the preview image do not exceed the maximum available layout area of the preview image (the window size minus the safe margins on all sides).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| availableLayoutArea20+ | [AvailableLayoutArea](#availablelayoutarea20) | No | Yes | 

Available layout area of the preview image. The percentage of the preview image is calculated based on this setting. The preview image may be compressed or cropped due to the safe area restriction.

**NOTE**

If this parameter is not set or is set to **undefined**, the percentage is calculated based on the window size. If this parameter is set to **AvailableLayoutArea.SAFE\_AREA**, the available layout area of the preview image is the window size minus the safe margins on all sides.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onAppear | () => void | No | Yes | 

Callback invoked after the menu appears.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onDisappear | () => void | No | Yes | 

Callback invoked after the menu disappears.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| aboutToAppear11+ | () => void | No | Yes | 

Callback triggered when the menu is about to appear.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| aboutToDisappear11+ | () => void | No | Yes | 

Callback triggered when the menu is about to disappear.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundColor11+ | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the menu.

Default value: **Color.Transparent**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle11+ | [BlurStyle](../../basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the menu.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| transition12+ | [TransitionEffect](../../../animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition effect for the entrance and exit of the menu.

**NOTE**

During the exit animation of the menu, if there is a switch between landscape and portrait modes, the menu will make way. Level-2 menus do not inherit custom animations. The level-2 menu can be clicked during the pop-up process, but not during the execution of the exit animation.

For details, see [TransitionEffect](../../../animation/component-transition-transition/document.md#transitioneffect10).

The menu animation uses a spring curve. Due to the rebound and oscillation of the spring curve during the exit of the animation, there is a prolonged tail effect, which prevents the menu from responding to other events after it disappears.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderRadius12+ | [Length](../../../common-definitions/basic-types/document.md#length) | [BorderRadiuses](../../../common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../../common-definitions/basic-types/document.md#localizedborderradiuses12) | No | Yes | 

Border radius of the menu.

Default value: **8vp** for 2-in-1 devices and **20vp** for other devices

**NOTE**

The value can be in percentage.

If the sum of the two maximum corner radii in the horizontal direction exceeds the menu's width, or if the sum of the two maximum corner radii in the vertical direction exceeds the menu's height, the default corner radius of the menu will be used.

When the Length type is used: Invalid input values will trigger a fallback to the default corner radius.

When the BorderRadiuses or LocalizedBorderRadiuses type is used: Invalid input values will result in the menu having no rounded corners by default.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyleOptions18+ | [BackgroundBlurStyleOptions](../../basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 

Background blur style.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| backgroundEffect18+ | [BackgroundEffectOptions](../../basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Background effect.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| hapticFeedbackMode18+ | [HapticFeedbackMode](#hapticfeedbackmode18) | No | Yes | 

Haptic feedback mode when the menu is displayed.

Default value: **HapticFeedbackMode.DISABLED**, indicating no vibration when the menu is displayed.

**NOTE**

The haptic feedback mode is only configurable for level-1 menus.

This parameter takes effect only when the user enables the haptic feedback function and the **ohos.permission.VIBRATE** permission is added to the **requestPermissions** field in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file. The configuration is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/l_BAjkeASjur5ba9a_MVQg/en-us_image_0000002568765189.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3975440C0D1778668B360BA01C60A3572484D9E4AB803FA4423F1EF10C064DB1)

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| outlineWidth20+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | [EdgeOutlineWidths](../../../common-definitions/basic-types/document.md#edgeoutlinewidths11) | No | Yes | 

Outline width of the menu border.

Default value: **0vp**

**NOTE**

Percentage values are not supported. **outlineWidth** is mandatory for customizing an outline effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| outlineColor20+ | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../../common-definitions/basic-types/document.md#edgecolors9) | No | Yes | 

Outline color of the menu border.

**NOTE**

Default value: **'#19ffffff'**

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| mask20+ | boolean | [MenuMaskType](#menumasktype20) | No | Yes | 

Sets whether a menu has a mask and the mask style.

**true**: yes; **false**: no; **MenuMaskType**: custom mask style

Default value: If a preview image is displayed for a menu, a mask is displayed by default. Otherwise, no mask is displayed.

**NOTE**

This API does not take effect when the device is configured not to display the menu mask. For example, this API does not take effect on 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| modalMode20+ | [ModalMode](#modalmode20) | No | Yes | 

Modal mode of a menu.

**NOTE**

Default value: **ModalMode.AUTO**

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| anchorPosition20+ | [Position](../../../common-definitions/basic-types/document.md#position) | No | Yes | 

Display position of the menu relative to the upper left corner of the bound component by setting the horizontal and vertical offsets. Unlike using the **offset** API alone, this allows the menu to overlay the bound component.

Default value: **{ x: undefined, y: undefined }**. Percentage values are not supported.

**NOTE**

1\. Offsets do not apply during menu preview state.

2\. The preset value of **placement** does not take effect.

3\. The **offset** parameter is added to determine the exact display position of the menu.

4\. When both horizontal and vertical offsets are set to negative values, the menu is reset to **Placement.BottomLeft** for display.

5\. If the horizontal or vertical offset is **undefined** or **null**, the effect is the same as that of not setting **anchorPosition**. In this case, the preset value of **placement** can take effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onWillAppear20+ | [Callback<void>](../../../common-definitions/basic-types/document.md#callback12) | No | Yes | 

Callback triggered when the menu is about to appear.

**NOTE**

1\. The normal sequence is **aboutToAppear** > **onWillAppear** > **onAppear** > **onDidAppear** > **aboutToDisappear** > **onWillDisappear** > **onDisappear** > **onDidDisappear**.

2\. **aboutToAppear** is invoked during initialization; **onWillAppear** is invoked before the animation starts but after **aboutToAppear**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onDidAppear20+ | [Callback<void>](../../../common-definitions/basic-types/document.md#callback12) | No | Yes | 

Callback invoked after the menu appears.

**NOTE**

1\. The normal sequence is **aboutToAppear** > **onWillAppear** > **onAppear** > **onDidAppear** > **aboutToDisappear** > **onWillDisappear** > **onDisappear** > **onDidDisappear**.

2\. If rapid clicks are triggered to display and then dismiss the menu, there may be cases where **onWillDisappear** is invoked before **onDidAppear**.

3\. If the menu is closed before the menu entrance animation is complete, this callback is not triggered.

4\. **onAppear** and **onDidAppear** are invoked at the same time, but **onDidAppear** takes effect after **onAppear**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onWillDisappear20+ | [Callback<void>](../../../common-definitions/basic-types/document.md#callback12) | No | Yes | 

Callback triggered when the menu is about to disappear.

**NOTE**

1\. The normal sequence is **aboutToAppear** > **onWillAppear** > **onAppear** > **onDidAppear** > **aboutToDisappear** > **onWillDisappear** > **onDisappear** > **onDidDisappear**.

2\. If rapid clicks are triggered to display and then dismiss the menu, there may be cases where **onWillDisappear** is invoked before **onDidAppear**.

3\. **aboutToDisappear** and **onWillDisappear** are invoked at the same time, but **onWillDisappear** takes effect after **aboutToDisappear**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onDidDisappear20+ | [Callback<void>](../../../common-definitions/basic-types/document.md#callback12) | No | Yes | 

Callback invoked after the menu disappears.

**NOTE**

1\. The normal sequence is **aboutToAppear** > **onWillAppear** > **onAppear** > **onDidAppear** > **aboutToDisappear** > **onWillDisappear** > **onDisappear** > **onDidDisappear**.

2\. **onDisappear** and **onDidDisappear** are triggered at the same time, but **onDidDisappear** takes effect after **onDisappear**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

**Table 1: Menu offset when both offset and placement are set**

| Value of placement | Menu Offset |
| :-- | :-- |
| Placement.TopLeft, Placement.Top, or Placement.TopRight | If the value of **x** is a positive number for **offset**, the menu shifts to the right relative to the component. If the value of **y** is a positive number, the menu shifts upward relative to the component. |
| Placement.BottomLeft, Placement.Bottom, or Placement.BottomRight | If the value of **x** is a positive number for **offset**, the menu shifts to the left relative to the component. If the value of **y** is a positive number, the menu shifts downward relative to the component. |
| Placement.RightTop, Placement.Right, or Placement.RightBottom | If the value of **x** is a positive number for **offset**, the menu shifts to the right relative to the component. If the value of **y** is a positive number, the menu shifts downward relative to the component. |

**Table 2: Default position of the menu arrow when both arrowOffset and placement are set**

| Value of placement | Menu Arrow Position |
| :-- | :-- |
| Placement.Top or Placement.Bottom | The arrow is displayed horizontally and centered by default, with a distance from the left edge of the menu equal to the arrow's safe distance. |
| Placement.Left or Placement.Right | The arrow is displayed vertically and centered by default, with a distance from the top edge of the menu equal to the arrow's safe distance. |
| Placement.TopLeft or Placement.BottomLeft | The arrow is displayed horizontally by default, with a distance from the left edge of the menu equal to the arrow's safe distance. |
| Placement.TopRight or Placement.BottomRight | The arrow is displayed horizontally by default, with a distance from the right edge of the menu equal to the arrow's safe distance. |
| Placement.LeftTop or Placement.RightTop | The arrow is displayed vertically by default, with a distance from the top edge of the menu equal to the arrow's safe distance. |
| Placement.LeftBottom or Placement.RightBottom | The arrow is displayed vertically by default, with a distance from the bottom edge of the menu equal to the arrow's safe distance. |

**Table 3 Default menu position when enableArrow is set to true and placement is not set or set to an invalid value**

| API | Default Menu Position |
| :-- | :-- |
| [bindMenu](#bindmenu) | Placement.BottomLeft |
| [bindMenu11+](#bindmenu11) | Placement.BottomLeft |
| [bindContextMenu8+](#bindcontextmenu8) | Placement.Top |
| [bindContextMenu12+](#bindcontextmenu12) | Placement.BottomLeft |

#### MenuPreviewMode11+

Defines the preview style of a menu.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No preview is displayed. |
| IMAGE | 1 | The preview is a screenshot of the component on which a long-press triggers the context menu. |

#### ContextMenuAnimationOptions11+

Defines the style for displaying a long-press preview.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scale | [AnimationRange](#animationrange11)<number> | No | Yes | 
Relative scale ratio at the start and end of the animation compared to the original preview image.

Default value: **\[0.95, 1.1\]**

**NOTE**

The scale ratio must be set based on the specific use case. It is recommended that it be less than the width of the preview image or the maximum constraint of the layout.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| transition12+ | [TransitionEffect](../../../animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition effect for the entrance and exit of the menu.

**NOTE**

If the screen orientation is switched during the exit animation of a menu, the menu will avoid obstacles. Level-2 menus do not inherit custom animations. The level-2 menu can be clicked during the display process, but not during the execution of the exit animation.

For details, see [TransitionEffect](../../../animation/component-transition-transition/document.md#transitioneffect10).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| hoverScale12+ | [AnimationRange](#animationrange11)<number> | No | Yes | 

In the custom preview (**preview** is of the CustomBuilder type) and menu displayed in long-press (**responseType** is set to **LongPress**) scenarios, **hoverScale** is used to set two parameters for the screenshot floating animation of the bound component: the start and end scale ratios relative to the original preview image. After **hoverScale** is set, the floating animation and preview image are switched with a transition effect.

**NOTE**

If the value is less than or equal to **0**, this parameter does not take effect.

This API does not take effect in [bindContextMenu12+](#bindcontextmenu12) scenarios.

This API does not take effect when **transition** is set.

If this API and the **scale** API are used at the same time, the start value of the **scale** API does not take effect.

To ensure the optimal experience, it is not recommended that the final preview image size be smaller than the size of the original component snapshot. The width and height of the preview animation are affected by the component snapshot and the custom preview size. Verify the display effect based on the actual use case.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| hoverScaleInterruption20+ | boolean | No | Yes | 

Whether lifting the finger before triggering the drag effect allows preview menu pop-up cancellation in scenarios where **preview** is of the CustomBuilder type (custom preview image), **responseType** is set to **LongPress** (display is triggered by a long-press action), and **hoverScaleInterruption** is set to **true**. The options are **true** (yes) and **false** (no).

Default value: **false**

**NOTE**

If the **hoverScale** API is not set or the **transition** API is set, this parameter does not take effect. If the finger is lifted before the long-press duration is sufficient to trigger the drag effect, the **hoverScale** effect of the preview menu will revert, the preview menu will not pop up, and gesture events such as click bound to the original component can still be triggered. If the finger is lifted after the long-press duration is sufficient to trigger the drag effect, the preview menu will pop up properly, and gesture events such as click bound to the original component will no longer be triggered.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### AnimationRange11+

type AnimationRange<T>=\[from: T, to: T\]

Sets the relative scale ratio at the start and end of the animation compared to the original preview image.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| \[from: T, to: T\] | **from** indicates the scale ratio at the beginning of the animation, and **to** indicates the scale ratio at the end of the animation. |

#### HapticFeedbackMode18+

Enumerates the haptic feedback modes used when the menu is displayed.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DISABLED | 0 | The menu is displayed without haptic feedback. |
| ENABLED | 1 | The menu is displayed with haptic feedback. |
| AUTO | 2 | Whether to enable haptic feedback is subject to system settings. It is enabled when the menu has a mask. |

#### BorderRadiusType19+

type BorderRadiusType = [Length](../../../common-definitions/basic-types/document.md#length) | [BorderRadiuses](../../../common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../../common-definitions/basic-types/document.md#localizedborderradiuses12)

Enumerates the border corner radius types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Length](../../../common-definitions/basic-types/document.md#length) | Size unit. |
| [BorderRadiuses](../../../common-definitions/basic-types/document.md#borderradiuses9) | Corner radius of a component's border. |
| [LocalizedBorderRadiuses](../../../common-definitions/basic-types/document.md#localizedborderradiuses12) | Localized corner radius of a component's border. |

#### MenuMaskType20+

Sets the mask type.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Mask color.

Default value: **$r('sys.color.ohos\_id\_color\_mask\_thin')**

 |
| backgroundBlurStyle | [BlurStyle](../../basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Blur material of the mask.

Default value: **BlurStyle.BACKGROUND\_THIN**

 |

#### ModalMode20+

Enumerates modal modes of the sub-window menu.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | Automatic mode, which is the default behavior of the menu component on the current device. In the current version, the effect on all devices is the same as that of **ModalMode.NONE**. |
| NONE | 1 | Events can be passed through areas other than the menu itself, allowing underlying controls to respond to events. |
| TARGET\_WINDOW | 2 | Events cannot be passed through the application window where the menu is located and the menu area, but can be passed through other areas. |

#### PreviewScaleMode20+

Enumerates the scale modes of the preview image.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | The preview image automatically adjusts its width, height, and scale based on [Placement](../../../common-definitions/enums/document.md#placement8). |
| CONSTANT | 1 | The preview image retains its original size. However, the preview image may still be compressed or cropped due to the safe area constraints. |
| MAINTAIN | 2 | The preview image maintains its aspect ratio when scaled. |

#### AvailableLayoutArea20+

Enumerates the reference sizes of the available layout area when the preview image width and height are set to percentages.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SAFE\_AREA | 0 | The reference size of the available layout area is the window size minus the safe margins on all sides. |

#### Example

**Atomic service API**: This API can be used in atomic services since API version 23.

This example demonstrates how to display a basic menu by configuring [MenuElement](#menuelement) for **bindMenu**.

@Entry
@Component
struct MenuExample {
  build() {
    Column() {
      Text('click for Menu')
        .bindMenu(\[
          {
            value: 'Menu1',
            action: () => {
              console.info('handle Menu1 select');
            }
          },
          {
            value: 'Menu2',
            action: () => {
              console.info('handle Menu2 select');
            }
          },
        \])
    }
    .width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/bP2_jLSPQ6aj-VBu8gPdGQ/en-us_image_0000002537765464.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C47F365369D0FAF94331912C42079C1BA258B9E9A62D1E31AD083DF42FF99E6F)

## Example 2: Displaying a Custom Menu

This example shows how to use **bindMenu** with a custom builder to create a custom menu. In addition, starting from API version 18, the **hapticFeedbackMode** property in [ContextMenuOptions](#contextmenuoptions10) can be configured to implement the haptic feedback effect when the menu is displayed.

@Entry
@Component
struct MenuExample {
  @State listData: number\[\] = \[0, 0, 0\];

  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      ForEach(this.listData, (item:number, index) => {
        Column() {
          Row() {
            // Replace $r('app.media.icon') with the image resource file you use.
            Image($r("app.media.icon")).width(20).height(20).margin({ right: 5 })
            Text(\`Menu${index as number + 1}\`).fontSize(20)
          }
          .width('100%')
          .height(30)
          .justifyContent(FlexAlign.Center)
          .align(Alignment.Center)
          .onClick(() => {
            console.info(\`Menu${index as number + 1} Clicked!\`);
          })

          if (index != this.listData.length - 1) {
            Divider().height(10).width('80%').color('#ccc')
          }
        }.padding(5).height(40)
      })
    }.width(100)
  }

  build() {
    Column() {
      Text('click for menu')
        .fontSize(20)
        .margin({ top: 20 })
        .bindMenu(this.MenuBuilder, { hapticFeedbackMode: HapticFeedbackMode.ENABLED })
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#f0f0f0')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/xZ692MsaTg-A04W1Sz7wSQ/en-us_image_0000002537925404.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3FC33A7BC302BB789B32FC69506A1F5C4269B8F949C89301B4DD8BCADC998D1)

## Example 3: Displaying a Menu on Long Press

This example demonstrates how to display a menu by setting [responseType](../../../common-definitions/enums/document.md#responsetype8).LongPress for **bindContextMenu**.

@Entry
@Component
struct ContextMenuExample {
  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Test menu item 1')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Test menu item 2')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
    }.width(100)
  }

  build() {
    Column() {
      Text('LongPress for menu')
    }
    .width('100%')
    .margin({ top: 5 })
    .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/9lNMDl2BSW2dj_MsDWQZeQ/en-us_image_0000002568685181.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD48DECD2A8681DC6B97C01B431A7275C2643E704E49BD860114D7F7CB5B1E30)

## Example 4: Displaying a Menu with an Arrow on Right-Clicking

This example demonstrates how to display a menu with an arrow by setting the **enableArrow** property in [responseType](../../../common-definitions/enums/document.md#responsetype8).RightClick and [ContextMenuOptions](#contextmenuoptions10) for **bindContextMenu**. In addition, starting from API version 18, the **hapticFeedbackMode** property in [ContextMenuOptions](#contextmenuoptions10) can be configured to implement the haptic feedback effect when the menu is displayed.

@Entry
@Component
struct DirectiveMenuExample {
  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('Options')
      Divider().strokeWidth(2).margin(5).color('#F0F0F0')
      Text('Hide')
      Divider().strokeWidth(2).margin(5).color('#F0F0F0')
      Text('Exit')
    }
    .width(200)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Column() {
        Text("DirectiveMenuExample")
          .fontSize(20)
          .width('100%')
          .height("25%")
          .backgroundColor('#F0F0F0')
          .textAlign(TextAlign.Center)
          .bindContextMenu(this.MenuBuilder, ResponseType.RightClick, {
            enableArrow: true,
            placement: Placement.Bottom,
            hapticFeedbackMode: HapticFeedbackMode.ENABLED
          })
      }
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/crZnJT8WSA6Lh0kULMBT0w/en-us_image_0000002568765191.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D81D19F8B9198A1F5B2B3C3648C988E4BE9127B26D8FC813EA5C05CAF2BC8B11)

## Example 5: Displaying a Menu with a Screenshot Preview on Long Press

This example demonstrates how to display a menu with a screenshot preview by setting [MenuPreviewMode](#menupreviewmode11) of the **preview** property in [responseType](../../../common-definitions/enums/document.md#responsetype8).LongPress and [ContextMenuOptions](#contextmenuoptions10) for **bindContextMenu**.

@Entry
@Component
struct Index {
  // Replace $r('app.media.icon') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.icon");

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Text('preview-image')
            .width(200)
            .height(100)
            .textAlign(TextAlign.Center)
            .margin(100)
            .fontSize(30)
            .bindContextMenu(this.MyMenu, ResponseType.LongPress,
              { preview: MenuPreviewMode.IMAGE,
                previewAnimationOptions: {scale: \[0.8, 1.0\]},
              })
            .backgroundColor("#ff3df2f5")
        }
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/5laxyGgVQbWezJlY1SzTCA/en-us_image_0000002537765466.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38CF44B58A2DCC14ADCBA910D2F2A9BC5CAD61BA0CB48E3CB7229A1BAB0450D4)

## Example 6: Displaying a Menu with a Custom Preview on Long Press

This example demonstrates how to display a menu with a custom preview by setting [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) of the **preview** property in [responseType](../../../common-definitions/enums/document.md#responsetype8).LongPress and [ContextMenuOptions](#contextmenuoptions10) for **bindContextMenu**.

@Entry
@Component
struct Index {
  // Replace $r('app.media.icon') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.icon");

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  @Builder
  MyPreview() {
    Column() {
      Image($r('app.media.icon'))
        .width(200)
        .height(200)
    }
  }

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Text('preview-builder')
            .width(200)
            .height(100)
            .textAlign(TextAlign.Center)
            .margin(100)
            .fontSize(30)
            .bindContextMenu(this.MyMenu, ResponseType.LongPress,
              {
                preview: this.MyPreview
              })
        }
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/NK1OFV6uSBiPv4NJ4UmmhA/en-us_image_0000002537925406.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28EB226DEB7E87F2B573DF7E51FCDF4899D1BB85BCC740660D59282406C7AB22)

## Example 7: Using a State Variable for Menu Visibility

This example demonstrates how to use [bindContextMenu](#bindcontextmenu12) with **isShown** to control the visibility of the menu.

@Entry
@Component
struct Index {
  // Replace $r('app.media.icon') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.icon");
  @State isShown: boolean = false;

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  @Builder
  MyPreview() {
    Column() {
      Image($r('app.media.icon'))
        .width(200)
        .height(200)
    }
  }

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Text('preview-builder')
            .width(200)
            .height(100)
            .textAlign(TextAlign.Center)
            .margin(100)
            .fontSize(30)
            .bindContextMenu(this.isShown, this.MyMenu,
              {
                preview: this.MyPreview,
                aboutToDisappear: ()=>{
                  this.isShown = false;
                }
              })
          Button('click')
            .onClick(()=>{
              this.isShown = true;
            })
        }
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/liWo2c5WReiddbJnoTFr9g/en-us_image_0000002537925406.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A06B3327EA406B757096CBE58B96C716D5758B47106E437D3AB7A055FB46840A)

## Example 8: Using Custom Menu and Preview Animations

This example demonstrates how implement custom entrance and exit animations for the menu and preview by setting the **transition** property in [ContextMenuOptions](#contextmenuoptions10) of **bindContextMenu**.

@Entry
@Component
struct MenuExample {
  @Builder
  MenuBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Menu item 1')
        .fontSize(12)
        .width(200)
        .height(30)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Menu item 2')
        .fontSize(12)
        .width(100)
        .height(30)
        .textAlign(TextAlign.Center)
    }.width(100)
  }

  @Builder
  MyPreview() {
    Column() {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      Image($r('app.media.startIcon'))
        .width(50)
        .height(50)
    }
  }

  build() {
    Column() {
      Button('LongPress bindContextMenu')
        .margin({ top: 15 })
        .bindContextMenu(
          this.MenuBuilder,
          ResponseType.LongPress, {
          transition: TransitionEffect.OPACITY.animation({ duration: 4000, curve: Curve.Ease }).combine(
            TransitionEffect.rotate({ z: 1, angle: 180 })),
          preview: this.MyPreview,
          previewAnimationOptions: {
            scale: \[0.8, 1.0\],
            transition: TransitionEffect.OPACITY.animation({ duration: 4000, curve: Curve.Ease }).combine(
              TransitionEffect.rotate({ z: 1, angle: 180 }))
          }
        })
    }
    .width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/4B8HvaLPTICXO1U2sZtsVw/en-us_image_0000002568685183.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37D2B8B0E798DFF1D57BC8731C399AD0E1887068F6CF1213375F5D80D3C98A43)

## Example 9: Setting the Symbol Icon

This example shows how to display a menu with symbol icons by setting **symbolIcon** in [MenuElement](#menuelement) of **bindMenu**.

import { SymbolGlyphModifier } from '@kit.ArkUI';
@Entry
@Component
struct MenuExample {
  @State symbolIconModifier1: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_photo')).fontSize('24vp');
  @State symbolIconModifier2: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_photo')).fontSize('24vp');
  build() {
    Column() {
      Text('click for Menu')
    }
    .width('100%')
    .margin({ top: 5 })
    .bindMenu(\[
      {
        value: 'Menu1',
        symbolIcon:this.symbolIconModifier1,
        action: () => {
          console.info('handle Menu1 select');
        }
      },
      {
        value: 'Menu2',
        symbolIcon:this.symbolIconModifier2,
        action: () => {
          console.info('handle Menu2 select');
        }
      },
    \])
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/g_tfnQ3NThGvPqRzAJgXkg/en-us_image_0000002568765193.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AD59799DDBBA1DDECDC0C8AC95AA3CDC654D1ADFEADE826177372B3A32186F5)

## Example 10: Using Shared Element Transition

This example demonstrates how to implement a shared element transition effect from the component screenshot to the custom preview by setting **hoverScale** of the **previewAnimationOptions** property in [ContextMenuOptions](#contextmenuoptions10) for **bindContextMenu**.

@Entry
@Component
struct Index {
  // Replace $r('app.media.xxx') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.app\_icon");

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  @Builder
  MyPreview() {
    Column() {
      Image($r('app.media.example'))
        .width(200)
        .height(200)
    }
  }

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Image($r('app.media.example'))
            .width(100)
            .height(100)
            .margin(100)
            .bindContextMenu(this.MyMenu, ResponseType.LongPress,
              {
                preview: this.MyPreview,
                previewAnimationOptions: {
                  hoverScale: \[1.0, 0.95\]
                }
              })
        }
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/K6Yfq6hLQs2H2iqXX6BLdg/en-us_image_0000002537765468.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE3FEBA1000440C2BEEC5CB8AEC06E6E6F573E4B6C2511BEFAC9D807C7378457)

## Example 11: Customizing the Background Blur Effect

This example demonstrates how to customize the blur background effect of a menu by setting the **backgroundBlurStyleOptions** property in [ContextMenuOptions](#contextmenuoptions10) for **bindMenu**.

The **backgroundBlurStyleOptions** property is added to **ContextMenuOptions** since API version 18.

@Entry
@Component
struct MenuExample {
  build() {
    Stack() {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Text('click for Menu')
          .bindMenu(\[
            {
              value: 'Menu1',
              action: () => {
                console.info('handle Menu1 select')
              }
            },
            {
              value: 'Menu2',
              action: () => {
                console.info('handle Menu2 select')
              }
            },
          \],
            {
              backgroundBlurStyle: BlurStyle.BACKGROUND\_THIN,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                blurOptions: { grayscale: \[20, 20\] },
                policy: BlurStyleActivePolicy.ALWAYS\_ACTIVE,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1
              },
            }
          )
      }
      .width('100%')
      .margin({ top: 5 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Xbs4_CL1Tk-yYvjSc0zWFg/en-us_image_0000002537925408.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB49727C6F554FBC7FEC9E0A4DA655E7844883326CFE38A9E448C2E5E94F321C)

## Example 12: Customizing the Background Effect

This example demonstrates how to customize the background effect of a menu by setting the **backgroundEffect** property in [ContextMenuOptions](#contextmenuoptions10) for **bindMenu**.

The **backgroundEffect** property is added to **ContextMenuOptions** since API version 18.

@Entry
@Component
struct MenuExample {
  build() {
    Stack() {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Text('click for Menu')
          .bindMenu(\[
            {
              value: 'Menu1',
              action: () => {
                console.info('handle Menu1 select');
              }
            },
            {
              value: 'Menu2',
              action: () => {
                console.info('handle Menu2 select');
              }
            },
          \],
            {
              backgroundBlurStyle: BlurStyle.BACKGROUND\_THIN,
              backgroundEffect: {
                radius: 60,
                saturation: 10,
                brightness: 1,
                color: '#661A1A1A',
                adaptiveColor: AdaptiveColor.AVERAGE,
                blurOptions:{grayscale:\[20,20\]}
              }
            }
          )
      }
      .width('100%')
      .margin({ top: 5 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/W9eA9SEYTsKCB3YmO4CBCg/en-us_image_0000002568685185.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=579E1DE77B6FA17DA6C7580A2C32BD0A7BE20573AE5F1F911425EC4C7FE43E6E)

## Sample 13: Configuring Lift-Finger Interruption for a Shared Element Transition

This example demonstrates how to implement a shared element transition by setting the **previewAnimationOptions** property in [ContextMenuOptions](#contextmenuoptions10) for **bindContextMenu** and how to control whether lifting the finger after a long press can cancel the menu pop-up by setting **hoverScaleInterruption**.

From API version 20, the **hoverScaleInterruption** property is added to the [ContextMenuAnimationOptions](#contextmenuanimationoptions11) type of **previewAnimationOptions**.

// xxx.ets
@Entry
@Component
struct Index {
  // Replace $r('app.media.xxx') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.app\_icon");

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  @Builder
  MyPreview() {
    Column() {
      Image($r('app.media.example'))
        .width(300)
        .height(200)
    }
  }

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Image($r('app.media.example'))
            .width(100)
            .height(100)
            .margin(100)
            .bindContextMenu(this.MyMenu, ResponseType.LongPress,
              {
                preview: this.MyPreview,
                previewAnimationOptions: {
                  hoverScale: \[1.0, 0.8\],
                  hoverScaleInterruption: true
                }
              })
            .onClick(() => {
              console.info('trigger onClick')
            })
        }
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/CxrZl3c-SKmoy16pD4rQjA/en-us_image_0000002568765195.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20295C405F5BE0D25E359F59A10100B38501CB630D19FB27BDAD809490C8DC06)

## Sample 14: Setting the Radius of the Rounded Corners of the Preview Image Border

This example demonstrates how to implement the function using **bindContextMenu** with [responseType](../../../common-definitions/enums/document.md#responsetype8).LongPress set. In addition, the [MenuPreviewMode](#menupreviewmode11) type of the **preview** property in [ContextMenuOptions](#contextmenuoptions10) is set to determine the menu preview mode. **previewBorderRadius** is set to implement the radius of the rounded corners of the preview image.

In API version 19, the **previewBorderRadius** property is added to [ContextMenuOptions](#contextmenuoptions10).

@Entry
@Component
struct Index {
  // Replace $r('app.media.startIcon') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.startIcon");

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Text('preview-image')
            .width(200)
            .height(100)
            .textAlign(TextAlign.Center)
            .margin(100)
            .fontSize(30)
            .bindContextMenu(this.MyMenu, ResponseType.LongPress,
              {
                preview: MenuPreviewMode.IMAGE,
                previewBorderRadius: 50
              })
            .backgroundColor("#ff7fcdff")
        }
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/6cbLp43RSMyWz-kIunk0Fw/en-us_image_0000002537765470.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44330BCA07B23F7C791FCE3FF9AD14F85FA5DCCF85FC6A028CA35C6817F1ACEB)

## Sample 15: Configuring Lifecycle Callbacks for bindMenu

This example shows how to configure the lifecycle callback for **bindMenu**.

From API version 20, the **onWillAppear**, **onDidAppear**, **onWillDisappear**, and **onDidDisappear** properties are added to [ContextMenuOptions](#contextmenuoptions10).

@Entry
@Component
struct Index {
  // Replace $r('app.media.startIcon') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.startIcon");
  @State isShown: boolean = false;
  @State textColor: Color = Color.Black;
  @State blueColor: Color = Color.Blue;
  @State onWillAppear: boolean = false;
  @State onDidAppear: boolean = false;
  @State onWillDisappear: boolean = false;
  @State onDidDisappear: boolean = false;

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  build() {
    Column() {
      Column({ space: 30 }) {
        Text('onWillAppear').fontColor(this.onWillAppear ? this.blueColor : this.textColor)
        Text('onDidAppear').fontColor(this.onDidAppear ? this.blueColor : this.textColor)
        Text('onWillDisappear').fontColor(this.onWillDisappear ? this.blueColor : this.textColor)
        Text('onDidDisappear').fontColor(this.onDidDisappear ? this.blueColor : this.textColor)
        Button('click')
          .onClick(() => {
            this.isShown = true;
          })
          .width(100)
          .height(50)
        Text('callback')
          .width(200)
          .height(100)
          .textAlign(TextAlign.Center)
          .fontSize(20)
          .fontColor(this.textColor)
          .bindMenu(this.isShown, this.MyMenu,
            {
              onWillAppear: () => {
                console.info("menu cycle life onWillAppear");
                this.onWillAppear = true;
              },
              onDidAppear: () => {
                console.info("menu cycle life onDidAppear");
                this.onDidAppear = true;
              },
              onWillDisappear: () => {
                this.isShown = false;
                console.info("menu cycle life onWillDisappear");
                this.onWillDisappear = true;
              },
              onDidDisappear: () => {
                console.info("menu cycle life onDidDisappear");
                this.onDidDisappear = true;
              }
            })
      }
    }.width('100%')
  }
}

## Example 16: Setting the Menu Mask

This example demonstrates how to implement the menu mask using **bindMenu** with the **mask** property.

In API version 20, the **mask** property is added to [ContextMenuOptions](#contextmenuoptions10).

import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_star'))
  @State isShow: boolean = false;

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Create folder",
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Sort by",
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "View mode",
      })
    }
  }

  build() {
    Button('bindMenu')
      .position({ top: 80, left: 80 })
      .onClick(() => {
        this.isShow = !this.isShow;
      })
      .bindMenu(this.isShow, this.MyMenu, {
        mask: { color: 'rgba(23,169,141,0.5)', backgroundBlurStyle: BlurStyle.Thin }
      })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/55xdyZhLToOxO4_GmEH33A/en-us_image_0000002537925410.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E8026B926E1E08956B44D46E3BA52C7C158AB727090622F6FC2BD7A5FD5E51A)

## Example 17: Setting the Outline Style of a Drop-Down Menu Using bindMenu

This example demonstrates how to set the outline style of the drop-down menu by setting the **outlineWidth** and **outlineColor** properties of **bindMenu**.

In API version 20, the **outlineWidth** and **outlineColor** properties are added to [ContextMenuOptions](#contextmenuoptions10).

@Entry
@Component
struct Index {
  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ content: "Menu option" })
      MenuItem({ content: "Menu option" })
      MenuItem({ content: "Menu option" })
    }.width(200)
  }

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Text('click for Menu')
            .width(200)
            .height(100)
            .textAlign(TextAlign.Center)
            .margin(100)
            .fontSize(30)
            .bindMenu(this.MyMenu,
              {
                outlineWidth: '5vp',
                outlineColor: Color.Blue
              })
        }
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#F0F2F5')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/BBiJWYwHSxKtrc7k7K2Row/en-us_image_0000002568685187.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40E581CDC837E98272F7CC24737E652205950CFCE4BA44BAE7D7BFB67E322A36)

## Example 18: Passing a CustomBuilder with Parameters to bindMenu

This example demonstrates how to configure the properties of a menu by passing a **CustomBuilder** with parameters to **bindMenu**.

// xxx.ets
@Entry
@Component
struct Index {
  @State menuItemList: string\[\] = \['New', 'History', 'Bookmark', 'Settings'\]

  @Builder
  MenuBuilder(itemList: string\[\]) {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      ForEach(itemList, (item: string, index) => {
        Row() {
          Text(item)
            .width('100%')
            .height(32)
            .fontWeight(400)
            .fontSize(14)
            .fontColor(Color.Black)
            .textAlign(TextAlign.Center)
        }
        .onClick(() => {
          console.info('handle' + item + 'Clicked!')
        })
        if (index != itemList.length - 1) {
          Divider().height(10).width('80%').color('#ccc')
        }
      })
    }
    .width(100)
  }

  build() {
    Column() {
      Text('click for Menu')
        .bindMenu(this.MenuBuilder(this.menuItemList))
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#f0f0f0')
  }
}

## Sample 19: Displaying Different Menus Based on the Trigger Mode

This example demonstrates how to set the **anchorPosition** property in [ContextMenuOptions](#contextmenuoptions10) to display the menu relative to the upper left corner of the bound component.

Since API version 20, the **anchorPosition** property is added to **ContextMenuOptions**.

@Entry
@Component
struct Index {
  // Replace $r('app.media.startIcon') with the image resource file you use.
  private iconStr: ResourceStr = $r('app.media.startIcon');
  @State isShown: boolean = false;

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: 'Menu option' })
      MenuItem({ startIcon: this.iconStr, content: 'Menu option' })
      MenuItem({ startIcon: this.iconStr, content: 'Menu option' })
    }
  }

  @State menuAnchorPositionIndex: number = 0;
  private menuAnchorPositionArray: Array<Position> = new Array<Position>(
    { x: 0, y: 0 },
    { x: 150, y: 0 },
    { x: 0, y: 150 },
    { x: 150, y: 150 },
  );

  build() {
    Column({ space: 50 }) {
      Column() {
        Column() {
          Text('Test Menu AnchorPosition')
            .width(500)
            .height(100)
            .textAlign(TextAlign.Center)
            .margin(100)
            .fontSize(30)
            .bindContextMenu(this.isShown, this.MyMenu,
              {
                anchorPosition: this.menuAnchorPositionArray\[this.menuAnchorPositionIndex\],
                aboutToDisappear: () => {
                  this.isShown = false;
                }
              })
          Button('click')
            .margin(5)
            .onClick(() => {
              this.isShown = true;
            })

          Button('AnchorPosition change')
            .margin(5)
            .onClick(() => {
              this.menuAnchorPositionIndex++;
              if (this.menuAnchorPositionIndex >= this.menuAnchorPositionArray.length) {
                this.menuAnchorPositionIndex = 0;
              }
            })
          Text('Current x: ' + this.menuAnchorPositionArray\[this.menuAnchorPositionIndex\]?.x +
            ' , y: ' + this.menuAnchorPositionArray\[this.menuAnchorPositionIndex\]?.y)
        }
      }.width('100%')
    }
  }
}
