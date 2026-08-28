# Class (EventResult)

Represents the event consumption result sent to the **Web** component. For details about the supported events, see [TouchType](../../../../arkui/arkts-components/common-definitions/enums/document.md#touchtype), [MouseAction](../../../../arkui/arkts-components/common-definitions/enums/document.md#mouseaction8), and left, middle, and right buttons in [MouseButton](../../../../arkui/arkts-components/common-definitions/enums/document.md#mousebutton8).

If the application does not consume the event, set the consumption result to **false**, and the event will be consumed by the **Web** component. If the application consumes the event, set the consumption result to **true**, and the **Web** component will not consume the event. If the consumption result set by the application does not comply with the above specifications, behavior inconsistent with developer expectations will occur.

For details about the sample code of the touch event, see [onNativeEmbedGestureEvent](../events/document.md#onnativeembedgestureevent11).

For details about the sample code of the mouse event, see [onNativeEmbedMouseEvent](../events/document.md#onnativeembedmouseevent20).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/-4J0SKSaSVi-S7361mmRMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A21B2B9F729D308EF4F698229FE81EB85716FBEEB0B28DACEC4F0EF44FD51525)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### constructor12+

constructor()

Constructs a **EventResult** object.

**System capability**: SystemCapability.Web.Webview.Core

#### setGestureEventResult12+

setGestureEventResult(result: boolean): void

Sets the gesture event consumption result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | boolean | Yes | 
Whether to consume the gesture event.

The value **true** means to consume the gesture event, and **false** means the opposite.

If **null** or **undefined** is passed in, the value is **true**.

 |

**Example**

For details, see [onNativeEmbedGestureEvent](../events/document.md#onnativeembedgestureevent11).

#### setGestureEventResult14+

setGestureEventResult(result: boolean, stopPropagation: boolean): void

Sets the gesture event consumption result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | boolean | Yes | 
Whether to consume the gesture event.

The value **true** means to consume the gesture event, and **false** means the opposite.

If **null** or **undefined** is passed in, the value is **true**.

 |
| stopPropagation | boolean | Yes | 

Whether to stop propagation. This parameter is valid only when **result** is set to **true**.

The value **true** means to stop propagation, and **false** means the opposite.

If **null** or **undefined** is passed in, the value is **true**.

 |

**Example**

For details, see [onNativeEmbedGestureEvent](../events/document.md#onnativeembedgestureevent11).

#### setMouseEventResult20+

setMouseEventResult(result: boolean, stopPropagation?: boolean): void

Sets the mouse event consumption result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | boolean | Yes | 
Whether to consume the mouse event.

The value **true** means to consume the mouse event, and **false** means the opposite.

If **null** or **undefined** is passed in, the value is **true**.

 |
| stopPropagation | boolean | No | 

Whether to stop propagation. This parameter is valid only when **result** is set to **true**.

The value **true** means to stop propagation, and **false** means the opposite.

If **null** or **undefined** is passed in, the value is **true**.

 |

**Example**

For details, see [onNativeEmbedMouseEvent](../events/document.md#onnativeembedmouseevent20).
