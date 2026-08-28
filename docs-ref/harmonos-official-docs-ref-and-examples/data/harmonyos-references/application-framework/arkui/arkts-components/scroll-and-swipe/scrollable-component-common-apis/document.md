# Scrollable Component Common APIs

The common attributes and events for scrollable components currently only support the [List](../list/document.md), [Grid](../grid/document.md), [Scroll](../scroll/document.md), and [WaterFlow](../waterflow/document.md) components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/009gJmxKS_G5k-LC907tcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44E0C6427B8213D8E488EA7B16A7BA23B8DA472A862876F21073469D2E1750CA)

The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Attributes

#### \[h2\]scrollBar11+

scrollBar(barState: BarState): T

Sets the scrollbar state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| barState | [BarState](../../common-definitions/enums/document.md#barstate) | Yes | 
Scrollbar state.

Default value: **BarState.Auto** for the **List**, **Grid**, and **Scroll** components and **BarState.Off** for the **WaterFlow** component

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]scrollBarColor11+

scrollBarColor(color: Color | number | string): T

Sets the scrollbar color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Color](../../common-definitions/enums/document.md#color) | number | string | Yes | 
Scrollbar color.

Default value: **'#182431'** (40% opacity)

A number value indicates a HEX color in RGB or ARGB format, for example, **0xffffff**. A string value indicates a color in RGB or ARGB format, for example, **'#ffffff'**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]scrollBarColor22+

scrollBarColor(color: Color | number | string | Resource): T

Sets the scrollbar color. Compared with [scrollBarColor11+](#scrollbarcolor11), this API supports the Resource type for the **color** parameter.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Color](../../common-definitions/enums/document.md#color) | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Scrollbar color.

Default value: **'#182431'** (40% opacity)

A number value indicates a HEX color in RGB or ARGB format, for example, **0xffffff**. A string value indicates a color in RGB or ARGB format, for example, **'#ffffff'**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]scrollBarWidth11+

scrollBarWidth(value: number | string): T

Sets the scrollbar width. This attribute cannot be set in percentage. After the width is set, the scrollbar is displayed with the set width in normal state and pressed state. If the set width exceeds the height of the scrollable component on the main axis, the scrollbar reverts to the default width.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Scrollbar width.

Default value: **4**

Unit: vp

If this parameter is set to a value less than or equal to 0, the default value is used. The value **0** means not to show the scrollbar.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]edgeEffect11+

edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T

Sets the effect used when the scroll boundary is reached.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| edgeEffect | [EdgeEffect](../../common-definitions/enums/document.md#edgeeffect) | Yes | 
Effect used when the scroll boundary is reached. The spring and shadow effects are supported.

Default value: **EdgeEffect.None** for the **Grid**, **Scroll**, and **WaterFlow** components and **EdgeEffect.Spring** for the **List** component

 |
| options | [EdgeEffectOptions](#edgeeffectoptions11) | No | 

Whether edge effects are enabled when content is smaller than component size, and effective edges. The value **{ alwaysEnabled: true }** means to enable the scroll effect, and **{ alwaysEnabled: false }** means the opposite.

Default value:

For the **List**, **Grid**, and **WaterFlow** components, the default value is **{ alwaysEnabled: false, EffectEdge: EffectEdge.START | EffectEdge.END}**. For the **Scroll** component, the default value is **{ alwaysEnabled: true, EffectEdge: EffectEdge.START | EffectEdge.END}**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]nestedScroll11+

nestedScroll(value: NestedScrollOptions): T

Sets the nested scrolling mode in the forward and backward directions to implement scrolling linkage with the parent component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NestedScrollOptions](#nestedscrolloptions10) | Yes | 
Nested scrolling options.

Default value: **{ scrollForward: NestedScrollMode.SELF\_ONLY, scrollBackward: NestedScrollMode.SELF\_ONLY }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]enableScrollInteraction11+

enableScrollInteraction(value: boolean): T

Sets whether to support scroll gestures.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to support scroll gestures. With the value **true**, scrolling via finger or mouse is enabled. With the value **false**, scrolling via finger or mouse is disabled, but this does not affect the scrolling APIs of the [Scroller](../scroll/document.md#scroller).

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]friction11+

friction(value: number | Resource): T

Sets the friction coefficient. It applies only to gestures in the scrolling area, and it affects only indirectly the scroll chaining during the inertial scrolling process. If this attribute is set to a value less than or equal to 0, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Friction coefficient.

