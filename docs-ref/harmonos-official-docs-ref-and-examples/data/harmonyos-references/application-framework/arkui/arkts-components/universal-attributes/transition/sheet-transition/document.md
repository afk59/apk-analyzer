# Sheet Transition

You can bind a sheet to a component through the **bindSheet** attribute. You can also set the sheet to the preset or custom height for when the component is inserted.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/e1iRRhDgR7Ok8glOiUzB7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88447ACFB490B8BBC5570161088D698DDB923D6AF0F89D6F6F470B0C565CB3E9)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

Route hopping is not supported.

#### bindSheet

bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T

Binds a sheet to the component, which is displayed when the component is touched.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/frB5m1EVTUWkQSIbfX0M5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=925FE086B6F25E107EA03E8DB2B0FB2170C53D1246D2442EE3B1939DDD4450F4)

This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isShow | boolean | Yes | 
Whether to display the sheet.

**true**: Display the sheet.

**false**: Hide the sheet.

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this attribute supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding).

 |
| builder | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Content of the sheet. |
| options | [SheetOptions](#sheetoptions) | No | Optional attributes of the sheet. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/cIiGD8rvSbG82GerKyR6QQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B17A26E24FEF94E252F5A2EA9CA3813AEC3C91FEB7DECE85648CD2166F50B49)

1.  When no two-way binding is set up for the **isShow** parameter, closing the sheet by dragging does not change the parameter value.
    
2.  To synchronize the value of the **isShow** parameter with the sheet UI state, set up a two-way binding for **isShow** through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync). Since API version 18, this parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).
    
3.  In scenarios where a sheet with a single detent is dragged upwards or a sheet with multiple detents is shifted to another detent by swiping up, the display area is updated after the drag ends or the shift is completed.
    
