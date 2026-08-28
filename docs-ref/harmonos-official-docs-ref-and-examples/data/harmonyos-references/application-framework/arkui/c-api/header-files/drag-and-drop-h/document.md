# drag\_and\_drop.h

#### Overview

Declares the APIs of **NativeDrag**.

**File to include**: <arkui/drag\_and\_drop.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [NativeDragDrop](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NativeDragDrop)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) | ArkUI\_NodeEvent | Defines a struct for a component event. |
| [ArkUI\_Context](../../structs/arkui-context/document.md) | ArkUI\_Context | Defines a struct for a native UI context object. |
| [ArkUI\_Context\*](../../structs/arkui-context--00020177/document.md) | ArkUI\_ContextHandle | Defines the handle to the native UI context. |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) | ArkUI\_DragEvent | Defines a struct for a drag event. |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md) | ArkUI\_DragPreviewOption | Defines a struct for custom drag preview options. |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md) | ArkUI\_DragAction | Defines a struct for a drag action. |
| [ArkUI\_DragAndDropInfo](../../structs/arkui-draganddropinfo/document.md) | ArkUI\_DragAndDropInfo | Defines a struct for drag and drop information returned through a drag status listener. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_DragResult](#arkui_dragresult) | ArkUI\_DragResult | Enumerates drag results, which are set by the data receiver and transferred by the system to the drag source so that the drag source is aware of the data processing result of the receiver. |
| [ArkUI\_DropOperation](#arkui_dropoperation) | ArkUI\_DropOperation | Enumerates data processing modes used when data is dropped, which affects the display of the badge. |
| [ArkUI\_PreDragStatus](#arkui_predragstatus) | ArkUI\_PreDragStatus | Enumerates interaction states prior to a drop and drop operation. |
| [ArkUI\_DragPreviewScaleMode](#arkui_dragpreviewscalemode) | ArkUI\_DragPreviewScaleMode | Enumerates drag preview scale modes. |
| [ArkUI\_DragStatus](#arkui_dragstatus) | ArkUI\_DragStatus | Enumerates drag operation states. |

#### \[h2\]Callback

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent\* OH\_ArkUI\_NodeEvent\_GetDragEvent(ArkUI\_NodeEvent\* nodeEvent)](#oh_arkui_nodeevent_getdragevent) | Obtains a **DragEvent** object from the specified **NodeEvent** object. |
| [ArkUI\_PreDragStatus OH\_ArkUI\_NodeEvent\_GetPreDragStatus(ArkUI\_NodeEvent\* nodeEvent)](#oh_arkui_nodeevent_getpredragstatus) | Obtains the state prior to a drop and drop operation. |
| [int32\_t OH\_ArkUI\_DragEvent\_DisableDefaultDropAnimation(ArkUI\_DragEvent\* event, bool disable)](#oh_arkui_dragevent_disabledefaultdropanimation) | Sets whether to disable the default drop animation, which is enabled by default. Use this API to apply a custom drop animation. |
| [int32\_t OH\_ArkUI\_DragEvent\_SetSuggestedDropOperation(ArkUI\_DragEvent\* event, ArkUI\_DropOperation dropOperation)](#oh_arkui_dragevent_setsuggesteddropoperation) | Sets the data processing mode. |
| [int32\_t OH\_ArkUI\_DragEvent\_SetDragResult(ArkUI\_DragEvent\* event, ArkUI\_DragResult result)](#oh_arkui_dragevent_setdragresult) | Sets the result for a drag event. |
| [int32\_t OH\_ArkUI\_DragEvent\_SetData(ArkUI\_DragEvent\* event, OH\_UdmfData\* data)](#oh_arkui_dragevent_setdata) | Set drag data for a drag event. |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_SetDataLoadParams(ArkUI\_DragEvent\* event, OH\_UdmfDataLoadParams\* dataLoadParams)](#oh_arkui_dragevent_setdataloadparams) | This API provides data loading parameters to the system instead of directly providing a complete data object. When the user drops data on the target application, the system will use **dataLoadParams** to request data. This can greatly improve the efficiency of dragging large amounts of data and the efficiency of processing dropped data in the target application. This API must always be used in preference to [OH\_ArkUI\_DragEvent\_SetData](#oh_arkui_dragevent_setdata). For details about how to create and prepare data loading parameters, see [OH\_UdmfDataLoadParams\_Create](../../../../arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfdataloadparams_create) in **udmf.h**. If this API conflicts with [OH\_ArkUI\_DragEvent\_SetData](#oh_arkui_dragevent_setdata), the system always uses the last called API. |
| [int32\_t OH\_ArkUI\_DragEvent\_GetUdmfData(ArkUI\_DragEvent\* event, OH\_UdmfData \*data)](#oh_arkui_dragevent_getudmfdata) | Obtains the default drag data from a drag event. |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDataTypeCount(ArkUI\_DragEvent\* event, int32\_t\* count)](#oh_arkui_dragevent_getdatatypecount) | Obtains the number of drag data types from a drag event. |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDataTypes(ArkUI\_DragEvent \*event, char \*eventTypeArray\[\], int32\_t length, int32\_t maxStrLen)](#oh_arkui_dragevent_getdatatypes) | Obtains the type list of drag data types from a drag event. |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDragResult(ArkUI\_DragEvent\* event, ArkUI\_DragResult\* result)](#oh_arkui_dragevent_getdragresult) | Obtains the drag and drop result from the drag event. |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDropOperation(ArkUI\_DragEvent\* event, ArkUI\_DropOperation\* operation)](#oh_arkui_dragevent_getdropoperation) | Obtains the data handling method from the drag event. |
| [float OH\_ArkUI\_DragEvent\_GetPreviewTouchPointX(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_getpreviewtouchpointx) | Obtains the x-coordinate of the touch point for a drag preview from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetPreviewTouchPointY(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_getpreviewtouchpointy) | Obtains the y-coordinate of the touch point on the preview image from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetPreviewRectWidth(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_getpreviewrectwidth) | Obtains the width of a drag preview from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetPreviewRectHeight(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_getpreviewrectheight) | Obtains the height of a drag preview from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointXToWindow(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_gettouchpointxtowindow) | Obtains the x-coordinate of the touch point relative to the window from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointYToWindow(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_gettouchpointytowindow) | Obtains the y-coordinate of the touch point relative to the window from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointXToDisplay(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_gettouchpointxtodisplay) | Obtains the x-coordinate of the touch point relative to the display from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointYToDisplay(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_gettouchpointytodisplay) | Obtains the y-coordinate of the touch point relative to the display from a drag event. |
| [float OH\_ArkUI\_DragEvent\_GetVelocityX(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_getvelocityx) | Obtains the dragging velocity along the x-axis. |
| [float OH\_ArkUI\_DragEvent\_GetVelocityY(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_getvelocityy) | Obtains the dragging velocity along the y-axis. |
| [float OH\_ArkUI\_DragEvent\_GetVelocity(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_getvelocity) | Obtains the dragging velocity along the main axis. |
| [int32\_t OH\_ArkUI\_DragEvent\_GetModifierKeyStates(ArkUI\_DragEvent\* event, uint64\_t\* keys)](#oh_arkui_dragevent_getmodifierkeystates) | Obtains the pressed status of modifier keys. |
| [int32\_t OH\_ArkUI\_DragEvent\_StartDataLoading(ArkUI\_DragEvent\* event, OH\_UdmfGetDataParams\* options, char\* key, unsigned int keyLen)](#oh_arkui_dragevent_startdataloading) | Starts data synchronization using the specified synchronization parameters. |
| [int32\_t OH\_ArkUI\_CancelDataLoading(ArkUI\_ContextHandle uiContext, const char\* key)](#oh_arkui_canceldataloading) | Cancels the ongoing data synchronization. |
| [int32\_t OH\_ArkUI\_DisableDropDataPrefetchOnNode(ArkUI\_NodeHandle node, bool disabled)](#oh_arkui_disabledropdataprefetchonnode) | Sets whether to disable the data prefetch process before executing [NODE\_ON\_DROP](../native-node-h/document.md#arkui_nodeeventtype). The system will retry data fetching until the maximum time limit (currently 2.4 seconds) is reached, which is useful for cross-device drag and drop operations as it helps stabilize system communication. However, this feature is redundant for the [OH\_ArkUI\_DragEvent\_StartDataLoading](#oh_arkui_dragevent_startdataloading) API. Since this API uses an asynchronous mechanism to fetch data, when [OH\_ArkUI\_DragEvent\_StartDataLoading](#oh_arkui_dragevent_startdataloading) is used in **NODE\_ON\_DROP**, this field must be set to **true** to prevent accidental data fetching before **NODE\_ON\_DROP** is executed. |
| [int32\_t OH\_ArkUI\_SetDragEventStrictReportWithNode(ArkUI\_NodeHandle node, bool enabled)](#oh_arkui_setdrageventstrictreportwithnode) | Sets whether to enable strict reporting on drag events. This feature is disabled by default, and you are advised to enable it. If this feature is disabled, the parent component is not notified when an item in it is dragged over its child component. If this feature is enabled, the component is notified of the dragged item's leaving, and the child component to which the dragged item is dropped is notified of the item's entering. This configuration is related to a specific UI instance. You can pass in a specific component node on the current UI instance for association. |
| [int32\_t OH\_ArkUI\_SetDragEventStrictReportWithContext(ArkUI\_ContextHandle uiContext, bool enabled)](#oh_arkui_setdrageventstrictreportwithcontext) | Sets whether to enable strict reporting on drag events. This feature is disabled by default, and you are advised to enable it. If this feature is disabled, the parent component is not notified when an item in it is dragged over its child component. If this feature is enabled, the component is notified of the dragged item's leaving, and the child component to which the dragged item is dropped is notified of the item's entering. This configuration is related to a specific UI instance. You can pass in a specific UI instance for association. |
| [int32\_t OH\_ArkUI\_SetNodeAllowedDropDataTypes(ArkUI\_NodeHandle node, const char\* typesArray\[\], int32\_t count)](#oh_arkui_setnodealloweddropdatatypes) | Sets the types of data that can be dropped to the specified component. This API resets the settings configured through [OH\_ArkUI\_DisallowNodeAnyDropDataTypes](#oh_arkui_disallownodeanydropdatatypes) or [OH\_ArkUI\_AllowNodeAllDropDataTypes](#oh_arkui_allownodealldropdatatypes). |
| [int32\_t OH\_ArkUI\_DisallowNodeAnyDropDataTypes(ArkUI\_NodeHandle node)](#oh_arkui_disallownodeanydropdatatypes) | Configures the specified component to disallow any data types. This API resets the settings configured through [OH\_ArkUI\_SetNodeAllowedDropDataTypes](#oh_arkui_setnodealloweddropdatatypes). |
| [int32\_t OH\_ArkUI\_AllowNodeAllDropDataTypes(ArkUI\_NodeHandle node)](#oh_arkui_allownodealldropdatatypes) | Configures the specified component to allow any data types. This API resets the settings configured through [OH\_ArkUI\_SetNodeAllowedDropDataTypes](#oh_arkui_setnodealloweddropdatatypes). |
| [int32\_t OH\_ArkUI\_SetNodeDraggable(ArkUI\_NodeHandle node, bool enabled)](#oh_arkui_setnodedraggable) | Sets whether the component is draggable. |
| [int32\_t OH\_ArkUI\_SetNodeDragPreview(ArkUI\_NodeHandle node, OH\_PixelmapNative\* preview)](#oh_arkui_setnodedragpreview) | Sets a custom drag preview for the specified component. |
| [ArkUI\_DragPreviewOption\* OH\_ArkUI\_CreateDragPreviewOption(void)](#oh_arkui_createdragpreviewoption) | Creates an **ArkUI\_DragPreviewOption** object. |
| [void OH\_ArkUI\_DragPreviewOption\_Dispose(ArkUI\_DragPreviewOption\* option)](#oh_arkui_dragpreviewoption_dispose) | Disposes of an **ArkUI\_DragPreviewOption** object. |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetScaleMode(ArkUI\_DragPreviewOption\* option, ArkUI\_DragPreviewScaleMode scaleMode)](#oh_arkui_dragpreviewoption_setscalemode) | Sets the scale mode for an **ArkUI\_DragPreviewOption** object. |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultShadowEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](#oh_arkui_dragpreviewoption_setdefaultshadowenabled) | Sets whether to enable the default shadow effect for an **ArkUI\_DragPreviewOption** object. The effect is disabled by default. |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultRadiusEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](#oh_arkui_dragpreviewoption_setdefaultradiusenabled) | Sets whether to enable the default rounded corner effect for an **ArkUI\_DragPreviewOption** object. The rounded corner radius is 12.0 vp by default. The effect is disabled by default. |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](#oh_arkui_dragpreviewoption_setnumberbadgeenabled) | Sets whether to enable the badge for an **ArkUI\_DragPreviewOption** object. If this feature is enabled, a badge that contains the number of dragged items is displayed. |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetBadgeNumber(ArkUI\_DragPreviewOption\* option, uint32\_t forcedNumber)](#oh_arkui_dragpreviewoption_setbadgenumber) | Sets the count on the badge. The settings will overwrite the value in [OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled](#oh_arkui_dragpreviewoption_setnumberbadgeenabled). |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultAnimationBeforeLiftingEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](#oh_arkui_dragpreviewoption_setdefaultanimationbeforeliftingenabled) | Sets whether to enable the default animation on a click or touch. |
| [int32\_t OH\_ArkUI\_SetNodeDragPreviewOption(ArkUI\_NodeHandle node, ArkUI\_DragPreviewOption\* option)](#oh_arkui_setnodedragpreviewoption) | Sets an **ArkUI\_DragPreviewOption** object for the specified component. |
| [ArkUI\_DragAction\* OH\_ArkUI\_CreateDragActionWithNode(ArkUI\_NodeHandle node)](#oh_arkui_createdragactionwithnode) | Creates a drag action object. The object needs to be associated with a UI instance, which can be specified by passing in a component node of the current UI instance. |
| [ArkUI\_DragAction\* OH\_ArkUI\_CreateDragActionWithContext(ArkUI\_ContextHandle uiContext)](#oh_arkui_createdragactionwithcontext) | Creates a drag action object for the specified UI instance. |
| [void OH\_ArkUI\_DragAction\_Dispose(ArkUI\_DragAction\* dragAction)](#oh_arkui_dragaction_dispose) | Disposes of an **ArkUI\_DragAction** object. |
| [int32\_t OH\_ArkUI\_DragAction\_SetPointerId(ArkUI\_DragAction\* dragAction, int32\_t pointer)](#oh_arkui_dragaction_setpointerid) | Sets the pointer ID. If only one finger is used on the screen, the finger ID is 0. Generally, you can set this parameter to **0**. |
| [int32\_t OH\_ArkUI\_DragAction\_SetPixelMaps(ArkUI\_DragAction\* dragAction, OH\_PixelmapNative\* pixelmapArray\[\], int32\_t size)](#oh_arkui_dragaction_setpixelmaps) | Sets the drag previews for a drag action. Only pixel map objects are supported. |
| [int32\_t OH\_ArkUI\_DragAction\_SetTouchPointX(ArkUI\_DragAction\* dragAction, float x)](#oh_arkui_dragaction_settouchpointx) | Sets the touch point relative to the upper left corner of the first drag preview (pixel map). |
| [int32\_t OH\_ArkUI\_DragAction\_SetTouchPointY(ArkUI\_DragAction\* dragAction, float y)](#oh_arkui_dragaction_settouchpointy) | Sets the touch point relative to the upper left corner of the first drag preview (pixel map). |
| [int32\_t OH\_ArkUI\_DragAction\_SetData(ArkUI\_DragAction\* dragAction, OH\_UdmfData\* data)](#oh_arkui_dragaction_setdata) | Sets the drag data. |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragAction\_SetDataLoadParams(ArkUI\_DragAction\* dragAction,OH\_UdmfDataLoadParams\* dataLoadParams)](#oh_arkui_dragaction_setdataloadparams) | This API provides data loading parameters to the system instead of directly providing a complete data object. When the user drops data on the target application, the system will use **dataLoadParams** to request data. This can significantly improve the efficiency of dragging large volumes of data and the efficiency of processing the dropped data in the target application. This API must always be used in preference to [OH\_ArkUI\_DragAction\_SetData](#oh_arkui_dragaction_setdata). For details about how to create and prepare data loading parameters, see [OH\_UdmfDataLoadParams\_Create](../../../../arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfdataloadparams_create) in **udmf.h**. If this API conflicts with [OH\_ArkUI\_DragAction\_SetData](#oh_arkui_dragaction_setdata), the system always uses the last called API. |
| [int32\_t OH\_ArkUI\_DragAction\_SetDragPreviewOption(ArkUI\_DragAction\* dragAction, ArkUI\_DragPreviewOption\* option)](#oh_arkui_dragaction_setdragpreviewoption) | Sets an **ArkUI\_DragPreviewOption** object for the specified drag action object. |
| [int32\_t OH\_ArkUI\_DragAction\_RegisterStatusListener(ArkUI\_DragAction\* dragAction, void\* userData,void(\*listener)(ArkUI\_DragAndDropInfo\* dragAndDropInfo, void\* userData))](#oh_arkui_dragaction_registerstatuslistener) | Registers a drag status listener. This listener can be used to check whether the data is successfully received and processed. |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_GetDisplayId(ArkUI\_DragEvent\* event, int32\_t\* displayId)](#oh_arkui_dragevent_getdisplayid) | Obtains the ID of the screen where this drag event occurs. This API is not supported when **eventType** is **NODE\_ON\_DRAG\_END**. |
| [void OH\_ArkUI\_DragAction\_UnregisterStatusListener(ArkUI\_DragAction\* dragAction)](#oh_arkui_dragaction_unregisterstatuslistener) | Unregisters a drag status listener. |
| [ArkUI\_DragStatus OH\_ArkUI\_DragAndDropInfo\_GetDragStatus(ArkUI\_DragAndDropInfo\* dragAndDropInfo)](#oh_arkui_draganddropinfo_getdragstatus) | Obtains the drag status of the [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md). **ArkUI\_DRAG\_STATUS\_UNKNOWN** is returned if the acquisition fails. |
| [ArkUI\_DragEvent\* OH\_ArkUI\_DragAndDropInfo\_GetDragEvent(ArkUI\_DragAndDropInfo\* dragAndDropInfo)](#oh_arkui_draganddropinfo_getdragevent) | Obtains a drag event based on the specified drag and drop information. The drag event can then be used to obtain the drag result. |
| [int32\_t OH\_ArkUI\_StartDrag(ArkUI\_DragAction\* dragAction)](#oh_arkui_startdrag) | Initiates a drag action through the specified **DragAction** object. |
| [int32\_t OH\_ArkUI\_DragEvent\_RequestDragEndPending(ArkUI\_DragEvent\* event, int32\_t\* requestIdentify)](#oh_arkui_dragevent_requestdragendpending) | Requests deferred processing of the drag end event, allowing the application to asynchronously confirm the operation result. The application must pass the final result back to the system via the [OH\_ArkUI\_NotifyDragResult](#oh_arkui_notifydragresult) API, and call [OH\_ArkUI\_NotifyDragEndPendingDone](#oh_arkui_notifydragendpendingdone) after all processing is completed. The maximum waiting time is 2 seconds. |
| [int32\_t OH\_ArkUI\_NotifyDragResult(int32\_t requestIdentify, ArkUI\_DragResult result)](#oh_arkui_notifydragresult) | Notifies the system of the final drag result. The system will verify whether the request identifier matches that returned by [OH\_ArkUI\_DragEvent\_RequestDragEndPending](#oh_arkui_dragevent_requestdragendpending). If they do not match, this call will be ignored. |
| [int32\_t OH\_ArkUI\_NotifyDragEndPendingDone(int32\_t requestIdentify)](#oh_arkui_notifydragendpendingdone) | Notifies the system that all asynchronous processing has been completed and the drag end pending state can be terminated. |
| [ArkUI\_ErrorCode OH\_ArkUI\_EnableDropDisallowedBadge(ArkUI\_ContextHandle uiContext, bool enabled)](#oh_arkui_enabledropdisallowedbadge) | Sets whether the drop-disallowed badge can be displayed. |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointXToGlobalDisplay(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_gettouchpointxtoglobaldisplay) | Obtains the x-coordinate of the drag touch point relative to the global display from the specified **ArkUI\_DragEvent** object. |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointYToGlobalDisplay(ArkUI\_DragEvent\* event)](#oh_arkui_dragevent_gettouchpointytoglobaldisplay) | Obtains the y-coordinate of the drag touch point relative to the global display from the specified **ArkUI\_DragEvent** object. |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_GetDragSource(ArkUI\_DragEvent\* event, char \*bundleName, int32\_t length)](#oh_arkui_dragevent_getdragsource) | Obtains the bundle name of the drag source application. The caller must provide a character array with a minimum length of 128 characters to store the bundle name. |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_IsRemote(ArkUI\_DragEvent\* event, bool\* isRemote)](#oh_arkui_dragevent_isremote) | Checks whether the current drag operation is a cross-device drag. |

#### Enum Description

#### \[h2\]ArkUI\_DragResult

enum ArkUI\_DragResult

**Description**

Enumerates drag results, which are set by the data receiver and transferred by the system to the drag source so that the drag source is aware of the data processing result of the receiver.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_DRAG\_RESULT\_SUCCESSFUL = 0 | The drag and drop operation succeeded. |
| ARKUI\_DRAG\_RESULT\_FAILED = 1 | The drag and drop operation failed. |
| ARKUI\_DRAG\_RESULT\_CANCELED = 2 | The drag and drop operation was canceled. |

#### \[h2\]ArkUI\_DropOperation

enum ArkUI\_DropOperation

**Description**

Enumerates data processing modes used when data is dropped, which affects the display of the badge. When the copy operation is set, the badge displays a plus sign (+). When the cut operation is set, the badge does not display a plus sign (+).

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_DROP\_OPERATION\_COPY = 0 | Copy. |
| ARKUI\_DROP\_OPERATION\_MOVE = 1 | Cut. |

#### \[h2\]ArkUI\_PreDragStatus

enum ArkUI\_PreDragStatus

**Description**

Enumerates interaction states prior to a drop and drop operation.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_PRE\_DRAG\_STATUS\_UNKNOWN = -1 | Unknown. |
| ARKUI\_PRE\_DRAG\_STATUS\_ACTION\_DETECTING = 0 | A drag gesture is being detected. |
| ARKUI\_PRE\_DRAG\_STATUS\_READY\_TO\_TRIGGER\_DRAG = 1 | The component is ready to be dragged. |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LIFT\_STARTED = 2 | A lift animation is started. |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LIFT\_FINISHED = 3 | A lift animation is finished. |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LANDING\_STARTED = 4 | A drop animation is started. |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LANDING\_FINISHED = 5 | A drop animation is finished. |
| ARKUI\_PRE\_DRAG\_STATUS\_CANCELED\_BEFORE\_DRAG = 6 | A drop animation is terminated. |

#### \[h2\]ArkUI\_DragPreviewScaleMode

enum ArkUI\_DragPreviewScaleMode

**Description**

Enumerates drag preview scale modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_DRAG\_PREVIEW\_SCALE\_AUTO = 0 | Enables the system to automatically change the position of the dragged point based on the scenario and apply scaling transformations to the drag preview based on set rules. |
| ARKUI\_DRAG\_PREVIEW\_SCALE\_DISABLED = 1 | Disables the system's scaling behavior for the drag preview. |

#### \[h2\]ArkUI\_DragStatus

enum ArkUI\_DragStatus

**Description**

Enumerates drag operation states.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_DRAG\_STATUS\_UNKNOWN = -1 | Unknown drag state. |
| ARKUI\_DRAG\_STATUS\_STARTED = 0 | The drag operation has started. |
| ARKUI\_DRAG\_STATUS\_ENDED = 1 | The drag operation has ended. |

#### Function Description

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetDragEvent()

ArkUI\_DragEvent\* OH\_ArkUI\_NodeEvent\_GetDragEvent(ArkUI\_NodeEvent\* nodeEvent)

**Description**

Obtains a **DragEvent** object from the specified **NodeEvent** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* nodeEvent | Pointer to the target **ArkUI\_NodeEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* | Returns the pointer to an **ArkUI\_DragEvent** object; returns null if the parameter passed in is invalid or is not a drag-related event. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetPreDragStatus()

ArkUI\_PreDragStatus OH\_ArkUI\_NodeEvent\_GetPreDragStatus(ArkUI\_NodeEvent\* nodeEvent)

**Description**

Obtains the state prior to a drop and drop operation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* nodeEvent | Pointer to the target **ArkUI\_NodeEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_PreDragStatus](#arkui_predragstatus) | State prior to the drop and drop operation. |

#### \[h2\]OH\_ArkUI\_DragEvent\_DisableDefaultDropAnimation()

int32\_t OH\_ArkUI\_DragEvent\_DisableDefaultDropAnimation(ArkUI\_DragEvent\* event, bool disable)

**Description**

Sets whether to disable the default drop animation, which is enabled by default. Use this API to apply a custom drop animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| bool disable | Whether to disable the default drop animation. The value **true** means to disable the default drop animation, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_SetSuggestedDropOperation()

int32\_t OH\_ArkUI\_DragEvent\_SetSuggestedDropOperation(ArkUI\_DragEvent\* event, ArkUI\_DropOperation dropOperation)

**Description**

Sets the data processing mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [ArkUI\_DropOperation](#arkui_dropoperation) dropOperation | Type of the suggested drop operation. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_SetDragResult()

int32\_t OH\_ArkUI\_DragEvent\_SetDragResult(ArkUI\_DragEvent\* event, ArkUI\_DragResult result)

**Description**

Sets the result for a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [ArkUI\_DragResult](#arkui_dragresult) result | Drag data processing result. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_SetData()

int32\_t OH\_ArkUI\_DragEvent\_SetData(ArkUI\_DragEvent\* event, OH\_UdmfData\* data)

**Description**

Set drag data for a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [OH\_UdmfData](../../../../arkdata/c-apis/structs/oh-udmfdata/document.md)\* data | Drag data configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_SetDataLoadParams()

ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_SetDataLoadParams(ArkUI\_DragEvent\* event, OH\_UdmfDataLoadParams\* dataLoadParams)

**Description**

This API provides data loading parameters to the system instead of directly providing a complete data object. When the user drops data on the target application, the system will use **dataLoadParams** to request data. This can significantly improve the efficiency of dragging large volumes of data and the efficiency of processing the dropped data in the target application. This API must always be used in preference to [OH\_ArkUI\_DragEvent\_SetData](#oh_arkui_dragevent_setdata). For details about how to create and prepare data loading parameters, see [OH\_UdmfDataLoadParams\_Create](../../../../arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfdataloadparams_create) in **udmf.h**. If this API conflicts with [OH\_ArkUI\_DragEvent\_SetData](#oh_arkui_dragevent_setdata), the system always uses the last called API.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [OH\_UdmfDataLoadParams](../../../../arkdata/c-apis/structs/oh-udmfdataloadparams/document.md)\* dataLoadParams | Data loading parameters used during a drop operation. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetUdmfData()

int32\_t OH\_ArkUI\_DragEvent\_GetUdmfData(ArkUI\_DragEvent\* event, OH\_UdmfData \*data)

**Description**

Obtains the default drag data from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [OH\_UdmfData](../../../../arkdata/c-apis/structs/oh-udmfdata/document.md) \*data | Pointer to an **OH\_UdmfData** object. The application needs to create a pointer for receiving data by using the [OH\_UdmfData\_Create](../../../../arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfdata_create) API. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetDataTypeCount()

int32\_t OH\_ArkUI\_DragEvent\_GetDataTypeCount(ArkUI\_DragEvent\* event, int32\_t\* count)

**Description**

Obtains the number of drag data types from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| int32\_t\* count | Number of drag data types returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetDataTypes()

int32\_t OH\_ArkUI\_DragEvent\_GetDataTypes(ArkUI\_DragEvent \*event, char \*eventTypeArray\[\], int32\_t length, int32\_t maxStrLen)

**Description**

Obtains the type list of drag data types from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) \*event | Pointer to the target **ArkUI\_DragEvent** object. |
| char \*eventTypeArray\[\] | List of the drag data types. You need to create a string array first. |
| int32\_t length | Total length of the array, which cannot be less than the number obtained using **OH\_ArkUI\_DragEvent\_GetDataTypesCount**. |
| int32\_t maxStrLen | Maximum length of each data type string. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the input buffer size is abnormal.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetDragResult()

int32\_t OH\_ArkUI\_DragEvent\_GetDragResult(ArkUI\_DragEvent\* event, ArkUI\_DragResult\* result)

**Description**

Obtains the drag and drop result from the drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [ArkUI\_DragResult](#arkui_dragresult)\* result | Drag result returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetDropOperation()

int32\_t OH\_ArkUI\_DragEvent\_GetDropOperation(ArkUI\_DragEvent\* event, ArkUI\_DropOperation\* operation)

**Description**

Obtains the data handling method from the drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [ArkUI\_DropOperation](#arkui_dropoperation)\* operation | Data handling method. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Possible causes: 1. Parameters are null or the event is not a valid DragEvent.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetPreviewTouchPointX()

float OH\_ArkUI\_DragEvent\_GetPreviewTouchPointX(ArkUI\_DragEvent\* event)

**Description**

Obtains the x-coordinate of the touch point for a drag preview from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the touch point, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetPreviewTouchPointY()

float OH\_ArkUI\_DragEvent\_GetPreviewTouchPointY(ArkUI\_DragEvent\* event)

**Description**

Obtains the y-coordinate of the touch point on the preview image from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the touch point, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetPreviewRectWidth()

float OH\_ArkUI\_DragEvent\_GetPreviewRectWidth(ArkUI\_DragEvent\* event)

**Description**

Obtains the width of a drag preview from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Width of the drag preview, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetPreviewRectHeight()

float OH\_ArkUI\_DragEvent\_GetPreviewRectHeight(ArkUI\_DragEvent\* event)

**Description**

Obtains the height of a drag preview from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Height of the drag preview, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetTouchPointXToWindow()

float OH\_ArkUI\_DragEvent\_GetTouchPointXToWindow(ArkUI\_DragEvent\* event)

**Description**

Obtains the x-coordinate of the touch point relative to the window from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the touch point relative to the window, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetTouchPointYToWindow()

float OH\_ArkUI\_DragEvent\_GetTouchPointYToWindow(ArkUI\_DragEvent\* event)

**Description**

Obtains the y-coordinate of the touch point relative to the window from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the touch point relative to the window, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetTouchPointXToDisplay()

float OH\_ArkUI\_DragEvent\_GetTouchPointXToDisplay(ArkUI\_DragEvent\* event)

**Description**

Obtains the x-coordinate of the touch point relative to the display from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the touch point relative to the display, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetTouchPointYToDisplay()

float OH\_ArkUI\_DragEvent\_GetTouchPointYToDisplay(ArkUI\_DragEvent\* event)

**Description**

Obtains the y-coordinate of the touch point relative to the display from a drag event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the touch point relative to the display, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetVelocityX()

float OH\_ArkUI\_DragEvent\_GetVelocityX(ArkUI\_DragEvent\* event)

**Description**

Obtains the dragging velocity along the x-axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Dragging velocity along the x-axis, in px/s, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetVelocityY()

float OH\_ArkUI\_DragEvent\_GetVelocityY(ArkUI\_DragEvent\* event)

**Description**

Obtains the dragging velocity along the y-axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Dragging velocity along the y-axis, in px/s, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetVelocity()

float OH\_ArkUI\_DragEvent\_GetVelocity(ArkUI\_DragEvent\* event)

**Description**

Obtains the dragging velocity along the main axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Dragging velocity along the main axis, in px/s, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetModifierKeyStates()

int32\_t OH\_ArkUI\_DragEvent\_GetModifierKeyStates(ArkUI\_DragEvent\* event, uint64\_t\* keys)

**Description**

Obtains the pressed status of modifier keys.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| uint64\_t\* keys | Pointer to the combination of pressed modifier keys (Ctrl, Shift, and Alt). The application can use bitwise operations to determine which keys are pressed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_StartDataLoading()

int32\_t OH\_ArkUI\_DragEvent\_StartDataLoading(ArkUI\_DragEvent\* event, OH\_UdmfGetDataParams\* options, char\* key, unsigned int keyLen)

**Description**

Starts data synchronization using the specified synchronization parameters.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| [OH\_UdmfGetDataParams](../../../../arkdata/c-apis/structs/oh-udmfgetdataparams/document.md)\* options | Pointer to the **OH\_UdmfGetDataParams** object. |
| char\* key | Key value returned after successful data setting. The length of the string must be no less than [UDMF\_KEY\_BUFFER\_LEN](../../../../arkdata/c-apis/header-files/udmf-h/document.md#udmf_key_buffer_len). |
| unsigned int keyLen | Length of the **key** string. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CancelDataLoading()

int32\_t OH\_ArkUI\_CancelDataLoading(ArkUI\_ContextHandle uiContext, const char\* key)

**Description**

Cancels the ongoing data synchronization.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | Pointer to the UI instance. |
| const char\* key | Data key value, which is returned via [OH\_ArkUI\_DragEvent\_StartDataLoading](#oh_arkui_dragevent_startdataloading). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DisableDropDataPrefetchOnNode()

int32\_t OH\_ArkUI\_DisableDropDataPrefetchOnNode(ArkUI\_NodeHandle node, bool disabled)

**Description**

Sets whether to disable the data prefetch process before executing [NODE\_ON\_DROP](../native-node-h/document.md#arkui_nodeeventtype). The system will retry data fetching until the maximum time limit (currently 2.4 seconds) is reached, which is useful for cross-device drag and drop operations as it helps stabilize system communication. However, this feature is redundant for the [OH\_ArkUI\_DragEvent\_StartDataLoading](#oh_arkui_dragevent_startdataloading) API. Since this API uses an asynchronous mechanism to fetch data, when [OH\_ArkUI\_DragEvent\_StartDataLoading](#oh_arkui_dragevent_startdataloading) is used in **NODE\_ON\_DROP**, this field must be set to **true** to prevent accidental data fetching before **NODE\_ON\_DROP** is executed.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |
| bool disabled | Whether to disable the data prefetching process. The value **true** means to disable the data prefetching process, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetDragEventStrictReportWithNode()

int32\_t OH\_ArkUI\_SetDragEventStrictReportWithNode(ArkUI\_NodeHandle node, bool enabled)

**Description**

Sets whether to enable strict reporting on drag events. This feature is disabled by default, and you are advised to enable it. If this feature is disabled, the parent component is not notified when an item in it is dragged over its child component. If this feature is enabled, the component is notified of the dragged item's leaving, and the child component to which the dragged item is dropped is notified of the item's entering. This configuration is related to a specific UI instance. You can pass in a specific component node on the current UI instance for association.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |
| bool enabled | Whether to enable strict reporting on drag events. The value **true** means to enable strict reporting on drag events, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetDragEventStrictReportWithContext()

int32\_t OH\_ArkUI\_SetDragEventStrictReportWithContext(ArkUI\_ContextHandle uiContext, bool enabled)

**Description**

Sets whether to enable strict reporting on drag events. This feature is disabled by default, and you are advised to enable it. If this feature is disabled, the parent component is not notified when an item in it is dragged over its child component. If this feature is enabled, the component is notified of the dragged item's leaving, and the child component to which the dragged item is dropped is notified of the item's entering. This configuration is related to a specific UI instance. You can pass in a specific UI instance for association.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | Pointer to the UI instance. |
| bool enabled | Whether to enable strict reporting on drag events. The value **true** means to enable strict reporting on drag events, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetNodeAllowedDropDataTypes()

int32\_t OH\_ArkUI\_SetNodeAllowedDropDataTypes(ArkUI\_NodeHandle node, const char\* typesArray\[\], int32\_t count)

**Description**

Sets the types of data that can be dropped to the specified component. This API resets the settings configured through [OH\_ArkUI\_DisallowNodeAnyDropDataTypes](#oh_arkui_disallownodeanydropdatatypes) or [OH\_ArkUI\_AllowNodeAllDropDataTypes](#oh_arkui_allownodealldropdatatypes).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |
| const char\* typesArray\[\] | Array of types of data that can be dropped. |
| int32\_t count | Length of the array. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DisallowNodeAnyDropDataTypes()

int32\_t OH\_ArkUI\_DisallowNodeAnyDropDataTypes(ArkUI\_NodeHandle node)

**Description**

Configures the specified component to disallow any data types. This API resets the settings configured through [OH\_ArkUI\_SetNodeAllowedDropDataTypes](#oh_arkui_setnodealloweddropdatatypes).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AllowNodeAllDropDataTypes()

int32\_t OH\_ArkUI\_AllowNodeAllDropDataTypes(ArkUI\_NodeHandle node)

**Description**

Configures the specified component to allow any data types. This API resets the settings configured through [OH\_ArkUI\_SetNodeAllowedDropDataTypes](#oh_arkui_setnodealloweddropdatatypes).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetNodeDraggable()

int32\_t OH\_ArkUI\_SetNodeDraggable(ArkUI\_NodeHandle node, bool enabled)

**Description**

Sets whether the component is draggable.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |
| bool enabled | Whether the component is draggable. The value **true** means that the component is draggable, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetNodeDragPreview()

int32\_t OH\_ArkUI\_SetNodeDragPreview(ArkUI\_NodeHandle node, OH\_PixelmapNative\* preview)

**Description**

Sets a custom drag preview for the specified component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* preview | Custom drag preview, which is a pixel map. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CreateDragPreviewOption()

ArkUI\_DragPreviewOption\* OH\_ArkUI\_CreateDragPreviewOption(void)

**Description**

Creates an **ArkUI\_DragPreviewOption** object.

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* | **ArkUI\_DragPreviewOption** object. |

#### \[h2\]OH\_ArkUI\_DragPreviewOption\_Dispose()

void OH\_ArkUI\_DragPreviewOption\_Dispose(ArkUI\_DragPreviewOption\* option)

**Description**

Disposes of an **ArkUI\_DragPreviewOption** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |

#### \[h2\]OH\_ArkUI\_DragPreviewOption\_SetScaleMode()

int32\_t OH\_ArkUI\_DragPreviewOption\_SetScaleMode(ArkUI\_DragPreviewOption\* option, ArkUI\_DragPreviewScaleMode scaleMode)

**Description**

Sets the scale mode for an **ArkUI\_DragPreviewOption** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |
| [ArkUI\_DragPreviewScaleMode](#arkui_dragpreviewscalemode) scaleMode | Scale mode to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragPreviewOption\_SetDefaultShadowEnabled()

int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultShadowEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)

**Description**

Sets whether to enable the default shadow effect for an **ArkUI\_DragPreviewOption** object. The effect is disabled by default.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |
| bool enabled | Whether to enable the default shadow effect. The value **true** means to enable the default shadow effect, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragPreviewOption\_SetDefaultRadiusEnabled()

int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultRadiusEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)

**Description**

Sets whether to enable the default rounded corner effect for an **ArkUI\_DragPreviewOption** object. The rounded corner radius is 12.0 vp by default. The effect is disabled by default.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |
| bool enabled | Whether to enable the default corner radius effect. The value **true** means to enable the default corner radius effect, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled()

int32\_t OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)

**Description**

Sets whether to enable the badge for an **ArkUI\_DragPreviewOption** object. If this feature is enabled, a badge that contains the number of dragged items is displayed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |
| bool enabled | Whether to enable the badge. The value **true** means to enable the badge, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragPreviewOption\_SetBadgeNumber()

int32\_t OH\_ArkUI\_DragPreviewOption\_SetBadgeNumber(ArkUI\_DragPreviewOption\* option, uint32\_t forcedNumber)

**Description**

Sets the count on the badge. The settings will overwrite the value in [OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled](#oh_arkui_dragpreviewoption_setnumberbadgeenabled).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |
| uint32\_t forcedNumber | Number of badges. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragPreviewOption\_SetDefaultAnimationBeforeLiftingEnabled()

int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultAnimationBeforeLiftingEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)

**Description**

Sets whether to enable the default animation on a click or touch.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |
| bool enabled | Whether to enable the default animation on a click or touch. The value **true** means to enable the default animation on a click or touch, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetNodeDragPreviewOption()

int32\_t OH\_ArkUI\_SetNodeDragPreviewOption(ArkUI\_NodeHandle node, ArkUI\_DragPreviewOption\* option)

**Description**

Sets an **ArkUI\_DragPreviewOption** object for the specified component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CreateDragActionWithNode()

ArkUI\_DragAction\* OH\_ArkUI\_CreateDragActionWithNode(ArkUI\_NodeHandle node)

**Description**

Creates a drag action object. The object needs to be associated with a UI instance, which can be specified by passing in a component node of the current UI instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* | Pointer to the created drag action object, or null if the operation fails. |

#### \[h2\]OH\_ArkUI\_CreateDragActionWithContext()

ArkUI\_DragAction\* OH\_ArkUI\_CreateDragActionWithContext(ArkUI\_ContextHandle uiContext)

**Description**

Creates a drag action object for the specified UI instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | Pointer to the UI instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* | Pointer to the created drag action object, or null if the operation fails. |

#### \[h2\]OH\_ArkUI\_DragAction\_Dispose()

void OH\_ArkUI\_DragAction\_Dispose(ArkUI\_DragAction\* dragAction)

**Description**

Disposes of an **ArkUI\_DragAction** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |

#### \[h2\]OH\_ArkUI\_DragAction\_SetPointerId()

int32\_t OH\_ArkUI\_DragAction\_SetPointerId(ArkUI\_DragAction\* dragAction, int32\_t pointer)

**Description**

Sets the pointer ID. If only one finger is used on the screen, the finger ID is 0. Generally, you can set this parameter to **0**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| int32\_t pointer | Pointer ID. The value ranges from 0 to 9. If the value is out of the range, **\-1** is used by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_SetPixelMaps()

int32\_t OH\_ArkUI\_DragAction\_SetPixelMaps(ArkUI\_DragAction\* dragAction, OH\_PixelmapNative\* pixelmapArray\[\], int32\_t size)

**Description**

Sets the drag previews for a drag action. Only pixel map objects are supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* pixelmapArray\[\] | 
Array of the drag previews to set, which must be pixel maps.

Note: This parameter must be an object allocated on the heap. You need to manually manage the lifecycle of the object.

 |
| int32\_t size | Number of drag previews. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_SetTouchPointX()

int32\_t OH\_ArkUI\_DragAction\_SetTouchPointX(ArkUI\_DragAction\* dragAction, float x)

**Description**

Sets the touch point relative to the upper left corner of the first drag preview (pixel map).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| float x | X-coordinate of the touch point, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_SetTouchPointY()

int32\_t OH\_ArkUI\_DragAction\_SetTouchPointY(ArkUI\_DragAction\* dragAction, float y)

**Description**

Sets the touch point relative to the upper left corner of the first drag preview (pixel map).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| float y | Y-coordinate of the touch point, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_SetData()

int32\_t OH\_ArkUI\_DragAction\_SetData(ArkUI\_DragAction\* dragAction, OH\_UdmfData\* data)

**Description**

Sets the drag data.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| [OH\_UdmfData](../../../../arkdata/c-apis/structs/oh-udmfdata/document.md)\* data | Drag data configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_SetDataLoadParams()

ArkUI\_ErrorCode OH\_ArkUI\_DragAction\_SetDataLoadParams(ArkUI\_DragAction\* dragAction,OH\_UdmfDataLoadParams\* dataLoadParams)

**Description**

This API provides data loading parameters to the system instead of directly providing a complete data object. When the user drops data on the target application, the system will use **dataLoadParams** to request data. This can significantly improve the efficiency of dragging large volumes of data and the efficiency of processing the dropped data in the target application. This API must always be used in preference to [OH\_ArkUI\_DragAction\_SetData](#oh_arkui_dragaction_setdata). For details about how to create and prepare data loading parameters, see [OH\_UdmfDataLoadParams\_Create](../../../../arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfdataloadparams_create) in **udmf.h**. If this API conflicts with [OH\_ArkUI\_DragAction\_SetData](#oh_arkui_dragaction_setdata), the system always uses the last called API.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| [OH\_UdmfDataLoadParams](../../../../arkdata/c-apis/structs/oh-udmfdataloadparams/document.md)\* dataLoadParams | Data loading parameters used during a drop operation. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_SetDragPreviewOption()

int32\_t OH\_ArkUI\_DragAction\_SetDragPreviewOption(ArkUI\_DragAction\* dragAction, ArkUI\_DragPreviewOption\* option)

**Description**

Sets an **ArkUI\_DragPreviewOption** object for the specified drag action object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| [ArkUI\_DragPreviewOption](../../structs/arkui-dragpreviewoption/document.md)\* option | Custom parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_RegisterStatusListener()

int32\_t OH\_ArkUI\_DragAction\_RegisterStatusListener(ArkUI\_DragAction\* dragAction, void\* userData,void(\*listener)(ArkUI\_DragAndDropInfo\* dragAndDropInfo, void\* userData))

**Description**

Registers a drag status listener. This listener can be used to check whether the data is successfully received and processed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |
| void\* userData | Custom user data. |
| listener | Listener to register. When the callback is invoked, the system returns a pointer to the drag status object. The pointer is destroyed after the callback is complete and the application should not hold it anymore. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetDisplayId()

ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_GetDisplayId(ArkUI\_DragEvent\* event, int32\_t\* displayId)

**Description**

Obtains the ID of the screen where this drag event occurs. This API is not supported when **eventType** is **NODE\_ON\_DRAG\_END**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| int32\_t\* displayId | ID of the screen where the current drag event occurs. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragAction\_UnregisterStatusListener()

void OH\_ArkUI\_DragAction\_UnregisterStatusListener(ArkUI\_DragAction\* dragAction)

**Description**

Unregisters a drag status listener.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Pointer to the target drag action object. |

#### \[h2\]OH\_ArkUI\_DragAndDropInfo\_GetDragStatus()

ArkUI\_DragStatus OH\_ArkUI\_DragAndDropInfo\_GetDragStatus(ArkUI\_DragAndDropInfo\* dragAndDropInfo)

**Description**

Obtains the drag status of the [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md). **ArkUI\_DRAG\_STATUS\_UNKNOWN** is returned if the acquisition fails.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAndDropInfo](../../structs/arkui-draganddropinfo/document.md)\* dragAndDropInfo | Drag and drop information returned by the drag status listener. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DragStatus](#arkui_dragstatus) | **ArkUI\_DragStatus** object, or **ArkUI\_DRAG\_STATUS\_UNKNOWN** if an error occurs. |

#### \[h2\]OH\_ArkUI\_DragAndDropInfo\_GetDragEvent()

ArkUI\_DragEvent\* OH\_ArkUI\_DragAndDropInfo\_GetDragEvent(ArkUI\_DragAndDropInfo\* dragAndDropInfo)

**Description**

Obtains a drag event based on the specified drag and drop information. The drag event can then be used to obtain the drag result.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAndDropInfo](../../structs/arkui-draganddropinfo/document.md)\* dragAndDropInfo | Drag and drop information returned by the drag status listener. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* | **ArkUI\_DragEvent** object, or null if an error occurs. |

#### \[h2\]OH\_ArkUI\_StartDrag()

int32\_t OH\_ArkUI\_StartDrag(ArkUI\_DragAction\* dragAction)

**Description**

Initiates a drag action through the specified **DragAction** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragAction](../../structs/arkui-dragaction/document.md)\* dragAction | Drag action object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_RequestDragEndPending()

int32\_t OH\_ArkUI\_DragEvent\_RequestDragEndPending(ArkUI\_DragEvent\* event, int32\_t\* requestIdentify)

**Description**

Requests deferred processing of the drag end event, allowing the application to asynchronously confirm the operation result. The application must pass the final result back to the system via the [OH\_ArkUI\_NotifyDragResult](#oh_arkui_notifydragresult) API, and call [OH\_ArkUI\_NotifyDragEndPendingDone](#oh_arkui_notifydragendpendingdone) after all processing is completed. The maximum waiting time is 2 seconds.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| int32\_t\* requestIdentify | System-generated request identifier, which is an output parameter and must point to a valid address. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED](../native-type-h/document.md#arkui_errorcode) if the operation is not allowed at the current stage.

 |

#### \[h2\]OH\_ArkUI\_NotifyDragResult()

int32\_t OH\_ArkUI\_NotifyDragResult(int32\_t requestIdentify, ArkUI\_DragResult result)

**Description**

Notifies the system of the final drag result. The system will verify whether the request identifier matches that returned by [OH\_ArkUI\_DragEvent\_RequestDragEndPending](#oh_arkui_dragevent_requestdragendpending). If they do not match, this call will be ignored.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t requestIdentify | Identifier returned by [OH\_ArkUI\_DragEvent\_RequestDragEndPending](#oh_arkui_dragevent_requestdragendpending). |
| [ArkUI\_DragResult](#arkui_dragresult) result | Enumerated value of the drag result (of the [ArkUI\_DragResult](#arkui_dragresult) type). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED](../native-type-h/document.md#arkui_errorcode) if the operation is not allowed at the current stage.

 |

#### \[h2\]OH\_ArkUI\_NotifyDragEndPendingDone()

int32\_t OH\_ArkUI\_NotifyDragEndPendingDone(int32\_t requestIdentify)

**Description**

Notifies the system that all asynchronous processing has been completed and the drag end pending state can be terminated.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t requestIdentify | Identifier returned by [OH\_ArkUI\_DragEvent\_RequestDragEndPending](#oh_arkui_dragevent_requestdragendpending). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED](../native-type-h/document.md#arkui_errorcode) if the operation is not allowed at the current stage.

 |

#### \[h2\]OH\_ArkUI\_EnableDropDisallowedBadge()

ArkUI\_ErrorCode OH\_ArkUI\_EnableDropDisallowedBadge(ArkUI\_ContextHandle uiContext, bool enabled)

**Description**

Sets whether the drop-disallowed badge can be displayed.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | Pointer to the UI instance. |
| bool enabled | Whether the drop-disallowed badge can be displayed. The value **true** means that the drop-disallowed badge can be displayed, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetTouchPointXToGlobalDisplay()

float OH\_ArkUI\_DragEvent\_GetTouchPointXToGlobalDisplay(ArkUI\_DragEvent\* event)

**Description**

Obtains the x-coordinate of the drag touch point relative to the global display from the specified **ArkUI\_DragEvent** object.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the touch point relative to the global display, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetTouchPointYToGlobalDisplay()

float OH\_ArkUI\_DragEvent\_GetTouchPointYToGlobalDisplay(ArkUI\_DragEvent\* event)

**Description**

Obtains the y-coordinate of the drag touch point relative to the global display from the specified **ArkUI\_DragEvent** object.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the touch point relative to the global display, in px, or the default value **0** if the input parameter is invalid. |

#### \[h2\]OH\_ArkUI\_DragEvent\_GetDragSource()

ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_GetDragSource(ArkUI\_DragEvent\* event, char \*bundleName, int32\_t length)

**Description**

Obtains the bundle name of the drag source application. The caller must provide a character array with a minimum length of 128 characters to store the bundle name.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| char \*bundleName | Character array to store the bundle name string, with a length of at least 128 characters. |
| int32\_t length | Length of the character array to store the bundle name string. The minimum length is 128 characters. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DragEvent\_IsRemote()

ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_IsRemote(ArkUI\_DragEvent\* event, bool\* isRemote)

**Description**

Checks whether the current drag operation is a cross-device drag.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md)\* event | Pointer to the target **ArkUI\_DragEvent** object. |
| bool\* isRemote | Pointer to a boolean variable to store the result. The value **true** means that the current drag operation is a cross-device drag, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
