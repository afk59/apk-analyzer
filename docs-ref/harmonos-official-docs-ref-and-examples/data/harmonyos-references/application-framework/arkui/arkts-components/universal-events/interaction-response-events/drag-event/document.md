# Drag Event

A drag event refers to a sequence of events triggered in the UI when a user drags an object (such as a file, component, or element). These events allow you to customize drag behaviors, enabling functions like drag-and-drop and position adjustment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/fIbSfH_jRQSiZ4fFSpIztg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24B09C76999AC00738BE4BFF2BB58D75E9F68C38B888FE39DF315EC8EC81ED75)

-   The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The resource files preset in the application (that is, the resource files that are contained in the HAP file before the application is installed) can be dragged and dropped only within the application.
    

The ArkUI framework provides default drag and drop capabilities for the following components, allowing them to serve as the drag source (from which data can be dragged) or drop target (to which data can be dropped). You can further customize drag and drop behavior by implementing universal drag events.

-   The following component supports drag actions by default: [Search](../../../text-and-input/search/document.md), [TextInput](../../../text-and-input/textinput/document.md), [TextArea](../../../text-and-input/textarea/document.md), [RichEditor](../../../text-and-input/richeditor/document.md), [Text](../../../text-and-input/text/document.md), [Image](../../../images-and-videos/image/document.md), [Hyperlink](../../../text-and-input/hyperlink/document.md). You can control the default drag behavior by setting the [draggable](../../../universal-attributes/interaction-properties/drag-and-drop-control/document.md#draggable) attribute.
    
-   The following component supports drop actions by default: [Search](../../../text-and-input/search/document.md), [TextInput](../../../text-and-input/textinput/document.md), [TextArea](../../../text-and-input/textarea/document.md), [RichEditor](../../../text-and-input/richeditor/document.md). You can disable the default drag behavior by setting the [allowDrop](../../../universal-attributes/interaction-properties/drag-and-drop-control/document.md#allowdrop) attribute to **null**.
    

To enable drag and drop for other components that support drag actions, set their [draggable](../../../universal-attributes/interaction-properties/drag-and-drop-control/document.md#draggable) attribute to **true** and implement data transmission in APIs such as [onDragStart](#ondragstart).

The draggable attribute of the Text, TextInput, TextArea, Hyperlink, Image, RichEditor, and Web components is true by default, indicating that the component is draggable.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/xaVbpkE6Q3yf_A8ODVzXfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DAD5208BBB56E51FC2F88A3158897A0C998730B582D0227CBCBE586065F37EB)

When using the **Text** component, set [copyOption](../../../text-and-input/text/document.md#copyoption9) to **CopyOptions.InApp** or **CopyOptions.LocalDevice**.

#### onDragStart

onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T

In a gesture-based drag scenario, this callback is triggered when a user long-presses a draggable component for more than 500 ms and then moves the finger more than 10 vp. In a mouse-drag scenario, it is triggered when the left mouse button is pressed on a draggable component and moved more than 1 vp.

For components that provide drag and drop capabilities by default, a custom **onDragStart** event, if set, is executed and:

-   If a custom drag preview is returned, it is used in place of the default drag preview.
-   If drag data is set, it is used in place of the default drag data.

The custom drag preview is not supported for dragging selected text in the following components: [Text](../../../text-and-input/text/document.md), [Search](../../../text-and-input/search/document.md), [TextInput](../../../text-and-input/textinput/document.md), [TextArea](../../../text-and-input/textarea/document.md), [RichEditor](../../../text-and-input/richeditor/document.md) When **onDragStart** is used with menu preview or any component that provides default drag and drop capabilities, custom content on menu items and the preview cannot be dragged.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/KiqVtCuzRbqHDYjxHGsIoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77872B3D3E9DE3BB0338295983FAD550F7953704514D309287E6A80562D1BD62)

This API can be called in [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 13.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Event priority**:

Long press duration < 500 ms: Long press event > Drag event

Long-press duration ≥ 500 ms: Drag event > Long press event

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [DragEvent](#dragevent7), extraParams?: string) => [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](#dragiteminfo) | Yes | 
Callback function.

**NOTE**

**event**: drag event information.

**extraParams**: additional information about the drag event. Its value must be parsed into JSON format. For details, see [extraParams](#extraparams).

**CustomBuilder**: component information displayed during dragging. Global builders are not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDragEnter

onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T

Triggered when a dragged item enters a valid drop target. This event takes effect only when a listener for the [onDrop](#ondrop) event is enabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [DragEvent](#dragevent7), extraParams?: string) => void | Yes | 
Callback function.

**NOTE**

**event**: drag event information, including the coordinates of the drag point.

**extraParams**: additional information about the drag event. Its value must be parsed into JSON format. For details, see [extraParams](#extraparams).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDragMove

onDragMove(event: (event: DragEvent, extraParams?: string) => void): T

Triggered when a dragged item moves in a valid drop target. This event takes effect only when a listener for the [onDrop](#ondrop) event is enabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [DragEvent](#dragevent7), extraParams?: string) => void | Yes | 
Callback function.

**NOTE**

**event**: drag event information, including the coordinates of the drag point.

**extraParams**: additional information about the drag event. Its value must be parsed into JSON format. For details, see [extraParams](#extraparams).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDragLeave

onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T

Triggered when a dragged item leaves a valid drop target. This event takes effect only when a listener for the [onDrop](#ondrop) event is enabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [DragEvent](#dragevent7), extraParams?: string) => void | Yes | 
Callback function.

**NOTE**

**event**: drag event information, including the coordinates of the drag point.

**extraParams**: additional information about the drag event. Its value must be parsed into JSON format. For details, see [extraParams](#extraparams).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDrop

onDrop(event: (event: DragEvent, extraParams?: string) => void): T

A component bound with this event can serve as a drop target. This callback is triggered when the drag-and-drop action stops within the bounds of this component If **event.setResult()** is not explicitly called in the **onDrop** callback to set the drag-and-drop result, then: For supported components, the result is determined based on the actual data processed; for other components, the system considers the data as successfully received.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [DragEvent](#dragevent7), extraParams?: string) => void | Yes | 
Callback function.

**NOTE**

**event**: drag event information, including the coordinates of the drag point.

**extraParams**: additional information about the drag event. Its value must be parsed into JSON format. For details, see [extraParams](#extraparams).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDrop15+

onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T

Triggered when a dragged item is dropped on a valid drop target. If you do not explicitly call event.[setResult](#setresult10)() in **onDrop** to set the result of the drag reception, the system handles it as follows:

\- If the component being dragged is one that supports drop actions by default, the system's actual data processing result is used.

\- For other components, the system assumes that the data is received successfully.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventCallback | [OnDragEventCallback](#ondrageventcallback15) | Yes | Callback function. |
| dropOptions | [DropOptions](#dropoptions15) | No | Parameters for the drop process. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDragEnd10+

onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T

Triggered when the dragging of the component bound to the event ends.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [DragEvent](#dragevent7), extraParams?: string) => void | Yes | 
Callback function.

**NOTE**

**event**: drag event information. The coordinates of the drag point are not included in **onDragEnd**.

**extraParams**: additional information about the drag event. Its value must be parsed into JSON format. For details, see [extraParams](#extraparams).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onPreDrag12+

onPreDrag(callback: Callback<PreDragStatus>): T

Triggered when the component enters a state prior to a gesture-based drag operation. For details about the state prior to the drag-and-drop operation, see [PreDragStatus](#predragstatus12). This API cannot be triggered in mouse-based drag scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/oxjc-hLGTpS6JVGv1TwT4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=326664192A0B8E64FB8926DF473105FAA1F24E9F4F92F6B5DE6030A7013BCF48)

This API can be called in [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[PreDragStatus](#predragstatus12)\> | Yes | Callback function. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDragSpringLoading20+

onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T

The component bound to this event can be used as a drag-response target with hover detection capability. When the dragged object hovers over the target, the callback is triggered. Only one target can become the responder at any time, and child components always have higher response priority.

For details about the hover detection triggering mechanism and usage, see [Spring Loading (Hover Detection) Support](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-drag-event#spring-loading-hover-detection-support).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[SpringLoadingContext](#springloadingcontext20)\> | null | Yes | Hover detection callback. If the value is **null**, hover detection is disabled. |
| configuration | [DragSpringLoadingConfiguration](../../../../arkts-api/ui/ohos-arkui-dragcontroller-dragcontroller/document.md#dragspringloadingconfiguration20) | No | Hover detection configuration. If the value is **undefined**, the default value of [DragSpringLoadingConfiguration](../../../../arkts-api/ui/ohos-arkui-dragcontroller-dragcontroller/document.md#dragspringloadingconfiguration20) is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### DragItemInfo

Defines the information about the dragged item during drag.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pixelMap | [PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Image to be displayed during dragging. |
| builder | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | 
Custom component to display during dragging. If **pixelMap** is set, this parameter is ignored.

**NOTE**

Global builder definition is not supported. If the [Image](../../../images-and-videos/image/document.md) component is used in the builder, enable synchronous loading whenever possible, that is, set the [syncLoad](../../../images-and-videos/image/document.md#syncload8) attribute of the component to **true**. The builder is used only to generate the image displayed during the current dragging. Changes to the builder, if any, apply to the next dragging, but not to the current dragging.

When passing the builder as a parameter, the format builder: ()=>{this.customBuilder()} is recommended to ensure correctness of this binding. For details, see [Using Functions Decorated with @Builder as CustomBuilder Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder#using-functions-decorated-with-builder-as-custombuilder-types).

 |
| extraInfo | string | No | Yes | Additional information about the dragged item, used to describe the item being dragged. |

#### PreviewConfiguration15+

Configures the style of the preview image during custom drag operations.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onlyForLifting | boolean | No | Yes | 
Whether the custom preview image is used only for lifting.

**NOTE**

The default value is **false**. **true**: The custom preview image is used only for lifting. **false**: The custom preview image is used for both lifting and dragging. When the value is set to **true**, the preview image is used only during the lifting phase of a long press. For the preview image used during the dragging phase: The [dragPreview](../../../universal-attributes/interaction-properties/drag-and-drop-control/document.md#dragpreview11) attribute is ignored, and the system prioritizes the image returned in [onDragStart](#ondragstart); if no image is returned in **onDragStart**, the component's snapshot is used.

 |
| delayCreating | boolean | No | Yes | 

Whether the preview builder is loaded at the time of setting.

The default value is **false**. The value **true** means that the preview builder is loaded at the time of setting, and **false** means the opposite.

 |

#### extraParams

Provides additional information required for dragging an item.

**extraParams** is a string converted from a JSON object. You can obtain the following attributes using the JSON object converted from **JSON.parse**.

| Name | Type | Description |
| :-- | :-- | :-- |
| selectedIndex | number | 
Index of the dragged item in the parent container. The value of **selectedindex** starts from **0**.

This parameter takes effect only in the drag event of the [ListItem](../../../scroll-and-swipe/listitem/document.md) component. Otherwise, **undefined** is returned.

 |
| insertIndex | number | 

Index of the element into which the dragged item is dropped in the **List** component. The value of **insertIndex** starts from **0**.

This parameter takes effect only in the drag event of the [List](../../../scroll-and-swipe/list/document.md) component. Otherwise, **undefined** is returned.

 |

#### DragEvent7+

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| useCustomDropAnimation10+ | boolean | No | No | 
Whether to disable the default drop animation when the dragging ends.

If this parameter is set to **true**, the default drop animation is disabled, and the custom one is used.

If this parameter is not set or is set to **false**, the default drop animation takes effect. When [setResult](#setresult10) is set to **DRAG\_SUCCESSFUL**, a shrink-out animation takes effect. Otherwise, an expand-out animation takes effect.

When the default drop animation is not disabled, avoid implementing custom animations to prevent conflicts.

Default value: **false**

 |
| dragBehavior10+ | [DragBehavior](#dragbehavior10) | No | No | 

Copy or paste mode.

Default value: **DragBehavior.COPY**

 |

#### \[h2\]setData10+

setData(unifiedData: UnifiedData): void

Sets drag-related data in **DragEvent**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| unifiedData | [UnifiedData](#unifieddata10) | Yes | Drag-related data. |

#### \[h2\]getData10+

getData(): UnifiedData

Obtains drag-related data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [UnifiedData](../../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddata) | Drag-related data. For details about the data obtaining result, see the error code description. |

**Error codes**

For details about the error codes, see [Drag Event Error Codes](../../../../error-codes/ui/drag-event-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 190001 | Data not found. |
| 190002 | Data error. |

#### \[h2\]getSummary10+

getSummary(): Summary

Obtains a summary of drag data, including data type and size information. In a delayed drag scenario, only data type information can be obtained.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Summary](#summary10) | Summary of drag data. |

#### \[h2\]setResult10+

setResult(dragResult: DragResult): void

Sets the drag result in **DragEvent**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dragResult | [DragResult](#dragresult10) | Yes | Drag result. |

#### \[h2\]getResult10+

getResult(): DragResult

Obtains the drag result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DragResult](#dragresult10) | Drag result. |

#### \[h2\]getPreviewRect10+

getPreviewRect(): Rectangle

Obtains the position of the drag preview relative to the current window and the preview size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Rectangle](../../../universal-attributes/interaction-properties/touch-interactions/touch-target/document.md#rectangle) | Position of the drag preview relative to the current window and the preview size, in vp. x and y indicate the window coordinates of the upper left corner of the preview, and width and height indicate the preview size. |

#### \[h2\]getVelocityX10+

getVelocityX(): number

Obtains the dragging velocity along the x-axis.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Dragging velocity along the x-axis. The origin of the coordinate axis is the upper left corner of the screen. The unit is vp. The velocity is positive if the movement is from left to right, and it is negative if the movement is from right to left. |

#### \[h2\]getVelocityY10+

getVelocityY(): number

Obtains the dragging velocity along the y-axis.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Dragging velocity along the y-axis. The origin of the coordinate axis is the upper left corner of the screen. The unit is vp. The velocity is positive if the movement is from top to bottom, and it is negative if the movement is from bottom to top. |

#### \[h2\]getVelocity10+

getVelocity(): number

Obtains the dragging velocity along the main axis.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Dragging velocity along the main axis. The value is the arithmetic square root of the sum of the squares of the velocities along the x-axis and y-axis, in vp. |

#### \[h2\]getWindowX10+

getWindowX(): number

Obtains the x-coordinate of the drag point relative to the upper left corner of the window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | X coordinate of the drag point relative to the upper left corner of the window, in vp. |

#### \[h2\]getWindowY10+

getWindowY(): number

Obtains the y-coordinate of the drag point relative to the upper left corner of the window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Y-coordinate of the drag point relative to the upper left corner of the window, in vp. |

#### \[h2\]getDisplayX10+

getDisplayX(): number

Obtains the x-coordinate of the drag point relative to the upper left corner of the screen.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | X-coordinate of the drag point relative to the upper left corner of the screen, in vp. |

#### \[h2\]getDisplayY10+

getDisplayY(): number

Obtains the y-coordinate of the drag point relative to the upper left corner of the screen.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Y-coordinate of the drag point relative to the upper left corner of the screen, in vp. |

#### \[h2\]getModifierKeyState12+

getModifierKeyState?(keys: Array<string>): boolean

Obtains the pressed status of modifier keys.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | Array<string> | Yes | 
Obtains the pressed status of modifier keys. For details about the error message, see the following error codes. The following modifier keys are supported: 'Ctrl' | 'Alt' | 'Shift'.

**NOTE**

This API is not supported in stylus scenarios.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the specified modifier keys are pressed. Returns **true** if the specified modifier keys are pressed; returns **false** otherwise. |

#### \[h2\]startDataLoading15+

startDataLoading(options: DataSyncOptions): string

Asynchronously obtains drag data and notifies you of the current data synchronization progress. This API is only supported in the **onDrop** callback.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DataSyncOptions](#datasyncoptions15) | Yes | Parameters for obtaining drag data, including the target path, file conflict options, and progress bar type. You can use the [cancelDataLoading](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#canceldataloading15) API to cancel data loading during data transmission. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Drag Event Error Codes](../../../../error-codes/ui/drag-event-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 190003 | Operation not allowed for current phase. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Identifier for the drag data. It is used to distinguish between different drag operations. |

#### \[h2\]executeDropAnimation18+

executeDropAnimation(customDropAnimation: Callback<void>): void

Sets the execution function of the custom drop animation. This parameter is valid only when [useCustomDropAnimation](#properties) is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| customDropAnimation | [Callback<void>](../../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback) | Yes | 
Custom drop animation in this callback.

**NOTE**

1\. This API is valid only in the **onDrop** callback.

2\. Before using this API, set **useCustomDropAnimation** to **true**. Otherwise, this API does not take effect.

3\. Do not implement logic unrelated to the animation in the animation callback to avoid affecting performance.

 |

#### \[h2\]getDisplayId20+

getDisplayId(): number

Obtains the ID of the screen where the current drag event occurs. This API is not supported in the [onDragEnd](#ondragend10) callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | ID of the screen where the current drag event occurs. |

#### \[h2\]getDragSource20+

getDragSource(): string

Obtains the package name of the drag source application.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | Package name of the drag source application. |

#### \[h2\]isRemote20+

isRemote(): boolean

Checks whether the drag operation is cross-device.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the drag operation is cross-device. Returns **true** for cross-device drag operations; returns **false** otherwise. |

#### \[h2\]setDataLoadParams20+

setDataLoadParams(dataLoadParams: DataLoadParams): void

Sets the parameters for deferred data loading from the drag source. This API provides data loading parameters to the system instead of directly providing complete data objects. When the user drops data on the target application, the system will use these parameters to request the actual data from the drag source. If this API is used together with [setData](#setdata10), the last called API takes precedence. This API takes effect only in the [onDragStart](#ondragstart) callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataLoadParams | [DataLoadParams](#dataloadparams20) | Yes | Data loading parameters used during a drop operation. |

#### \[h2\]getX(deprecated)

getX(): number

Obtains the x-coordinate of the drag point relative to the upper left corner of the window, in vp.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3CACuWbCRPOwKJ2jFdTFew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B5B6EFA57E1ABD63D1567FF1CC1FA10E5E743A2EF14F4792235338D2D8AE513)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [getWindowX](#getwindowx10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
X-coordinate of the drag point relative to the upper left corner of the window.

Unit: vp.

 |

#### \[h2\]getY(deprecated)

getY(): number

Obtains the y-coordinate of the drag point relative to the upper left corner of the window, in vp.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Gq3ngzz_RcSxMwAlnPHsQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0E3D79D25D3A149720BA770572D9D73992F49806DB77AAD3A9F41BD36777855)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [getWindowY](#getwindowy10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Y-coordinate of the drag point relative to the upper left corner of the window.

Unit: vp.

 |

#### \[h2\]getGlobalDisplayX20+

getGlobalDisplayX(): number

Obtains the x-coordinate of the drag point relative to the upper left corner of the global screen.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
X-coordinate of the drag point relative to the upper left corner of the global screen.

Unit: vp. Value range: \[0, +∞)

 |

#### \[h2\]getGlobalDisplayY20+

getGlobalDisplayY(): number

Obtains the y-coordinate of the drag point relative to the upper left corner of the global screen.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Y-coordinate of the drag point relative to the upper left corner of the global screen.

Unit: vp. Value range: \[0, +∞)

 |

#### DragResult10+

Defines the result of a drag operation and the drop-selection state of a component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DRAG\_SUCCESSFUL | 0 | The drag is successful. This value applies to [onDrop](#ondrop). |
| DRAG\_FAILED | 1 | The drag fails. This value applies to [onDrop](#ondrop). |
| DRAG\_CANCELED | 2 | The drag is canceled. This value applies to [onDrop](#ondrop). |
| DROP\_ENABLED | 3 | The component allows dropping. This value applies to [onDragEnter](#ondragenter), [onDragMove](#ondragmove), and [onDragLeave](#ondragleave). |
| DROP\_DISABLED | 4 | The component does not allow dropping. This value applies to [onDragEnter](#ondragenter), [onDragMove](#ondragmove), and [onDragLeave](#ondragleave). |

#### DragBehavior10+

Describes the drag behavior. When [DragResult](#dragresult10) is set to **DROP\_ENABLED**, you can define **DragBehavior** as either **COPY** or **MOVE**. When **DragBehavior** is set to **COPY**, a plus sign will be displayed in the badge of the dragged object. When **DragBehavior** is set to **MOVE**, the plus sign will not be displayed. **DragBehavior** is used to indicate the intended way of handling data (either copy or move) without governing the actual data processing. This behavior is reported back to the drag source through **onDragEnd**, enabling the drag initiator to distinguish whether the operation results in a copy or a move of the data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| COPY | 0 | The data is handled as a copy operation. |
| MOVE | 1 | The data is handled as a move operation, effectively cutting it from its original location. |

#### PreDragStatus12+

Defines the states before the drag gesture is triggered.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTION\_DETECTING\_STATUS | 0 | 
A drag gesture is being detected. (Triggered when the component is long pressed for 50 ms.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| READY\_TO\_TRIGGER\_DRAG\_ACTION | 1 | 

The component is ready to be dragged. (Triggered when the component is long pressed for 500 ms.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PREVIEW\_LIFT\_STARTED | 2 | 

A lift animation is started. (Triggered when the component is long pressed for 800 ms.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PREVIEW\_LIFT\_FINISHED | 3 | 

A lift animation is finished. (Triggered at the completion of the lift animation.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PREVIEW\_LANDING\_STARTED | 4 | 

A drop animation is started. (Triggered when the drop animation starts.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PREVIEW\_LANDING\_FINISHED | 5 | 

A drop animation is finished. (Triggered when the drop animation ends.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ACTION\_CANCELED\_BEFORE\_DRAG | 6 | 

A drop animation is terminated. (Triggered when the finger is lifted off the screen after the component enters the **READY\_TO\_TRIGGER\_DRAG\_ACTION** state.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PREPARING\_FOR\_DRAG\_DETECTION18+ | 7 | 

The component is ready to be dragged. (Triggered when the component is long pressed for 350 ms.)

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### UnifiedData10+

type UnifiedData = UnifiedData

Defines drag-related data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [UnifiedData](../../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddata) | Drag-related data. |

#### Summary10+

type Summary = Summary

Provides a summary of drag-related data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Summary](../../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#summary) | Summary of drag-related data. |

#### DataLoadParams20+

type DataLoadParams = DataLoadParams

Defines the data loading parameters used during a drop operation.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [DataLoadParams](../../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#dataloadparams20) | Data loading parameters used during a drop operation. |

#### DataSyncOptions15+

type DataSyncOptions = GetDataParams

Defines the input parameter object for **startDataLoading**.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [GetDataParams](../../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#getdataparams15) | Represents the parameters for obtaining data from [UDMF](../../../../../arkdata/c-apis/modules/udmf/document.md), including the destination directory, option for resolving file conflicts, and progress indicator type. |

#### OnDragEventCallback15+

type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void

Defines a callback for drag events.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [DragEvent](#dragevent7) | Yes | **event**: drag event information, including the coordinates of the drag point. |
| extraParams | string | No | **extraParams**: additional information about the drag event. Its value must be parsed into JSON format. For details, see [extraParams](#extraparams). |

#### DropOptions15+

Sets parameters for the drop process.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| disableDataPrefetch | boolean | No | Yes | 
Whether to disable data prefetching for the drag-and-drop operation. The value **true** means to disable data prefetching for the drag-and-drop operation, and **false** means the opposite. Default value: **false**.

**NOTE**

Set this parameter to **true** when using [startDataLoading](#startdataloading15) to enable data prefetching.

 |

#### DragSpringLoadingConfiguration20+

type DragSpringLoadingConfiguration = DragSpringLoadingConfiguration

Defines the configuration parameters for drag hover detection.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [DragSpringLoadingConfiguration](../../../../arkts-api/ui/ohos-arkui-dragcontroller-dragcontroller/document.md#dragspringloadingconfiguration20) | Defines the configuration parameters for drag hover detection. |

#### SpringLoadingContext20+

type SpringLoadingContext = SpringLoadingContext

Defines callback context information, which is passed to the application in the hover detection callback to allow the application to access the drag status.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [SpringLoadingContext](../../../../arkts-api/ui/ohos-arkui-dragcontroller-dragcontroller/document.md#springloadingcontext20) | Callback context information, which is passed to the application in the hover detection callback to allow the application to access the drag status. |

#### Example

## Example 1: Setting Draggable and Droppable Areas

This example demonstrates how to set draggable and droppable areas for certain components, such as **Image** and **Text**.

// xxx.ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State targetImage: string = '';
  @State targetText: string = 'Drag Text';
  @State imageWidth: number = 100;
  @State imageHeight: number = 100;
  @State imgState: Visibility = Visibility.Visible;
  @State abstractContent: string = "abstract";
  @State textContent: string = "";
  @State backGroundColor: Color = Color.Transparent;

  @Builder
  pixelMapBuilder() {
    Column() {
      // Replace $r('app.media.icon') with the image resource file you use.
      Image($r('app.media.icon'))
        .width(120)
        .height(120)
        .backgroundColor(Color.Yellow)
    }
  }

  // Obtain UDMF data.
  getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
    try {
      let data: UnifiedData = event.getData();
      if (!data) {
        return false;
      }
      let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
      if (!records || records.length <= 0) {
        return false;
      }
      callback(event);
      return true;
    } catch (e) {
      console.error(\`getData failed, code = ${(e as BusinessError).code}, message = ${(e as BusinessError).message}\`);
      return false;
    }
  }

  // Automatically retry after the first failure to obtain UDMF data.
  getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
    if (this.getDataFromUdmfRetry(event, callback)) {
      return;
    }
    setTimeout(() => {
      this.getDataFromUdmfRetry(event, callback);
    }, 1500);
  }

  // Change the background color based on the state before drag.
  private PreDragChange(preDragStatus: PreDragStatus): void {
    if (preDragStatus == PreDragStatus.READY\_TO\_TRIGGER\_DRAG\_ACTION) {
      this.backGroundColor = Color.Red;
    } else if (preDragStatus == PreDragStatus.ACTION\_CANCELED\_BEFORE\_DRAG
      || preDragStatus == PreDragStatus.PREVIEW\_LANDING\_FINISHED) {
      this.backGroundColor = Color.Blue;
    }
  }

  build() {
    Row() {
      Column() {
        Text('start Drag')
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        // Replace $r('app.media.icon') with the image resource file you use.
        Image($r('app.media.icon'))
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .visibility(this.imgState)
          .onDragEnd((event) => {
            // The result value obtained from onDragEnd is set in onDrop of the drop target.
            if (event.getResult() === DragResult.DRAG\_SUCCESSFUL) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
            } else if (event.getResult() === DragResult.DRAG\_FAILED) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
            }
          })
        Text('test drag event')
          .width('100%')
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .copyOption(CopyOptions.InApp)
        TextArea({ placeholder: 'please input words' })
          .copyOption(CopyOptions.InApp)
          .width('100%')
          .height(50)
          .draggable(true)
        Search({ placeholder: 'please input you word' })
          .searchButton('Search')
          .width('100%')
          .height(80)
          .textFont({ size: 20 })

        Column() {
          Text('this is abstract')
            .fontSize(20)
            .width('100%')
        }
        .margin({ left: 40, top: 20 })
        .width('100%')
        .height(100)
        .onDragStart((event) => {
          this.backGroundColor = Color.Transparent;
          let data: unifiedDataChannel.PlainText = new unifiedDataChannel.PlainText();
          data.abstract = 'this is abstract';
          data.textContent = 'this is content this is content';
          (event as DragEvent).setData(new unifiedDataChannel.UnifiedData(data));
        })
        .onPreDrag((status: PreDragStatus) => {
          this.PreDragChange(status);
        })
        .backgroundColor(this.backGroundColor)
      }.width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        Image(this.targetImage)
          .width(this.imageWidth)
          .height(this.imageHeight)
          .draggable(true)
          .margin({ left: 15 })
          .border({ color: Color.Black, width: 1 })
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.IMAGE\])
          .onDrop((dragEvent?: DragEvent) => {
            this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
              let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
              let rect: Rectangle = event.getPreviewRect();
              this.imageWidth = Number(rect.width);
              this.imageHeight = Number(rect.height);
              this.targetImage = (records\[0\] as unifiedDataChannel.Image).imageUri;
              event.useCustomDropAnimation = false;
              this.imgState = Visibility.None;
              // If result is explicitly set to successful, the value is passed in to onDragEnd of the drag source.
              event.setResult(DragResult.DRAG\_SUCCESSFUL);
            })
          })

        Text(this.targetText)
          .width('100%')
          .height(100)
          .border({ color: Color.Black, width: 1 })
          .margin(15)
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.PLAIN\_TEXT\])
          .onDrop((dragEvent?: DragEvent) => {
            this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
              let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
              let plainText: unifiedDataChannel.PlainText = records\[0\] as unifiedDataChannel.PlainText;
              this.targetText = plainText.textContent;
            })
          })

        Column() {
          Text(this.abstractContent).fontSize(20).width('100%')
          Text(this.textContent).fontSize(15).width('100%')
        }
        .width('100%')
        .height(100)
        .margin(20)
        .border({ color: Color.Black, width: 1 })
        .allowDrop(\[uniformTypeDescriptor.UniformDataType.PLAIN\_TEXT\])
        .onDrop((dragEvent?: DragEvent) => {
          this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
            let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
            let plainText: unifiedDataChannel.PlainText = records\[0\] as unifiedDataChannel.PlainText;
            this.abstractContent = plainText.abstract as string;
            this.textContent = plainText.textContent;
          })
        })
      }.width('45%')
      .height('100%')
      .margin({ left: '5%' })
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/rmxvPpFUTS2xJrOje5xJxw/en-us_image_0000002537925318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12A3E79DE8D3BFB421D0B26CABD48819C3656A7A6ED0E3B7C89AE609267F7095)

## Example 2: Implementing a Custom Drop Animation

In API version 18 and later versions, this example demonstrates how to implement a drop animation by using the custom API [executeDropAnimation](#executedropanimation18).

import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct DropAnimationExample {
  @State targetImage: string = '';
  @State imageWidth: number = 100;
  @State imageHeight: number = 100;
  @State imgState: Visibility = Visibility.Visible;
  customDropAnimation =
    () => {
      this.getUIContext().animateTo({ duration: 1000, curve: Curve.EaseOut, playMode: PlayMode.Normal }, () => {
        this.imageWidth = 200;
        this.imageHeight = 200;
        this.imgState = Visibility.None;
      })
    }

  build() {
    Row() {
      Column() {
        // Replace $r('app.media.app\_icon') with the image resource file you use.
        Image($r('app.media.app\_icon'))
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15, top: 40 })
          .visibility(this.imgState)
          .onDragStart((event) => {
          })
          .onDragEnd((event) => {
            if (event.getResult() === DragResult.DRAG\_SUCCESSFUL) {
              console.info('Drag Success');
            } else if (event.getResult() === DragResult.DRAG\_FAILED) {
              console.error('Drag failed');
            }
          })
      }.width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width(180)
          .height(40)
          .textAlign(TextAlign.Center)
          .margin(10)
          .backgroundColor('rgb(240,250,255)')
        Column() {
          Image(this.targetImage)
            .width(this.imageWidth)
            .height(this.imageHeight)
        }
        .draggable(true)
        .margin({ left: 15 })
        .border({ color: Color.Black, width: 1 })
        .allowDrop(\[uniformTypeDescriptor.UniformDataType.IMAGE\])
        // onDrop callback, which is used to obtain the information (size included) of the dragged image, update the display, and enable and execute the custom drop animation.
        .onDrop((dragEvent: DragEvent) => {
          let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
          let rect: Rectangle = dragEvent.getPreviewRect();
          this.imageWidth = Number(rect.width);
          this.imageHeight = Number(rect.height);
          this.targetImage = (records\[0\] as unifiedDataChannel.Image).imageUri;
          dragEvent.useCustomDropAnimation = true;
          dragEvent.executeDropAnimation(this.customDropAnimation)
        })
        .width(this.imageWidth)
        .height(this.imageHeight)
      }.width('45%')
      .height('100%')
      .margin({ left: '5%' })
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/733MREMNSAagg46ZmxBRPg/en-us_image_0000002568685095.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4593DEB2AC2DE5074FCF20D179087B2A4597BE9AB24053D49C9907605B27453)

## Example 3: Obtaining Data Asynchronously Through Drag-and-Drop

In API version 15 and later versions, this example shows how to obtain data asynchronously through drag-and-drop by using the [startDataLoading](#startdataloading15) API.

import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { fileUri, fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct ImageExample {
  @State uri: string = "";
  @State blockArr: string\[\] = \[\];
  uiContext = this.getUIContext();
  udKey: string = '';

  build() {
    Column() {
      Text('Image drag and drop')
        .fontSize('30dp')
      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
        // Replace $r('app.media.startIcon') with the image resource file you use.
        Image($r('app.media.startIcon'))
          .width(100)
          .height(100)
          .border({ width: 1 })
          .draggable(true)
          .onDragStart((event: DragEvent) => {
            const context: Context | undefined = this.uiContext.getHostContext();
            if (context) {
              let data = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id, 120);
              const arrayBuffer: ArrayBuffer = data.buffer.slice(data.byteOffset, data.byteLength + data.byteOffset);
              let filePath = context.filesDir + '/test.png';
              let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
              fs.writeSync(file.fd, arrayBuffer);
              // Obtain the image URI.
              let uri = fileUri.getUriFromPath(filePath);
              let image: unifiedDataChannel.Image = new unifiedDataChannel.Image();
              image.imageUri = uri;
              let dragData: unifiedDataChannel.UnifiedData = new unifiedDataChannel.UnifiedData(image);
              (event as DragEvent).setData(dragData);
            }
          })
      }
      .margin({ bottom: 20 })

      Row() {
        Column() {
          Text('Valid drop target')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.blockArr, (item: string, index) => {
              ListItem() {
                Image(item)
                  .width(100)
                  .height(100)
                  .border({ width: 1 })
              }
              .margin({ left: 30, top: 30 })
            }, (item: string) => item)
          }
          .border({ width: 1 })
          .height('90%')
          .width('100%')
          .onDrop((event?: DragEvent, extraParams?: string) => {
            console.info("enter onDrop")
            let context = this.uiContext.getHostContext() as common.UIAbilityContext;
            let pathDir: string = context.distributedFilesDir;
            let destUri = fileUri.getUriFromPath(pathDir);
            // Create DataProgressListener to monitor the data transfer progress.
            let progressListener: unifiedDataChannel.DataProgressListener =
              (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
                if (dragData != null) {
                  // Obtain the data array.
                  let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
                  if (arr.length > 0) {
                    // Check whether the first record is of the IMAGE type.
                    if (arr\[0\].getType() === uniformTypeDescriptor.UniformDataType.IMAGE) {
                      // If the type matches, record the URI.
                      let image = arr\[0\] as unifiedDataChannel.Image;
                      this.uri = image.imageUri;
                      this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
                    }
                  } else {
                    console.info('dragData arr is null');
                  }
                } else {
                  console.info('dragData is undefined');
                }
                console.info(\`percentage: ${progress.progress}\`);
              };
            // Set the asynchronous data loading parameters.
            let options: DataSyncOptions = {
              destUri: destUri,
              fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
              progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
              dataProgressListener: progressListener,
            }
            try {
              // Start data transfer.
              this.udKey = (event as DragEvent).startDataLoading(options);
              console.info(\`udKey: ${this.udKey}\`);
            } catch (e) {
              console.error(\`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}\`);
            }
          }, { disableDataPrefetch: true })
        }
        .height("50%")
        .width("90%")
        .border({ width: 1 })
      }

      Button('Cancel data transfer')
        .onClick(() => {
          try {
            this.getUIContext().getDragController().cancelDataLoading(this.udKey);
          } catch (e) {
            console.error(\`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}\`);
          }
        })
        .margin({ top: 10 })
    }.width('100%')
  }
}

## Example 4: Obtaining the Screen ID for the Drag Event

In API version 20 and later versions, this example shows how to obtain the drag event by calling the **onDragXXX** (not **onDragEnd**) API and obtain the screen ID by calling the [getDisplayId](#getdisplayid20) API in the drag event.

import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State targetImage: string = '';
  @State imageWidth: number = 100;
  @State imageHeight: number = 100;
  @State imgState: Visibility = Visibility.Visible;
  @State backGroundColor: Color = Color.Transparent;
  @State startDisplayId: number = -1;
  @State enterDisplayId: number = -1;
  @State moveDisplayId: number = -1;
  @State leaveDisplayId: number = -1;
  @State dropDisplayId: number = -1;

  @Builder
  pixelMapBuilder() {
    Column() {
      // Replace $r('app.media.app\_icon') with the image resource file you use.
      Image($r('app.media.app\_icon'))
        .width(120)
        .height(120)
        .backgroundColor(Color.Yellow)
    }
  }

  getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
    try {
      let data: UnifiedData = event.getData();
      if (!data) {
        return false;
      }
      let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
      if (!records || records.length <= 0) {
        return false;
      }
      callback(event);
      return true;
    } catch (e) {
      console.error(\`getData failed, code = ${(e as BusinessError).code}, message = ${(e as BusinessError).message}\`);
      return false;
    }
  }

  getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
    if (this.getDataFromUdmfRetry(event, callback)) {
      return;
    }
    setTimeout(() => {
      this.getDataFromUdmfRetry(event, callback);
    }, 1500);
  }

  private PreDragChange(preDragStatus: PreDragStatus): void {
    if (preDragStatus == PreDragStatus.READY\_TO\_TRIGGER\_DRAG\_ACTION) {
      this.backGroundColor = Color.Red;
    } else if (preDragStatus == PreDragStatus.ACTION\_CANCELED\_BEFORE\_DRAG
      || preDragStatus == PreDragStatus.PREVIEW\_LANDING\_FINISHED) {
      this.backGroundColor = Color.Blue;
    }
  }

  build() {
    Row() {
      Column() {
        Text('start Drag')
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        // Replace $r('app.media.startIcon') with the image resource file you use.
        Image($r('app.media.startIcon'))
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .visibility(this.imgState)
          .onDragStart((event) => {
            let id = event.getDisplayId();
            this.startDisplayId = id;
          })

          .onDragEnd((event) => {
            if (event.getResult() === DragResult.DRAG\_SUCCESSFUL) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
            } else if (event.getResult() === DragResult.DRAG\_FAILED) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
            }
          })

        Text('displayID in onDragStart: ' + this.startDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDragEnter: ' + this.enterDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDragMove: ' + this.moveDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDragLeave: ' + this.leaveDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDrop: ' + this.dropDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
          .onPreDrag((status: PreDragStatus) => {
            this.PreDragChange(status);
          })
      }.width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        Image(this.targetImage)
          .width(this.imageWidth)
          .height(this.imageHeight)
          .draggable(true)
          .margin({ left: 15 })
          .border({ color: Color.Black, width: 1 })
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.IMAGE\])
          .onDragEnter((event) => {
            let id = event.getDisplayId();
            this.enterDisplayId = id;
          })
          .onDragMove((event) => {
            let id = event.getDisplayId();
            this.moveDisplayId = id;
          })
          .onDragLeave((event) => {
            let id = event.getDisplayId();
            this.leaveDisplayId = id;
          })
          .onDrop((dragEvent: DragEvent) => {
            let id = dragEvent.getDisplayId();
            this.dropDisplayId = id;
            this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
              let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
              let rect: Rectangle = event.getPreviewRect();
              this.imageWidth = Number(rect.width);
              this.imageHeight = Number(rect.height);
              this.targetImage = (records\[0\] as unifiedDataChannel.Image).imageUri;
              event.useCustomDropAnimation = false;
              this.imgState = Visibility.None;
              event.setResult(DragResult.DRAG\_SUCCESSFUL);
            })
          })
      }.width('45%')
      .height('100%')
      .margin({ left: '5%' })
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Ax7s-SfGSRqsydNSVSKhxQ/en-us_image_0000002568765105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76942C11C0B59CFB98AD9E206BDFE0DEC160FA565A425E954D196EC20BA51385)

## Example 5: Obtaining the Package Name and Cross-Device Status

In API version 20 and later versions, this example shows how to obtain the drag event by calling the **onDragXXX** API, obtain the package name by calling the [getDragSource](#getdragsource20) API in the drag event, and obtain the cross-device status by calling the **isRemote** API.

@Entry
@Component
struct Index {
  @State targetImage: string = '';
  @State startDragSource: string = '';
  @State startIsRemote: boolean = true;
  @State enterDragSource: string = '';
  @State enterIsRemote: boolean = true;

  build() {
    Column() {
      Row() {
        Column() {
          Text('start Drag Area')
            .fontSize(18)
            .width('100%')
            .height(40)
            .margin(10)
            .backgroundColor('#008888')
          // Replace $r('app.media.startIcon') with the image resource file you use.
          Image($r('app.media.startIcon'))
            .onDragStart((event) => {
              this.startDragSource = (event as DragEvent).getDragSource();
              this.startIsRemote = (event as DragEvent).isRemote();
            })
            .width(100)
            .height(100)
            .draggable(true)
            .margin({ left: 15 })
        }
        .border({ color: Color.Black, width: 1 })
        .width('45%')
        .height('50%')

        Column() {
          Text('Drag Target Area')
            .fontSize(20)
            .width('100%')
            .height(40)
            .margin(10)
            .backgroundColor('#008888')
          Image(this.targetImage)
            .width(100)
            .height(100)
            .draggable(true)
            .margin({ left: 15 })
            .border({ color: Color.Black, width: 1 })
            .onDragEnter((event) => {
              this.enterDragSource = (event as DragEvent).getDragSource();
              this.enterIsRemote = (event as DragEvent).isRemote();
            })
            .onDrop(() => {
            })
        }
        .border({ color: Color.Black, width: 1 })
        .width('45%')
        .height('50%')
        .margin({ left: '5%' })
      }
      .height('70%')

      Text('onDragStart dragSource: ' + this.startDragSource.toString() + '\\n' + 'onDragStart isRemote: ' +
      this.startIsRemote.toString())
        .width('100%')
        .height(50)
        .margin({ left: 15 })
      Text('onDragEnter dragSource: ' + this.enterDragSource.toString() + '\\n' + 'onDragEnter isRemote: ' +
      this.enterIsRemote.toString())
        .width('100%')
        .height(50)
        .margin({ left: 15 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/AHRycksaRcOVViaDx_Npow/en-us_image_0000002537765380.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAE30981F17DE8E320638790812664E729CF7D7105F76D32ED469773182B4306)

## Example 6: Implementing Hover Detection Support

In API version 20 and later versions, this example demonstrates how to register a callback by calling the [onDragSpringLoading](#ondragspringloading20) API and obtain the context (current status and notification sequence) by calling the [SpringLoadingContext](#springloadingcontext20) API.

// xxx.ets
@Entry
@Component
struct Index {
  @State targetText: string = 'Drag Text';
  @State state: number = 0;
  @State currentNotifySequence: number = 0;
  @State config: DragSpringLoadingConfiguration = {
    stillTimeLimit: 200,
    updateInterval: 300,
    updateNotifyCount: 4,
    updateToFinishInterval: 300
  };

  build() {
    Row() {
      Column() {
        Text('start Drag')
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        // Replace $r('app.media.startIcon') with the image resource file you use.
        Image($r('app.media.startIcon'))
          .id("ori\_image")
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
        Text('Current state: ' + this.state)
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
        Text('Current notification sequence: ' + this.currentNotifySequence)
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
      }
      .width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
          .id("text")
        Image("")
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .border({ color: Color.Black, width: 2 })
          .onDragSpringLoading((context: SpringLoadingContext) => {
            this.state = context.state;
            this.currentNotifySequence = context.currentNotifySequence;
          }, this.config)
      }
      .width('45%')
      .height('100%')
      .margin({ left: '5%' })
      .onDragSpringLoading((context: SpringLoadingContext) => {
        this.state = context.state;
        this.currentNotifySequence = context.currentNotifySequence;
      }, this.config)
      .id("column")
      .backgroundColor(Color.Grey)
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/SuocYGuuTR6eINOkJ_xjpQ/en-us_image_0000002537925320.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC3F74FECEDF1FC2AAA7A288418080B20E479CB053D26D91A7C0387DB62343C1)

## Example 7: Delaying Data Provision from the Drag Source

In API version 20 and later versions, this example shows how to call [setDataLoadParams](#setdataloadparams20) in [onDragStart](#ondragstart) to delay data provision and call [startDataLoading](#startdataloading15) in [onDrop](#ondrop) to asynchronously obtain data.

import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { fileUri, fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct VideoExample {
  @State uri: string = "";
  @State blockArr: string\[\] = \[\];
  uiContext = this.getUIContext();
  udKey: string = '';

  build() {
    Column() {
      Text('Video drag and drop')
        .fontSize('30dp')
      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
        // Replace \*\*$rawfile('test1.mp4')\*\* with the resource file you use.
        Video({ src: $rawfile('test1.mp4'), controller: new VideoController() })
          .width(200)
          .height(200)
          .border({ width: 1 })
          .draggable(true)
          .onDragStart((event: DragEvent) => {
            const context: Context | undefined = this.uiContext.getHostContext();
            if (context) {
              let loadHandler: unifiedDataChannel.DataLoadHandler = (acceptableInfo) => {
                console.info(\`acceptableInfo recordCount ${acceptableInfo?.recordCount}\`);
                if (acceptableInfo?.types) {
                  console.info(\`acceptableInfo types ${Array.from(acceptableInfo.types)}\`);
                } else {
                  console.error('acceptableInfo types is undefined');
                }
                let data = context.resourceManager.getRawFdSync('test1.mp4');
                let filePath = context.filesDir + '/test1.mp4';
                let file: fs.File = null!;
                try {
                  file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
                  let bufferSize = data.length as number;
                  let buf = new ArrayBuffer(bufferSize);
                  fs.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
                  fs.writeSync(file.fd, buf, { offset: 0, length: bufferSize });
                } catch (error) {
                  console.error(\`openSync errorCode: ${error.code}, errorMessage: ${error.message}\`);
                } finally {
                  fs.closeSync(file.fd);
                }
                context.resourceManager.closeRawFdSync('test1.mp4')
                this.uri = fileUri.getUriFromPath(filePath);
                let videoMp: uniformDataStruct.FileUri = {
                  uniformDataType: 'general.file-uri',
                  oriUri: this.uri,
                  fileType: 'general.video',
                }
                let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
                let unifiedData = new unifiedDataChannel.UnifiedData();
                unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.FILE\_URI, videoMp);
                unifiedData.addRecord(unifiedRecord);
                return unifiedData;
              }
              (event as DragEvent).setDataLoadParams({
                loadHandler: loadHandler,
                dataLoadInfo: { types: new Set(\[uniformTypeDescriptor.UniformDataType.FILE\_URI\]), recordCount: 1 }
              });
            }
          })
      }
      .margin({ bottom: 20 })

      Row() {
        Column() {
          Text('Valid drop target')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.blockArr, (item: string, index) => {
              ListItem() {
                Video({ src: item, controller: new VideoController() })
                  .width(100)
                  .height(100)
                  .border({ width: 1 })
              }
              .margin({ left: 30, top: 30 })
            }, (item: string) => item)
          }
          .border({ width: 1 })
          .height('90%')
          .width('100%')
          .onDrop((event: DragEvent, extraParams?: string) => {
            let context = this.uiContext.getHostContext() as common.UIAbilityContext;
            let pathDir: string = context.distributedFilesDir;
            let destUri = fileUri.getUriFromPath(pathDir);
            let progressListener: unifiedDataChannel.DataProgressListener =
              (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
                if (dragData != null) {
                  let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
                  if (arr.length > 0) {
                    if (arr\[0\].getType() === uniformTypeDescriptor.UniformDataType.VIDEO) {
                      this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
                    }
                  } else {
                    console.info('dragData arr is null');
                  }
                } else {
                  console.info('dragData is undefined');
                }
                console.info(\`percentage: ${progress.progress}\`);
              };
            let info: unifiedDataChannel.DataLoadInfo =
              { types: new Set(\[uniformTypeDescriptor.UniformDataType.VIDEO\]), recordCount: 100 }
            let options: DataSyncOptions = {
              destUri: destUri,
              fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
              progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
              dataProgressListener: progressListener,
              acceptableInfo: info,
            }
            try {
              this.udKey = (event as DragEvent).startDataLoading(options);
              console.info(\`udKey: ${this.udKey}\`);
            } catch (e) {
              console.error(\`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}\`);
            }
          }, { disableDataPrefetch: true })
        }
        .height("50%")
        .width("90%")
        .border({ width: 1 })
      }

      Button('Cancel Data Transfer')
        .onClick(() => {
          try {
            this.getUIContext().getDragController().cancelDataLoading(this.udKey);
          } catch (e) {
            console.error(\`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}\`);
          }
        })
        .margin({ top: 10 })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/e6PlW5LSRHGWzYDcdMLHQg/en-us_image_0000002568685097.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE2D4A6B8FF0235DE62C771E6BD69CC4C2B296ADF30573209C4839480BC8EE33)