Default value: **0.6** for non-wearable devices and **0.9** for wearable devices.

Since API version 11, the default value for non-wearable devices is **0.7**.

Since API version 12, the default value for non-wearable devices is **0.75**.

Value range: (0, +∞). If this parameter is set to a value less than or equal to 0, the default value is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]flingSpeedLimit11+

flingSpeedLimit(speedLimit: number): T

Sets the maximum initial speed for inertial animation after a fling gesture.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/vY98f99gTr2OuGzzuOoJvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=829AE90822B0A451CAA2566A9AD5229A712505515D35F63D53EE702464D3274B)

-   Inertial animation is the effect that the scrolling content continues to scroll and gradually decelerates and stops after the finger quickly flings and leaves the screen. It is also called inertial scrolling.
    
-   Inertial animation is triggered when the finger quickly flings and leaves the screen, or when the [fling](../scroll/document.md#fling12) method is called.
    
-   Inertial animation is not generated when the mouse wheel or keyboard arrow keys are used to scroll, or when the [scrollTo](../scroll/document.md#scrollto) method is used to scroll to a specified position.
    
-   If the inertial animation is triggered by the [fling](../scroll/document.md#fling12) method, the **flingSpeedLimit** setting does not take effect.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speedLimit | number | Yes | 
Maximum initial speed for inertial animation.

Default value: **9000**

Unit: vp/s

Value range: (0, +∞). If this parameter is set to a value less than or equal to 0, the default value is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]fadingEdge14+

fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T

Sets whether to enable the edge fading effect and the length of the fading edge.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/i-CFahfNTD2rOrv8FD4sag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA5C72CEFEECD8C19F119B00115712B191DDCA214C9EE072A95393C2C020DB62)

The **fadingEdge** effect is implemented by configuring the [overlay](../../universal-attributes/basic-attributes/overlay-control/document.md#overlay) and [blendMode](../../universal-attributes/visual-effects/image-effect/document.md#blendmode11) attributes (parameter values: **BlendMode.SRC\_OVER** and **BlendApplyType.OFFSCREEN**). When the **fadingEdge** effect takes effect, the **.overlay()** and **.blendMode()** attributes of the original component are overwritten. As a result, the screenshot APIs of the current component and its child components cannot capture the correct image. APIs that require screen capture: [blur](../../universal-attributes/visual-effects/image-effect/document.md#blur), [linearGradientBlur](../../universal-attributes/visual-effects/image-effect/document.md#lineargradientblur12), [brightness](../../universal-attributes/visual-effects/image-effect/document.md#brightness), [visualEffect](../../universal-attributes/visual-effects/visual-effect/document.md#visualeffect), [grayscale](../../universal-attributes/visual-effects/image-effect/document.md#grayscale), [saturate](../../universal-attributes/visual-effects/image-effect/document.md#saturate), [contrast](../../universal-attributes/visual-effects/image-effect/document.md#contrast), [invert](../../universal-attributes/visual-effects/image-effect/document.md#invert), [sepia](../../universal-attributes/visual-effects/image-effect/document.md#sepia), [hueRotate](../../universal-attributes/visual-effects/image-effect/document.md#huerotate), [colorBlend](../../universal-attributes/visual-effects/image-effect/document.md#colorblend), [lightUpEffect](../../universal-attributes/visual-effects/image-effect/document.md#lightupeffect12), [pixelStretchEffect](../../universal-attributes/visual-effects/image-effect/document.md#pixelstretcheffect12), [blendMode](../../universal-attributes/visual-effects/image-effect/document.md#blendmode11) and [backgroundBrightness](../../universal-attributes/basic-attributes/background/document.md#backgroundbrightness12).

When **fadingEdge** is enabled, avoid setting [background](../../universal-attributes/basic-attributes/background/document.md#background10)\-related attributes on the component with **fadingEdge**, as this may interfere with the fade effect.

With **fadingEdge** set to **true**, the component is clipped to the boundary, and setting the component's [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) attribute to **false** will not take effect.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable the edge fading effect. **true** to enable, **false** otherwise.

Default value: **false**.

 |
| options | [FadingEdgeOptions](#fadingedgeoptions14) | No | 

Object defining edge fading effect properties, such as the fading edge length.

If the value is less than 0, undefined, or not set, the default value is used. The default length is 32 vp.

If the value exceeds half the height of the container, it is adjusted to exactly half the height of the container.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]clipContent14+

clipContent(clip: ContentClipMode | RectShape): T

Sets the content clipping area for this scrollable component.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| clip | [ContentClipMode](#contentclipmode14) | [RectShape](../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#rectshape) | Yes | 
Clipping to apply, which is effective only for the content (that is, child components) of the scrollable component, not the background. When a custom rectangular area is passed through **RectShape**, only width, height, and [offset](../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#offset) relative to the component's upper left corner are supported, and rounded corners are not supported.

Default value: The default value for **Grid** and **Scroll** is **ContentClipMode.BOUNDARY**, and the default value for **List** and **WaterFlow** is **ContentClipMode.CONTENT\_ONLY**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]backToTop15+

backToTop(backToTop: boolean): T

Sets whether to enable the back-to-top feature for the scrollable component when the status bar is touched.

When a status bar touch event is received, the scrollable component on the current page can scroll to the top with an animation. This behavior does not affect scrollable components in background applications, which will not scroll to the top. This attribute is independent of the [enableScrollInteraction](#enablescrollinteraction11) setting.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| backToTop | boolean | Yes | 
Whether to enable the back-to-top feature for the scrollable component when the status bar is touched. **true** to enable, **false** otherwise.

Default value:

Versions earlier than API version 18: **false**

API version 18 and later: **false** for horizontal scrolling and **true** for vertical scrolling

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]scrollBarMargin20+

scrollBarMargin(margin: ScrollBarMargin): T

Sets the margin of the scrollbar. The margin is calculated from the offset distance where the scrollbar avoids corners. If the scrollbar area is smaller than the minimum scrollbar length, the scrollbar remains hidden.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| margin | [ScrollBarMargin](../../common-definitions/basic-types/document.md#scrollbarmargin20) | Yes | 
Start and end margins of the scrollbar.

Default value: {start: LengthMetrics.vp(0), end: LengthMetrics.vp(0)}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]digitalCrownSensitivity18+

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T

Sets the sensitivity of the digital crown's response to events.

A component must have focus to receive [crown events](../../universal-events/basic-input-events/crown-event/document.md). Focus control can be managed using [focusable](../../universal-attributes/interaction-properties/focus-control/document.md#focusable), [defaultFocus](../../universal-attributes/interaction-properties/focus-control/document.md#defaultfocus9), and [focusOnTouch](../../universal-attributes/interaction-properties/focus-control/document.md#focusontouch9).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sensitivity | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[CrownSensitivity](../../common-definitions/enums/document.md#crownsensitivity18)\> | Yes | 
Sensitivity to the digital crown rotation.

Default value: **CrownSensitivity.MEDIUM**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]contentStartOffset22+

contentStartOffset(offset: number | Resource): T

Sets the offset from the start of the content area. When the component scrolls to the start position, the content area maintains a specified distance from the component's display boundary.

If the combined value of contentStartOffset and contentEndOffset exceeds the scrollable content area length, both offsets are reset to 0.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Offset from the start of the content to the boundary of the content area.

Default value: **0**

Unit: vp

Invalid values (negative numbers or non-numeric Resource values) revert to the default value.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]contentEndOffset22+

contentEndOffset(offset: number | Resource): T

Sets the offset from the end of the content area. When the component scrolls to the end position, the content area maintains a specified distance from the component's display boundary.

If the combined value of contentStartOffset and contentEndOffset exceeds the scrollable content area length, both offsets are reset to 0.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Offset from content end to component display boundary.

Default value: **0**

Unit: vp

Invalid values (negative numbers or non-numeric Resource values) revert to the default value.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### Events

#### \[h2\]onReachStart11+

onReachStart(event: () => void): T

Triggered when the scrollable component reaches the start position.

This event is triggered once when the component is initialized and once when the component scrolls to the start position. If the edge effect is set to a spring effect, this event is triggered once when the swipe passes the start position, and triggered again when the swipe rebounds back to the start position.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when the scrollable component reaches the start position. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onReachEnd11+

onReachEnd(event: () => void): T

Triggered when the scrollable component reaches the end position.

If the edge effect is set to a spring effect, this event is triggered once when the swipe passes the end position, and triggered again when the swipe rebounds back to the end position.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when the scrollable component reaches the end position. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onScrollStart11+

onScrollStart(event: () => void): T

Triggered when the scrollable component starts scrolling initiated by the user's finger dragging the component or its scrollbar. For animated scrolling initiated via the [Scroller](../scroll/document.md#scroller) controller, this event is triggered when the animation starts.

Trigger conditions:

1.  The scrollable component starts scrolling, supporting various input settings including keyboard and mouse operations.
    
2.  Scrolling is initiated through scroller controller API calls with transition animation effects.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when scrolling starts. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onScrollStop11+

onScrollStop(event: () => void): T

Triggered when scrolling stops. This event is triggered when scrolling initiated by dragging the scrollable component or its scrollbar stops after the finger leaves the screen. For animated scrolling initiated via the [Scroller](../scroll/document.md#scroller) controller, this event is triggered when the animation stops.

Trigger conditions:

1.  The scrollable component stops scrolling, supporting various input settings including keyboard and mouse operations.
    
2.  The animation stops after scroller controller API calls with transition effects.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when scrolling stops. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onWillScroll12+

onWillScroll(handler: Optional<OnWillScrollCallback>): T

Triggered when the scrollable component is about to scroll.

The callback provides the amount of offset that is about to be scrolled in the current frame, along with the current scroll status and the source of the scrolling operation. The offset provided in the callback is the calculated intended scrolling offset, not the final actual scrolling offset. You can specify the intended scrolling offset for the scrollable component through the return value of this callback. The parameter type of the [onWillScroll](../scroll/document.md#onwillscroll12) API of the [Scroll](../scroll/document.md) component is [ScrollOnWillScrollCallback](../scroll/document.md#scrollonwillscrollcallback12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/JKSoiBfuTNSaD9p3-PjBCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71AC88CE0641BFF2412093400CC76A35D6FBD615007DA45235CB50F14311A39C)

-   This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 14.
    
-   When [ScrollEdge](../scroll/document.md#scrolledge) and [ScrollToIndex](../scroll/document.md#scrolltoindex) without animation are called, **onWillScroll** is not triggered.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[OnWillScrollCallback](#onwillscrollcallback12)\> | Yes | Callback triggered when the scrollable component is about to scroll. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/C0Bj7ZkpTY-TXl7Vp7k7hA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=991989F9E1F29E264902BD9F5C470CD69D15BAFB09E645D44C92F9BDB2E281E9)

**onWillScroll** is not triggered when **ScrollEdge** and **ScrollToIndex** without animation are called.

#### \[h2\]onDidScroll12+

onDidScroll(handler: OnScrollCallback): T

Triggered when the scrollable component scrolls. The return value is the offset amount by which the list has scrolled and the current scroll state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/wAZetpnmTcGccWnuS_djAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06690E1F533B813C08A99AFFF2DAAF0265B6AB360A98C38702A5117EADDBFA12)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 14.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [OnScrollCallback](#onscrollcallback12) | Yes | Callback triggered when the scrollable component scrolls. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onScroll(deprecated)

onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T

Triggered when the scrollable component scrolls.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/7NS2oh5lTtGMRLmGFcBZ4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2544545D28E6D3BF64FF1E85919188B115F33EB008F46A08DCCA34BB03697DA4)

This API is supported since API version 11 and deprecated since API version 12. If the **onScroll** events of the [List](../list/document.md), [Grid](../grid/document.md), and [WaterFlow](../waterflow/document.md) components are triggered after the layout, you are advised to use [onDidScroll](#ondidscroll12) instead. If the **onScroll** event of the [Scroll](../scroll/document.md) component is triggered before the layout, you are advised to use [onWillScroll](#onwillscroll12) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (scrollOffset: number, scrollState: [ScrollState](../list/document.md#scrollstate)) => void | Yes | 
Callback triggered when the scrollable component scrolls.

**scrollOffset**: offset relative to the previous frame. The offset is positive when the scrollable component is scrolled up and negative when it is scrolled down. Unit: vp

**scrollState**: current scroll state.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onWillStartDragging21+

onWillStartDragging(handler: VoidCallback): T

Triggered when the scrollable component starts to be dragged.

**Widget capability**: This API can be used in ArkTS widgets since API version 21.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback invoked when the scrollable component starts to be dragged. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onWillStopDragging20+

onWillStopDragging(handler: OnWillStopDraggingCallback): T

Triggered when the scrollable component is released. It is not triggered for scrolling via mouse wheel.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [OnWillStopDraggingCallback](#onwillstopdraggingcallback20) | Yes | Callback invoked when the scrollable component is released. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onDidStopDragging21+

onDidStopDragging(handler: OnDidStopDraggingCallback): T

Triggered when dragging of the scrollable component ends.

**Widget capability**: This API can be used in ArkTS widgets since API version 21.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [OnDidStopDraggingCallback](#ondidstopdraggingcallback21) | Yes | Callback invoked when the scrollable component stops being dragged. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onWillStartFling21+

onWillStartFling(handler: VoidCallback): T

Triggered when the scrollable component is about to initiate an inertial animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Re2VuPUeTuyYYQghqqcABA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F108B25AB7D1144F94AD1462C71D4BA1D6A6D018BFE25AB79E848E88880AD495)

-   If the inertial animation is triggered by the [fling](../scroll/document.md#fling12) method, **onWillStartFling** is not triggered.
    
-   For details about the triggering scenarios of the inertial animation, see the description of [flingSpeedLimit](#flingspeedlimit11).
    

**Widget capability**: This API can be used in ArkTS widgets since API version 21.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback invoked when the scrollable component is about to initiate an inertial animation. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### \[h2\]onDidStopFling21+

onDidStopFling(handler: VoidCallback): T

Triggered when the inertial animation of the scrollable component ends. It is not triggered if the animation is interrupted by a new swipe gesture.

**Widget capability**: This API can be used in ArkTS widgets since API version 21.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback invoked when the inertial animation of the scrollable component ends. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current scrollable component. |

#### ItemDragInfo

Provides information about the drag point.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | X-coordinate of the dragged item, in vp. |
| y | number | No | No | Y-coordinate of the dragged item, in vp. |

#### NestedScrollOptions10+

Implements an object used to configure the [nestedScroll](#nestedscroll11) attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scrollForward | [NestedScrollMode](../../common-definitions/enums/document.md#nestedscrollmode10) | No | No | Nested scrolling options when the scrollable component scrolls forward. |
| scrollBackward | [NestedScrollMode](../../common-definitions/enums/document.md#nestedscrollmode10) | No | No | Nested scrolling options when the scrollable component scrolls backward. |

#### EdgeEffectOptions11+

Implements an object used to configure the [edgeEffect](#edgeeffect11) attribute.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alwaysEnabled | boolean | No | No | 
Whether to enable the scroll effect when the component content is smaller than the component itself. **true** to enable, **false** otherwise. The default value is **false** for the [List](../list/document.md), [Grid](../grid/document.md), and [WaterFlow](../waterflow/document.md) components, and **true** for the [Scroll](../scroll/document.md) component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| effectEdge18+ | number | No | Yes | 

Edge where the edge effect is applied.

With **[EffectEdge](#effectedge18).START**, the edge effect is applied to the start edge only. With **[EffectEdge](#effectedge18).END**, the edge effect is applied to the end edge only.

The default value is [EffectEdge](#effectedge18).START | [EffectEdge](#effectedge18).END, which means that the edge effect is applied to both the start and end edges. If an invalid value is set, the edge effect is applied to both the start and end edges.

To disable the effect on both edges, set **edgeEffect** to **EdgeEffect.None**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### FadingEdgeOptions14+

Implements an object used to configure the [fadingEdge](#fadingedge14) attribute.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fadingEdgeLength | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Length of the fading edge. |

#### EffectEdge18+

Enumerates the edges where the edge effect is applied.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| START | 1 | Start edge. |
| END | 2 | End edge. |

#### ContentClipMode14+

Enumerates the content clipping modes for the scrollable container.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

The figure below illustrates the clipping areas corresponding to each enumeration value after the component has been configured with margin and padding attributes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0dS7jRVLQLyKaRf8Un-70g/en-us_image_0000002568685279.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=942747BC2E4B4B710F1BF978B8A0323A7A3E12F9BEDA7838237D8A30073A860F)

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTENT\_ONLY | 0 | Clip to the content area, corresponding to the green area in the figure. |
| BOUNDARY | 1 | Clip to the component area, corresponding to the entire blue area in the figure. |
| SAFE\_AREA | 2 | Clip to the safe area configured for the component, corresponding to the entire yellow area in the figure. |

#### OnWillScrollCallback12+

type OnWillScrollCallback = (scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult

Triggered when the scrollable component is about to scroll.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scrollOffset | number | Yes | 
Offset relative to the previous frame. The offset is positive when the scrollable component is scrolled up and negative when it is scrolled down.

Unit: vp

 |
| scrollState | [ScrollState](../list/document.md#scrollstate) | Yes | Current scroll state. |
| scrollSource | [ScrollSource](../../common-definitions/enums/document.md#scrollsource12) | Yes | Source of the current scrolling operation. |

**Return value**

| Type | Description |
| :-- | :-- |
| void | [ScrollResult](#scrollresult12) | 
Returns a **ScrollResult** object if the scrollable component scrolls by the developer-specified offset relative to the previous frame; returns no **ScrollResult** object if the component scrolls by the offset specified by **scrollOffset** in the callback.

Value range: (-∞, +∞)

 |

#### OnScrollCallback12+

type OnScrollCallback = (scrollOffset: number, scrollState: ScrollState) => void

Triggered when the scrollable component scrolls.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scrollOffset | number | Yes | 
Offset relative to the previous frame. The offset is positive when the scrollable component is scrolled up and negative when it is scrolled down.

Unit: vp

 |
| scrollState | [ScrollState](../list/document.md#scrollstate) | Yes | Current scroll state. |

#### ScrollResult12+

Implements a return value object of the [OnWillScrollCallback](#onwillscrollcallback12) callback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offsetRemain | number | No | No | Amount by which the component is about to be scrolled, in vp. |

#### ChildrenMainSize12+

Provides the size information of the child components of the **List** or **ListItemGroup** component along the main axis. This object only supports one-to-one binding to the **List** or **ListItemGroup** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ESZ1r7qcQKOxDsJo3DhJ0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6760EDB647CDCD5F85BDCBA463BC97DF859E712BE0810CFA07B095E049EDC8BA)

-   The main axis size information must match the actual main axis size of the child components. When child components' main axis sizes change or components are added or removed, the **ChildrenMainSize** object methods must be invoked to notify the **List** or **ListItemGroup** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor12+

constructor(childDefaultSize: number)

A constructor used to create a **ChildrenMainSize** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| childDefaultSize | number | Yes | 
Default size of the child component along the main axis.

Unit: vp

**NOTE**

The value must be a finite non-negative number; otherwise, an exception will be thrown.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

#### \[h2\]childDefaultSize12+

set childDefaultSize(value: number)

Sets the default size of the child component along the main axis.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Default size of the child component along the main axis.

Unit: vp

**NOTE**

The value must be a finite non-negative number; otherwise, an exception will be thrown.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

get childDefaultSize(): number

Obtains the default size of the child component along the main axis.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Default size of the child component along the main axis.

Unit: vp

Value range: \[0, +∞)

 |

#### \[h2\]splice12+

splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void

Performs batch operations to add, delete, or modify the size information of child components along the main axis.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| start | number | Yes | 
Index starting from 0, which indicates the position at which to begin modifying the size information of child components along the main axis.

**NOTE**

1\. The value must be a finite non-negative number; otherwise, an exception will be thrown.

2\. Non-integer values are truncated to the nearest integer.

3\. Values exceeding the maximum index do not take effect.

Value range: \[0, +∞)

 |
| deleteCount | number | No | 

Number of size information entries to be deleted starting from the **start** position.

**NOTE**

1\. The value must be a finite non-negative number; otherwise, it will be treated as **0**.

2\. Non-integer values are truncated to the nearest integer.

3\. The result of (start + deleteCount - 1) can exceed the maximum index, which will delete all size information of child components starting from the **start** position.

Default value: **+∞**

Value range: \[0, +∞)

 |
| childrenSize | Array<number > | No | 

Size information of all child components to be inserted, starting from the **start** position.

Unit for each value in the array: vp

**NOTE**

1\. If the values in the array are finite non-negative number, they are considered specified sizes and will not change with the default size.

2\. If the values in the array are not finite non-negative number, they will be treated as the default size and will change with the default size.

The default value is an empty array.

Value range: \[0, +∞)

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ESJnWXrGQL--pur9T--dIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D02CF011BCDB1C213D18C5E3CD17CE92E4163636E4585BBA97843D278846702)

-   If only the **start** parameter is used, it means to delete the size information of the child components starting from the **start** position and beyond.
-   If only the **start** and **deleteCount** parameters are used, it means to delete the **deleteCount**\-specified number of size information entries starting from the **start** position. This is generally used when you remove child components.
-   If all three parameters are used, it means to delete the **deleteCount**\-specified number of size information entries starting from the **start** position, and then insert all the size information from **childrenSize** at the **start** position. This is generally used when you add child components or batch update the main axis size of child components. If it's only about adding child components, **deleteCount** should be **0**, and the number of elements in **childrenSize** should be equal to the number of child components being added. If it's only about batch updating the main axis size of child components, the number of elements in **childrenSize** should be equal to **deleteCount**, which is the number of updates being made.
-   If you want to notify that the size of a child component should be the default size, the corresponding value in **childrenSize** should not be given as a finite non-negative value, but rather as **NaN**, any negative value, or any other value that can be processed as the default size.

#### \[h2\]update12+

update(index: number, childSize: number): void

Updates the main axis size information of the child component corresponding to the specified index.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index starting from 0, which indicates the position at which to begin modifying the size information of child components along the main axis.

**NOTE**

1\. The value must be a finite non-negative number; otherwise, an exception will be thrown.

2\. Non-integer values are truncated to the nearest integer.

3\. Values exceeding the maximum index do not take effect.

Value range: \[0, +∞)

 |
| childSize | number | Yes | 

Size to be updated to.

Unit: vp

**NOTE**

1\. If the value is a finite non-negative number, it is considered a specified size and will not change with the default size.

2\. If the value is not a finite non-negative number, it will be processed as the default size and will change with the default size.

Value range: \[0, +∞)

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

#### UIScrollableCommonEvent19+

Configures scroll event callbacks.

#### \[h2\]setOnReachStart19+

setOnReachStart(callback: Callback<void> | undefined): void

Sets the callback for the [onReachStart](#onreachstart11) event.

If the input parameter of an API is **undefined**, the corresponding event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../common-definitions/basic-types/document.md#callback12)<void> | undefined | Yes | Callback for the **onReachStart** event. |

#### \[h2\]setOnReachEnd19+

setOnReachEnd(callback: Callback<void> | undefined): void

Sets the callback for the [onReachEnd](#onreachend11) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../common-definitions/basic-types/document.md#callback12)<void> | undefined | Yes | Callback for the **onReachEnd** event. |

#### \[h2\]setOnScrollStart19+

setOnScrollStart(callback: Callback<void> | undefined): void

Sets the callback for the [onScrollStart](#onscrollstart11) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../common-definitions/basic-types/document.md#callback12)<void> | undefined | Yes | Callback for the **onScrollStart** event. |

#### \[h2\]setOnScrollStop19+

setOnScrollStop(callback: Callback<void> | undefined): void

Sets the callback for the [onScrollStop](#onscrollstop11) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../common-definitions/basic-types/document.md#callback12)<void> | undefined | Yes | Callback for the **onScrollStop** event. |

#### \[h2\]setOnScrollFrameBegin19+

setOnScrollFrameBegin(callback: OnScrollFrameBeginCallback | undefined): void

Sets the callback for the [onScrollFrameBegin](../scroll/document.md#onscrollframebegin9) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnScrollFrameBeginCallback](../scroll/document.md#onscrollframebegincallback18) | undefined | Yes | Callback for the **onScrollFrameBegin** event. |

#### OnWillStopDraggingCallback20+

type OnWillStopDraggingCallback = (velocity: number) => void

Defines the callback invoked when the scrollable component is released.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| velocity | number | Yes | 
Scroll velocity. Positive for scrolling upward, negative for scrolling downward.

Unit: vp/s.

 |

#### OnDidStopDraggingCallback21+

type OnDidStopDraggingCallback = (willFling: boolean) => void

Defines the callback invoked when the scrollable component stops being dragged.

**Widget capability**: This API can be used in ArkTS widgets since API version 21.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| willFling | boolean | Yes | Whether an inertial animation will follow. **true**: An inertial animation will follow. **false**: No inertial animation will follow. |

#### Example

## Example 1: Implementing Gesture-based Scrolling

This example configures the [enableScrollInteraction](#enablescrollinteraction11) attribute to enable gesture-based scrolling in a vertical list, with index callbacks triggered during page transitions.

For details about ListDataSource and the complete code, see [Example 1: Adding a Scroll Event](../list/document.md#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]);

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .enableScrollInteraction(true)
      .listDirection(Axis.Vertical) // Arrangement direction
      .scrollBar(BarState.Off)
      .friction(0.6)
      .divider({
        strokeWidth: 2,
        color: 0xFFFFFF,
        startMargin: 20,
        endMargin: 20
      }) // Divider between rows
      .edgeEffect(EdgeEffect.Spring) // Set the edge scrolling effect to Spring.
      .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
        console.info('first' + firstIndex);
        console.info('last' + lastIndex);
        console.info('center' + centerIndex);
      })
      .onScrollVisibleContentChange((start: VisibleListContentInfo, end: VisibleListContentInfo) => {
        console.info(' start index: ' + start.index +
          ' start item group area: ' + start.itemGroupArea +
          ' start index in group: ' + start.itemIndexInGroup);
        console.info(' end index: ' + end.index +
          ' end item group area: ' + end.itemGroupArea +
          ' end index in group: ' + end.itemIndexInGroup);
      })
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(\`onScroll scrollState = ScrollState\` + scrollState + \`, scrollOffset = \` + scrollOffset);
      })
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/yz2Qj_E3TSGKhDmRSnvZfw/en-us_image_0000002568765237.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E06A428244E0CF4D05124E348FC9DC7109A618E8F70CE591192DFDA5CC31DEB)

## Example 2: Setting Edge Fading

This example demonstrates how to use [fadingEdge](#fadingedge14) to implement a [List](../list/document.md) component with an edge fading effect and set the length of the fading edge.

For details about ListDataSource and the complete code, see [Example 1: Adding a Scroll Event](../list/document.md#example-1-adding-a-scroll-event).

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\]);
  scrollerForList: Scroller = new Scroller();

  build() {
    Column() {

      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/LFk3XFCqTuu8ftnBKQoq-Q/en-us_image_0000002537925454.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41FED594CBA09049C9F45FAEEE6E5D9FC9C0E2259FEEB99ACEAE2D214DE4A755)

## Example 3: Setting the Clipping Region

This example demonstrates how to use the [clipContent](#clipcontent14) attribute to modify the clipping region of the component's content layer.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\];
  @State clipContent: ContentClipMode | RectShape | undefined = undefined;

  build() {
    Column() {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width(300)
              .height(80)
              .fontSize(20)
              .textAlign(TextAlign.Center)
              .backgroundColor(Color.Grey)
          }, (item: string) => item)
        }
      }
      .backgroundColor(Color.Blue)
      .clipContent(this.clipContent)
      .scrollBar(BarState.Off)
      .friction(0.6)
      .width(300)
      .height('50%')
      .padding(10)
      .safeAreaPadding(LengthMetrics.vp(10))
      .initialOffset({ yOffset: 80 })
      .margin({ top: 20 })

      Button('clipContent SAFE\_AREA')
        .onClick(() => {
          this.clipContent = ContentClipMode.SAFE\_AREA;
        }).margin({ top: 30 })

      Button('clipContent BOUNDARY')
        .onClick(() => {
          this.clipContent = ContentClipMode.BOUNDARY;
        }).margin({ top: 35 })

      Button('clipContent CONTENT\_ONLY')
        .onClick(() => {
          this.clipContent = ContentClipMode.CONTENT\_ONLY;
        }).margin({ top: 40 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/QMkoIHBzQLeTqM7vggaKAg/en-us_image_0000002568765289.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=862E64FFB5C1EE92CAF13190D7DD03D39CE7C8D03677DDAE134923397DF5D0ED)

## Example 4: Setting the Scrollbar Margin

This example demonstrates how to use the [scrollBarMargin](#scrollbarmargin20) attribute to adjust the scrollbar margins of a scrollable component, available since API version 20.

For details about ListDataSource and the complete code, see [Example 1: Adding a Scroll Event](../list/document.md#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ListExample {
  arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]);
  @State scrollBarMargin: ScrollBarMargin = { start: LengthMetrics.vp(0), end: LengthMetrics.vp(0) };

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          LazyForEach(this.arr, (item: number, index?: number) => {
            ListItem() {
              Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
                Text('' + item)
                  .width('100%')
                  .height(80)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(Color.White)
                  .flexShrink(1)
              }
            }
          }, (item: number) => item.toString())
        }.width('90%')
        .friction(0.6)
        .scrollBar(BarState.On)
        .scrollBarMargin(this.scrollBarMargin)
      }.width('100%')

      Button('scrollBarMargin')
        .onClick(() => {
          this.scrollBarMargin = { start: LengthMetrics.vp(45), end: LengthMetrics.vp(70) };
        }).margin({ top: 5, left: 20 })

      Button('scrollBarMargin2')
        .onClick(() => {
          this.scrollBarMargin = { start: LengthMetrics.vp(15), end: LengthMetrics.vp(100) };
        }).margin({ top: 200, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/l69O-TfKRceTflQeQfvqGw/en-us_image_0000002537765564.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C5C9F3DA9DDF679D19DD1ADEBC269034CA8EEB4FCFF5BEF6B1C81F5C5E0B82D)
