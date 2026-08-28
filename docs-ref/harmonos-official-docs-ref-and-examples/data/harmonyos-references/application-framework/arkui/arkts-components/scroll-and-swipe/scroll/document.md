# Scroll

The **Scroll** component scrolls the content when the layout size of a component exceeds the size of its parent component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/yf4e799eQH69YaXHNAUmPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6079E793FF52AE084F6C97E9844E70F290EB1550C0A218CA99FA572D78965764)

-   This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
-   When nesting a **List** within this component, specify the width and height for the **List** under scenarios where consistently high performance is required. If the width and height are not specified, this component will load all content of the **List**. For details, see [On-Demand Loading Failure Due to the Scroll-Nested List](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-lazyforeach-optimization#section6296154115367).
-   This component can scroll only when the size on the main axis is less than the content size.
-   The default value of the universal attribute [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) is **true** for the **Scroll** component.
-   If the **Scroll** component's height exceeds the screen height, use the [layoutWeight](../../universal-attributes/layout-and-borders/sizing/document.md#layoutweight) attribute to make it fill the remaining main-axis space.
-   A touch on the screen stops all ongoing scroll animations within the touch area (except those triggered by [scrollTo](#scrollto) or [scrollToIndex](#scrolltoindex)), including edge bounce effects.
-   The component includes built-in gesture recognition for finger‑following and other interactive features. For details about how to add custom gestures, see [Gesture Blocking Enhancement](../../gesture-handling/gesture-control/gesture-blocking-enhancement/document.md).

#### Child Components

This component supports only one child component.

Starting from API version 21, the maximum width or height for a single child component inside a **Scroll** container is 16,777,216 px. In API version 20 and earlier versions, the limit was 1,000,000 px. If a child component exceeds the applicable size limit, scrolling or display behavior may become abnormal.

#### APIs

Scroll(scroller?: Scroller)

Creates a **Scroll** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scroller | [Scroller](#scroller) | No | 
Scroller, which can be bound to scrollable components.

**NOTE**

The scroller cannot be bound to other scrollable components, such as [ArcList](../arclist/document.md), [List](../list/document.md), [Grid](../grid/document.md), [Scroll](#), or [WaterFlow](../waterflow/document.md).

 |

#### Attributes

In addition to [universal attributes](../../universal-attributes/document.md) and [scrollable component common attributes](../scrollable-component-common-apis/document.md#attributes), the following attributes are also supported.

#### \[h2\]scrollable

scrollable(value: ScrollDirection)

Sets the scrolling direction. The scroll offset is reset when this value is changed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScrollDirection](#scrolldirection) | Yes | 
Scrolling direction.

Default value: **ScrollDirection.Vertical**

 |

When the scrolling direction is set to [ScrollDirection.FREE](#scrolldirection), the **Scroll** component supports only a subset of its capabilities. For details, see [Capabilities Supported in Free Scrolling Mode](#scrolldirection).

#### \[h2\]scrollBar

scrollBar(barState: BarState)

Sets the scrollbar state. If the container component cannot be scrolled, the scrollbar is not displayed. If the size of a child component of a container component is infinite, the scrollbar cannot be dragged or scrolled with the child component.

Since API version 10, when the scrollable component has rounded corners, to prevent the scrollbar from being cut off by the corners, the scrollbar will automatically calculate the clearance distance from the top and bottom.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| barState | [BarState](../../common-definitions/enums/document.md#barstate) | Yes | 
Scrollbar state.

Default value: **BarState.Auto**

 |

#### \[h2\]scrollBarColor

scrollBarColor(color: Color | number | string)

Sets the scrollbar color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Color](../../common-definitions/enums/document.md#color) | number | string | Yes | 
Scrollbar color.

Default value: **'#66182431'**.

A number value indicates a HEX color in RGB or ARGB format, for example, **0xffffff**.

A string value indicates a color in RGB or ARGB format, for example, **'#ffffff'**.

 |

#### \[h2\]scrollBarColor22+

scrollBarColor(color: Color | number | string | Resource)

Sets the scrollbar color. Compared with [scrollBarColor](#scrollbarcolor), this API supports the Resource type for the **color** parameter.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Color](../../common-definitions/enums/document.md#color) | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Scrollbar color.

Default value: **'#66182431'**.

A number value indicates a HEX color in RGB or ARGB format, for example, **0xffffff**. A string value indicates a color in RGB or ARGB format, for example, **'#ffffff'**.

 |

#### \[h2\]scrollBarWidth

scrollBarWidth(value: number | string)

Sets the scrollbar width. This attribute cannot be set in percentage. After the width is set, the scrollbar is displayed with the set width in normal state and pressed state. If the set width exceeds the height of the **Scroll** component on the main axis, the scrollbar reverts to the default width.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Scrollbar width.

Default value: **4**

Unit: vp

Values less than 0 are treated as the default value. The value **0** means not to show the scrollbar.

 |

#### \[h2\]scrollSnap10+

scrollSnap(value: ScrollSnapOptions)

Sets the scroll snapping mode.

During the snap animation, the scroll operation source type reported by the [onWillScroll](#onwillscroll12) event is **ScrollSource.FLING**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScrollSnapOptions](#scrollsnapoptions10) | Yes | Scroll snapping mode. |

#### \[h2\]edgeEffect

edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions)

Sets the effect used when the scroll boundary is reached.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| edgeEffect | [EdgeEffect](../../common-definitions/enums/document.md#edgeeffect) | Yes | 
Effect used when the scroll boundary is reached. The spring and shadow effects are supported.

Default value: **EdgeEffect.None**

 |
| options11+ | [EdgeEffectOptions](../scrollable-component-common-apis/document.md#edgeeffectoptions11) | No | 

Whether to enable the scroll effect when the component content is smaller than the component itself. The value **{ alwaysEnabled: true }** means to enable the scroll effect, and **{ alwaysEnabled: false }** means the opposite.

Default value: **{ alwaysEnabled: true }**

 |

#### \[h2\]enableScrollInteraction10+

enableScrollInteraction(value: boolean)

Sets whether to enable scroll gestures.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable scroll gestures. With the value **true**, scrolling via finger or mouse is enabled. With the value **false**, scrolling via finger or mouse is disabled, but this does not affect the scrolling APIs of the [Scroller](#scroller).

Default value: **true**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/gq-oHMQpQFe7CP7n6jZAdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DDCEC88860B884B6FCE5E7212482BCE41D49EF5263C924BEE0293FA4DADFD60)

The component cannot be scrolled by dragging the mouse.

#### \[h2\]nestedScroll10+

nestedScroll(value: NestedScrollOptions)

Sets the nested scrolling mode in the forward and backward directions to implement scrolling linkage with the parent component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NestedScrollOptions](../scrollable-component-common-apis/document.md#nestedscrolloptions10) | Yes | 
Nested scrolling options.

Default value: **{ scrollForward: NestedScrollMode.SELF\_ONLY, scrollBackward: NestedScrollMode.SELF\_ONLY }**

Nested scrolling will not take effect when both of the following conditions are met: (1) The child **Scroll** component has [enablePaging](#enablepaging11) or [scrollSnap](#scrollsnap10) enabled. (2) The parent component is configured to have scrolling priority.

 |

#### \[h2\]friction10+

friction(value: number | Resource)

Sets the friction coefficient. It applies only to gestures in the scrolling area, and it affects only indirectly the scroll chaining during the inertial scrolling process.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Friction coefficient.

Default value: **0.9** for wearable devices and **0.6** for non-wearable devices

Since API version 11, the default value for non-wearable devices is **0.7**.

Since API version 12, the default value for non-wearable devices is **0.75**.

Value range: (0, +∞). If the value is less than or equal to 0, the default value is used.

 |

#### \[h2\]enablePaging11+

enablePaging(value: boolean)

Sets whether to enable the swipe-to-turn-pages feature. If both **enablePaging** and **scrollSnap** are set, **scrollSnap** takes effect, but **enablePaging** does not.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable the swipe-to-turn-pages feature. The value **true** means to enable the swipe-to-turn-pages feature, and **false** means the opposite.

Default value: **false**

 |

#### \[h2\]initialOffset12+

initialOffset(value: OffsetOptions)

Sets the initial scrolling offset. This attribute takes effect only during the initial layout of the component. After the initial layout, dynamically changing the value of this attribute does not have any effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [OffsetOptions](#offsetoptions12) | Yes | Initial scrolling offset. When the value specified is a percentage, the initial scrolling offset is calculated as the product of the **Scroll** component's size in the main axis direction and the percentage value. |

#### \[h2\]maxZoomScale20+

maxZoomScale(scale: number)

Sets the maximum gesture‑based zoom scale for the **Scroll** component's content.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | Yes | 
Maximum gesture‑based zoom scale for the **Scroll** component's content.

Default value: **1**.

Value range: (0, +∞). If the value is less than or equal to 0, the default value 1 is used.

 |

#### \[h2\]minZoomScale20+

minZoomScale(scale: number)

Sets the minimum gesture-based zoom scale for the **Scroll** component's content.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | Yes | 
Minimum gesture-based zoom scale for the **Scroll** component's content.

Default value: **1**.

Value range: (0, maxZoomScale\]. If the value is less than or equal to 0, the default value **1** is used. If the value is greater than **maxZoomScale**, **maxZoomScale** is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ypl2eA6cRQ2yjDOe5N9wAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A21E1F43056A316F30C91CFF8D3897E191570E06481F5E926EEFE08D8B4AAB5B)

Setting either **maxZoomScale** and **minZoomScale** to a value other than 1 automatically enables the zoom gesture.

#### \[h2\]zoomScale20+

zoomScale(scale: number)

Sets the zoom scale of the **Scroll** component's content.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | Yes | 
Zoom scale of the **Scroll** component's content. This parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding).

Default value: **1**.

Value range: (0, +∞). If the value is less than or equal to 0, the default value 1 is used.

 |

#### \[h2\]enableBouncesZoom20+

enableBouncesZoom(enable: boolean)

Sets whether to enable the zoom bounce effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable the zoom bounce effect. **true** to enable, **false** otherwise.

Default value: **true**

 |

#### ScrollDirection

Enumerates the scrolling directions.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Vertical | 0 | 
Vertical scrolling only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Horizontal | 1 | 

Horizontal scrolling only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Free(deprecated) | 2 | 

Both vertical and horizontal scrolling.

Note: This API is supported since API version 7 and deprecated since API version 9. You are advised to use **FREE** instead. The enum value **FREE** is supported since API version 20.

 |
| None | 3 | 

Scrolling disabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FREE20+ | 4 | 

Free scrolling in both directions.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

**Capabilities Supported in Free Scrolling Mode**

| Supported Attribute | Supported Event | Supported [Scroller](#scroller) API |
| :-- | :-- | :-- |
| [scrollBar](#scrollbar) | [onWillScroll](#onwillscroll12) | [scrollTo](#scrollto) |
| [scrollBarColor](#scrollbarcolor) | [onDidScroll](#ondidscroll12) | [scrollEdge](#scrolledge) |
| [scrollBarWidth](#scrollbarwidth) | [onScrollEdge](#onscrolledge) | [scrollPage](#scrollpage9) |
| [scrollBarMargin](../scrollable-component-common-apis/document.md#scrollbarmargin20) | [onScrollStart](#onscrollstart9) | [currentOffset](#currentoffset) |
| [edgeEffect](#edgeeffect) | [onScrollStop](#onscrollstop9) | [scrollBy](#scrollby9) |
| [enableScrollInteraction](#enablescrollinteraction10) | \- | [getItemRect](#getitemrect11) |
| [friction](#friction10) | \- | \- |
| [clipContent](../scrollable-component-common-apis/document.md#clipcontent14) | \- | \- |
| [initialOffset](#initialoffset12) | \- | \- |
| [scrollable](#scrollable) | \- | \- |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/QZkeKS18SzevUjT6o-mOXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D39D665E166EF3FF86F9FAEAFC9D3684033063B6336EB3EC3A53DE327B88A61E)

-   The **edgeEffect** attribute supports only **Spring** and **None**. Other edge effects are not available.
-   The **onWillScroll** callback can only modify the offset during the follow‑up (inertial) scrolling phase, not during direct dragging.
-   The **onScrollEdge** callback is triggered once when the content reaches the edge, but not again during the subsequent bounce animation.
-   Changing the edge effect mode during a flick animation does not interrupt that animation.

#### ScrollSnapOptions10+

Defines a scroll snapping mode object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| snapAlign | [ScrollSnapAlign](../list/document.md#scrollsnapalign10) | No | No | 
Alignment mode for the scroll snap position.

**NOTE**

1\. Default value: **ScrollSnapAlign.NONE**

 |
| snapPagination | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | Array<Dimension> | No | Yes | 

Pagination points for scroll snapping.

**NOTE**

1\. If the value is of the Dimension type, it indicates the size of each page, and the system will paginate based on this size.

2\. If the value is of the Array<Dimension> type, each **Dimension** represents a pagination point, and the system will paginate accordingly. Each **Dimension** value must be within the \[0, scrollable distance\] range.

3\. If this parameter is not set or **Dimension** is set to a value less than or equal to 0, the value is regarded as an invalid value. In this case, there is no scroll snapping. When the value is of the Array<Dimension> type, the items in the array must be monotonically increasing.

4\. When the value is a percentage, the actual size is the product of the viewport of the **Scroll** component and the percentage value.

 |
| enableSnapToStart | boolean | No | Yes | 

Whether to enable free scrolling between the start position and the first snap point. **true**: Free scrolling between the start position and the first snap point is disabled. **false**: Free scrolling between the start position and the first snap point is allowed.

**NOTE**

1\. Default value: **true**

2\. This attribute takes effect only when **snapPagination** is set to a value of the **Array<Dimension>** type; it does not work with values of the **Dimension** type.

 |
| enableSnapToEnd | boolean | No | Yes | 

Whether to enable free scrolling between the end position and the last snap point. **true**: Free scrolling between the end position and the last snap point is disabled. **false**: Free scrolling between the end position and the last snap point is allowed.

**NOTE**

1\. Default value: **true**

2\. This attribute takes effect only when **snapPagination** is set to a value of the **Array<Dimension>** type; it does not work with values of the **Dimension** type.

 |

#### Events

In addition to [universal events](../../universal-events/document.md) and [scrollable component common events](../scrollable-component-common-apis/document.md#events), the following events are also supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/zzAdhcbIQNeQOUulmP9aIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A76B510F42D60BDE239C7F4FEFC4D74EB81E55683DA34611117A56831A68B006)

The [onWillScroll](../scrollable-component-common-apis/document.md#onwillscroll12) and [onDidScroll](../scrollable-component-common-apis/document.md#ondidscroll12) events are not supported.

#### \[h2\]onScrollFrameBegin9+

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

Triggered at the beginning of each scroll frame. The event parameter provides the pending scroll offset. The event handler can calculate the actual scroll amount based on the use case and return this value as its result. The **Scroll** component then scrolls according to the returned actual scroll amount.

The value of [offsetRemain](#onscrollframebeginhandlerresult18) can be negative.

If the **onScrollFrameBegin** event and [scrollBy](#scrollby9) method are used to implement nested scrolling, set the [EdgeEffect](#edgeeffect) attribute of the scrollable child component to **None**. For example, if a **List** component is nested in the **Scroll** container, [edgeEffect](../list/document.md#edgeeffect) of the **List** component must be set to **EdgeEffect.None**. Otherwise, swiping the **List** triggers its edge bounce animation, which results in failed nested scrolling.

This event is triggered when any of the following conditions is met:

1.  Scrolling is initiated by user interaction (for example, finger swipe, keyboard, or mouse operation).
2.  The **Scroll** component scrolls by inertia.
3.  Scrolling is triggered by calling the [fling](#fling12) API.

This event is not triggered when any of the following conditions is met:

1.  A scroll control API other than [fling](#fling12) is called.
2.  The out-of-bounds bounce effect is active.
3.  The scrollbar is dragged.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [OnScrollFrameBeginCallback](#onscrollframebegincallback18) | Yes | Callback triggered when each frame scrolling starts. |

#### \[h2\]onScroll(deprecated)

onScroll(event: (xOffset: number, yOffset: number) => void)

Triggered to return the horizontal and vertical offsets, in vp, during scrolling when the specified scroll event occurs.

Trigger conditions:

1.  Scrolling is started by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).
    
2.  The scroll controller API is called.
    
3.  The out-of-bounds bounce effect is active.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/jlBcAvsJR4OtTTGAo94Ffw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E50B15D7D19B4CBD1877E3ABCBC8A46798FFE7DAE7C833DDEA5DDC12ABAC994E)

This API is supported since API version 7 and deprecated since API version 12. You are advised to use [onWillScroll](#onwillscroll12) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| xOffset | number | Yes | 
Horizontal offset relative to the previous frame. A positive offset indicates scrolling to the left, and a negative offset indicates scrolling to the right.

Unit: vp

 |
| yOffset | number | Yes | 

Vertical offset relative to the previous frame. A positive offset indicates scrolling upward, and a negative offset indicates scrolling downward.

Unit: vp

 |

#### \[h2\]onWillScroll12+

onWillScroll(handler: ScrollOnWillScrollCallback)

Triggered before scrolling.

The callback provides the amount of offset that is about to be scrolled in the current frame, along with the current scroll status and the source of the scrolling operation. The offset provided in the callback is the calculated intended scrolling offset, not the final actual scrolling offset. You can specify the intended scrolling offset for the **Scroll** through the return value of this callback.

Trigger conditions:

1.  Scrolling is started by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).
    
2.  The scroll controller API is called.
    
3.  The out-of-bounds bounce effect is active.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/hRzLqEi9T_umoQ-8ZE-xIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2B47CC81EC5B8DE6EDCC3EA22A8AF3AAFD337CC90A11EC652D43D95300E543B)

The scrolling event callback is triggered frequently during scrolling. To avoid frame freezing or dropped frames, do not perform time-consuming operations in this callback. For best practices, see [High-Frequency Callback Scenarios](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-time-optimization-of-the-main-thread#section10112623611).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [ScrollOnWillScrollCallback](#scrollonwillscrollcallback12) | Yes | Callback triggered before scrolling. |

#### \[h2\]onDidScroll12+

onDidScroll(handler: ScrollOnScrollCallback)

Triggered when the **Scroll** component scrolls.

The return value is the scrolling offset amount in the current frame, along with the current scroll state.

Trigger conditions:

1.  Scrolling is started by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).
    
2.  The scroll controller API is called.
    
3.  This event supports the out-of-bounds bounce effect.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [ScrollOnScrollCallback](#scrollonscrollcallback12) | Yes | Represents the callback triggered when the **Scroll** component scrolls. |

#### \[h2\]onScrollEdge

onScrollEdge(event: OnScrollEdgeCallback)

Triggered when scrolling reaches the edge.

Trigger conditions:

1.  Scrolling reaches the edge after being started by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).
    
    2\. The scroll controller API is called.
    
    3\. The out-of-bounds bounce effect is active.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [OnScrollEdgeCallback](#onscrolledgecallback18) | Yes | 
Edge position to scroll to.

For horizontal scrolling, [Edge.Center](../../common-definitions/enums/document.md#edge) represents the start position, and [Edge.Baseline](../../common-definitions/enums/document.md#edge) represents the end position. Note: The enum values [Edge.Center](../../common-definitions/enums/document.md#edge) and [Edge.Baseline](../../common-definitions/enums/document.md#edge) are deprecated. You are advised to use the [onReachStart](../scrollable-component-common-apis/document.md#onreachstart11) and [onReachEnd](../scrollable-component-common-apis/document.md#onreachend11) to detect when the component reaches its boundary.

 |

#### \[h2\]onScrollEnd(deprecated)

onScrollEnd(event: () => void)

Triggered when scrolling stops.

Trigger conditions:

1.  Scrolling is stopped by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).
    
    2\. The controller API is called to stop the scrolling, accompanied by a transition animation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/wtMP6xGaTEWEOyD1Ihir1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=773CF51E649343CCC08F8DA7DC7235323FFAC4999373AE5C0C636017DD46A898)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [onScrollStop](#onscrollstop9) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when scrolling stops. |

#### \[h2\]onScrollStart9+

onScrollStart(event: VoidCallback)

Triggered when scrolling starts and is initiated by the user's finger dragging the **Scroll** component or its scrollbar. This event is also triggered when the animation contained in the scrolling triggered by [Scroller](#scroller) starts.

Trigger conditions:

1.  Scrolling is started by the **Scroll** component (supports keyboard, mouse, and other input methods that trigger scrolling).
    
    2\. The controller API is called to start the scrolling, accompanied by a transition animation.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback triggered when scrolling starts. |

#### \[h2\]onScrollStop9+

onScrollStop(event: VoidCallback)

Triggered when scrolling stops after the user's finger leaves the screen. This event is also triggered when the animation contained in the scrolling triggered by [Scroller](#scroller) stops.

Trigger conditions:

1.  Scrolling is stopped by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).
    
    2\. The controller API is called to start the scrolling, accompanied by a transition animation.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback triggered when scrolling stops. |

#### \[h2\]onDidZoom20+

onDidZoom(event: ScrollOnDidZoomCallback)

Triggered when the zoom operation of each frame is completed.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ScrollOnDidZoomCallback](#scrollondidzoomcallback20) | Yes | Callback triggered when the zoom operation of each frame is completed. |

#### \[h2\]onZoomStart20+

onZoomStart(event: VoidCallback)

Triggered when a zoom gesture starts.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback triggered when the zoom gesture starts. |

#### \[h2\]onZoomStop20+

onZoomStop(event: VoidCallback)

Triggered when a zoom gesture stops.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback triggered when the zoom gesture stops. |

#### ScrollOnScrollCallback12+

type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void

Represents the callback triggered when the **Scroll** component scrolls.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| xOffset | number | Yes | 
Horizontal offset relative to the previous frame. A positive offset indicates scrolling to the left, and a negative offset indicates scrolling to the right.

Unit: vp

 |
| yOffset | number | Yes | 

Vertical offset relative to the previous frame. A positive offset indicates scrolling upward, and a negative offset indicates scrolling downward.

Unit: vp

 |
| scrollState | [ScrollState](../list/document.md#scrollstate) | Yes | Current scrolling state. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/aKhYGjzySz6FtwO0fNcuaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=592C578F7DA787A0C0C6E02F27E9547943DB3B32164728D06325E0C4371EFE03)

If the [onScrollFrameBegin](#onscrollframebegin9) event and [scrollBy](#scrollby9) method are used to implement nested scrolling, set the **EdgeEffect** attribute of the scrollable child component to **None**. For example, if a **List** component is nested in the **Scroll** container, [edgeEffect](../list/document.md#edgeeffect) of the **List** component must be set to **EdgeEffect.None**.

#### ScrollOnWillScrollCallback12+

type ScrollOnWillScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | OffsetResult

Callback triggered before scrolling.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| xOffset | number | Yes | 
Horizontal offset relative to the previous frame. A positive offset indicates scrolling to the left, and a negative offset indicates scrolling to the right.

Unit: vp

 |
| yOffset | number | Yes | 

Vertical offset relative to the previous frame. A positive offset indicates scrolling upward, and a negative offset indicates scrolling downward.

Unit: vp

 |
| scrollState | [ScrollState](../list/document.md#scrollstate) | Yes | Current scrolling state. |
| scrollSource | [ScrollSource](../../common-definitions/enums/document.md#scrollsource12) | Yes | Source of the current scrolling operation. |

**Return value**

| Type | Description |
| :-- | :-- |
| void | [OffsetResult](#offsetresult11) | If **OffsetResult** is returned, the scrolling will be performed with the offsets specified. Otherwise, the scrolling will be performed with the offsets determined by **(xOffset, yOffset)**. |

#### OnScrollEdgeCallback18+

type OnScrollEdgeCallback = (side: Edge) => void

Represents the callback triggered when scrolling reaches an edge.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| side | [Edge](../../common-definitions/enums/document.md#edge) | Yes | Edge position to scroll to. |

#### OnScrollFrameBeginCallback18+

type OnScrollFrameBeginCallback = (offset: number, state: ScrollState) => OnScrollFrameBeginHandlerResult;

Represents the callback triggered before each frame scrolling starts.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Amount to scroll by, in vp. |
| state | [ScrollState](../list/document.md#scrollstate) | Yes | Current scroll state. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OnScrollFrameBeginHandlerResult](#onscrollframebeginhandlerresult18) | Actual scroll offset. |

#### OnScrollFrameBeginHandlerResult18+

Represents the actual scroll offset relative to the previous frame returned by [OnScrollFrameBeginCallback](#onscrollframebegincallback18).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/OBdgvbfASBCjZgLtRtsM2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FB52BF505E46A46B5AD6E8C8FD316A94A6F970B20555AC94C1A6AC676AD00A9)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offsetRemain9+ | number | No | No | 
Actual scroll offset relative to the previous frame.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ScrollOnDidZoomCallback20+

type ScrollOnDidZoomCallback = (scale: number) => void

Defines the callback triggered when the scroll scaling of each frame is complete.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | Yes | Current scale factor. |

#### Scroller

Defines a controller for scrollable container components. It can be bound to a container component to control its scrolling behavior. A single **Scroller** instance cannot control multiple container components simultaneously. Currently, it can be bound to the following components: **ArcList**, **ArcScrollBar**, **List**, **Scroll**, **ScrollBar**, **Grid**, and **WaterFlow**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/oSJ_jJBRQkCd2l-GA6MKLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFE394963AE6A2F3DAC6296B2C9D78FCD9C1A1CD841091F5400BE5AAB5FEA1D6)

1.  The binding of a **Scroller** instance to a scrollable container component occurs during the component creation phase.
    
2.  **Scroller** APIs can only be effectively called after the **Scroller** instance is bound to a scrollable container component. Otherwise, depending on the API called, it may have no effect or throw an exception.
    
3.  For example, with [aboutToAppear](../../custom-components/custom-component-lifecycle/document.md#abouttoappear), this callback is executed after a new instance of a custom component is created and before its **build()** method is called. Therefore, if a scrollable component is defined within the **build** method of a custom component, the internal scrollable component has not yet been created during the **aboutToAppear** callback of that custom component, and therefore the **Scroller** APIs cannot be called effectively.
    
4.  For example, with [onAppear](../../universal-events/component-change-events/show-hide-event/document.md#onappear), this callback is triggered after the component is mounted and displayed. Therefore, when the **onAppear** callback of a scrollable component is executed, the scrollable component has already been created and successfully bound to the **Scroller** instance, allowing the **Scroller** APIs to be called effectively.

## Objects to Import

scroller: Scroller = new Scroller();

#### \[h2\]constructor

constructor()

A constructor used to create a **Scroller** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]scrollTo

scrollTo(options: ScrollOptions)

Scrolls to the specified position.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ScrollOptions](#scrolloptions18) | Yes | Parameters for scrolling to the specified position. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/CKnJ_BanROqq8biNLRnPeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00C13E8D95FC2A3994E4B066AD2B1E9212E82328A3027A87E1F8A6A816959CDA)

If the scrolling speed of the **scrollTo** animation exceeds 200 vp/s, the components within the scrollable area will not respond to click events.

#### \[h2\]scrollEdge

scrollEdge(value: Edge, options?: ScrollEdgeOptions)

Scrolls to the edge of the container, regardless of the scroll axis direction. **Edge.Top** and **Edge.Start** produce the same effect, and **Edge.Bottom** and **Edge.End** produce the same effect.

By default, the **Scroll** component comes with an animation, while the **Grid**, **List**, and **WaterFlow** components do not.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Edge](../../common-definitions/enums/document.md#edge) | Yes | Edge position to scroll to. |
| options12+ | [ScrollEdgeOptions](#scrolledgeoptions12) | No | Mode of scrolling to the edge position. |

#### \[h2\]fling12+

fling(velocity: number): void

Performs inertial scrolling based on the initial velocity passed in.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| velocity | number | Yes | 
Initial velocity of inertial scrolling. Unit: vp/s

**NOTE**

If the value specified is 0, it is considered as invalid, and the scrolling for this instance will not take effect. A positive value indicates scrolling towards the top, while a negative value indicates scrolling towards the bottom.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to component. |

#### \[h2\]scrollPage9+

scrollPage(value: ScrollPageOptions)

Scrolls to the next or previous page.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScrollPageOptions](#scrollpageoptions14) | Yes | Page turning mode. |

#### \[h2\]scrollPage(deprecated)

scrollPage(value: { next: boolean, direction?: Axis })

Scrolls to the next or previous page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/nWbXQvkrQ4CZqe7BntX0mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96B5EEBFFD200ECEADCA4371615E6739B41EF3B202EEB78EEDCD1CD5A7DC1257)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [scrollPage9+](#scrollpage9) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| next | boolean | Yes | Whether to turn to the next page. The value **true** means to scroll to the next page, and **false** means to scroll to the previous page. |
| direction | [Axis](../../common-definitions/enums/document.md#axis) | No | Scrolling direction: horizontal or vertical. |

#### \[h2\]currentOffset

currentOffset(): OffsetResult

Obtains the current scroll offset.

The **Grid**, **List**, and **WaterFlow** components use a lazy loading mechanism. Before all content is fully loaded and laid out, the total content offset is estimated, and this estimation may be inaccurate. For the **List** component, the [childrenMainSize](../list/document.md#childrenmainsize12) attribute can be used to mitigate such inaccuracies.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [OffsetResult11+](#offsetresult11) | 
Current scroll offset.

**NOTE**

If **Scroller** is not bound to a container or the container is released abnormally, the return value for **currentOffset** is **undefined**.

 |

#### \[h2\]scrollToIndex

scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)

Scrolls to a specified index, with support for setting an extra offset for the scroll.

When smooth scrolling is enabled, all items encountered during the scroll are loaded and their layout is calculated. Loading a large number of items may cause performance issues. It is recommended that you first call **scrollToIndex** without animation to jump to a position near the target, then call it again with animation to smoothly scroll to the final target position.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/V3VjgoLMTwy01vy0d8K8Pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16FD15ECF6D52D85DBBC236762BC2FA330B301C24A121E638DCC2AA04993BCFD)

1.  This API applies only to the **ArcList**, **Grid**, **List**, and **WaterFlow** components.
    
2.  When refreshing the data source using [LazyForEach](../../state-management-and-rendering-control/lazyforeach/document.md), [ForEach](../../state-management-and-rendering-control/foreach/document.md), or [Repeat](../../state-management-and-rendering-control/repeat/document.md), ensure this API is called after the data refresh is complete.
    
3.  Starting from API version 11, the **List** component supports [contentStartOffset](../list/document.md#contentstartoffset11) and [contentEndOffset](../list/document.md#contentendoffset11). Starting from API version 22, the **Grid** and **WaterFlow** components also support setting [contentStartOffset](../scrollable-component-common-apis/document.md#contentstartoffset22) and [contentEndOffset](../scrollable-component-common-apis/document.md#contentendoffset22).
    

-   If the scrollable container has **contentStartOffset** set and **ScrollAlign** is **START**, after scrolling, the start of the specified item will align with the **contentStartOffset** of the container.
    
-   If the scrollable container has **contentEndOffset** set and **ScrollAlign** is **END**, after scrolling, the end of the specified item will align with the **contentEndOffset** of the container.
    
-   If the scrollable container has **contentStartOffset** or **contentEndOffset** set and **ScrollAlign** is **AUTO**: When the specified item is completely within the visible area, no adjustment is made. Otherwise, following the shortest-scroll-distance principle, the start of the item will align with the container's **contentStartOffset**, or the end will align with the container's **contentEndOffset**, ensuring the item is fully displayed.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Index of the item to be scrolled to in the container.

**NOTE**

If the value set is a negative value or greater than the maximum index of the items in the container, the value is deemed abnormal, and no scrolling will be performed.

 |
| smooth | boolean | No | 

Whether to enable the smooth animation for scrolling to the item with the specified index. The value **true** means to enable that the smooth animation, and **false** means the opposite.

Default value: **false**

 |
| align | [ScrollAlign](#scrollalign10) | No | 

How the list item to scroll to is aligned with the container.

Default value when the container is **List**: **ScrollAlign.START**

Default value when the container is **Grid**: **ScrollAlign.AUTO**

Default value when the container is **WaterFlow**: **ScrollAlign.START**

**NOTE**

This parameter is only available for the **List**, **Grid**, and **WaterFlow** components.

 |
| options12+ | [ScrollToIndexOptions](#scrolltoindexoptions12) | No | 

Options for scrolling to a specified index, for example, an extra offset for the scroll.

Default value: **0**, in vp

 |

#### \[h2\]scrollBy9+

scrollBy(dx: Length, dy: Length)

Scrolls by the specified amount.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/v1w4bRNaRX2k62i8ZECuMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A726B624D4CEF2B8FEFEF21402F13ACAB551D53C9253E9324561F183149A9EFB)

This API is available for the **ArcList**, **Scroll**, **List**, **Grid**, and **WaterFlow** components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dx | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Amount to scroll by in the horizontal direction. The percentage format is not supported.

Value range: (-∞, +∞).

 |
| dy | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 

Amount to scroll by in the vertical direction. The percentage format is not supported.

Value range: (-∞, +∞).

 |

#### \[h2\]isAtEnd10+

isAtEnd(): boolean

Checks whether the component has scrolled to the bottom.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/5MXX2eIOTaeuaK87wzpEww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F5E503E13C95491AEDB44CD7747DE974AA46C5DED774C7465A4CBE9FF49E8B7)

This API is available for the **ArcList**, **Scroll**, **List**, **Grid**, and **WaterFlow** components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means that the component has scrolled to the bottom, and **false** means the opposite. |

#### \[h2\]getItemRect11+

getItemRect(index: number): RectResult

Obtains the size and position of a child component relative to its container.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/kZttrKrqSpyLtqx5Ibct_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A0354142B27DF755C3396BDE69FD7179ED79D24AE2606DBBEA9CD9F5671FE2B)

This API is available for the **ArcList**, **Scroll**, **List**, **Grid**, and **WaterFlow** components.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the target child component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/wZYHGUO8ReaeOUyZjYZyCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFEC4CD4DCB962D2FC0486B9CA4F7FBFB67E03D5F06E0AF51AB552C5F071006E)

-   The value of **index** must be the index of a child component visible in the display area. Otherwise, the value is considered invalid.
-   The size and position returned for an invalid value are both **0**.

**Return value**

| Type | Description |
| :-- | :-- |
| [RectResult](../../universal-events/event-dispatch-control/custom-event-dispatch/document.md#rectresult) | 
Size and position of the child component relative to the component.

Unit: vp

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to component. |

#### \[h2\]getItemIndex14+

getItemIndex(x: number, y: number): number

Obtains the index of a child component based on coordinates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/zor_o_bFTyyck9m-WyazXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34BBCBB9B4499F53308809C20D3A2C5C880BB867E0D6486284EB0661A022B113)

This API is available for the **List**, **Grid**, and **WaterFlow** components.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X-coordinate, in vp. |
| y | number | Yes | Y-coordinate, in vp. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/ot0f1MgSQKOMJ3Wiq-ZM2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F505DCDC2819F294C0E24AD748B8DFBF5950E46C5587F8D9A62CB9440949B07)

The returned index is **\-1** for invalid coordinates.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Index of the child component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | The controller not bound to component. |

#### \[h2\]contentSize22+

contentSize(): SizeResult

Obtains the total size of the scrollable component's content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/RwPNx6kgRwaUVYYt8Ho9Kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1B0FADADB582290A00635235B70F9CE1EBAABDE84445B10B94FEFADC36E6DEB)

-   For **Grid**, **List**, **WaterFlow**, and **Scroll** components, the content size along the main axis is the total size after layout of all child components. The content size along the cross axis is the component's own cross-axis size minus paddings and borders.
    
-   **Grid**, **List**, and **WaterFlow** components employ lazy-loading mechanisms. This API relies on laid-out child nodes for estimation. If component content is not fully laid out and child component heights vary, the estimation may be inaccurate and require your adaptation. For the **List** component, you can use the **childrenMainSize** attribute to address estimation inaccuracies.
    
-   If an application dynamically adds or removes child nodes, it should dynamically obtain the total content size to ensure the API returns up-to-date results.
    
-   When the **Scroll** component has **scrollable** set to **ScrollDirection.FREE**, the obtained total content size is the total size of the child components after scaling.
    
-   When the **Scroll** component has **scrollable** set to **ScrollDirection.NONE**, the obtained total content size is 0.
    
-   If the **Grid** component has both **columnsTemplate** and **rowsTemplate** set, or neither of them set (under a non-scrollable scenario), the obtained total content size has a height of 0 and a width equal to the **Grid** component's content area width.
    

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [SizeResult](../../custom-components/custom-component-layout/document.md#sizeresult10) | 
Total size of the scrollable component's content, including the content width and height.

Unit: vp

 |

**Error codes**

For details about the error codes, see [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 100004 | Controller not bound to a component. |

#### OffsetResult11+

Represents the offset values resulting from a scroll operation.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| xOffset | number | No | No | 
Horizontal scrolling offset.

The unit of the return value is vp.

 |
| yOffset | number | No | No | 

Vertical scrolling offset.

The unit of the return value is vp.

 |

#### ScrollAnimationOptions12+

Provides parameters for customizing scroll animations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| duration | number | No | Yes | 
Scrolling duration.

Default value: **1000**

**NOTE**

A value less than 0 evaluates to the default value.

 |
| curve | [Curve](../../common-definitions/enums/document.md#curve) | [ICurve](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#icurve9) | No | Yes | 

Scrolling curve.

Default value: **Curve.Ease**

 |
| canOverScroll | boolean | No | Yes | 

Whether the scroll animation is converted to an out-of-bounds bounce animation after reaching the boundary.

Default value: **false**

**NOTE**

This conversion occurs only when **canOverScroll** is **true** and the component's **edgeEffect** attribute is set to [EdgeEffect.Spring](../../common-definitions/enums/document.md#edgeeffect). When **canOverScroll** is **false**, the animation stops directly at the boundary without converting to a bounce animation.

Since API version 20, if **canOverScroll** in [ScrollOptions](#scrolloptions18) is **true**, the scroll animation can remain at the boundary. After exceeding the boundary, it will not be converted to a bounce animation.

 |

#### ScrollAlign10+

Enumerates alignment modes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| START | 0 | Start alignment. Aligns the start of the specified item with the start of the scrollable container. |
| CENTER | 1 | Center alignment. Centers the specified item along the main axis within the scrollable container. |
| END | 2 | End alignment. Aligns the end of the specified item with the end of the scrollable container. |
| AUTO | 3 | 
Automatic alignment.

If the specified item is entirely within the visible area, no adjustment is made. Otherwise, following the shortest-scroll-distance principle, either the start or the end of the item is aligned with the scrollable container to make the item fully visible.

 |

#### ScrollToIndexOptions12+

Provides parameters for scrolling to a specific index.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| extraOffset | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Extra offset for scrolling to a specified index. A positive value offsets the scroll position downward (or toward the end); a negative value offsets it upward (or toward the start). |

#### ScrollPageOptions14+

Provides parameters for page scrolling behavior.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| next | boolean | No | No | Whether to turn to the next page. The value **true** means to scroll to the next page, and **false** means to scroll to the previous page. |
| animation | boolean | No | Yes | 
Whether to enable the page-turning animation. The value **true** means to enable the page-turning animation, and **false** means the opposite.

Default value: **false**

 |

#### OffsetOptions12+

Provides parameters for setting the initial scrolling offset.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| xOffset | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 
Horizontal scrolling offset.

Default value: **0**

 |
| yOffset | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Vertical scrolling offset.

Default value: **0**

 |

#### ScrollEdgeOptions12+

Provides parameters for scrolling to the edge of a scrollable container.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| velocity | number | No | Yes | 
Fixed velocity for scrolling to the edge of the container. If the value specified is less than or equal to 0, the parameter will not take effect.

Default value: **0**

Unit: vp/s

 |

#### ScrollOptions18+

Provides parameters for scrolling to a specific position in a scrollable container.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/EIHuL5SCRKqbLP58hCxwvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89CDCE6588F5924390A86549381979364D96ABD273F95C06BA48607D090C6817)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| xOffset10+ | number | string | No | No | 
Horizontal scroll offset.

**NOTE**

This parameter cannot be set in percentage.

This parameter takes effect only when the scroll axis is the x-axis.

Value range: Values less than 0 are treated as 0, and scrolling occurs without animation. Animated scrolling stops at the starting position by default. By setting the **animation** parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| yOffset10+ | number | string | No | No | 

Vertical scroll offset.

**NOTE**

This parameter cannot be set in percentage.

This parameter takes effect only when the scroll axis is the y-axis.

Value range: Values less than 0 are treated as 0, and scrolling occurs without animation. Animated scrolling stops at the starting position by default. By setting the **animation** parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| animation10+ | [ScrollAnimationOptions](#scrollanimationoptions12) | boolean | No | Yes | 

Animation configuration, which includes the following:

\- **ScrollAnimationOptions**: custom animation settings.

\- **boolean**: whether to enable the default spring animation.

Default value:

ScrollAnimationOptions: { duration: 1000, curve: Curve.Ease, canOverScroll: false }

boolean: false

**NOTE**

Currently, the **List**, **Scroll**, **Grid**, and **WaterFlow** support the **Boolean** type and **ICurve**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| canOverScroll20+ | boolean | No | Yes | 

Whether the scroll target position is allowed to stay beyond the boundary. This setting only takes effect when the component's **edgeEffect** is set to **EdgeEffect.Spring**.

**true**: The scroll position can stay beyond the boundary. **false**: The scroll position cannot stay beyond the boundary.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### UIScrollEvent19+

Represents the return value of the [getEvent('Scroll')](../../../arkts-api/ui/arkui/framenode/document.md#geteventscroll19) method in **frameNode**, which can be used to set scroll events for a **Scroll** node.

**UIScrollEvent** inherits from [UIScrollableCommonEvent](../scrollable-component-common-apis/document.md#uiscrollablecommonevent19).

#### \[h2\]setOnWillScroll19+

setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void

Sets the callback for the [onWillScroll](#onwillscroll12) event.

Passing **undefined** as the input parameter resets the event callback.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [ScrollOnWillScrollCallback](#scrollonwillscrollcallback12) | undefined | Yes | Callback for the **onWillScroll** event. |

#### \[h2\]setOnDidScroll19+

setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void

Sets the callback for the [onDidScroll](#ondidscroll12) event.

Passing **undefined** as the input parameter resets the event callback.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [ScrollOnScrollCallback](#scrollonscrollcallback12) | undefined | Yes | Callback for the **onDidScroll** event. |

#### Example

## Example 1: Setting the Scroller

This example demonstrates the use of some attributes of the **Scroll** component and the **Scroller**.

// xxx.ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: number) => item.toString())
        }.width('100%')
      }
      .scrollable(ScrollDirection.Vertical) // The scrollbar scrolls in the vertical direction.
      .scrollBar(BarState.On) // The scrollbar is always displayed.
      .scrollBarColor(Color.Gray) // The scrollbar color is gray.
      .scrollBarWidth(10) // The scrollbar width is 10.
      .friction(0.6)
      .edgeEffect(EdgeEffect.None)
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
        console.info(xOffset + ' ' + yOffset);
      })
      .onScrollEdge((side: Edge) => {
        console.info('To the edge');
      })
      .onScrollStop(() => {
        console.info('Scroll Stop');
      })

      Button('scroll 150')
        .height('5%')
        .onClick(() => { // Click to scroll down by 150.0 vp.
          this.scroller.scrollBy(0, 150);
        })
        .margin({ top: 10, left: 20 })
      Button('scroll 100')
        .height('5%')
        .onClick(() => { // Click to scroll down by 100.0 vp.
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 100 });
        })
        .margin({ top: 60, left: 20 })
      Button('scroll 100')
        .height('5%')
        .onClick(() => {// Click to scroll down by 100.0 vp. An animation is applied to the scrolling.
          let curve = curves.interpolatingSpring(10, 1, 228, 30); // Create a spring curve.
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 100, animation: { duration: 1000, curve: curve } });
        })
        .margin({ top: 110, left: 20 })
      Button('back top')
        .height('5%')
        .onClick(() => { // Click to go back to the top.
          this.scroller.scrollEdge(Edge.Top);
        })
        .margin({ top: 160, left: 20 })
      Button('next page')
        .height('5%')
        .onClick(() => { // Click to go to the next page.
          this.scroller.scrollPage({ next: true ,animation: true });
        })
        .margin({ top: 210, left: 20 })
      Button('fling -3000')
        .height('5%')
        .onClick(() => { // Trigger a fling with an initial velocity of -3000 vp/s.
          this.scroller.fling(-3000);
        })
        .margin({ top: 260, left: 20 })
      Button('scroll to bottom 700')
        .height('5%')
        .onClick(() => {// After the button is clicked, the component scrolls to the bottom edge at a velocity of 700 vp/s.
          this.scroller.scrollEdge(Edge.Bottom, { velocity: 700 });
        })
        .margin({ top: 310, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/c9DBIrUgRuaN5Jnw1el1rg/en-us_image_0000002537765538.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4C84B0D9FDE38CAA66CACFE552BEDF26656020926AC1FE6063378004D6B9BD3)

## Example 2: Implementing Nested Scrolling (Method 1)

This example uses the **onScrollFrameBegin** event to achieve nested scrolling between an inner **List** component and an outer **Scroll** component.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct NestedScroll {
  @State listPosition: number = 0; // 0 indicates scrolling to the top of the list, 1 indicates scrolling to the middle of the list, and 2 indicates scrolling to the bottom of the list.
  private arr: number\[\] = \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\];
  private scrollerForScroll: Scroller = new Scroller();
  private scrollerForList: Scroller = new Scroller();

  build() {
    Flex() {
      Scroll(this.scrollerForScroll) {
        Column() {
          Text('Scroll Area')
            .width('100%')
            .height('40%')
            .backgroundColor(0X330000FF)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .onClick(() => {
              this.scrollerForList.scrollToIndex(5, false, ScrollAlign.START, { extraOffset: LengthMetrics.vp(5) });
            })

          List({ space: 20, scroller: this.scrollerForList }) {
            ForEach(this.arr, (item: number) => {
              ListItem() {
                Text('ListItem' + item)
                  .width('100%')
                  .height('100%')
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(Color.White)
              }.width('100%').height(100)
            }, (item: string) => item)
          }
          .width('100%')
          .height('50%')
          .edgeEffect(EdgeEffect.None)
          .friction(0.6)
          .onReachStart(() => {
            this.listPosition = 0;
          })
          .onReachEnd(() => {
            this.listPosition = 2;
          })
          .onScrollFrameBegin((offset: number) => {
            if ((this.listPosition == 0 && offset <= 0) || (this.listPosition == 2 && offset >= 0)) {
              this.scrollerForScroll.scrollBy(0, offset);
              return { offsetRemain: 0 };
            }
            this.listPosition = 1;
            return { offsetRemain: offset };
          })

          Text('Scroll Area')
            .width('100%')
            .height('40%')
            .backgroundColor(0X330000FF)
            .fontSize(16)
            .textAlign(TextAlign.Center)
        }
      }
      .width('100%').height('100%')
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/buCtKF_-RlikIVbYMvAEmg/en-us_image_0000002537925478.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67921A87E60FFB904045144795597C29C4AF035135AEF2E0DE5745A2789C759A)

## Example 3: Implementing Nested Scrolling (Method 2)

This example uses the [nestedScroll](#nestedscroll10) attribute to achieve nested scrolling between an inner **List** component and an outer **Scroll** component.

@Entry
@Component
struct StickyNestedScroll {
  @State arr: number\[\] = \[\];

  @Styles
  listCard() {
    .backgroundColor(Color.White)
    .height(72)
    .width('100%')
    .borderRadius(12)
  }

  build() {
    Scroll() {
      Column() {
        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor('#0080DC')
          .textAlign(TextAlign.Center)
        Tabs({ barPosition: BarPosition.Start }) {
          TabContent() {
            List({ space: 10 }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('item' + item)
                    .fontSize(16)
                }.listCard()
              }, (item: number) => item.toString())
            }.width('100%')
            .edgeEffect(EdgeEffect.Spring)
            .nestedScroll({
              scrollForward: NestedScrollMode.PARENT\_FIRST,
              scrollBackward: NestedScrollMode.SELF\_FIRST
            })
          }.tabBar('Tab1')

          TabContent() {
          }.tabBar('Tab2')
        }
        .vertical(false)
        .height('100%')
      }.width('100%')
    }
    .edgeEffect(EdgeEffect.Spring)
    .friction(0.6)
    .backgroundColor('#DCDCDC')
    .scrollBar(BarState.Off)
    .width('100%')
    .height('100%')
  }

  aboutToAppear() {
    for (let i = 0; i < 30; i++) {
      this.arr.push(i);
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/stG4OtteQVK9nZSGupGcOA/en-us_image_0000002568685255.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56CDEECDFCE68D926C5900F9CDCEEF15C815F5250F66B3DA0552C7E5E88C50AC)

## Example 4: Implementing Nested Scrolling with Parent-to-Child Scrolling Propagation

This example demonstrates how to propagate scrolling from a parent component to a child component using the [enableScrollInteraction](#enablescrollinteraction10) attribute and the [onScrollFrameBegin](#onscrollframebegin9) event.

@Entry
@Component
struct NestedScroll {
  private headerHeight: number = 0;
  private arr: number\[\] = \[\];
  private scrollerForParent: Scroller = new Scroller();
  private scrollerForChild: Scroller = new Scroller();

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.arr.push(i);
    }
  }

  build() {
    Scroll(this.scrollerForParent) {
      Column() {
        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor(0X330000FF)
          .fontSize(16)
          .textAlign(TextAlign.Center)
          .onClick(() => {
            this.scrollerForChild.scrollToIndex(5);
          })
          .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
            this.headerHeight = newValue.height! as number;
          })
        List({ space: 20, scroller: this.scrollerForChild }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('ListItem' + item)
                .width('100%')
                .height('100%')
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .backgroundColor(Color.White)
            }.width('100%').height(100)
          }, (item: number) => item.toString())
        }
        .width('100%')
        .height('100%')
        .edgeEffect(EdgeEffect.None)
        .scrollBar(BarState.Off)
        .enableScrollInteraction(false)

        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor(0X330000FF)
          .fontSize(16)
          .textAlign(TextAlign.Center)
      }
    }
    .scrollBar(BarState.Off)
    .edgeEffect(EdgeEffect.Spring)
    .onScrollFrameBegin((offset: number, state: ScrollState) => {
      let retOffset = offset;
      let currOffset = this.scrollerForParent.currentOffset().yOffset;
      let newOffset = currOffset + offset;
      if (offset > 0) {
        if (this.scrollerForChild.isAtEnd()) {
          return { offsetRemain: offset };
        }
        if (newOffset > this.headerHeight) {
          retOffset = this.headerHeight - currOffset;
        }
        this.scrollerForChild.scrollBy(0, offset - retOffset);
      } else {
        if (this.scrollerForChild.currentOffset().yOffset <= 0) {
          return { offsetRemain: offset };
        }
        if (newOffset < this.headerHeight) {
          retOffset = this.headerHeight - currOffset;
        }
        this.scrollerForChild.scrollBy(0, offset - retOffset);
      }
      return { offsetRemain: retOffset };
    })
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/n6x2SUMrTuSA_Epa2cicjw/en-us_image_0000002568765265.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1F201C52F48A777AD01C0CFDD2B6C73CEA4D907BB9328B716210B3FD918C394)

## Example 5: Setting Scroll Snapping

This example shows how to set scroll snapping for a **Scroll** component.

@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15\];
  build() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item: number) => {
          Text(item.toString())
            .width('90%')
            .height(200)
            .backgroundColor(0xFFFFFF)
            .borderWidth(1)
            .borderColor(Color.Black)
            .borderRadius(15)
            .fontSize(16)
            .textAlign(TextAlign.Center)
        }, (item: number) => item.toString())
      }.width('100%').backgroundColor(0xDCDCDC)
    }
    .backgroundColor(Color.Yellow)
    .height('100%')
    .edgeEffect(EdgeEffect.Spring)
    .scrollSnap({snapAlign:ScrollSnapAlign.START, snapPagination:400, enableSnapToStart:true, enableSnapToEnd:true})
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/YXFV5WeyRbyyGUJ7B-RGFw/en-us_image_0000002537765540.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19B85A1F6B79F5707553E48280DDF9986F5B1A17A748CE2CC7097DB24D408D74)

## Example 6: Obtaining the Index of a Child Component

This example demonstrates how to obtain the index of a child component in a **List** component.

// xxx.ets
@Entry
@Component
struct ListExample {
  private arr: number\[\] = \[\];
  private scroller: ListScroller = new ListScroller();
  @State listSpace: number = 10;
  @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100);
  @State listIndex: number = -1;
  @State itemBackgroundColorArr: boolean\[\] = \[false\];
  aboutToAppear(){
    // Initialize the data source.
    for (let i = 0; i < 10; i++) {
      this.arr.push(i);
    }
    this.listChildrenSize.splice(0, 5, \[100, 100, 100, 100, 100\]);
  }
  build() {
    Column() {
      List({ space: this.listSpace, initialIndex: 4, scroller: this.scroller }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('item-' + item)
              .height( item < 5 ? 100 : this.listChildrenSize.childDefaultSize)
              .width('90%')
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor( this.itemBackgroundColorArr\[item\] ? 0x68B4FF: 0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .backgroundColor(Color.Gray)
      .layoutWeight(1)
      .scrollBar(BarState.On)
      .childrenMainSize(this.listChildrenSize)
      .alignListItem(ListItemAlign.Center)
      .gesture(
        PanGesture()
          .onActionUpdate((event: GestureEvent) => {
            if (event.fingerList\[0\] != undefined && event.fingerList\[0\].localX != undefined && event.fingerList\[0\].localY != undefined) {
              this.listIndex = this.scroller.getItemIndex(event.fingerList\[0\].localX, event.fingerList\[0\].localY);
              this.itemBackgroundColorArr\[this.listIndex\] = true;
            }
          })
      )
      .gesture(
        TapGesture({ count: 1 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.itemBackgroundColorArr.splice(0,this.itemBackgroundColorArr.length);
            }
          })
      )

      Text('You are currently at index '+ this.listIndex)
        .fontColor(Color.Red)
        .height(50)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/-TaNYg9rSIelxJbbL4SigA/en-us_image_0000002537925480.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA998301EAF22C05E1448DAA1492834A9B573771939A9943B92BDBB4C8B5ADC7)

## Example 7: Setting Edge Fading

This example demonstrates how to implement a **Scroll** component with an edge fading effect and set the length of the fading edge.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }.width('100%')
      }
      .fadingEdge(true,{fadingEdgeLength:LengthMetrics.vp(80)})

    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/aDwQOV11Qr2lbBrZqfSyBw/en-us_image_0000002568685257.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E5B65D78440373AF5510E541CAA497597678E8AB51CE6A0702BA7ED0F609990)

## Example 8: Setting the Single-Side Edge Effect

This example demonstrates how to set a single-side edge effect for the **Scroll** component using the [edgeEffect](#edgeeffect) API.

// xxx.ets
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }.width('100%')
      }
      .edgeEffect(EdgeEffect.Spring,{alwaysEnabled:true,effectEdge:EffectEdge.START})
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/VwGYxca-R0WhusFy5S0tzA/en-us_image_0000002568765267.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4C7C15791A030FE63DD02C2D0DC4DF6665C4CE890999F5529066112146BA24C)

## Example 9: Implementing the Swipe-to-Turn-Pages Feature

This example demonstrates how to implement the swipe-to-turn-pages feature for a **Scroll** component using the [enablePaging](#enablepaging11) API.

// xxx.ets
@Entry
@Component
struct EnablePagingExample {
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Scroll() {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('100%')
              .height('100%')
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .backgroundColor(0xFFFFFF)
          }, (item: number) => item.toString())
        }
      }.width('90%').height('90%')
      .enablePaging(true)
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/i5nBWUJ7QLqzPMBKl6E_cQ/en-us_image_0000002537765542.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28F97061C3CAC787145C535E06B461DBD4132BBE7CA7AF56A89FEC8732FBA13E)

## Example 10: Implementing the Overscroll Stay Effect

This example demonstrates how to implement the overscroll stay effect for a **Scroll** component using the [scrollTo](#scrollto) API.

// xxx.ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct StickyNestedScroll {
  scroller: Scroller = new Scroller;

  build() {
    Column() {
      Row() {
        Button('scrollTo: Animation').onClick(() => {
          let curve = curves.interpolatingSpring(0.5, 5, 10, 15) // Create a spring curve.
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({
            xOffset: 0,
            yOffset: yOffset - 100,
            animation: { duration: 1000, curve: curve, canOverScroll: true },
            canOverScroll: true
          })
        }).margin({ top: 10 })
        Button('scrollTo: No Animation').onClick(() => {
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({
            xOffset: 0,
            yOffset: yOffset - 100,
            animation: false,
            canOverScroll: true
          })
        }).margin({ top: 10, left: 20 })
      }.margin({ bottom: 20 })

      Scroll(this.scroller) {
        Column() {
          Text('Scroll Area')
            .width('100%')
            .height('100%')
            .backgroundColor('#0080DC')
            .textAlign(TextAlign.Center)
        }
        .width('100%')
        .height('100%')
      }
      .scrollable(ScrollDirection.Vertical)
      .edgeEffect(EdgeEffect.Spring) // Set the edge effect.
      .fadingEdge(false) // Disable the edge fading effect.
      .scrollBar(BarState.Auto)
      .friction(undefined)
      .backgroundColor('#DCDCDC')
      .width('100%')
      .height('50%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Kp688g1dQ72gk2NbJ73k9w/en-us_image_0000002537925482.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A65063432F3CFDE9C726EBCFA0D2FEF73430E9EE8105FE9979E5B54040785684)

## Example 11: Implementing Free Scrolling and Scaling

This example demonstrates how to implement free scrolling and scaling of the **Scroll** component. This functionality is supported since API version 20.

@Entry
@Component
struct ScrollZoomExample {
  @State currScale:number = 1;
  build() {
    Column() {
      Scroll() {
        Image($r('app.media.image1')) // 'app.media.image1' is only as an example. Replace it with the actual image.
      }
      .height(400)
      .scrollable(ScrollDirection.FREE)
      .minZoomScale(1)
      .maxZoomScale(2)
      .zoomScale(this.currScale!!)
      .enableBouncesZoom(true)
      .onDidZoom((scale: number) => {
        console.info(\`onDidZoom:${scale}\`);
      })
      .onZoomStart(() => {
        console.info('onZoomStart');
      })
      .onZoomStop(() => {
        console.info('onZoomStop');
      })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/fEy7Kz2zTAShw6aW7fmL4g/en-us_image_0000002568685259.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F88275C3561EB5EA1BCC3199006AA5FCFEA6EC76D884159D6B444A157945810)

## Example 12: Obtaining the Total Content Size

This example demonstrates how to obtain the total content size. This functionality is supported since API version 22.

import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ScrollExample1 {
  scroller: Scroller = new Scroller();
  private arr: number\[\] = \[\]

  aboutToAppear() {
    for (let j = 0; j < 10; j++) {
      this.arr.push(j);
    }
  }

  @State contentWidth: number = -1;
  @State contentHeight: number = -1;

  build() {
    Column() {
      Text('Set Scroller Controller and ForEach')
      Row() {
        // Button to obtain the content size.
        Button('GetContentSize')
          .onClick(() => {
            // Scroller throws an exception when not bound to a component; wrap with try-catch for safety.
            try {
              // Obtain the content width using contentSize.
              this.contentWidth = this.scroller.contentSize().width;
              // Obtain the content height using contentSize.
              this.contentHeight = this.scroller.contentSize().height;
            } catch (error) {
              let err: BusinessError = error as BusinessError;
                console.error(\`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}\`);
            }
          })
        // Display the obtained content size.
        Text('Width: ' + this.contentWidth + ', Height: ' + this.contentHeight)
          .fontColor(Color.Red)
          .height(50)
      }

      Stack({ alignContent: Alignment.TopStart }) {
        Scroll(this.scroller) {
          Column() {
            ForEach(this.arr, (item: number) => {
              Text(item.toString())
                .width('90%')
                .height(150)
                .backgroundColor(0xFFFFFF)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            }, (item: number) => item.toString())
          }.width('100%')
        }
        .scrollable(ScrollDirection.Vertical) // The scrollbar scrolls in the vertical direction.
        .scrollBar(BarState.On) // The scrollbar is always displayed.
        .scrollBarColor(Color.Gray) // The scrollbar color is gray.
        .scrollBarWidth(10) // The scrollbar width is 10.
        .friction(0.6)
        .edgeEffect(EdgeEffect.None)
      }.width('100%').height('100%').backgroundColor(0xDCDCDC)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/fggamU_hQL24AoLkeR_p4Q/en-us_image_0000002568765269.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82484623C754D5989E805D90AE0A23E577EE61A8A4C974B00784D44CB50504BF)

## Example 13: Setting Scrolling Events

This example obtains a [UIScrollEvent](#uiscrollevent19) instance via [getEvent('Scroll')](../../../arkts-api/ui/arkui/framenode/document.md#geteventscroll19) on a FrameNode and sets scroll event callbacks for a **Scroll** component. This approach is intended for scenarios where the page code cannot be directly modified to use declarative callbacks.

The **UIScrollEvent** API is supported since API version 19.

import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute.width(100);
    return this.rootNode;
  }

  addCommonEvent(frameNode: FrameNode) {
    // Obtain the Scroll event object.
    let scrollEvent: UIScrollEvent | undefined = typeNode.getEvent(frameNode, 'Scroll');

    // Set the OnWillScroll callback.
    scrollEvent?.setOnWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState,
      scrollSource: ScrollSource) => {
      console.info('onWillScroll xOffset = ${xOffset}, yOffset = ${yOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}');
    });

    // Set the OnDidScroll callback.
    scrollEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
      console.info('onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}');
    });

    // Set the OnReachStart callback.
    scrollEvent?.setOnReachStart(() => {
      console.info('onReachStart');
    });

    // Set the OnReachEnd callback.
    scrollEvent?.setOnReachEnd(() => {
      console.info('onReachEnd');
    });

    // Set the OnScrollStart callback.
    scrollEvent?.setOnScrollStart(() => {
      console.info('onScrollStart');
    });

    // Set the OnScrollStop callback.
    scrollEvent?.setOnScrollStop(() => {
      console.info('onScrollStop');
    });

    // Set the OnScrollFrameBegin callback.
    scrollEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
      console.info('onScrollFrameBegin offset = ${offset}, state = ${state}');
      return undefined;
    });
  }
}

@Entry
@Component
struct Index {
  @State index: number = 0;
  private myNodeController: MyNodeController = new MyNodeController();
  @State numbers: string\[\] = \[\];

  aboutToAppear() {
    for (let i = 0; i < 30; i++) {
      this.numbers.push('${i+1}');
    }
  }

  build() {
    Column() {
      Button('add CommonEvent to Scroll')
        .onClick(() => {
          this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!)
        })
      Scroll() {
        Column() {
          ForEach(this.numbers, (day: string, index: number) => {
            Column() {
              Text(day)
                .fontSize(16)
                .backgroundColor(0xF9CF93)
                .width('90%')
                .height(80)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            }
            .width('100%')
            .justifyContent(FlexAlign.Center)
            .alignItems(HorizontalAlign.Center)
          }, (day: string, index: number) => index.toString() + day)
        }
      }
      .scrollable(ScrollDirection.Vertical)
      .edgeEffect(EdgeEffect.Spring)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
      NodeContainer(this.myNodeController)
    }
  }
}
