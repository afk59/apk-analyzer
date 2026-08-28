# Common Event Callbacks

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/BivwMWNjSt6iDavo9b3Eiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9696723AD2C13EC9771FD4C0285082CE0DD022D1C34405A4626ACECE90064BDB)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### UICommonEvent

Implements a common event callback. Passing **undefined** as the input parameter resets the corresponding event callback.

#### \[h2\]setOnClick

setOnClick(callback: Callback<ClickEvent> | undefined): void

Set the callback for the [click event](../../universal-events/interaction-response-events/click-event/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<[ClickEvent](../../universal-events/interaction-response-events/click-event/document.md#clickevent)\> | undefined | Yes | Callback for the click event. |

#### \[h2\]setOnTouch

setOnTouch(callback: Callback<TouchEvent> | undefined): void

Sets the callback for the [touch event](../../universal-events/basic-input-events/touch-event/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<[TouchEvent](../../universal-events/basic-input-events/touch-event/document.md#touchevent)\> | undefined | Yes | Callback for the touch event. |

#### \[h2\]setOnAppear

setOnAppear(callback: Callback<void> | undefined): void

Sets the callback for the [onAppear](../../universal-events/component-change-events/show-hide-event/document.md#onappear) event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<void> | undefined | Yes | Callback invoked when the component appears. |

#### \[h2\]setOnDisappear

setOnDisappear(callback: Callback<void> | undefined): void

Sets the callback for the [onDisAppear](../../universal-events/component-change-events/show-hide-event/document.md#ondisappear) event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<void> | undefined | Yes | Callback invoked when the component disappears. |

#### \[h2\]setOnKeyEvent

setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void

Sets the callback for the [key event](../../universal-events/basic-input-events/key-event/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<[KeyEvent](../../universal-events/basic-input-events/key-event/document.md#keyevent)\> | undefined | Yes | Callback for the key event. |

#### \[h2\]setOnFocus

setOnFocus(callback: Callback<void> | undefined): void

Sets the callback for the [onFocus](../../universal-events/interaction-response-events/focus-event/document.md#onfocus) event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<void> | undefined | Yes | Callback for the focus event. |

#### \[h2\]setOnBlur

setOnBlur(callback: Callback<void> | undefined): void

Sets the callback for the [onBlur](../../universal-events/interaction-response-events/focus-event/document.md#onblur) event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<void> | undefined | Yes | Callback for the blur event. |

#### \[h2\]setOnHover

setOnHover(callback: HoverCallback | undefined): void

Sets the callback for the [onHover](../../universal-events/interaction-response-events/hover-event/document.md#onhover) event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [HoverCallback](#hovercallback) | undefined | Yes | Callback for the hover event. |

#### \[h2\]setOnMouse

setOnMouse(callback: Callback<MouseEvent> | undefined): void

Sets the callback for the [onMouse](../../universal-events/basic-input-events/mouse-event/document.md#onmouse) event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../basic-types/document.md#callback12)<[MouseEvent](../../universal-events/basic-input-events/mouse-event/document.md#mouseevent)\> | undefined | Yes | Callback for the mouse event. |

#### \[h2\]setOnSizeChange

setOnSizeChange(callback: SizeChangeCallback | undefined): void

Sets the callback for the [onSizeChange](../../universal-events/component-change-events/component-size-change-event/document.md#onsizechange) event, which is triggered when the component's size changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [SizeChangeCallback](../../universal-events/component-change-events/component-size-change-event/document.md#sizechangecallback) | undefined | Yes | Callback invoked when the component's size changes. |

#### \[h2\]setOnVisibleAreaApproximateChange

setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void

Sets the callback for the [onVisibleAreaChange](../../universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange) visible area change event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [VisibleAreaEventOptions](../../universal-events/component-change-events/visible-area-change-event/document.md#visibleareaeventoptions12) | Yes | Configuration options for visible area change detection. |
| event | [VisibleAreaChangeCallback](../../universal-events/component-change-events/visible-area-change-event/document.md#visibleareachangecallback12) | undefined | Yes | Callback invoked when the ratio of the component's visible area to its total area crosses the threshold specified in **options**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/IRFS3ZuXRzajTtsRn9_UEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=038C7339B2C0F95F529DD9960ECBE499F4F12216ECB5261D64C2E823B4E84D2F)

Difference from [onVisibleAreaChange](../../universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange): **onVisibleAreaChange** calculates the visible area ratio every frame, which can lead to high power consumption when many nodes are registered. This API reduces the calculation frequency: The interval is controlled by the **expectedUpdateInterval** parameter in [VisibleAreaEventOptions](../../universal-events/component-change-events/visible-area-change-event/document.md#visibleareaeventoptions12).

By default, the interval threshold of the visible area change callback includes 0. This means that, if the provided threshold is \[0.5\], the effective threshold will be \[0.0, 0.5\].

#### HoverCallback

type HoverCallback = (isHover: boolean, event: HoverEvent)=> void

Defines the callback type for hover events.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isHover | boolean | Yes | Whether the element is in the hover state. **true**: yes; **false**: no. |
| event | [HoverEvent](../../universal-events/interaction-response-events/hover-event/document.md#hoverevent10) | Yes | Position coordinates of the hovered mouse or stylus. |
