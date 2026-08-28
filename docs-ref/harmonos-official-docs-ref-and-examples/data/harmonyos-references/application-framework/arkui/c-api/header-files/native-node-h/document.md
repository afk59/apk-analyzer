# native\_node.h

#### Overview

Provides type definitions for **NativeNode** APIs.

**File to include**: <arkui/native\_node.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [native\_node\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/native_node_sample)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) | ArkUI\_AttributeItem | Defines the general input parameter structure of the [setAttribute](../../structs/arkui-nativenodeapi-1/document.md#setattribute) function. |
| [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) | ArkUI\_NodeComponentEvent | Defines a struct for the component callback event. |
| [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) | ArkUI\_StringAsyncEvent | Defines a struct for the component callback event that uses string parameters. |
| [ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md) | ArkUI\_TextChangeEvent | Defines a hybrid data structure for component events. |
| [ArkUI\_NativeNodeAPI\_1](../../structs/arkui-nativenodeapi-1/document.md) | ArkUI\_NativeNodeAPI\_1 | Defines a struct for node APIs of ArkUI on the native side. APIs related to the Node module must be called on the main thread. |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) | ArkUI\_NodeEvent | Defines a struct for the component event. |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md) | ArkUI\_NodeCustomEvent | Defines a struct for the custom component event. |
| [ArkUI\_NodeAdapter\*](../../structs/arkui-nodeadapter/document.md) | ArkUI\_NodeAdapterHandle | Defines a struct for the component adapter, which is used for lazy loading of elements of scrollable components. |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md) | ArkUI\_NodeAdapterEvent | Defines a struct for the component adapter event. |
| [ArkUI\_NodeContentEvent](../../structs/arkui-nodecontentevent/document.md) | ArkUI\_NodeContentEvent | Defines a struct for the NodeContent event. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_NodeType](#arkui_nodetype) | ArkUI\_NodeType | Enumerates ArkUI component types that can be created on the native side. |
| [ArkUI\_NodeAttributeType](#arkui_nodeattributetype) | ArkUI\_NodeAttributeType | Enumerates the ArkUI style attributes that can be set on the native side. |
| [ArkUI\_NodeEventType](#arkui_nodeeventtype) | ArkUI\_NodeEventType | Enumerates the event types supported by the **NativeNode** component. |
| [ArkUI\_NodeDirtyFlag](#arkui_nodedirtyflag) | ArkUI\_NodeDirtyFlag | Enumerates the flags passed to indicate the need to re-execute measurement, layout, or rendering when a custom component calls the **::markDirty** API. |
| [ArkUI\_NodeCustomEventType](#arkui_nodecustomeventtype) | ArkUI\_NodeCustomEventType | Enumerates the custom component event types. |
| [ArkUI\_NodeAdapterEventType](#arkui_nodeadaptereventtype) | ArkUI\_NodeAdapterEventType | Enumerates node adapter events. |
| [ArkUI\_NodeContentEventType](#arkui_nodecontenteventtype) | ArkUI\_NodeContentEventType | Enumerates the event types for **NodeContent**. |
| [ArkUI\_InspectorErrorCode](#arkui_inspectorerrorcode) | ArkUI\_InspectorErrorCode | Enumerates the inspector error codes. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_NodeEventType OH\_ArkUI\_NodeEvent\_GetEventType(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_geteventtype) | \- | Obtains the type of a component event. |
| [int32\_t OH\_ArkUI\_NodeEvent\_GetTargetId(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_gettargetid) | \- | Obtains the custom ID of a component event. The event ID is passed in as a parameter when the [registerNodeEvent](../../structs/arkui-nativenodeapi-1/document.md#registernodeevent) function is called and can be applied to the dispatch logic of the same event entry point function [registerNodeEventReceiver](../../structs/arkui-nativenodeapi-1/document.md#registernodeeventreceiver). |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeEvent\_GetNodeHandle(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_getnodehandle) | \- | Obtains the component object that triggers an event. |
| [ArkUI\_UIInputEvent\* OH\_ArkUI\_NodeEvent\_GetInputEvent(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_getinputevent) | \- | Obtains input event (for example, touch event) data for a component event. |
| [ArkUI\_NodeComponentEvent\* OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_getnodecomponentevent) | \- | Obtains the numerical data in a component event. |
| [ArkUI\_StringAsyncEvent\* OH\_ArkUI\_NodeEvent\_GetStringAsyncEvent(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_getstringasyncevent) | \- | Obtains the string data in a component event. |
| [ArkUI\_TextChangeEvent\* OH\_ArkUI\_NodeEvent\_GetTextChangeEvent(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_gettextchangeevent) | \- | Obtains the **ArkUI\_TextChangeEvent** data from the specified component event. |
| [void\* OH\_ArkUI\_NodeEvent\_GetUserData(ArkUI\_NodeEvent\* event)](#oh_arkui_nodeevent_getuserdata) | \- | Obtains the custom data in a component event. This parameter is passed in [registerNodeEvent](../../structs/arkui-nativenodeapi-1/document.md#registernodeevent) and can be applied to the service logic when the event is triggered. |
| [int32\_t OH\_ArkUI\_NodeEvent\_GetNumberValue(ArkUI\_NodeEvent\* event, int32\_t index, ArkUI\_NumberValue\* value)](#oh_arkui_nodeevent_getnumbervalue) | \- | Obtains the numeric-type parameter of a component event. |
| [int32\_t OH\_ArkUI\_NodeEvent\_GetStringValue(ArkUI\_NodeEvent\* event, int32\_t index, char\*\* string, int32\_t\* stringSize)](#oh_arkui_nodeevent_getstringvalue) | \- | Obtains the string-type parameter of a component event. The string data is valid only during an event callback. To use it outside an event callback, you are advised to copy the string data. |
| [int32\_t OH\_ArkUI\_NodeEvent\_SetReturnNumberValue(ArkUI\_NodeEvent\* event, ArkUI\_NumberValue\* value, int32\_t size)](#oh_arkui_nodeevent_setreturnnumbervalue) | \- | Sets the return value for a component event. |
| [ArkUI\_NodeAdapterHandle OH\_ArkUI\_NodeAdapter\_Create()](#oh_arkui_nodeadapter_create) | \- | Creates a component adapter. |
| [void OH\_ArkUI\_NodeAdapter\_Dispose(ArkUI\_NodeAdapterHandle handle)](#oh_arkui_nodeadapter_dispose) | \- | Disposes of a component adapter. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(ArkUI\_NodeAdapterHandle handle, uint32\_t size)](#oh_arkui_nodeadapter_settotalnodecount) | \- | Sets the total number of elements in the specified adapter. |
| [uint32\_t OH\_ArkUI\_NodeAdapter\_GetTotalNodeCount(ArkUI\_NodeAdapterHandle handle)](#oh_arkui_nodeadapter_gettotalnodecount) | \- | Obtains the total number of elements in the specified adapter. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver(ArkUI\_NodeAdapterHandle handle, void\* userData, void (\*receiver)(ArkUI\_NodeAdapterEvent\* event))](#oh_arkui_nodeadapter_registereventreceiver) | \- | Registers an event callback for the specified adapter. |
| [void OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver(ArkUI\_NodeAdapterHandle handle)](#oh_arkui_nodeadapter_unregistereventreceiver) | \- | Unregisters an event callback for the specified adapter. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_ReloadAllItems(ArkUI\_NodeAdapterHandle handle)](#oh_arkui_nodeadapter_reloadallitems) | \- | Instructs the specified adapter to reload all elements. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_ReloadItem(ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)](#oh_arkui_nodeadapter_reloaditem) | \- | Instructs the specified adapter to reload certain elements. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_RemoveItem(ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)](#oh_arkui_nodeadapter_removeitem) | \- | Instructs the specified adapter to remove certain elements. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_InsertItem(ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)](#oh_arkui_nodeadapter_insertitem) | \- | Instructs the specified adapter to insert certain elements. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_MoveItem(ArkUI\_NodeAdapterHandle handle, uint32\_t from, uint32\_t to)](#oh_arkui_nodeadapter_moveitem) | \- | Instructs the specified adapter to move certain elements. |
| [int32\_t OH\_ArkUI\_NodeAdapter\_GetAllItems(ArkUI\_NodeAdapterHandle handle, ArkUI\_NodeHandle\*\* items, uint32\_t\* size)](#oh_arkui_nodeadapter_getallitems) | \- | Obtains all elements stored in the specified adapter. When the API is called, the array object pointer of the element is returned. You must release the memory data to which the pointer points. |
| [void\* OH\_ArkUI\_NodeAdapterEvent\_GetUserData(ArkUI\_NodeAdapterEvent\* event)](#oh_arkui_nodeadapterevent_getuserdata) | \- | Obtains the custom data passed in during registration of the specified event. |
| [ArkUI\_NodeAdapterEventType OH\_ArkUI\_NodeAdapterEvent\_GetType(ArkUI\_NodeAdapterEvent\* event)](#oh_arkui_nodeadapterevent_gettype) | \- | Obtains the event type. |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeAdapterEvent\_GetRemovedNode(ArkUI\_NodeAdapterEvent\* event)](#oh_arkui_nodeadapterevent_getremovednode) | \- | Obtains the element to be removed for the event to be destroyed. |
| [uint32\_t OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(ArkUI\_NodeAdapterEvent\* event)](#oh_arkui_nodeadapterevent_getitemindex) | \- | Obtains the index of the element to be operated for the specified adapter event. |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeAdapterEvent\_GetHostNode(ArkUI\_NodeAdapterEvent\* event)](#oh_arkui_nodeadapterevent_gethostnode) | \- | Obtains the scrollable container node that uses the specified adapter. |
| [int32\_t OH\_ArkUI\_NodeAdapterEvent\_SetItem(ArkUI\_NodeAdapterEvent\* event, ArkUI\_NodeHandle node)](#oh_arkui_nodeadapterevent_setitem) | \- | Sets the component to be added to the specified adapter. |
| [int32\_t OH\_ArkUI\_NodeAdapterEvent\_SetNodeId(ArkUI\_NodeAdapterEvent\* event, int32\_t id)](#oh_arkui_nodeadapterevent_setnodeid) | \- | Sets the component ID to be generated. |
| [ArkUI\_LayoutConstraint\* OH\_ArkUI\_NodeCustomEvent\_GetLayoutConstraintInMeasure(ArkUI\_NodeCustomEvent\* event)](#oh_arkui_nodecustomevent_getlayoutconstraintinmeasure) | \- | Obtains the size constraint for measurement through a custom component event. |
| [ArkUI\_IntOffset OH\_ArkUI\_NodeCustomEvent\_GetPositionInLayout(ArkUI\_NodeCustomEvent\* event)](#oh_arkui_nodecustomevent_getpositioninlayout) | \- | Obtains the expected position of a component relative to its parent component in the layout phase through a custom component event. |
| [ArkUI\_DrawContext\* OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(ArkUI\_NodeCustomEvent\* event)](#oh_arkui_nodecustomevent_getdrawcontextindraw) | \- | Obtains the drawing context through a custom component event. |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId(ArkUI\_NodeCustomEvent\* event)](#oh_arkui_nodecustomevent_geteventtargetid) | \- | Obtains the ID of a custom component event. |
| [void\* OH\_ArkUI\_NodeCustomEvent\_GetUserData(ArkUI\_NodeCustomEvent\* event)](#oh_arkui_nodecustomevent_getuserdata) | \- | Obtains custom event parameters through a custom component event. |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeCustomEvent\_GetNodeHandle(ArkUI\_NodeCustomEvent\* event)](#oh_arkui_nodecustomevent_getnodehandle) | \- | Obtains a component object through a custom component event. |
| [ArkUI\_NodeCustomEventType OH\_ArkUI\_NodeCustomEvent\_GetEventType(ArkUI\_NodeCustomEvent\* event)](#oh_arkui_nodecustomevent_geteventtype) | \- | Obtains the event type through a custom component event. |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanMeasureInfo(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanMeasureInfo\* info)](#oh_arkui_nodecustomevent_getcustomspanmeasureinfo) | \- | Obtains the measurement information of a custom span through a custom component event. |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_SetCustomSpanMetrics(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanMetrics\* metrics)](#oh_arkui_nodecustomevent_setcustomspanmetrics) | \- | Sets the measurement metrics of a custom span through a custom component event. |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanDrawInfo(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanDrawInfo\* info)](#oh_arkui_nodecustomevent_getcustomspandrawinfo) | \- | Obtains the drawing information of a custom span through a custom component event. |
| [typedef void (\*ArkUI\_NodeContentCallback)(ArkUI\_NodeContentEvent\* event)](#arkui_nodecontentcallback) | ArkUI\_NodeContentCallback | Defines a callback for the NodeContent event. |
| [int32\_t OH\_ArkUI\_NodeContent\_RegisterCallback(ArkUI\_NodeContentHandle content, ArkUI\_NodeContentCallback callback)](#oh_arkui_nodecontent_registercallback) | \- | Registers an event callback for the **NodeContent**. |
| [ArkUI\_NodeContentEventType OH\_ArkUI\_NodeContentEvent\_GetEventType(ArkUI\_NodeContentEvent\* event)](#oh_arkui_nodecontentevent_geteventtype) | \- | Obtains the type of the specified **NodeContent** event. |
| [ArkUI\_NodeContentHandle OH\_ArkUI\_NodeContentEvent\_GetNodeContentHandle(ArkUI\_NodeContentEvent\* event)](#oh_arkui_nodecontentevent_getnodecontenthandle) | \- | Obtains the object that triggers the specified **NodeContent** event. |
| [int32\_t OH\_ArkUI\_NodeContent\_SetUserData(ArkUI\_NodeContentHandle content, void\* userData)](#oh_arkui_nodecontent_setuserdata) | \- | Saves custom data to the specified **NodeContent** object. |
| [void\* OH\_ArkUI\_NodeContent\_GetUserData(ArkUI\_NodeContentHandle content)](#oh_arkui_nodecontent_getuserdata) | \- | Obtains the custom data saved on the specified **NodeContent** object. |
| [int32\_t OH\_ArkUI\_NodeContent\_AddNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)](#oh_arkui_nodecontent_addnode) | \- | Adds an ArkUI component node to the specified **NodeContent** object. |
| [int32\_t OH\_ArkUI\_NodeContent\_RemoveNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)](#oh_arkui_nodecontent_removenode) | \- | Removes an ArkUI component node from the specified **NodeContent** object. |
| [int32\_t OH\_ArkUI\_NodeContent\_InsertNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node, int32\_t position)](#oh_arkui_nodecontent_insertnode) | \- | Inserts an ArkUI component node into a specific position of the specified **NodeContent** object. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutSize(ArkUI\_NodeHandle node, ArkUI\_IntSize\* size)](#oh_arkui_nodeutils_getlayoutsize) | \- | Obtains the layout area size of the component. The size does not count in transformation attributes, such as scale. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPosition(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* localOffset)](#oh_arkui_nodeutils_getlayoutposition) | \- | Obtains the position of the component's layout area relative to its parent component. The relative position does not count in transformation attributes, such as translate. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInWindow(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* globalOffset)](#oh_arkui_nodeutils_getlayoutpositioninwindow) | \- | Obtains the position of the component's layout area relative to the window. The relative position does not count in transformation attributes, such as translate. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInScreen(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* screenOffset)](#oh_arkui_nodeutils_getlayoutpositioninscreen) | \- | Obtains the position of the component's layout area relative to the screen. The relative position does not count in transformation attributes, such as translate. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInGlobalDisplay(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* offset)](#oh_arkui_nodeutils_getlayoutpositioninglobaldisplay) | \- | Obtains the offset of the specified component relative to the global display. The relative position does not count in transformation attributes, such as translate. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInWindow(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* translateOffset)](#oh_arkui_nodeutils_getpositionwithtranslateinwindow) | \- | Obtains the position of the component in the window, including the translate attribute. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInScreen(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* translateOffset)](#oh_arkui_nodeutils_getpositionwithtranslateinscreen) | \- | Obtains the position of the component on the screen, including the translate attribute. |
| [void OH\_ArkUI\_NodeUtils\_AddCustomProperty(ArkUI\_NodeHandle node, const char\* name, const char\* value)](#oh_arkui_nodeutils_addcustomproperty) | \- | Sets a custom property for a component. This API takes effect only in the main thread. |
| [void OH\_ArkUI\_NodeUtils\_RemoveCustomProperty(ArkUI\_NodeHandle node, const char\* name)](#oh_arkui_nodeutils_removecustomproperty) | \- | Removes a custom property that has been set for the specified component. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetCustomProperty(ArkUI\_NodeHandle node, const char\* name, ArkUI\_CustomProperty\*\* handle)](#oh_arkui_nodeutils_getcustomproperty) | \- | Obtains the value of a custom property of the specified component. |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeUtils\_GetParentInPageTree(ArkUI\_NodeHandle node)](#oh_arkui_nodeutils_getparentinpagetree) | \- | Obtains the parent node, which can be a component node created with ArkTS. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo(ArkUI\_NodeHandle head, ArkUI\_ActiveChildrenInfo\*\* handle)](#oh_arkui_nodeutils_getactivechildreninfo) | \- | Obtains all active child nodes of the specified node. Spans are not counted as child nodes. |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeUtils\_GetCurrentPageRootNode(ArkUI\_NodeHandle node)](#oh_arkui_nodeutils_getcurrentpagerootnode) | \- | Obtains the root node of the current page. |
| [bool OH\_ArkUI\_NodeUtils\_IsCreatedByNDK(ArkUI\_NodeHandle node)](#oh_arkui_nodeutils_iscreatedbyndk) | \- | Checks whether the specified component is created with C APIs. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetNodeType(ArkUI\_NodeHandle node)](#oh_arkui_nodeutils_getnodetype) | \- | Obtains the type of the specified node. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetWindowInfo(ArkUI\_NodeHandle node, ArkUI\_HostWindowInfo\*\* info)](#oh_arkui_nodeutils_getwindowinfo) | \- | Obtains the information about the window to which a node belongs. |
| [int32\_t OH\_ArkUI\_NodeUtils\_MoveTo(ArkUI\_NodeHandle node, ArkUI\_NodeHandle target\_parent, int32\_t index)](#oh_arkui_nodeutils_moveto) | \- | Moves a node to a target parent node as a child. |
| [int32\_t OH\_ArkUI\_NativeModule\_InvalidateAttributes(ArkUI\_NodeHandle node)](#oh_arkui_nativemodule_invalidateattributes) | \- | Triggers the node attribute update in this frame. |
| [int32\_t OH\_ArkUI\_List\_CloseAllSwipeActions(ArkUI\_NodeHandle node, void\* userData, void (\*onFinish)(void\* userData))](#oh_arkui_list_closeallswipeactions) | \- | Collapses [list items](../../../arkts-components/scroll-and-swipe/listitem/document.md) in the expanded state. |
| [ArkUI\_ContextHandle OH\_ArkUI\_GetContextByNode(ArkUI\_NodeHandle node)](#oh_arkui_getcontextbynode) | \- | Obtains the pointer to the UI context object of the specified node. |
| [int32\_t OH\_ArkUI\_RegisterSystemColorModeChangeEvent(ArkUI\_NodeHandle node,void\* userData, void (\*onColorModeChange)(ArkUI\_SystemColorMode colorMode, void\* userData))](#oh_arkui_registersystemcolormodechangeevent) | \- | Registers an event listener for system color mode changes. A single component can only register one callback for system color mode changes. For implementation examples, see [Listening for Component Events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-listen-to-component-events). |
| [void OH\_ArkUI\_UnregisterSystemColorModeChangeEvent(ArkUI\_NodeHandle node)](#oh_arkui_unregistersystemcolormodechangeevent) | \- | Unregisters the event listener for system color mode changes. |
| [int32\_t OH\_ArkUI\_RegisterSystemFontStyleChangeEvent(ArkUI\_NodeHandle node,void\* userData, void (\*onFontStyleChange)(ArkUI\_SystemFontStyleEvent\* event, void\* userData))](#oh_arkui_registersystemfontstylechangeevent) | \- | Registers an event listener for system font style changes. A single component can only register one callback for system font style changes. |
| [void OH\_ArkUI\_UnregisterSystemFontStyleChangeEvent(ArkUI\_NodeHandle node)](#oh_arkui_unregistersystemfontstylechangeevent) | \- | Unregisters the event listener for system font style changes. |
| [float OH\_ArkUI\_SystemFontStyleEvent\_GetFontSizeScale(const ArkUI\_SystemFontStyleEvent\* event)](#oh_arkui_systemfontstyleevent_getfontsizescale) | \- | Obtains the font size from the system font style change event. |
| [float OH\_ArkUI\_SystemFontStyleEvent\_GetFontWeightScale(const ArkUI\_SystemFontStyleEvent\* event)](#oh_arkui_systemfontstyleevent_getfontweightscale) | \- | Obtains the font weight from the system font style change event. |
| [int32\_t OH\_ArkUI\_RegisterLayoutCallbackOnNodeHandle(ArkUI\_NodeHandle node,void\* userData, void (\*onLayoutCompleted)(void\* userData))](#oh_arkui_registerlayoutcallbackonnodehandle) | \- | Registers a layout completion callback function for a specific node. |
| [int32\_t OH\_ArkUI\_RegisterDrawCallbackOnNodeHandle(ArkUI\_NodeHandle node,void\* userData, void (\*onDrawCompleted)(void\* userData))](#oh_arkui_registerdrawcallbackonnodehandle) | \- | Registers a drawing completion callback function for a specific node. |
| [int32\_t OH\_ArkUI\_UnregisterLayoutCallbackOnNodeHandle(ArkUI\_NodeHandle node)](#oh_arkui_unregisterlayoutcallbackonnodehandle) | \- | Unregisters the layout completion callback function for a specific node. |
| [int32\_t OH\_ArkUI\_UnregisterDrawCallbackOnNodeHandle(ArkUI\_NodeHandle node)](#oh_arkui_unregisterdrawcallbackonnodehandle) | \- | Unregisters the drawing completion callback function for a specific node. |
| [int32\_t OH\_ArkUI\_GetNodeSnapshot(ArkUI\_NodeHandle node, ArkUI\_SnapshotOptions\* snapshotOptions,OH\_PixelmapNative\*\* pixelmap)](#oh_arkui_getnodesnapshot) | \- | Obtains a snapshot of a given component. If the node is not in the component tree or has not been rendered, the snapshot operation will fail. When the PixelMap is no longer used, you should call [OH\_PixelmapNative\_Release](../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_release) to release it. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById(const char\* id, ArkUI\_NodeHandle\* node)](#oh_arkui_nodeutils_getattachednodehandlebyid) | \- | Obtains the target node based on the provided user ID. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId(const uint32\_t uniqueId, ArkUI\_NodeHandle\* node)](#oh_arkui_nodeutils_getnodehandlebyuniqueid) | \- | Obtain a node by its unique ID. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetNodeUniqueId(ArkUI\_NodeHandle node, int32\_t\* uniqueId)](#oh_arkui_nodeutils_getnodeuniqueid) | \- | Obtains the unique ID of the target node. |
| [int32\_t OH\_ArkUI\_NativeModule\_AdoptChild(ArkUI\_NodeHandle node, ArkUI\_NodeHandle child)](#oh_arkui_nativemodule_adoptchild) | \- | Adopts the target node as an affiliated node. The adopted node must not have an existing parent. This operation establishes a lifecycle relationship without adding the node as a visual child in the component tree. |
| [int32\_t OH\_ArkUI\_NativeModule\_RemoveAdoptedChild(ArkUI\_NodeHandle node, ArkUI\_NodeHandle child)](#oh_arkui_nativemodule_removeadoptedchild) | \- | Removes a previously-adopted affiliated node. |
| [int32\_t OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption(ArkUI\_NodeHandle node, ArkUI\_CrossLanguageOption\* option)](#oh_arkui_nodeutils_setcrosslanguageoption) | \- | Sets the cross-language options for the target node. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption(ArkUI\_NodeHandle node, ArkUI\_CrossLanguageOption\* option)](#oh_arkui_nodeutils_getcrosslanguageoption) | \- | Obtains the cross-language options for the target node. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand(ArkUI\_NodeHandle node, uint32\_t\* index)](#oh_arkui_nodeutils_getfirstchildindexwithoutexpand) | \- | Obtains the index of the first child node of the target node in the tree without expanding any nodes. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand(ArkUI\_NodeHandle node, uint32\_t\* index)](#oh_arkui_nodeutils_getlastchildindexwithoutexpand) | \- | Obtains the index of the last child node of the target node in the tree without expanding any nodes. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode(ArkUI\_NodeHandle node, int32\_t position,ArkUI\_NodeHandle\* subnode, uint32\_t expandMode)](#oh_arkui_nodeutils_getchildwithexpandmode) | \- | Obtains a child node at the specified index using different expansion modes. |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetPositionToParent(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* globalOffset)](#oh_arkui_nodeutils_getpositiontoparent) | \- | Obtains the offset of the target node relative to its parent node, in px. |
| [ArkUI\_ErrorCode OH\_ArkUI\_AddSupportedUIStates(ArkUI\_NodeHandle node, int32\_t uiStates,void (statesChangeHandler)(int32\_t currentStates, void\* userData), bool excludeInner, void\* userData)](#oh_arkui_addsupporteduistates) | \- | Adds the [polymorphic style states](../../../arkts-components/universal-attributes/polymorphic-style/document.md) supported by the component. To handle states efficiently, specify the states of interest and their corresponding handlers. When a state of interest occurs, the handler will be executed. You can adjust the UI style based on the current state within the callback. If this API is called multiple times on the same node, the last set of states and handlers will take precedence. Some component types have default system handling for certain states. For example, the **Button** component has a default style effect for the PRESSED state. When custom state handling is implemented on such components, the default style effect will be applied first, followed by the custom style changes, resulting in a combined effect. To disable the default style effects, set **excludeInner** to **true**, if this is allowed by the system implementation. When this API is called, the provided handler function will be executed immediately. There is no need to explicitly register a listener for the NORMAL state. Once a non-NORMAL state is registered, the system will automatically notify your application when the state changes back to NORMAL. |
| [ArkUI\_ErrorCode OH\_ArkUI\_RemoveSupportedUIStates(ArkUI\_NodeHandle node, int32\_t uiStates)](#oh_arkui_removesupporteduistates) | \- | Removes registered UI states. When all states registered using **OH\_ArkUI\_AddSupportedUIStates** are removed, the registered **stateChangeHandler** will no longer be executed. |
| [int32\_t OH\_ArkUI\_RunTaskInScope(ArkUI\_ContextHandle uiContext, void\* userData, void(\*callback)(void\* userData))](#oh_arkui_runtaskinscope) | \- | Executes the specified callback in the target UI context. For the implementation example, see [Ensuring Multi-Instance Functionality in the NDK](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-scope-task). |
| [int32\_t OH\_ArkUI\_PostAsyncUITask(ArkUI\_ContextHandle context, void\* asyncUITaskData, void (\*asyncUITask)(void\* asyncUITaskData), void (\*onFinish)(void\* asyncUITaskData))](#oh_arkui_postasyncuitask) | \- | Submits the **asyncUITask** function to a non-UI thread provided by the ArkUI framework for execution. After **asyncUITask** finishes execution, the **onFinish** function is called in the UI thread. This is suitable for scenarios involving multi-threaded UI component creation. You can use this API to create UI components in non-UI threads and then mount the created components to the main tree in the UI thread. |
| [int32\_t OH\_ArkUI\_PostUITask(ArkUI\_ContextHandle context, void\* taskData, void (\*task)(void\* taskData))](#oh_arkui_postuitask) | \- | Submits the **task** function to the UI thread for execution. This is suitable for scenarios involving multi-threaded UI component creation. When you create UI components in a self-built thread, you can use this API to mount the created components to the main tree on the UI thread. |
| [int32\_t OH\_ArkUI\_PostUITaskAndWait(ArkUI\_ContextHandle context, void\* taskData, void (\*task)(void\* taskData))](#oh_arkui_postuitaskandwait) | \- | Submits the **task** function to the UI thread for execution. The thread calling this API will block until the **task** function completes execution. Calling this API from the UI thread is equivalent to synchronously calling the **task** function. This is suitable for scenarios involving multi-threaded UI component creation. When you need to call functions that are only supported on the UI thread during the multi-threaded component creation process, you can use this API to return to the UI thread to call the function and then resume multi-threaded component creation after the call completes. When the UI thread is under high load, non-UI threads calling this API may block for extended periods, affecting the performance of multi-threaded UI component creation. Frequent use is not recommended. |
| [int32\_t OH\_ArkUI\_NativeModule\_RegisterCommonEvent(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType, void\* userData, void (callback)(ArkUI\_NodeEvent event))](#oh_arkui_nativemodule_registercommonevent) | \- | Registers a basic event callback for the target node. |
| [int32\_t OH\_ArkUI\_NativeModule\_UnregisterCommonEvent(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType)](#oh_arkui_nativemodule_unregistercommonevent) | \- | Unregisters the basic event callback for the target node. |
| [int32\_t OH\_ArkUI\_NativeModule\_RegisterCommonVisibleAreaApproximateChangeEvent(ArkUI\_NodeHandle node, float\* ratios, int32\_t size, float expectedUpdateInterval, void\* userData, void (callback)(ArkUI\_NodeEvent event))](#oh_arkui_nativemodule_registercommonvisibleareaapproximatechangeevent) | \- | Registers a basic event callback for visible area changes with a constrained callback interval. |
| [int32\_t OH\_ArkUI\_NativeModule\_UnregisterCommonVisibleAreaApproximateChangeEvent(ArkUI\_NodeHandle node)](#oh_arkui_nativemodule_unregistercommonvisibleareaapproximatechangeevent) | \- | Unregisters the basic event callback for visible area changes with a constrained callback interval. |
| [int32\_t OH\_ArkUI\_Swiper\_FinishAnimation(ArkUI\_NodeHandle node)](#oh_arkui_swiper_finishanimation) | \- | Stops the page turning animation being executed by the specified **Swiper** node. |
| [int32\_t OH\_ArkUI\_SetForceDarkConfig(ArkUI\_ContextHandle uiContext, bool forceDark, ArkUI\_NodeType nodeType, uint32\_t (\*colorInvertFunc)(uint32\_t color))](#oh_arkui_setforcedarkconfig) | \- | Sets the color inversion algorithm for the component and instance. |
| [ArkUI\_TouchTestInfo\* OH\_ArkUI\_NodeEvent\_GetTouchTestInfo(ArkUI\_NodeEvent\* nodeEvent)](#oh_arkui_nodeevent_gettouchtestinfo) | \- | Obtains the touch test information in the component event. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| MAX\_NODE\_SCOPE\_NUM 1000 | Defines the maximum number methods for a component. |
| MAX\_COMPONENT\_EVENT\_ARG\_NUM 12 | Defines the maximum number of parameters for a component event. |

#### Enum Description

#### \[h2\]ArkUI\_NodeType

enum ArkUI\_NodeType

**Description**

Enumerates ArkUI component types that can be created on the native side.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_NODE\_CUSTOM = 0 | Custom node. |
| ARKUI\_NODE\_TEXT = 1 | Text. |
| ARKUI\_NODE\_SPAN = 2 | Text span. |
| ARKUI\_NODE\_IMAGE\_SPAN = 3 | Image span. |
| ARKUI\_NODE\_IMAGE = 4 | Image. |
| ARKUI\_NODE\_TOGGLE = 5 | Toggle. |
| ARKUI\_NODE\_LOADING\_PROGRESS = 6 | Loading icon. |
| ARKUI\_NODE\_TEXT\_INPUT = 7 | Single-line text input. |
| ARKUI\_NODE\_TEXT\_AREA = 8 | Multi-line text input. |
| ARKUI\_NODE\_BUTTON = 9 | Icon. |
| ARKUI\_NODE\_PROGRESS = 10 | Progress indicator. |
| ARKUI\_NODE\_CHECKBOX = 11 | Check box. |
| ARKUI\_NODE\_XCOMPONENT = 12 | XComponent of the SURFACE type. |
| ARKUI\_NODE\_DATE\_PICKER = 13 | Date picker. |
| ARKUI\_NODE\_TIME\_PICKER = 14 | Time picker. |
| ARKUI\_NODE\_TEXT\_PICKER = 15 | Text picker. |
| ARKUI\_NODE\_CALENDAR\_PICKER = 16 | Calendar picker. |
| ARKUI\_NODE\_SLIDER = 17 | Slider. |
| ARKUI\_NODE\_RADIO = 18 | Radio button. |
| ARKUI\_NODE\_IMAGE\_ANIMATOR = 19 | Frame animation component. |
| ARKUI\_NODE\_XCOMPONENT\_TEXTURE | 
XComponent of the TEXTURE type.

**Since**: 18

 |
| ARKUI\_NODE\_CHECKBOX\_GROUP = 21 | 

Check box group.

**Since**: 15

 |
| ARKUI\_NODE\_STACK = MAX\_NODE\_SCOPE\_NUM | Stack container. |
| ARKUI\_NODE\_SWIPER | Swiper. |
| ARKUI\_NODE\_SCROLL | Scrolling container. |
| ARKUI\_NODE\_LIST = 1003 | List. |
| ARKUI\_NODE\_LIST\_ITEM = 1004 | List item. |
| ARKUI\_NODE\_LIST\_ITEM\_GROUP = 1005 | List item group. |
| ARKUI\_NODE\_COLUMN | Column container. |
| ARKUI\_NODE\_ROW | Row container. |
| ARKUI\_NODE\_FLEX | Flex container. |
| ARKUI\_NODE\_REFRESH | Refresh component. |
| ARKUI\_NODE\_WATER\_FLOW | Water flow container. |
| ARKUI\_NODE\_FLOW\_ITEM | Water flow item. |
| ARKUI\_NODE\_RELATIVE\_CONTAINER | Relative layout component. |
| ARKUI\_NODE\_GRID | Grid. |
| ARKUI\_NODE\_GRID\_ITEM | Grid item. |
| ARKUI\_NODE\_CUSTOM\_SPAN | Custom span. |
| ARKUI\_NODE\_EMBEDDED\_COMPONENT | 

In-application embedded component.

**Since**: 20

 |
| ARKUI\_NODE\_UNDEFINED | 

Undefined component type. All component types in the color inversion API.

**Since**: 20

 |

#### \[h2\]ArkUI\_NodeAttributeType

enum ArkUI\_NodeAttributeType

**Description**

Defines the ArkUI style attributes that can be set on the native side.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NODE\_WIDTH = 0 | 
Defines the width attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: width, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: width, in vp.

 |
| NODE\_HEIGHT = 1 | 

Defines the height attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: height, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: height, in vp.

 |
| NODE\_BACKGROUND\_COLOR = 2 | 

Defines the background color attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: background color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: background color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

 |
| NODE\_BACKGROUND\_IMAGE = 3 | 

Defines the background image attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: image address, which can be an online URL, a local path, a Base64-encoded string, or a [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) object. [SVG](../../../javascript-components/javascript-compatible-web-like-development-paradigm-arkui-full/svg-components/svg/document.md) images, GIF images, and WebP images are not supported.

.value\[0\]?.i32: whether to repeat the image. Optional. The parameter type is [ArkUI\_ImageRepeat](../native-type-h/document.md#arkui_imagerepeat). The default value is **ARKUI\_IMAGE\_REPEAT\_NONE**.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: image address, which can be an online URL, a local path, a Base64-encoded string, or a PixelMap object. SVG images are not supported.

.value\[0\].i32: whether the image is repeated. The parameter type is [ArkUI\_ImageRepeat](../native-type-h/document.md#arkui_imagerepeat).

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md). Either **.object** or **.string** must be set.

 |
| NODE\_PADDING = 4 | 

Defines the padding attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: Specify the same padding for the four directions.

.value\[0\].f32: padding, in vp.

2: Specify different paddings for different directions.

.value\[0\].f32: top padding, in vp. The default value is **0**.

.value\[1\].f32: right padding, in vp. The default value is **0**.

.value\[2\].f32: bottom padding, in vp. The default value is **0**.

.value\[3\].f32: left padding, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: top padding, in vp.

.value\[1\].f32: right padding, in vp.

.value\[2\].f32: bottom padding, in vp.

.value\[3\].f32: left padding, in vp.

 |
| NODE\_ID = 5 | 

Defines the component ID attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: component ID.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: component ID.

 |
| NODE\_ENABLED = 6 | 

Defines the interactivity attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: The value **true** means that the component can interact with users, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: The value **1** means that the component can interact with users, and **0** means the opposite.

 |
| NODE\_MARGIN = 7 | 

Defines the margin attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: Specify the same margin for the four directions.

.value\[0\].f32: margin, in vp.

2: Specify different margins for different directions.

.value\[0\].f32: top margin, in vp. The default value is **0**.

.value\[1\].f32: right margin, in vp. The default value is **0**.

.value\[2\].f32: bottom margin, in vp. The default value is **0**.

.value\[3\].f32: left margin, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: top margin, in vp.

.value\[1\].f32: right margin, in vp.

.value\[2\].f32: bottom margin, in vp.

.value\[3\].f32: left margin, in vp.

 |
| NODE\_TRANSLATE = 8 | 

Defines the translate attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: distance to translate along the x-axis, in vp. The default value is **0**.

.value\[1\].f32: distance to translate along the y-axis, in vp. The default value is **0**.

.value\[2\].f32: distance to translate along the z-axis, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: distance to translate along the x-axis, in vp.

.value\[1\].f32: distance to translate along the y-axis, in vp.

.value\[2\].f32: distance to translate along the z-axis, in vp.

 |
| NODE\_SCALE = 9 | 

Defines the scale attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: scale factor along the x-axis. The default value is **1**.

.value\[1\].f32: scale factor along the y-axis. The default value is **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: scale factor along the x-axis.

.value\[1\].f32: scale factor along the y-axis.

 |
| NODE\_ROTATE = 10 | 

Defines the rotate attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: X-coordinate of the rotation axis vector. The default value is **0**.

.value\[1\].f32: Y-coordinate of the rotation axis vector. The default value is **0**.

.value\[2\].f32: Z-coordinate of the rotation axis vector. The default value is **0**.

.value\[3\].f32: rotation angle. The default value is **0**.

.value\[4\].f32: line of sight, that is, the distance from the viewpoint to the z=0 plane, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: X-coordinate of the rotation axis vector.

.value\[1\].f32: Y-coordinate of the rotation axis vector.

.value\[2\].f32: Z-coordinate of the rotation axis vector.

.value\[3\].f32: rotation angle.

.value\[4\].f32: line of sight, that is, the distance from the viewpoint to the z=0 plane, in vp.

 |
| NODE\_BRIGHTNESS = 11 | 

Sets the brightness attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: brightness value. The default value is **1.0**, and the recommended value range is \[0, 2.0\].

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: brightness value.

 |
| NODE\_SATURATION = 12 | 

Sets the saturation attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: saturation value. The default value is **1.0**, and the recommended value range is \[0, 50.0).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: saturation value.

 |
| NODE\_BLUR = 13 | 

Sets the blur attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: blur radius. A larger value indicates a higher blur degree. If the value is **0**, the component is not blurred. If the value is less than 0, it is treated as **0** and no error code is returned. The unit is vp. The default value is **0.0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: blur radius. The larger the fuzzy radius, the more blurred the image. If the value is **0**, the image is not blurred. The unit is vp.

 |
| NODE\_LINEAR\_GRADIENT = 14 | 

Sets the gradient attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: start angle of the linear gradient. This attribute takes effect only when [ArkUI\_LinearGradientDirection](../native-type-h/document.md#arkui_lineargradientdirection) is set to **ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM**. A positive value indicates a clockwise rotation from the origin, (0, 0). The default value is **180**.

.value\[1\].i32: direction of the linear gradient. When it is set to any value other than **ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM**, the **angle** setting becomes ineffective. The data type is [ArkUI\_LinearGradientDirection](../native-type-h/document.md#arkui_lineargradientdirection).

.value\[2\].i32: whether the colors are repeated. The default value is **false**.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops.

**stops**: stop positions of the color stops.

**size**: number of colors.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: start angle of the linear gradient. The set value is used only when **ArkUI\_LinearGradientDirection** is set to **ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM**. In other cases, the default value is used.

.value\[1\].i32: direction of the linear gradient.

.value\[2\].i32: whether the colors are repeated.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops.

**stops**: stop positions of the color stops.

**size**: number of colors.

 |
| NODE\_ALIGNMENT = 15 | 

Sets the alignment attribute, which can be set, reset, and obtained as required through APIs. In the **Stack** component, this attribute has the same effect as **NODE\_STACK\_ALIGN\_CONTENT**, which means that it sets the alignment mode of child components in the container.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: alignment mode. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment). The default value is **ARKUI\_ALIGNMENT\_CENTER**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: alignment mode. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment).

 |
| NODE\_OPACITY = 16 | 

Defines the opacity attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: opacity value. The default value is **1**. The value ranges from 0 to 1.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: opacity value. The value ranges from 0 to 1.

 |
| NODE\_BORDER\_WIDTH = 17 | 

Defines the border width attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: .value\[0\].f32: width of the four borders.

2: .value\[0\].f32: width of the top border.

.value\[1\].f32: width of the right border.

.value\[2\].f32: width of the bottom border.

.value\[3\].f32: width of the left border.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: width of the top border.

.value\[1\].f32: width of the right border.

.value\[2\].f32: width of the bottom border.

.value\[3\].f32: width of the left border.

 |
| NODE\_BORDER\_RADIUS = 18 | 

Defines the border corner radius attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: .value\[0\].f32: radius of the four corners.

2: .value\[0\].f32: radius of the upper left corner.

.value\[1\].f32: radius of the upper right corner.

.value\[2\].f32: radius of the lower left corner.

.value\[3\].f32: radius of the lower right corner.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: radius of the upper left corner.

.value\[1\].f32: radius of the upper right corner.

.value\[2\].f32: radius of the lower left corner.

.value\[3\].f32: radius of the lower right corner.

 |
| NODE\_BORDER\_COLOR = 19 | 

Defines the border color attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: .value\[0\].u32: color of the four borders, in 0xARGB format, for example, **0xFFFF11FF**.

2: .value\[0\].u32: color of the top border, in 0xARGB format. The default value is **0xFF000000**.

.value\[1\].u32: color of the right border, in 0xARGB format. The default value is **0xFF000000**.

.value\[2\].u32: color of the bottom border, in 0xARGB format. The default value is **0xFF000000**.

.value\[3\].u32: color of the left border, in 0xARGB format. The default value is **0xFF000000**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the top border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[1\].u32: color of the right border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[2\].u32: color of the lower border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[3\].u32: color of the left border, in 0xARGB format, for example, **0xFFFF11FF**.

 |
| NODE\_BORDER\_STYLE = 20 | 

Defines the border line style attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: .value\[0\].i32: line style of the four borders. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**.

2: .value\[0\].i32: line style of the top border. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**.

.value\[1\].i32: line style of the right border. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**.

.value\[2\].i32: line style of the bottom border. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**.

.value\[3\].i32: line style of the left border. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: line style of the top border.

.value\[1\].i32: line style of the right border.

.value\[2\].i32: line style of the bottom border.

.value\[3\].i32: line style of the left border.

 |
| NODE\_Z\_INDEX = 21 | 

Defines the z-index attribute for the stack sequence. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: z-index value.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: z-index value.

 |
| NODE\_VISIBILITY = 22 | 

Defines the visibility attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show or hide the component. The parameter type is [ArkUI\_Visibility](../native-type-h/document.md#arkui_visibility). The default value is **ARKUI\_VISIBILITY\_VISIBLE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the component is shown or hidden. The parameter type is [ArkUI\_Visibility](../native-type-h/document.md#arkui_visibility). The default value is **ARKUI\_VISIBILITY\_VISIBLE**.

 |
| NODE\_CLIP = 23 | 

Defines the clip attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to clip the area of child components that extend beyond the bounds of the parent component. The value **0** indicates no clipping, and the value **1** indicates clipping. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the area of child components that extend beyond the bounds of the parent component is clipped. The value **0** indicates no clipping, and the value **1** indicates clipping.

 |
| NODE\_CLIP\_SHAPE = 24 | 

Defines the clipping region on the component. This attribute can be set and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1\. Rectangle:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_RECTANGLE**.

.value\[1\].f32: width of the rectangle.

.value\[2\].f32: height of the rectangle.

.value\[3\].f32: width of the rounded corner of the rectangle.

.value\[4\].f32: height of the rounded corner of the rectangle.

.value\[5\]?.f32: radius of the upper left corner of the rectangle.

.value\[6\]?.f32: radius of the lower left corner of the rectangle.

.value\[7\]?.f32: radius of the upper right corner of the rectangle.

.value\[8\]?.f32: radius of the lower right corner of the rectangle.

.object: coordinate offset of the rectangle. The parameter type is [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md). It takes effect when only the **.object** parameter is passed.

2\. Circle:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_CIRCLE**.

.value\[1\].f32: width of the circle.

.value\[2\].f32: height of the circle.

.object: coordinate offset of the circle. The parameter type is [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md). It takes effect when only the **.object** parameter is passed.

3\. Ellipse:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_ELLIPSE**.

.value\[1\].f32: width of the ellipse.

.value\[2\].f32: height of the ellipse.

.object: coordinate offset of the ellipse. The parameter type is [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md). It takes effect when only the **.object** parameter is passed.

4\. Path:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_PATH**.

.value\[1\].f32: width of the path.

.value\[2\].f32: height of the path.

.string: command for drawing the path.

.object: command for drawing the path. The parameter type is [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md). It takes effect when only the **.object** parameter is passed.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

1\. Rectangle:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_RECTANGLE**.

.value\[1\].f32: width of the rectangle.

.value\[2\].f32: height of the rectangle.

.value\[3\].f32: width of the rounded corner of the rectangle.

.value\[4\].f32: height of the rounded corner of the rectangle.

.value\[5\]?.f32: radius of the upper left corner of the rectangle.

.value\[6\]?.f32: radius of the lower left corner of the rectangle.

.value\[7\]?.f32: radius of the upper right corner of the rectangle.

.value\[8\]?.f32: radius of the lower right corner of the rectangle.

.value\[9\]?.f32: horizontal coordinate offset of the rectangle.

.value\[10\]?.f32: vertical coordinate offset of the rectangle.

2\. Circle:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_CIRCLE**.

.value\[1\].f32: width of the circle.

.value\[2\].f32: height of the circle.

.value\[3\]?.f32: horizontal coordinate offset of the circle.

.value\[4\]?.f32: vertical coordinate offset of the circle.

3\. Ellipse:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_ELLIPSE**.

.value\[1\].f32: width of the ellipse.

.value\[2\].f32: height of the ellipse.

.value\[3\]?.f32: horizontal coordinate offset of the ellipse.

.value\[4\]?.f32: vertical coordinate offset of the ellipse.

4\. Path:

.value\[0\].i32: type of shape. The parameter type is [ArkUI\_ClipType](../native-type-h/document.md#arkui_cliptype). The value is **ARKUI\_CLIP\_TYPE\_PATH**.

.value\[1\].f32: width of the path.

.value\[2\].f32: height of the path.

.string: command for drawing the path.

 |
| NODE\_TRANSFORM = 25 | 

Defines the transform attribute, which can be used to translate, rotate, and scale images. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0...15\].f32: 16 floating-point numbers.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0...15\].f32: 16 floating-point numbers.

 |
| NODE\_HIT\_TEST\_BEHAVIOR = 26 | 

Defines the hit test behavior attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: hit test mode. The parameter type is [ArkUI\_HitTestMode](../native-type-h/document.md#arkui_hittestmode). The default value is **ARKUI\_HIT\_TEST\_MODE\_DEFAULT**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: hit test mode. The parameter type is **ArkUI\_HitTestMode**. The default value is **ARKUI\_HIT\_TEST\_MODE\_DEFAULT**.

 |
| NODE\_POSITION = 27 | 

Defines the offset attribute, which specifies the offset of the component's upper left corner relative to the parent container's. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: x-coordinate.

.value\[1\].f32: y-coordinate.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: x-coordinate.

.value\[1\].f32: y-coordinate.

 |
| NODE\_SHADOW = 28 | 

Defines the shadow attribute. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: shadow effect. The parameter type is [ArkUI\_ShadowStyle](../native-type-h/document.md#arkui_shadowstyle).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: shadow effect. The parameter type is [ArkUI\_ShadowStyle](../native-type-h/document.md#arkui_shadowstyle).

 |
| NODE\_CUSTOM\_SHADOW = 29 | 

Defines the custom shadow effect. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.f32: blur radius of the shadow, in px.

.value\[1\]?.i32: whether to enable the coloring strategy. The value **1** means to enable the coloring strategy, and **0** (default value) means the opposite.

.value\[2\]?.f32: offset of the shadow along the x-axis, in px.

.value\[3\]?.f32: offset of the shadow along the y-axis, in px.

.value\[4\]?.i32: shadow type [ArkUI\_ShadowType](../native-type-h/document.md#arkui_shadowtype). The default value is **ARKUI\_SHADOW\_TYPE\_COLOR**.

.value\[5\]?.u32: shadow color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

.value\[6\]?.u32: whether to fill the shadow. The value **1** means to fill the shadow, and **0** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: blur radius of the shadow, in px.

.value\[1\].i32: whether the coloring strategy is enabled.

.value\[2\].f32: offset of the shadow along the x-axis, in px.

.value\[3\].f32: offset of the shadow along the y-axis, in px.

.value\[4\].i32: shadow type [ArkUI\_ShadowType](../native-type-h/document.md#arkui_shadowtype). The default value is **ARKUI\_SHADOW\_TYPE\_COLOR**.

.value\[5\].u32: shadow color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

.value\[6\].u32: whether the shadow is filled. The value **1** means that the shadow is filled, and **0** means the opposite.

 |
| NODE\_BACKGROUND\_IMAGE\_SIZE = 30 | 

Defines the background image width and height. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: width of the image. The value range is \[0, +∞), and the unit is vp.

.value\[1\].f32: height of the image. The value range is \[0, +∞), and the unit is vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: width of the image, in vp.

.value\[1\].f32: height of the image, in vp.

 |
| NODE\_BACKGROUND\_IMAGE\_SIZE\_WITH\_STYLE = 31 | 

Defines the background image size. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: size of the background image. The value is an enumerated value of [ArkUI\_ImageSize](../native-type-h/document.md#arkui_imagesize).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: size of the background image. The value is an enumerated value of [ArkUI\_ImageSize](../native-type-h/document.md#arkui_imagesize).

 |
| NODE\_BACKGROUND\_BLUR\_STYLE = 32 | 

Defines the background blur attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: blur type. The value is an enumerated value of [ArkUI\_BlurStyle](../native-type-h/document.md#arkui_blurstyle).

.value\[1\]?.i32: color mode, specified by an enumerated value of [ArkUI\_ColorMode](../native-type-h/document.md#arkui_colormode).

.value\[2\]?.i32: adaptive color mode, specified by an enumerated value of [ArkUI\_AdaptiveColor](../native-type-h/document.md#arkui_adaptivecolor).

.value\[3\]?.f32: blur degree. The value range is \[0.0, 1.0\].

.value\[4\]?.f32: start boundary of grayscale blur.

.value\[5\]?.f32: end boundary of grayscale blur.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: blur type. The value is an enumerated value of [ArkUI\_BlurStyle](../native-type-h/document.md#arkui_blurstyle).

.value\[1\].i32: color mode, specified by an enumerated value of [ArkUI\_ColorMode](../native-type-h/document.md#arkui_colormode).

.value\[2\].i32: adaptive color mode, specified by an enumerated value of [ArkUI\_AdaptiveColor](../native-type-h/document.md#arkui_adaptivecolor).

.value\[3\].f32: blur degree. The value range is \[0.0, 1.0\].

.value\[4\].f32: start boundary of grayscale blur.

.value\[5\].f32: end boundary of grayscale blur.

 |
| NODE\_TRANSFORM\_CENTER = 33 | 

Defines the transform center attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.f32: x-coordinate of the center point, in vp.

.value\[1\]?.f32: y-coordinate of the center point, in vp.

.value\[2\]?.f32: z-coordinate of the center point, in vp.

.value\[3\]?.f32: x-coordinate of the center point, expressed in a number that represents a percentage. For example, 0.2 indicates 20%. This attribute overwrites value\[0\].f32. The default value is **0.5f**.

.value\[4\]?.f32: y-coordinate of the center point, expressed in a number that represents a percentage. For example, 0.2 indicates 20%. This attribute overwrites value\[1\].f32. The default value is **0.5f**.

.value\[5\]?.f32: z-coordinate of the center point, expressed in a number that represents a percentage. For example, 0.2 indicates 20%. This attribute overwrites value\[2\].f32. The default value is **0.0f**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: x-coordinate of the center point, in vp.

.value\[1\].f32: y-coordinate of the center point, in vp.

.value\[2\].f32: z-coordinate of the center point, in vp.

Note: If the coordinate is expressed in a number that represents a percentage, the attribute obtaining API returns the calculated value in vp.

 |
| NODE\_OPACITY\_TRANSITION = 34 | 

Defines the transition opacity attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: opacity values of the start and end points.

.value\[1\].i32: animation duration, in ms.

.value\[2\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

.value\[3\]?.i32: animation delay duration, in ms.

.value\[4\]?.i32: number of times that the animation is played.

.value\[5\]?.i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

.value\[6\]?.f32: animation playback speed.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: opacity values of the start and end points.

.value\[1\].i32: animation duration, in ms.

.value\[2\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

.value\[3\].i32: animation delay duration, in ms.

.value\[4\].i32: number of times that the animation is played.

.value\[5\].i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

.value\[6\].f32: animation playback speed.

 |
| NODE\_ROTATE\_TRANSITION = 35 | 

Defines the transition rotation attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: x-component of the rotation vector.

.value\[1\].f32: y-component of the rotation vector.

.value\[2\].f32: z-component of the rotation vector

.value\[3\].f32: angle.

.value\[4\].f32: line of sight. The default value is **0.0f**.

.value\[5\].i32: animation duration, in ms.

.value\[6\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

.value\[7\]?.i32: animation delay duration, in ms.

.value\[8\]?.i32: number of times that the animation is played.

.value\[9\]?.i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

.value\[10\]?.f32: animation playback speed.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: x-component of the rotation vector.

.value\[1\].f32: y-component of the rotation vector.

.value\[2\].f32: z-component of the rotation vector

.value\[3\].f32: angle.

.value\[4\].f32: line of sight.

.value\[5\].i32: animation duration, in ms.

.value\[6\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

.value\[7\].i32: animation delay duration, in ms.

.value\[8\].i32: number of times that the animation is played.

.value\[9\].i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

.value\[10\].f32: animation playback speed.

 |
| NODE\_SCALE\_TRANSITION = 36 | 

Defines the transition scaling attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: scale factor along the X-axis.

.value\[1\].f32: scale factor along the Y-axis.

.value\[2\].f32: scale factor along the Z-axis.

value\[3\].i32: animation duration, in ms.

.value\[4\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

.value\[5\]?.i32: animation delay duration, in ms.

.value\[6\]?.i32: number of times that the animation is played.

.value\[7\]?.i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

value\[8\]?.f32: animation playback speed.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: scale factor along the X-axis.

.value\[1\].f32: scale factor along the Y-axis.

.value\[2\].f32: scale factor along the Z-axis.

value\[3\].i32: animation duration, in ms.

.value\[4\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

value\[5\].i32: animation delay duration, in ms.

value\[6\].i32: number of times that the animation is played.

.value\[7\].i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

value\[8\].f32: animation playback speed.

 |
| NODE\_TRANSLATE\_TRANSITION = 37 | 

Defines the transition translation attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

value\[0\].f32: translation distance along the x-axis, in vp. The default value is **0.0**.

value\[1\].f32: translation distance along the y-axis, in vp. The default value is **0.0**.

value\[2\].f32: translation distance along the z-axis, in vp. The default value is **0.0**.

value\[3\].i32: animation duration, in ms.

value\[4\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

value\[5\]?.i32: animation delay duration, in ms.

value\[6\]?.i32: number of times that the animation is played.

value\[7\]?.i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

value\[8\]?.f32: animation playback speed.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].f32: translation distance along the x-axis, in vp.

value\[1\].f32: translation distance along the y-axis, in vp.

value\[2\].f32: translation distance along the z-axis, in vp.

value\[3\].i32: animation duration, in ms.

value\[4\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

value\[5\].i32: animation delay duration, in ms.

value\[6\].i32: number of times that the animation is played.

value\[7\].i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

value\[8\].f32: animation playback speed.

 |
| NODE\_MOVE\_TRANSITION = 38 | 

Defines the slide-in and slide-out of the component from the screen edge during transition. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: [ArkUI\_TransitionEdge](../native-type-h/document.md#arkui_transitionedge) type.

.value\[1\].i32: animation duration, in ms.

.value\[2\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

.value\[3\]?.i32: animation delay duration, in ms.

.value\[4\]?.i32: number of times that the animation is played.

.value\[5\]?.i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

.value\[6\]?.f32: animation playback speed.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: [ArkUI\_TransitionEdge](../native-type-h/document.md#arkui_transitionedge) type.

.value\[1\].i32: animation duration, in ms.

.value\[2\].i32: animation curve type. The value is an enumerated value of [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve).

.value\[3\].i32: animation delay duration, in ms.

.value\[4\].i32: number of times that the animation is played.

.value\[5\].i32: animation playback mode. The value is an enumerated value of [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode).

.value\[6\].f32: animation playback speed.

 |
| NODE\_FOCUSABLE = 39 | 

Defines the focus attribute, which can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: The value **1** indicates focusable, and **0** indicates not focusable. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: The value **1** indicates focusable, and **0** indicates not focusable.

 |
| NODE\_DEFAULT\_FOCUS = 40 | 

Defines the default focus attribute, which can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

value\[0\].i32: The value **1** indicates that the target is the default focus, and **0** indicates that it is not the default focus.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].i32: The value **1** indicates that the target is the default focus, and **0** indicates that it is not the default focus.

 |
| NODE\_RESPONSE\_REGION = 41 | 

Defines the touch target attribute, which can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.data\[0\].f32: X coordinate of the touch point relative to the upper left corner of the component, in vp.

.data\[1\].f32: Y coordinate of the touch point relative to the upper left corner of the component, in vp.

.data\[2\].f32: width of the touch target, in percentage.

.data\[3\].f32: height of the touch target, in percentage.

.data\[4...\].f32: Multiple touch targets can be set. The sequence of the parameters is the same as the preceding.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.data\[0\].f32: X coordinate of the touch point relative to the upper left corner of the component, in vp.

.data\[1\].f32: Y coordinate of the touch point relative to the upper left corner of the component, in vp.

.data\[2\].f32: width of the touch target, in percentage.

.data\[3\].f32: height of the touch target, in percentage.

.data\[4...\].f32: Multiple touch targets can be set. The sequence of the parameters is the same as the preceding.

Note: During configuration, the data array can contain any number of values (all will be accepted), but only the first 20 values can be retrieved.

 |
| NODE\_OVERLAY = 42 | 

Defines the overlay attribute. This attribute can be set, reset, and obtained as required through APIs. You can set the overlay content through .string or .object, with .string having higher priority. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: mask text.

.value\[0\]?.i32: position of the overlay relative to the component. Optional. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment). The default value is **ARKUI\_ALIGNMENT\_TOP\_START**.

.value\[1\]?.f32: offset of the overlay relative to the upper left corner of itself on the x-axis, in vp. Optional. The default value is **0** vp.

.value\[2\]? .f32: offset of the overlay relative to the upper left corner of itself on the y-axis, in vp. Optional. The default value is **0** vp.

.value\[3\]?.i32: layout direction of the overlay. Optional. The parameter type is [ArkUI\_Direction](../native-type-h/document.md#arkui_direction). The default value is **ARKUI\_DIRECTION\_LTR**.

In most scenarios, this parameter should be set to **Auto**, which allows the system to automatically handle the layout direction. If specific directions need to be maintained in certain scenarios, set this parameter to **LTR** (left-to-right) or **RTL** (right-to-left). It is supported since API version 21.

.object: node tree used for overlay. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md), and the default value is **nullptr**. It is supported since API version 21.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: mask text.

.value\[0\].i32: position of the overlay relative to the component. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment). The default value is **ARKUI\_ALIGNMENT\_TOP\_START**.

.value\[1\].f32: offset of the overlay relative to the upper left corner of itself on the x-axis, in vp.

.value\[2\].f32: offset of the overlay relative to the upper left corner of itself on the y-axis, in vp.

.value\[3\].i32: layout direction of the overlay. The parameter type is [ArkUI\_Direction](../native-type-h/document.md#arkui_direction). The default value is **ARKUI\_DIRECTION\_LTR**. It is supported since API version 21.

.object: node tree used for overlay. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md). It is supported since API version 21.

 |
| NODE\_SWEEP\_GRADIENT = 43 | 

Defines the sweep gradient effect. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.f32: x-coordinate of the sweep gradient center relative to the upper left corner of the component.

.value\[1\]?.f32: y-coordinate of the sweep gradient center relative to the upper left corner of the component.

.value\[2\]?.f32: start point of the sweep gradient. The default value is **0**.

.value\[3\]?.f32: end point of the sweep gradient. The default value is **0**.

.value\[4\]?.f32: rotation angle of the sweep gradient. The default value is **0**.

.value\[5\]?.i32: whether the colors are repeated. The value **1** means that the colors are repeated, and **0** means the opposite.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops.

**stops**: stop positions of the color stops.

**size**: number of colors.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: x-coordinate of the sweep gradient center relative to the upper left corner of the component.

.value\[1\].f32: y-coordinate of the sweep gradient center relative to the upper left corner of the component.

.value\[2\].f32: start point of the sweep gradient. The default value is **0**.

.value\[3\].f32: end point of the sweep gradient. The default value is **0**.

.value\[4\].f32: rotation angle of the sweep gradient. The default value is **0**.

.value\[5\].i32: whether the colors are repeated. The value **1** means that the colors are repeated, and **0** means the opposite.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops.

**stops**: stop positions of the color stops.

**size**: number of colors.

 |
| NODE\_RADIAL\_GRADIENT = 44 | 

Defines the radial gradient effect. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.f32: x-coordinate of the radial gradient center relative to the upper left corner of the component.

.value\[1\]?.f32: y-coordinate of the radial gradient center relative to the upper left corner of the component.

.value\[2\]?.f32: radius of the radial gradient. The default value is **0**.

.value\[3\]?.i32: whether the colors are repeated. The value **1** means that the colors are repeated, and **0** means the opposite.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops.

**stops**: stop positions of the color stops.

**size**: number of colors.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: x-coordinate of the radial gradient center relative to the upper left corner of the component.

.value\[1\].f32: y-coordinate of the radial gradient center relative to the upper left corner of the component.

.value\[2\].f32: radius of the radial gradient. The default value is **0**.

.value\[3\].i32: whether the colors are repeated. The value **1** means that the colors are repeated, and **0** means the opposite.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops.

**stops**: stop positions of the color stops.

**size**: number of colors.

 |
| NODE\_MASK = 45 | 

Adds a mask of the specified shape to the component. This attribute can be set and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1\. Rectangle:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type. The parameter type is [ArkUI\_MaskType](../native-type-h/document.md#arkui_masktype). The value is **ARKUI\_MASK\_TYPE\_RECTANGLE**.

.value\[4\].f32: width of the rectangle, in vp.

.value\[5\].f32: height of the rectangle, in vp.

.value\[6\].f32: corner radius width of the rectangle, in vp.

.value\[7\].f32: corner radius height of the rectangle, in vp.

.value\[8\]?.f32: radius of the upper left corner of the rectangle, in vp.

.value\[9\]?.f32: radius of the lower left corner of the rectangle, in vp.

.value\[10\]?.f32: radius of the upper right corner of the rectangle, in vp.

.value\[11\]?.f32: radius of the lower right corner of the rectangle, in vp.

2\. Circle:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type. The parameter type is [ArkUI\_MaskType](../native-type-h/document.md#arkui_masktype). The value is **ARKUI\_MASK\_TYPE\_CIRCLE**.

.value\[4\].f32: width of the circle, in vp.

.value\[5\].f32: height of the circle, in vp.

3\. Ellipse:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type. The parameter type is [ArkUI\_MaskType](../native-type-h/document.md#arkui_masktype). The value is **ARKUI\_MASK\_TYPE\_ELLIPSE**.

.value\[4\].f32: width of the ellipse, in vp.

.value\[5\].f32: height of the ellipse, in vp.

4\. Path:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type. The parameter type is [ArkUI\_MaskType](../native-type-h/document.md#arkui_masktype). The value is **ARKUI\_MASK\_TYPE\_PATH**.

.value\[4\].f32: width of the path, in vp.

.value\[5\].f32: height of the path, in vp.

.string: command for drawing the path.

5\. Progress:

.value\[0\].i32: mask type. The parameter type is [ArkUI\_MaskType](../native-type-h/document.md#arkui_masktype). The value is **ARKUI\_MASK\_TYPE\_PROGRESS**.

.value\[1\].f32: current value of the progress indicator.

.value\[2\].f32: maximum value of the progress indicator.

.value\[3\].u32: color of the progress indicator.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

1\. Rectangle:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type.

.value\[4\].f32: width of the rectangle, in vp.

.value\[5\].f32: height of the rectangle, in vp.

.value\[6\].f32: corner radius width of the rectangle, in vp.

.value\[7\].f32: corner radius height of the rectangle, in vp.

.value\[8\]?.f32: radius of the upper left corner of the rectangle, in vp.

.value\[9\]?.f32: radius of the lower left corner of the rectangle, in vp.

.value\[10\]?.f32: radius of the upper right corner of the rectangle, in vp.

.value\[11\]?.f32: radius of the lower right corner of the rectangle, in vp.

2\. Circle:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type.

.value\[4\].f32: width of the circle, in vp.

.value\[5\].f32: height of the circle, in vp.

3\. Ellipse:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type.

.value\[4\].f32: width of the ellipse, in vp.

.value\[5\].f32: height of the ellipse, in vp.

4\. Path:

.value\[0\].u32: fill color, in 0xARGB format.

.value\[1\].u32: stroke color, in 0xARGB format.

.value\[2\].f32: stroke width, in vp.

.value\[3\].i32: mask type.

.value\[4\].f32: width of the path, in vp.

.value\[5\].f32: height of the path, in vp.

.string: command for drawing the path.

5\. Progress:

.value\[0\].i32: mask type.

.value\[1\].f32: current value of the progress indicator.

.value\[2\].f32: maximum value of the progress indicator.

.value\[3\].u32: color of the progress indicator.

 |
| NODE\_BLEND\_MODE = 46 | 

Blends the component's background with the content of the component's child node. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: blend mode. The parameter type is [ArkUI\_BlendMode](../native-type-h/document.md#arkui_blendmode). The default value is **ARKUI\_BLEND\_MODE\_NONE**.

.value\[1\].?i32: how the specified blend mode is applied. The parameter type is [ArkUI\_BlendApplyType](../native-type-h/document.md#arkui_blendapplytype). The default value is **BLEND\_APPLY\_TYPE\_FAST**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: blend mode. The parameter type is [ArkUI\_BlendMode](../native-type-h/document.md#arkui_blendmode). The default value is **ARKUI\_BLEND\_MODE\_NONE**.

.value\[1\].i32: how the specified blend mode is applied. The parameter type is [ArkUI\_BlendApplyType](../native-type-h/document.md#arkui_blendapplytype). The default value is **BLEND\_APPLY\_TYPE\_FAST**.

 |
| NODE\_DIRECTION = 47 | 

Sets the direction of the main axis. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: direction of the main axis.

The parameter type is [ArkUI\_Direction](../native-type-h/document.md#arkui_direction). The default value is **ARKUI\_DIRECTION\_AUTO**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: direction of the main axis.

The parameter type is [ArkUI\_Direction](../native-type-h/document.md#arkui_direction). The default value is **ARKUI\_DIRECTION\_AUTO**.

 |
| NODE\_CONSTRAINT\_SIZE = 48 | 

Defines the size constraints. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum width, in vp.

.value\[1\].f32: maximum width, in vp.

.value\[2\].f32: minimum height, in vp.

.value\[3\].f32: maximum height, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum width, in vp.

.value\[1\].f32: maximum width, in vp.

.value\[2\].f32: minimum height, in vp.

.value\[3\].f32: maximum height, in vp.

 |
| NODE\_GRAY\_SCALE = 49 | 

Defines the grayscale effect. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: grayscale conversion ratio. The value ranges from 0 to 1. The default value is **0**. For example, **0.5** indicates a 50% grayscale conversion ratio.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: grayscale conversion ratio. The value ranges from 0 to 1.

 |
| NODE\_INVERT = 50 | 

Inverts the image. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: image inversion ratio. The value ranges from 0 to 1. The default value is **0**. For example, **0.5** indicates a 50% image inversion ratio.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: image inversion ratio. The value ranges from 0 to 1.

 |
| NODE\_SEPIA = 51 | 

Defines the sepia conversion ratio. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: sepia conversion ratio. The value ranges from 0 to 1. The default value is **0**. For example, **0.5** indicates that a 50% sepia conversion ratio.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: sepia conversion ratio. The value ranges from 0 to 1.

 |
| NODE\_CONTRAST = 52 | 

Defines the contrast attribute. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: contrast. If the value is **1**, the source image is displayed. A larger value indicates a higher contrast. The default value is **1**. The value range is \[0, 10).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: contrast. Value range: \[0, 10).

 |
| NODE\_FOREGROUND\_COLOR = 53 | 

Sets the foreground color attribute. This attribute can be set and reset as required through APIs. However, the reset API has no effect on this attribute.

There are two parameter formats of [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) for setting the attribute:

1: .value\[0\].u32: color value, in 0xARGB format. For example, **0xFFFF0000** indicates red. The default value is **0xFF000000**.

2: .value\[0\].i32: color enum **ArkUI\_ColoringStrategy**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value, in 0xARGB format.

 |
| NODE\_OFFSET = 54 | 

Defines the offset of the component's child relative to the component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32 : offset along the x-axis, in vp.

.value\[1\].f32 : offset along the y-axis, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32 : offset along the x-axis, in vp.

.value\[1\].f32 : offset along the y-axis, in vp.

 |
| NODE\_MARK\_ANCHOR = 55 | 

Sets the anchor for locating the component's child. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: x-coordinate of the anchor, in vp.

.value\[1\].f32: y-coordinate of the anchor, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: x-coordinate of the anchor, in vp.

.value\[1\].f32: y-coordinate of the anchor, in vp.

 |
| NODE\_BACKGROUND\_IMAGE\_POSITION = 56 | 

Defines the position of the background image in the component, that is, the coordinates relative to the upper left corner of the component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: position along the x-axis, in px.

.value\[1\].f32: position along the y-axis, in px.

.value\[2\].?i32: alignment mode. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment). The default value is **ARKUI\_ALIGNMENT\_TOP\_START**. **Since**: 12

.value\[3\].?i32: layout direction. The parameter type is [ArkUI\_Direction](../native-type-h/document.md#arkui_direction). The default value is **ARKUI\_DIRECTION\_AUTO**. **Since**: 12

In most scenarios, this parameter should be set to **AUTO**, which allows the system to automatically handle the layout direction. If specific directions need to be maintained in certain scenarios, set this parameter to **LTR** (left-to-right) or **RTL** (right-to-left).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: position along the x-axis, in px.

.value\[1\].f32: position along the y-axis, in px.

.value\[2\].?i32: alignment mode. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment). The default value is **ARKUI\_ALIGNMENT\_TOP\_START**. **Since**: 12

.value\[3\].i32: layout direction. The parameter type is [ArkUI\_Direction](../native-type-h/document.md#arkui_direction). The default value is **ARKUI\_DIRECTION\_AUTO**. **Since**: 12

 |
| NODE\_ALIGN\_RULES = 57 | 

Sets the alignment rules in the relative container. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md) object that defines the alignment rules.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md) object that defines the alignment rules.

 |
| NODE\_ALIGN\_SELF = 58 | 

Sets the alignment mode of the child components along the cross axis of the parent container. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: alignment mode of the child components along the cross axis of the parent container.

The parameter type is [ArkUI\_ItemAlignment](../native-type-h/document.md#arkui_itemalignment). The default value is **ARKUI\_ITEM\_ALIGNMENT\_AUTO**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: alignment mode of the child components along the cross axis of the parent container.

The parameter type is [ArkUI\_ItemAlignment](../native-type-h/document.md#arkui_itemalignment). The default value is **ARKUI\_ITEM\_ALIGNMENT\_AUTO**.

 |
| NODE\_FLEX\_GROW = 59 | 

Sets the percentage of the parent container's remaining space that is allocated to the component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: percentage of the parent container's remaining space that is allocated to the component.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: percentage of the parent container's remaining space that is allocated to the component.

 |
| NODE\_FLEX\_SHRINK = 60 | 

Sets the percentage of the parent container's shrink size that is allocated to the component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: percentage of the parent container's shrink size that is allocated to the component.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: percentage of the parent container's shrink size that is allocated to the component.

 |
| NODE\_FLEX\_BASIS = 61 | 

Sets the base size of the component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: base size of the component on the main axis of the parent container.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: base size of the component on the main axis of the parent container.

 |
| NODE\_ACCESSIBILITY\_GROUP = 62 | 

Sets the accessibility group. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: Accessibility group. The value **1** means that the component and all its child components form an entire selectable component. In this case, the accessibility service will no longer be available for the content of its child components. The value is **1** or **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: Accessibility group. The value **1** means that the component and all its child components form an entire selectable component. In this case, the accessibility service will no longer be available for the content of its child components. The value is **1** or **0**.

 |
| NODE\_ACCESSIBILITY\_TEXT = 63 | 

Sets the accessibility text. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: accessibility text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: accessibility text.

 |
| NODE\_ACCESSIBILITY\_MODE = 64 | 

Defines the accessibility mode. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: accessibility mode. The parameter type is [ArkUI\_AccessibilityMode](../native-type-h/document.md#arkui_accessibilitymode).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: accessibility mode. The parameter type is [ArkUI\_AccessibilityMode](../native-type-h/document.md#arkui_accessibilitymode).

 |
| NODE\_ACCESSIBILITY\_DESCRIPTION = 65 | 

Sets the accessibility description. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: accessibility description.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: accessibility description.

 |
| NODE\_FOCUS\_STATUS = 66 | 

Defines the component focus status. This attribute can be set and obtained as required through APIs.

Note: Setting the parameter to **0** shifts focus from the currently focused component on the current level of the page to the root container.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: The value **1** indicates that the component gains focus and **0** indicates that the component loses focus.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: The value **1** indicates that the component gains focus and **0** indicates that the component loses focus.

 |
| NODE\_ASPECT\_RATIO = 67 | 

Defines the aspect ratio attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: aspect ratio of the component, in width/height format.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: aspect ratio of the component, in width/height format.

 |
| NODE\_LAYOUT\_WEIGHT = 68 | 

Defines the weight of the component within its row, column, or flex container for proportional distribution of available space within the container. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: weight of the component along the main axis.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: weight of the component along the main axis.

 |
| NODE\_DISPLAY\_PRIORITY = 69 | 

Sets the display priority for the component in the row, column, or flex (single-line) container. When the **displayPriority** value of a child component is greater than 1, a larger value indicates higher priority. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: display priority of the component in the container.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: display priority of the component in the container.

 |
| NODE\_OUTLINE\_WIDTH = 70 | 

Sets the thickness of an element's outline.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: thickness of the left outline.

.value\[1\].f32: thickness of the top outline.

.value\[2\].f32: thickness of the right outline.

.value\[3\].f32: thickness of the bottom outline.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: thickness of the left outline.

.value\[1\].f32: thickness of the top outline.

.value\[2\].f32: thickness of the right outline.

.value\[3\].f32: thickness of the bottom outline.

 |
| NODE\_WIDTH\_PERCENT = 71 | 

Defines the width attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: width, in percentage.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: width, in percentage.

 |
| NODE\_HEIGHT\_PERCENT = 72 | 

Defines the height attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: height, in percentage.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: height, in percentage.

 |
| NODE\_PADDING\_PERCENT = 73 | 

Defines the padding attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: Specify the same padding for the four directions.

.value\[0\].f32: padding, in percentage.

2: Specify different paddings for different directions.

.value\[0\].f32: top padding, in percentage.

.value\[1\].f32: right padding, in percentage.

.value\[2\].f32: bottom padding, in percentage.

.value\[3\].f32: left padding, in percentage.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: top padding, in percentage.

.value\[1\].f32: right padding, in percentage.

.value\[2\].f32: bottom padding, in percentage.

.value\[3\].f32: left padding, in percentage.

 |
| NODE\_MARGIN\_PERCENT = 74 | 

Defines the margin attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: Specify the same margin for the four directions.

.value\[0\].f32: margin, in percentage.

2: Specify different margins for different directions.

.value\[0\].f32: top margin, in percentage.

.value\[1\].f32: right margin, in percentage.

.value\[2\].f32: bottom margin, in percentage.

.value\[3\].f32: left margin, in percentage.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: top margin, in percentage.

.value\[1\].f32: right margin, in percentage.

.value\[2\].f32: bottom margin, in percentage.

.value\[3\].f32: left margin, in percentage.

 |
| NODE\_GEOMETRY\_TRANSITION = 75 | 

Implements an implicit shared element transition. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: two components bound to the shared element. The parameter type is 1 or 0. By default, the out component does not continue to participate in the shared element animation when not yet deleted, which means that it stays in its original position.

.string: ID used to set up a binding relationship. If this attribute is set to an empty string **""**, the binding relationship is cleared. The value can be dynamically changed to refresh the binding relationship. One ID can be bound to only two components, which function as in and out components.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: two components bound to the shared element. The parameter type is 1 or 0. By default, the out component does not continue to participate in the shared element animation when not yet deleted, which means that it stays in its original position.

.string: ID used to set up a binding relationship. If this attribute is set to an empty string **""**, the binding relationship is cleared. The value can be dynamically changed to refresh the binding relationship. One ID can be bound to only two components, which function as in and out components.

 |
| NODE\_RELATIVE\_LAYOUT\_CHAIN\_MODE = 76 | 

Sets the parameters of the chain in which the component is the head. This attribute can be set, reset, and obtained as required through APIs. This attribute has effect only when the parent container is **RelativeContainer**.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: direction of the chain. The value is an enumerated value of [ArkUI\_Axis](../native-type-h/document.md#arkui_axis).

.value\[1\].i32: style of the chain. The value is an enumerated value of [ArkUI\_RelativeLayoutChainStyle](../native-type-h/document.md#arkui_relativelayoutchainstyle).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: direction of the chain. The value is an enumerated value of [ArkUI\_Axis](../native-type-h/document.md#arkui_axis).

.value\[1\].i32: style of the chain. The value is an enumerated value of [ArkUI\_RelativeLayoutChainStyle](../native-type-h/document.md#arkui_relativelayoutchainstyle).

 |
| NODE\_RENDER\_FIT = 77 | 

Sets how the final state of the component's content is rendered during its width and height animation process. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: how the final state of the component's content is rendered. The value is an enumerated value of [ArkUI\_RenderFit](../native-type-h/document.md#arkui_renderfit).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: how the final state of the component's content is rendered. The value is an enumerated value of [ArkUI\_RenderFit](../native-type-h/document.md#arkui_renderfit).

 |
| NODE\_OUTLINE\_COLOR = 78 | 

Defines the border color attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: .value\[0\].u32: color of the four borders, in 0xARGB format, for example, **0xFFFF11FF**.

2: .value\[0\].u32: color of the top border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[1\].u32: color of the right border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[2\].u32: color of the lower border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[3\].u32: color of the left border, in 0xARGB format, for example, **0xFFFF11FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the top border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[1\].u32: color of the right border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[2\].u32: color of the lower border, in 0xARGB format, for example, **0xFFFF11FF**.

.value\[3\].u32: color of the left border, in 0xARGB format, for example, **0xFFFF11FF**.

 |
| NODE\_SIZE = 79 | 

Sets the size. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: width, in vp.

.value\[1\].f32: height, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: width, in vp.

.value\[1\].f32: height, in vp.

 |
| NODE\_RENDER\_GROUP = 80 | 

Sets whether the component and its child components are rendered off the screen and then drawn together with its parent. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the component and its child components are rendered off the screen and then drawn together with its parent. The value **1** means that the component and its child components are rendered off the screen and then drawn together with its parent, and **0** means the opposite. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the component and its child components are rendered off the screen and then drawn together with its parent. The value **1** means that the component and its child components are rendered off the screen and then drawn together with its parent, and **0** means the opposite.

 |
| NODE\_COLOR\_BLEND = 81 | 

Applies a color blend effect to the component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color to blend with the component, in 0xARGB format. The default value is **0x00000000**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color to blend with the component, in 0xARGB format, for example, **0xFFFF11FF**.

 |
| NODE\_FOREGROUND\_BLUR\_STYLE = 82 | 

Applies a foreground blur style to the component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: foreground blur style. The value is an enumerated value of [ArkUI\_BlurStyle](../native-type-h/document.md#arkui_blurstyle).

.value\[1\]?.i32: color mode used for the foreground blur. The value is an enumerated value of [ArkUI\_ColorMode](../native-type-h/document.md#arkui_colormode).

.value\[2\]?.i32: adaptive color mode used for the foreground blur. The value is an enumerated value of [ArkUI\_AdaptiveColor](../native-type-h/document.md#arkui_adaptivecolor).

.value\[3\]?.f32: blur degree. The value range is \[0.0, 1.0\].

.value\[4\]?.i32: brightness of black in the grayscale blur. The value range is \[0, 127\].

.value\[5\]?.i32: degree of darkening the white color in the grayscale blur. The value range is \[0, 127\].

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: foreground blur style. The value is an enumerated value of [ArkUI\_BlurStyle](../native-type-h/document.md#arkui_blurstyle).

.value\[1\].i32: color mode used for the foreground blur. The value is an enumerated value of [ArkUI\_ColorMode](../native-type-h/document.md#arkui_colormode).

.value\[2\].i32: adaptive color mode used for the foreground blur. The value is an enumerated value of [ArkUI\_AdaptiveColor](../native-type-h/document.md#arkui_adaptivecolor).

.value\[3\].f32: blur degree. The value range is \[0.0, 1.0\].

.value\[4\].i32: brightness of black in the grayscale blur. The value range is \[0, 127\].

.value\[5\].i32: degree of darkening the white color in the grayscale blur. The value range is \[0, 127\].

 |
| NODE\_LAYOUT\_RECT = 83 | 

Defines the component size and position for layout. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: X coordinate of the component, in px.

.value\[1\].i32: Y coordinate of the component, in px.

.value\[2\].i32: width of the component, in px.

.value\[3\].i32: height of the component, in px.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: X coordinate of the component, in px.

.value\[1\].i32: Y coordinate of the component, in px.

.value\[2\].i32: width of the component, in px.

.value\[3\].i32: height of the component, in px.

 |
| NODE\_FOCUS\_ON\_TOUCH = 84 | 

Sets whether the component is focusable on touch. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the component is focusable on touch. The value **1** means that the component is focusable on touch, and **0** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the component is focusable on touch. The value **1** means that the component is focusable on touch, and **0** means the opposite.

 |
| NODE\_BORDER\_WIDTH\_PERCENT = 85 | 

Defines the border width attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: .value\[0\].f32: width of the four borders, in percentage.

2: .value\[0\].f32: width of the top border, in percentage.

.value\[1\].f32: width of the right border, in percentage.

.value\[2\].f32: width of the bottom border, in percentage.

.value\[3\].f32: width of the left border, in percentage.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: width of the top border, in percentage.

.value\[1\].f32: width of the right border, in percentage.

.value\[2\].f32: width of the bottom border, in percentage.

.value\[3\].f32: width of the left border, in percentage.

 |
| NODE\_BORDER\_RADIUS\_PERCENT = 86 | 

Defines the border corner radius attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

1: .value\[0\].f32: radius of the four corners, in percentage.

2: .value\[0\].f32: radius of the upper left corner, in percentage.

.value\[1\].f32: radius of the upper right corner, in percentage.

.value\[2\].f32: radius of the lower left corner, in percentage.

.value\[3\].f32: radius of the lower right corner, in percentage.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: radius of the upper left corner, in percentage.

.value\[1\].f32: radius of the upper right corner, in percentage.

.value\[2\].f32: radius of the lower left corner, in percentage.

.value\[3\].f32: radius of the lower right corner, in percentage.

 |
| NODE\_ACCESSIBILITY\_ID = 87 | 

Sets the custom accessibility ID. This attribute can be obtained. Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: custom accessibility ID.

 |
| NODE\_ACCESSIBILITY\_ACTIONS = 88 | 

Sets the accessibility action type. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: accessibility action type. The parameter type is [ArkUI\_AccessibilityActionType](../native-type-h/document.md#arkui_accessibilityactiontype).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: accessibility action type. The parameter type is [ArkUI\_AccessibilityActionType](../native-type-h/document.md#arkui_accessibilityactiontype).

 |
| NODE\_ACCESSIBILITY\_ROLE = 89 | 

Defines the accessibility component role. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: accessibility component role. The parameter type is [ArkUI\_NodeType](#arkui_nodetype).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: accessibility component role. The parameter type is [ArkUI\_NodeType](#arkui_nodetype).

 |
| NODE\_ACCESSIBILITY\_STATE = 90 | 

Sets the accessibility state. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: accessibility state. The parameter type is [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: accessibility state. The parameter type is [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md).

 |
| NODE\_ACCESSIBILITY\_VALUE = 91 | 

Sets the accessibility value. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: accessibility value. The parameter type is [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: accessibility value. The parameter type is [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md).

 |
| NODE\_EXPAND\_SAFE\_AREA = 92 | 

Sets the safe area to be expanded to. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.u32: types of the expanded safe area, which are enumerated values of [ArkUI\_SafeAreaType](../native-type-h/document.md#arkui_safeareatype). Example: ARKUI\_SAFE\_AREA\_TYPE\_SYSTEM | ARKUI\_SAFE\_AREA\_TYPE\_CUTOUT.

.value\[1\]?.u32: edges for expanding the safe area, which are enumerated values of [ArkUI\_SafeAreaEdge](../native-type-h/document.md#arkui_safeareaedge). Example: ARKUI\_SAFE\_AREA\_EDGE\_TOP | ARKUI\_SAFE\_AREA\_EDGE\_BOTTOM.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: expanded safe area.

.value\[1\].u32: edges for expanding the safe area.

 |
| NODE\_VISIBLE\_AREA\_CHANGE\_RATIO = 93 | 

Defines the visible area ratio (visible area/total area of the component) threshold for invoking the visible area change event of the component. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[...\].f32: threshold array. The value ranges from 0 to 1.

.object: The parameter type is [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md).

**Since**: 22

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[...\].f32: threshold array.

.object: The return type is [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md).

**Since**: 22

 |
| NODE\_TRANSITION = 94 | 

Sets the transition effect when the component is inserted or deleted. This attribute can be set and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: transition effect. The parameter type is [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: transition effect. The parameter type is [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md).

 |
| NODE\_UNIQUE\_ID(deprecated) = 95 | 

Defines the component ID. This attribute can be obtained through APIs.

The component ID is read-only and unique in a process.

This API is sudpported since API version 12 and deprecated since API version 20. You are advised to use [OH\_ArkUI\_NodeUtils\_GetNodeUniqueId](#oh_arkui_nodeutils_getnodeuniqueid) instead.

 |
| NODE\_FOCUS\_BOX = 96 | 

Sets the style of the system focus box for this component.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: distance between the focus box and the edge of the component

A positive number indicates the outside, and a negative number indicates the inside.

The value cannot be in percentage.

.value\[1\].f32: width of the focus box. Negative numbers and percentages are not supported.

.value\[2\].u32: color of the focus box.

 |
| NODE\_CLICK\_DISTANCE = 97 | 

Defines the moving distance limit for the component-bound tap gesture. This attribute can be set as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: allowed moving distance of a finger, in vp.

 |
| NODE\_TAB\_STOP = 98 | 

Sets whether the focus can be placed on this component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the focus can be placed on the current component. The value **1** means that the focus can be placed on the current component, and **0** means the opposite. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the focus can be placed on the current component. The value **1** means that the focus can be placed on the current component, and **0** means the opposite.

**Since**: 14

 |
| NODE\_BACKDROP\_BLUR = 99 | 

Sets the background blur effect. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: background blur radius. The value range is \[0, +∞). The unit is px. The default value is **0.0**.

.value\[1\]?.f32: brightness of black in the grayscale blur. The value range is \[0, 127\].

.value\[2\]?.f32: degree of darkening the white color in the grayscale blur. The value range is \[0, 127\].

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: background blur radius. The value range is \[0, +∞). The unit is px.

.value\[1\].f32: brightness of black in the grayscale blur. The value range is \[0, 127\].

.value\[2\].f32: degree of darkening the white color in the grayscale blur. The value range is \[0, 127\].

**Since**: 15

 |
| NODE\_BACKGROUND\_IMAGE\_RESIZABLE\_WITH\_SLICE = 100 | 

Sets the resizable attribute of a background image when it is stretched. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: pixel value of the image that remains unchanged when the left side of the image is stretched, in vp.

.value\[1\].f32: pixel value of the image that remains unchanged when the top side of the image is stretched, in vp.

.value\[2\].f32: pixel value of the image that remains unchanged when the right side of the image is stretched, in vp.

.value\[3\].f32: pixel value of the image that remains unchanged when the bottom side of the image is stretched, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: pixel value of the image that remains unchanged when the left side of the image is stretched, in vp.

.value\[1\].f32: pixel value of the image that remains unchanged when the top side of the image is stretched, in vp.

.value\[2\].f32: pixel value of the image that remains unchanged when the right side of the image is stretched, in vp.

.value\[3\].f32: pixel value of the image that remains unchanged when the bottom side of the image is stretched, in vp.

**Since**: 19

 |
| NODE\_NEXT\_FOCUS = 101 | 

Sets the next focus node. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: focus movement direction, as defined in [ArkUI\_FocusMove](../native-type-h/document.md#arkui_focusmove). .object: next focus node. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md).

**Since**: 18

 |
| NODE\_VISIBLE\_AREA\_APPROXIMATE\_CHANGE\_RATIO = 102 | 

Sets the threshold ratio for triggering a visible area change event.

Note: The visible area change callback is not a real-time callback. The actual callback interval may differ from the expected interval due to system load and other factors. The interval between two visible area change callbacks will not be less than the expected update interval. If the provided expected interval is too short, the actual callback interval will be determined by the system load. By default, the interval threshold of the visible area change callback includes 0. This means that, if the provided threshold is \[0.5\], the effective threshold will be \[0.0, 0.5\].

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: parameters for visible area change events. The parameter type is [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: parameters for visible area change events. The parameter type is [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md).

**Since**: 17

 |
| NODE\_TRANSLATE\_WITH\_PERCENT = 103 | 

Sets component translation, with support for percentage-based translation parameters. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: translation distance along the x-axis. The default unit is percentage, unless **value\[3\]** exists and is **0** (then the unit is vp). The default value is **0**.

.value\[1\].f32: translation distance along the y-axis. The default unit is percentage, unless **value\[4\]** exists and is **0** (then the unit is vp). The default value is **0**.

.value\[2\].f32: distance to translate along the z-axis, in vp. The default value is **0**.

.value\[3\]?.i32: whether the x-axis movement distance is in percentage format. Valid values: 0 or 1. The value **1** means percentage format (for example, value\[0\].f32=0.1 and value\[3\].i32=1 translates 10% along the x-axis). The default value is **1**.

.value\[4\]?.i32: whether the y-axis movement distance is in percentage. Valid values: 0 or 1. The value **1** means percentage format (for example, value\[1\].f32=0.1 and value\[4\].i32=1 translates 10% along the y-axis). The default value is **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: translation distance along the X-axis. The unit depends on **value\[3\]**.

.value\[1\].f32: translation distance along the y-axis. The unit depends on **value\[4\]**.

.value\[2\].f32: translation distance along the z-axis, in vp.

.value\[3\].i32: whether the unit of x-axis movement distance is percentage. When **value\[3\].i32** is **0**, the unit of x-axis movement distance is vp; when **value\[3\].i32** is **1**, the unit is percentage.

.value\[4\].i32: whether the unit of y-axis movement distance is percentage. When **value\[4\].i32** is **0**, the unit of y-axis movement distance is vp; when **value\[4\].i32** is **1**, the unit is percentage.

**Since**: 20

 |
| NODE\_ROTATE\_ANGLE = 104 | 

Sets component rotation with multi-axis angle control. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: x-axis rotation angle. The default value is **0**.

.value\[1\].f32: y-axis rotation angle. The default value is **0**.

.value\[2\].f32: z-axis rotation angle. The default value is **0**.

.value\[3\].f32: perspective distance from the viewpoint to the z=0 plane, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: x-axis rotation angle. The default value is **0**.

.value\[1\].f32: y-axis rotation angle. The default value is **0**.

.value\[2\].f32: z-axis rotation angle. The default value is **0**.

.value\[3\].f32: perspective distance from the viewpoint to the z=0 plane, in vp. The default value is **0**.

**Since**: 20

 |
| NODE\_WIDTH\_LAYOUTPOLICY = 105 | 

Sets the width layout policy of a component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: layout policy. The parameter type is [ArkUI\_LayoutPolicy](../native-type-h/document.md#arkui_layoutpolicy).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: layout policy. The parameter type is [ArkUI\_LayoutPolicy](../native-type-h/document.md#arkui_layoutpolicy).

**Since**: 21

 |
| NODE\_HEIGHT\_LAYOUTPOLICY = 106 | 

Sets the height layout policy of a component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: layout policy. The parameter type is [ArkUI\_LayoutPolicy](../native-type-h/document.md#arkui_layoutpolicy).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: layout policy. The parameter type is [ArkUI\_LayoutPolicy](../native-type-h/document.md#arkui_layoutpolicy).

**Since**: 21

 |
| NODE\_POSITION\_EDGES = 107 | 

Sets the position of a component relative to the boundaries of the container's content area. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: position of the component relative to the boundaries of the container's content area. The parameter type is [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: position of the component relative to the boundaries of the container's content area. The parameter type is [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md).

**Since**: 21

 |
| NODE\_ALLOW\_FORCE\_DARK = 108 | 

Sets whether to enable color inversion of a component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable color inversion. The value can be **0** (no) or **1** (yes).

**Since**: 21

 |
| NODE\_PIXEL\_ROUND = 109 | 

Sets the pixel rounding policy of a component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: pixel rounding policy of the component. The parameter type is [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: pixel rounding policy of the component. The parameter type is [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md).

**Since**: 21

 |
| NODE\_TEXT\_CONTENT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT = 1000 | 

Defines the text content attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: text content.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: text content.

 |
| NODE\_FONT\_COLOR = 1001 | 

Defines the font color attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: font color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: font color value, in 0xARGB format.

 |
| NODE\_FONT\_SIZE = 1002 | 

Defines the font size attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: font size, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: font size, in fp.

 |
| NODE\_FONT\_STYLE = 1003 | 

Defines the font style attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: font style [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle). The default value is **ARKUI\_FONT\_STYLE\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: font style [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle).

 |
| NODE\_FONT\_WEIGHT = 1004 | 

Defines the font weight attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight). The default value is **ARKUI\_FONT\_WEIGHT\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight).

 |
| NODE\_TEXT\_LINE\_HEIGHT = 1005 | 

Defines the text line height attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: line height, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: line height, in fp.

 |
| NODE\_TEXT\_DECORATION = 1006 | 

Defines the text decoration line style and its color. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: text decoration type [ArkUI\_TextDecorationType](../native-type-h/document.md#arkui_textdecorationtype). The default value is **ARKUI\_TEXT\_DECORATION\_TYPE\_NONE**.

.value\[1\]?.u32: text decoration color, in 0xARGB format. For example, 0xFFFF0000 indicates red. Optional.

.value\[2\]?.i32: text decoration style [ArkUI\_TextDecorationStyle](../native-type-h/document.md#arkui_textdecorationstyle).

.value\[3\]?.f32: thickness of the text decoration line. The parameter is optional. The default value is **1.0**. The value range is \[0, +∞). This parameter is supported since API version 22.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: text decoration type [ArkUI\_TextDecorationType](../native-type-h/document.md#arkui_textdecorationtype).

.value\[1\].u32: text decoration color, in 0xARGB format.

.value\[2\].i32: text decoration style [ArkUI\_TextDecorationStyle](../native-type-h/document.md#arkui_textdecorationstyle).

.value\[3\].f32: thickness of the text decoration line. This return value is supported since API version 22.

 |
| NODE\_TEXT\_CASE = 1007 | 

Defines the text case attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: text case [ArkUI\_TextCase](../native-type-h/document.md#arkui_textcase). The default value is **ARKUI\_TEXT\_CASE\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: text case [ArkUI\_TextCase](../native-type-h/document.md#arkui_textcase).

 |
| NODE\_TEXT\_LETTER\_SPACING = 1008 | 

Defines the letter spacing attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: letter spacing, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: letter spacing, in fp.

 |
| NODE\_TEXT\_MAX\_LINES = 1009 | 

Sets the maximum number of lines in the text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: maximum number of lines in the text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: maximum number of lines in the text.

 |
| NODE\_TEXT\_ALIGN = 1010 | 

Defines the horizontal alignment mode of the text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: horizontal alignment mode of the text. The value is an enumerated value of [ArkUI\_TextAlignment](../native-type-h/document.md#arkui_textalignment). The default value is **ARKUI\_TEXT\_ALIGNMENT\_START**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: horizontal alignment mode of the text. The value is an enumerated value of [ArkUI\_TextAlignment](../native-type-h/document.md#arkui_textalignment).

 |
| NODE\_TEXT\_OVERFLOW = 1011 | 

Defines the text overflow attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: display mode when the text is too long, specified using [ArkUI\_TextOverflow](../native-type-h/document.md#arkui_textoverflow). The default value is **ARKUI\_TEXT\_OVERFLOW\_NONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: display mode when the text is too long.[ArkUI\_TextOverflow](../native-type-h/document.md#arkui_textoverflow)

 |
| NODE\_FONT\_FAMILY = 1012 | 

Defines the font family attribute, which can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: fonts, separated by commas (,).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: fonts, separated by commas (,).

 |
| NODE\_TEXT\_COPY\_OPTION = 1013 | 

Defines the copy option attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: copy option [ArkUI\_CopyOptions](../native-type-h/document.md#arkui_copyoptions). The default value is **ARKUI\_COPY\_OPTIONS\_NONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: copy option [ArkUI\_CopyOptions](../native-type-h/document.md#arkui_copyoptions).

 |
| NODE\_TEXT\_BASELINE\_OFFSET = 1014 | 

Defines the text baseline offset attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: baseline offset, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: baseline offset, in fp.

 |
| NODE\_TEXT\_TEXT\_SHADOW = 1015 | 

Defines the shadow attribute. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: blur radius of the shadow, in vp.

.value\[1\].i32: shadow type [ArkUI\_ShadowType](../native-type-h/document.md#arkui_shadowtype). The default value is **ARKUI\_SHADOW\_TYPE\_COLOR**.

.value\[2\].u32: shadow color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

.value\[3\].f32: offset of the shadow along the x-axis, in vp.

.value\[4\].f32: offset of the shadow along the y-axis, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: blur radius of the shadow, in vp.

.value\[1\].i32: shadow type [ArkUI\_ShadowType](../native-type-h/document.md#arkui_shadowtype).

.value\[2\].u32: shadow color, in 0xARGB format.

.value\[3\].f32: offset of the shadow along the x-axis, in vp.

.value\[4\].f32: offset of the shadow along the y-axis, in vp.

 |
| NODE\_TEXT\_MIN\_FONT\_SIZE = 1016 | 

Defines the minimum font size attribute, which can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum font size, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum font size, in fp.

 |
| NODE\_TEXT\_MAX\_FONT\_SIZE = 1017 | 

Defines the maximum font size attribute, which can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum font size, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: maximum font size, in fp.

 |
| NODE\_TEXT\_FONT = 1018 | 

Defines the text style attribute, which can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string?: font family. Optional. Use commas (,) to separate multiple fonts.

.value\[0\].f32: font size, in fp.

.value\[1\]? .i32: font weight. Optional. The parameter type is [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight). The default value is **ARKUI\_FONT\_WEIGHT\_NORMAL**.

.value\[2\]?.i32: font style. Optional. The parameter type is [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle). The default value is **ARKUI\_FONT\_STYLE\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: font family. Use commas (,) to separate multiple fonts.

.value\[0\].f32: font size, in fp.

.value\[1\] .i32: font weight. The parameter type is [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight). The default value is **ARKUI\_FONT\_WEIGHT\_NORMAL**.

.value\[2\].i32: font style. The parameter type is [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle). The default value is **ARKUI\_FONT\_STYLE\_NORMAL**.

 |
| NODE\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY = 1019 | 

Defines how the adaptive height is determined for the text. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: how the adaptive height is determined for the text. The parameter type is [ArkUI\_TextHeightAdaptivePolicy](../native-type-h/document.md#arkui_textheightadaptivepolicy). The default value is **ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MAX\_LINES\_FIRST**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: how the adaptive height is determined for the text. The parameter type is [ArkUI\_TextHeightAdaptivePolicy](../native-type-h/document.md#arkui_textheightadaptivepolicy).

 |
| NODE\_TEXT\_INDENT = 1020 | 

Defines the indentation of the first line. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: indentation of the first line, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: indentation of the first line, in vp.

 |
| NODE\_TEXT\_WORD\_BREAK = 1021 | 

Defines the line break rule. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: line break rule. The parameter type is [ArkUI\_WordBreak](../native-type-h/document.md#arkui_wordbreak). The default value is **ARKUI\_WORD\_BREAK\_BREAK\_WORD**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: line break rule. The parameter type is [ArkUI\_WordBreak](../native-type-h/document.md#arkui_wordbreak).

 |
| NODE\_TEXT\_ELLIPSIS\_MODE = 1022 | 

Defines the ellipsis position. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: ellipsis position. The parameter type is [ArkUI\_EllipsisMode](../native-type-h/document.md#arkui_ellipsismode). The default value is **ARKUI\_ELLIPSIS\_MODE\_END**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: ellipsis position. The parameter type is [ArkUI\_EllipsisMode](../native-type-h/document.md#arkui_ellipsismode).

 |
| NODE\_TEXT\_LINE\_SPACING = 1023 | 

Defines the line spacing attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: line spacing, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: line spacing, in fp.

 |
| NODE\_FONT\_FEATURE = 1024 | 

Sets the font feature. **NODE\_FONT\_FEATURE** provides advanced typographic features in OpenType fonts. These features such as hyphenation and monospace are generally used in custom fonts and require support from the respective fonts. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: string that describes the font feature settings. The value format is normal | <feature-tag-value>.

Syntax for <feature-tag-value>: <string> \[ <integer> | on | off \],

There can be multiple **<feature-tag-value>** values, separated by commas (,). For example, for the monospace feature, you can pass in **ss01 on**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: font feature. Multiple font features are separated by commas (,).

 |
| NODE\_TEXT\_ENABLE\_DATA\_DETECTOR = 1025 | 

Sets whether to enable text recognition.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable text recognition. The default value is **false**. The value **true** means to enable text recognition, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether text recognition is enabled.

 |
| NODE\_TEXT\_ENABLE\_DATA\_DETECTOR\_CONFIG = 1026 | 

Configures text recognition settings.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0...\].i32: array of entity types. The parameter type is [ArkUI\_TextDataDetectorType](../native-type-h/document.md#arkui_textdatadetectortype).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0...\].i32: array of entity types. The parameter type is [ArkUI\_TextDataDetectorType](../native-type-h/document.md#arkui_textdatadetectortype).

 |
| NODE\_TEXT\_SELECTED\_BACKGROUND\_COLOR = 1027 | 

Defines the background color of the selected text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color value, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value, in 0xARGB format.

 |
| NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING = 1028 | 

Sets the string to use in the styled string. This attribute can be set, reset, and obtained as required through APIs. Configuring a custom [OH\_Drawing\_Typography](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-typography/document.md) object for the **Text** component will skip the layout measurement phase of the component. Note the following:

1\. Ensure that the lifecycles of the\*\* OH\_ArkUI\_StyledString\*\* object and **OH\_Drawing\_Typography** object are aligned with the lifecycle of the **Text** component. Reset the **OH\_ArkUI\_StyledString** object when the **Text** component is destroyed; otherwise, it may lead to null pointer crashes in the application.

2\. Ensure that the **OH\_Drawing\_TypographyLayout** API is called prior to the layout measurement of the **Text** component.

3\. When the **OH\_ArkUI\_StyledString** and **OH\_Drawing\_Typography** objects are released, the **reset** API of the **Text** component must be called synchronously; otherwise, it may cause null pointer crashes in the application.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: string to use in the styled string. The parameter type is [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: string to use in the styled string. The parameter type is [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md).

 |
| NODE\_TEXT\_HALF\_LEADING = 1029 | 

Sets whether to center text vertically in the **Text** component.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to center text vertically. The default value is **false**.

The value **true** means to center text vertically, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the text is centered vertically.

 |
| NODE\_IMMUTABLE\_FONT\_WEIGHT = 1030 | 

Defines the font weight attribute, which can be set, reset, and obtained as required through APIs. The font weight specified by this API is not affected by any changes in the system font weight settings.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight). The default value is **ARKUI\_FONT\_WEIGHT\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight).

**Since**: 15

 |
| NODE\_TEXT\_LINE\_COUNT = 1031 | 

Sets the number of lines in the text. This attribute can be obtained through APIs. Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of text lines.

**Since**: 20

 |
| NODE\_TEXT\_OPTIMIZE\_TRAILING\_SPACE = 1032 | 

Sets whether to optimize the trailing spaces at the end of each line during text layout. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to optimize trailing spaces at the end of each line during text layout. The default value is **false**.

The value **true** means to optimize trailing spaces at the end of each line during text layout, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the trailing spaces at the end of each line is optimized during text layout.

**Since**: 20

 |
| NODE\_TEXT\_LINEAR\_GRADIENT = 1033 | 

Sets a linear gradient effect for text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: start angle of the linear gradient. The setting takes effect only when **direction** is set to **ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM**. A positive value indicates a clockwise rotation from the origin, (0, 0). The default value is **180**.

.value\[1\].i32: direction of the linear gradient [ArkUI\_LinearGradientDirection](../native-type-h/document.md#arkui_lineargradientdirection). When a direction other than **ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM** is set, the **angle** property is ignored. Default value: **ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM**.

.value\[2\].i32: whether the colors are repeated. The value **true** means that the colors are repeated, and **false** means the opposite. Default value: **false**.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops, in 0xARGB format. For example, 0xFFFF0000 indicates red.

**stops**: stop positions of the color stops. The value range is \[0, 1.0\]. **0** represents the start of the gradient container, and **1.0** represents the end. To create a gradient with multiple color stops, you are advised to set the array elements in ascending order. If a later element is smaller than a previous one, it will be treated as equal to the previous value.

**size**: number of colors. If the value is smaller than the length of the **colors** array, only the first **size** colors take effect. Values greater than the **colors** array length, values less than or equal to 0, or invalid values are not recommended.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: start angle of the linear gradient. The set value is used only when **ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM** is used. In other cases, the default value **0** is used.

.value\[1\].i32: direction of the linear gradient [ArkUI\_LinearGradientDirection](../native-type-h/document.md#arkui_lineargradientdirection).

.value\[2\].i32: whether the colors are repeated. The value **1** means that the colors are repeated, and **0** means the opposite. Default value: **0**.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops, in 0xARGB format. For example, 0xFFFF0000 indicates red.

**stops**: stop positions of the color stops. The value range is \[0, 1.0\]. **0** represents the start of the gradient container, and **1.0** represents the end.

**size**: number of effective gradient colors.

**Since**: 20

 |
| NODE\_TEXT\_RADIAL\_GRADIENT = 1034 | 

Sets a radial gradient effect for text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.f32: x-coordinate of the radial gradient center relative to the upper left corner of the text box.

.value\[1\]?.f32: y-coordinate of the radial gradient center relative to the upper left corner of the text box. The coordinates of the upper left corner of the text box are \[0, 0\].

.value\[2\]?.f32: radius of the radial gradient. The default value is **0**.

.value\[3\].i32: whether the colors are repeated. The value **true** means that the colors are repeated, and **false** means the opposite. Default value: **false**.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops, in 0xARGB format. For example, 0xFFFF0000 indicates red.

**stops**: stop positions of the color stops. The value range is \[0, 1.0\]. **0** represents the start of the gradient container, and **1.0** represents the end. To create a gradient with multiple color stops, you are advised to set the array elements in ascending order. If a later element is smaller than a previous one, it will be treated as equal to the previous value.

**size**: number of colors. If the value is smaller than the length of the **colors** array, only the first **size** colors take effect. Values greater than the **colors** array length, values less than or equal to 0, or invalid values are not recommended.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\]?.f32: x-coordinate of the radial gradient center relative to the upper left corner of the text box.

.value\[1\]?.f32: y-coordinate of the radial gradient center relative to the upper left corner of the text box. The coordinates of the upper left corner of the text box are \[0, 0\].

.value\[2\]?.f32: radius of the radial gradient. The default value is **0**.

.value\[3\]?.i32: whether the colors are repeated. The value **1** means that the colors are repeated, and **0** means the opposite. Default value: **0**.

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). It specifies an array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

**colors**: colors of the color stops, in 0xARGB format. For example, 0xFFFF0000 indicates red.

**stops**: stop positions of the color stops. The value range is \[0, 1.0\]. **0** represents the start of the gradient container, and **1.0** represents the end.

**size**: number of effective gradient colors.

**Since**: 20

 |
| NODE\_TEXT\_VERTICAL\_ALIGN = 1035 | 

Sets the vertical alignment of the text content. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: vertical alignment of the text content, specified using the [ArkUI\_TextVerticalAlignment](../native-type-h/document.md#arkui_textverticalalignment) enum. The default value is **ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_BASELINE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: vertical alignment of the text content, specified using the [ArkUI\_TextVerticalAlignment](../native-type-h/document.md#arkui_textverticalalignment) enum.

**Since**: 20

 |
| NODE\_TEXT\_CONTENT\_ALIGN = 1036 | 

Sets the vertical alignment of the text content area. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: vertical alignment of the text content area, specified using the [ArkUI\_TextContentAlign](../native-type-h/document.md#arkui_textcontentalign) enum. The default value is **ARKUI\_TEXT\_CONTENT\_ALIGN\_CENTER**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: vertical alignment of the text content area, specified using the [ArkUI\_TextContentAlign](../native-type-h/document.md#arkui_textcontentalign) enum.

**Since**: 21

 |
| NODE\_TEXT\_MIN\_LINES = 1037 | 

Sets the minimum number of lines in the text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: minimum number of text lines.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: minimum number of text lines.

**Since**: 22

 |
| NODE\_TEXT\_ENABLE\_SELECTED\_DATA\_DETECTOR = 1038 | 

Sets whether to enable entity recognition for selected text.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable entity recognition for selected text. **true** indicates to enable; **false** otherwise. Default value: **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether entity recognition for selected text is enabled.

**Since**: 22

 |
| NODE\_TEXT\_MIN\_LINE\_HEIGHT = 1040 | 

Minimum line height. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum line height of the text. The default value is **0**. The unit is fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum line height of the text. The unit is fp.

**Since**: 22

 |
| NODE\_TEXT\_MAX\_LINE\_HEIGHT = 1041 | 

Maximum line height. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum line height of the text. The default value is **0**, indicating that the maximum line height is not limited. The unit is fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: maximum line height of the text. The unit is fp.

**Since**: 22

 |
| NODE\_TEXT\_LINE\_HEIGHT\_MULTIPLE = 1042 | 

Defines the multiple value of the multiple line height mode. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: multiple value of the multiple line height mode. The default value is **0**, indicating that the default line height is used.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: multiple value of the multiple line height mode.

**Since**: 22

 |
| NODE\_TEXT\_LAYOUT\_MANAGER = 1043 | 

Defines the text layout manager. This attribute can be obtained as required through APIs.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: text layout manager object. The parameter type is [ArkUI\_LayoutManager](../../structs/arkui-textlayoutmanager/document.md).

**Since**: 22

 |
| NODE\_TEXT\_EDIT\_MENU\_OPTIONS = 1044 | 

Defines the extended options of the text menu. This attribute can be obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: configuration data of the extended item of the text menu. The parameter type is [ArkUI\_TextEditMenuOptions](../../structs/arkui-texteditmenuoptions/document.md).

**Since**: 22

 |
| NODE\_TEXT\_BIND\_SELECTION\_MENU = 1045 | 

Customizes the text selection menu. This attribute can be obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: configuration data of the custom text selection menu. The parameter type is [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md).

**Since**: 22

 |
| NODE\_SPAN\_CONTENT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SPAN = 2000 | 

Defines the text content attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: text content of the [span](../../../arkts-components/text-and-input/span/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: content of the text span.

 |
| NODE\_SPAN\_TEXT\_BACKGROUND\_STYLE = 2001 | 

Defines the text background style. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the text background, in 0xARGB format, for example, **0xFFFF0000** indicating red.

The second parameter is used to set the rounded corner of the text background. The options are as follows:

\-.value\[1\].f32: radius of the four corners, in vp.

\- .value\[1\].f32: radius of the upper left corner, in vp.

.value\[2\].f32: radius of the upper right corner, in vp.

.value\[3\].f32: radius of the lower left corner, in vp.

.value\[4\].f32: radius of the lower right corner, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the text background, in 0xARGB format.

.value\[1\].f32: radius of the upper left corner, in vp.

.value\[2\].f32: radius of the upper right corner, in vp.

.value\[3\].f32: radius of the lower left corner, in vp.

.value\[4\].f32: radius of the lower right corner, in vp.

 |
| NODE\_SPAN\_BASELINE\_OFFSET = 2002 | 

Defines the text baseline offset attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: baseline offset, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: baseline offset, in fp.

 |
| NODE\_IMAGE\_SPAN\_SRC = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE\_SPAN = 3000 | 

Defines the image source for an image span. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: image address of the image span.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: image address of the image span.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Either **.object** or **.string** must be set.

 |
| NODE\_IMAGE\_SPAN\_VERTICAL\_ALIGNMENT = 3001 | 

Defines the alignment mode of the image with the text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: alignment mode of the image with the text, specified using the [ArkUI\_ImageSpanAlignment](../native-type-h/document.md#arkui_imagespanalignment) enum.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: alignment mode of the image with the text, specified using the [ArkUI\_ImageSpanAlignment](../native-type-h/document.md#arkui_imagespanalignment) enum.

 |
| NODE\_IMAGE\_SPAN\_ALT = 3002 | 

Defines the image source for an image span. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: placeholder image address for the image span. GIF images are not supported.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Either **.object** or **.string** must be set.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: image source for the image span.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

 |
| NODE\_IMAGE\_SPAN\_BASELINE\_OFFSET = 3003 | 

Defines the baseline offset attribute of the **ImageSpan** component. This attribute can be set, reset, and obtained as required through APIs. A positive value means an upward offset, while a negative value means a downward offset. The default value is **0**, and the unit is fp.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: baseline offset, in fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: baseline offset, in fp.

**Since**: 13

 |
| NODE\_IMAGE\_SPAN\_COLOR\_FILTER = 3004 | 

Defines the color filter of the image. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32 to .value\[19\].f32: filter matrix array.

.size: indicates that the size of the filter array is 5 × 4.

.object: color filter pointer. The parameter type is [OH\_Drawing\_ColorFilter](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-colorfilter/document.md).

Either **.object** or **.size** must be set.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32 to .value\[19\].f32: filter matrix array.

.size: indicates that the size of the filter array is 5 × 4.

.object: color filter pointer. The parameter type is [OH\_Drawing\_ColorFilter](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-colorfilter/document.md).

**Since**: 22

 |
| NODE\_IMAGE\_SPAN\_SUPPORT\_SVG2 = 3005 | 

Sets whether to enable the SVG parsing capability, which allows you to set the scope of SVG parsing functionality support. This attribute can be set, reset, and obtained as required through APIs. After the **ImageSpan** component is created, the value of this attribute cannot be dynamically changed.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the new SVG parsing capability. **true**: enable enhanced SVG tag parsing. **false**: use original SVG tag parsing.

Default value: **false**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the new SVG parsing capability is enabled.

**Since**: 22

 |
| NODE\_IMAGE\_SRC = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE = 4000 | 

Defines the image source of the **Image** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: image address.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Either **.object** or **.string** must be set.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: image address.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

 |
| NODE\_IMAGE\_OBJECT\_FIT = 4001 | 

Defines how the image is resized to fit its container. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: how the image is resized to fit its container, specified using the [ArkUI\_ObjectFit](../native-type-h/document.md#arkui_objectfit) enum.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: how the image is resized to fit its container, specified using the [ArkUI\_ObjectFit](../native-type-h/document.md#arkui_objectfit) enum.

 |
| NODE\_IMAGE\_INTERPOLATION = 4002 | 

Defines the interpolation effect of the image. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: interpolation effect, specified using the [ArkUI\_ImageInterpolation](../native-type-h/document.md#arkui_imageinterpolation) enum.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: interpolation effect, specified using the [ArkUI\_ImageInterpolation](../native-type-h/document.md#arkui_imageinterpolation) enum.

 |
| NODE\_IMAGE\_OBJECT\_REPEAT = 4003 | 

Defines how the image is repeated. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: how the image is repeated, specified using the [ArkUI\_ImageRepeat](../native-type-h/document.md#arkui_imagerepeat) enum.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: how the image is repeated, specified using the [ArkUI\_ImageRepeat](../native-type-h/document.md#arkui_imagerepeat) enum.

 |
| NODE\_IMAGE\_COLOR\_FILTER = 4004 | 

Defines the color filter of the image. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32 to .value\[19\].f32: filter matrix array.

.size: 5 x 4 filter array size.

.object: pointer to the color filter. The parameter type is **OH\_Drawing\_ColorFilter**.

Either **.object** or **.size** must be set.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32 to .value\[19\].f32: filter matrix array.

.size: 5 x 4 filter array size.

.object: pointer to the color filter. The parameter type is **OH\_Drawing\_ColorFilter**.

 |
| NODE\_IMAGE\_AUTO\_RESIZE = 4005 | 

Defines the auto resize attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable auto resizing. The default value is **false**. **true**: Enable auto resizing. **false**: Disable auto resizing.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the image is resized.

 |
| NODE\_IMAGE\_ALT = 4006 | 

Defines the placeholder image attribute. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: address of the placeholder image.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Either **.object** or **.string** must be set. Network images are not supported.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: image source for the image span.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

 |
| NODE\_IMAGE\_DRAGGABLE = 4007 | 

Defines whether the image is draggable. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the image is draggable. The value **true** means that the image is draggable.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the image is draggable.

 |
| NODE\_IMAGE\_RENDER\_MODE = 4008 | 

Defines the image rendering mode. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: image rendering mode. The parameter type is [ArkUI\_ImageRenderMode](../native-type-h/document.md#arkui_imagerendermode).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: image rendering mode. The parameter type is [ArkUI\_ImageRenderMode](../native-type-h/document.md#arkui_imagerendermode).

 |
| NODE\_IMAGE\_FIT\_ORIGINAL\_SIZE = 4009 | 

Sets whether the display size of an image follows the original size of the image source. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: indicates whether the display size of an image follows the original size of the image source. The value **1** indicates that the display size of an image follows the original size of the image source, and the value **0** indicates the opposite. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: The value **1** indicates that the display size of an image follows the original size of the image source, and **0** means the opposite.

 |
| NODE\_IMAGE\_FILL\_COLOR = 4010 | 

Sets the fill color to be superimposed on the image. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: fill color. The value is in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: fill color. The value is in 0xARGB format.

 |
| NODE\_IMAGE\_RESIZABLE = 4011 | 

Sets the resizable image options.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: fixed distance (unchanged during stretching) from the left edge of the image. The unit is vp.

.value\[1\].f32: fixed distance (unchanged during stretching) from the top edge of the image. The unit is vp.

.value\[2\].f32: fixed distance (unchanged during stretching) from the right edge of the image. The unit is vp.

.value\[3\].f32: fixed distance (unchanged during stretching) from the bottom edge of the image. The unit is vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: fixed distance (unchanged during stretching) from the left edge of the image. The unit is vp.

.value\[1\].f32: fixed distance (unchanged during stretching) from the top edge of the image. The unit is vp.

.value\[2\].f32: fixed distance (unchanged during stretching) from the right edge of the image. The unit is vp.

.value\[3\].f32: fixed distance (unchanged during stretching) from the bottom edge of the image. The unit is vp.

 |
| NODE\_IMAGE\_SYNC\_LOAD = 4012 | 

Defines the synchronous image loading attribute. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to load the image synchronously. The default value is **false**. **true**: Load the image synchronously. **false**: Load the image asynchronously.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the image is loaded synchronously.

**Since**: 20

 |
| NODE\_IMAGE\_SOURCE\_SIZE = 4013 | 

Sets the decoding size of the image. This attribute works only when the target size is smaller than the source size. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: width for image decoding, in px.

.value\[1\].i32: height for image decoding, in px. If either parameter is set to a value less than or equal to 0, the attribute setting fails, and [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: width for image decoding, in px.

.value\[1\].i32: height for image decoding, in px.

**Since**: 21

 |
| NODE\_IMAGE\_IMAGE\_MATRIX = 4014 | 

Sets the transformation matrix of the image. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0...15\].f32: 4x4 matrix represented by a floating-point array of length 16. If the number of parameters is less than 16, the attribute setting fails, and [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned. If the number of parameters exceeds 16, only the first 16 data entries are used.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0...15\].f32: 4x4 matrix represented by a floating-point array of length 16.

**Since**: 21

 |
| NODE\_IMAGE\_MATCH\_TEXT\_DIRECTION = 4015 | 

Specifies whether the image follows the system language direction, displaying a mirrored effect in a right-to-left (RTL) language environments. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the image follows the system language direction. The default value is **false**. **true**: The image follows the system language direction. **false**: The image does not follow the system language direction.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the image follows the system language direction. **true**: The image follows the system language direction. **false**: The image does not follow the system language direction.

**Since**: 21

 |
| NODE\_IMAGE\_COPY\_OPTION = 4016 | 

Sets the image copy mode. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: image copy mode, specified using the [ArkUI\_CopyOptions](../native-type-h/document.md#arkui_copyoptions) enum. The default value is **ARKUI\_COPY\_OPTIONS\_NONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: image copy mode, specified using the [ArkUI\_CopyOptions](../native-type-h/document.md#arkui_copyoptions) enum.

**Since**: 21

 |
| NODE\_IMAGE\_ENABLE\_ANALYZER = 4017 | 

Sets whether to enable the AI image analyzer, which supports subject recognition, text recognition, and object lookup. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the AI image analyzer. The default value is **false**. **true**: Enable the AI image analyzer. **false**: Disable the AI image analyzer.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the AI image analyzer is enabled. **true**: Enable the AI image analyzer. **false**: Disable the AI image analyzer.

**Since**: 21

 |
| NODE\_IMAGE\_DYNAMIC\_RANGE\_MODE = 4018 | 

Defines the dynamic range attribute for image display, specifying the dynamic range mode for image rendering (for example, SDR/HDR). This attribute can be set, reset, and obtained as required through APIs. It is used to match the capabilities of the display device and ensure accurate presentation of image brightness and colors.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: dynamic range mode, specified using the [ArkUI\_DynamicRangeMode](../native-type-h/document.md#arkui_dynamicrangemode) enum. The default value is **ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: dynamic range mode, specified using the [ArkUI\_DynamicRangeMode](../native-type-h/document.md#arkui_dynamicrangemode) enum.

**Since**: 21

 |
| NODE\_IMAGE\_HDR\_BRIGHTNESS = 4019 | 

Defines the brightness attribute of the image in HDR mode, used to control brightness parameters for high dynamic range display. This attribute can be set, reset, and obtained as required through APIs. It is used to ensure accurate presentation of details in the bright and dark areas of HDR images.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: brightness value. The value range is \[0, 1\]. Values less than 0 or greater than 1 are clamped to 1. **0**: The image is displayed at SDR brightness. **1**: The image is displayed at the highest allowed HDR brightness.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: brightness value. The value range is \[0, 1\].

**Since**: 21

 |
| NODE\_IMAGE\_ORIENTATION = 4020 | 

Sets the display orientation of the image content. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: expected display orientation of the image content, specified using the [ArkUI\_Orientation](../native-type-h/document.md#arkui_imagerotateorientation) enum. The default value is **ARKUI\_ORIENTATION\_UP**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: expected display orientation of the image content, specified using the [ArkUI\_Orientation](../native-type-h/document.md#arkui_imagerotateorientation) enum.

**Since**: 21

 |
| NODE\_IMAGE\_SUPPORT\_SVG2 = 4021 | 

Sets whether to enable the SVG parsing capability, which allows you to set the scope of SVG parsing functionality support. This attribute can be set, reset, and obtained as required through APIs. After the **Image** component is created, the value of this attribute cannot be dynamically changed.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the new SVG parsing capability.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the new SVG parsing capability is enabled.

**Since**: 21

 |
| NODE\_IMAGE\_CONTENT\_TRANSITION = 4022 | 

Defines the transition effect when the image changes. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: custom transition animation. The parameter type is [ArkUI\_ContentTransitionEffect](../../structs/arkui-contenttransitioneffect/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: custom transition animation. The parameter type is [ArkUI\_ContentTransitionEffect](../../structs/arkui-contenttransitioneffect/document.md).

**Since**: 21

 |
| NODE\_IMAGE\_ALT\_PLACEHOLDER = 4023 | 

Configures a placeholder image during the loading process. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: placeholder image address during the loading of the image component.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Either **.object** or **.string** must be set. Network images are not supported.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: placeholder image address during the loading of the image component.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

**Since**: 22

 |
| NODE\_IMAGE\_ALT\_ERROR = 4024 | 

Configures a placeholder image in the loading failure scenarios. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: placeholder image address in the loading failure scenarios.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

Either **.object** or **.string** must be set. Network images are not supported.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: placeholder image address in the loading failure scenarios.

.object: **PixelMap** object. The parameter type is [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md).

**Since**: 22

 |
| NODE\_TOGGLE\_SELECTED\_COLOR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TOGGLE = 5000 | 

Defines the color of the component when it is selected. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: background color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: background color, in 0xARGB format.

 |
| NODE\_TOGGLE\_SWITCH\_POINT\_COLOR = 5001 | 

Defines the color of the circular thumb for the component of the switch type. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the circular thumb, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the circular thumb, in 0xARGB format.

 |
| NODE\_TOGGLE\_VALUE = 5002 | 

Defines the toggle switch value. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the toggle. The value **true** means to enable the toggle.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the toggle is enabled.

 |
| NODE\_TOGGLE\_UNSELECTED\_COLOR = 5003 | 

Defines the color of the component when it is deselected. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: background color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: background color, in 0xARGB format.

 |
| NODE\_LOADING\_PROGRESS\_COLOR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LOADING\_PROGRESS = 6000 | 

Defines the foreground color of the loading progress bar. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: foreground color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: foreground color, in 0xARGB format.

 |
| NODE\_LOADING\_PROGRESS\_ENABLE\_LOADING = 6001 | 

Defines whether to show the loading animation for the **LoadingProgress** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show the loading animation. **true** to show; **false** otherwise. The default value is **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the loading animation is shown. The value **1** means that the loading animation is shown, and **0** means the opposite.

 |
| NODE\_TEXT\_INPUT\_PLACEHOLDER = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_INPUT = 7000 | 

Defines the default placeholder text of the single-line text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: default placeholder text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: default placeholder text.

 |
| NODE\_TEXT\_INPUT\_TEXT = 7001 | 

Defines the default text of the single-line text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: default text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: default text.

 |
| NODE\_TEXT\_INPUT\_CARET\_COLOR = 7002 | 

Defines the caret color attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: caret color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: caret color, in 0xARGB format.

 |
| NODE\_TEXT\_INPUT\_CARET\_STYLE = 7003 | 

Defines the caret style attribute. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: caret width, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: caret width, in vp.

 |
| NODE\_TEXT\_INPUT\_SHOW\_UNDERLINE = 7004 | 

Defines the underline attribute of the single-line text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show an underline. The value **true** means to show an underline, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: The value **1** means that an underline is shown, and **0** means the opposite.

 |
| NODE\_TEXT\_INPUT\_MAX\_LENGTH = 7005 | 

Defines the maximum number of characters in the text input. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: maximum number of characters in the text input, without a unit.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: maximum number of characters in the text input.

 |
| NODE\_TEXT\_INPUT\_ENTER\_KEY\_TYPE = 7006 | 

Defines the type of the Enter key. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: type of the Enter key, specified using the [ArkUI\_EnterKeyType](../native-type-h/document.md#arkui_enterkeytype) enum. The default value is **ARKUI\_ENTER\_KEY\_TYPE\_DONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: type of the Enter key, specified using the [ArkUI\_EnterKeyType](../native-type-h/document.md#arkui_enterkeytype) enum.

 |
| NODE\_TEXT\_INPUT\_PLACEHOLDER\_COLOR = 7007 | 

Defines the placeholder text color. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color value, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value, in 0xARGB format.

 |
| NODE\_TEXT\_INPUT\_PLACEHOLDER\_FONT = 7008 | 

Defines the placeholder text font. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.f32: font size, in fp. Optional. The default value is **16.0**.

.value\[1\]?.i32: font style [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle). The default value is **ARKUI\_FONT\_STYLE\_NORMAL**.

.value\[2\]?.i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight). The default value is **ARKUI\_FONT\_WEIGHT\_NORMAL**.

?.string: font family. Multiple font families are separated by commas (,). For example, "font weight; font family 1, font family 2".

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: font size, in fp.

.value\[1\].i32: font style [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle).

.value\[2\].i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight).

.string: font family. Multiple font families are separated by commas (,).

 |
| NODE\_TEXT\_INPUT\_ENABLE\_KEYBOARD\_ON\_FOCUS = 7009 | 

Defines whether to enable the input method when the component obtains focus. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the input method when the component obtains focus. The value **true** means to enable the input method, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the input method is enabled when the component obtains focus. The value **1** means that the input method is enabled when the component obtains focus, and **0** means the opposite.

 |
| NODE\_TEXT\_INPUT\_TYPE = 7010 | 

Defines the text box type. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: text box type, specified using the [ArkUI\_TextInputType](../native-type-h/document.md#arkui_textinputtype) enum. The default value is **ARKUI\_TEXTINPUT\_TYPE\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: text box type, specified using the [ArkUI\_TextInputType](../native-type-h/document.md#arkui_textinputtype) enum.

 |
| NODE\_TEXT\_INPUT\_SELECTED\_BACKGROUND\_COLOR = 7011 | 

Defines the background color of the selected text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color value, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value, in 0xARGB format.

 |
| NODE\_TEXT\_INPUT\_SHOW\_PASSWORD\_ICON = 7012 | 

Defines whether to display the password icon at the end of the password text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to display the password icon. **true** to display; **false** otherwise. The default value is **false**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: The value **1** means that the password icon is displayed at the end of the password text box, and **0** means the opposite.

 |
| NODE\_TEXT\_INPUT\_EDITING = 7013 | 

Defines the editable state for the single-line text box. This attribute can be set as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to remain in the editable state. The value **true** means to remain in the editable state, and **false** means to exit the editable state.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for obtaining the attribute:

.value\[0\].i32: whether to remain in the editable state. The value **true** means to remain in the editable state, and **false** means to exit the editable state.

 |
| NODE\_TEXT\_INPUT\_CANCEL\_BUTTON = 7014 | 

Defines the style of the cancel button on the right of the single-line text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: button style [ArkUI\_CancelButtonStyle](../native-type-h/document.md#arkui_cancelbuttonstyle). The default value is **ARKUI\_CANCELBUTTON\_STYLE\_INPUT**.

.value\[1\]?.f32: button icon size, in vp.

.value\[2\]?.u32: button icon color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

?.string: button icon image address. The value is the local address of an image, for example, **/pages/icon.png**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: button style [ArkUI\_CancelButtonStyle](../native-type-h/document.md#arkui_cancelbuttonstyle).

.value\[1\].f32: icon size, in vp.

.value\[2\].u32: button icon color, in 0xARGB format.

.string: button icon image source.

 |
| NODE\_TEXT\_INPUT\_TEXT\_SELECTION = 7015 | 

Sets the text selection area, which will be highlighted. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: start position of the text selection.

.value\[1\].i32: end position of the text selection.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: start position of the text selection.

.value\[1\].i32: end position of the text selection.

 |
| NODE\_TEXT\_INPUT\_UNDERLINE\_COLOR = 7016 | 

Sets the color of the underline when it is shown. The default underline color configured for the theme is **'0x33182431'**.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the underline applied to the text being typed in. The value is in 0xARGB format.

.value\[1\].u32: color of the underline applied to the text in the normal state. The value is in 0xARGB format.

.value\[2\].u32: color of the underline applied to the text when an error is detected. The value is in 0xARGB format.

.value\[3\].u32: color of the underline applied to the text when it is disabled. The value is in 0xARGB format.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the underline applied to the text being typed in. The value is in 0xARGB format.

.value\[1\].u32: color of the underline applied to the text in the normal state. The value is in 0xARGB format.

.value\[2\].u32: color of the underline applied to the text when an error is detected. The value is in 0xARGB format.

.value\[3\].u32: color of the underline applied to the text when it is disabled. The value is in 0xARGB format.

 |
| NODE\_TEXT\_INPUT\_ENABLE\_AUTO\_FILL = 7017 | 

Sets whether to enable autofill.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable autofill. The default value is **true**.

**true** to enable; **false** otherwise.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether autofill is enabled.

 |
| NODE\_TEXT\_INPUT\_CONTENT\_TYPE = 7018 | 

Sets the autofill type.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: autofill type. The parameter type is [ArkUI\_TextInputContentType](../native-type-h/document.md#arkui_textinputcontenttype).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: autofill type. The parameter type is [ArkUI\_TextInputContentType](../native-type-h/document.md#arkui_textinputcontenttype).

 |
| NODE\_TEXT\_INPUT\_PASSWORD\_RULES = 7019 | 

Defines the rules for generating passwords. When autofill is used, these rules are transparently transmitted to Password Vault for generating a new password.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: rules for generating passwords.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: rules for generating passwords.

 |
| NODE\_TEXT\_INPUT\_SELECT\_ALL = 7020 | 

Sets whether to select all text in the initial state. This attribute is not available for the inline input style.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to select all text in the initial state. The default value is **false**.

**true**: Select all text in the initial state. **false**: Do not select all text in the initial state.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether all text is selected in the initial state.

 |
| NODE\_TEXT\_INPUT\_INPUT\_FILTER = 7021 | 

Sets the regular expression for input filtering. Only inputs that comply with the regular expression can be displayed. Other inputs are filtered out. For single-character input scenarios, only single-character matching is supported; for multi-character input scenarios (such as pasting), string matching is supported.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: regular expression.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: regular expression.

 |
| NODE\_TEXT\_INPUT\_STYLE = 7022 | 

Sets the text box to the default style or inline input style. The inline input style is only available when [ArkUI\_TextInputType](../native-type-h/document.md#arkui_textinputtype) is set to **ARKUI\_TEXTINPUT\_TYPE\_NORMAL**.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: text input style. The parameter type is [ArkUI\_TextInputStyle](../native-type-h/document.md#arkui_textinputstyle). The default value is **ARKUI\_TEXTINPUT\_STYLE\_DEFAULT**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: text input style. The parameter type is [ArkUI\_TextInputStyle](../native-type-h/document.md#arkui_textinputstyle).

 |
| NODE\_TEXT\_INPUT\_CARET\_OFFSET = 7023 | 

Sets or obtains the caret position.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

Sets the position of the caret.

.value\[0\].i32: length from the start of the string to the position where the input cursor is located.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

Returns the position information of the caret. If this API is called when the caret position is updated in the current frame, it will not take effect.

.value\[0\].i32: index of the caret position.

.value\[1\].f32: x-coordinate of the caret relative to the text box.

.value\[2\].f32: y-coordinate of the caret relative to the text box.

 |
| NODE\_TEXT\_INPUT\_CONTENT\_RECT = 7024 | 

Obtains the position of the edited text area relative to the component and its size. Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: horizontal coordinate.

.value\[1\].f32: vertical coordinate.

.value\[2\].f32: content width.

.value\[3\].f32: content height.

 |
| NODE\_TEXT\_INPUT\_CONTENT\_LINE\_COUNT = 7025 | 

Obtains the number of lines of the edited text. Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].i32: number of lines in the edited text.

 |
| NODE\_TEXT\_INPUT\_SELECTION\_MENU\_HIDDEN = 7026 | 

Sets whether to hide the text selection menu when the text box is long-pressed, double-clicked, or right-clicked. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to hide the text selection menu when the text box is long-pressed, double-clicked, or right-clicked. The default value is **false**.

**true**: The system text selection menu is hidden under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box.

**false**: The system text selection menu is displayed under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the text selection menu is hidden when the text box is long-pressed, double-clicked, or right-clicked.

 |
| NODE\_TEXT\_INPUT\_BLUR\_ON\_SUBMIT = 7027 | 

Sets whether the text box loses focus after the **Enter** key is pressed to submit information.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the text box loses focus after the Enter key is pressed to submit information. The default value is **true**.

**true**: The text box loses focus. **false**: The text box does not lose focus.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the text box loses focus after the Enter key is pressed to submit information.

 |
| NODE\_TEXT\_INPUT\_CUSTOM\_KEYBOARD = 7028 | 

Sets a custom keyboard.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: custom keyboard. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md).

.value\[0\]?.i32: whether the custom keyboard supports avoidance. The default value is **false**.

**true**: The custom keyboard supports avoidance. **false**: The custom keyboard does not support avoidance.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: custom keyboard. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md).

.value\[0\].i32: whether the custom keyboard supports avoidance.

 |
| NODE\_TEXT\_INPUT\_WORD\_BREAK = 7029 | 

Defines the line break rule. This attribute can be set, reset, and obtained as required through APIs. It takes effect only when the component is in the inline input editing state.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: line break rule. The parameter type is [ArkUI\_WordBreak](../native-type-h/document.md#arkui_wordbreak). The default value is **ARKUI\_WORD\_BREAK\_BREAK\_WORD**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: line break rule. The parameter type is [ArkUI\_WordBreak](../native-type-h/document.md#arkui_wordbreak).

 |
| NODE\_TEXT\_INPUT\_NUMBER\_OF\_LINES = 7031 | 

Sets the number of lines in the [TextInput](../../../arkts-components/text-and-input/textinput/document.md) component, which can be used to work out the height of the component. For example, if **numberOfLines** is set to **3**, the component displays three lines of text by default.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of lines.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of lines.

 |
| NODE\_TEXT\_INPUT\_LETTER\_SPACING = 7032 | 

Sets the letter spacing of the [TextInput](../../../arkts-components/text-and-input/textinput/document.md) component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: [letter spacing](../../../arkts-components/text-and-input/text/document.md#letterspacing). The default unit is fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: letter spacing. The default unit is fp.

**Since**: 15

 |
| NODE\_TEXT\_INPUT\_ENABLE\_PREVIEW\_TEXT = 7033 | 

Sets whether to enable preview text for the [TextInput](../../../arkts-components/text-and-input/textinput/document.md) component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable preview text. The default value is **true**.

**true**: Enable preview text. **false**: Disable preview text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether preview text is enabled.

**Since**: 15

 |
| NODE\_TEXT\_INPUT\_HALF\_LEADING = 7034 | 

Sets whether to enable half leading.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable half leading. The default value is **false**.

Half leading is the leading split in half and applied equally to the top and bottom edges. The value **true** means to enable half leading, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether half leading is enabled.

**Since**: 18

 |
| NODE\_TEXT\_INPUT\_KEYBOARD\_APPEARANCE = 7035 | 

Sets the appearance of the keyboard when the text box is focused.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: appearance of the keyboard. The parameter type is [ArkUI\_KeyboardAppearance](../native-type-h/document.md#arkui_keyboardappearance).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: appearance of the keyboard. The parameter type is [ArkUI\_KeyboardAppearance](../native-type-h/document.md#arkui_keyboardappearance). The default value is **ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE**.

**Since**: 15

 |
| NODE\_TEXT\_INPUT\_ENABLE\_FILL\_ANIMATION = 7036 | 

Sets whether to enable the autofill animation.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the autofill animation.

**true** to enable; **false** otherwise.

The default value is **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the autofill animation is enabled. When enabled, the animation only takes effect for text boxes whose [ArkUI\_TextInputType](../native-type-h/document.md#arkui_textinputtype) is set to **ARKUI\_TEXTINPUT\_TYPE\_PASSWORD**, **ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD**, or **ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD**.

**Since**: 20

 |
| NODE\_TEXT\_INPUT\_SHOW\_KEYBOARD\_ON\_FOCUS = 7030 | 

Sets whether to show the keyboard when the text box obtains focus. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show the keyboard when the text box obtains focus. **true**: Show the keyboard when the text box obtains focus. **false**: Do not show the keyboard when the text box obtains focus.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the keyboard is shown when the text box obtains focus.

 |
| NODE\_TEXT\_INPUT\_LINE\_HEIGHT = 7037 | 

Sets the line height of text in the text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: numeric value for the text line height. Default value: adaptive to the font size. If this parameter is set to **undefined**, the text line height is **5**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: numeric value for the text line height.

**Since**: 20

 |
| NODE\_TEXT\_INPUT\_ENABLE\_SELECTED\_DATA\_DETECTOR = 7038 | 

Sets whether to enable entity recognition for selected text.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable entity recognition for selected text. **true** indicates to enable; **false** otherwise. Default value: **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether entity recognition for selected text is enabled.

**Since**: 22

 |
| NODE\_TEXT\_INPUT\_SHOW\_COUNTER = 7040 | 

Sets whether to display a counter and its style when the number of input characters exceeds a threshold. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show a character counter. **true** to enable; **false** otherwise.

.value\[1\]?.f32: percentage of the number of characters that can be entered to the maximum number of characters allowed. When the percentage exceeds this value, the counter is displayed. The value range is \[1, 100\]. If the value is a decimal, it is rounded down. If the value is out of the range, the attribute setting does not take effect.

.value\[2\]?.i32: whether to highlight the border when the number of entered characters exceeds the maximum. **true** means to highlight; **false** otherwise.

.object: counter configuration. The configuration attributes are the color of the counter when the number of characters entered in the text box does not reach the maximum and the color of the counter when the number of characters entered in the text box exceeds the maximum. The parameter type is [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether a character counter is shown.

.value\[1\].f32: percentage of the number of characters that can be entered to the maximum number of characters allowed. When the percentage exceeds this value, the counter is displayed. The value range is \[1, 100\].

.value\[2\].i32: whether the border is highlighted when the number of entered characters exceeds the maximum. **true** indicates that the border is highlighted; **false** otherwise. The default value is **true**.

.object: counter configuration. The configuration attributes are the color of the counter when the number of characters entered in the text box does not reach the maximum and the color of the counter when the number of characters entered in the text box exceeds the maximum. The parameter type is [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md).

**Since**: 22

 |
| NODE\_TEXT\_AREA\_PLACEHOLDER = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_AREA = 8000 | 

Defines the default placeholder text of the multi-line text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: default placeholder text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: default placeholder text.

 |
| NODE\_TEXT\_AREA\_TEXT = 8001 | 

Defines the default text content for the multi-line text box. The attribute setting, attribute resetting, and attribute obtaining interfaces are supported.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: default text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: default text.

 |
| NODE\_TEXT\_AREA\_MAX\_LENGTH = 8002 | 

Defines the maximum number of characters in the text input. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: maximum number of characters in the text input.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: maximum number of characters in the text input.

 |
| NODE\_TEXT\_AREA\_PLACEHOLDER\_COLOR = 8003 | 

Defines the placeholder text color. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color value, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value, in 0xARGB format.

 |
| NODE\_TEXT\_AREA\_PLACEHOLDER\_FONT = 8004 | 

Defines the placeholder text font. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.f32: font size, in fp. Optional. The default value is **16.0**.

.value\[1\]?.i32: font style [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle). The default value is **ARKUI\_FONT\_STYLE\_NORMAL**.

.value\[2\]?.i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight). The default value is **ARKUI\_FONT\_WEIGHT\_NORMAL**.

?.string: font family. Multiple font families are separated by commas (,). For example, "font weight; font family 1, font family 2".

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: font size, in fp.

.value\[1\].i32: font style [ArkUI\_FontStyle](../native-type-h/document.md#arkui_fontstyle).

.value\[2\].i32: font weight [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight).

.string: font family. Multiple font families are separated by commas (,).

 |
| NODE\_TEXT\_AREA\_CARET\_COLOR = 8005 | 

Defines the caret color attribute, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: background color, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: background color, in 0xARGB format.

 |
| NODE\_TEXT\_AREA\_EDITING = 8006 | 

Defines the editable state for the multi-line text box. This attribute can be set and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to remain in the editable state. The value **true** means to remain in the editable state, and **false** means to exit the editable state.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for obtaining the attribute:

.value\[0\].i32: whether to remain in the editable state. The value **true** means to remain in the editable state, and **false** means to exit the editable state.

 |
| NODE\_TEXT\_AREA\_TYPE = 8007 | 

Defines the text box type. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: text box type, specified using the [ArkUI\_TextAreaType](../native-type-h/document.md#arkui_textareatype) enum. The default value is **ARKUI\_TEXTAREA\_TYPE\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: text box type, specified using the [ArkUI\_TextAreaType](../native-type-h/document.md#arkui_textareatype) enum.

 |
| NODE\_TEXT\_AREA\_SHOW\_COUNTER = 8008 | 

Sets whether to display a counter and its style when the number of input characters exceeds a threshold. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show a character counter. The value **true** means to show a character counter. The default value is **false**.

.value\[1\]?.f32: percentage of the number of characters that can be entered to the maximum number of characters allowed. When the percentage exceeds this value, the counter is displayed. The value range is \[1, 100\]. If the value is a decimal, it is rounded down. If the value is out of the range, the attribute setting does not take effect.

.value\[2\]?.i32: whether to highlight the border when the number of entered characters reaches the maximum. **true** to highlight; **false** otherwise. The default value is **true**.

.object: counter configuration. The configuration attributes are the color of the counter when the number of characters entered in the text box does not reach the maximum and the color of the counter when the number of characters entered in the text box exceeds the maximum. The parameter type is [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether a character counter is shown. The value **true** means that a character counter is shown.

.value\[1\].f32: percentage of the number of characters that can be entered to the maximum number of characters allowed. When the percentage exceeds this value, the counter is displayed. The value range is \[1, 100\].

.value\[2\].i32: whether the border is highlighted when the number of entered characters exceeds the maximum. The value **true** means that the border is highlighted.

.object: counter configuration. The configuration attributes are the color of the counter when the number of characters entered in the text box does not reach the maximum and the color of the counter when the number of characters entered in the text box exceeds the maximum. The parameter type is [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md).

 |
| NODE\_TEXT\_AREA\_SELECTION\_MENU\_HIDDEN = 8009 | 

Sets whether to hide the text selection menu when the text box is long-pressed, double-clicked, or right-clicked. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to hide the text selection menu when the text box is long-pressed, double-clicked, or right-clicked. The default value is **false**.

**true**: The system text selection menu is hidden under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box.

**false**: The system text selection menu is displayed under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the text selection menu is hidden when the text box is long-pressed, double-clicked, or right-clicked.

 |
| NODE\_TEXT\_AREA\_BLUR\_ON\_SUBMIT = 8010 | 

Sets whether the multi-line text box loses focus after the **Enter** key is pressed to submit information.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the text box loses focus after the Enter key is pressed to submit information. **true**: The text box loses focus. **false**: The text box does not lose focus.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the text box loses focus after the Enter key is pressed to submit information.

 |
| NODE\_TEXT\_AREA\_INPUT\_FILTER = 8011 | 

Sets the regular expression for input filtering. Only inputs that comply with the regular expression can be displayed. Other inputs are filtered out. For single-character input scenarios, only single-character matching is supported; for multi-character input scenarios (such as pasting), string matching is supported.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: regular expression.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: regular expression.

 |
| NODE\_TEXT\_AREA\_SELECTED\_BACKGROUND\_COLOR = 8012 | 

Sets the background color of the selected text. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color value, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value, in 0xARGB format.

 |
| NODE\_TEXT\_AREA\_ENTER\_KEY\_TYPE = 8013 | 

Defines the type of the **Enter** key. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: type of the Enter key, specified using the [ArkUI\_EnterKeyType](../native-type-h/document.md#arkui_enterkeytype) enum. The default value is **ARKUI\_ENTER\_KEY\_TYPE\_DONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: type of the Enter key, specified using the [ArkUI\_EnterKeyType](../native-type-h/document.md#arkui_enterkeytype) enum.

 |
| NODE\_TEXT\_AREA\_ENABLE\_KEYBOARD\_ON\_FOCUS = 8014 | 

Sets whether to enable the input method when the multi-line text box obtains focus in a way other than clicking. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the input method when the multi-line text box obtains focus in a way other than clicking. The value **true** means to enable the input method, and **false** means the opposite. The default value is **false**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the input method is enabled when the component obtains focus. The value **1** means that the input method is enabled when the component obtains focus, and **0** means the opposite.

 |
| NODE\_TEXT\_AREA\_CARET\_OFFSET = 8015 | 

Sets or obtains the caret position.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

Sets the position of the caret.

.value\[0\].i32: length from the start of the string to the position where the input cursor is located.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

Returns the position information of the caret. If this API is called when the caret position is updated in the current frame, it will not take effect.

.value\[0\].i32: index of the caret position.

.value\[1\].f32: x-coordinate of the caret relative to the text box.

.value\[2\].f32: y-coordinate of the caret relative to the text box.

 |
| NODE\_TEXT\_AREA\_CONTENT\_RECT = 8016 | 

Obtains the position of the edited text area relative to the component and its size.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: horizontal coordinate.

.value\[1\].f32: vertical coordinate.

.value\[2\].f32: content width.

.value\[3\].f32: content height.

 |
| NODE\_TEXT\_AREA\_CONTENT\_LINE\_COUNT = 8017 | 

Obtains the number of lines of the edited text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of lines of the edited text.

 |
| NODE\_TEXT\_AREA\_TEXT\_SELECTION = 8018 | 

Sets the text selection range and highlights the selected text when the component is focused. This API works only when the value of **selectionStart** is less than that of **selectionEnd**.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: start position of the text selection.

.value\[1\].i32: end position of the text selection.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: start position of the text selection.

.value\[1\].i32: end position of the text selection.

 |
| NODE\_TEXT\_AREA\_ENABLE\_AUTO\_FILL = 8019 | 

Sets whether to enable autofill.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable autofill. The default value is **true**.

**true** to enable; **false** otherwise.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether autofill is enabled.

 |
| NODE\_TEXT\_AREA\_CONTENT\_TYPE = 8020 | 

Sets the autofill type.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: autofill type. The parameter type is [ArkUI\_TextInputContentType](../native-type-h/document.md#arkui_textinputcontenttype).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: autofill type. The parameter type is [ArkUI\_TextInputContentType](../native-type-h/document.md#arkui_textinputcontenttype).

 |
| NODE\_TEXT\_AREA\_NUMBER\_OF\_LINES = 8022 | 

Sets the number of lines in the **TextArea** component, which can be used to work out the height of the component.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of lines.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of lines.

 |
| NODE\_TEXT\_AREA\_LETTER\_SPACING = 8023 | 

Sets the letter spacing of the **TextArea** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: [letter spacing](../../../arkts-components/text-and-input/text/document.md#letterspacing). The default unit is fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: [letter spacing](../../../arkts-components/text-and-input/text/document.md#letterspacing). The default unit is fp.

**Since**: 15

 |
| NODE\_TEXT\_AREA\_ENABLE\_PREVIEW\_TEXT = 8024 | 

Sets whether to enable preview text for the **TextArea** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable preview text. **true**: Enable preview text. **false**: Disable preview text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether preview text is enabled.

**Since**: 15

 |
| NODE\_TEXT\_AREA\_HALF\_LEADING = 8025 | 

Sets whether to enable half leading.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable half leading. The default value is **false**.

Half leading is the leading split in half and applied equally to the top and bottom edges. The value **true** means to enable half leading, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether half leading is enabled.

**Since**: 18

 |
| NODE\_TEXT\_AREA\_KEYBOARD\_APPEARANCE = 8026 | 

Sets the appearance of the keyboard when the text box is focused.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: appearance of the keyboard. The parameter type is [ArkUI\_KeyboardAppearance](../native-type-h/document.md#arkui_keyboardappearance).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: appearance of the keyboard. The parameter type is [ArkUI\_KeyboardAppearance](../native-type-h/document.md#arkui_keyboardappearance).

**Since**: 15

 |
| NODE\_TEXT\_AREA\_MAX\_LINES = 8027 | 

Sets the maximum number of lines that can be displayed with the inline style in the editing state. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: maximum number of lines that can be displayed with the inline style in the editing state. With the inline style, the default value is **3**.

With the non-inline style, the default value is +∞, indicating that there is no limit on the maximum number of lines. If this parameter is set to **undefined**, the maximum number of lines is **5**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: maximum number of lines.

**Since**: 20

 |
| NODE\_TEXT\_AREA\_LINE\_SPACING = 8028 | 

Sets the letter spacing of text in the text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: numeric value for the letter spacing. The default value is **0**, in fp. If this parameter is set to **undefined**, the letter spacing is **5**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: numeric value for the letter spacing, in fp.

**Since**: 20

 |
| NODE\_TEXT\_AREA\_MIN\_LINES = 8029 | 

Sets the minimum number of lines for the node. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum number of lines.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum number of lines.

**Since**: 20

 |
| NODE\_TEXT\_AREA\_MAX\_LINES\_WITH\_SCROLL = 8030 | 

Sets the maximum number of lines for the node when scrolling is enabled. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum number of lines when scrolling is enabled.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: maximum number of lines when scrolling is enabled.

**Since**: 20

 |
| NODE\_TEXT\_AREA\_SHOW\_KEYBOARD\_ON\_FOCUS = 8021 | 

Sets whether to show the keyboard when the text box obtains focus. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show the keyboard when the text box obtains focus. The default value is **true**.

**true**: Show the keyboard when the text box obtains focus. **false**: Do not show the keyboard when the text box obtains focus.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the keyboard is shown when the text box obtains focus.

 |
| NODE\_TEXT\_AREA\_LINE\_HEIGHT = 8031 | 

Sets the line height of text in the text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: numeric value for the text line height. Default value: adaptive to the font size. The unit is fp. If this parameter is set to **undefined**, the text line height is **5**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: numeric value for the text line height, in fp.

**Since**: 20

 |
| NODE\_TEXT\_AREA\_BAR\_STATE = 8032 | 

Defines the scrollbar status of the text input box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: scrollbar status of the text input box. The parameter type is [ArkUI\_BarState](../native-type-h/document.md#arkui_barstate). The default value is **ARKUI\_BAR\_STATE\_AUTO**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: scrollbar status of the text input box. The parameter type is [ArkUI\_BarState](../native-type-h/document.md#arkui_barstate).

**Since**: 22

 |
| NODE\_TEXT\_AREA\_ENABLE\_SELECTED\_DATA\_DETECTOR = 8033 | 

Sets whether to enable entity recognition for selected text.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable entity recognition for selected text. **true** indicates to enable; **false** otherwise. Default value: **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether entity recognition for selected text is enabled.

**Since**: 22

 |
| NODE\_TEXT\_AREA\_SCROLL\_BAR\_COLOR = 8035 | 

Defines the scrollbar color of the text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color value of the scrollbar, in 0xARGB format. Default value: **0x66182431**, which indicates gray.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value of the scrollbar.

**Since**: 22

 |
| NODE\_TEXT\_AREA\_CUSTOM\_KEYBOARD = 8036 | 

Defines the custom keyboard of the text box. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: custom keyboard. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md).

.value\[0\]?.i32: whether the custom keyboard supports avoidance.

**true**: The custom keyboard supports avoidance. **false**: The custom keyboard does not support avoidance.

Default value: **false**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: custom keyboard. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md).

.value\[0\].i32: whether the custom keyboard supports avoidance.

**Since**: 22

 |
| NODE\_BUTTON\_LABEL = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_BUTTON = 9000 | 

Defines the button text content. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: default text.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: default text.

 |
| NODE\_BUTTON\_TYPE = 9001 | 

Sets the button type. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: button style. The parameter type is [ArkUI\_ButtonType](../native-type-h/document.md#arkui_buttontype). The default value is **ARKUI\_BUTTON\_TYPE\_CAPSULE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: button style. The parameter type is [ArkUI\_ButtonType](../native-type-h/document.md#arkui_buttontype). The default value is **ARKUI\_BUTTON\_TYPE\_CAPSULE**.

 |
| NODE\_BUTTON\_MIN\_FONT\_SCALE = 9002 | 

Defines the minimum font scale factor for the button. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum font scale factor. The default unit is fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum font scale factor. The default unit is fp.

**Since**: 18

 |
| NODE\_BUTTON\_MAX\_FONT\_SCALE = 9003 | 

Defines the maximum font scale factor for the button. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum font scale factor. The default unit is fp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: maximum font scale factor. The default unit is fp.

**Since**: 18

 |
| NODE\_PROGRESS\_VALUE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_PROGRESS = 10000 | 

Defines the current value of the progress indicator. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: current value of the progress indicator.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: current value of the progress indicator.

 |
| NODE\_PROGRESS\_TOTAL = 10001 | 

Defines the total value of the progress indicator. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: total value of the progress indicator.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: total value of the progress indicator.

 |
| NODE\_PROGRESS\_COLOR = 10002 | 

Defines the color for the progress value on the progress indicator. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color value, in 0xARGB format. For example, 0xFFFF0000 indicates red.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color value, in 0xARGB format.

 |
| NODE\_PROGRESS\_TYPE = 10003 | 

Defines the type of the progress indicator. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: type of the progress indicator, specified using the [ArkUI\_ProgressType](../native-type-h/document.md#arkui_progresstype) enum. The default value is **ARKUI\_PROGRESS\_TYPE\_LINEAR**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: type of the progress indicator, specified using the [ArkUI\_ProgressType](../native-type-h/document.md#arkui_progresstype) enum.

 |
| NODE\_PROGRESS\_LINEAR\_STYLE = 10004 | 

Defines the linear progress indicator style. This attribute can be set, reset, and obtained as required through APIs. Note that the settings are effective only if the progress indicator type is linear.

.object: [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md) object that defines the component style.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md) object that defines the component style.

**Since**: 15

 |
| NODE\_CHECKBOX\_SELECT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX = 11000 | 

Defines whether the [CheckBox](../../../arkts-components/buttons-and-selections/checkbox/document.md) component is selected. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the component is selected. The value **1** means that the component is selected, and **0** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the component is selected. The value **1** means that the component is selected, and **0** means the opposite.

 |
| NODE\_CHECKBOX\_SELECT\_COLOR = 11001 | 

Defines the color of the [CheckBox](../../../arkts-components/buttons-and-selections/checkbox/document.md) component when it is selected. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the check box when it is selected, in 0xARGB format, for example, **0xFF1122FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the check box when it is selected, in 0xARGB format, for example, **0xFF1122FF**.

 |
| NODE\_CHECKBOX\_UNSELECT\_COLOR = 11002 | 

Defines the border color of the [CheckBox](../../../arkts-components/buttons-and-selections/checkbox/document.md) component when it is not selected. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: border color, in 0xARGB format, for example, **0xFF1122FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: border color, in 0xARGB format, for example, **0xFF1122FF**.

 |
| NODE\_CHECKBOX\_MARK = 11003 | 

Defines the internal icon style of the [CheckBox](../../../arkts-components/buttons-and-selections/checkbox/document.md) component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: border color, in 0xARGB format, for example, **0xFF1122FF**.

.value\[1\]?.f32: size of the internal mark, in vp. Optional.

.value\[2\]?.f32: stroke width of the internal mark, in vp. Optional. The default value is **2**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: border color, in 0xARGB format, for example, **0xFF1122FF**.

.value\[1\].f32: size of the internal mark, in vp.

.value\[2\].f32: stroke width of the internal mark, in vp. The default value is **2**.

 |
| NODE\_CHECKBOX\_SHAPE = 11004 | 

Defines the shape of the **CheckBox** component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: component shape. The parameter type is [ArkUI\_CheckboxShape](../native-type-h/document.md#arkui_checkboxshape).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: component shape. The parameter type is [ArkUI\_CheckboxShape](../native-type-h/document.md#arkui_checkboxshape).

 |
| NODE\_CHECKBOX\_NAME = 11005 | 

Defines the name of the **CheckBox** component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: component name.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: component name.

**Since**: 15

 |
| NODE\_CHECKBOX\_GROUP = 11006 | 

Defines the name of the **CheckboxGroup** component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: component name.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: component name.

**Since**: 15

 |
| NODE\_XCOMPONENT\_ID = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_XCOMPONENT = 12000 | 

Defines the ID of the **XComponent** component. This attribute can be set and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: component ID.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: component ID.

 |
| NODE\_XCOMPONENT\_TYPE = 12001 | 

Specifies the type of the **XComponent** component. This attribute is read-only.

The type of the **XComponent** component must be explicitly set during creation using **ARKUI\_NODE\_XCOMPONENT** or **ARKUI\_NODE\_XCOMPONENT\_TEXTURE** in [ArkUI\_NodeType](#arkui_nodetype), and cannot be modified afterward.

Attempting to change the type through [setAttribute](../../structs/arkui-nativenodeapi-1/document.md#setattribute) will cause rendering exceptions.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: font style [ArkUI\_XComponentType](../native-type-h/document.md#arkui_xcomponenttype).

 |
| NODE\_XCOMPONENT\_SURFACE\_SIZE = 12002 | 

Specifies the size of the **XComponent** component. This attribute is read-only.

Attempting to modify the size through [setAttribute](../../structs/arkui-nativenodeapi-1/document.md#setattribute) will have no effect.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: width, in px.

.value\[1\].u32: height, in px.

 |
| NODE\_XCOMPONENT\_SURFACE\_RECT = 12003 | 

Sets the display area of the surface held by the **XComponent** component.This attribute can be set and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: x-coordinate of the surface display area relative to the upper left corner of the **XComponent** component, in px.

.value\[1\].i32: y-coordinate of the surface display area relative to the upper left corner of the **XComponent** component, in px.

.value\[2\].i32: width of the surface display area, in px.

.value\[3\].i32: height of the surface display area, in px.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: x-coordinate of the surface display area relative to the upper left corner of the **XComponent** component, in px.

.value\[1\].i32: y-coordinate of the surface display area relative to the upper left corner of the **XComponent** component, in px.

.value\[2\].i32: width of the surface display area, in px.

.value\[3\].i32: height of the surface display area, in px.

**Since**: 18

 |
| NODE\_XCOMPONENT\_ENABLE\_ANALYZER = 12004 | 

Sets whether to enable the AI analyzer for the **XComponent** component. This attribute can be set and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the AI analyzer. **1**: enable the AI analyzer. **0**: disable the AI analyzer. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the AI analyzer is enabled. **1**: The AI analyzer is enabled. **0**: The AI analyzer is disabled. The default value is **0**.

**Since**: 18

 |
| NODE\_DATE\_PICKER\_LUNAR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_DATE\_PICKER = 13000 | 

Defines whether to display the lunar calendar in the date picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to display the lunar calendar in the date picker. The default value is **false**. **true**: Display the lunar calendar. **false**: Do not display the lunar calendar.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the lunar calendar is displayed in the date picker.

 |
| NODE\_DATE\_PICKER\_START = 13001 | 

Defines the start date of the date picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: date. The default value is **"1970-1-1"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: date.

 |
| NODE\_DATE\_PICKER\_END = 13002 | 

Defines the end date of the date picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: date. The default value is **"2100-12-31"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: date.

 |
| NODE\_DATE\_PICKER\_SELECTED = 13003 | 

Defines the selected date of the date picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: date. The default value is **"2024-01-22"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: date.

 |
| NODE\_DATE\_PICKER\_DISAPPEAR\_TEXT\_STYLE = 13004 | 

Defines the text color, font size, and font weight for the top and bottom items in the date picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are enumerated values: "bold", "normal", "bolder", "lighter", "medium", "regular".

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are **"normal"** and **"italic"**.

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_DATE\_PICKER\_TEXT\_STYLE = 13005 | 

Defines the text color, font size, and font weight of all items except the top, bottom, and selected items in the date picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are enumerated values: "bold", "normal", "bolder", "lighter", "medium", "regular".

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are **"normal"** and **"italic"**.

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_DATE\_PICKER\_SELECTED\_TEXT\_STYLE = 13006 | 

Defines the text color, font size, and font weight of the selected item in the date picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are enumerated values: "bold", "normal", "bolder", "lighter", "medium", "regular".

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are **"normal"** and **"italic"**.

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_DATE\_PICKER\_MODE = 13007 | 

Sets the date columns to be displayed. This attribute can be set, reset, and obtained as required through APIs. **DatePicker** displays different styles of date columns.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: type of date column to be displayed. The parameter type is [ArkUI\_DatePickerMode](../native-type-h/document.md#arkui_datepickermode).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: type of date column to be displayed. The parameter type is [ArkUI\_DatePickerMode](../native-type-h/document.md#arkui_datepickermode).

**Since**: 18

 |
| NODE\_DATE\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK = 13008 | 

Specifies whether to enable haptic feedback. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: whether to enable haptic feedback. The value **true** means to enable haptic feedback, and **false** means the opposite. The default value is **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].f32: whether haptic feedback is enabled.

**Since**: 18

 |
| NODE\_DATE\_PICKER\_CAN\_LOOP = 13009 | 

Defines whether to enable looping for the picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable looping. The value **true** means to enable looping, and **false** means the opposite. Default value: **true**. If an invalid value is provided, the default value is used.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].i32: The value **1** means that the looping is enabled, and **0** means the opposite.

Note: When looping is enabled, the year increments or decrements in linkage with the month's cycle, and the month increments or decrements in linkage with the day's cycle.

When looping is disabled, scrolling beyond the bounds of the year, month, or day columns is prevented, and cross-column value synchronization (between year, month, and day) is also disabled.

**Since**: 20

 |
| NODE\_TIME\_PICKER\_USE\_MILITARY\_TIME = 14001 | 

Defines whether the display time is in 24-hour format. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the display time is in 24-hour format. The default value is **false**. **true**: The display time is in 24-hour format. **false**: The display time is in 12-hour format.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the display time is in 24-hour format.

 |
| NODE\_TIME\_PICKER\_DISAPPEAR\_TEXT\_STYLE = 14002 | 

Defines the text color, font size, and font weight for the top and bottom items in the time picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are enumerated values: "bold", "normal", "bolder", "lighter", "medium", "regular".

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are **"normal"** and **"italic"**.

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_TIME\_PICKER\_TEXT\_STYLE = 14003 | 

Defines the text color, font size, and font weight of all items except the top, bottom, and selected items in the time picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are enumerated values: "bold", "normal", "bolder", "lighter", "medium", "regular".

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are **"normal"** and **"italic"**.

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_TIME\_PICKER\_SELECTED\_TEXT\_STYLE = 14004 | 

Defines the text color, font size, and font weight of the selected item in the time picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are enumerated values: "bold", "normal", "bolder", "lighter", "medium", "regular".

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are **"normal"** and **"italic"**.

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_TIME\_PICKER\_SELECTED = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TIME\_PICKER = 14000 | 

Sets the selected time for the timer picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: time. Default value: current system time. Format: only hours and minutes are supported (for example, 23:59/23-59).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: time. Default value: current system time. Format: hour, minute, and second (for example, 23,59,1).

 |
| NODE\_TIME\_PICKER\_START = 14005 | 

Sets the start time for the timer picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: time. Default value: **"0:0:0"**. Format: only hours and minutes are supported (for example, 12:59/12-59).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: time. Default value: **"0:0:0"**. Format: hour, minute, and second (for example, 12:59:0).

**Since**: 18

 |
| NODE\_TIME\_PICKER\_END = 14006 | 

Sets the end time for the timer picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: time. Default value: **"23:59:59"**. Format: only hours and minutes are supported (for example, 23:59/23-59).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: time. Default value: **"23:59:59"**. Format: hour, minute, and second (for example, 23:59:0).

**Since**: 18

 |
| NODE\_TIME\_PICKER\_ENABLE\_CASCADE = 14007 | 

Sets whether the AM/PM indicator automatically switches based on the hour in 12-hour format. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the AM/PM indicator automatically switches based on the hour in 12-hour format. The default value is **false**. The value **true** means that the AM/PM indicator automatically switches based on the hour in 12-hour format, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the AM/PM indicator automatically switches based on the hour in 12-hour format.

**Since**: 18

 |
| NODE\_TEXT\_PICKER\_OPTION\_RANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_PICKER = 15000 | 

Defines the data selection range of the text picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: type of the text picker [ArkUI\_TextPickerRangeType](../native-type-h/document.md#arkui_textpickerrangetype). The default value is **ARKUI\_TEXTPICKER\_RANGETYPE\_SINGLE**.

?.string: string input, whose format varies by picker type.

1: single-column picker. The input format is a group of strings separated by semicolons (;).

2: multi-column picker. Multiple pairs of plain text strings are supported. The pairs are separated by semicolons (;), and strings within each pair are separated by commas (,).

?.object: object input, whose format varies by picker type.

1: single-column picker with image support. The input struct is [ARKUI\_TextPickerRangeContentArray](../../structs/arkui-textpickerrangecontentarray/document.md).

2: multi-column cascading picker. The input struct is [ARKUI\_TextCascadePickerRangeContentArray](../../structs/arkui-textcascadepickerrangecontentarray/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: type of the text picker [ArkUI\_TextPickerRangeType](../native-type-h/document.md#arkui_textpickerrangetype).

?.string: string output, whose format varies by picker type.

1: single-column picker. The output format is a group of strings separated by semicolons (;).

2: multi-column picker. Multiple pairs of plain text strings are supported. The pairs are separated by semicolons (;), and strings within each pair are separated by commas (,).

 |
| NODE\_TEXT\_PICKER\_OPTION\_SELECTED = 15001 | 

Defines the index of the default selected item in the data selection range of the text picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: index. If there are multiple index values, add them one by one.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: index. If there are multiple index values, add them one by one.

 |
| NODE\_TEXT\_PICKER\_OPTION\_VALUE = 15002 | 

Defines the value of the default selected item in the text picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: value of the selected item. If there are multiple values, add them one by one and separate them with semicolons (;).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: value of the selected item. If there are multiple values, add them one by one and separate them with semicolons (;).

 |
| NODE\_TEXT\_PICKER\_DISAPPEAR\_TEXT\_STYLE = 15003 | 

Defines the text color, font size, and font weight for the top and bottom items in the text picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_TEXT\_PICKER\_TEXT\_STYLE = 15004 | 

Defines the text color, font size, and font weight for all items except the top, bottom, and selected items in the text picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are enumerated values: "bold", "normal", "bolder", "lighter", "medium", "regular".

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are **"normal"** and **"italic"**.

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_TEXT\_PICKER\_SELECTED\_TEXT\_STYLE = 15005 | 

Defines the text color, font size, and font weight of the selected item in the text picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: font size, in fp. The value is a number.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: fonts, separated by commas (,).

Parameter 5: font style. Available options are ("normal", "italic").

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: five parameters of the string type, separated by semicolons (;).

Parameter 1: text color, in #ARGB format.

Parameter 2: text size. The value is a number, and the unit is fp.

Parameter 3: font weight. Available options are ("bold", "normal", "bolder", "lighter", "medium", "regular").

Parameter 4: text font list, which is separated by commas (,).

Parameter 5: text style, string enumeration ("normal", "italic")

Example: **"#ff182431;14;normal;Arial,HarmonyOS Sans;normal"**.

 |
| NODE\_TEXT\_PICKER\_SELECTED\_INDEX = 15006 | 

Defines the index of the default selected item in the data selection range of the text picker. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter:

.value\[0...\].i32: index of the default item in the data selection range.

 |
| NODE\_TEXT\_PICKER\_CAN\_LOOP = 15007 | 

Defines whether to enable looping for the picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to support scroll looping. The value **true** means to support scroll looping, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].i32: The value **1** means that the looping is enabled, and **0** means the opposite.

 |
| NODE\_TEXT\_PICKER\_DEFAULT\_PICKER\_ITEM\_HEIGHT = 15008 | 

Defines the height of each item in the picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

value\[0\].f32: item height, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].f32: item height, in vp.

 |
| NODE\_TEXT\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK = 15010 | 

Specifies whether to enable haptic feedback. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: whether to enable haptic feedback. The value **true** means to enable haptic feedback, and **false** means the opposite. The default value is **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].f32: whether haptic feedback is enabled.

**Since**: 18

 |
| NODE\_TEXT\_PICKER\_SELECTED\_BACKGROUND\_STYLE = 15011 | 

Sets the background color and border radius of the selected item. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: background color, in 0xARGB format, for example, **0xFF1122FF**.

1: .value\[1\].f32: unified radius for all four corners, in vp.

2: .value\[1\].f32: radius of the upper left corner, in vp.

.value\[2\].f32: radius of the upper right corner, in vp.

.value\[3\].f32: radius of the lower left corner, in vp.

.value\[4\].f32: radius of the lower right corner, in vp.

Default values: background color = 0x0C182431; border radius = 24.0.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: background color, in 0xARGB format, for example, **0xFF1122FF**.

.value\[1\].f32: radius of the upper left corner, in vp.

.value\[2\].f32: radius of the upper right corner, in vp.

.value\[3\].f32: radius of the lower left corner, in vp.

.value\[4\].f32: radius of the lower right corner, in vp.

**Since**: 20

 |
| NODE\_CALENDAR\_PICKER\_HINT\_RADIUS = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CALENDAR\_PICKER = 16000 | 

Defines the style of the background in the selected state of the calendar picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: corner radius for the background in the selected state of the calendar picker. The default value is **16.0**, in vp, indicating that the background is a circle. If the value is **0.0**, the background is a right-angled rectangle. If the value is in the (0.0, 16.0) range, the background is a rounded rectangle. If the value is a negative number or greater than **16.0**, the default value **16.0** is used, which means the background is a circle.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: corner radius for the background in the selected state of the calendar picker. The default value is **16.0**, in vp, indicating that the background is a circle. The value range is \[0.0, 16.0\]. If the value is **0.0**, the background is a right-angled rectangle.

 |
| NODE\_CALENDAR\_PICKER\_SELECTED\_DATE = 16001 | 

Defines the date of the selected item in the calendar picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: year of the selected date.

.value\[1\].u32: month of the selected date.

.value\[2\].u32: day of the selected date.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: year of the selected date.

.value\[1\].u32: month of the selected date.

.value\[2\].u32: day of the selected date.

 |
| NODE\_CALENDAR\_PICKER\_EDGE\_ALIGNMENT = 16002 | 

Defines how the calendar picker is aligned with the entry component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: alignment mode. The parameter type is [ArkUI\_CalendarAlignment](../native-type-h/document.md#arkui_calendaralignment).

.value\[1\]?.f32: offset of the picker relative to the entry component along the x-axis after alignment based on the specified alignment mode.

.value\[2\]?.f32: offset of the picker relative to the entry component along the y-axis after alignment based on the specified alignment mode.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: alignment mode. The parameter type is [ArkUI\_CalendarAlignment](../native-type-h/document.md#arkui_calendaralignment).

.value\[1\].f32: offset of the picker relative to the entry component along the x-axis after alignment based on the specified alignment mode.

.value\[2\].f32: offset of the picker relative to the entry component along the y-axis after alignment based on the specified alignment mode.

 |
| NODE\_CALENDAR\_PICKER\_TEXT\_STYLE = 16003 | 

Defines the text color, font size, and font weight in the entry area of the calendar picker.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.u32: text color of the entry area.

.value\[1\]?.f32: font size of the entry area, in fp.

.value\[2\]?.i32: font weight of the entry area. The parameter type is [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: font color of the entry area.

.value\[1\].f32: font size of the entry area, in fp.

.value\[2\].i32: font weight of the entry area. The parameter type is [ArkUI\_FontWeight](../native-type-h/document.md#arkui_fontweight).

 |
| NODE\_CALENDAR\_PICKER\_START = 16004 | 

Sets the start date for the calendar picker. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: date. The value format is "YYYY-M-D", for example, **"1970-1-1"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: date.

**Since**: 18

 |
| NODE\_CALENDAR\_PICKER\_END = 16005 | 

Sets the end date for the calendar picker. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: date. The value format is "YYYY-M-D", for example, **"2100-12-31"**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: date.

**Since**: 18

 |
| NODE\_CALENDAR\_PICKER\_DISABLED\_DATE\_RANGE = 16006 | 

Sets the disabled date ranges for the calendar picker. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: string representing the disabled date ranges. The format is "start\_date,end\_date" for each range, with multiple ranges separated by commas (,).

Example: "1910-01-01,1910-12-31,2020-01-01,2020-12-31".

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: string representing the disabled date ranges.

**Since**: 19

 |
| NODE\_CALENDAR\_PICKER\_MARK\_TODAY = 16007 | 

Sets whether to highlight the current system date in the calendar picker. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

value\[0\].i32: whether to highlight the current system date in the calendar picker. The default value is **false**. The value **true** means to highlight the current system date in the calendar picker, and **false** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].i32: whether the current system date is highlighted in the calendar picker.

**Since**: 19

 |
| NODE\_SLIDER\_BLOCK\_COLOR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SLIDER = 17000 | 

Defines the color of the slider thumb. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the slider thumb, in 0xARGB format, for example, **0xFF1122FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the slider thumb, in 0xARGB format, for example, **0xFF1122FF**.

 |
| NODE\_SLIDER\_TRACK\_COLOR = 17001 | 

Defines the background color of the slider. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: background color, in 0xARGB format, for example, **0xFF1122FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: background color, in 0xARGB format, for example, **0xFF1122FF**.

 |
| NODE\_SLIDER\_SELECTED\_COLOR = 17002 | 

Defines the color of the selected part of the slider track. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the selected part of the slider track, in 0xARGB format, for example, **0xFF1122FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the selected part of the slider track, in 0xARGB format, for example, **0xFF1122FF**.

 |
| NODE\_SLIDER\_SHOW\_STEPS = 17003 | 

Sets whether to display the step scale value, which can be set, reset, and obtained as required. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to display the step scale value. The value **1** means to display the step scale value, and **0** (default value) means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the step scale value is displayed. The value **1** means that the step scale value is displayed, and **0** (default value) means the opposite.

 |
| NODE\_SLIDER\_BLOCK\_STYLE = 17004 | 

Defines the slider thumb shape, which can be set, reset, and obtained as required. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: shape. The parameter type is [ArkUI\_SliderBlockStyle](../native-type-h/document.md#arkui_sliderblockstyle).

.string?: depends on the shape. Optional.

ARKUI\_SLIDER\_BLOCK\_STYLE\_IMAGE: image resource of the slider thumb. Example: /pages/common/icon.png.

**ARKUI\_SLIDER\_BLOCK\_STYLE\_SHAPE**: custom shape of the slider thumb. In this case, the width and height values in the defined shape do not represent the actual size of the thumb; they are scaled proportionally to ensure the thumb displays correctly.

There are five types:

1\. Rectangle:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_RECTANGLE**.

.value\[2\].f32: height of the rectangle.

.value\[3\].f32: height of the rectangle.

.value\[4\].f32: height of the rounded corner of the rectangle.

.value\[5\].f32: height of the rounded corner of the rectangle.

2\. Circle:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_CIRCLE**.

.value\[2\].f32: height of the circle.

.value\[3\].f32: height of the circle.

3\. Ellipse:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_ELLIPSE**.

.value\[2\].f32: height of the ellipse.

.value\[3\].f32: height of the ellipse.

4\. Path:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_PATH**.

.value\[2\].f32: width of the path.

.value\[3\].f32: height of the path.

.string: command for drawing the path.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: shape. The parameter type is [ArkUI\_SliderBlockStyle](../native-type-h/document.md#arkui_sliderblockstyle).

.string?: depends on the shape. Optional.

ARKUI\_SLIDER\_BLOCK\_STYLE\_IMAGE: image resource of the slider thumb. Example: /pages/common/icon.png.

ARKUI\_SLIDER\_BLOCK\_STYLE\_SHAPE: custom shape of the slider thumb.

There are five types:

1\. Rectangle:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_RECTANGLE**.

.value\[2\].f32: height of the rectangle.

.value\[3\].f32: height of the rectangle.

.value\[4\].f32: height of the rounded corner of the rectangle.

.value\[5\].f32: height of the rounded corner of the rectangle.

2\. Circle:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_CIRCLE**.

.value\[2\].f32: height of the circle.

.value\[3\].f32: height of the circle.

3\. Ellipse:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_ELLIPSE**.

.value\[2\].f32: height of the ellipse.

.value\[3\].f32: height of the ellipse.

4\. Path:

.value\[1\].i32: type of shape. The parameter type is [ArkUI\_ShapeType](../native-type-h/document.md#arkui_shapetype). The value is **ARKUI\_SHAPE\_TYPE\_PATH**.

.value\[2\].f32: width of the path.

.value\[3\].f32: height of the path.

.string: command for drawing the path.

 |
| NODE\_SLIDER\_VALUE = 17005 | 

Defines the current value of the slider. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: current value.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: current value.

 |
| NODE\_SLIDER\_MIN\_VALUE = 17006 | 

Defines the minimum value of the slider. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum value.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum value.

 |
| NODE\_SLIDER\_MAX\_VALUE = 17007 | 

Defines the maximum value of the slider. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum value.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: maximum value.

 |
| NODE\_SLIDER\_STEP = 17008 | 

Defines the step of the slider. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: step. The value range is \[0.01, 100\].

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: step. The value range is \[0.01, 100\].

 |
| NODE\_SLIDER\_DIRECTION = 17009 | 

Defines the slider direction. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: display style. The parameter type is [ArkUI\_SliderDirection](../native-type-h/document.md#arkui_sliderdirection).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: display style. The parameter type is [ArkUI\_SliderDirection](../native-type-h/document.md#arkui_sliderdirection).

 |
| NODE\_SLIDER\_REVERSE = 17010 | 

Defines whether the slider values are reversed. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the slider values are reversed. The value **1** means that the slider values are reversed, and **0** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the slider values are reversed. The value **1** means that the slider values are reversed, and **0** means the opposite.

 |
| NODE\_SLIDER\_STYLE = 17011 | 

Defines the style of the slider thumb and track. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: display style. The parameter type is [ArkUI\_SliderStyle](../native-type-h/document.md#arkui_sliderstyle).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: display style. The parameter type is [ArkUI\_SliderStyle](../native-type-h/document.md#arkui_sliderstyle).

 |
| NODE\_SLIDER\_TRACK\_THICKNESS = 17012 | 

Sets the track thickness of the slider. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: track thickness of the slider, in vp. The default value is 4.0 vp when **NODE\_SLIDER\_STYLE** is set to **ARKUI\_SLIDER\_STYLE\_OUT\_SET** and 20.0 vp when **NODE\_SLIDER\_STYLE** is set to **ARKUI\_SLIDER\_STYLE\_IN\_SET**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: track thickness of the slider, in vp.

 |
| NODE\_SLIDER\_ENABLE\_HAPTIC\_FEEDBACK = 17013 | 

Specifies whether to enable haptic feedback. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: whether to enable haptic feedback. The value **true** means to enable haptic feedback, and **false** means the opposite. The default value is **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].f32: whether haptic feedback is enabled.

To enable haptic feedback, you must add **"name": "ohos.permission.VIBRATE"** under **requestPermissions** in the **module.json5** file of the project.

**Since**: 18

 |
| NODE\_SLIDER\_PREFIX = 17014 | 

Sets a custom prefix component for the start edge of the slider. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md). The prefix component is typically placed on the left in LTR layouts.

**Since**: 20

 |
| NODE\_SLIDER\_SUFFIX = 17015 | 

Sets a custom suffix component for the end edge of the slider. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md). The suffix component is typically placed on the right in LTR layouts.

**Since**: 20

 |
| NODE\_SLIDER\_BLOCK\_LINEAR\_GRADIENT\_COLOR = 17016 | 

Defines the color of the slider thumb. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

\- **colors**: colors of the color stops.

\- **stops**: stop positions of the color stops.

\- **size**: number of colors.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). Array of color stops, each of which consists of a color and its stop position.

\- **colors**: colors of the color stops.

\- **stops**: stop positions of the color stops.

\- **size**: number of colors.

**Since**: 21

 |
| NODE\_SLIDER\_TRACK\_LINEAR\_GRADIENT\_COLOR = 17017 | 

Defines the background color of the slider. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

\- **colors**: colors of the color stops.

\- **stops**: stop positions of the color stops.

\- **size**: number of colors.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). Array of color stops, each of which consists of a color and its stop position.

\- **colors**: colors of the color stops.

\- **stops**: stop positions of the color stops.

\- **size**: number of colors.

**Since**: 21

 |
| NODE\_SLIDER\_SELECTED\_LINEAR\_GRADIENT\_COLOR = 17018 | 

Defines the color of the selected part of the slider track. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

\- **colors**: colors of the color stops.

\- **stops**: stop positions of the color stops.

\- **size**: number of colors.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: The parameter type is [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md). Array of color stops, each of which consists of a color and its stop position.

\- **colors**: colors of the color stops.

\- **stops**: stop positions of the color stops.

\- **size**: number of colors.

**Since**: 21

 |
| NODE\_RADIO\_CHECKED = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_RADIO = 18000 | 

Sets whether the radio button is selected. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the radio button is selected. The default value is **false**. **true**: The radio button is selected. **false**: The radio button is not selected. Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the radio button is selected.

 |
| NODE\_RADIO\_STYLE = 18001 | 

Sets the style of the radio button in selected or deselected state. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.u32: color of the background when the radio button is selected, in 0xARGB format. The default value is **0xFF007DFF**.

.value\[1\]?.u32: color of the border when the radio button is deselected, in 0xARGB format. The default value is **0xFF182431**.

.value\[2\]?.u32: color of the indicator when the radio button is selected, in 0xARGB format. The default value is **0xFFFFFFFF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the background when the radio button is selected, in 0xARGB format. The default value is **0xFF007DFF**.

.value\[1\].u32: color of the border when the radio button is deselected, in 0xARGB format. The default value is **0xFF182431**.

.value\[2\].u32: color of the indicator when the radio button is selected, in 0xARGB format. The default value is **0xFFFFFFF**.

 |
| NODE\_RADIO\_VALUE = 18002 | 

Sets the current value of the radio button. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: value of the radio button.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: value of the radio button.

 |
| NODE\_RADIO\_GROUP = 18003 | 

Sets the name of the group to which the radio button belongs. Only one radio button in a given group can be selected at a time. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: name of the group to which the radio button belongs.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: name of the group to which the radio button belongs.

 |
| NODE\_CHECKBOX\_GROUP\_NAME = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX\_GROUP = 21000 | 

Defines the name of the **CheckboxGroup** component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: component name.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: component name.

**Since**: 15

 |
| NODE\_CHECKBOX\_GROUP\_SELECT\_ALL = 21001 | 

Defines whether to select all check boxes in the [CheckBoxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md) component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to select all check boxes in the **CheckBoxGroup** component. The value **1** means that all check boxes are selected, and **0** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the component is selected. The value **1** means that the component is selected, and **0** means the opposite.

**Since**: 15

 |
| NODE\_CHECKBOX\_GROUP\_SELECTED\_COLOR = 21002 | 

Defines the color for the selected state of the [CheckBoxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md) component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the selected state in 0xARGB format, for example, **0xFF1122FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the selected state in 0xARGB format, for example, **0xFF1122FF**.

**Since**: 15

 |
| NODE\_CHECKBOX\_GROUP\_UNSELECTED\_COLOR = 21003 | 

Defines the border color for the unselected state of the [CheckBoxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md) component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: border color in 0xARGB format, for example, **0xFF1122FF**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: border color in 0xARGB format, for example, **0xFF1122FF**.

**Since**: 15

 |
| NODE\_CHECKBOX\_GROUP\_MARK = 21004 | 

Defines the internal icon style of the [CheckBoxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md) component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: border color in 0xARGB format, for example, **0xFF1122FF**.

.value\[1\]?.f32: size of the check mark, in vp.

.value\[2\]?.f32: stroke width of the check mark, in vp. The default value is **2**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: border color in 0xARGB format, for example, **0xFF1122FF**.

.value\[1\]?.f32: size of the check mark, in vp.

.value\[2\]?.f32: stroke width of the check mark, in vp. The default value is **2**.

**Since**: 15

 |
| NODE\_CHECKBOX\_GROUP\_SHAPE = 21005 | 

Defines the shape of the [CheckBoxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md) component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: component shape. The parameter type is [ArkUI\_CheckboxShape](../native-type-h/document.md#arkui_checkboxshape).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: component shape. The parameter type is [ArkUI\_CheckboxShape](../native-type-h/document.md#arkui_checkboxshape).

**Since**: 15

 |
| NODE\_STACK\_ALIGN\_CONTENT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_STACK = 1000000 | 

Defines the alignment mode of the child components in the container. This attribute can be set, reset, and obtained as required through APIs. If this attribute and the universal attribute **NODE\_ALIGNMENT** are both set, whichever is set later takes effect.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: alignment mode. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment). The default value is **ARKUI\_ALIGNMENT\_CENTER**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: alignment mode. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment).

 |
| NODE\_SCROLL\_BAR\_DISPLAY\_MODE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SCROLL = 1002000 | 

Defines the scrollbar display mode. This attribute can be set, reset, and obtained as required through APIs. [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md), and [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md) are supported since API version 12, and [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md) is supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: scrollbar display mode. The parameter type is [ArkUI\_ScrollBarDisplayMode](../native-type-h/document.md#arkui_scrollbardisplaymode). Default value: **ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO** for the **List**, **Grid**, and **Scroll** components; **ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF** for the **WaterFlow** component.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: scrollbar display mode. The parameter type is [ArkUI\_ScrollBarDisplayMode](../native-type-h/document.md#arkui_scrollbardisplaymode).

 |
| NODE\_SCROLL\_BAR\_WIDTH = 1002001 | 

Defines the width of the scrollbar. This attribute can be set, reset, and obtained as required through APIs. [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md), and [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md) are supported since API version 12, and [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md) is supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: width of the scrollbar, in vp. The default value is **4**.

Values less than 0 are treated as the default value. The value **0** means not to show the scrollbar.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: width of the scrollbar, in vp.

 |
| NODE\_SCROLL\_BAR\_COLOR = 1002002 | 

Defines the color of the scrollbar. This attribute can be set, reset, and obtained as required through APIs. [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md), and [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md) are supported since API version 12, and [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md) is supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.data\[0\].u32: color of the scrollbar, in 0xARGB format. Default value: **0x66182431**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.data\[0\].u32: color of the scrollbar, in 0xARGB format.

 |
| NODE\_SCROLL\_SCROLL\_DIRECTION = 1002003 | 

Defines the scroll direction. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: scroll direction. The parameter type is [ArkUI\_ScrollDirection](../native-type-h/document.md#arkui_scrolldirection). The default value is **ARKUI\_SCROLL\_DIRECTION\_VERTICAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: scroll direction. The parameter type is [ArkUI\_ScrollDirection](../native-type-h/document.md#arkui_scrolldirection).

 |
| NODE\_SCROLL\_EDGE\_EFFECT = 1002004 | 

Defines the effect used at the edges of the component when the boundary of the scrollable content is reached. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: effect used at the edges of the component when the boundary of the scrollable content is reached. The parameter type is [ArkUI\_EdgeEffect](../native-type-h/document.md#arkui_edgeeffect). Default value: **ARKUI\_EDGE\_EFFECT\_NONE** for the **Grid**, **Scroll**, and **WaterFlow** components; **ARKUI\_EDGE\_EFFECT\_SPRING** for the **List** component.

.value\[1\]?.i32: whether to enable the scroll effect when the component content size is smaller than the component itself. The value **1** means to enable the scroll effect, and **0** means the opposite. Default value: **0** for the **List**, **Grid**, and **WaterFlow** components; **1** for the **Scroll** component.

.value\[2\]?.i32: direction where the edge effect takes effect. The parameter type is [ArkUI\_EffectEdge](../native-type-h/document.md#arkui_effectedge). The default value is **ARKUI\_EFFECT\_EDGE\_START**.

 |
| NODE\_SCROLL\_ENABLE\_SCROLL\_INTERACTION = 1002005 | 

Sets whether to support scroll gestures. When this attribute is set to **0**, scrolling by finger or mouse is not supported, but the scrolling controller API is not affected.

The **List**, **Scroll**, and **WaterFlow** components are supported since API version 12, and the **Grid** component is supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to support scroll gestures. The default value is **1**. **1**: Scroll gestures are supported. **0**: Scroll gestures are not supported.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether scroll gestures are supported.

 |
| NODE\_SCROLL\_FRICTION = 1002006 | 

Sets the friction coefficient. It applies only to gestures in the scrolling area, and it affects only indirectly the scroll chaining during the inertial scrolling process.

The **List**, **Scroll**, and **WaterFlow** components are supported since API version 12, and the **Grid** component is supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: friction coefficient. The default value is **0.6** for non-wearable devices and **0.9** for wearable devices. Value range: (0, +∞). If this parameter is set to a value less than or equal to 0, the default value is used.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: friction coefficient.

 |
| NODE\_SCROLL\_SNAP = 1002007 | 

Defines the scroll snapping mode of the [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md) component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: scroll snapping mode. The parameter type is [ArkUI\_ScrollSnapAlign](../native-type-h/document.md#arkui_scrollsnapalign). The default value is **ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE**.

.value\[1\].i32: whether to enable the snap to start feature. When scroll snapping is defined for the **Scroll** component, setting this attribute to **false** enables the component to scroll between the start edge and the first snap point. The default value is **true**. It is valid only when there are multiple snap points.

.value\[2\].i32: Whether to enable the snap to end feature. When scroll snapping is defined for the **Scroll** component, setting this attribute to **false** enables the component to scroll between the end edge and the last snap point. The default value is **true**. It is valid only when there are multiple snap points.

.value\[3...\].f32: snap points for the **Scroll** component. Each snap point defines the offset from an edge to which the **Scroll** component can scroll. One or more snap points are supported.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: scroll snapping mode. The parameter type is [ArkUI\_ScrollSnapAlign](../native-type-h/document.md#arkui_scrollsnapalign).

.value\[1\].i32: whether the snap is enabled to start feature. When scroll snapping is defined for the **Scroll** component, setting this attribute to **false** enables the component to scroll between the start edge and the first snap point.

.value\[2\].i32: whether the snap is enabled to end feature. When scroll snapping is defined for the **Scroll** component, setting this attribute to **false** enables the component to scroll between the end edge and the last snap point.

.value\[3...\].f32: snap points for the **Scroll** component. Each snap point defines the offset from an edge to which the **Scroll** component can scroll.

 |
| NODE\_SCROLL\_NESTED\_SCROLL = 1002008 | 

Defines nested scrolling attribute, which can be set, reset, and obtained as required through APIs. The **List**, **Scroll**, and **WaterFlow** components are supported since API version 12, and the **Grid** component is supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: nested scrolling behavior when the scrollable component scrolls toward the end edge. The parameter type is [ArkUI\_ScrollNestedMode](../native-type-h/document.md#arkui_scrollnestedmode).

.value\[1\].i32: nested scrolling behavior when the scrollable component scrolls toward the start edge. The parameter type is [ArkUI\_ScrollNestedMode](../native-type-h/document.md#arkui_scrollnestedmode).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: nested scrolling behavior when the scrollable component scrolls toward the end edge. The parameter type is [ArkUI\_ScrollNestedMode](../native-type-h/document.md#arkui_scrollnestedmode).

.value\[1\].i32: nested scrolling behavior when the scrollable component scrolls toward the start edge. The parameter type is [ArkUI\_ScrollNestedMode](../native-type-h/document.md#arkui_scrollnestedmode).

 |
| NODE\_SCROLL\_OFFSET = 1002009 | 

Defines the specified position to scroll to. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: horizontal scrolling offset, in vp. Value range: If the value is less than 0, the offset will be 0 for non-animated scrolling. A value greater than 0 triggers an animated scroll to the specified offset. By default, the scroll stops at the target offset. The **.value\[5\]?.i32** parameter can be set to enable a bounce effect when the scroll exceeds the content bounds.

.value\[1\].f32: vertical scrolling offset, in vp. Value range: If the value is less than 0, the offset will be 0 for non-animated scrolling. A value greater than 0 triggers an animated scroll to the specified offset. By default, the scroll stops at the target offset. The **.value\[5\]?.i32** parameter can be set to enable a bounce effect when the scroll exceeds the content bounds.

.value\[2\]?.i32: scrolling duration, in ms. The default value is **1000**.

.value\[3\]?.i32: scrolling curve. The parameter type is [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve). The default value is **ARKUI\_CURVE\_EASE**.

.value\[4\]?.i32: whether to enable the default spring animation. Optional. The default value **0** means not to enable the default spring animation.

.value\[5\]?.i32: whether to convert the scroll animation to an overshoot animation when the boundary is reached. The default value is **0**, meaning not to convert the scroll animation to an overshoot animation when the boundary is reached.

.value\[6\]?.i32: whether the component can stop at an overscrolled position. The default value is **0**, meaning the component cannot stop at an overscrolled position. This parameter is supported since API version 20.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: horizontal scrolling offset, in vp.

.value\[1\].f32: vertical scrolling offset, in vp.

 |
| NODE\_SCROLL\_EDGE = 1002010 | 

Defines the edge position to scroll to. This attribute can be set and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: edge position to scroll to. The parameter type is [ArkUI\_ScrollEdge](../native-type-h/document.md#arkui_scrolledge).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the container is at the edge. The value **\-1** indicates that the container is not at the edge. If the container is at the edge, the parameter type is [ArkUI\_ScrollEdge](../native-type-h/document.md#arkui_scrolledge).

 |
| NODE\_SCROLL\_ENABLE\_PAGING = 1002011 | 

Defines whether to enable the swipe-to-turn-pages feature. This attribute can be set, reset, and obtained as required through APIs. If both **enablePaging** and **scrollSnap** are set, **scrollSnap** takes effect, but **enablePaging** does not.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the swipe-to-turn-pages feature. The default value is **0**. **0**: disable; **1**: enable.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the swipe-to-turn-pages feature is enabled.

 |
| NODE\_SCROLL\_PAGE = 1002012 | 

Scrolls to the next or previous page.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to scroll to the next page. The value **0** means to scroll to the next page, and **1** means to scroll to the previous page.

.value\[1\]?.i32: whether to enable the page turning animation. The value **1** means to enable the page turning animation, and **0** means the opposite. Default value: **0**.

 |
| NODE\_SCROLL\_BY = 1002013 | 

Defines the scrolling distance.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: horizontal scrolling distance, in vp by default.

.value\[1\].f32: vertical scrolling distance, in vp by default.

 |
| NODE\_SCROLL\_FLING = 1002014 | 

Performs inertial scrolling based on the initial velocity passed in.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: initial velocity of inertial scrolling. The default unit is vp/s. If the value specified is 0, it is considered as invalid, and the scrolling for this instance will not take effect. If the value is positive, the scroll will move downward; if the value is negative, the scroll will move upward.

**Since**: 13

 |
| NODE\_SCROLL\_FADING\_EDGE = 1002015 | 

Sets the edge fade effect for the scrollable component.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the edge fade effect. **0**: Disable the edge fade effect. **1**: Enable the edge fade effect. The default value is **0**.

.value\[1\]?.f32: length of the edge fade effect, in vp. The default value is **32**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the edge fade effect is enabled. **0**: The edge fade effect is disabled. **1**: The edge fade effect is enabled.

.value\[1\].f32: length of the edge fade effect, in vp.

**Since**: 14

 |
| NODE\_SCROLL\_SIZE = 1002016 | 

Obtains the total size of all child components when fully expanded in the scrollable component. Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: total width of all child components when fully expanded in the scrollable component. The default unit is vp.

.value\[1\].f32: total height of all child components when fully expanded in the scrollable component. The default unit is vp.

When **NODE\_PADDING**, **NODE\_MARGIN**, **NODE\_BORDER\_WIDTH** is set, the values are rounded to the nearest pixel when being converted from vp to px. The return values are calculated based on these rounded pixel values.

**Since**: 14

 |
| NODE\_SCROLL\_CONTENT\_START\_OFFSET = 1002017 | 

Sets the offset from the start of the content of this scrollable component. The **List** component is supported since API version 15, and the **Grid**, **Scroll**, and **WaterFlow** components are supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: offset from the start of the content, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: offset from the start of the content, in vp.

**Since**: 15

 |
| NODE\_SCROLL\_CONTENT\_END\_OFFSET = 1002018 | 

Sets the offset from the end of the content of this scrollable component. The **List** component is supported since API version 15, and the **Grid**, **Scroll**, and **WaterFlow** components are supported since API version 22.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: offset from the end of the content, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: offset from the end of the content, in vp.

**Since**: 15

 |
| NODE\_SCROLL\_FLING\_SPEED\_LIMIT = 1002019 | 

Sets the maximum initial velocity at the start of the fling animation that occurs after gesture-driven scrolling ends. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum initial velocity at the start of the fling animation, in vp/s.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: maximum initial velocity at the start of the fling animation.

**Since**: 18

 |
| NODE\_SCROLL\_CLIP\_CONTENT = 1002020 | 

Sets the content clipping area for this scrollable component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: content clipping mode. The parameter type is [ArkUI\_ContentClipMode](../native-type-h/document.md#arkui_contentclipmode). Default value: **ARKUI\_CONTENT\_CLIP\_MODE\_BOUNDARY** for the **Grid** and **Scroll** components; **ARKUI\_CONTENT\_CLIP\_MODE\_CONTENT\_ONLY** for the **List** and **WaterFlow** components.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: content clipping mode. The parameter type is [ArkUI\_ContentClipMode](../native-type-h/document.md#arkui_contentclipmode).

**Since**: 18

 |
| NODE\_SCROLL\_BACK\_TO\_TOP = 1002021 | 

Sets whether to scroll back to the top when the status bar is clicked. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to scroll back to the top. The value **1** means to scroll back to the top, and **0** means to stay at the current position. Default value:

API versions earlier than 18: **0**. API version 18 and later: **0** for the horizontal scroll direction, and **1** for the vertical scroll direction.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether scrolling back to the top is supported.

**Since**: 15

 |
| NODE\_SCROLL\_BAR\_MARGIN = 1002022 | 

Defines the margin of the scrollbar. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: start margin of the scrollbar, in vp. The default value is **0**.

.value\[1\].f32: end margin of the scrollbar, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: start margin of the scrollbar, in vp.

.value\[1\].f32: end margin of the scrollbar, in vp.

**Since**: 20

 |
| NODE\_SCROLL\_MAX\_ZOOM\_SCALE = 1002023 | 

Sets the maximum zoom scale for scrollable content.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum zoom scale to set. Default value: **1**.

Value range: (0, +∞). If the value is less than or equal to 0, the default value is used.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: current maximum zoom scale.

**Since**: 20

 |
| NODE\_SCROLL\_MIN\_ZOOM\_SCALE = 1002024 | 

Sets the minimum zoom scale for scrollable content.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum zoom scale for scrollable content. The default value is **1**.

Value range: (0, NODE\_SCROLL\_MAX\_ZOOM\_SCALE\]. If the value is less than or equal to 0, the default value **1** is used. If the value is greater than **NODE\_SCROLL\_MAX\_ZOOM\_SCALE**, **NODE\_SCROLL\_MAX\_ZOOM\_SCALE** is used.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: current minimum zoom scale.

**Since**: 20

 |
| NODE\_SCROLL\_ZOOM\_SCALE = 1002025 | 

Sets the zoom scale for scrollable content.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: zoom scale for scrollable content. The default value is **1**.

Value range: (0, +∞). If the value is less than or equal to 0, the default value is used.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: current zoom scale.

**Since**: 20

 |
| NODE\_SCROLL\_ENABLE\_BOUNCES\_ZOOM = 1002026 | 

Sets whether to enable the zoom bounce effect when the scaling exceeds the limits.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the zoom bounce effect when the scaling exceeds the limits. The value **1** means to enable the effect, and **0** means the opposite. Default value: **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the zoom bounce effect is enabled when the scaling exceeds the limits. The value **1** means that the effect is enabled, and **0** means the opposite.

**Since**: 20

 |
| NODE\_LIST\_DIRECTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST = 1003000 | 

Sets the direction in which the [list](#arkui_nodetype) items are arranged. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: direction in which the list items are arranged. The parameter type is [ArkUI\_Axis](../native-type-h/document.md#arkui_axis). The default value is **ARKUI\_AXIS\_VERTICAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: direction in which the list items are arranged. The parameter type is [ArkUI\_Axis](../native-type-h/document.md#arkui_axis).

 |
| NODE\_LIST\_STICKY = 1003001 | 

Defines whether to pin the header to the top or the footer to the bottom in the [ListItemGroup](#arkui_nodetype) component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to pin the header to the top or the footer to the bottom in the **ListItemGroup** component. It is used together with the **ListItemGroup** component. The parameter type is [ArkUI\_StickyStyle](../native-type-h/document.md#arkui_stickystyle). The default value is **ARKUI\_STICKY\_STYLE\_NONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the header is pinned to the top or the footer to the bottom in the **ListItemGroup** component. It is used together with the **ListItemGroup** component. The parameter type is [ArkUI\_StickyStyle](../native-type-h/document.md#arkui_stickystyle).

 |
| NODE\_LIST\_SPACE = 1003002 | 

Defines the spacing between list items. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: spacing between list items along the main axis. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: spacing between list items along the main axis.

 |
| NODE\_LIST\_NODE\_ADAPTER = 1003003 | 

Defines the adapter of the **List** component. The attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object used as the adapter.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object.

 |
| NODE\_LIST\_CACHED\_COUNT = 1003004 | 

Sets the number of cached items in the adapter of the **List** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: used together with **Adapter** of the **List** component to set the number of cached items in the adapter.

.value\[1\]?.i32: whether to show cached items. The value **0** means to hide cached items, and **1** means to show cached items. The default value is **0**. This parameter is supported since API version 15.

.value\[2\]?.i32: maximum number of cached items in the **List** component. The default value is the same as that of the first parameter. This parameter is supported since API version 22.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: number of cached items in the list adapter.

.value\[1\].i32: whether cached items are shown. The value **0** means that cached items are hidden, and **1** means that cached items are shown. This parameter is supported since API version 15.

.value\[2\]?.i32: maximum number of cached items in the **List** component. This parameter is supported since API version 22.

 |
| NODE\_LIST\_SCROLL\_TO\_INDEX = 1003005 | 

Scrolls to the item with the specified index. When **smooth** is set to **true**, all passed items are loaded and counted in layout calculation. This may result in performance issues if a large number of items are involved.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: index of the item to be scrolled to in the container.

.value\[1\]?.i32: whether to enable the smooth animation for scrolling to the item with the specified index. The value **1** means to enable the animation, and **0** means the opposite. The default value is **0**.

.value\[2\]?.i32: how the item to scroll to is aligned with the container. The parameter type is [ArkUI\_ScrollAlignment](../native-type-h/document.md#arkui_scrollalignment). The default value is **ARKUI\_SCROLL\_ALIGNMENT\_START**.

.value\[3\]?.f32: extra offset, in vp. The default value is **0**. This parameter is supported since API version 15.

 |
| NODE\_LIST\_ALIGN\_LIST\_ITEM = 1003006 | 

Sets the alignment mode of list items along the cross axis when the cross-axis width of the list is greater than the cross-axis width of list items multiplied by the value of lanes. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: alignment mode of list items along the cross axis. The parameter type is [ArkUI\_ListItemAlign](../native-type-h/document.md#arkui_listitemalignment). Default value: **ARKUI\_LIST\_ITEM\_ALIGNMENT\_START**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: alignment mode of list items along the cross axis. The parameter type is [ArkUI\_ListItemAlign](../native-type-h/document.md#arkui_listitemalignment).

 |
| NODE\_LIST\_CHILDREN\_MAIN\_SIZE = 1003007 | 

Sets the default main axis size of the child components in this list.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

object: [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md) object.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

object: [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md) object.

 |
| NODE\_LIST\_INITIAL\_INDEX = 1003008 | 

Sets the item displayed at the beginning of the viewport when the current list is loaded for the first time. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: item displayed at the beginning of the viewport when the current list is loaded for the first time. Default value: **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: item displayed at the beginning of the viewport when the current list is loaded for the first time.

 |
| NODE\_LIST\_DIVIDER = 1003009 | 

Defines the style of the divider for the list items. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the divider, in 0xARGB format. The default value is **0x08000000**.

.value\[1\].f32: stroke width of the divider, in vp. The default value is **0**.

.value\[2\].f32: distance between the divider and the start of the list, in vp. The default value is **0**.

.value\[3\].f32: distance between the divider and the end of the list, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the divider, in 0xARGB format.

.value\[1\].f32: stroke width of the divider.

.value\[2\].f32: distance between the divider and the start of the list, in vp.

.value\[3\].f32: distance between the divider and the end of the list, in vp.

 |
| NODE\_LIST\_SCROLL\_TO\_INDEX\_IN\_GROUP = 1003010 | 

Scrolls to the item with the specified index in the specified [list item group](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md). When **smooth** is set to **true**, all passed items are loaded and counted in layout calculation. This may result in performance issues if a large number of items are involved.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: index of the target [list item group](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md) in the current [list](../../../arkts-components/scroll-and-swipe/list/document.md).

.value\[1\].i32: index of the target [list item](../../../arkts-components/scroll-and-swipe/listitem/document.md) in the [list item group](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md).

.value\[2\]?.i32: whether to enable the smooth animation for scrolling to the item with the specified index. The value **1** means to enable the animation, and **0** means the opposite. The default value is **0**.

.value\[3\]?.i32: how the item to scroll to is aligned with the container. The parameter type is [ArkUI\_ScrollAlignment](../native-type-h/document.md#arkui_scrollalignment). The default value is **ARKUI\_SCROLL\_ALIGNMENT\_START**.

**Since**: 15

 |
| NODE\_LIST\_LANES = 1003011 | 

Sets the number of lanes in a list. (The number of columns is used when the list is scrolled vertically, and the number of rows is used when the list is scrolled horizontally.) This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: number of lanes in the list. If the maximum and minimum lane widths are set, setting the number of lanes will not take effect. The default value is **1**. The value range is \[1, +∞). If an abnormal value is set, the default value is used.

.value\[1\]?.f32: minimum lane width, in vp.

.value\[2\]?.f32: maximum column width, in vp.

.value\[3\]?.f32: lane spacing, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: number of lanes in the list.

.value\[1\].f32: minimum lane width, in vp.

.value\[2\].f32: maximum lane width, in vp.

.value\[3\].f32: lane spacing, in vp.

**Since**: 15

 |
| NODE\_LIST\_SCROLL\_SNAP\_ALIGN = 1003012 | 

Sets the scroll snap alignment mode for the **List** component.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: scroll snapping mode. The parameter type is [ArkUI\_ScrollSnapAlign](../native-type-h/document.md#arkui_scrollsnapalign). The default value is **ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: scroll snapping mode. The parameter type is [ArkUI\_ScrollSnapAlign](../native-type-h/document.md#arkui_scrollsnapalign).

**Since**: 15

 |
| NODE\_LIST\_MAINTAIN\_VISIBLE\_CONTENT\_POSITION = 1003013 | 

Sets whether to maintain the visible content's position when data is inserted or deleted outside the display area of the **List** component.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to maintain the visible content's position when data is inserted or deleted outside the display area of the **List** component. The value **0** means not to maintain the visible content's position, and **1** means the opposite. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the visible content's position is maintained when data is inserted or deleted outside the display area of the **List** component. The value **0** means not to maintain the visible content's position, and **1** means the opposite. The default value is **0**.

**Since**: 15

 |
| NODE\_LIST\_STACK\_FROM\_END = 1003014 | 

Sets whether the **List** component starts layout from the end.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the **List** component starts layout from the end. The value **0** means layout starts from the top, and **1** means layout starts from the end. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the **List** component starts layout from the end. The value **0** means layout starts from the top, and **1** means layout starts from the end. The default value is **0**.

**Since**: 19

 |
| NODE\_LIST\_FOCUS\_WRAP\_MODE = 1003015 | 

Defines the focus wrap mode for the **List** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: focus wrap mode of the **List** component. The parameter type is [ArkUI\_FocusWrapMode](../native-type-h/document.md#arkui_focuswrapmode). The default value is **ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: focus wrap mode of the **List** component. The parameter type is [ArkUI\_FocusWrapMode](../native-type-h/document.md#arkui_focuswrapmode).

**Since**: 20

 |
| NODE\_LIST\_SYNC\_LOAD = 1003016 | 

Defines whether the **List** component loads child nodes synchronously. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the **List** component synchronously loads child nodes. **0**: frame-by-frame loading. **1**: synchronous loading. Default value: **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the **List** component synchronously loads child nodes. **0**: frame-by-frame loading. **1**: synchronous loading.

**Since**: 20

 |
| NODE\_LIST\_SCROLL\_SNAP\_ANIMATION\_SPEED = 1003017 | 

Defines the scroll snap animation speed for the **List** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: scroll snap animation speed for the **List** component. The parameter type is [ArkUI\_ScrollSnapAnimationSpeed](../native-type-h/document.md#arkui_scrollsnapanimationspeed). Default value: **ARKUI\_SCROLL\_SNAP\_ANIMATION\_NORMAL**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: scroll snap animation speed for the **List** component. The parameter type is [ArkUI\_ScrollSnapAnimationSpeed](../native-type-h/document.md#arkui_scrollsnapanimationspeed).

**Since**: 22

 |
| NODE\_LIST\_LANES\_ITEMFILLPOLICY = 1003018 | 

Defines the responsive column layout policy of the **List** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of columns at different breakpoint specifications. The parameter type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

.value\[1\]?.f32: column spacing, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of columns at different breakpoint specifications. The parameter type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

.value\[1\].f32: column spacing, in vp.

**Since**: 22

 |
| NODE\_SWIPER\_LOOP = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SWIPER = 1001000 | 

Defines whether to enable loop playback for the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable loop playback. The value **1** means to enable loop playback, and **0** means the opposite. The default value is **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether loop playback is enabled. The value **1** means that loop playback is enabled, and **0** means the opposite. The default value is **1**.

 |
| NODE\_SWIPER\_AUTO\_PLAY = 1001001 | 

Defines whether to enable automatic playback for child component switching in the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable automatic playback for child component switching. The value **1** means to enable automatic playback, and **0** means the opposite. The default value is **0**.

.value\[1\]?.i32: whether to stop automatic playback when the user touches the screen. The value **0** means to stop automatic playback, and **1** means the opposite. The default value is **0**. This parameter is supported since API version 16.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether automatic playback is enabled for child component switching. The value **1** means that automatic playback is enabled, and **0** means the opposite. The default value is **0**.

.value\[1\].i32: whether automatic playback is stopped when the user touches the screen. The value **0** means that automatic playback is stopped, and **1** means the opposite. This parameter is supported since API version 16.

 |
| NODE\_SWIPER\_SHOW\_INDICATOR = 1001002 | 

Defines whether to enable the navigation indicator for the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to enable the navigation indicator. The value **1** means to enable the navigation indicator, and **0** means the opposite. The default value is **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the navigation indicator is enabled. The value **1** means that the navigation indicator is enabled, and **0** means the opposite. The default value is **1**.

 |
| NODE\_SWIPER\_INTERVAL = 1001003 | 

Defines the interval for automatic playback. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: interval for automatic playback, in ms.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: interval for automatic playback, in ms.

 |
| NODE\_SWIPER\_VERTICAL = 1001004 | 

Defines whether vertical swiping is used for the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether vertical swiping is used. The value **1** means that vertical swiping is used, and **0** means the opposite. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether vertical swiping is used. The value **1** means that vertical swiping is used, and **0** means the opposite. The default value is **0**.

 |
| NODE\_SWIPER\_DURATION = 1001005 | 

Defines the duration of the animation for switching child components. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: duration of the animation for switching child components, in ms. The default value is **400**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: duration of the animation for switching child components, in ms. The default value is **400**.

 |
| NODE\_SWIPER\_CURVE = 1001006 | 

Defines the animation curve for the swiper. This attribute can be set, reset, and obtained as required through APIs. If this attribute is not set or reset, the animation curve is [interpolatingSpring](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesinterpolatingspring10)(-1, 1, 328, 34). If an exception occurs when setting this attribute, the default value **ARKUI\_CURVE\_LINEAR** is used.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: animation curve. The parameter type is [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve). The default value is **ARKUI\_CURVE\_LINEAR**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: animation curve. The parameter type is [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve). The default value is **ARKUI\_CURVE\_LINEAR**.

 |
| NODE\_SWIPER\_ITEM\_SPACE = 1001007 | 

Defines the spacing between child components in the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: spacing between child components.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: spacing between child components.

 |
| NODE\_SWIPER\_INDEX = 1001008 | 

Defines the index of the child component currently displayed in the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of elements to display per page.

.value\[1\]?.i32: switching animation mode. The parameter type is [ArkUI\_SwiperAnimationMode](../native-type-h/document.md#arkui_swiperanimationmode). The setting is only effective for the current call.

This parameter is supported since API version 15.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of elements to display per page.

 |
| NODE\_SWIPER\_DISPLAY\_COUNT = 1001009 | 

Defines the number of elements to display per page. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of elements to display within the viewport.

.value\[1\]?.i32: whether to paginate by group. The value **0** means to paginate by individual child elements, and **1** means to paginate by groups of child elements displayed within the viewport. The default value is **0**.

.string?: whether to enable auto-adaptation. This parameter accepts only the value **"auto"**. When this parameter is set to **"auto"**, the **value\[\]** parameters are ignored.

This parameter is supported since API version 19.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of elements to display within the viewport.

.value\[1\].i32: whether to paginate by group. This parameter is supported since API version 19.

 |
| NODE\_SWIPER\_DISABLE\_SWIPE = 1001010 | 

Sets whether to disable the swipe-to-switch feature of the **Swiper** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to disable the swipe-to-switch feature. The value **1** means to disable the feature, and **0** means the opposite. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the swipe-to-switch feature is disabled. The value **1** means that the feature is disabled, and **0** means the opposite. The default value is **0**.

 |
| NODE\_SWIPER\_SHOW\_DISPLAY\_ARROW = 1001011 | 

Defines whether to show the arrow when the mouse pointer hovers over the navigation indicator. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to show the arrow when the mouse pointer hovers over the navigation indicator. The parameter type is [ArkUI\_SwiperArrow](../native-type-h/document.md#arkui_swiperarrow). The default value is **ARKUI\_SWIPER\_ARROW\_HIDE**.

.?object: style of the arrow displayed when the mouse pointer hovers over the navigation indicator. The parameter type is [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md). This parameter is supported since API version 19.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the arrow is shown when the mouse pointer hovers over the navigation indicator. The parameter type is [ArkUI\_SwiperArrow](../native-type-h/document.md#arkui_swiperarrow).

.object: style of the arrow displayed when the mouse pointer hovers over the navigation indicator. The parameter type is [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md). This parameter is supported since API version 19.

 |
| NODE\_SWIPER\_EDGE\_EFFECT\_MODE = 1001012 | 

Defines the effect used at the edges of the swiper when the boundary of the scrollable content is reached. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: effect used at the edges of the component when the boundary of the scrollable content is reached. The parameter type is [ArkUI\_EdgeEffect](../native-type-h/document.md#arkui_edgeeffect).

The default value is **ARKUI\_EDGE\_EFFECT\_SPRING**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: effect used at the edges of the component when the boundary of the scrollable content is reached. The parameter type is [ArkUI\_EdgeEffect](../native-type-h/document.md#arkui_edgeeffect).

 |
| NODE\_SWIPER\_NODE\_ADAPTER = 1001013 | 

Defines the swiper adapter. The attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object used as the adapter.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object.

 |
| NODE\_SWIPER\_CACHED\_COUNT = 1001014 | 

Sets the number of cached items in the swiper adapter. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of cached items in the swiper adapter.

.value\[1\]?.i32: whether to show cached items. The value **0** means to hide cached items, and **1** means to show cached items. The default value is **0**. This parameter is supported since API version 19.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of cached items in the list adapter.

.value\[1\].i32: whether cached items are shown. The value **0** means that cached items are hidden, and **1** means that cached items are shown. This parameter is supported since API version 19.

 |
| NODE\_SWIPER\_PREV\_MARGIN = 1001015 | 

Sets the leading margin of the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: leading margin, in vp. The default value is **0**.

.value\[1\].i32: whether to ignore blank areas. The value **1** means to ignore blank areas, and **0** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: leading margin, in vp. .value\[1\].i32: whether blank areas are ignored. The value **1** means that blank areas are ignored, and **0** means the opposite.

 |
| NODE\_SWIPER\_NEXT\_MARGIN = 1001016 | 

Sets the trailing margin of the swiper. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: trailing margin, in vp. The default value is **0**.

.value\[1\].i32: whether to ignore blank areas. The value **1** means to ignore blank areas, and **0** means the opposite.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: trailing margin, in vp. .value\[1\].i32: whether blank areas are ignored. The value **1** means that blank areas are ignored, and **0** means the opposite.

 |
| NODE\_SWIPER\_INDICATOR = 1001017 | 

Sets the navigation indicator type of the **Swiper** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: navigation indicator type. The parameter type is [ArkUI\_SwiperIndicatorType](../native-type-h/document.md#arkui_swiperindicatortype).

.object: additional configuration for the navigation indicator, depending on the type. For **ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT**, the parameter type is [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md).

For **ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT**, the parameter type is [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md).

The **ArkUI\_SwiperDigitIndicator** type is supported since API version 19. Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: navigation indicator type. The parameter type is [ArkUI\_SwiperIndicatorType](../native-type-h/document.md#arkui_swiperindicatortype).

.object: additional configuration for the navigation indicator, depending on the type. For **ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT**, the parameter type is [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md).

For **ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT**, the parameter type is [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md).

The **ArkUI\_SwiperDigitIndicator** type is supported since API version 19.

 |
| NODE\_SWIPER\_NESTED\_SCROLL = 1001018 | 

Sets the nested scrolling mode of the **Swiper** component and its parent container.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: nested scrolling mode. The parameter type is [ArkUI\_SwiperNestedScrollMode](../native-type-h/document.md#arkui_swipernestedscrollmode).

The default value is **ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_ONLY**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: nested scrolling mode. The parameter type is [ArkUI\_SwiperNestedScrollMode](../native-type-h/document.md#arkui_swipernestedscrollmode).

 |
| NODE\_SWIPER\_SWIPE\_TO\_INDEX = 1001019 | 

Sets the swiper to switch to the specified page.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: index of the target page in the swiper.

.value\[1\]?.i32: whether to use an animation for when the target page is reached. The value **1** indicates that the dynamic effect is enabled, and the value **0** indicates that the dynamic effect is disabled. The default value is **0**.

 |
| NODE\_SWIPER\_INDICATOR\_INTERACTIVE = 1001020 | 

Sets whether the navigation indicator is interactive.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the navigation indicator is interactive. The default value **true** means that the navigation indicator is interactive, and **false** means the opposite. The default value is **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the navigation indicator is interactive.

 |
| NODE\_SWIPER\_PAGE\_FLIP\_MODE = 1001021 | 

Sets the page flipping mode using the mouse wheel.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: page flipping mode using the mouse wheel. The parameter type is [ArkUI\_PageFlipMode](../native-type-h/document.md#arkui_pageflipmode).

Format of the return value [ArkUI\_PageFlipMode](../native-type-h/document.md#arkui_pageflipmode):

.value\[0\].i32: page flipping mode using the mouse wheel.

**Since**: 15

 |
| NODE\_SWIPER\_AUTO\_FILL = 1001022 | 

Configures the **Swiper** component to automatically adjust the number of elements displayed per page based on the minimum width of the elements. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum width of the elements to be displayed, in vp.

.value\[1\]?.i32: whether to paginate by group. The value **0** means to paginate by individual child elements, and **1** means to paginate by groups of child elements displayed within the viewport. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum width of the elements to be displayed, in vp.

.value\[1\].i32: whether pagination by group is enabled.

**Since**: 19

 |
| NODE\_SWIPER\_MAINTAIN\_VISIBLE\_CONTENT\_POSITION = 1001023 | 

Sets whether to maintain the visible content's position when data is inserted or deleted outside the display area of the **Swiper** component.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to maintain the visible content's position when data is inserted or deleted outside the display area of the **Swiper** component. The value **0** means not to maintain the visible content's position, and **1** means the opposite. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the visible content's position is maintained when data is inserted or deleted outside the display area of the **Swiper** component. The value **0** means that the visible content's position is not maintained, and **1** means the opposite. The default value is **0**.

**Since**: 20

 |
| NODE\_SWIPER\_ITEMFILLPOLICY = 1001024 | 

Defines the responsive column layout policy of the **Swiper** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of columns at different breakpoint specifications. The parameter type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

.value\[1\]?.i32: whether to paginate by group. The value **0** means to paginate by individual child elements, and **1** means to paginate by groups of child elements displayed within the viewport. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of columns at different breakpoint specifications. The parameter type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

.value\[1\].i32: whether pagination by group is enabled.

**Since**: 22

 |
| NODE\_LIST\_ITEM\_SWIPE\_ACTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST\_ITEM = 1004000 | 

Sets the swipe action item displayed when the list item is swiped out from the screen edge. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md) object.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md) object.

 |
| NODE\_LIST\_ITEM\_GROUP\_SET\_HEADER = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST\_ITEM\_GROUP = 1005000 | 

Defines the header of the list item group. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) object used as the header of the list item group.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) object used as the header of the list item group.

 |
| NODE\_LIST\_ITEM\_GROUP\_SET\_FOOTER = 1005001 | 

Defines the footer of the list item group. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) object used as the footer of the list item group.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) object used as the footer of the list item group.

 |
| NODE\_LIST\_ITEM\_GROUP\_SET\_DIVIDER = 1005002 | 

Defines the style of the divider for the list items. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].u32: color of the divider, in 0xARGB format. The default value is **0x08000000**.

.value\[1\].f32: stroke width of the divider, in vp. The default value is **0**.

.value\[2\].f32: distance between the divider and the start of the list, in vp. The default value is **0**.

.value\[3\].f32: distance between the divider and the end of the list, in vp. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].u32: color of the divider, in 0xARGB format.

.value\[1\].f32: stroke width of the divider, in vp.

.value\[2\].f32: distance between the divider and the start of the list, in vp.

.value\[3\].f32: distance between the divider and the end of the list, in vp.

 |
| NODE\_LIST\_ITEM\_GROUP\_CHILDREN\_MAIN\_SIZE = 1005003 | 

Sets the default main axis size of the **ListItemGroup** child components.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

object: [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md) object.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md) object.

 |
| NODE\_LIST\_ITEM\_GROUP\_NODE\_ADAPTER = 1005004 | 

Defines the adapter of the [ListItemGroup](#arkui_nodetype) component. The attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object used as the adapter.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object.

**Since**: 15

 |
| NODE\_COLUMN\_ALIGN\_ITEMS = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_COLUMN = 1006000 | 

Defines the horizontal alignment mode of child components in the column. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: horizontal alignment mode of child components. The parameter type is [ArkUI\_HorizontalAlignment](../native-type-h/document.md#arkui_horizontalalignment).

Default value: **ARKUI\_HORIZONTAL\_ALIGNMENT\_CENTER**

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: horizontal alignment mode of child components. The parameter type is [ArkUI\_HorizontalAlignment](../native-type-h/document.md#arkui_horizontalalignment).

 |
| NODE\_COLUMN\_JUSTIFY\_CONTENT = 1006001 | 

Defines the vertical alignment mode of child components in the **Column** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: vertical alignment mode of child components. The parameter type is [ArkUI\_FlexAlignment](../native-type-h/document.md#arkui_flexalignment).

Default value: **ARKUI\_FLEX\_ALIGNMENT\_START**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: vertical alignment mode of child components. The parameter type is [ArkUI\_FlexAlignment](../native-type-h/document.md#arkui_flexalignment).

 |
| NODE\_ROW\_ALIGN\_ITEMS = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_ROW = 1007000 | 

Defines the vertical alignment mode of child components in the **Row** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: vertical alignment mode of child components. The parameter type is [ArkUI\_VerticalAlignment](../native-type-h/document.md#arkui_verticalalignment).

Default value: **ARKUI\_VERTICAL\_ALIGNMENT\_CENTER**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: vertical alignment mode of child components. The parameter type is [ArkUI\_VerticalAlignment](../native-type-h/document.md#arkui_verticalalignment).

 |
| NODE\_ROW\_JUSTIFY\_CONTENT = 1007001 | 

Defines the horizontal alignment mode of child components in the **Row** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: horizontal alignment mode of child components. The parameter type is [ArkUI\_FlexAlignment](../native-type-h/document.md#arkui_flexalignment).

Default value: **ARKUI\_FLEX\_ALIGNMENT\_START**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: horizontal alignment mode of child components. The parameter type is [ArkUI\_FlexAlignment](../native-type-h/document.md#arkui_flexalignment).

 |
| NODE\_FLEX\_OPTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_FLEX = 1008000 | 

Sets **Flex** attributes, which can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\]?.i32: direction in which child components are arranged within the **Flex** container. The parameter type is [ArkUI\_FlexDirection](../native-type-h/document.md#arkui_flexdirection). The default value is **ARKUI\_FLEX\_DIRECTION\_ROW**.

.value\[1\]?.i32: wrapping rule [ArkUI\_FlexWrap](../native-type-h/document.md#arkui_flexwrap). The default value is **ARKUI\_FLEX\_WRAP\_NO\_WRAP**.

.value\[2\]?.i32: alignment mode along the main axis. The parameter type is [ArkUI\_FlexAlignment](../native-type-h/document.md#arkui_flexalignment). The default value is **ARKUI\_FLEX\_ALIGNMENT\_START**.

.value\[3\]?.i32: alignment mode along the cross axis. The parameter type is [ArkUI\_ItemAlignment](../native-type-h/document.md#arkui_itemalignment). The default value is **ARKUI\_ITEM\_ALIGNMENT\_START**.

.value\[4\]?.i32: alignment mode for multi-line content when there is extra space in the cross axis. The parameter type is [ArkUI\_FlexAlignment](../native-type-h/document.md#arkui_flexalignment). The default value is **ARKUI\_FLEX\_ALIGNMENT\_START**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: direction in which child components are arranged within the **Flex** container.

.value\[1\].i32: wrapping rule.

.value\[2\].i32: alignment mode along the main axis.

.value\[3\].i32: alignment mode along the cross axis.

.value\[4\].i32: alignment mode for multi-line content when there is extra space in the cross axis.

 |
| NODE\_REFRESH\_REFRESHING = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_REFRESH = 1009000 | 

Sets whether the component is being refreshed. This attribute can be set and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the component is being refreshed. **1**: being refreshed. **0**: not being refreshed. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the component is being refreshed. **1**: being refreshed. **0**: not being refreshed.

 |
| NODE\_REFRESH\_CONTENT = 1009001 | 

Sets the custom content in the pull-down area. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: custom content. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md).

 |
| NODE\_REFRESH\_PULL\_DOWN\_RATIO = 1009002 | 

Sets the pull-down follow ratio. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: pull-down follow ratio. The value is in the range from 0 to 1.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: pull-down follow ratio. The value is in the range from 0 to 1.

 |
| NODE\_REFRESH\_OFFSET = 1009003 | 

Sets the pull-down offset that triggers refresh. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: pull-down offset, in vp. The default value is 64 vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: pull-down offset, in vp. The default value is 64 vp.

 |
| NODE\_REFRESH\_PULL\_TO\_REFRESH = 1009004 | 

Sets whether to initiate a refresh when the pull-down distance exceeds the value of **refreshOffset**. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether to initiate a refresh. The value **true** means to initiate a refresh, and **false** means the opposite. The default value is **true**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether a refresh is initiated. The value **1** means that a refresh is initiated, and **0** means the opposite.

 |
| NODE\_REFRESH\_MAX\_PULL\_DOWN\_DISTANCE = 1009005 | 

Sets the maximum pull-down distance for refreshing. This attribute can be set, reset, and obtained through the API as required. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: maximum pull-down distance, in vp.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: maximum pull-down distance, in vp.

**Since**: 20

 |
| NODE\_WATER\_FLOW\_LAYOUT\_DIRECTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_WATER\_FLOW = 1010000 | 

Defines the main axis direction of the **WaterFlow** component layout. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32 main axis direction. The parameter type is [ArkUI\_FlexDirection](../native-type-h/document.md#arkui_flexdirection). Default value: **ARKUI\_FLEX\_DIRECTION\_COLUMN**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32 main axis direction. The parameter type is [ArkUI\_FlexDirection](../native-type-h/document.md#arkui_flexdirection).

 |
| NODE\_WATER\_FLOW\_COLUMN\_TEMPLATE = 1010001 | 

Sets the number of columns in the water flow layout. If this parameter is not set, one column is used by default. This attribute can be set, reset, and obtained as required through APIs. For example, **'1fr 1fr 2fr'** indicates three columns, with the first column taking up 1/4 of the parent component's full width, the second column 1/4, and the third column 2/4. You can use **columnsTemplate('repeat(auto-fill,track-size)')** to automatically calculate the number of rows based on the specified row height **track-size**. **repeat** and **auto-fill** are keywords. The units for **track-size** can be px, vp (default), %, or a valid number. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: number of columns in the layout. Default value: **'1fr'**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: number of columns in the layout.

 |
| NODE\_WATER\_FLOW\_ROW\_TEMPLATE = 1010002 | 

Sets the number of rows in the water flow layout. If this parameter is not set, one row is used by default. This attribute can be set, reset, and obtained as required through APIs. For example, **'1fr 1fr 2fr'** indicates three rows, with the first row taking up 1/4 of the parent component's full height, the second row 1/4, and the third row 2/4. You can use **rowsTemplate('repeat(auto-fill,track-size)')** to automatically calculate the number of rows based on the specified row height **track-size**. **repeat** and **auto-fill** are keywords. The units for **track-size** can be px, vp (default), %, or a valid number. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: number of rows in the layout. Default value: **'1fr'**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: number of rows in the layout.

 |
| NODE\_WATER\_FLOW\_COLUMN\_GAP = 1010003 | 

Sets the gap between columns. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: gap between columns, in vp. The default value is **0**. Value range: \[0, +∞).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: gap between columns, in vp.

 |
| NODE\_WATER\_FLOW\_ROW\_GAP = 1010004 | 

Sets the gap between rows. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: gap between rows, in vp. The default value is **0**. Value range: \[0, +∞).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: gap between rows, in vp.

 |
| NODE\_WATER\_FLOW\_SECTION\_OPTION = 1010005 | 

Defines the water flow section configuration. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: zero-based index of the water flow item section to update. The value is converted to an integer.

.object: [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md) object.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md) object.

 |
| NODE\_WATER\_FLOW\_NODE\_ADAPTER = 1010006 | 

Defines the **WaterFlow** component adapter. The attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object used as the adapter.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object.

 |
| NODE\_WATER\_FLOW\_CACHED\_COUNT = 1010007 | 

Sets the number of cached items in the **WaterFlow** component adapter. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of cached items in the **WaterFlow** component adapter.

.value\[1\]?.i32: whether to show cached items. The value **0** means to hide cached items, and **1** means to show cached items. The default value is **0**. This parameter is supported since API version 16.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: number of cached items in the list adapter.

.value\[1\].i32: whether cached items are shown. The value **0** means that cached items are hidden, and **1** means that cached items are shown. This parameter is supported since API version 16.

 |
| NODE\_WATER\_FLOW\_FOOTER = 1010008 | 

Sets the custom footer for the **WaterFlow** component. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: custom content. The parameter type is [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md).

 |
| NODE\_WATER\_FLOW\_SCROLL\_TO\_INDEX = 1010009 | 

Scrolls to the item with the specified index. When **smooth** is set to **true**, all passed items are loaded and counted in layout calculation. This may result in performance issues if a large number of items are involved.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: index of the item to be scrolled to in the container.

.value\[1\]?.i32: whether to enable the smooth animation for scrolling to the item with the specified index. The value **1** means to enable the animation, and **0** means the opposite. The default value is **0**.

.value\[2\]?.i32: how the item to scroll to is aligned with the container. The parameter type is [ArkUI\_ScrollAlignment](../native-type-h/document.md#arkui_scrollalignment). The default value is **ARKUI\_SCROLL\_ALIGNMENT\_START**.

 |
| NODE\_WATER\_FLOW\_ITEM\_CONSTRAINT\_SIZE = 1010010 | 

Defines the size constraints to apply to water flow items. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: minimum width. The value **\-1** indicates that the minimum width is not set.

.value\[1\].f32: maximum width. The value **\-1** indicates that the maximum width is not set.

.value\[2\].f32: minimum height. The value **\-1** indicates that the minimum height is not set.

.value\[3\].f32: maximum height. The value **\-1** indicates that the maximum height is not set.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: minimum width. The value **\-1** indicates that the minimum width is not set.

.value\[1\].f32: maximum width. The value **\-1** indicates that the maximum width is not set.

.value\[2\].f32: minimum height. The value **\-1** indicates that the minimum height is not set.

.value\[3\].f32: maximum height. The value **\-1** indicates that the maximum height is not set.

 |
| NODE\_WATER\_FLOW\_LAYOUT\_MODE = 1010011 | 

Sets the layout mode for this **WaterFlow** component. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: layout mode. The parameter type is [ArkUI\_WaterFlowLayoutMode](../native-type-h/document.md#arkui_waterflowlayoutmode). The default value is **ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_ALWAYS\_TOP\_DOWN**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: layout mode. The parameter type is [ArkUI\_WaterFlowLayoutMode](../native-type-h/document.md#arkui_waterflowlayoutmode).

**Since**: 18

 |
| NODE\_WATER\_FLOW\_SYNC\_LOAD = 1010012 | 

Defines whether the **WaterFlow** component loads child nodes synchronously. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the **WaterFlow** component synchronously loads child nodes. **0**: frame-by-frame loading. **1**: synchronous loading. Default value: **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the **WaterFlow** component synchronously loads child nodes. **0**: frame-by-frame loading. **1**: synchronous loading.

**Since**: 20

 |
| NODE\_WATER\_FLOW\_COLUMN\_TEMPLATE\_ITEMFILLPOLICY = 1010013 | 

Sets the responsive column layout policy for the **WaterFlow** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of columns at different breakpoint specifications. The data type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of columns at different breakpoint specifications. The data type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

**Since**: 22

 |
| NODE\_RELATIVE\_CONTAINER\_GUIDE\_LINE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_RELATIVE\_CONTAINER = 1012000 | 

Sets the guideline in the **RelativeContainer** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: guideline in the **RelativeContainer** component.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: guideline in the **RelativeContainer** component.

 |
| NODE\_RELATIVE\_CONTAINER\_BARRIER = 1012001 | 

Sets the barrier in the **RelativeContainer** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: guideline in the **RelativeContainer** component.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: barrier in the **RelativeContainer** component.

 |
| NODE\_GRID\_COLUMN\_TEMPLATE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_GRID = 1013000 | 

Sets the number of columns in the **Grid** component. If this parameter is not set, one column is used by default. This attribute can be set, reset, and obtained as required through APIs. For example, **'1fr 1fr 2fr'** indicates three columns, with the first column taking up 1/4 of the parent component's full width, the second column 1/4, and the third column 2/4. You can use **columnsTemplate('repeat(auto-fill,track-size)')** to automatically calculate the number of rows based on the specified row height **track-size**. **repeat** and **auto-fill** are keywords. The units for **track-size** can be px, vp (default), %, or a valid number. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: number of columns in the layout.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: number of columns in the layout.

 |
| NODE\_GRID\_ROW\_TEMPLATE = 1013001 | 

Sets the number of rows or the minimum row height in the **Grid** component. If this parameter is not set, one row is used by default. This attribute can be set, reset, and obtained as required through APIs. For example, **'1fr 1fr 2fr'** indicates three rows, with the first row taking up 1/4 of the parent component's full height, the second row 1/4, and the third row 2/4. You can use **rowsTemplate('repeat(auto-fill,track-size)')** to automatically calculate the number of rows based on the specified row height **track-size**. **repeat** and **auto-fill** are keywords. The units for **track-size** can be px, vp (default), %, or a valid number. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.string: number of rows in the layout.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.string: number of rows in the layout.

 |
| NODE\_GRID\_COLUMN\_GAP = 1013002 | 

Sets the gap between columns. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: gap between columns, in vp. The default value is **0**. Value range: \[0, +∞).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: gap between columns, in vp.

 |
| NODE\_GRID\_ROW\_GAP = 1013003 | 

Sets the gap between rows. This attribute can be set, reset, and obtained as required through APIs. Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: gap between rows, in vp. The default value is **0**. Value range: \[0, +∞).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].f32: gap between rows, in vp.

 |
| NODE\_GRID\_NODE\_ADAPTER = 1013004 | 

Defines the **Grid** component adapter. The attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object used as the adapter.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: [ArkUI\_NodeAdapter](../../structs/arkui-nodeadapter/document.md) object.

 |
| NODE\_GRID\_CACHED\_COUNT = 1013005 | 

Sets the number of cached items in the **Grid** component adapter. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of cached items in the **Grid** component adapter.

 |
| NODE\_GRID\_FOCUS\_WRAP\_MODE = 1013006 | 

Defines the focus wrap mode for the **Grid** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: focus wrap mode of the **Grid** component. The parameter type is [ArkUI\_FocusWrapMode](../native-type-h/document.md#arkui_focuswrapmode). The default value is **FOCUS\_WRAP\_MODE\_DEFAULT**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: focus wrap mode of the **Grid** component. The parameter type is [ArkUI\_FocusWrapMode](../native-type-h/document.md#arkui_focuswrapmode).

**Since**: 20

 |
| NODE\_GRID\_SYNC\_LOAD = 1013007 | 

Defines whether the **Grid** component loads child nodes synchronously. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the **Grid** component synchronously loads child nodes. **0**: frame-by-frame loading. **1**: synchronous loading. Default value: **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the **Grid** component synchronously loads child nodes. **0**: frame-by-frame loading. **1**: synchronous loading.

**Since**: 20

 |
| NODE\_GRID\_ALIGN\_ITEMS = 1013008 | 

Defines the alignment mode of [GridItem](../../../arkts-components/scroll-and-swipe/griditem/document.md) in **Grid**. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: alignment mode of **GridItem** in **Grid**. The parameter type is [ArkUI\_GridItemAlignment](../native-type-h/document.md#arkui_griditemalignment). The default value is **GRID\_ITEM\_ALIGNMENT\_DEFAULT**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: alignment mode of **GridItem** in **Grid**. The parameter type is [ArkUI\_GridItemAlignment](../native-type-h/document.md#arkui_griditemalignment).

**Since**: 22

 |
| NODE\_GRID\_LAYOUT\_OPTIONS = 1013009 | 

Defines the layout options of **Grid**. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: The parameter type is [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.object: The return value type is [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md).

**Since**: 22

 |
| NODE\_GRID\_COLUMN\_TEMPLATE\_ITEMFILLPOLICY = 1013010 | 

Defines the responsive column layout policy of the **Grid** component. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of columns at different breakpoint specifications. The data type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of columns at different breakpoint specifications. The data type is [ArkUI\_ItemFillPolicy](../native-type-h/document.md#arkui_itemfillpolicy).

**Since**: 22

 |
| NODE\_GRID\_ITEM\_STYLE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_GRID\_ITEM = 1014000 | 

Defines the style for **GridItem**. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: style for **GridItem**. The parameter type is [ArkUI\_GridItemStyle](../native-type-h/document.md#arkui_griditemstyle). The default value is **GRID\_ITEM\_STYLE\_NONE**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: style for **GridItem**. The parameter type is [ArkUI\_GridItemStyle](../native-type-h/document.md#arkui_griditemstyle).

**Since**: 22

 |
| NODE\_TEXT\_PICKER\_COLUMN\_WIDTHS = 15009 | 

Sets the width of columns in the picker. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].f32: width of the first column, specified as a percentage of the total width. By default, all columns have equal widths.

.value\[1\]?.f32: width of the second column, specified as a percentage of the total width. By default, all columns have equal widths.

.value\[2\]?.f32: width of the third column, specified as a percentage of the total width. By default, all columns have equal widths.

...

.value\[n\]?.f32: width of the (n+1)-th column, specified as a percentage of the total width. By default, all columns have equal widths.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

value\[0\].f32: width of the first column as a percentage of the total width.

value\[1\].f32: width of the second column as a percentage of the total width.

value\[2\].f32: width of the third column as a percentage of the total width.

...

value\[n\].f32: width of the (n+1)-th column as a percentage of the total width.

**Since**: 18

 |
| NODE\_IMAGE\_ANIMATOR\_IMAGES = ARKUI\_NODE\_IMAGE\_ANIMATOR \* MAX\_NODE\_SCOPE\_NUM = 19000 | 

Sets the image frame information set of the frame animation component. Dynamic update is not supported. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.size: number of image frames.

.object: image frame array. The parameter type is [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md).

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.size: number of image frames.

.object: image frame array. The parameter type is [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md).

 |
| NODE\_IMAGE\_ANIMATOR\_STATE = 19001 | 

Sets the playback status of the frame-by-frame animation. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: playback state of the frame-by-frame animation. The parameter type is [ArkUI\_AnimationStatus](../native-type-h/document.md#arkui_animationstatus). The default state is initial.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: playback state of the frame-by-frame animation. The parameter type is [ArkUI\_AnimationStatus](../native-type-h/document.md#arkui_animationstatus).

 |
| NODE\_IMAGE\_ANIMATOR\_DURATION = 19002 | 

Sets the playback duration of the frame-by-frame animation. This attribute does not take effect when a separate duration is set for any of the image frames. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: playback duration, in ms. The default value is **1000**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: playback duration, in ms. The default value is **1000**.

 |
| NODE\_IMAGE\_ANIMATOR\_REVERSE = 19003 | 

Sets the playback direction of the frame-by-frame animation. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: playback direction. The value **0** indicates that images are played from the first one to the last one, and **1** indicates that images are played from the last one to the first one. The default value is **0**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: playback direction. The value **0** indicates that images are played from the first one to the last one, and **1** indicates that images are played from the last one to the first one.

 |
| NODE\_IMAGE\_ANIMATOR\_FIXED\_SIZE = 19004 | 

Sets whether the image size is fixed at the component size. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: whether the image size is the fixed at the component size. The value **1** indicates that the image size is fixed at the component size. The value **0** indicates that the **width**, **height**, **top**, and **left** attributes of each image must be set separately. The default value is **1**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: whether the image size is the fixed at the component size. The value **1** indicates that the image size is fixed at the component size. The value **0** indicates that the **width**, **height**, **top**, and **left** attributes of each image must be set separately.

 |
| NODE\_IMAGE\_ANIMATOR\_FILL\_MODE = 19005 | 

Sets the status before and after execution of the frame-by-frame animation in the current playback direction. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: status before and after execution of the frame-by-frame animation in the current playback direction. The parameter type is [ArkUI\_AnimationFillMode](../native-type-h/document.md#arkui_animationfillmode). The default value is **ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS**.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: status before and after execution of the frame-by-frame animation in the current playback direction. The parameter type is [ArkUI\_AnimationFillMode](../native-type-h/document.md#arkui_animationfillmode).

 |
| NODE\_IMAGE\_ANIMATOR\_ITERATION = 19006 | 

Sets the number of times that the frame-by-frame animation is played. This attribute can be set, reset, and obtained as required through APIs.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.value\[0\].i32: number of times that the animation is played.

Format of the return value [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md):

.value\[0\].i32: number of times that the animation is played.

 |
| NODE\_EMBEDDED\_COMPONENT\_WANT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_EMBEDDED\_COMPONENT = 1016000 | 

Defines the want used to launch an EmbeddedAbility. This attribute can be set.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: want parameter for the **EmbeddedComponent**. The parameter type is [AbilityBase\_Want](../../structs/abilitybase-want/document.md). The default value is **nullptr**.

**Since**: 20

 |
| NODE\_EMBEDDED\_COMPONENT\_OPTION = 1016001 | 

Defines the options of **EmbeddedComponent**. This attribute can be set.

Format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter for setting the attribute:

.object: list of options for **EmbeddedComponent**. The parameter type is [ArkUI\_EmbeddedComponentOption](../../structs/arkui-embeddedcomponentoption/document.md).

**Since**: 20

 |

#### \[h2\]ArkUI\_NodeEventType

enum ArkUI\_NodeEventType

**Description**

Enumerates the event types supported by the **NativeNode** component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NODE\_TOUCH\_EVENT = 0 | Gesture event. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md). |
| NODE\_EVENT\_ON\_APPEAR = 1 | 
Mount event. This event is triggered when the component is mounted and displayed.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_EVENT\_ON\_DISAPPEAR = 2 | 

Unmount event. This event is triggered when the component is unmounted from the component tree and disappears.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_EVENT\_ON\_AREA\_CHANGE = 3 | 

Component area change event. This event is triggered when the component area changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: original width of the target element, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: original height of the target element, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[2\].f32**: original x-coordinate of the target element's upper left corner relative to the parent element's, in vp. The value type is number.

ArkUI\_NodeComponentEvent.data\[3\].f32: original y-coordinate of the target element's upper left corner relative to the parent element's, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[4\].f32**: original x-coordinate of the target element's upper left corner relative to the page's, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[5\].f32**: original y-coordinate of the target element's upper left corner relative to the page's, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[6\].f32**: new width of the target element, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[7\].f32**: new height of the target element, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[8\].f32**: new x-coordinate of the target element's upper left corner relative to the parent element's, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[9\].f32**: new y-coordinate of the target element's upper left corner relative to the parent element's, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[10\].f32**: new x-coordinate of the target element's upper left corner relative to the page's, in vp. The value type is number.

**ArkUI\_NodeComponentEvent.data\[11\].f32**: new y-coordinate of the target element's upper left corner relative to the page's, in vp. The value type is number.

 |
| NODE\_ON\_FOCUS = 4 | 

Event of obtaining focus. This event is triggered when the component obtains the focus.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_ON\_BLUR = 5 | 

Event of losing focus. This event is triggered when the component loses the focus.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_ON\_CLICK = 6 | 

Click event. This event is triggered when the component is clicked.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: x-coordinate of the click relative to the upper left corner of the clicked component's original area, in vp.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: y-coordinate of the click relative to the upper left corner of the clicked component's original area, in vp.

**ArkUI\_NodeComponentEvent.data\[2\].f32**: event timestamp. It is the interval between the time when the event is triggered and the time when the system starts, in microseconds.

**ArkUI\_NodeComponentEvent.data\[3\].i32**: event input device. The value **1** indicates the mouse, **2** indicates the touchscreen, and **4** indicates the key.

**ArkUI\_NodeComponentEvent.data\[4\].f32**: x-coordinate of the click relative to the upper left corner of the application window, in vp.

**ArkUI\_NodeComponentEvent.data\[5\].f32**: y-coordinate of the click relative to the upper left corner of the application window, in vp.

**ArkUI\_NodeComponentEvent.data\[6\].f32**: x-coordinate of the click relative to the upper left corner of the application screen, in vp.

**ArkUI\_NodeComponentEvent.data\[7\].f32**: y-coordinate of the click relative to the upper left corner of the application screen, in vp.

 |
| NODE\_ON\_TOUCH\_INTERCEPT = 7 | 

Custom component event interception. This event is triggered when the component is clicked.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md).

 |
| NODE\_EVENT\_ON\_VISIBLE\_AREA\_CHANGE = 8 | 

Visible area change event. This event is triggered when the ratio of the component's visible area to its total area is greater than or less than the threshold. Before registering the event, you need to use **NODE\_VISIBLE\_AREA\_CHANGE\_RATIO** to configure the threshold.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: whether the component's visible area has increased or decreased relative to its total area since the last update. The value **1** indicates that the visible area has increased, and **0** indicates that the visible area has decreased.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: ratio of the component's visible area to its total area when this callback is invoked.

 |
| NODE\_ON\_HOVER = 9 | 

Event triggered when the mouse pointer is moved over or away from the component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: whether the mouse pointer is hovered over the component. The value **1** indicates that the mouse pointer is hovered over the component, and **0** indicates that the mouse pointer is moved away from the component.

 |
| NODE\_ON\_MOUSE = 10 | 

Click event. This event is triggered when the component is clicked by a mouse device button or when the mouse pointer moves within the component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md).

 |
| NODE\_EVENT\_ON\_ATTACH = 11 | 

Attach event. This event is triggered when the component is attached to the component tree.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_EVENT\_ON\_DETACH = 12 | 

Detach event. This event is triggered when the component is detached from the component tree.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_ON\_ACCESSIBILITY\_ACTIONS = 13 | 

Accessibility-supported action event. This event is triggered when an accessibility action is performed after the corresponding accessibility action type is set.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].u32**: action type that triggers the callback. The parameter type is [ArkUI\_AccessibilityActionType](../native-type-h/document.md#arkui_accessibilityactiontype).

 |
| NODE\_ON\_PRE\_DRAG = 14 | 

Notifies the listener of the interaction state prior to a drop and drop operation. This event is triggered when a component is draggable and when a long press, lift, or drag initiation occurs.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: corresponds to [ArkUI\_PreDragStatus](../drag-and-drop-h/document.md#arkui_predragstatus).

 |
| NODE\_ON\_DRAG\_START = 15 | 

Event triggered when the user starts to drag an item. A drag operation is recognized only when the dragged item is moved far enough.

When the event callback occurs, the [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

 |
| NODE\_ON\_DRAG\_ENTER = 16 | 

Event triggered when a dragged item enters the boundaries of the current component. The current component refers to the component that listens for this event.

When the event callback occurs, the [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

 |
| NODE\_ON\_DRAG\_MOVE = 17 | 

Event triggered when a dragged item moves in the current component. The current component refers to the component that listens for this event.

When the event callback occurs, the [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

 |
| NODE\_ON\_DRAG\_LEAVE = 18 | 

Event triggered when a dragged item leaves the boundaries of the current component. The current component refers to the component that listens for this event.

When the event callback occurs, the [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

 |
| NODE\_ON\_DROP = 19 | 

Event triggered when a dragged item is dropped on the current component. The component can obtain the drag data for processing through the callback. The current component refers to the component that listens for this event.

When the event callback occurs, the [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

 |
| NODE\_ON\_DRAG\_END = 20 | Event triggered when a drag operation ends. The drag source can obtain the drag result by registering this callback. A drag operation ends when the dragged item is released. When the event callback occurs, the [ArkUI\_DragEvent](../../structs/arkui-dragevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object. |
| NODE\_ON\_KEY\_EVENT = 21 | 

Event triggered when a key event occurs. The callback can be triggered during interactions with a focused window using an external keyboard or other input device.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

**Since**: 14

 |
| NODE\_ON\_KEY\_PRE\_IME = 22 | 

Event triggered before the input method responds to the key action. If the return value of this callback is **true**, the key event is considered consumed, and subsequent event callbacks (**keyboardShortcut**, input method events, **onKeyEvent**) will be intercepted and no longer triggered. The callback can be triggered during interactions with a focused window using an external keyboard or other input device.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

**Since**: 14

 |
| NODE\_ON\_FOCUS\_AXIS = 23 | 

Event triggered when the bound component receives a focus axis event after gaining focus. The event callback is triggered by interactions with a joystick and a focused component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md).

**Since**: 15

 |
| NODE\_DISPATCH\_KEY\_EVENT = 24 | 

Component key event re-dispatch event. When a component node receives a key event, this callback is triggered instead of dispatching the event to its child nodes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

**Since**: 15

 |
| NODE\_ON\_AXIS = 25 | 

Event triggered when the bound component receives an axis event. Defines the event triggered when the bound component receives an axis event.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md).

**Since**: 17

 |
| NODE\_ON\_HOVER\_EVENT = 27 | 

Event triggered when the mouse pointer moves over or away from the component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md).

**Since**: 17

 |
| NODE\_ON\_CLICK\_EVENT = 26 | 

Event triggered when the bound component is clicked.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md).

**Since**: 18

 |
| NODE\_VISIBLE\_AREA\_APPROXIMATE\_CHANGE\_EVENT = 28 | 

Sets the callback for the NODE\_EVENT\_ON\_VISIBLE\_AREA\_CHANGE event, which limits the callback interval. This event is triggered when the ratio of the component's visible area to its total area is greater than or less than the threshold. Before registering the event, you need to use **NODE\_VISIBLE\_AREA\_APPROXIMATE\_CHANGE\_RATIO** to configure the threshold and update interval.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: whether the component's visible area has increased or decreased relative to its total area since the last update. The value **1** indicates that the visible area has increased, and **0** indicates that the visible area has decreased.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: ratio of the component's visible area to its total area when this callback is invoked.

**Since**: 17

 |
| NODE\_ON\_HOVER\_MOVE = 29 | 

Hover event. This event is triggered when the stylus pointer hovers over the component.

When the event callback occurs, the [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

**Since**: 15

 |
| NODE\_ON\_SIZE\_CHANGE = 30 | 

Size change event. This event is triggered when the component size changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: width of the component before the size change.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: height of the component before the size change.

**ArkUI\_NodeComponentEvent.data\[2\].f32**: width of the component after the size change.

**ArkUI\_NodeComponentEvent.data\[3\].f32**: height of the component after the size change.

Note: This event can be registered only by using the [OH\_ArkUI\_NativeModule\_RegisterCommonEvent](#oh_arkui_nativemodule_registercommonevent) API.

**Since**: 21

 |
| NODE\_ON\_COASTING\_AXIS\_EVENT = 31 | 

Coasting axis event. When a user slides two fingers on the touchpad for a certain distance and quickly lifts the fingers, the system continuously constructs the event based on the speed at which the fingers are lifted and a certain attenuation curve. You can listen to this type of events to handle the fling effect after the normal scrolling axis event.

When the event callback occurs, you can obtain the [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) object from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object by calling [OH\_ArkUI\_NodeEvent\_GetInputEvent](#oh_arkui_nodeevent_getinputevent). Then, you can obtain the [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md) object from the [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) object by calling [OH\_ArkUI\_UIInputEvent\_GetCoastingAxisEvent](../ui-input-event-h/document.md#oh_arkui_uiinputevent_getcoastingaxisevent). You can obtain more information from the object by calling the \*\*OH\_ArkUI\_CoastingAxisEvent\_\*\*XXX series APIs.

**Since**: 22

 |
| NODE\_ON\_CHILD\_TOUCH\_TEST = 32 | 

Pre-touch test event of a child component. This event is called to specify how to perform a touch test on the child component of the current component. This event is triggered when the component is touched.

When the event callback occurs, you can obtain the [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md) object from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object by calling [OH\_ArkUI\_NodeEvent\_GetTouchTestInfo](#oh_arkui_nodeevent_gettouchtestinfo). Then ,you can obtain the list of touch test items from the [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md) object by calling [OH\_ArkUI\_TouchTestInfo\_GetTouchTestInfoList](../ui-input-event-h/document.md#oh_arkui_touchtestinfo_gettouchtestinfolist). You can obtain more information by using the [OH\_ArkUI\_TouchTestInfoItem\_GetXXX](../ui-input-event-h/document.md#oh_arkui_touchtestinfoitem_getx) series APIs. Use [OH\_ArkUI\_TouchTestInfo\_SetTouchResultStrategy](../ui-input-event-h/document.md#oh_arkui_touchtestinfo_settouchresultstrategy) to set the touch test policy. Use [OH\_ArkUI\_TouchTestInfo\_SetTouchResultId](../ui-input-event-h/document.md#oh_arkui_touchtestinfo_settouchresultid) to set the child component to be affected during the hit test.

**Since**: 22

 |
| NODE\_TEXT\_ON\_DETECT\_RESULT\_UPDATE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT = 1000 | 

Event triggered when text recognition with the configured **TextDataDetectorConfig** settings succeeds.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: text recognition result in JSON format.

 |
| NODE\_TEXT\_SPAN\_ON\_LONG\_PRESS = 1001 | 

Long-press event for the span component. This callback is triggered when the component is long-pressed.

When the event callback occurs, the [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) object can be obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

**Since**: 20

 |
| NODE\_IMAGE\_ON\_COMPLETE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE = 4000 | 

Image loading success event. This event is triggered when an image is successfully loaded or decoded.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: loading status. The value **0** indicates that the image is loaded successfully, and **1** indicates that the image is decoded successfully.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: width of the image, in px.

**ArkUI\_NodeComponentEvent.data\[2\].f32**: height of the image, in px.

**ArkUI\_NodeComponentEvent.data\[3\].f32**: width of the component, in px.

**ArkUI\_NodeComponentEvent.data\[4\].f32**: height of the component, in px.

**ArkUI\_NodeComponentEvent.data\[5\].f32**: offset of the rendered content relative to the component on the x-axis, in px.

**ArkUI\_NodeComponentEvent.data\[6\].f32**: offset of the rendered content relative to the component on the y-axis, in px.

**ArkUI\_NodeComponentEvent.data\[7\].f32**: actual rendered width of the image, in px.

**ArkUI\_NodeComponentEvent.data\[8\].f32**: actual rendered height of the image, in px.

 |
| NODE\_IMAGE\_ON\_ERROR = 4001 | 

Image loading failure event. This event is triggered when an error occurs during image loading.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: result code.

**401**: The image could not be obtained because the image path is invalid.

**103101**: The image format is not supported.

 |
| NODE\_IMAGE\_ON\_SVG\_PLAY\_FINISH = 4002 | 

SVG animation playback completion event. This event is triggered when the animation playback in the loaded SVG image is complete.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_IMAGE\_ON\_DOWNLOAD\_PROGRESS = 4003 | 

Event triggered during image download. This event is triggered when the page component downloads a web page image.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].u32**: number of bytes that have been downloaded.

**ArkUI\_NodeComponentEvent.data\[1\].u32**: total number of bytes of the image to be downloaded.

 |
| NODE\_TOGGLE\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TOGGLE = 5000 | 

Event triggered when the toggle status changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: toggle status. **1**: on; **0**: off.

 |
| NODE\_TEXT\_INPUT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_INPUT = 7000 | 

Event triggered when the text input content changes in the **TextInput** component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: text input.

 |
| NODE\_TEXT\_INPUT\_ON\_SUBMIT = 7001 | 

Event triggered when the **Enter** key on the keyboard is pressed for the **TextInput** component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: type of the **Enter** key.

 |
| NODE\_TEXT\_INPUT\_ON\_CUT = 7002 | 

Event triggered when the cut button on the pasteboard, which displays when the text box is long pressed, is clicked.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: text that is cut.

 |
| NODE\_TEXT\_INPUT\_ON\_PASTE = 7003 | 

Event triggered when the paste button on the pasteboard, which displays when the text box is long pressed, is clicked.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: text that is pasted.

 |
| NODE\_TEXT\_INPUT\_ON\_TEXT\_SELECTION\_CHANGE = 7004 | 

Event triggered when the text selection position changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: start position of the text selection area.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: end position of the text selection area.

 |
| NODE\_TEXT\_INPUT\_ON\_EDIT\_CHANGE = 7005 | 

Called when the input state changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: **true** indicates that text input is in progress.

 |
| NODE\_TEXT\_INPUT\_ON\_INPUT\_FILTER\_ERROR = 7006 | 

Event triggered when matching with the regular expression specified by **NODE\_TEXT\_INPUT\_INPUT\_FILTER** fails.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: content that is filtered out when regular expression matching fails.

 |
| NODE\_TEXT\_INPUT\_ON\_CONTENT\_SCROLL = 7007 | 

Event triggered when the text content is scrolled.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: offset in the x-coordinate of the text in the content area.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: offset in the y-coordinate of the text in the content area.

 |
| NODE\_TEXT\_INPUT\_ON\_CONTENT\_SIZE\_CHANGE = 7008 | 

Event triggered when the text input content changes in the **TextInput** component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: width of the text.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: height of the text.

 |
| NODE\_TEXT\_INPUT\_ON\_WILL\_INSERT = 7009 | 

Event triggered when text is about to be entered. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32 at index 0: position of the text to be inserted; obtained using [OH\_ArkUI\_NodeEvent\_GetNumberValue](#oh_arkui_nodeevent_getnumbervalue).

buffer at index 0: text to be inserted; obtained using [OH\_ArkUI\_NodeEvent\_GetStringValue](#oh_arkui_nodeevent_getstringvalue).

 |
| NODE\_TEXT\_INPUT\_ON\_DID\_INSERT = 7010 | 

Event triggered when input is completed. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32 at index 0: position of the text inserted; obtained using [OH\_ArkUI\_NodeEvent\_GetNumberValue](#oh_arkui_nodeevent_getnumbervalue).

buffer at index 0: inserted text; obtained using [OH\_ArkUI\_NodeEvent\_GetStringValue](#oh_arkui_nodeevent_getstringvalue).

 |
| NODE\_TEXT\_INPUT\_ON\_WILL\_DELETE = 7011 | 

Event triggered when text is about to be deleted. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32 at index 0: position of the text to be deleted; obtained using [OH\_ArkUI\_NodeEvent\_GetNumberValue](#oh_arkui_nodeevent_getnumbervalue).

value.i32: direction for deleting the text, with the index of **1**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**. The value **0** indicates backward-delete, and **1** indicates forward-delete.

buffer at index 0: text to be deleted; obtained using [OH\_ArkUI\_NodeEvent\_GetStringValue](#oh_arkui_nodeevent_getstringvalue).

 |
| NODE\_TEXT\_INPUT\_ON\_DID\_DELETE = 7012 | 

Event triggered when deletion is completed. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32 at index 0: position of the text deleted; obtained using [OH\_ArkUI\_NodeEvent\_GetNumberValue](#oh_arkui_nodeevent_getnumbervalue).

value.i32: direction for deleting the text, with the index of **1**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**. The value **0** indicates backward-delete, and **1** indicates forward-delete.

buffer at index 0: deleted text; obtained using [OH\_ArkUI\_NodeEvent\_GetStringValue](#oh_arkui_nodeevent_getstringvalue).

 |
| NODE\_TEXT\_INPUT\_ON\_CHANGE\_WITH\_PREVIEW\_TEXT = 7013 | 

Event triggered when content (including preview text) changes in the **TextInput** component. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md).

[ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md) contains the following parameters:

**ArkUI\_TextChangeEvent.pStr**: content in the **TextInput** component.

**ArkUI\_TextChangeEvent.pExtendStr**: content of the preview text in the **TextInput** component.

**ArkUI\_TextChangeEvent.number**: start position of the preview text in the **TextInput** component.

**Since**: 15

 |
| NODE\_TEXT\_INPUT\_ON\_WILL\_CHANGE = 7014 | 

Event triggered when content (including preview text) is about to change in the **TextInput** component. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md).

[ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md) contains the following parameters:

**ArkUI\_TextChangeEvent.pStr**: content in the **TextInput** component.

**ArkUI\_TextChangeEvent.pExtendStr**: content of the preview text in the **TextInput** component.

**ArkUI\_TextChangeEvent.number**: start position of the preview text in the **TextInput** component.

**Since**: 20

 |
| NODE\_TEXT\_AREA\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_AREA = 8000 | 

Called when the input in the text box changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: current text input.

 |
| NODE\_TEXT\_AREA\_ON\_PASTE = 8001 | 

Event triggered when the paste button on the pasteboard, which displays when the text box is long pressed, is clicked.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: text that is pasted.

 |
| NODE\_TEXT\_AREA\_ON\_TEXT\_SELECTION\_CHANGE = 8002 | 

Event triggered when the text selection position changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: start position of the text selection area.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: end position of the text selection area.

 |
| NODE\_TEXT\_AREA\_ON\_EDIT\_CHANGE = 8003 | 

Called when the input state changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: **true** indicates that text input is in progress.

 |
| NODE\_TEXT\_AREA\_ON\_SUBMIT = 8004 | 

Event triggered when the **Enter** key on the keyboard is pressed for the **TextArea** component. This event is not triggered when **keyType** is **ARKUI\_ENTER\_KEY\_TYPE\_NEW\_LINE**.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: type of the **Enter** key.

 |
| NODE\_TEXT\_AREA\_ON\_INPUT\_FILTER\_ERROR = 8005 | 

Event triggered when matching with the regular expression specified by **NODE\_TEXT\_AREA\_INPUT\_FILTER** fails.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

[ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md) contains the following parameters:

**ArkUI\_StringAsyncEvent.pStr**: content that is filtered out when regular expression matching fails.

 |
| NODE\_TEXT\_AREA\_ON\_CONTENT\_SCROLL = 8006 | 

Event triggered when the text content is scrolled.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: offset in the x-coordinate of the text in the content area.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: offset in the y-coordinate of the text in the content area.

 |
| NODE\_TEXT\_AREA\_ON\_CONTENT\_SIZE\_CHANGE = 8007 | 

Event triggered when the text input content changes in the **TextArea** component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: width of the text.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: height of the text.

 |
| NODE\_TEXT\_AREA\_ON\_WILL\_INSERT = 8008 | 

Event triggered when text is about to be entered. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32: position of the text, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**.

buffer: string value of the text, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetStringValue**.

 |
| NODE\_TEXT\_AREA\_ON\_DID\_INSERT = 8009 | 

Event triggered when input is completed. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32: position of the text, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**.

buffer: string value of the text, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetStringValue**.

 |
| NODE\_TEXT\_AREA\_ON\_WILL\_DELETE = 8010 | 

Event triggered when text is about to be deleted. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32: position of the text deleted, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**.

value.i32: direction for deleting the text, with the index of **1**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**. The value **0** indicates backward-delete, and **1** indicates forward-delete.

buffer: string value of the text, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetStringValue**.

 |
| NODE\_TEXT\_AREA\_ON\_DID\_DELETE = 8011 | 

Event triggered when deletion is completed. When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md).

value.f32: position of the text deleted, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**.

value.i32: direction for deleting the text, with the index of **1**; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**. The value **0** indicates backward-delete, and **1** indicates forward-delete.

buffer: string value of the text, with the index of **0**; obtained using **OH\_ArkUI\_NodeEvent\_GetStringValue**.

 |
| NODE\_TEXT\_AREA\_ON\_CHANGE\_WITH\_PREVIEW\_TEXT = 8012 | 

Event triggered when content (including preview text) changes in the [TextArea](../../../arkts-components/text-and-input/textarea/document.md) component. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md).

[ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md) contains the following parameters:

**ArkUI\_TextChangeEvent.pStr**: content in the **TextArea** component.

**ArkUI\_TextChangeEvent.pExtendStr**: content of the preview text in the **TextArea** component.

**ArkUI\_TextChangeEvent.number**: start position of the preview text in the **TextArea** component.

**Since**: 15

 |
| NODE\_TEXT\_AREA\_ON\_WILL\_CHANGE = 8013 | 

Event triggered when content (including preview text) is about to change in the **TextArea** component. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md).

[ArkUI\_TextChangeEvent](../../structs/arkui-textchangeevent/document.md) contains the following parameters:

**ArkUI\_TextChangeEvent.pStr**: content in the **TextArea** component.

**ArkUI\_TextChangeEvent.pExtendStr**: content of the preview text in the **TextArea** component.

**ArkUI\_TextChangeEvent.number**: start position of the preview text in the **TextArea** component.

**Since**: 20

 |
| NODE\_CHECKBOX\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX = 11000 | 

Event triggered when the selected status of the **ARKUI\_NODE\_CHECKBOX** component changes. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

**ArkUI\_NodeComponentEvent.data\[0\].i32**: **1**: selected. **0**: not selected.

 |
| NODE\_DATE\_PICKER\_EVENT\_ON\_DATE\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_DATE\_PICKER = 13000 | 

Event triggered when a date is selected in the **ARKUI\_NODE\_DATE\_PICKER** component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: year of the selected date.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: month of the selected date. Value range: \[0-11\].

**ArkUI\_NodeComponentEvent.data\[2\].i32**: day of the selected date.

 |
| NODE\_TIME\_PICKER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TIME\_PICKER = 14000 | 

Event triggered when a time is selected in the **ARKUI\_NODE\_TIME\_PICKER** component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: hour of the selected time. Value range: \[0-23\].

**ArkUI\_NodeComponentEvent.data\[1\].i32**: minute of the selected time. Value range: \[0-59\].

 |
| NODE\_TEXT\_PICKER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_PICKER = 15000 | 

Event triggered when an item is selected in the **ARKUI\_NODE\_TEXT\_PICKER** component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0...11\].i32**: value of the selected item.

 |
| NODE\_TEXT\_PICKER\_EVENT\_ON\_SCROLL\_STOP = 15001 | 

Event triggered when an item is selected in the **ARKUI\_NODE\_TEXT\_PICKER** component. This event is triggered when the user stops sliding to select a text item.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0...11\].i32**: value of the selected item.

**Since**: 14

 |
| NODE\_CALENDAR\_PICKER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CALENDAR\_PICKER = 16000 | 

Event triggered when a date is selected in the **NODE\_CALENDAR\_PICKER** component. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

**ArkUI\_NodeComponent.data\[0\].u32**: year of the selected date.

**ArkUI\_NodeComponent.data\[1\].u32**: month of the selected date.

**ArkUI\_NodeComponent.data\[2\].u32**: day of the selected date.

 |
| NODE\_SLIDER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SLIDER = 17000 | 

Event triggered when the **ARKUI\_NODE\_SLIDER** component is dragged or clicked. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: current slider value.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: state triggered by the event.

 |
| NODE\_RADIO\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_RADIO = 18000 | 

Event triggered when the **ARKUI\_NODE\_RADIO** component is dragged or clicked. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: status of the radio button.

 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_START = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE\_ANIMATOR = 19000 | 

Event triggered when the frame-by-frame animation starts to play.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_PAUSE = 19001 | 

Event triggered when the frame-by-frame animation playback is paused.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_REPEAT = 19002 | 

Event triggered when the frame-by-frame animation playback is repeated.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_CANCEL = 19003 | 

Event triggered when the frame-by-frame animation playback returns to the initial state.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_FINISH = 19004 | 

Event triggered when the frame-by-frame animation playback is complete or stopped.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_CHECKBOX\_GROUP\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX\_GROUP = 21000 | 

Event triggered when the selected state of **ARKUI\_NODE\_CHECKBOX\_GROUP** or any [check box](../../../arkts-components/buttons-and-selections/checkbox/document.md) within it changes. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_StringAsyncEvent](../../structs/arkui-stringasyncevent/document.md).

**ArkUI\_StringAsyncEvent.pStr**Name: name of the selected check box; Status: **0**: All check boxes in the group are selected. **1**: Some check boxes in the group are selected. **2**: No check box in the group is selected.

**Since**: 15

 |
| NODE\_SWIPER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SWIPER = 1001000 | 

Event triggered when the index of the currently displayed element of this **ARKUI\_NODE\_SWIPER** instance changes. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the currently displayed element.

 |
| NODE\_SWIPER\_EVENT\_ON\_ANIMATION\_START = 1001001 | 

Event triggered when the switching animation of this **ARKUI\_NODE\_SWIPER** instance starts. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the currently displayed element.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: index of the target element to switch to.

**ArkUI\_NodeComponentEvent.data\[2\].f32**: offset of the currently displayed element relative to the start position of the swiper along the main axis.

**ArkUI\_NodeComponentEvent.data\[3\].f32**: offset of the target element relative to the start position of the swiper along the main axis.

**ArkUI\_NodeComponentEvent.data\[4\].f32**: hands-off velocity.

 |
| NODE\_SWIPER\_EVENT\_ON\_ANIMATION\_END = 1001002 | 

Event triggered when the switching animation of this **ARKUI\_NODE\_SWIPER** instance ends. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the currently displayed element.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: offset of the currently displayed element relative to the start position of the swiper along the main axis.

 |
| NODE\_SWIPER\_EVENT\_ON\_GESTURE\_SWIPE = 1001003 | 

Event triggered on a frame-by-frame basis when the page is turned by a swipe. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the currently displayed element.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: offset of the currently displayed element relative to the start position of the swiper along the main axis.

 |
| NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL = 1001004 | 

Event triggered when the [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md) page scrolls, which is listened by **ARKUI\_NODE\_SWIPER**. Instructions:

1\. This API does not work when **NODE\_SWIPER\_DISPLAY\_COUNT** is set to **'auto'**.

2\. This API does not work when **prevMargin** and **nextMargin** are set in such a way that the **Swiper** frontend and backend display the same page during loop playback.

3\. During page scrolling, the **ContentDidScrollCallback** callback is invoked for all pages in the viewport on a frame-by-frame basis.

For example, when there are two pages whose subscripts are 0 and 1 in the viewport, two callbacks whose indexes are 0 and 1 are invoked in each frame.

4\. When the **swipeByGroup** parameter of the **displayCount** attribute is set to **true**, the callback is invoked

for all pages in a group if any page in the group is within the viewport.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the **Swiper** component, which is the same as the index in the [onChange](../../../arkts-components/scroll-and-swipe/swiper/document.md#onchange) event.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: index of a page in the viewport.

\* **ArkUI\_NodeComponentEvent.data\[2\].f32**: position of the page relative to the start position of the **Swiper** component's main axis (start position of the page corresponding to **selectedIndex**).

**ArkUI\_NodeComponentEvent.data\[3\].f32**: length of the page in the main axis direction.

 |
| NODE\_SWIPER\_EVENT\_ON\_SELECTED = 1001005 | 

Event triggered when the selection changes in the **ARKUI\_NODE\_SWIPER** component. This event is triggered in the following scenarios:

1\. When the page switching animation starts after the user lifts their finger after swiping and the swipe meets the threshold for page turning.

2\. When the page is changed programmatically using either **NODE\_SWIPER\_INDEX** or **NODE\_SWIPER\_SWIPE\_TO\_INDEX**.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the currently selected element.

**Since**: 18

 |
| NODE\_SWIPER\_EVENT\_ON\_UNSELECTED = 1001006 | 

Event triggered when the selection changes in the **ARKUI\_NODE\_SWIPER** component. This event is triggered when any of the following occurs:

1\. When the page switching animation starts after the user lifts their finger after swiping and the swipe meets the threshold for page turning.

2\. When the page is changed using either **NODE\_SWIPER\_INDEX** or **NODE\_SWIPER\_SWIPE\_TO\_INDEX**.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the item that is about to be hidden.

**Since**: 18

 |
| NODE\_SWIPER\_EVENT\_ON\_CONTENT\_WILL\_SCROLL = 1001007 | 

Event for swipe behavior interception in the **ARKUI\_NODE\_SWIPER** component. Usage: The [ContentWillScrollCallback](../../../arkts-components/scroll-and-swipe/swiper/document.md#contentwillscrollcallback15) callback is triggered before a swipe operation.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the currently displayed element. The value of this parameter is used as the result of the interception event. The value **0** indicates that interception is performed; the value **1** indicates that interception is not performed.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: index of the target element to switch to.

**ArkUI\_NodeComponentEvent.data\[2\].f32**: swipe offset per frame. A positive value indicates swiping backward (for example, from index=1 to index=0), and a negative value indicates swiping forward (for example, from index=0 to index=1).

**Since**: 15

 |
| NODE\_SWIPER\_EVENT\_ON\_SCROLL\_STATE\_CHANGED = 1001008 | 

**ARKUI\_NODE\_SWIPER** scroll state change event. This event is triggered in the following scenarios:

The **Swiper** transitions between three scroll states: scrolling with the touch, animating after release, and stopped. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: current scroll state. The parameter type is [ArkUI\_ScrollState](../native-type-h/document.md#arkui_scrollstate).

**Since**: 20

 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SCROLL = 1002000 | 

Event triggered when scrolling occurs. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: horizontal scrolling offset.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: vertical scrolling offset.

 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_FRAME\_BEGIN = 1002001 | 

Event triggered when each frame scrolling starts in the scrollable component. The **List**, **Scroll**, and **WaterFlow** components are supported since API version 12, and the **Grid** component is supported since API version 22.

This event is triggered in the following scenarios:

1\. This event is triggered when scrolling is started by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).

2\. This event is not triggered when the controller API is called.

3\. This event is not triggered when the component bounces back out of bounds.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: amount to scroll by.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: current scroll state.

**::ArkUI\_NodeComponentEvent** contains one return value:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: The event handler can work out the amount by which the component needs to scroll based on the real-world situation and return the result in this parameter.

 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_SCROLL = 1002002 | 

Event triggered when the container is about to scroll. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame, in vp. The offset is positive when the content is scrolled left and negative when the content is scrolled right.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: scroll offset of each frame, in vp. The offset is positive when the content is scrolled up and negative when the content is scrolled down.

**ArkUI\_NodeComponentEvent.data\[2\].i32**: current scroll state. The parameter type is [ArkUI\_ScrollState](../native-type-h/document.md#arkui_scrollstate).

**ArkUI\_NodeComponentEvent.data\[3\].i32**: current scroll source. The parameter type is [ArkUI\_ScrollSource](../native-type-h/document.md#arkui_scrollsource).

 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_SCROLL = 1002003 | 

Event triggered when the container scrolls. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame, in vp. The offset is positive when the content is scrolled left and negative when the content is scrolled right.

**ArkUI\_NodeComponentEvent.data\[1\].f32**: scroll offset of each frame, in vp. The offset is positive when the content is scrolled up and negative when the content is scrolled down.

**ArkUI\_NodeComponentEvent.data\[2\].i32**: current scroll state. The parameter type is [ArkUI\_ScrollState](../native-type-h/document.md#arkui_scrollstate).

 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_START = 1002004 | 

Event triggered when the container starts scrolling. The **List**, **Scroll**, and **WaterFlow** components are supported since API version 12, and the **Grid** component is supported since API version 22.

This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).

2\. The controller API is called to start the scrolling, accompanied by a transition animation.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_STOP = 1002005 | 

Event triggered when the container stops scrolling. The **List**, **Scroll**, and **WaterFlow** components are supported since API version 12, and the **Grid** component is supported since API version 22.

This event is triggered in the following scenarios:

1\. Scrolling is stopped by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).

2\. The controller API is called to stop the scrolling, accompanied by a transition animation.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_EDGE = 1002006 | 

Event triggered when the container reaches the scroll boundary. This event is triggered in the following scenarios:

1\. Scrolling reaches the edge after being started by the scrollable component (supports keyboard, mouse, and other input methods that trigger scrolling).

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: edge (top, bottom, left, or right) that the scrolling reaches.

 |
| NODE\_SCROLL\_EVENT\_ON\_REACH\_START = 1002007 | 

Event triggered when the scrollable component reaches the start edge.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_SCROLL\_EVENT\_ON\_REACH\_END = 1002008 | 

Event triggered when the scrollable component reaches the end edge.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_STOP\_DRAGGING = 1002009 | 

Event triggered when the user is about to release the drag on the scrollable component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: speed at which the user releases the drag, in vp/s.

**Since**: 20

 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_ZOOM = 1002010 | 

**Scroll** component zoom event, triggered at the end of each frame during zooming.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: current zoom scale.

**Since**: 20

 |
| NODE\_SCROLL\_EVENT\_ON\_ZOOM\_START = 1002011 | 

**Scroll** component's zoom start event, triggered when zooming begins.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

**Since**: 20

 |
| NODE\_SCROLL\_EVENT\_ON\_ZOOM\_STOP = 1002012 | 

[Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md) component's zoom end event, triggered when zooming ends.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

**Since**: 20

 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_START\_DRAGGING = 1002013 | 

Event triggered when the user is about to drag the scrollable component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

**Since**: 21

 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_STOP\_DRAGGING = 1002014 | 

Event triggered when the user ends dragging the scrollable component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: whether to trigger the sliding animation after the drag ends.

**Since**: 21

 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_START\_FLING = 1002015 | 

Event triggered when the scrollable component's sliding animation is about to start.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

**Since**: 21

 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_STOP\_FLING = 1002016 | 

Event triggered when the scrollable component's sliding animation ends.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

**Since**: 21

 |
| NODE\_LIST\_ON\_SCROLL\_INDEX = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST = 1003000 | 

Event triggered when a child component of [ARKUI\_NODE\_LIST](#arkui_nodetype) enters or leaves the list display area. This event is triggered in the following scenario:

This event is triggered once when the list is initialized and when the index of the first child component or the next child component in the list display area changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the first child component in the list display area.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: index of the last child component in the list display area.

**ArkUI\_NodeComponentEvent.data\[2\].i32**: index of the center child component in the list display area.

 |
| NODE\_LIST\_ON\_WILL\_SCROLL = 1003001 | 

Event triggered when the [ARKUI\_NODE\_LIST](#arkui_nodetype) component is about to scroll. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame. The offset is positive when the list is scrolled up and negative when the list is scrolled down.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: current scroll state. The parameter type is [ArkUI\_ScrollState](../native-type-h/document.md#arkui_scrollstate).

**ArkUI\_NodeComponentEvent.data\[2\].i32**: current scroll source. The parameter type is [ArkUI\_ScrollSource](../native-type-h/document.md#arkui_scrollsource).

 |
| NODE\_LIST\_ON\_DID\_SCROLL = 1003002 | 

Event triggered when the [ARKUI\_NODE\_LIST](#arkui_nodetype) component scrolls. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame. The offset is positive when the list is scrolled up and negative when the list is scrolled down.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: current scroll state.

 |
| NODE\_LIST\_ON\_SCROLL\_VISIBLE\_CONTENT\_CHANGE = 1003003 | 

Event triggered when the currently displayed content of the **ARKUI\_NODE\_LIST** component changes. This event is triggered in the following scenario:

This event is triggered once when the list is initialized and when the index of the first child component or the next child component in the list display area changes. During trigger condition calculation, [header](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) or [footer](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) in each [ListItem](../../../arkts-components/scroll-and-swipe/listitem/document.md) and [ListItemGroup](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md) is considered as a child component.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the first child component in the list display area.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: area in the list item group where the list display area starts. The type is [ArkUI\_ListItemGroupArea](../native-type-h/document.md#arkui_listitemgrouparea).

**ArkUI\_NodeComponentEvent.data\[2\].i32**: index of the list item at the start of the list display area in the list item group. If the start of the list display area is not on a list item, the value is **\-1**.

**ArkUI\_NodeComponentEvent.data\[3\].i32**: index of the last child component in the list display area.

**ArkUI\_NodeComponentEvent.data\[4\].i32**: area in the list item group where the list display area ends. The type is [ArkUI\_ListItemGroupArea](../native-type-h/document.md#arkui_listitemgrouparea).

**ArkUI\_NodeComponentEvent.data\[5\].i32**: index of the list item at the end of the list display area in the list item group. If the end of the list display area is not on a list item, the value is **\-1**.

**Since**: 15

 |
| NODE\_REFRESH\_STATE\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_REFRESH = 1009000 | 

Event triggered when the refresh state of the **ARKUI\_NODE\_REFRESH** object changes. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: refresh state.

**0** (Inactive): This is the default status, indicating that the user has not pulled down the list.

**1** (Drag): The user is pulling down the list, and the distance between the current position and the top of the list is less than the refresh distance. If the user releases the list at this time, the component enters the **Inactive** state. If the user continues to pull down the list and the distance between the current position and the top of the list exceeds the refresh distance, the component enters the **OverDrag** state.

**2** (OverDrag): The user is pulling down the list, and the distance between the current position and the top of the list exceeds the refresh distance. If the user releases the list at this time, the component enters the **Refresh** state. If the user swipes upward and the pull-down distance is less than the refresh distance, the component enters the **Drag** state.

**3** (Refresh): The user has pulled down the list to the refresh distance, and the component enters the **Refresh** state.

**4** (Done): The refresh is complete, and the component returns to the initial state (the top of the list).

 |
| NODE\_REFRESH\_ON\_REFRESH = 1009001 | 

Event triggered when the **ARKUI\_NODE\_REFRESH** object enters the refresh state. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) does not contain parameters.

 |
| NODE\_REFRESH\_ON\_OFFSET\_CHANGE = 1009002 | 

Event triggered when the pull-down distance of the **ARKUI\_NODE\_REFRESH** object changes. When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: drop-down distance.

 |
| NODE\_ON\_WILL\_SCROLL = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_WATER\_FLOW = 1010000 | 

Event triggered when the **ARKUI\_NODE\_WATER\_FLOW** component is about to scroll. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame. The offset is positive when the content is scrolled up and negative when the content is scrolled down.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: current scroll state. The parameter type is [ArkUI\_ScrollState](../native-type-h/document.md#arkui_scrollstate).

**ArkUI\_NodeComponentEvent.data\[2\].i32**: current scroll source. The parameter type is [ArkUI\_ScrollSource](../native-type-h/document.md#arkui_scrollsource).

 |
| NODE\_WATER\_FLOW\_ON\_DID\_SCROLL = 1010001 | 

Event triggered when the **ARKUI\_NODE\_WATER\_FLOW** component scrolls. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame. The offset is positive when the content is scrolled up and negative when the content is scrolled down.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: current scroll state.

 |
| NODE\_WATER\_FLOW\_ON\_SCROLL\_INDEX = 1010002 | 

Event triggered when the first or last item displayed in the water flow container changes. This event is triggered in the following scenario:

This event is triggered when the index value of the first or last item in the water flow container changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the first item of the water flow container.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: index of the last item of the water flow container.

 |
| NODE\_GRID\_ON\_SCROLL\_INDEX = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_GRID = 1013000 | 

Event triggered when a child component of **ARKUI\_NODE\_GRID** enters or leaves the grid display area. This event is triggered in the following scenario:

This event is triggered once when the grid is initialized and when the index of the first or last child component in the grid display area changes.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].i32**: index of the first child component in the grid display area.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: index of the last child component in the grid display area.

**Since**: 22

 |
| NODE\_GRID\_ON\_WILL\_SCROLL = 1013001 | 

Event triggered when the **ARKUI\_NODE\_GRID** component is about to scroll. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame. The offset is positive when the content is scrolled up in the grid and negative when the content is scrolled down.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: current scroll state. The parameter type is [ArkUI\_ScrollState](../native-type-h/document.md#arkui_scrollstate).

**ArkUI\_NodeComponentEvent.data\[2\].i32**: current scroll source. The parameter type is [ArkUI\_ScrollSource](../native-type-h/document.md#arkui_scrollsource).

**Since**: 22

 |
| NODE\_GRID\_ON\_DID\_SCROLL = 1013002 | 

Event triggered when the **ARKUI\_NODE\_GRID** component scrolls. This event is triggered in the following scenarios:

1\. Scrolling is started by the scrollable component or other input settings, such as keyboard and mouse operations.

2\. Scrolling is initiated by calling the controller API.

3\. The out-of-bounds bounce effect is active.

When the event callback occurs, the union type in the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object is [ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md).

[ArkUI\_NodeComponentEvent](../../structs/arkui-nodecomponentevent/document.md) contains the following parameters:

**ArkUI\_NodeComponentEvent.data\[0\].f32**: scroll offset of each frame. The offset is positive when the content is scrolled up in the grid and negative when the content is scrolled down.

**ArkUI\_NodeComponentEvent.data\[1\].i32**: current scroll state. The parameter type is [ArkUI\_ScrollState](../native-type-h/document.md#arkui_scrollstate).

**Since**: 22

 |
| NODE\_GRID\_ON\_SCROLL\_BAR\_UPDATE = 1013003 | 

Event triggered at the end of each frame layout of the **ARKUI\_NODE\_GRID** component, which is used to set the position and length of the scrollbar.

When the event callback occurs, the event parameter is [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md). value.i32 at index 0: index of the first item in the currently displayed grid; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**.

value.f32 at index 1: offset of the item at the starting position of the currently displayed grid relative to the starting position of the grid display, in vp; obtained using **OH\_ArkUI\_NodeEvent\_GetNumberValue**.

**Since**: 22

 |

#### \[h2\]ArkUI\_NodeDirtyFlag

enum ArkUI\_NodeDirtyFlag

**Description**

Enumerates the flags passed to indicate the need to re-execute measurement, layout, or rendering when a custom component calls the ::[markDirty](../../structs/arkui-nativenodeapi-1/document.md#markdirty) API.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NODE\_NEED\_MEASURE = 1 | Remeasure. When this type of flag is specified, re-layout is triggered by default. |
| NODE\_NEED\_LAYOUT = 2 | Re-layout. |
| NODE\_NEED\_RENDER = 3 | Re-rendering. |

#### \[h2\]ArkUI\_NodeCustomEventType

enum ArkUI\_NodeCustomEventType

**Description**

Enumerates the custom component event types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE = 1 << 0 | Custom measurement. |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT = 1 << 1 | Custom layout. |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW = 1 << 2 | Custom content layer drawing. |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_FOREGROUND\_DRAW = 1 << 3 | Custom foreground drawing. |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_OVERLAY\_DRAW = 1 << 4 | Custom overlay drawing. |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_FRONT = 1 << 5 | 
Custom content layer foreground drawing.

**Since**: 20

 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_BEHIND = 1 << 6 | 

Custom content layer background drawing.

**Since**: 20

 |

#### \[h2\]ArkUI\_NodeAdapterEventType

enum ArkUI\_NodeAdapterEventType

**Description**

Enumerates node adapter events.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NODE\_ADAPTER\_EVENT\_WILL\_ATTACH\_TO\_NODE = 1 | This event occurs when the component is attached to the adapter. |
| NODE\_ADAPTER\_EVENT\_WILL\_DETACH\_FROM\_NODE = 2 | This event occurs when the component is detached from the adapter. |
| NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID = 3 | This event occurs when the adapter obtains the unique ID of the new element to add. |
| NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER = 4 | This event occurs when the adapter obtains the content of the new element to add. |
| NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER = 5 | This event occurs when the adapter removes an element. |

#### \[h2\]ArkUI\_NodeContentEventType

enum ArkUI\_NodeContentEventType

**Description**

Enumerates the event types for **NodeContent**.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NODE\_CONTENT\_EVENT\_ON\_ATTACH\_TO\_WINDOW = 0 | Attach event. |
| NODE\_CONTENT\_EVENT\_ON\_DETACH\_FROM\_WINDOW = 1 | Detach event. |

#### \[h2\]ArkUI\_InspectorErrorCode

enum ArkUI\_InspectorErrorCode

**Description**

Enumerates the [inspector](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-inspector-overview) error codes.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_INSPECTOR\_NATIVE\_RESULT\_SUCCESSFUL = 0 | Operation successful. |
| ARKUI\_INSPECTOR\_NATIVE\_RESULT\_BAD\_PARAMETER = -1 | Parameter error. |

#### Function Description

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetEventType()

ArkUI\_NodeEventType OH\_ArkUI\_NodeEvent\_GetEventType(ArkUI\_NodeEvent\* event)

**Description**

Obtains the type of a component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeEventType](#arkui_nodeeventtype) | Returns the type of the component event. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetTargetId()

int32\_t OH\_ArkUI\_NodeEvent\_GetTargetId(ArkUI\_NodeEvent\* event)

**Description**

Obtains the custom ID of a component event. The event ID is passed in as a parameter when the [registerNodeEvent](../../structs/arkui-nativenodeapi-1/document.md#registernodeevent) function is called and can be applied to the dispatch logic of the same event entry point function [registerNodeEventReceiver](../../structs/arkui-nativenodeapi-1/document.md#registernodeeventreceiver).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Custom ID of the component event. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetNodeHandle()

ArkUI\_NodeHandle OH\_ArkUI\_NodeEvent\_GetNodeHandle(ArkUI\_NodeEvent\* event)

**Description**

Obtains the component object that triggers an event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Component object that triggers the event. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetInputEvent()

ArkUI\_UIInputEvent\* OH\_ArkUI\_NodeEvent\_GetInputEvent(ArkUI\_NodeEvent\* event)

**Description**

Obtains input event (for example, touch event) data for a component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_UIInputEvent\*](../../structs/arkui-uiinputevent/document.md) | Pointer to the input event data. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent()

ArkUI\_NodeComponentEvent\* OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(ArkUI\_NodeEvent\* event)

**Description**

Obtains the numerical data in a component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeComponentEvent\*](../../structs/arkui-nodecomponentevent/document.md) | Pointer to the numerical data. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetStringAsyncEvent()

ArkUI\_StringAsyncEvent\* OH\_ArkUI\_NodeEvent\_GetStringAsyncEvent(ArkUI\_NodeEvent\* event)

**Description**

Obtains the string data in a component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_StringAsyncEvent\*](../../structs/arkui-stringasyncevent/document.md) | Pointer to the string data. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetTextChangeEvent()

ArkUI\_TextChangeEvent\* OH\_ArkUI\_NodeEvent\_GetTextChangeEvent(ArkUI\_NodeEvent\* event)

**Description**

Obtains the **ArkUI\_TextChangeEvent** data from the specified component event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to a component event. It cannot be null. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TextChangeEvent\*](../../structs/arkui-textchangeevent/document.md) | Pointer to the **ArkUI\_TextChangeEvent** object. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetUserData()

void\* OH\_ArkUI\_NodeEvent\_GetUserData(ArkUI\_NodeEvent\* event)

**Description**

Obtains the custom data in a component event. This parameter is passed in [registerNodeEvent](../../structs/arkui-nativenodeapi-1/document.md#registernodeevent) and can be applied to the service logic when the event is triggered.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to user data. |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetNumberValue()

int32\_t OH\_ArkUI\_NodeEvent\_GetNumberValue(ArkUI\_NodeEvent\* event, int32\_t index, ArkUI\_NumberValue\* value)

**Description**

Obtains the numeric-type parameter of a component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |
| int32\_t index | Return value index. |
| [ArkUI\_NumberValue](../../structs/arkui-numbervalue/document.md)\* value | Return value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INDEX\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter length in the parameter event exceeds the limit.

Returns [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the data does not exist in the component event.

 |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetStringValue()

int32\_t OH\_ArkUI\_NodeEvent\_GetStringValue(ArkUI\_NodeEvent\* event, int32\_t index, char\*\* string, int32\_t\* stringSize)

**Description**

Obtains the string-type parameter of a component event. The string data is valid only during an event callback. To use it outside an event callback, you are advised to copy the string data.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |
| int32\_t index | Return value index. |
| char\*\* string | Pointer to the string array. |
| int32\_t\* stringSize | Length of the string array. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INDEX\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter length in the parameter event exceeds the limit.

Returns [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the data does not exist in the component event.

 |

#### \[h2\]OH\_ArkUI\_NodeEvent\_SetReturnNumberValue()

int32\_t OH\_ArkUI\_NodeEvent\_SetReturnNumberValue(ArkUI\_NodeEvent\* event, ArkUI\_NumberValue\* value, int32\_t size)

**Description**

Sets the return value for a component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |
| [ArkUI\_NumberValue](../../structs/arkui-numbervalue/document.md)\* value | Event numeric type array. |
| int32\_t size | Size of the array. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the data does not exist in the component event.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_Create()

ArkUI\_NodeAdapterHandle OH\_ArkUI\_NodeAdapter\_Create()

**Description**

Creates a component adapter.

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) | Component adapter object. |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_Dispose()

void OH\_ArkUI\_NodeAdapter\_Dispose(ArkUI\_NodeAdapterHandle handle)

**Description**

Disposes of a component adapter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount()

int32\_t OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(ArkUI\_NodeAdapterHandle handle, uint32\_t size)

**Description**

Sets the total number of elements in the specified adapter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |
| uint32\_t size | Number of elements. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_GetTotalNodeCount()

uint32\_t OH\_ArkUI\_NodeAdapter\_GetTotalNodeCount(ArkUI\_NodeAdapterHandle handle)

**Description**

Obtains the total number of elements in the specified adapter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Total number of elements in the adapter. |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver()

int32\_t OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver(
ArkUI\_NodeAdapterHandle handle, void\* userData, void (\*receiver)(ArkUI\_NodeAdapterEvent\* event))

**Description**

Registers an event callback for the specified adapter. After the callback event is no longer needed, you need to call [OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver](#oh_arkui_nodeadapter_unregistereventreceiver) to deregister the callback event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |
| void\* userData | Custom data. |
| receiver | Event receiving callback. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver()

void OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver(ArkUI\_NodeAdapterHandle handle)

**Description**

Unregisters an event callback for the specified adapter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_ReloadAllItems()

int32\_t OH\_ArkUI\_NodeAdapter\_ReloadAllItems(ArkUI\_NodeAdapterHandle handle)

**Description**

Instructs the specified adapter to reload all elements.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_ReloadItem()

int32\_t OH\_ArkUI\_NodeAdapter\_ReloadItem(
ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)

**Description**

Instructs the specified adapter to reload certain elements.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |
| uint32\_t startPosition | Start position of an element change. |
| uint32\_t itemCount | Number of changed elements. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns **ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR** if the NodeAdapter requires a listener to be added.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_RemoveItem()

int32\_t OH\_ArkUI\_NodeAdapter\_RemoveItem(
ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)

**Description**

Instructs the specified adapter to remove certain elements.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |
| uint32\_t startPosition | Start position for deleting an element. |
| uint32\_t itemCount | Number of deleted elements. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns **ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR** if the NodeAdapter requires a listener to be added.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_InsertItem()

int32\_t OH\_ArkUI\_NodeAdapter\_InsertItem(
ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)

**Description**

Instructs the specified adapter to insert certain elements.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |
| uint32\_t startPosition | Start position for inserting an element. |
| uint32\_t itemCount | Number of inserted elements. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns **ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR** if the NodeAdapter requires a listener to be added.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_MoveItem()

int32\_t OH\_ArkUI\_NodeAdapter\_MoveItem(ArkUI\_NodeAdapterHandle handle, uint32\_t from, uint32\_t to)

**Description**

Instructs the specified adapter to move certain elements.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |
| uint32\_t from | Start position of the element shift. |
| uint32\_t to | End position of the element shift. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns **ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR** if the NodeAdapter requires a listener to be added.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapter\_GetAllItems()

int32\_t OH\_ArkUI\_NodeAdapter\_GetAllItems(ArkUI\_NodeAdapterHandle handle, ArkUI\_NodeHandle\*\* items, uint32\_t\* size)

**Description**

Obtains all elements stored in the specified adapter. When the API is called, the array object pointer of the element is returned. You must release the memory data to which the pointer points.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterHandle](../../structs/arkui-nodeadapter/document.md) handle | Component adapter object. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md)\*\* items | Array of nodes in the adapter. |
| uint32\_t\* size | Number of elements. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns **ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR** if the NodeAdapter requires a listener to be added.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapterEvent\_GetUserData()

void\* OH\_ArkUI\_NodeAdapterEvent\_GetUserData(ArkUI\_NodeAdapterEvent\* event)

**Description**

Obtains the custom data passed in during registration of the specified event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md)\* event | Adapter event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to custom data. |

#### \[h2\]OH\_ArkUI\_NodeAdapterEvent\_GetType()

ArkUI\_NodeAdapterEventType OH\_ArkUI\_NodeAdapterEvent\_GetType(ArkUI\_NodeAdapterEvent\* event)

**Description**

Obtains the event type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md)\* event | Adapter event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEventType](#arkui_nodeadaptereventtype) | Event type. |

#### \[h2\]OH\_ArkUI\_NodeAdapterEvent\_GetRemovedNode()

ArkUI\_NodeHandle OH\_ArkUI\_NodeAdapterEvent\_GetRemovedNode(ArkUI\_NodeAdapterEvent\* event)

**Description**

Obtains the element to be removed for the event to be destroyed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md)\* event | Adapter event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Element to be destroyed. |

#### \[h2\]OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex()

uint32\_t OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(ArkUI\_NodeAdapterEvent\* event)

**Description**

Obtains the index of the element to be operated for the specified adapter event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md)\* event | Adapter event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Sequence number of an element. |

#### \[h2\]OH\_ArkUI\_NodeAdapterEvent\_GetHostNode()

ArkUI\_NodeHandle OH\_ArkUI\_NodeAdapterEvent\_GetHostNode(ArkUI\_NodeAdapterEvent\* event)

**Description**

Obtains the scrollable container node that uses the specified adapter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md)\* event | Adapter event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Returns the scrollable container node that uses the specified adapter. |

#### \[h2\]OH\_ArkUI\_NodeAdapterEvent\_SetItem()

int32\_t OH\_ArkUI\_NodeAdapterEvent\_SetItem(ArkUI\_NodeAdapterEvent\* event, ArkUI\_NodeHandle node)

**Description**

Sets the component to be added to the specified adapter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md)\* event | Adapter event object. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Component to be added. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeAdapterEvent\_SetNodeId()

int32\_t OH\_ArkUI\_NodeAdapterEvent\_SetNodeId(ArkUI\_NodeAdapterEvent\* event, int32\_t id)

**Description**

Sets the component ID to be generated.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeAdapterEvent](../../structs/arkui-nodeadapterevent/document.md)\* event | Adapter event object. |
| int32\_t id | Returned component ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetLayoutConstraintInMeasure()

ArkUI\_LayoutConstraint\* OH\_ArkUI\_NodeCustomEvent\_GetLayoutConstraintInMeasure(ArkUI\_NodeCustomEvent\* event)

**Description**

Obtains the size constraint for measurement through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* | Pointer to the constraint size. |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetPositionInLayout()

ArkUI\_IntOffset OH\_ArkUI\_NodeCustomEvent\_GetPositionInLayout(ArkUI\_NodeCustomEvent\* event)

**Description**

Obtains the expected position of a component relative to its parent component in the layout phase through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md) | Expected position relative to the parent component. |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw()

ArkUI\_DrawContext\* OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(ArkUI\_NodeCustomEvent\* event)

**Description**

Obtains the drawing context through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DrawContext\*](../../structs/arkui-drawcontext/document.md) | Drawing context. |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId()

int32\_t OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId(ArkUI\_NodeCustomEvent\* event)

**Description**

Obtains the ID of a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the custom event ID. |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetUserData()

void\* OH\_ArkUI\_NodeCustomEvent\_GetUserData(ArkUI\_NodeCustomEvent\* event)

**Description**

Obtains custom event parameters through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | Custom event. |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetNodeHandle()

ArkUI\_NodeHandle OH\_ArkUI\_NodeCustomEvent\_GetNodeHandle(ArkUI\_NodeCustomEvent\* event)

**Description**

Obtains a component object through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Returns the obtained component object. |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetEventType()

ArkUI\_NodeCustomEventType OH\_ArkUI\_NodeCustomEvent\_GetEventType(ArkUI\_NodeCustomEvent\* event)

**Description**

Obtains the event type through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEventType](#arkui_nodecustomeventtype) | Returns the type of the custom component event. |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanMeasureInfo()

int32\_t OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanMeasureInfo(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanMeasureInfo\* info)

**Description**

Obtains the measurement information of a custom span through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |
| [ArkUI\_CustomSpanMeasureInfo](../../structs/arkui-customspanmeasureinfo/document.md)\* info | Measurement information to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_SetCustomSpanMetrics()

int32\_t OH\_ArkUI\_NodeCustomEvent\_SetCustomSpanMetrics(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanMetrics\* metrics)

**Description**

Sets the measurement metrics of a custom span through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |
| [ArkUI\_CustomSpanMetrics](../../structs/arkui-customspanmetrics/document.md)\* metrics | Measurement metrics to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanDrawInfo()

int32\_t OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanDrawInfo(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanDrawInfo\* info)

**Description**

Obtains the drawing information of a custom span through a custom component event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeCustomEvent](../../structs/arkui-nodecustomevent/document.md)\* event | Pointer to the custom component event. |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md)\* info | Drawing information to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]ArkUI\_NodeContentCallback()

typedef void (\*ArkUI\_NodeContentCallback)(ArkUI\_NodeContentEvent\* event)

**Description**

Defines a callback for the NodeContent event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentEvent](../../structs/arkui-nodecontentevent/document.md)\* event | Pointer to the **NodeContent** event. |

#### \[h2\]OH\_ArkUI\_NodeContent\_RegisterCallback()

int32\_t OH\_ArkUI\_NodeContent\_RegisterCallback(ArkUI\_NodeContentHandle content, ArkUI\_NodeContentCallback callback)

**Description**

Registers an event callback for the **NodeContent**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md) content | **NodeContent** object for which an event needs to be registered. |
| [ArkUI\_NodeContentCallback](#arkui_nodecontentcallback) callback | Callback to be executed when the event is triggered. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeContentEvent\_GetEventType()

ArkUI\_NodeContentEventType OH\_ArkUI\_NodeContentEvent\_GetEventType(ArkUI\_NodeContentEvent\* event)

**Description**

Obtains the type of the specified **NodeContent** event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentEvent](../../structs/arkui-nodecontentevent/document.md)\* event | Pointer to the **NodeContent** event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeContentEventType](#arkui_nodecontenteventtype) | **NodeContent** event type. |

#### \[h2\]OH\_ArkUI\_NodeContentEvent\_GetNodeContentHandle()

ArkUI\_NodeContentHandle OH\_ArkUI\_NodeContentEvent\_GetNodeContentHandle(ArkUI\_NodeContentEvent\* event)

**Description**

Obtains the object that triggers the specified **NodeContent** event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentEvent](../../structs/arkui-nodecontentevent/document.md)\* event | Pointer to the **NodeContent** event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md) | **NodeContent** object that triggers the event. |

#### \[h2\]OH\_ArkUI\_NodeContent\_SetUserData()

int32\_t OH\_ArkUI\_NodeContent\_SetUserData(ArkUI\_NodeContentHandle content, void\* userData)

**Description**

Saves custom data to the specified **NodeContent** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md) content | **NodeContent** object whose user-defined data needs to be saved. |
| void\* userData | User-defined data to be saved. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeContent\_GetUserData()

void\* OH\_ArkUI\_NodeContent\_GetUserData(ArkUI\_NodeContentHandle content)

**Description**

Obtains the custom data saved on the specified **NodeContent** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md) content | **NodeContent** object whose user-defined data needs to be saved. |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | Custom data. |

#### \[h2\]OH\_ArkUI\_NodeContent\_AddNode()

int32\_t OH\_ArkUI\_NodeContent\_AddNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)

**Description**

Adds an ArkUI component node to the specified **NodeContent** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md) content | **NodeContent** object to which a node is to be added. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Node to be added. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](../native-type-h/document.md#arkui_errorcode) if a child node has been accepted. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_NodeContent\_RemoveNode()

int32\_t OH\_ArkUI\_NodeContent\_RemoveNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)

**Description**

Removes an ArkUI component node from the specified **NodeContent** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md) content | **NodeContent** object of the node to be deleted. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Node to be deleted. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeContent\_InsertNode()

int32\_t OH\_ArkUI\_NodeContent\_InsertNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node, int32\_t position)

**Description**

Inserts an ArkUI component node into a specific position of the specified **NodeContent** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeContentHandle](../../structs/arkui-nodecontent/document.md) content | **NodeContent** object of the node to be inserted. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Node to be inserted. |
| int32\_t position | Start time for an asset to be inserted, |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](../native-type-h/document.md#arkui_errorcode) if a child node has been accepted. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetLayoutSize()

int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutSize(ArkUI\_NodeHandle node, ArkUI\_IntSize\* size)

**Description**

Obtains the layout area size of the component. The size does not count in transformation attributes, such as scale.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_IntSize](../../structs/arkui-intsize/document.md)\* size | Size of the layout area, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetLayoutPosition()

int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPosition(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* localOffset)

**Description**

Obtains the position of the component's layout area relative to its parent component. The relative position does not count in transformation attributes, such as translate.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md)\* localOffset | Offset of the component handle relative to the parent component, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetLayoutPositionInWindow()

int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInWindow(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* globalOffset)

**Description**

Obtains the position of the component's layout area relative to the window. The relative position does not count in transformation attributes, such as translate.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md)\* globalOffset | Offset of the component handle relative to the window, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetLayoutPositionInScreen()

int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInScreen(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* screenOffset)

**Description**

Obtains the position of the component's layout area relative to the screen. The relative position does not count in transformation attributes, such as translate.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md)\* screenOffset | Offset of the component handle relative to the screen, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetLayoutPositionInGlobalDisplay()

int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInGlobalDisplay(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* offset)

**Description**

Obtains the offset of the specified component relative to the global display. The relative position does not count in transformation attributes, such as translate.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md)\* offset | Offset of the component handle relative to the screen, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInWindow()

int32\_t OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInWindow(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* translateOffset)

**Description**

Obtains the position of the component in the window, including the translate attribute.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md)\* translateOffset | Accumulated offset of the component, its parent component, and its ancestor node, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInScreen()

int32\_t OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInScreen(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* translateOffset)

**Description**

Obtains the position of the component on the screen, including the translate attribute.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md)\* translateOffset | Accumulated offset of the component, its parent component, and its ancestor node, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_AddCustomProperty()

void OH\_ArkUI\_NodeUtils\_AddCustomProperty(ArkUI\_NodeHandle node, const char\* name, const char\* value)

**Description**

Sets a custom property for a component. This API takes effect only in the main thread.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| const char\* name | Name of the custom property. A null pointer is not allowed. |
| const char\* value | Value of the custom property. A null pointer is not allowed. |

#### \[h2\]OH\_ArkUI\_NodeUtils\_RemoveCustomProperty()

void OH\_ArkUI\_NodeUtils\_RemoveCustomProperty(ArkUI\_NodeHandle node, const char\* name)

**Description**

Removes a custom property that has been set for the specified component.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| const char\* name | Name of the custom property. |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetCustomProperty()

int32\_t OH\_ArkUI\_NodeUtils\_GetCustomProperty(ArkUI\_NodeHandle node, const char\* name, ArkUI\_CustomProperty\*\* handle)

**Description**

Obtains the value of a custom property of the specified component.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| const char\* name | Name of the custom property. |
| [ArkUI\_CustomProperty](../../structs/arkui-customproperty/document.md)\*\* handle | Pointer to the struct that receives the custom property corresponding to the key parameter name. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetParentInPageTree()

ArkUI\_NodeHandle OH\_ArkUI\_NodeUtils\_GetParentInPageTree(ArkUI\_NodeHandle node)

**Description**

Obtains the parent node, which can be a component node created with ArkTS.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Pointer to the component if the component exists; returns **NULL** otherwise. |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo()

int32\_t OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo(ArkUI\_NodeHandle head, ArkUI\_ActiveChildrenInfo\*\* handle)

**Description**

Obtains all active child nodes of the specified node. Spans are not counted as child nodes. In **LazyForEach** scenarios, you are advised to use the [OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode](#oh_arkui_nodeutils_getchildwithexpandmode) API for traversal.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) head | Node for which to obtain the child nodes. |
| [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md)\*\* handle | Pointer to the struct containing information about the child nodes of the head node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetCurrentPageRootNode()

ArkUI\_NodeHandle OH\_ArkUI\_NodeUtils\_GetCurrentPageRootNode(ArkUI\_NodeHandle node)

**Description**

Obtains the root node of the current page.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Returns the pointer to the root node if the node exists; returns **NULL** otherwise. |

#### \[h2\]OH\_ArkUI\_NodeUtils\_IsCreatedByNDK()

bool OH\_ArkUI\_NodeUtils\_IsCreatedByNDK(ArkUI\_NodeHandle node)

**Description**

Checks whether the specified component is created with C APIs.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Returns whether the node is created with the C API. The value **true** means that the node is created with the C API, and **false** means the opposite. |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetNodeType()

int32\_t OH\_ArkUI\_NodeUtils\_GetNodeType(ArkUI\_NodeHandle node)

**Description**

Obtains the type of the specified node.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the type of the node. Returns **\-1** if the type is not supported yet. For details about the available types, see [ArkUI\_NodeType](#arkui_nodetype). |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetWindowInfo()

int32\_t OH\_ArkUI\_NodeUtils\_GetWindowInfo(ArkUI\_NodeHandle node, ArkUI\_HostWindowInfo\*\* info)

**Description**

Obtains the information about the window to which a node belongs.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md)\*\* info | Pointer to the window information object. The memory allocated for this object must be released using [OH\_ArkUI\_HostWindowInfo\_Destroy](../native-type-h/document.md#oh_arkui_hostwindowinfo_destroy). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](../native-type-h/document.md#arkui_errorcode) if the node is not mounted on the main component tree.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_MoveTo()

int32\_t OH\_ArkUI\_NodeUtils\_MoveTo(ArkUI\_NodeHandle node, ArkUI\_NodeHandle target\_parent, int32\_t index)

**Description**

Moves a node to a target parent node as a child.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Node to be moved. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) target\_parent | Pointer to the target parent node. |
| int32\_t index | Index of the node after the movement. If the index is invalid, the node will be added to the end of the target parent node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](../native-type-h/document.md#arkui_errorcode) if a child node has been accepted. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_NativeModule\_InvalidateAttributes()

int32\_t OH\_ArkUI\_NativeModule\_InvalidateAttributes(ArkUI\_NodeHandle node)

**Description**

Triggers the node attribute update in this frame.

If the attributes of the current node are modified after the build phase, these changes do not take effect immediately but are deferred for batch processing in the next frame.

This API forces immediate node updates within the current frame, ensuring that rendering effects are applied synchronously.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Node whose attributes are to be updated. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_List\_CloseAllSwipeActions()

int32\_t OH\_ArkUI\_List\_CloseAllSwipeActions(ArkUI\_NodeHandle node, void\* userData, void (\*onFinish)(void\* userData))

**Description**

Collapses the list items in the expanded state.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Node object for which an event needs to be registered. |
| void\* userData | Custom event parameter, which is passed in the callback when the event is triggered. |
| onFinish | Callback triggered after the collapse animation is complete. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the event is not supported.

 |

#### \[h2\]OH\_ArkUI\_GetContextByNode()

ArkUI\_ContextHandle OH\_ArkUI\_GetContextByNode(ArkUI\_NodeHandle node)

**Description**

Obtains the pointer to the UI context object of the specified node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Specified node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) | Pointer to the UI context object. |

#### \[h2\]OH\_ArkUI\_RegisterSystemColorModeChangeEvent()

int32\_t OH\_ArkUI\_RegisterSystemColorModeChangeEvent(ArkUI\_NodeHandle node,void\* userData, void (\*onColorModeChange)(ArkUI\_SystemColorMode colorMode, void\* userData))

**Description**

Registers an event listener for system color mode changes. A single component can only register one callback for system color mode changes. For implementation examples, see [Listening for Component Events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-listen-to-component-events).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Specified node. |
| void\* userData | Custom event parameter, which is passed in the callback when the event is triggered. |
| onColorModeChange | Callback to be executed when the event is triggered. [ArkUI\_SystemColorMode](../native-type-h/document.md#arkui_systemcolormode) defines the system color mode (light/dark). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_UnregisterSystemColorModeChangeEvent()

void OH\_ArkUI\_UnregisterSystemColorModeChangeEvent(ArkUI\_NodeHandle node)

**Description**

Unregisters the event listener for system color mode changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Specified node. |

#### \[h2\]OH\_ArkUI\_RegisterSystemFontStyleChangeEvent()

int32\_t OH\_ArkUI\_RegisterSystemFontStyleChangeEvent(ArkUI\_NodeHandle node,void\* userData, void (\*onFontStyleChange)(ArkUI\_SystemFontStyleEvent\* event, void\* userData))

**Description**

Registers an event listener for system font style changes. A single component can only register one callback for system font style changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Specified node. |
| void\* userData | Custom event parameter, which is passed in the callback when the event is triggered. |
| onFontStyleChange | Callback to be executed when the event is triggered. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_UnregisterSystemFontStyleChangeEvent()

void OH\_ArkUI\_UnregisterSystemFontStyleChangeEvent(ArkUI\_NodeHandle node)

**Description**

Unregisters the event listener for system font style changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Specified node. |

#### \[h2\]OH\_ArkUI\_SystemFontStyleEvent\_GetFontSizeScale()

float OH\_ArkUI\_SystemFontStyleEvent\_GetFontSizeScale(const ArkUI\_SystemFontStyleEvent\* event)

**Description**

Obtains the font size from the system font style change event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_SystemFontStyleEvent](../../structs/arkui-systemfontstyleevent/document.md)\* event | Pointer to the current system font style change event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Returns the font size scale after the change. Default value: **1.0**. |

#### \[h2\]OH\_ArkUI\_SystemFontStyleEvent\_GetFontWeightScale()

float OH\_ArkUI\_SystemFontStyleEvent\_GetFontWeightScale(const ArkUI\_SystemFontStyleEvent\* event)

**Description**

Obtains the font weight from the system font style change event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_SystemFontStyleEvent](../../structs/arkui-systemfontstyleevent/document.md)\* event | Pointer to the current system font style change event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Returns the font weight scale after the change. Default value: **1.0**. |

#### \[h2\]OH\_ArkUI\_RegisterLayoutCallbackOnNodeHandle()

int32\_t OH\_ArkUI\_RegisterLayoutCallbackOnNodeHandle(ArkUI\_NodeHandle node,void\* userData, void (\*onLayoutCompleted)(void\* userData))

**Description**

Registers a layout completion callback function for a specific node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node for which the callback function is to be registered. |
| void\* userData | Custom parameter passed to the callback function when it is invoked. |
| onLayoutCompleted | Callback function to be invoked when layout is completed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_RegisterDrawCallbackOnNodeHandle()

int32\_t OH\_ArkUI\_RegisterDrawCallbackOnNodeHandle(ArkUI\_NodeHandle node,void\* userData, void (\*onDrawCompleted)(void\* userData))

**Description**

Registers a drawing completion callback function for a specific node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node for which the callback function is to be registered. |
| void\* userData | Custom parameter passed to the callback function when it is invoked. |
| onDrawCompleted | Callback function to be invoked when drawing is completed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_UnregisterLayoutCallbackOnNodeHandle()

int32\_t OH\_ArkUI\_UnregisterLayoutCallbackOnNodeHandle(ArkUI\_NodeHandle node)

**Description**

Unregisters the layout completion callback function for a specific node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node for which the callback function is to be unregistered. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_UnregisterDrawCallbackOnNodeHandle()

int32\_t OH\_ArkUI\_UnregisterDrawCallbackOnNodeHandle(ArkUI\_NodeHandle node)

**Description**

Unregisters the drawing completion callback function for a specific node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node for which the callback function is to be unregistered. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetNodeSnapshot()

int32\_t OH\_ArkUI\_GetNodeSnapshot(ArkUI\_NodeHandle node, ArkUI\_SnapshotOptions\* snapshotOptions,OH\_PixelmapNative\*\* pixelmap)

**Description**

Obtains a snapshot of a given component. If the node is not in the component tree or has not been rendered, the snapshot operation will fail. When the **Pixelmap** object created is no longer in use, it should be released by calling **OH\_PixelmapNative\_Release**.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node to capture a snapshot. |
| [ArkUI\_SnapshotOptions](../../structs/arkui-snapshotoptions/document.md)\* snapshotOptions | Snapshot settings. If the value is null, the default settings are used. |
| [OH\_PixelmapNative\*](../../structs/oh-pixelmapnative/document.md)\* pixelmap | Pointer to the Pixelmap created by the system. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_INTERNAL\_ERROR](../native-type-h/document.md#arkui_errorcode) if the snapshot fails, returning a null pointer.

Returns [ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_TIMEOUT](../native-type-h/document.md#arkui_errorcode) if the snapshot operation times out.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById()

int32\_t OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById(const char\* id, ArkUI\_NodeHandle\* node)

**Description**

Obtains the target node based on the provided user ID.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* id | ID of the target node. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md)\* node | Pointer to the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId()

int32\_t OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId(const uint32\_t uniqueId, ArkUI\_NodeHandle\* node)

**Description**

Obtain a node by its unique ID.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const uint32\_t uniqueId | Unique ID of the target node. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md)\* node | Pointer to the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetNodeUniqueId()

int32\_t OH\_ArkUI\_NodeUtils\_GetNodeUniqueId(ArkUI\_NodeHandle node, int32\_t\* uniqueId)

**Description**

Obtains the unique ID of the target node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | ArkUI node pointer. |
| int32\_t\* uniqueId | Unique ID of the target node. The component ID is read-only and unique in the process. If the node exists, the unique ID of the node is returned. Otherwise, **\-1** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_NativeModule\_AdoptChild()

int32\_t OH\_ArkUI\_NativeModule\_AdoptChild(ArkUI\_NodeHandle node, ArkUI\_NodeHandle child)

**Description**

Adopts the target node as an affiliated node. The adopted node must not have an existing parent. This operation establishes a lifecycle relationship without adding the node as a visual child in the component tree.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to an **ArkUI\_NodeHandle**, representing the parent node that will adopt another node. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) child | Pointer to an **ArkUI\_NodeHandle**, representing the child node to be adopted. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_NODE\_HAS\_PARENT](../native-type-h/document.md#arkui_errorcode) if the adopted node already has a parent node.

Returns [ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_BE\_ADOPTED](../native-type-h/document.md#arkui_errorcode) if the node cannot be adopted as an affiliated node.

Returns [ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_ADOPT\_TO](../native-type-h/document.md#arkui_errorcode) if the node cannot adopt other affiliated nodes.

 |

#### \[h2\]OH\_ArkUI\_NativeModule\_RemoveAdoptedChild()

int32\_t OH\_ArkUI\_NativeModule\_RemoveAdoptedChild(ArkUI\_NodeHandle node, ArkUI\_NodeHandle child)

**Description**

Removes a previously-adopted affiliated node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**, which specifies the parent node. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) child | Pointer to **ArkUI\_NodeHandle**, which specifies the node to be removed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_NOT\_IN\_ADOPTED\_CHILDREN](../native-type-h/document.md#arkui_errorcode) if the node is not an affiliated node adopted by the target node.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption()

int32\_t OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption(ArkUI\_NodeHandle node, ArkUI\_CrossLanguageOption\* option)

**Description**

Sets the cross-language options for the target node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the target node. |
| [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md)\* option | Cross-language configuration option [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption()

int32\_t OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption(ArkUI\_NodeHandle node, ArkUI\_CrossLanguageOption\* option)

**Description**

Obtains the cross-language options for the target node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the target node. |
| [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md)\* option | Cross-language configuration option [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand()

int32\_t OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand(ArkUI\_NodeHandle node, uint32\_t\* index)

**Description**

Obtains the index of the first child node of the target node in the tree without expanding any nodes.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the target node. |
| uint32\_t\* index | Pointer to a variable where the index of the first child node is stored. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand()

int32\_t OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand(ArkUI\_NodeHandle node, uint32\_t\* index)

**Description**

Obtains the index of the last child node of the target node in the tree without expanding any nodes.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the target node. |
| uint32\_t\* index | Pointer to a variable where the index of the first child node is stored. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode()

int32\_t OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode(ArkUI\_NodeHandle node, int32\_t position,ArkUI\_NodeHandle\* subnode, uint32\_t expandMode)

**Description**

Obtains a child node at the specified index using different expansion modes.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the target node. |
| int32\_t position | Index of the child node to obtain. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md)\* subnode | Pointer to the obtained child node. |
| uint32\_t expandMode | Expansion mode for node traversal. For details, see [ArkUI\_ExpandMode](../native-type-h/document.md#arkui_expandmode). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NodeUtils\_GetPositionToParent()

int32\_t OH\_ArkUI\_NodeUtils\_GetPositionToParent(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* globalOffset)

**Description**

Obtains the offset of the target node relative to its parent node, in px.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md)\* globalOffset | Offset of the target node relative to its parent node, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AddSupportedUIStates()

ArkUI\_ErrorCode OH\_ArkUI\_AddSupportedUIStates(ArkUI\_NodeHandle node, int32\_t uiStates,void (statesChangeHandler)(int32\_t currentStates, void\* userData), bool excludeInner, void\* userData)

**Description**

Adds the [polymorphic style states](../../../arkts-components/universal-attributes/polymorphic-style/document.md) supported by the component. To handle states efficiently, specify the states of interest and their corresponding handlers. When a state of interest occurs, the handler will be executed. You can adjust the UI style based on the current state within the callback. If this API is called multiple times on the same node, the last set of states and handlers will take precedence. Some component types have default system handling for certain states. For example, the **Button** component has a default style effect for the PRESSED state. When custom state handling is implemented on such components, the default style effect will be applied first, followed by the custom style changes, resulting in a combined effect. To disable the default style effects, set **excludeInner** to **true**, if this is allowed by the system implementation. When this API is called, the provided handler function will be executed immediately. There is no need to explicitly register a listener for the NORMAL state. Once a non-NORMAL state is registered, the system will automatically notify your application when the state changes back to NORMAL.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| int32\_t uiStates | Target UI states to be handled on the node. The combined result of all target UI states can be calculated using the **|** operator. Example: **targetUIStates = ArkUI\_UIState::PRESSED | ArkUI\_UIState::FOCUSED**. |
| void (statesChangeHandler)(int32\_t currentStates, void\* userData) | Handler for UI state changes. It returns the current UI status. The value is the result of combining all current state enum values using the **|** operator. You can determine the state using the **&** operator. Example: **if (currentStates & ArkUI\_UIState::PRESSED == ArkUI\_UIState::PRESSED)**. However, for checking the normal state, use the equality operator directly. Example: **if (currentStates == ArkUI\_UIState::NORMAL)**. |
| bool excludeInner | Whether to disable the default state styles. **true**: Disable the default state styles. **false**: Do not disable the default state styles. |
| void\* userData | Custom data used in the **onDrawCompleted** callback. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_RemoveSupportedUIStates()

ArkUI\_ErrorCode OH\_ArkUI\_RemoveSupportedUIStates(ArkUI\_NodeHandle node, int32\_t uiStates)

**Description**

Removes registered UI states. When all states registered using **OH\_ArkUI\_AddSupportedUIStates** are removed, the registered **stateChangeHandler** will no longer be executed.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| int32\_t uiStates | Target UI states to be removed. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_RunTaskInScope()

int32\_t OH\_ArkUI\_RunTaskInScope(ArkUI\_ContextHandle uiContext, void\* userData, void(\*callback)(void\* userData))

**Description**

Executes the specified callback in the target UI context. For the implementation example, see [Ensuring Multi-Instance Functionality in the NDK](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-scope-task).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | Pointer to the target UI context. |
| void\* userData | User-defined data pointer for processing custom data within the callback function. You are responsible for ensuring the validity of the data when the custom function is executed. |
| void(\*callback)(void\* userData) | User-defined callback function. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID](../native-type-h/document.md#arkui_errorcode) if the **UIContext** object is invalid.

Returns [ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID](../native-type-h/document.md#arkui_errorcode) if the callback function is invalid.

 |

#### \[h2\]OH\_ArkUI\_PostAsyncUITask()

int32\_t OH\_ArkUI\_PostAsyncUITask(ArkUI\_ContextHandle context, void\* asyncUITaskData,
    void (\*asyncUITask)(void\* asyncUITaskData), void (\*onFinish)(void\* asyncUITaskData))

**Description**

Submits the **asyncUITask** function to a non-UI thread provided by the ArkUI framework for execution. After **asyncUITask** finishes execution, the **onFinish** function is called in the UI thread.

This is suitable for scenarios involving multi-threaded UI component creation. You can use this API to create UI components in non-UI threads and then mount the created components to the main tree in the UI thread.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) context | Pointer to the UI instance object. |
| void\* asyncUITaskData | Pointer to the user-defined data, which is passed as the input parameter of **asyncUITask** and **onFinish**. A null pointer is allowed. |
| asyncUITask | Function executed in the non-UI thread. |
| onFinish | Function executed on the UI thread after **asyncUITask** is completed. A null pointer is allowed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the context object is invalid, or **asyncUITask** is a null pointer.

 |

#### \[h2\]OH\_ArkUI\_PostUITask()

int32\_t OH\_ArkUI\_PostUITask(ArkUI\_ContextHandle context, void\* taskData, void (\*task)(void\* taskData))

**Description**

Submits the **task** function to the UI thread for execution.

This is suitable for scenarios involving multi-threaded UI component creation. When you create UI components in a self-built thread, you can use this API to mount the created components to the main tree on the UI thread.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) context | Pointer to the UI instance object. |
| void\* taskData | Pointer to the user-defined data, which is passed as the input parameter of **task**. A null pointer is allowed. |
| task | Function executed in the UI thread. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the context object is invalid, or **task** is a null pointer.

 |

#### \[h2\]OH\_ArkUI\_PostUITaskAndWait()

int32\_t OH\_ArkUI\_PostUITaskAndWait(ArkUI\_ContextHandle context, void\* taskData, void (\*task)(void\* taskData))

**Description**

Submits the **task** function to the UI thread for execution. The thread calling this API will block until the **task** function completes execution. Calling this API from the UI thread is equivalent to synchronously calling the **task** function.

This is suitable for scenarios involving multi-threaded UI component creation. When you need to call functions that are only supported on the UI thread during the multi-threaded component creation process, you can use this API to return to the UI thread to call the function and then resume multi-threaded component creation after the call completes.

When the UI thread is under high load, non-UI threads calling this API may block for extended periods, affecting the performance of multi-threaded UI component creation. Frequent use is not recommended.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) context | Pointer to the UI instance object. |
| void\* taskData | Pointer to the user-defined data, which is passed as the input parameter of **task**. A null pointer is allowed. |
| task | Function executed in the UI thread. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if the context object is invalid, or **task** is a null pointer.

 |

#### \[h2\]OH\_ArkUI\_NativeModule\_RegisterCommonEvent()

int32\_t OH\_ArkUI\_NativeModule\_RegisterCommonEvent(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType, void\* userData, void (\*callback)(ArkUI\_NodeEvent\* event))

**Description**

Registers a basic event callback for the target node.

Currently, the following event types are supported: **NODE\_ON\_CLICK\_EVENT**, **NODE\_TOUCH\_EVENT**, **NODE\_EVENT\_ON\_APPEAR**, **NODE\_EVENT\_ON\_DISAPPEAR**, **NODE\_ON\_KEY\_EVENT**, **NODE\_ON\_FOCUS**, **NODE\_ON\_BLUR**, **NODE\_ON\_HOVER**, **NODE\_ON\_MOUSE**, and **NODE\_ON\_SIZE\_CHANGE**. For details, see [ArkUI\_NodeEventType](#arkui_nodeeventtype).

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_NodeEventType](#arkui_nodeeventtype) eventType | Event type. |
| void\* userData | User-defined data pointer for processing custom data within the callback function. You are responsible for ensuring the validity of the data when the custom function is executed. |
| callback | User-defined callback function. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NODE\_UNSUPPORTED\_EVENT\_TYPE](../native-type-h/document.md#arkui_errorcode) if the event type is not supported.

 |

#### \[h2\]OH\_ArkUI\_NativeModule\_UnregisterCommonEvent()

int32\_t OH\_ArkUI\_NativeModule\_UnregisterCommonEvent(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType)

**Description**

Unregisters the basic event callback for the target node.

For details about the supported event types, see [OH\_ArkUI\_NativeModule\_RegisterCommonEvent](#oh_arkui_nativemodule_registercommonevent).

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_NodeEventType](#arkui_nodeeventtype) eventType | Event type. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NODE\_UNSUPPORTED\_EVENT\_TYPE](../native-type-h/document.md#arkui_errorcode) if the event type is not supported.

 |

#### \[h2\]OH\_ArkUI\_NativeModule\_RegisterCommonVisibleAreaApproximateChangeEvent()

int32\_t OH\_ArkUI\_NativeModule\_RegisterCommonVisibleAreaApproximateChangeEvent(ArkUI\_NodeHandle node, float\* ratios, int32\_t size, float expectedUpdateInterval, void\* userData, void (\*callback)(ArkUI\_NodeEvent\* event))

**Description**

Registers a basic event callback for visible area changes with a constrained callback interval.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| float\* ratios | Array of threshold ratios, representing the visible area of the component. |
| int32\_t size | Size of the array of threshold ratios. |
| float expectedUpdateInterval | Expected calculation interval. |
| void\* userData | User-defined data pointer for processing custom data within the callback function. You are responsible for ensuring the validity of the data when the custom function is executed. |
| callback | User-defined callback function. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_NativeModule\_UnregisterCommonVisibleAreaApproximateChangeEvent()

int32\_t OH\_ArkUI\_NativeModule\_UnregisterCommonVisibleAreaApproximateChangeEvent(ArkUI\_NodeHandle node)

**Description**

Unregisters the basic event callback for visible area changes with a constrained callback interval.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Swiper\_FinishAnimation()

int32\_t OH\_ArkUI\_Swiper\_FinishAnimation(ArkUI\_NodeHandle node)

**Description**

Stops the page flip animation that is being executed on the specified **Swiper** node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Specified node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetForceDarkConfig()

int32\_t OH\_ArkUI\_SetForceDarkConfig(ArkUI\_ContextHandle uiContext, bool forceDark, ArkUI\_NodeType nodeType, uint32\_t (\*colorInvertFunc)(uint32\_t color))

**Description**

Sets the color inversion algorithm for components and instances. For details, see [Using Color Inversion for Quick Dark Mode Adaptation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ui-dark-light-color-adaptation#using-color-inversion-for-quick-dark-mode-adaptation).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | 
Pointer to the UI instance object.

If the value is **null**, this function applies to the entire application process.

 |
| bool forceDark | Whether to use the color inversion capability. **true** to use; **false** otherwise. |
| [ArkUI\_NodeType](#arkui_nodetype) nodeType | 

Component scope where the color inversion capability takes effect.

**ARKUI\_NODE\_UNDEFINED** indicates that the setting takes effect for all component types.

 |
| colorInvertFunc | 

Custom color inversion algorithm function.

If the value is **nullptr**, the default color inversion algorithm is used for the component, that is, the three primary colors are inverted.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_FORCE\_DARK\_CONFIG\_INVALID](../native-type-h/document.md#arkui_errorcode) if the input parameter of the color inversion capability is incorrect.

 |

#### \[h2\]OH\_ArkUI\_NodeEvent\_GetTouchTestInfo()

ArkUI\_TouchTestInfo\* OH\_ArkUI\_NodeEvent\_GetTouchTestInfo(ArkUI\_NodeEvent\* nodeEvent)

**Description**

Obtains the touch test information in a component event.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md)\* event | Pointer to the component event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md)\* | Pointer to the [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md) object. If the input parameter is invalid or is not touch test information, **null** is returned. |
