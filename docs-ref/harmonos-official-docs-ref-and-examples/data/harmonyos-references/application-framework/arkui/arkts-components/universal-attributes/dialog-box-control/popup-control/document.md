# Popup Control

Binds a popup to a component and sets the popup content, interaction logic, and display status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/LdDkXYfKSaiP10PEXPBl4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA217F8707E77C7C941DE550598EF71232DD1056C2FD3C4E0378C1887A7EAC34)

-   The feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The display status of the popup is reported in the **onStateChange** callback of [PopupOptions](#popupoptions) or [CustomPopupOptions](#custompopupoptions8). When the component bound to the popup is destroyed, the popup disappears, but the display status is not reported through **onStateChange**.
    
-   The maximum height of the popup is calculated as follows: Current window height – Top/Bottom safe area height (status bar and navigation bar) – 80 vp.
    
-   When multiple popups are displayed at the same time, popups displayed in child windows have a higher z-index than those in the main window. When in the same window, popups displayed later have a higher z-index than those displayed earlier.
    
-   By default, the PC/2-in-1 device has double outlines, while other devices do not.
    
-   Nested subwindow dialog boxes are not supported. For example, when **bindPopup** has **showInSubWindow** set to **true**, another dialog box with **showInSubWindow=true** cannot be displayed.
    
-   When the component bound to the popup is destroyed, the screen is rotated, or the application enters the background, the popup automatically disappears, and the [onWillDismiss](#popupoptions) event is not triggered.
    

#### bindPopup

bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T

Binds a popup to the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/B8lYRCx6QZuh3igw2Z4dzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6919303CE1DFAC01852B0A72D71B42BC6EA5AE225E84694A39B409893FA0E71A)

-   **bindPopup** with subwindow display (**showInSubwindow** set to **true**) is not supported in input method windows. For details, see the constraints in [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1) of the input method framework documentation.
    
-   This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| show | boolean | Yes | 
Popup display status. The popup can be displayed only after the entire page is fully constructed. Setting **show** to **true** during page construction will cause incorrect positioning and layout. Since API version 18, this parameter supports two-way binding through the [!! syntax](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**true**: The popup is displayed; **false**: The popup is closed.

Default value: **false**

 |
| popup | [PopupOptions](#popupoptions) | [CustomPopupOptions](#custompopupoptions8)8+ | Yes | Configuration options of the popup. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### PopupOptions

Provides the configuration options for the popup.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| message | string | No | No | 
Content of the popup.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| primaryButton | 

{

value: string,

action: () => void

}

 | No | Yes | 

Primary button.

**value**: text of the primary button in the popup.

**action**: callback function for clicking of the primary button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| secondaryButton | 

{

value: string,

action: () => void

}

 | No | Yes | 

Secondary button.

**value**: text of the secondary button in the popup.

**action**: callback function for clicking of the secondary button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onStateChange | (event: { isVisible: boolean }) => void | No | Yes | 

Callback for popup visibility state changes. The parameter **isVisible** indicates the visibility of the popup. It returns **true** when the popup transitions from closed to open, and **false** when the popup transitions from open to closed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showInSubWindow9+ | boolean | No | Yes | 

Whether the popup is displayed in the created subwindow.

**true**: The popup is displayed in the created subwindow; **false**: The popup is displayed in the corresponding main window.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| mask10+ | boolean | { color : [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) } | No | Yes | 

Whether to apply a mask with the specified color to the popup.

**true**: A transparent mask is applied; **false**: No mask is applied.

**Color**: A mask with the specified color is applied.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| messageOptions10+ | [PopupMessageOptions](#popupmessageoptions10) | No | Yes | 

Configuration options of the popup message.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| targetSpace10+ | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Spacing between the popup and the host node. Percentage values are not supported.

Default value: **8**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| placement10+ | [Placement](../../../common-definitions/enums/document.md#placement8) | No | Yes | 

Display position of the popup relative to the host node. The default value is **Placement.Bottom**.

If both **placementOnTop** and **placement** are set, the latter prevails. If the popup cannot be completely displayed in the specified position, the popup automatically adjusts its position to completely show itself.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offset10+ | [Position](../../../common-definitions/basic-types/document.md#position) | No | Yes | 

Offset of the popup relative to the display position specified by **placement**.

Default value: **{x:0, y:0}**

Unit: vp

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enableArrow10+ | boolean | No | Yes | 

Whether to display the arrow.

**true**: The arrow is displayed; **false**: The arrow is not displayed.

Default value: **true**

**NOTE**

If the available space on the screen is insufficient, the popup will cover part of the component and the arrow will not be displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| arrowPointPosition11+ | [ArrowPointPosition](../../../common-definitions/enums/document.md#arrowpointposition11) | No | Yes | 

Position of the tooltip arrow relative to its parent component. Available positions are **START**, **CENTER**, and **END**, in both vertical and horizontal directions. All these positions are within the parent component area.

Default value: **ArrowPointPosition.CENTER**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| arrowWidth11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Arrow thickness. If the arrow thickness exceeds the length of the edge minus twice the size of the popup rounded corner, the arrow is not drawn.

Default value: **16**

Unit: vp

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| arrowHeight11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Arrow height.

Default value: **8**

Unit: vp

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| arrowOffset9+ | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Offset of the popup arrow relative to the popup.

When the arrow is at the top or bottom of the popup: The value **0** indicates that the arrow is located on the leftmost, and any other value indicates the distance from the arrow to the leftmost; the arrow is centered by default.

When the arrow is on the left or right side of the popup: The value indicates the distance from the arrow to the top; the arrow is centered by default.

When the popup is displayed on either edge of the screen, it automatically adjusts horizontally. When the value is **0**, the arrow always points to the bound component.

Unit: vp

**NOTE**

1\. If **arrowOffset** is not set, the distance between the popup arrow and the four corners must be no less than the corner radius.

2\. If **arrowPointPosition** is set, **arrowOffset** does not take effect.

3\. Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| popupColor11+ | [Color](../../../common-definitions/enums/document.md#color) | string | [Resource](../../../common-definitions/basic-types/document.md#resource) | number | No | Yes | 

Color of the popup. To remove the background blur, set **backgroundBlurStyle** to **BlurStyle.NONE**.

Default value: [TRANSPARENT](../../../common-definitions/enums/document.md#color) plus [COMPONENT\_ULTRA\_THICK](../../basic-attributes/background/document.md#blurstyle9)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| autoCancel11+ | boolean | No | Yes | 

Whether the popup is automatically closed when an operation is performed on the page.

**true**: The popup is automatically closed; **false**: The popup is not automatically closed.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| width11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the popup. If this parameter is not set or the value is invalid, the popup width is automatically adjusted to adapt to the content width.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| radius11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Rounded corner radius of the popup.

Default value: **20**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow11+ | [ShadowOptions](../../visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Popup shadow.

Default value: **ShadowStyle.OUTER\_DEFAULT\_MD**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle11+ | [BlurStyle](../../basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the popup.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| transition12+ | [TransitionEffect](../../../animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition animations for the entrance and exit of the popup.

**NOTE**

1\. If this parameter is not set, the default entrance and exit animations are used.

2\. Touching the back button during the entrance animation interrupts it and starts the exit animation. The final effect is one obtained after the curves of the entrance and exit animations are combined.

3\. Touching the back button during the exit animation does not affect the animation playback; the back button is unresponsive.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDismiss12+ | boolean | Callback<[DismissPopupAction](#dismisspopupaction12)\> | No | Yes | 

Interactive dismissal behavior. The default value is **true**, meaning that the popup responds to clicks, swipes (left or right), and the back button.

1\. For the boolean type, if this parameter is set to **false**, the popup ignores clicks, swipes, back button, route navigation, and **Esc** key events, and can only be dismissed by setting the **show** parameter to **false**; if this parameter is set to **true**, the popup responds to dismissal events.

2\. If this parameter is set to a function, the dismissal event is intercepted and the callback function is executed. For swipes, back button, route navigation, and the **Esc** key, the value of **reason** returned in the callback function is **PRESS\_BACK**. For clicks, the value is **TOUCH\_OUTSIDE**.

**NOTE**

Nesting **onWillDismiss** callbacks is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| followTransformOfTarget13+ | boolean | No | Yes | 

Whether the popup aligns with the transformed position of the target when the target component or its parent container has transformations (such as rotation and scaling).

**true**: The popup aligns with the transformed position of the target; **false**: The popup does not track such transformations, which may result in incorrect display.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| keyboardAvoidMode15+ | [KeyboardAvoidMode](#keyboardavoidmode12) | No | Yes | 

Whether to avoid the soft keyboard. By default, the popup does not avoid the soft keyboard. When configured to avoid the soft keyboard, if the popup display space is insufficient, the display mode of the popup changes from being centered over the parent component to being translated and covering the parent component.. In addition, if the popup arrow does not point to the host, the arrow will not be displayed.

Default value: **KeyboardAvoidMode.NONE**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| enableHoverMode18+ | boolean | No | Yes | 

Whether the popup responds when the device is in hover mode (semi-folded state), that is, whether it triggers avoidance of the crease area in hover mode.

Default value: **false** (**true** for 2-in-1 devices by default). If this parameter is not set or set to an invalid value, the default value is used.

**NOTE**

1\. If the popup position is within the crease area in hover mode, it will not respond in hover mode.

2\. This parameter is supported on 2-in-1 devices since API version 20.

3\. This parameter only takes effect in window waterfall mode for 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| outlineWidth20+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the outer outline of the popup.

Default value: **1**

Unit: vp

**NOTE**

1\. Percentage values are not supported. If a percentage value is set, the value **0** is used.

2\. If the outer outline is not set, this parameter must be used together with **outlineLinearGradient**.

3\. For double outlines, it is recommended that the outer outline width should not exceed 10 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| borderWidth20+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the inner outline of the popup.

Default value: **1**

Unit: vp

**NOTE**

1\. Percentage values are not supported. If a percentage value is set, the value **0** is used.

2\. If no inner outline is set, this parameter must be used together with **borderLinearGradient**.

3\. For double outlines, it is recommended that the inner outline width should not exceed 10 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| outlineLinearGradient20+ | [PopupBorderLinearGradient](#popupborderlineargradient20) | No | Yes | 

Linear gradient color of the outer outline of the popup.

**NOTE**

1\. If **outlineLinearGradient** is not set or set to **null** or **undefined**, the linear gradient color of the outer outline does not take effect.

2\. When **outlineLinearGradient** is set, the default value of **direction** is **GradientDirection.Bottom**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| borderLinearGradient20+ | [PopupBorderLinearGradient](#popupborderlineargradient20) | No | Yes | 

Linear gradient color of the inner outline of the popup.

**NOTE**

1\. If **borderLinearGradient** is not set or set to **null** or **undefined**, the linear gradient color of the inner outline does not take effect.

2\. When **borderLinearGradient** is set, the default value of **direction** is **GradientDirection.Bottom**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| avoidTarget20+ | [AvoidanceMode](../../../buttons-and-selections/select/document.md#avoidancemode19) | No | Yes | 

Whether the popup covers the pointing component during avoidance.

Default value: **AvoidanceMode.COVER\_TARGET**

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| placementOnTop(deprecated) | boolean | No | Yes | 

Whether to display the popup above the component. The default value is **false**. **true**: The popup is displayed above the bound component; **false**: The popup is displayed below the bound component.

**NOTE**

This parameter is supported since API version 7 and deprecated since API version 10. You are advised to use **placement** instead.

 |

#### PopupMessageOptions10+

Describes the popup message text style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| textColor | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Text color of the popup message. |
| font | [Font](../../../common-definitions/basic-types/document.md#font) | No | Yes | 
Font settings of the popup message.

**NOTE**

1\. Setting **family** is not supported.

2\. The **weight** attribute in **Font** does not support the number type.

 |

#### DismissPopupAction12+

Provides information about the dismissal of the popup.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dismiss | Callback<void> | No | No | Callback for dismissing the popup. This API is called only when the popup needs to be dismissed. |
| reason | [DismissReason](#dismissreason12) | No | No | Reason why the popup is dismissed. |

#### DismissReason12+

Enumerates the reasons for popup dismissal.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| PRESS\_BACK | 0 | 
Touching the **Back** button, swiping left or right on the screen, or pressing the **Esc** key.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TOUCH\_OUTSIDE | 1 | 

Touching the mask.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CLOSE\_BUTTON | 2 | 

Touching the close button.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SLIDE\_DOWN | 3 | 

Swiping down.

**NOTE**

This API is effective only in [sheet transition](../../transition/sheet-transition/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SLIDE20+ | 4 | 

Swiping left or right on the screen. By default, swiping right dismisses the popup, while swiping left is used in the mirror scenario. This setting is not user-defined.

**NOTE**

This API is effective only in [sheet transition](../../transition/sheet-transition/document.md).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### CustomPopupOptions8+

Provides information for displaying a custom popup.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| builder | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | No | No | 
Builder of the tooltip content.

**NOTE**

1\. The **Popup** attribute is a universal attribute. A custom popup does not support display of another popup. The **position** attribute cannot be used for the first-layer container in the builder. If the **position** attribute is used, the popup will not be displayed.

2\. If a custom component is used in the **builder**, the **aboutToAppear** and **aboutToDisappear** lifecycle callbacks of the custom component are irrelevant to the visibility of the popup. As such, the lifecycle of the custom component cannot be used to determine whether the popup is displayed or not.

3\. The **builder** of this constructor can be defined only in UI components, such as the **Builder** function/method or the [build](../../../custom-components/custom-component-lifecycle/document.md#build) method.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| placement | [Placement](../../../common-definitions/enums/document.md#placement8) | No | Yes | 

Preferred position of the tooltip component. If the set position is insufficient for holding the component, it will be automatically adjusted.

Default value: **Placement.Bottom**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| popupColor | [Color](../../../common-definitions/enums/document.md#color) | string | [Resource](../../../common-definitions/basic-types/document.md#resource) | number | No | Yes | 

Color of the popup. To remove the background blur, set **backgroundBlurStyle** to **BlurStyle.NONE**.

The default value varies by API version.

API version 10: **'#4d4d4d'**

API version 11 and later: [TRANSPARENT](../../../common-definitions/enums/document.md#color) plus [COMPONENT\_ULTRA\_THICK](../../basic-attributes/background/document.md#blurstyle9)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| autoCancel | boolean | No | Yes | 

Whether the popup is automatically closed when an operation is performed on the page.

**true**: The popup is automatically closed; **false**: The popup is not automatically closed.

Default value: **true**

**NOTE**

To dismiss the popup upon a click on it, place a layout component in the **builder**, place the **Popup** component in the layout component, and set **show** to **false** in the **onClick** event of the layout component.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onStateChange | (event: { isVisible: boolean }) => void | No | Yes | 

Callback for popup visibility state changes. The parameter indicates the visibility of the popup. It returns **true** when the popup transitions from closed to open, and **false** when the popup transitions from open to closed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enableArrow | boolean | No | Yes | 

Whether to display the arrow.

**true**: The arrow is displayed; **false**: The arrow is not displayed.

Since API version 9, if the position set for the popup is not large enough, the arrow will not be displayed. For example, if **placement** is set to **Left**, and the popup height is less than the sum of the arrow width (32 vp) and twice the popup corner radius (48 vp), that is, 80 vp, the arrow will not be displayed.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| arrowOffset9+ | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Offset of the popup arrow relative to the popup.

When the arrow is at the top or bottom of the popup: The value **0** indicates that the arrow is located on the leftmost, and any other value indicates the distance from the arrow to the leftmost; the arrow is centered by default.

When the arrow is on the left or right side of the popup: The value indicates the distance from the arrow to the top; the arrow is centered by default.

When the popup is displayed on either edge of the screen, it automatically adjusts horizontally. When the value is **0**, the arrow always points to the bound component.

Unit: vp

**NOTE**

1\. If **arrowOffset** is not set, the distance between the popup arrow and the four corners must be no less than the corner radius.

2\. If **arrowPointPosition** is set, **arrowOffset** does not take effect.

3\. Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| arrowPointPosition11+ | [ArrowPointPosition](../../../common-definitions/enums/document.md#arrowpointposition11) | No | Yes | 

Position of the tooltip arrow relative to its parent component. Available positions are **START**, **CENTER**, and **END**, in both vertical and horizontal directions. All these positions are within the parent component area.

Default value: **ArrowPointPosition.CENTER**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| arrowWidth11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Arrow thickness. If the arrow thickness exceeds the length of the edge minus twice the size of the popup rounded corner, the arrow is not drawn.

Default value: **16**

Unit: vp

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| arrowHeight11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Arrow height.

Default value: **8**

Unit: vp

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| showInSubWindow9+ | boolean | No | Yes | 

Whether the popup is displayed in the created subwindow.

**true**: The popup is displayed in the created subwindow; **false**: The popup is displayed in the corresponding main window.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskColor(deprecated) | [Color](../../../common-definitions/enums/document.md#color) | string | [Resource](../../../common-definitions/basic-types/document.md#resource) | number | No | Yes | 

Color of the popup mask.

**NOTE**

This parameter is deprecated since API version 10. You are advised to use **mask** instead.

 |
| mask10+ | boolean | { color : [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) } | No | Yes | 

Whether to apply a mask with the specified color to the popup. The value **true** means to apply a transparent mask to the popup, **false** means not to apply a mask to the popup, and a color value means to apply a mask in the corresponding color to the popup. Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| targetSpace10+ | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Spacing between the popup and the host node. Percentage values are not supported.

Default value: **8**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offset10+ | [Position](../../../common-definitions/basic-types/document.md#position) | No | Yes | 

Offset of the popup relative to the display position specified by **placement**.

**NOTE**

Percentage values are not supported.

Default value: **{x:0, y:0}**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| width11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the popup. If this parameter is not set or the value is invalid, the popup width is automatically adjusted to adapt to the content width.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| radius11+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Rounded corner radius of the popup.

Default value: **20**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow11+ | [ShadowOptions](../../visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Popup shadow.

Default value: **ShadowStyle.OUTER\_DEFAULT\_MD**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle11+ | [BlurStyle](../../basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the popup.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| focusable11+ | boolean | No | Yes | 

Whether the popup obtains focus when displayed.

**true**: The popup can obtain the focus; **false**: The popup cannot obtain the focus.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| transition12+ | [TransitionEffect](../../../animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition animations for the entrance and exit of the popup.

**NOTE**

If this parameter is not set, the default effect is used.

2\. Touching the back button during the entrance animation interrupts it and starts the exit animation. The final effect is one obtained after the curves of the entrance and exit animations are combined.

3\. Touching the back button during the exit animation does not affect the animation playback; the back button is unresponsive.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDismiss12+ | boolean | Callback<[DismissPopupAction](#dismisspopupaction12)\> | No | Yes | 

Interactive dismissal behavior. The default value is **true**, meaning that the popup responds to clicks, swipes (left or right), and the back button.

1\. For the boolean type, if this parameter is set to **false**, the popup ignores clicks, swipes, back button, route navigation, and **Esc** key events, and can only be dismissed by setting the **show** parameter to **false**; if this parameter is set to **true**, the popup responds to dismissal events.

2\. If this parameter is set to a function, the dismissal event is intercepted and the callback function is executed. For swipes, back button, route navigation, and the **Esc** key, the value of **reason** returned in the callback function is **PRESS\_BACK**. For clicks, the value is **TOUCH\_OUTSIDE**.

**NOTE**

Nesting **onWillDismiss** callbacks is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| followTransformOfTarget13+ | boolean | No | Yes | 

Whether the popup aligns with the transformed position of the target when the target component or its parent container has transformations (such as rotation and scaling).

**true**: The popup aligns with the transformed position of the target; **false**: The popup does not track such transformations, which may result in incorrect display.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| keyboardAvoidMode15+ | [KeyboardAvoidMode](#keyboardavoidmode12) | No | Yes | 

Whether to avoid the soft keyboard. By default, the popup does not avoid the soft keyboard. When configured to avoid the soft keyboard, if the popup display space is insufficient, the display mode of the popup changes from being centered over the parent component to being translated and covering the parent component.. In addition, if the popup arrow does not point to the host, the arrow will not be displayed.

Default value: **KeyboardAvoidMode.NONE**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| enableHoverMode18+ | boolean | No | Yes | 

Whether the popup responds when the device is in hover mode (semi-folded state), that is, whether it triggers avoidance of the crease area in hover mode.

Default value: **false** (**true** for 2-in-1 devices by default). If this parameter is not set or set to an invalid value, the default value is used.

**NOTE**

1\. If the popup position is within the crease area in hover mode, it will not respond in hover mode.

2\. This parameter is supported on 2-in-1 devices since API version 20.

3\. This parameter only takes effect in window waterfall mode for 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| outlineWidth20+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the outer outline of the popup.

Default value: **1**

Unit: vp

**NOTE**

1\. Percentage values are not supported. If a percentage value is set, the value **0** is used.

2\. If the outer outline is not set, this parameter must be used together with **outlineLinearGradient**.

3\. For double outlines, it is recommended that the outer outline width should not exceed 10 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| borderWidth20+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the inner outline of the popup.

Default value: **1**

Unit: vp

**NOTE**

1\. Percentage values are not supported. If a percentage value is set, the value **0** is used.

2\. If no inner outline is set, this parameter must be used together with **borderLinearGradient**.

3\. For double outlines, it is recommended that the inner outline width should not exceed 10 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| outlineLinearGradient20+ | [PopupBorderLinearGradient](#popupborderlineargradient20) | No | Yes | 

Linear gradient color of the outer outline of the popup.

**NOTE**

1\. If **outlineLinearGradient** is not set or set to **null** or **undefined**, the linear gradient color of the outer outline does not take effect.

2\. When **outlineLinearGradient** is set, the default value of **direction** is **GradientDirection.Bottom**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| borderLinearGradient20+ | [PopupBorderLinearGradient](#popupborderlineargradient20) | No | Yes | 

Linear gradient color of the inner outline of the popup.

**NOTE**

1\. If **borderLinearGradient** is not set or set to **null** or **undefined**, the linear gradient color of the inner outline does not take effect.

2\. When **borderLinearGradient** is set, the default value of **direction** is **GradientDirection.Bottom**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| avoidTarget20+ | [AvoidanceMode](../../../buttons-and-selections/select/document.md#avoidancemode19) | No | Yes | 

Whether the popup covers the pointing component during avoidance.

**NOTE**

When **avoidTarget** is set to **AvoidanceMode.AVOID\_AROUND\_TARGET**, the popup is compressed if the remaining display space is insufficient. In this case, the popup content needs to be used together with **Scroll**. Otherwise, the popup content will be blocked.

Default value: **AvoidanceMode.COVER\_TARGET**

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### PopupCommonOptions18+

Configures the parameters of a popup. You can use the [getPromptAction()](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object, and then call the attributes of **options** when [openPopup](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#openpopup18) or [updatePopup](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatepopup18) is called.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| placement | [Placement](../../../common-definitions/enums/document.md#placement8) | No | Yes | 
Preferred position of the tooltip component. If the set position is insufficient for holding the component, it will be automatically adjusted.

Default value: **Placement.Bottom**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| popupColor | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the popup. To remove the background blur, set **backgroundBlurStyle** to **BlurStyle.NONE**. Default value: [TRANSPARENT](../../../common-definitions/enums/document.md#color) plus [COMPONENT\_ULTRA\_THICK](../../basic-attributes/background/document.md#blurstyle9)

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| autoCancel | boolean | No | Yes | 

Whether to automatically dismiss the popup when there is a page operation. The value **true** means to automatically dismiss the popup when there is a page operation, and **false** means the opposite.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onStateChange | [PopupStateChangeCallback](#popupstatechangecallback18) | No | Yes | 

Represents the callback invoked when the popup state changes.

**NOTE**

[updatePopup](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatepopup18) cannot be used for update.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| showInSubWindow | boolean | No | Yes | 

Whether to show the popup in a subwindow. The value **true** means to show the popup in a subwindow, and **false** means to show the popup in the main window.

Default value: **false**

**NOTE**

[updatePopup](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatepopup18) cannot be used for update.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| mask | boolean | [PopupMaskType](#popupmasktype18) | No | Yes | 

Whether to apply a mask with the specified color to the popup. The value **false** means that no mask is applied, **true** means that a transparent mask is applied, and **PopupMaskType** means that a mask with the specified color is applied. Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| targetSpace | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Spacing between the popup and the host node. Percentage values are not supported.

Default value: **8**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| offset | [Position](../../../common-definitions/basic-types/document.md#position) | No | Yes | 

Offset of the popup relative to the display position specified by **placement**.

**NOTE**

Percentage values are not supported.

Default value: **{x:0, y:0}**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| width | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the popup.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| enableArrow | boolean | No | Yes | 

Whether to display the arrow. The value **true** means to display the arrow, and **false** means the opposite.

If the position set for the popup is not large enough, the arrow will not be displayed. For example, if **placement** is set to **Left**, and the popup height is less than the sum of the arrow width (32 vp) and twice the popup corner radius (48 vp), that is, 80 vp, the arrow will not be displayed.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| arrowOffset | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Offset of the popup arrow relative to the popup.

When the arrow is at the top or bottom of the popup: The value **0** indicates that the arrow is located on the leftmost, and any other value indicates the distance from the arrow to the leftmost; the arrow is centered by default.

When the arrow is on the left or right side of the popup: The value indicates the distance from the arrow to the top; the arrow is centered by default.

When the popup is displayed on either edge of the screen, it automatically adjusts horizontally. When the value is **0**, the arrow always points to the bound component.

Unit: vp

**NOTE**

1\. If **arrowOffset** is not set, the distance between the popup arrow and the four corners must be no less than the corner radius.

2\. If **arrowPointPosition** is set, **arrowOffset** does not take effect.

3\. Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| arrowPointPosition | [ArrowPointPosition](../../../common-definitions/enums/document.md#arrowpointposition11) | No | Yes | 

Position of the tooltip arrow relative to its parent component. Available positions are **START**, **CENTER**, and **END**, in both vertical and horizontal directions. All these positions are within the parent component area.

Default value: **ArrowPointPosition.CENTER**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| arrowWidth | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Arrow thickness. If the arrow thickness exceeds the length of the edge minus twice the size of the popup rounded corner, the arrow is not drawn.

Default value: **16**

Unit: vp

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| arrowHeight | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Arrow height.

Default value: **8**

Unit: vp

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| radius | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Rounded corner radius of the popup.

Default value: **20**

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| shadow | [ShadowOptions](../../visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Popup shadow.

Default value: **ShadowStyle.OUTER\_DEFAULT\_MD**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| backgroundBlurStyle | [BlurStyle](../../basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the popup.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| focusable | boolean | No | Yes | 

Whether the popup obtains focus when displayed.

**true**: The popup can obtain the focus; **false**: The popup cannot obtain the focus.

Default value: **false**

**NOTE**

[updatePopup](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatepopup18) cannot be used for update.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| transition | [TransitionEffect](../../../animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition animations for the entrance and exit of the popup.

**NOTE**

1\. If this parameter is not set, the default effect is used.

2\. Touching the back button during the entrance animation interrupts it and starts the exit animation. The final effect is one obtained after the curves of the entrance and exit animations are combined.

3\. Touching the back button during the exit animation does not affect the animation playback; the back button is unresponsive.

4\. [updatePopup](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatepopup18) cannot be used for update.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onWillDismiss | boolean|Callback<[DismissPopupAction](#dismisspopupaction12)\> | No | Yes | 

Interactive dismissal behavior. The default value is **true**, meaning that the popup responds to clicks, swipes (left or right), and the back button.

1\. For the boolean type, if this parameter is set to **false**, the popup ignores clicks, swipes, back button, route navigation, and **Esc** key events, and can only be dismissed by setting the **show** parameter to **false**; if this parameter is set to **true**, the popup responds to dismissal events.

2\. If this parameter is set to a function, the dismissal event is intercepted and the callback function is executed. For swipes, back button, route navigation, and the **Esc** key, the value of **reason** returned in the callback function is **PRESS\_BACK**. For clicks, the value is **TOUCH\_OUTSIDE**.

**NOTE**

1\. No further interception with **onWillDismiss** is allowed in an **onWillDismiss** callback.

2\. [updatePopup](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatepopup18) cannot be used for update.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| followTransformOfTarget | boolean | No | Yes | 

Whether the popup aligns with the transformed position of the target when the target component or its parent container has transformations (such as rotation and scaling).

**true**: The popup aligns with the transformed position of the target; **false**: The popup does not track such transformations, which may result in incorrect display.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| enableHoverMode | boolean | No | Yes | 

Whether the popup responds when the device is in hover mode (semi-folded state), that is, whether it triggers avoidance of the crease area in hover mode.

Default value: **false** (**true** for 2-in-1 devices by default). If this parameter is not set or set to an invalid value, the default value is used.

**NOTE**

1\. If the popup position is within the crease area in hover mode, it will not respond in hover mode.

2\. This parameter is supported on 2-in-1 devices since API version 20.

3\. This parameter only takes effect in window waterfall mode for 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| outlineWidth20+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the outer outline of the popup.

Default value: **1**

Unit: vp

**NOTE**

1\. Percentage values are not supported. If a percentage value is set, the value **0** is used.

2\. If the outer outline is not set, this parameter must be used together with **outlineLinearGradient**.

3\. For double outlines, it is recommended that the outer outline width should not exceed 10 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| borderWidth20+ | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the inner outline of the popup.

Default value: **1**

Unit: vp

**NOTE**

1\. Percentage values are not supported. If a percentage value is set, the value **0** is used.

2\. If no inner outline is set, this parameter must be used together with **borderLinearGradient**.

3\. For double outlines, it is recommended that the inner outline width should not exceed 10 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| outlineLinearGradient20+ | [PopupBorderLinearGradient](#popupborderlineargradient20) | No | Yes | 

Linear gradient color of the outer outline of the popup.

**NOTE**

1\. If **outlineLinearGradient** is not set or set to **null** or **undefined**, the linear gradient color of the outer outline does not take effect.

2\. When **outlineLinearGradient** is set, the default value of **direction** is **GradientDirection.Bottom**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| borderLinearGradient20+ | [PopupBorderLinearGradient](#popupborderlineargradient20) | No | Yes | 

Linear gradient color of the inner outline of the popup.

**NOTE**

1\. If **borderLinearGradient** is not set or set to **null** or **undefined**, the linear gradient color of the inner outline does not take effect.

2\. When **borderLinearGradient** is set, the default value of **direction** is **GradientDirection.Bottom**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| avoidTarget20+ | [AvoidanceMode](../../../buttons-and-selections/select/document.md#avoidancemode19) | No | Yes | 

Whether the popup covers the pointing component during avoidance.

**NOTE**

When **avoidTarget** is set to **AvoidanceMode.AVOID\_AROUND\_TARGET**, the popup is compressed if the remaining display space is insufficient. In this case, the popup content needs to be used together with **Scroll**. Otherwise, the popup content will be blocked.

Default value: **AvoidanceMode.COVER\_TARGET**

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### PopupStateChangeParam18+

Display state of the popup.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isVisible | boolean | No | No | Display state of the popup. It returns **true** when the popup transitions from closed to open, and **false** when the popup transitions from open to closed. |

#### PopupStateChangeCallback18+

type PopupStateChangeCallback = (event: PopupStateChangeParam) => void;

Represents the callback invoked when the popup state changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [PopupStateChangeParam](#popupstatechangeparam18) | Yes | Display state of the popup. |

#### PopupMaskType18+

Sets the color of the mask.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | No | Color of the mask. |

#### PopupBorderLinearGradient20+

Sets the color and direction of the linear gradient for the outlines.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| direction | [GradientDirection](../../../common-definitions/enums/document.md#gradientdirection) | No | Yes | 
Direction of the linear gradient.

Default value: **GradientDirection.Bottom**

**NOTE**

When the direction is set to **GradientDirection.None**, the default value is used.

 |
| colors | Array<\[[ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor), number\]> | No | No | 

Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**NOTE**

For details about how to set colors, see [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor). Colors that are not within the types of [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) are invalid.

If the color in the array is set to **undefined** or **null**, the default color is black.

When using the **colors** parameter, take note of the following:

[ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) indicates the color, and **number** indicates the color's position, which ranges from 0 to 1.0: **0** indicates the start of the gradient color container, and **1.0** indicates the end of the container. To create a gradient with multiple color stops, you are advised to set the **number** values in ascending order. If a value of **number** in an array is smaller than that in the previous one, the value of **number** in the previous array is used.

 |

#### KeyboardAvoidMode12+

Enumerates modes in which a popup responds when the keyboard is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Automatically avoids the soft keyboard and compresses the height when reaching the maximum limit. |
| NONE | 1 | Does not avoid the soft keyboard. |

#### Example

## Example 1: Displaying Different Types of Popups

This example shows how to configure the **keyboardAvoidMode** attribute in [PopupOptions](#popupoptions) or [CustomPopupOptions](#custompopupoptions8) to determine whether the popup avoids the soft keyboard.

The **keyboardAvoidMode** attribute is added to **PopupOptions** and **CustomPopupOptions** since API version 15.

// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;
  @State customPopup: boolean = false;

  // Popup builder
  @Builder popupBuilder() {
    Row({ space: 2 }) {
      // Replace $r('app.media.icon') with the image resource file you use.
      Image($r("app.media.icon")).width(24).height(24).margin({ left: -5 })
      Text('Custom Popup').fontSize(10)
    }.width(100).height(50).padding(5)
  }

  build() {
    Flex({ direction: FlexDirection.Column }) {
      // PopupOptions for setting the popup
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
          placement: Placement.Top,
          showInSubWindow:false,
          keyboardAvoidMode: KeyboardAvoidMode.DEFAULT, // Set the popup to avoid the soft keyboard.
          primaryButton: {
            value: 'confirm',
            action: () => {
              this.handlePopup = !this.handlePopup;
              console.info('confirm Button click');
            }
          },
          // Secondary button
          secondaryButton: {
            value: 'cancel',
            action: () => {
              this.handlePopup = !this.handlePopup;
              console.info('cancel Button click');
            }
          },
          onStateChange: (e) => {
            console.info(JSON.stringify(e.isVisible))
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          }
        })
        .position({ x: 100, y: 150 })

      // CustomPopupOptions for setting the popup
      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Top,
          mask: {color:'#33000000'},
          popupColor: Color.Yellow,
          enableArrow: true,
          keyboardAvoidMode: KeyboardAvoidMode.DEFAULT, // Set the popup to avoid the soft keyboard.
          showInSubWindow: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          }
        })
        .position({ x: 80, y: 300 })
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/XBDbjULoTyeSPACKcj3Ddw/en-us_image_0000002537925398.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C4B3F4445E924A1DF68295985BB89763086A6E24CE71967863E79898755596D)

## Example 2: Setting the Popup Text Style

In this example, the **messageOptions** attribute in [PopupOptions](#popupoptions) is configured to display a popup with a custom text style.

// xxx.ets

@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;

  build() {
    Column({ space: 100 }) {
      Button('PopupOptions').margin(100)
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          // Popup of the PopupOptions type
          message: 'This is a popup with PopupOptions',
          messageOptions: {
            // Text style of the popup
            textColor: Color.Red,
            font: {
              size: '14vp',
              style: FontStyle.Italic,
              weight: FontWeight.Bolder
            }
          },
          placement: Placement.Bottom,
          enableArrow: false, // Set the arrow not to display.
          targetSpace: '15vp',
          onStateChange: (e) => {
            console.info(JSON.stringify(e.isVisible));
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          }
        })
    }.margin(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/rT3ViM9uTBOadfyJfzpSvg/en-us_image_0000002568685175.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FD70F2852047DC6E442B25CC67EE7028EC09C3661A914CDE517102BF16D409B)

## Example 3: Setting the Popup Style

This example sets the **arrowHeight**, **arrowWidth**, **radius**, **shadow**, and **popupColor** attributes in [PopupOptions](#popupoptions) to implement the style of the popup arrow and the popup itself.

// xxx.ets

@Entry
@Component
struct PopupExample {
  @State customPopup: boolean = false;
  @State handlePopup: boolean = false;

  build() {
    Column({ space: 100 }) {
      Button("popup")
        .margin({ top: 50 })
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup!!, {
          message: "this is a popup",
          arrowHeight: 20, // Set the height for the popup arrow.
          arrowWidth: 20, // Set the width for the popup arrow.
          radius: 20, // Set the corner radius of the popup.
          shadow: ShadowStyle.OUTER\_DEFAULT\_XS, // Set the shadow for the popup.
        })

      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup!!, {
          width: 300,
          message: 'This is a popup with PopupOptions',
          arrowPointPosition: ArrowPointPosition.START, // Set the position for the popup arrow.
          backgroundBlurStyle: BlurStyle.NONE, // Disable the background blur for the popup.
          popupColor: Color.Red, // Set the background color for the popup.
          autoCancel: true,
        })
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/19qMfV9xTdu5uWm9C5v43Q/en-us_image_0000002568765185.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C605FD73E45B39CB557BE35749793C217BBAC8675A56E5406D37B57CC204845)

## Example 4: Setting the Popup Animation

This example shows how to configure the **transition** attribute in [PopupOptions](#popupoptions) or [CustomPopupOptions](#custompopupoptions8) to implement the entrance and exit animations on the popup.

// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;
  @State customPopup: boolean = false;

  // Popup builder
  @Builder
  popupBuilder() {
    Row() {
      Text('Custom Popup with transitionEffect').fontSize(10)
    }.height(50).padding(5)
  }

  build() {
    Flex({ direction: FlexDirection.Column }) {
      // PopupOptions for setting the popup
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with transitionEffect',
          placement: Placement.Top,
          showInSubWindow: false,
          onStateChange: (e) => {
            console.info(JSON.stringify(e.isVisible))
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          },
          // Set the popup animation to a combination of opacity and translation effects, with no exit animation.
          transition: TransitionEffect.asymmetric(
            TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Ease }).combine(
              TransitionEffect.translate({ x: 50, y: 50 })),
            TransitionEffect.IDENTITY)
        })
        .position({ x: 100, y: 150 })

      // CustomPopupOptions for setting the popup
      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Top,
          showInSubWindow: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          },
          // Set the popup entrance and exit animations to be a scaling effect.
          transition: TransitionEffect.scale({ x: 1, y: 0 }).animation({ duration: 500, curve: Curve.Ease })
        })
        .position({ x: 80, y: 300 })
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Ak2CPeTLT2qP7zoyPSIBxw/en-us_image_0000002537765460.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7D6B6BA4346AF8C3C996D749BB0F600907517B682873E3E75BD0BC9FA44B91D)

## Example 5: Adding an Event to a Popup

This example shows how to use the **onWillDismiss** attribute in [PopupOptions](#popupoptions) to intercept popup dismissal events and execute callback functions.

// xxx.ets

@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;
  build() {
    Column() {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = true;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
          messageOptions: {
            textColor: Color.Red,
            font: {
              size: '14vp',
              style: FontStyle.Italic,
              weight: FontWeight.Bolder
            }
          },
          placement: Placement.Bottom,
          enableArrow: false,
          targetSpace: '15vp',
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          },
          onWillDismiss: (
            (dismissPopupAction: DismissPopupAction) => {
              console.info("dismissReason:" + JSON.stringify(dismissPopupAction.reason));
              if (dismissPopupAction.reason === DismissReason.PRESS\_BACK) {
                dismissPopupAction.dismiss();
              }
            }
          )
        })
    }.margin(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/YakGRtURToaNiU-yMufzhw/en-us_image_0000002537925400.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF5F5C0DBC90C47EA353E1147ABB5DC34EF93653396C0624C44FDB2653787B5C)

## Example 6: Intercepting the Popup Dismissal Event

This example demonstrates how to set the **onWillDismiss** attribute in [PopupOptions](#popupoptions) to **false** to intercept popup dismissal events. In addition, configuring the **followTransformOfTarget** attribute in [PopupOptions](#popupoptions) sets whether the popup follows and displays at the corresponding position when the host component's position is transformed.

// xxx.ets

@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;

  build() {
    Column() {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = true;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
          messageOptions: {
            textColor: Color.Red,
            font: {
              size: '14vp',
              style: FontStyle.Italic,
              weight: FontWeight.Bolder
            }
          },
          placement: Placement.Bottom,
          enableArrow: false,
          targetSpace: '15vp',
          followTransformOfTarget: true,
          onStateChange: (e) => {
            let timer = setTimeout(() => {
              this.handlePopup = false;
            }, 6000);
            if (!e.isVisible) {
              this.handlePopup = false;
              clearTimeout(timer);
            }
          },
          onWillDismiss: false
        })
    }.margin(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/-DIhW-j2QFOvFeuCdndE1w/en-us_image_0000002568685177.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3C381CA68E053D12D0235F575531E009F6B9981F1B6A16EBA5FD71A0A21C2A5)

## Example 7: Setting the Linear Gradient for the Inner and Outer Outlines of a Popup

This example configures the **outlineWidth**, **borderWidth**, **outlineLinearGradient**, and **borderLinearGradient** attributes in [PopupOptions](#popupoptions) to set the color and direction of the linear gradient of the inner and outer outlines of the popup.

The **outlineWidth**, **borderWidth**, **outlineLinearGradient**, and **borderLinearGradient** attributes are added to **PopupOptions** since API version 20.

// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup
        })
        .bindPopup(this.handlePopup!!, {
          message: 'This is a popup with PopupOptions',
          placement: Placement.Top,
          outlineWidth: 1,
          outlineLinearGradient: {
            direction: GradientDirection.Top,
            colors: \[\[Color.Yellow, 0.0\], \[Color.Green, 1.0\]\]
          },
          borderWidth: 1,
          borderLinearGradient: {
            direction: GradientDirection.Bottom,
            colors: \[\[Color.Red, 0.0\], \[Color.Blue, 1.0\]\]
          }
        })
        .position({ x: 100, y: 150 })
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/ke3cmay8Rt2q5TUaADMzqg/en-us_image_0000002568765187.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2280E27F71A4DF8D52A46EFA1BE2AE9231608286786DC17F12BE8BB713E8F5A7)

## Example 8: Setting the Host Avoidance Mode for Popups

This example configures the **avoidTarget** attribute of [PopupOptions](#popupoptions) to enable the popup to avoid the bound component.

The **avoidTarget** attribute is added to **PopupOptions** since API version 20.

// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup
        })
        .bindPopup(this.handlePopup!!, {
          message: 'popup message '.repeat(200),
          placement: Placement.Top,
          avoidTarget: AvoidanceMode.AVOID\_AROUND\_TARGET,
        })
        .position({ x: 100, y: 150 })
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/6RXuKRW2T1mI2cOCogGQ6g/en-us_image_0000002537765462.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BEFEDE93DB1150817BCF743813B1F523A78AA9D413B2377D6DDF967605346DD)