4.  A sheet is a popup that is strictly bound to its host node. To achieve an effect where the sheet appears the moment the page is displayed, ensure that the host node is mounted in the view hierarchy. If the host node is not yet mounted when **isShow** is set to **true**, the sheet will not be displayed. You are advised to use the [onAppear](../../../universal-events/component-change-events/show-hide-event/document.md#onappear) to ensure that the sheet is shown after the host node is mounted.
    
    When [SheetMode](#sheetmode12) is set to **EMBEDDED**, in addition to the host node, also ensure that the corresponding page node is successfully mounted.
    
5.  The exit animation of the sheet does not support interruption, and the sheet cannot respond to other gestures during the execution. The current exit animation uses a [spring curve](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-spring-curve), which has a subtle trailing effect that is not visually prominent. Therefore, when the sheet exits, although it may appear to have disappeared, the animation might not have fully finished, and attempting to initiate the sheet again by a touch will not work. You must wait for the animation to fully complete before you can initiate the sheet again.
    

#### SheetOptions

Inherits from [BindOptions](#bindoptions).

Provides content configuration options of the sheet.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| height | [SheetSize](#sheetsize) | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 
Height of the sheet. Default value: **LARGE**.

**NOTE**

Since API version 14, for a bottom sheet in landscape mode, the maximum height is 8 vp from the top of the screen if there is no status bar, and 8 vp from the status bar if there is one.

When a bottom sheet has **detents** set, this attribute is ineffective.

For a bottom sheet in portrait mode, the maximum height is 8 vp from the status bar.

For center and popup sheets set to **SheetSize.LARGE** or **SheetSize.MEDIUM**, this attribute is ineffective, with the default height being 560 vp. For center and popup sheets, the minimum height is 320 vp, and the maximum height is 90% of the shorter edge of the window. If the height specified by **Length** and the height adaptively set with **SheetSize.FIT\_CONTENT** exceed the maximum height, the maximum height is used instead. If they are less than the minimum height, the minimum height is used instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| detents11+ | \[([SheetSize](#sheetsize) | [Length](../../../common-definitions/basic-types/document.md#length)), ( [SheetSize](#sheetsize) | [Length](../../../common-definitions/basic-types/document.md#length))?, ([SheetSize](#sheetsize) | [Length](../../../common-definitions/basic-types/document.md#length))?\] | No | Yes | 

Array of heights where the sheet can rest.

**NOTE**

Since API version 12, this attribute takes effect for a bottom sheet in landscape mode.

In earlier versions, this attribute takes effect only for the bottom sheet in portrait mode. The first height in the tuple is the initial height.

The sheet can switch between heights by dragging. After the sheet is dragged and released, it switches to the target height or remains at the current height, depending on the velocity and distance. If the velocity exceeds the threshold, the sheet switches to the target height in the same direction as the velocity. If the velocity is less than the threshold, the displacement distance is used for judgement. If the displacement distance is greater than 1/2 of the distance between the current and target positions, the sheet switches to the target height in the same direction as the velocity; otherwise, the sheet remains at the current height.

Velocity threshold: 1000; Distance threshold: 50%.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| preferType11+ | [SheetType](#sheettype11) | No | Yes | 

Type of the sheet.

**NOTE**

The types supported by the sheet vary by window.

1\. Width < 600 vp: bottom, full-screen. It is a default bottom style.

2\. 600 vp <= Width < 840 vp: bottom, center, popup, side-aligned, full-screen. It is a default center style.

3\. Width >= 840 vp: bottom, center, popup, side-aligned, full-screen. It is a default popup style.

4\. Since API version 20, when the window width is greater than 600 vp, **preferType** can be set to **SheetType.SIDE**.

5\. Since API version 20, **preferType** can be set to **SheetType.CONTENT\_COVER**, enabling full-screen sheet style.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| showClose11+ | boolean | [Resource](../../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Whether to display the close icon.

On 2-in-1 devices, the icon does not have a background by default.

Default value: **true**.

**true**: Display the close icon.

**false**: Do not display the close icon.

**NOTE**

The value of **Resource** must be of the Boolean type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| dragBar | boolean | No | Yes | 

Whether to display the drag bar.

Default value: **true**

**true**: Display the drag bar.

**false**: Do not display the drag bar.

**NOTE**

By default, the drag bar is displayed only when the sheet's **detents** attribute is set to multiple heights and the settings take effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| blurStyle11+ | [BlurStyle](../../basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur of the sheet. By default, there is no background blur.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maskColor | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Mask color of the sheet.

Default value: **$r('sys.color.ohos\_id\_color\_mask\_thin')**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| title11+ | [SheetTitleOptions](#sheettitleoptions11) | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | 

Title of the sheet.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableOutsideInteractive11+ | boolean | No | Yes | 

Whether to allow users to interact with the underlying page when the sheet is displayed.

**NOTE**

The value **true** means that interactions are allowed, in which case no mask is not displayed. The value **false** means that interactions are not allowed, in which case a mask is displayed. If this parameter is not set, interactions are allowed for the popup sheet, but not for bottom and center sheets. If this parameter is set to **true**, the setting of **maskColor** does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shouldDismiss11+ | (sheetDismiss: [SheetDismiss](#sheetdismiss11)) => void | No | Yes | 

Callback invoked when the user performs an interactive dismiss operation: pulling down, side swiping, or clicking the mask or the close icon.

**NOTE**

If this callback is registered, the sheet is not dismissed immediately when the user performs the above operations. To dismiss the sheet, you must call **shouldDismiss.dismiss()** in the callback.

If this callback is not registered, the sheet is dismissed immediately when the user performs the above operations, without any additional behavior.

Side swiping for dismissal refers to any of the following operations: swiping left or right, touching the Back button, and pressing the Esc key.

It is recommended that this API be used in scenarios where a [secondary confirmation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sheet-page#secondary-confirmation-capability) is required

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDismiss12+ | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[DismissSheetAction](#dismisssheetaction12)\> | No | Yes | 

Callback invoked when the user performs an interactive dismiss operation: pulling down, side swiping, or clicking the mask or the close icon. Use this callback to determine whether to proceed with dismissal based on the operation type.

**NOTE**

If this callback is registered, the sheet is not dismissed immediately when the user performs the above operations. Instead, you can use the **reason** parameter in the [DismissSheetAction](#dismisssheetaction12) callback to determine the type of dismiss operation and decide whether to dismiss the sheet.

If this callback is not registered, the sheet is dismissed immediately when the user performs the above operations, without any additional behavior.

Side swiping for dismissal refers to any of the following operations: swiping left or right, touching the Back button, and pressing the Esc key.

No further interception with **onWillDismiss** is allowed in an **onWillDismiss** callback.

It is recommended that this API be used in scenarios where a [secondary confirmation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sheet-page#secondary-confirmation-capability) is required

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillSpringBackWhenDismiss12+ | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[SpringBackAction](#springbackaction12)\> | No | Yes | 

Callback to control the interactive spring back before the sheet is dismissed. You can register this callback to control the spring back effect when the sheet is dismissed.

**NOTE**

If this callback is registered along with **shouldDismiss** or **onWillDismiss**, you can control whether the sheet bounces back during the pull-down-to-dismiss operation by calling **springBack** in the callback.

If this callback is not registered but **shouldDismiss** or **onWillDismiss** is registered, the sheet will bounce back before remaining open or being dismissed based on the callback behavior.

If neither this callback nor **shouldDismiss** or **onWillDismiss** is registered, the sheet is dismissed by default during the pull-down-to-dismiss operation.

For side-aligned sheets, **springBack** works only side swiping is performed for dismissal.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onHeightDidChange12+ | Callback<number> | No | Yes | 

Callback for changes in the height of the sheet.

**NOTE**

For a bottom sheet, the height of each frame is only returned when there are changes in detents or during drag actions. When the sheet is pulled up or making space for the soft keyboard, only the final height is returned. For other types of sheets, the final height is only returned when the sheet is pulled up.

The return value is in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDetentsDidChange12+ | Callback<number> | No | Yes | 

Callback for changes in the detents of the sheet.

**NOTE**

For a bottom sheet, the final height is returned when there are changes in detents.

The return value is in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWidthDidChange12+ | Callback<number> | No | Yes | 

Callback for changes in the width of the sheet.

**NOTE**

The final height is returned when there are changes in the width.

The return value is in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onTypeDidChange12+ | Callback<[SheetType](#sheettype11)\> | No | Yes | 

Callback for changes in the type of the sheet.

**NOTE**

The final type is returned when there are changes in the type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderWidth12+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9) | [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+ | No | Yes | 

Border width of the sheet.

You can set the width for all four sides or set separate widths for individual sides.

Default value: **0**

Percentage parameter method: Set the border width of the sheet as a percentage of the width of the parent element.

If the left and right border widths of the sheet are greater than the width of the sheet, and the top and bottom border widths are greater than the height of the sheet, the display may not appear as expected.

**NOTE**

For bottom sheets, the bottom border width setting is ineffective.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderColor12+ | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../../common-definitions/basic-types/document.md#edgecolors9) | [LocalizedEdgeColors](../../../common-definitions/basic-types/document.md#localizededgecolors12)12+ | No | Yes | 

Border color of the sheet.

Default value: **Color.Black**

**borderColor** must be used with **borderWidth** in pairs.

**NOTE**

For bottom sheets, the bottom border color setting is ineffective.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderStyle12+ | [BorderStyle](../../../common-definitions/enums/document.md#borderstyle) | [EdgeStyles](../../../common-definitions/basic-types/document.md#edgestyles9) | No | Yes | 

Border style of the sheet.

Default value: **BorderStyle.Solid**

**borderStyle** must be used with **borderWidth** in pairs.

**NOTE**

For bottom sheets, the bottom border style setting is ineffective.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| width12+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the sheet.

Percentage parameter method: Set the width of the sheet as a percentage of the width of the parent element.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow12+ | [ShadowOptions](../../visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the sheet.

Default value for 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_SM**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| uiContext12+ | [UIContext](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | No | Yes | 

**UIContext** instance corresponding to the window where the sheet is displayed.

**NOTE**

The sheet launched with [openBindSheet](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#openbindsheet12) does not support setting or updating this attribute.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mode12+ | [SheetMode](#sheetmode12) | No | Yes | 

Display mode of the sheet.

Default value: **SheetMode.OVERLAY**

**NOTE**

1\. During the display of the sheet, the **mode** attribute does not support dynamic changes. The display hierarchy of the two modes is entirely different, making it impossible to switch a sheet from one mode to another while it is being displayed. You are advised to clearly define and fix the **mode** value to ensure consistency in the display hierarchy.

2\. The **UIContext** attribute cannot be set when **SheetMode.EMBEDDED** is set, as their corresponding sheet display hierarchy effects are mutually conflicting.

3\. For a sheet launched with [openBindSheet](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#openbindsheet12), if a valid target ID is not provided, **SheetMode.EMBEDDED** cannot be set, and the default value **SheetMode.OVERLAY** is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| scrollSizeMode12+ | [ScrollSizeMode](#scrollsizemode12) | No | Yes | 

Content update mode of the sheet when it is scrolled.

Default value: **ScrollSizeMode.FOLLOW\_DETENT**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| keyboardAvoidMode13+ | [SheetKeyboardAvoidMode](#sheetkeyboardavoidmode13) | No | Yes | 

How the sheet avoids the soft keyboard when it is brought up.

Default value: **TRANSLATE\_AND\_SCROLL**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode.

Default value: **false**, meaning not to enable the hover mode.

Default value for 2-in-1 devices: **true**

**true**: Respond when the device is in semi-folded mode.

**false**: Do not respond when the device is in semi-folded mode.

**NOTE**

The bottom and popup sheets do not respond when the device is in semi-folded mode. The subwindow mode does not support the semi-folded mode.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](#hovermodeareatype14) | No | Yes | 

Display area of the dialog box in hover mode.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

Default value for 2-in-1 devices: **HoverModeAreaType.TOP\_SCREEN**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| radius15+ | [LengthMetrics](../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | [BorderRadiuses](../../../common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../../common-definitions/basic-types/document.md#localizedborderradiuses12) | No | Yes | 

Corner radius of the sheet.

To deliver the optimal experience, use the same radius for the four corners.

Default value: **32vp**

**NOTE**

1\. The corner radius is displayed based on the set value. If it is not set, the default value is used. The bottom sheet does not display the bottom two corners, even if they are set.

2\. If different corner radii are set for the four corners and one of the values is invalid, the corner pertaining to the invalid value is reset to the default value, while the other corners retain their set values. If a uniform corner radius is set for all four corners and the value is invalid, all four corners are reset to the default value.

3\. When the corner radius is set as a percentage, the width of the sheet is used as the reference.

4\. If the corner radius is greater than half the width of the sheet, it is set to half the width of the sheet.

5\. If the height of the sheet is too small and the corner radius is set too large, it may cause display issues.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| 

detentSelection15+

 | [SheetSize](#sheetsize) | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Initial detent (position) for non-gesture switching.

Default value: **detents\[0\]**

**NOTE**

1\. The value must be within the range of the **detents** array. If the value is outside this range, this API has no effect.

2\. When **SheetSize.FIT\_CONTENT** is used, this API has no effect.

3\. Avoid calling this API when gesture-based detent switching is used.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| placement18+ | [Placement](../../../common-definitions/enums/document.md#placement8) | No | Yes | 

Display position of the sheet popup relative to the target.

Default value: **Placement.Bottom**

**NOTE**

1\. The system attempts to display the popup at the specified position if the popup fits within the window. If this is not feasible, it tries vertical flipping first, followed by a 90° horizontal rotation.

2\. If the alignment causes the popup to exceed the window bounds, it will be adjusted horizontally or vertically until fully visible.

3\. If none of the four directions can accommodate the popup, the behavior depends on the **placementOnTarget** attribute:

(1) If the attribute value is **true**, the popup moves in the mirror direction of the specified placement until fully visible.

(2) If the attribute value is **false**, the system selects the direction that can fully display the popup width and has the most remaining height. It then adjusts the sheet height to fit this direction, ensuring that the popup is displayed while maintaining the alignment specified by the **placement** setting.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| placementOnTarget18+ | boolean | No | Yes | 

Whether the sheet popup can overlap the target if none of the four directions can accommodate the popup.

Default value: **true**

**true**: The sheet popup can overlap the target.

**false**: The sheet popup cannot overlap the target.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| effectEdge18+ | number | No | Yes | 

Edge effect used when the boundary of the scrolling area in reached in the sheet. Single-edge activation is supported.

Default value: [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).START | [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).END (that is, value **3**)

**NOTE**

1\. Only start edge: [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).START

2\. Only end edge: [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).END

3\. Both edges: [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).START | [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).END (that is, value **3**)

4\. Neither edge: [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).START & [EffectEdge](../../../scroll-and-swipe/scrollable-component-common-apis/document.md#effectedge18).END (that is, value **0**)

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| showInSubWindow19+ | boolean | No | Yes | 

Whether to show the sheet in a separate subwindow.

Default value: **false**.

**NOTE**

1\. **true**: The sheet displays in a separate subwindow and can extend beyond application window bounds.

2\. **false**: The sheet displays only within application window bounds.

3\. To prevent disruptions to the normal behavior of associated components, do not nest multiple dialog boxes where **showInSubWindow** is set to **true**.

4\. Avoid using picker components (such as **CalendarPicker**, **CalendarPickerDialog**, **DatePickerDialog**, **TextPickerDialog**, and **TimePickerDialog**) in the dialog box where **showInSubWindow** is set to **true**, as the dialog box may affect the behavior of these components.

5\. This attribute cannot be dynamically changed when the sheet is displayed.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| enableFloatingDragBar20+ | boolean | No | Yes | 

Whether to display the drag bar in a floating style. **true** to display in a floating style, **false** otherwise.

Default value: **false**.

**NOTE**

The floating style takes effect only when the drag bar is visible, and the floating drag bar does not occupy layout space.

This parameter is fixed at **false** when **title** uses [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| modalTransition20+ | [ModalTransition](#modaltransition) | No | Yes | 

Transition animation for full-screen sheet style.

Default value: **ModalTransition.DEFAULT**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### SheetSize

Enumerates the sheet height modes.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| MEDIUM | 0 | 
The sheet height is 60% of the window height on non-TV devices

and 50% on TVs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LARGE | 1 | 

The sheet height approximates the full window height.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FIT\_CONTENT11+ | 2 | 

The sheet height automatically adapts to the content.

**Atomic service API**: This API can be used in atomic services since API version 12.

**NOTE**

In this mode, the height is determined by the builder's root node layout. Percentage-based heights are not supported for the root node. Circular dependencies between sheet and content height are prohibited.

 |

#### HoverModeAreaType14+

Enumerates the display area types when the device is in semi-folded mode.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP\_SCREEN | 0 | Upper half screen. |
| BOTTOM\_SCREEN | 1 | Lower half screen. |

#### BindOptions

Defines the common configuration for sheets and modals.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundColor | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Background color of the sheet.

Default value: **Color.White**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onWillAppear12+ | () => void | No | Yes | Callback for when the sheet is about to be displayed (before the animation starts). **Atomic service API**: This API can be used in atomic services since API version 12. |
| onAppear | () => void | No | Yes | 

Callback for when the sheet is displayed (after the animation ends).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onWillDisappear12+ | () => void | No | Yes | 

Callback for when the sheet is about to disappear (before the animation starts).

**NOTE**

Modifying state variables within the **onWillDisappear** function is not allowed, as it may lead to unstable component behavior. **Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDisappear | () => void | No | Yes | 

Callback for when the sheet disappears (after the animation ends).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ModalTransition

Enumerates the modal transition types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Slide-up and slide-down animation for the modal. |
| NONE | 1 | No transition animation for the modal. |
| ALPHA | 2 | Opacity gradient animation for the modal. |

#### SheetType11+

Enumerates the sheet styles.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| BOTTOM | 0 | 
Bottom sheet.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CENTER | 1 | 

Center sheet.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| POPUP | 2 | 

Popup sheet. The popup sheet cannot be dismissed with a pull-down gesture.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SIDE20+ | 3 | 

Side sheet.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| CONTENT\_COVER20+ | 4 | 

Full-screen sheet.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

**Side sheet behavior**:

1.  Transition animation: By default, the sheet enters from the right and exits to the right. In right-to-left (RTL) locales, it enters from the left and exits to the left. Custom transitions are not supported.
    
2.  The multi-level detent is unavailable, and the **detents** and **detentSelection** APIs are not supported. The control bar-related APIs, such as **dragBar**, are not supported.
    
3.  The bottom dialog box style can be swiped up after the transition ends. However, the side dialog box style can only be swiped right to close. The capabilities in the mirroring scenario are opposite.
    
4.  The height cannot be customized and it is full screen by default.
    
5.  Other display level APIs, such as **showInSubWindow = true** and **mode = SheetMode.EMBEDDED**, cannot be specified. The level of the side dialog box is the same as that of **SheetMode.OVERLAY**. Such dialog box can be displayed only at the top of the current **UIContext**. It is displayed at the same level as dialog boxes.
    
6.  Hover state avoidance is not supported.
    
7.  Default width of the side sheets:
    
    -   md [breakpoint](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#breakpoints): 1/2 window width
    -   [Breakpoints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#breakpoints) larger than md: 400 vp fixed width

**APIs not supported by side sheets**

| Name | Description |
| :-- | :-- |
| height | Only full screen height is supported. |
| detents | No detent. |
| dragBar | **DragBar** is not supported. |
| onDetentsDidChange | No detent. |
| uiContext | The display level cannot be specified. |
| mode | The display level cannot be specified. |
| scrollSizeMode | No detent. |
| enableHoverMode | Hover state avoidance is not supported. |
| hoverModeArea | Hover state avoidance is not supported. |
| detentSelection | No detent. |
| placement | Only the popup style is supported. |
| placementOnTarget | Only the popup style is supported. |
| showInSubWindow | The display level cannot be specified. |

**Full-screen bindSheet styles**

1.  In full-screen mode, the border, shadow, title bar, close button, and rounded corner are not supported.
    
2.  By default, the builder content is laid out in the safe area.
    
3.  The full-screen style supports the system transition mode [ModalTransition](#modaltransition), whose default value is **ModalTransition.DEFAULT**. Customized transition is not supported.
    
4.  The **detents** and **detentSelection** APIs are not supported.
    
5.  The sheet can be closed only by swiping left/right.
    
6.  The width and height cannot be customized, and they are set to full screen by default.
    
7.  Other display level APIs, such as **showInSubWindow = true** and **mode = SheetMode.EMBEDDED**, cannot be specified. The display level of the full-screen popup is the same as that of **SheetMode.OVERLAY**. Such popup can be displayed only at the top of the current **UIContext**, and is displayed at the same level as the popup component.
    
8.  The soft keyboard is not avoided by default. You need to customize the settings.
    
9.  The mask is not supported.
    

**APIs not supported by the full-screen bindSheet style**

| Name | Description |
| :-- | :-- |
| height | Only full screen height is supported. |
| width | Only full screen width is supported. |
| detents | No detent. |
| dragBar | The drag bar is not supported. |
| onDetentsDidChange | No detent. |
| showClose | The close button cannot be displayed. |
| title | The title bar cannot be displayed. |
| uiContext | The display level cannot be specified. |
| mode | The display level cannot be specified. |
| scrollSizeMode | No detent. |
| keyboardAvoidMode | The soft keyboard is not avoided by default. You need to customize the settings. |
| enableHoverMode | Hover state avoidance is not supported. |
| hoverModeArea | Hover state avoidance is not supported. |
| detentSelection | No detent. |
| showInSubWindow | The display level cannot be specified. |
| radius | The rounded corner is not supported. |
| borderWidth | The border width is not supported. |
| borderColor | The border color is not supported. |
| borderStyle | The border style is not supported. |
| shadow | The shadow is not supported. |
| maskColor | The mask color is not supported. |
| enableOutsideInteractive | Whether interaction is allowed cannot be set. |
| effectEdge | The edge rebound effect is not supported. |
| enableFloatingDragBar | The floating drag bar is not supported. |
| onWillSpringBackWhenDismiss | The spring effect is not supported. |

#### SheetDismiss11+

Controls the dismissal of a sheet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dismiss | () => void | No | No | Callback for dismissing the sheet. Call this API only when you need the sheet to exit. |

#### SheetTitleOptions11+

Provides the options for configuring the title of a sheet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | No | No | Main title of the sheet. |
| subtitle | [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Subtitle of the sheet. |

#### SheetMode12+

Enumerates the display layer modes of a sheet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| OVERLAY | 0 | The sheet is displayed at the top of the window corresponding to the current **UIContext** instance, above all pages. It is displayed at the same level as dialog boxes. |
| EMBEDDED | 1 | 
The sheet is displayed at the top of the current page.

**NOTE**

Currently, the sheet can only be mounted on a **Page** or **NavDestination** node, with priority given to the **NavDestination** node if it is present. This means that, the sheet can only be displayed at the top of these two types of pages.

In this mode, new pages can overlay the sheet, and when the user returns to the previous page, the sheet remains present without losing its content.

In this mode, you must ensure that the target page node, such as the **Page** node, has been attached to the tree before bringing up the sheet; otherwise, the sheet will not be able to be attached to the corresponding page node.

 |

#### ScrollSizeMode12+

Enumerates the content update modes of a sheet when it is scrolled vertically.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FOLLOW\_DETENT | 0 | The sheet updates the content display area after a swipe ends. |
| CONTINUOUS | 1 | The sheet continuously updates the content display area during the scroll process. |

#### DismissSheetAction12+

Defines the callback triggered when a sheet is about to be dismissed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dismiss | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | No | No | Callback for dismissing the sheet. Call this API when you need to exit the page. |
| reason | [DismissReason](../../dialog-box-control/popup-control/document.md#dismissreason12) | No | No | 
Type of operation that causes the sheet to be dismissed.

**NOTE**

**DismissReason.SLIDE**: right swipe (left swipe in RTL) to dismiss; only available for side sheets.

**DismissReason.SLIDE\_DOWN**: downward swipe to dismiss; only available for bottom and center sheets.

Bubble-style sheets do not support swipe dismissal.

 |

#### SpringBackAction12+

Controls the interactive spring back of a sheet before it is dismissed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| springBack | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | No | No | Callback to control the interactive spring back before the sheet is dismissed. |

#### SheetKeyboardAvoidMode13+

Defines how the sheet avoids the soft keyboard when it is brought up.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | 
Disables keyboard avoidance for the sheet.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| TRANSLATE\_AND\_RESIZE | 1 | 

Translates the sheet upward;

resizes content if translation is insufficient.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| RESIZE\_ONLY | 2 | 

Resizes content to accommodate the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| TRANSLATE\_AND\_SCROLL | 3 | 

Translates the sheet upward;

scrolls content if translation is insufficient.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| POPUP\_SHEET20+ | 4 | 

Repositions popup sheets to avoid the keyboard.

1\. When keyboard avoidance is triggered, if the current display space is insufficient for the popup, the popup is flipped vertically and then rotated by 90 degrees to reposition. For example, if the popup is initially displayed below the keyboard, it will be repositioned in the following sequence: below, above, right, and left.

2\. If the alignment causes the popup to exceed the window bounds, it will be adjusted horizontally or vertically until fully visible.

3\. If none of the four directions can accommodate the popup, the behavior depends on the **placementOnTarget** attribute:

(1) If the attribute value is **true**, the popup moves in the mirror direction of the specified **placement** until fully visible.

(2) If the attribute value is **false**, the system selects the direction that can fully display the popup width and has the most remaining height. It then adjusts the sheet height to fit this direction, ensuring that the popup is displayed while maintaining the alignment specified by the **placement** setting.

4\. Non-popup style sheets do not support keyboard avoidance.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/fB7TzhB0SdSomrMPy6p8rQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=333557C72991456EFFCDE5A7ED44B2CA6BFABA2B99CB0A3558F1FC4638AE4914)

When the **POPUP\_SHEET** avoidance mode is set, the sheet avoids only the soft keyboard started by the text box in the panel.

#### Example

## Example 1: Setting Sheets with Different Heights

This example demonstrates how to set different heights for sheets using the **height** attribute.

// xxx.ets
@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;
  @State sheetHeight: number = 300;

  @Builder
  myBuilder() {
    Column() {
      Button("change height")
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.sheetHeight = 500;
        })

      Button("Set Illegal height")
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.sheetHeight = -1;
        })

      Button("close modal 1")
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.isShow = false;
        })
    }
    .width('100%')
    .height('100%')
  }

  build() {
    Column() {
      Button("transition modal 1")
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: this.sheetHeight,
          backgroundColor: Color.Green,
          onWillAppear: () => {
            console.info("BindSheet onWillAppear.");
          },
          onAppear: () => {
            console.info("BindSheet onAppear.");
          },
          onWillDisappear: () => {
            console.info("BindSheet onWillDisappear.");
          },
          onDisappear: () => {
            console.info("BindSheet onDisappear.");
          }
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/VIsOEta-RCOIM1suAtkktg/en-us_image_0000002568685191.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=391774B9F62E2138E2BC0041321512DDEC79FF629DFBC6780BDE63D38155B7FB)

## Example 2: Setting Three Different Height Detents

This example demonstrates how to use the **detents** attribute of **bindSheet** to set three different height detents for a sheet.

1.  The drag bar is only effective when there are multiple height detents.
2.  Unlike the **height** attribute, which can set different heights at different times, the **detents** attribute provides a gesture to switch between detent heights and is more suitable for fixed height intervals.
3.  If the height range is uncertain or there may be more than three different heights, avoid using the **detents** attribute.

// xxx.ets
@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Column() {
      Button("content1")
        .margin(10)
        .fontSize(20)

      Button("content2")
        .margin(10)
        .fontSize(20)
    }
    .width('100%')
  }

  build() {
    Column() {
      Button("transition modal 1")
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          detents: \[SheetSize.MEDIUM, SheetSize.LARGE, 200\],
          blurStyle: BlurStyle.Thick,
          showClose: true,
          title: { title: "title", subtitle: "subtitle" },
        })
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/nSc-G9HcTW2R4TzirhiMTA/en-us_image_0000002568765201.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F743630F66D570F7BF8C0DAF4557A875596EAD1908020DB138509C0A185C3BD7)

## Example 3: Setting the Border Width and Color

This example demonstrates how to use the **borderWidth** and **borderColor** attributes with **LocalizedEdgeWidths** and **LocalizedEdgeColors** types in **bindSheet**.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Column() {
      Button("content1")
        .margin(10)
        .fontSize(20)

      Button("content2")
        .margin(10)
        .fontSize(20)
    }
    .width('100%')
  }

  build() {
    Column() {
      Button("transition modal 1")
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          detents: \[SheetSize.MEDIUM, SheetSize.LARGE, 200\],
          backgroundColor: Color.Gray,
          blurStyle: BlurStyle.Thick,
          showClose: true,
          title: { title: "title", subtitle: "subtitle" },
          borderWidth: { top: LengthMetrics.vp(10), start: LengthMetrics.vp(10), end: LengthMetrics.vp(20) },
          borderColor: { top: Color.Pink, start: Color.Blue, end: Color.Yellow },
        })
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%')
  }
}

The following shows how the example is represented with left-to-right scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/tG08jABcSla2jdl2uABdaw/en-us_image_0000002537765476.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4E7A9AB548A7807E23284DA00C13285AAE135B864550C229AC418B23AB1BF00)

The following shows how the example is represented with right-to-left scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/ujV2Z0oxRWeXcCBKjTJfDw/en-us_image_0000002537925416.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEC83012D7E63057863772649072B74BBEA06058FF09FA5DD5C354884B6CB477)

## Example 4: Using Dismiss Callbacks

This example shows how to register **onWillDismiss** and **onWillSpringBackWhenDismiss** with **bindSheet**.

// xxx.ets
@Entry
@Component
struct bindSheetExample {
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Column() {
      Button("CONTEXT")
        .margin(10)
        .fontSize(20)
    }
  }

  build() {
    Column() {
      Button("NoRegisterSpringback")
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: SheetSize.MEDIUM,
          blurStyle: BlurStyle.Thick,
          showClose: true,
          title: { title: "title", subtitle: "subtitle" },
          preferType: SheetType.CENTER,

          onWillDismiss: ((dismissSheetAction: DismissSheetAction) => {
            if (dismissSheetAction.reason == DismissReason.SLIDE\_DOWN) {
              dismissSheetAction.dismiss();// Register the dismiss behavior.
            }
          }),

          onWillSpringBackWhenDismiss: ((SpringBackAction: SpringBackAction) => {
          // No springBack is registered, so the modal sheet will not bounce back when swiped down.
          // SpringBackAction.springBack();
          }),
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/N1s8sTVNRmerZdkXreLZbA/en-us_image_0000002568685193.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDFADC8F0E15EF3416634652866B350A0D776D6BFA59A6E832688647935347E0)

## Example 5: Setting the Content Update Mode

This example shows how to use **ScrollSizeMode.CONTINUOUS**, which continuously updates the content and is suitable for detents with multiple height settings.

Whenever possible, minimize UI loading time within the builder, as real-time content refreshing during scrolling has higher performance requirements.

// xxx.ets
@Entry
@Component
struct Index {
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Column() {
      Column()
        .backgroundColor(Color.Blue)
        .height(200)
        .width('100%')
      Column()
        .backgroundColor(Color.Green)
        .height(200)
        .width('100%')
    }
  }

  build() {
    Column() {
      Button('BindSheet')
        .onClick(() => {
          this.isShow = true;
        })
        .bindSheet($$this.isShow, this.myBuilder(), {
          detents: \[300, 600, 900\],
          uiContext: this.getUIContext(),
          mode: SheetMode.OVERLAY,
          scrollSizeMode: ScrollSizeMode.CONTINUOUS,
          backgroundColor: Color.Orange,
          title: { title: 'Title', subtitle: 'Subtitle' }
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

The sheet's content height is not updated until the user stops dragging and releases the sheet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/cDuMfsQnSoOHjTi9SNDnhw/en-us_image_0000002568765203.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=774A79B127337644C65CA1220FF90FD72722B1DC60B6538CC453F4FC1EEE293C)

The sheet's content height is updated in real time as the user drags the sheet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/YYmcM-DLTHqIvIo41pJM-g/en-us_image_0000002537765478.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD0EE6D5639448992DE47E101A7EFCF7387CD74650910097CCCD7AB05FF0F6EE)

## Example 6: Configuring the Sheet to Resize to Avoid the Keyboard

This example demonstrates how to adjust the scrollable content within a sheet when the keyboard height changes by setting **SheetKeyboardAvoidMode** to **RESIZE\_ONLY**.

// xxx.ets
import window from '@ohos.window';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct ListenKeyboardHeightChange {
  @State isShow: boolean = false;
  @State avoidMode: SheetKeyboardAvoidMode = SheetKeyboardAvoidMode.RESIZE\_ONLY;
  scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6\];
  windowClass: window.Window | undefined = undefined;

  aboutToAppear(): void {
    try {
      window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to obtain the top window, Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        this.windowClass = data;
        try {
          if (this.windowClass !== undefined) {
            console.info('success in listen height change');
            this.windowClass.on('keyboardHeightChange', this.callback);
          }
        } catch (exception) {
          console.error(\`Failed to enable the listener for keyboard height changes, Cause code: ${exception.code}, message: ${exception.message}\`);
        }
        console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
      });
    } catch (exception) {
      console.error(\`Failed to obtain the top window, Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }

  callback = (height: number) => {
    console.info('height change: ' + height);
    if (height !== 0) {
      this.scroller.scrollTo({
        xOffset: 0, yOffset: height + this.scroller.currentOffset().yOffset,
        animation: { duration: 1000, curve: Curve.Ease, canOverScroll: false }
      });
    }
  }

  @Builder
  myBuilder() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item: number) => {
          Row() {
            Text(item.toString())
              .width('80%')
              .height(60)
              .backgroundColor('#3366CC')
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 5 })
          }
        }, (item: number) => item.toString())

        TextInput().height('100')

        Flex({ alignItems: ItemAlign.End }) {
          Row() {
            Button("click")
              .margin(10)
              .fontSize(20)
              .width('45%')

            Button("cancel")
              .margin(10)
              .fontSize(20)
              .width('45%')
          }.width('100%')
        }.height(100)
      }.margin({ right: 15, bottom: 50 })
    }
    .height('100%')
    .scrollBar(BarState.On)
    .scrollable(ScrollDirection.Vertical)
  }

  build() {
    Column() {
      Button("transition modal 1")
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: 750,
          backgroundColor: Color.Gray,
          blurStyle: BlurStyle.Thick,
          showClose: true,
          title: { title: "title", subtitle: "subtitle" },
          keyboardAvoidMode: SheetKeyboardAvoidMode.RESIZE\_ONLY,
        })
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/USmr0EBxSgu3Tz9ROAcckA/en-us_image_0000002537925418.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFB7895DA92F244C03DF10E015AE124F05CC403A2714220F038A688009DED825)

## Example 7: Setting the Corner Radius in a Mirrored Layout

This example demonstrates how to set different corner radii for a sheet in a mirrored layout. Typically, to avoid a poor visual experience, do not set different values.

Since API version 15, the **radius** attribute supports the LocalizedBorderRadiuses type.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Column() {
      Button("content1")
        .margin(10)
        .fontSize(20)

      Button("content2")
        .margin(10)
        .fontSize(20)
    }
    .width('100%')
  }

  build() {
    Column() {
      Button("transition modal 1")
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          detents: \[SheetSize.MEDIUM, SheetSize.LARGE, 200\],
          title: { title: "title", subtitle: "subtitle" },
          radius: { topStart: LengthMetrics.vp(50), topEnd: LengthMetrics.vp(10) },
        })
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%')
  }
}

The following shows how the example is represented with left-to-right scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/2zjxhsswThSWgBnjW3wFzg/en-us_image_0000002568685195.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36F17BADA7F3B462055E3A0FA1048E44543D14BC1BD8AAAE832DD68E617FA40A)

The following shows how the example is represented with right-to-left scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/YQLMN31GT1CQWkgGgt9VDA/en-us_image_0000002568765205.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D19ED71003F9EDBEB7167B43F57321EEFC0BC3067E2ABE68AF608165123A0F1)

## Example 8: Implementing a Side Sheet

This example demonstrates how to implement a side sheet. This feature is supported since API version 20.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SheetSideExample {
  @State isShowSide: boolean = false;
  @State enableOutsideInteractive: boolean = false;
  @State borderWidths: LocalizedEdgeWidths | undefined = undefined;
  @State borderColors: Resource | undefined = undefined;
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16\];

  @Builder
  sideBuilder() {
    Column() {
      ForEach(this.arr, (item: number) => {
        Row() {
          Text(item.toString())
            .width('90%')
            .height(60)
            .backgroundColor('#3366CC')
            .borderRadius(15)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .margin({ top: 5 })
        }
      }, (item: number) => item.toString())
      TextInput()
        .margin({ top: 5 })
      Text('Change Sheet Interaction Mode')
        .fontSize(22).fontColor(0xFFFFFF).fontWeight(FontWeight.Bold).textAlign(TextAlign.Center)
        .width('100%').height(50).backgroundColor('#2ebd82')
      Button("change enableOutsideInteractive = " + this.enableOutsideInteractive)
        .margin({ top: 5 })
        .onClick(() => {
          this.enableOutsideInteractive = !this.enableOutsideInteractive;
          if (this.enableOutsideInteractive) {
            this.borderWidths = {start : LengthMetrics.vp(1)};
            this.borderColors = $r('sys.color.comp\_divider');
          } else {
            this.borderWidths = undefined;
            this.borderColors = undefined;
          }
        })
    }
    .width('100%')
    .height('auto')
  }

  build() {
    Column({space:3}) {
      Button("Side sheet")
        .onClick(() => {
          this.isShowSide = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShowSide, this.sideBuilder(), {
          title: { title: "SideSheet", subtitle: "Default width" },
          backgroundColor: Color.Grey,
          onWillAppear: () => {
            console.info("SideSheet onWillAppear.");
          },
          onAppear: () => {
            console.info("SideSheet onAppear.");
          },
          onWillDisappear: () => {
            console.info("SideSheet onWillDisappear.");
          },
          onDisappear: () => {
            console.info("SideSheet onDisappear.");
          },

          preferType: SheetType.SIDE,  // SheetType.SIDE
          blurStyle: BlurStyle.Regular,
          maskColor: "#4bffc62d",  // Customize the mask color.
          enableOutsideInteractive: this.enableOutsideInteractive,

          borderWidth: this.borderWidths,
          borderColor: this.borderColors,

          onHeightDidChange: (height: number)=>{
            console.info("SideSheet height change:" + height);
          },
          onTypeDidChange: (type: SheetType) => {
            console.info("SideSheet type change:" + type);
          },
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

## Example 9: Implementing a Full-Screen Content Cover Sheet

This example demonstrates how to implement a full-screen sheet. This feature is supported since API version 20.

// xxx.ets
@Entry
@Component
struct ContentCoverExample {
  @State isShow: boolean = false

  @Builder
  myBuilder() {
    Column() {
      Button("Close Content Cover Sheet")
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.isShow = false;
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  build() {
    Column() {
      Button("Show Content Cover Sheet")
        .onClick(() => {
          this.isShow = true
        })
        .fontSize(20)
        .margin(10)
        .bindSheet(this.isShow, this.myBuilder(), {
          modalTransition: ModalTransition.DEFAULT,
          preferType: SheetType.CONTENT\_COVER,
          backgroundColor: '#ffd5d5d5',
          maskColor: '#ff707070',
          onWillAppear: () => {
            console.info("ContentCover onWillAppear.")
          },
          onAppear: () => {
            console.info("ContentCover onAppear.")
          },
          onWillDisappear: () => {
            console.info("ContentCover onWillDisappear.")
          },
          onDisappear: () => {
            console.info("ContentCover onDisappear.")
          },
        })
    }
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.White)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/b0PPrnYrR6Sct6Fv3CYEZQ/en-us_image_0000002537765480.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC510CF30D78E2DF89C355E1D81C19AE78A764B275B498D5970F96C5B6EE8DC2)
