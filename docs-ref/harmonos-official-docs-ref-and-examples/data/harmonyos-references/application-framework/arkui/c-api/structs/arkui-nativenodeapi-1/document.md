# ArkUI\_NativeNodeAPI\_1

typedef struct {...} ArkUI\_NativeNodeAPI\_1

#### Overview

Provides a collection of native-side Node type APIs provided by ArkUI. APIs related to the Node module must be called on the main thread.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_node.h](../../header-files/native-node-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t version | Structure version, that is, the version number of the **ArkUI\_NativeNodeAPI\_1** structure. The version number is provided by the system and does not need to be modified. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle (\*createNode)(ArkUI\_NodeType type)](#createnode) | Creates a component based on [ArkUI\_NodeType](../../header-files/native-node-h/document.md#arkui_nodetype) and returns the pointer to the component object. |
| [void (\*disposeNode)(ArkUI\_NodeHandle node)](#disposenode) | Disposes of the component to which the specified pointer points. |
| [int32\_t (\*addChild)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child)](#addchild) | Attaches a component to a parent node. |
| [int32\_t (\*removeChild)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child)](#removechild) | Removes a component from its parent node. |
| [int32\_t (\*insertChildAfter)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child, ArkUI\_NodeHandle sibling)](#insertchildafter) | Attaches a component to a parent node, with the position after the **sibling** node. |
| [int32\_t (\*insertChildBefore)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child, ArkUI\_NodeHandle sibling)](#insertchildbefore) | Attaches a component to a parent node, with the position before the **sibling** node. |
| [int32\_t (\*insertChildAt)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child, int32\_t position)](#insertchildat) | Attaches a component to a parent node, with the position specified by **position**. |
| [int32\_t (\*setAttribute)(ArkUI\_NodeHandle node, ArkUI\_NodeAttributeType attribute, const ArkUI\_AttributeItem\* item)](#setattribute) | Sets component attributes. |
| [const ArkUI\_AttributeItem\* (\*getAttribute)(ArkUI\_NodeHandle node, ArkUI\_NodeAttributeType attribute)](#getattribute) | Obtains attributes. The pointer returned by this API is an internal buffer pointer of the ArkUI framework. As such, you do not need to call **delete** to free the memory. However, the pointer must be used before this API is called next time. Otherwise, the pointer may be overwritten by other values. |
| [int32\_t (\*resetAttribute)(ArkUI\_NodeHandle node, ArkUI\_NodeAttributeType attribute)](#resetattribute) | Resets component attributes. |
| [int32\_t (\*registerNodeEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType, int32\_t targetId, void\* userData)](#registernodeevent) | Registers an event for the specified node. |
| [void (\*unregisterNodeEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType)](#unregisternodeevent) | Unregisters an event for the specified node. |
| [void (\*registerNodeEventReceiver)(void (\*eventReceiver)(ArkUI\_NodeEvent\* event))](#registernodeeventreceiver) | 
Registers a unified entry point for event callbacks. The ArkUI framework collects component events generated during processing and returns them through the registered **eventReceiver** API.

Repeated calls will override the previously registered API. Avoid directly saving pointers to **ArkUI\_NodeEvent** objects, as the data will be destroyed after the callback is complete.

To bind with a component instance, you can use the **addNodeEventReceiver** function.

 |
| [void (\*unregisterNodeEventReceiver)()](#unregisternodeeventreceiver) | Unregisters the unified entry point for event callbacks. |
| [void (\*markDirty)(ArkUI\_NodeHandle node, ArkUI\_NodeDirtyFlag dirtyFlag)](#markdirty) | Forcibly marks the current node for re-measurement, re-layout, or re-drawing. Regarding updates to system attributes, the ArkUI framework automatically marks nodes and re-executes measurement, layout, or drawing; you do not need to call this API actively. |
| [uint32\_t (\*getTotalChildCount)(ArkUI\_NodeHandle node)](#gettotalchildcount) | Obtains the number of child nodes. |
| [ArkUI\_NodeHandle (\*getChildAt)(ArkUI\_NodeHandle node, int32\_t position)](#getchildat) | Obtains a child node. |
| [ArkUI\_NodeHandle (\*getFirstChild)(ArkUI\_NodeHandle node)](#getfirstchild) | Obtains the first child node. |
| [ArkUI\_NodeHandle (\*getLastChild)(ArkUI\_NodeHandle node)](#getlastchild) | Obtains the last child node. |
| [ArkUI\_NodeHandle (\*getPreviousSibling)(ArkUI\_NodeHandle node)](#getprevioussibling) | Obtains the previous sibling node. |
| [ArkUI\_NodeHandle (\*getNextSibling)(ArkUI\_NodeHandle node)](#getnextsibling) | Obtains the next sibling node. |
| [int32\_t (\*registerNodeCustomEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeCustomEventType eventType, int32\_t targetId, void\* userData)](#registernodecustomevent) | Registers a custom event for a node. Triggered events are returned through the custom event entry point function registered using **registerNodeCustomEventReceiver**. |
| [void (\*unregisterNodeCustomEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeCustomEventType eventType)](#unregisternodecustomevent) | Unregisters a custom event for a node. |
| [void (\*registerNodeCustomEventReceiver)(void (\*eventReceiver)(ArkUI\_NodeCustomEvent\* event))](#registernodecustomeventreceiver) | 

Registers a unified entry point for custom node event callbacks. The ArkUI framework collects custom component events generated during processing and returns them through the custom event entry point function registered using **registerNodeCustomEventReceiver**.

Repeated calls will override the previously registered API.

Do not directly save the **ArkUI\_NodeCustomEvent** object pointer. The data will be destroyed after the callback is complete.

To bind with a component instance, you can use the **addNodeCustomEventReceiver** function.

 |
| [void (\*unregisterNodeCustomEventReceiver)()](#unregisternodecustomeventreceiver) | Unregisters the unified entry point function for custom node event callbacks. |
| [int32\_t (\*setMeasuredSize)(ArkUI\_NodeHandle node, int32\_t width, int32\_t height)](#setmeasuredsize) | Sets the width and height for a component after the measurement in the measurement callback function. |
| [int32\_t (\*setLayoutPosition)(ArkUI\_NodeHandle node, int32\_t positionX, int32\_t positionY)](#setlayoutposition) | Sets the position of a component in the layout callback function. |
| [ArkUI\_IntSize (\*getMeasuredSize)(ArkUI\_NodeHandle node)](#getmeasuredsize) | Obtains the width and height of a component after measurement. |
| [ArkUI\_IntOffset (\*getLayoutPosition)(ArkUI\_NodeHandle node)](#getlayoutposition) | Obtains the offset of a node relative to its parent node after component layout is completed. The unit is px. The offset is the result after the parent container lays out the node. Therefore, the **offset** attribute that takes effect after the layout and the **position** attribute that does not participate in the layout do not affect the offset value. |
| [int32\_t (\*measureNode)(ArkUI\_NodeHandle node, ArkUI\_LayoutConstraint\* Constraint)](#measurenode) | Measures a node. You can use the **getMeasuredSize** API to obtain the size after the measurement. |
| [int32\_t (\*layoutNode)(ArkUI\_NodeHandle node, int32\_t positionX, int32\_t positionY)](#layoutnode) | Lays outs a node and specifies the expected position of the node relative to its parent node. |
| [int32\_t (\*addNodeEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeEvent\* event))](#addnodeeventreceiver) | 

Adds a component event callback function to a component to receive component events generated by it. Unlike the global registration function **registerNodeEventReceiver**, this API allows multiple event receivers to be added to the same component.

The callback added by this function is triggered before the global callback registered by **registerNodeEventReceiver**.

Avoid directly saving pointers to **ArkUI\_NodeEvent** objects, as the data will be destroyed after the callback is complete.

 |
| [int32\_t (\*removeNodeEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeEvent\* event))](#removenodeeventreceiver) | Removes a registered component event callback function from a component. |
| [int32\_t (\*addNodeCustomEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeCustomEvent\* event))](#addnodecustomeventreceiver) | 

Adds a custom event callback function to a component to receive custom events (such as layout and drawing events) generated by it. Unlike the global registration function **registerNodeCustomEventReceiver**, this API allows multiple event receivers to be added to the same component.

The callback added by this function is triggered before the global callback registered by **registerNodeCustomEventReceiver**.

Do not directly save the **ArkUI\_NodeCustomEvent** object pointer. The data will be destroyed after the callback is complete.

 |
| [int32\_t (\*removeNodeCustomEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeCustomEvent\* event))](#removenodecustomeventreceiver) | Removes a registered custom event callback function from a component. |
| [int32\_t (\*setUserData)(ArkUI\_NodeHandle node, void\* userData)](#setuserdata) | Saves custom data on a component. |
| [void\* (\*getUserData)(ArkUI\_NodeHandle node)](#getuserdata) | Obtains the custom data stored on a component. |
| [int32\_t (\*setLengthMetricUnit)(ArkUI\_NodeHandle node, ArkUI\_LengthMetricUnit unit)](#setlengthmetricunit) | Sets the unit of measurement for a component. |
| [ArkUI\_NodeHandle (\*getParent)(ArkUI\_NodeHandle node)](#getparent) | Obtains the parent node. |
| [int32\_t (\*removeAllChildren)(ArkUI\_NodeHandle parent)](#removeallchildren) | Removes all child nodes from the parent component. |

#### Member Function Description

#### \[h2\]createNode()

ArkUI\_NodeHandle (\*createNode)(ArkUI\_NodeType type)

**Description**

Creates a component based on [ArkUI\_NodeType](../../header-files/native-node-h/document.md#arkui_nodetype) and returns the pointer to the component object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeType](../../header-files/native-node-h/document.md#arkui_nodetype) type | Type of the component to create. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) | Pointer to the created component. If the component fails to be created, **NULL** is returned. You need to manage the lifecycle of the returned component object pointer. Otherwise, issues such as Use After Free may cause process crashes or memory leaks. |

#### \[h2\]disposeNode()

void (\*disposeNode)(ArkUI\_NodeHandle node)

**Description**

Disposes of the component to which the specified pointer points. When calling this API on a non-main thread, special attention must be paid to the lifecycle of the component object to be destroyed. Improper lifecycle management may cause the application to crash; therefore, it is not recommended to call this API on non-main threads.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Pointer to a component object. |

#### \[h2\]addChild()

int32\_t (\*addChild)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child)

**Description**

Attaches a component to a parent node. This API is used for node operations, and you are advised to call this API in the main thread.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) parent | Pointer to the parent node. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) child | Pointer to the child node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the node has been adopted as an affiliated node. This specification is supported since API version 22.

 |

#### \[h2\]removeChild()

int32\_t (\*removeChild)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child)

**Description**

Removes a component from its parent node. This API is used for node operations, and you are advised to call this API in the main thread.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) parent | Pointer to the parent node. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) child | Pointer to the child node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

 |

#### \[h2\]insertChildAfter()

int32\_t (\*insertChildAfter)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child, ArkUI\_NodeHandle sibling)

**Description**

Attaches a component to a parent node, with the position after the **sibling** node. This API is used for node operations, and you are advised to call this API in the main thread.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) parent | Pointer to the parent node. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) child | Pointer to the child node. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) sibling | Pointer to the sibling node after which the target node is to be inserted. If the value is null, the node is inserted at the end of the parent node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the node has been adopted as an affiliated node. This specification is supported since API version 22.

 |

#### \[h2\]insertChildBefore()

int32\_t (\*insertChildBefore)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child, ArkUI\_NodeHandle sibling)

**Description**

Attaches a component to a parent node, with the position before the **sibling** node. This API is used for node operations, and you are advised to call this API in the main thread.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) parent | Pointer to the parent node. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) child | Pointer to the child node. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) sibling | Pointer to the sibling node before which the target node is to be inserted. If the value is null, the node is inserted at the end of the parent node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the node has been adopted as an affiliated node. This specification is supported since API version 22.

 |

#### \[h2\]insertChildAt()

int32\_t (\*insertChildAt)(ArkUI\_NodeHandle parent, ArkUI\_NodeHandle child, int32\_t position)

**Description**

Attaches a component to a parent node, with the position specified by **position**. This API is used for node operations, and you are advised to call this API in the main thread.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) parent | Pointer to the parent node. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) child | Pointer to the child node. |
| int32\_t position | Inserting position. The value range is \[-2147483648, 2147483647\]. If the value is a negative number or invalid, the component is inserted at the end of the parent node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

Returns [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the node has been adopted as an affiliated node. This specification is supported since API version 22.

 |

#### \[h2\]setAttribute()

int32\_t (\*setAttribute)(ArkUI\_NodeHandle node, ArkUI\_NodeAttributeType attribute, const ArkUI\_AttributeItem\* item)

**Description**

Sets attributes. You are advised to call this API in the main thread.

In actual service scenarios, if the attributes set for a component contain the heap memory you apply for, ensure that the component is no longer used before calling the corresponding release API. For example, **NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING** in [ArkUI\_NodeAttributeType](../../header-files/native-node-h/document.md#arkui_nodeattributetype).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Node whose attribute needs to be set. |
| [ArkUI\_NodeAttributeType](../../header-files/native-node-h/document.md#arkui_nodeattributetype) attribute | Type of attribute to set. |
| const [ArkUI\_AttributeItem](../arkui-attributeitem/document.md)\* item | Attribute value to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the attribute is not supported.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

Returns [ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_EXIST](../../header-files/native-type-h/document.md#arkui_errorcode) if **NodeAdapter** already exists.

 |

#### \[h2\]getAttribute()

const ArkUI\_AttributeItem\* (\*getAttribute)(ArkUI\_NodeHandle node, ArkUI\_NodeAttributeType attribute)

**Description**

Obtains attributes. The pointer returned by this API is an internal buffer pointer of the ArkUI framework. As such, you do not need to call **delete** to free the memory. However, the pointer must be used before this API is called next time. Otherwise, the pointer may be overwritten by other values.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Node whose attribute needs to be obtained. |
| [ArkUI\_NodeAttributeType](../../header-files/native-node-h/document.md#arkui_nodeattributetype) attribute | Type of the attribute to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| const [ArkUI\_AttributeItem](../arkui-attributeitem/document.md)\* | Attribute value. If the operation fails, a null pointer is returned. |

#### \[h2\]resetAttribute()

int32\_t (\*resetAttribute)(ArkUI\_NodeHandle node, ArkUI\_NodeAttributeType attribute)

**Description**

Resets attributes. You are advised to call this API in the main thread.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Node whose attribute needs to be reset. |
| [ArkUI\_NodeAttributeType](../../header-files/native-node-h/document.md#arkui_nodeattributetype) attribute | Type of the attribute to reset. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the attribute is not supported.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

 |

#### \[h2\]registerNodeEvent()

int32\_t (\*registerNodeEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType, int32\_t targetId, void\* userData)

**Description**

Registers an event for the specified node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_NodeEventType](../../header-files/native-node-h/document.md#arkui_nodeeventtype) eventType | Type of the event to register. |
| int32\_t targetId | Custom event ID, which is passed in the callback of [ArkUI\_NodeEvent](../arkui-nodeevent/document.md) when the event is triggered. |
| void\* userData | Custom event parameter, which is passed in the callback of [ArkUI\_NodeEvent](../arkui-nodeevent/document.md) when the event is triggered. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the event is not supported.

Returns [ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is not supported for the node created in ArkTS.

 |

#### \[h2\]unregisterNodeEvent()

void (\*unregisterNodeEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType)

**Description**

Unregisters an event for the specified node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_NodeEventType](../../header-files/native-node-h/document.md#arkui_nodeeventtype) eventType | Type of the event to unregister. |

#### \[h2\]registerNodeEventReceiver()

void (\*registerNodeEventReceiver)(void (\*eventReceiver)(ArkUI\_NodeEvent\* event))

**Description**

Registers a unified entry point for event callbacks. The ArkUI framework collects component events generated during processing and returns them through the registered **eventReceiver** API.

Repeated calls will override the previously registered API. Do not directly save the pointer to the [ArkUI\_NodeEvent](../arkui-nodeevent/document.md) object. The data will be destroyed after the callback is complete.

To bind with a component instance, you can use the [addNodeEventReceiver](#addnodeeventreceiver) API.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void (\*eventReceiver)([ArkUI\_NodeEvent](../arkui-nodeevent/document.md)\* event) | Unified entry point for event callbacks to register. |

#### \[h2\]unregisterNodeEventReceiver()

void (\*unregisterNodeEventReceiver)()

**Description**

Unregisters the unified entry point for event callbacks.

**Since**: 12

#### \[h2\]markDirty()

void (\*markDirty)(ArkUI\_NodeHandle node, ArkUI\_NodeDirtyFlag dirtyFlag)

**Description**

Forcibly marks the current node for re-measurement, re-layout, or re-drawing. Regarding updates to system attributes, the ArkUI framework automatically marks nodes and re-executes measurement, layout, or drawing; you do not need to call this API actively.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Node object that needs to be marked for re-measurement, re-layout, or re-drawing. |
| [ArkUI\_NodeDirtyFlag](../../header-files/native-node-h/document.md#arkui_nodedirtyflag) dirtyFlag | Type for re-measurement, re-layout, or re-drawing. |

#### \[h2\]getTotalChildCount()

uint32\_t (\*getTotalChildCount)(ArkUI\_NodeHandle node)

**Description**

Obtains the number of child nodes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns the number of child nodes; returns **0** if there is no child node. |

#### \[h2\]getChildAt()

ArkUI\_NodeHandle (\*getChildAt)(ArkUI\_NodeHandle node, int32\_t position)

**Description**

Obtains a child node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| int32\_t position | Position of the child node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) | Pointer to the node, or **NULL** if the node is not found. |

#### \[h2\]getFirstChild()

ArkUI\_NodeHandle (\*getFirstChild)(ArkUI\_NodeHandle node)

**Description**

Obtains the first child node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) | Pointer to the node, or **NULL** if the node is not found. |

#### \[h2\]getLastChild()

ArkUI\_NodeHandle (\*getLastChild)(ArkUI\_NodeHandle node)

**Description**

Obtains the last child node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) | Pointer to the node, or **NULL** if the node is not found. |

#### \[h2\]getPreviousSibling()

ArkUI\_NodeHandle (\*getPreviousSibling)(ArkUI\_NodeHandle node)

**Description**

Obtains the previous sibling node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) | Pointer to the node, or **NULL** if the node is not found. |

#### \[h2\]getNextSibling()

ArkUI\_NodeHandle (\*getNextSibling)(ArkUI\_NodeHandle node)

**Description**

Obtains the next sibling node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) | Pointer to the node, or **NULL** if the node is not found. |

#### \[h2\]registerNodeCustomEvent()

int32\_t (\*registerNodeCustomEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeCustomEventType eventType, int32\_t targetId, void\* userData)

**Description**

Registers a custom event for a node. Triggered events are returned through the custom event entry point function registered using **registerNodeCustomEventReceiver**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_NodeCustomEventType](../../header-files/native-node-h/document.md#arkui_nodecustomeventtype) eventType | Type of the event to register. |
| int32\_t targetId | Custom event ID, which is passed in the callback of [ArkUI\_NodeCustomEvent](../arkui-nodecustomevent/document.md) when the event is triggered. |
| void\* userData | Custom event parameter, which is passed in the callback of [ArkUI\_NodeCustomEvent](../arkui-nodecustomevent/document.md) when the event is triggered. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED](../../header-files/native-type-h/document.md#arkui_errorcode) if the event is not supported.

 |

#### \[h2\]unregisterNodeCustomEvent()

void (\*unregisterNodeCustomEvent)(ArkUI\_NodeHandle node, ArkUI\_NodeCustomEventType eventType)

**Description**

Unregisters a custom event for a node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_NodeCustomEventType](../../header-files/native-node-h/document.md#arkui_nodecustomeventtype) eventType | Type of the event to unregister. |

#### \[h2\]registerNodeCustomEventReceiver()

void (\*registerNodeCustomEventReceiver)(void (\*eventReceiver)(ArkUI\_NodeCustomEvent\* event))

**Description**

Registers a unified entry point for custom node event callbacks. The ArkUI framework collects custom component events generated during processing and returns them through the custom event entry point function registered using **registerNodeCustomEventReceiver**.

Repeated calls will override the previously registered API.

Do not directly save the pointer to the [ArkUI\_NodeCustomEvent](../arkui-nodecustomevent/document.md) object. The data will be destroyed after the callback is complete.

To bind with a component instance, you can use the **addNodeCustomEventReceiver** function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void (\*eventReceiver)([ArkUI\_NodeCustomEvent](../arkui-nodecustomevent/document.md)\* event) | Unified entry point for event callbacks to register. |

#### \[h2\]unregisterNodeCustomEventReceiver()

void (\*unregisterNodeCustomEventReceiver)()

**Description**

Unregisters the unified entry point function for custom node event callbacks.

**Since**: 12

#### \[h2\]setMeasuredSize()

int32\_t (\*setMeasuredSize)(ArkUI\_NodeHandle node, int32\_t width, int32\_t height)

**Description**

Sets the width and height for a component after the measurement in the measurement callback function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| int32\_t width | Width to set. |
| int32\_t height | Height to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setLayoutPosition()

int32\_t (\*setLayoutPosition)(ArkUI\_NodeHandle node, int32\_t positionX, int32\_t positionY)

**Description**

Sets the position of a component in the layout callback function. This API has a lower priority than [NODE\_POSITION](../../header-files/native-type-h/document.md#enums).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| int32\_t positionX | X-coordinate. |
| int32\_t positionY | Y-coordinate. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]getMeasuredSize()

ArkUI\_IntSize (\*getMeasuredSize)(ArkUI\_NodeHandle node)

**Description**

Obtains the width and height of a component after measurement.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_IntSize](../arkui-intsize/document.md) | Width and height of the component, wrapped in an **ArkUI\_IntSize** structure. |

#### \[h2\]getLayoutPosition()

ArkUI\_IntOffset (\*getLayoutPosition)(ArkUI\_NodeHandle node)

**Description**

Obtains the offset of a node relative to its parent node after component layout is completed. The unit is px. The offset is the result after the parent container lays out the node. Therefore, the **offset** attribute that takes effect after the layout and the **position** attribute that does not participate in the layout do not affect the offset value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_IntOffset](../arkui-intoffset/document.md) | Position of the component, wrapped in an **ArkUI\_IntOffset** structure. |

#### \[h2\]measureNode()

int32\_t (\*measureNode)(ArkUI\_NodeHandle node, ArkUI\_LayoutConstraint\* Constraint)

**Description**

Measures a node. You can use the **getMeasuredSize** API to obtain the size after the measurement.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| [ArkUI\_LayoutConstraint](../arkui-layoutconstraint/document.md)\* Constraint | Size constraint. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]layoutNode()

int32\_t (\*layoutNode)(ArkUI\_NodeHandle node, int32\_t positionX, int32\_t positionY)

**Description**

Lays outs a node and specifies the expected position of the node relative to its parent node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |
| int32\_t positionX | X-coordinate. |
| int32\_t positionY | Y-coordinate. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]addNodeEventReceiver()

int32\_t (\*addNodeEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeEvent\* event))

**Description**

Adds a component event callback function to a component to receive component events generated by it. Unlike the global registration function **registerNodeEventReceiver**, this API allows multiple event receivers to be added to the same component.

The callback added by this function is triggered before the global callback registered by **registerNodeEventReceiver**.

Do not directly save the pointer to the [ArkUI\_NodeEvent](../arkui-nodeevent/document.md) object. The data will be destroyed after the callback is complete.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Component for which you want to add the event callback function. |
| void (\*eventReceiver)([ArkUI\_NodeEvent](../arkui-nodeevent/document.md)\* event) | Event callback for the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]removeNodeEventReceiver()

int32\_t (\*removeNodeEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeEvent\* event))

**Description**

Removes a registered component event callback function from a component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Component for which you want to remove the event callback function. |
| void (eventReceiver)([ArkUI\_NodeEvent](../arkui-nodeevent/document.md) event) | Component event callback function to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]addNodeCustomEventReceiver()

int32\_t (\*addNodeCustomEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeCustomEvent\* event))

**Description**

Adds a custom event callback function to a component to receive custom events (such as layout and drawing events) generated by it. Unlike the global registration function **registerNodeCustomEventReceiver**, this API allows multiple event receivers to be added to the same component.

The callback added by this function is triggered before the global callback registered by **registerNodeCustomEventReceiver**.

Do not directly save the pointer to the [ArkUI\_NodeCustomEvent](../arkui-nodecustomevent/document.md) object. The data will be destroyed after the callback is complete.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Component for which you want to add the custom event callback function. |
| void (\*eventReceiver)([ArkUI\_NodeCustomEvent](../arkui-nodecustomevent/document.md)\* event) | Custom event callback for the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]removeNodeCustomEventReceiver()

int32\_t (\*removeNodeCustomEventReceiver)(ArkUI\_NodeHandle node, void (\*eventReceiver)(ArkUI\_NodeCustomEvent\* event))

**Description**

Removes a registered custom event callback function from a component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Component for which you want to remove the custom event callback function. |
| void (\*eventReceiver)([ArkUI\_NodeCustomEvent](../arkui-nodecustomevent/document.md)\* event) | Custom event callback function to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setUserData()

int32\_t (\*setUserData)(ArkUI\_NodeHandle node, void\* userData)

**Description**

Saves custom data on a component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Component on which the custom data will be saved. |
| void\* userData | Custom data to be saved. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]getUserData()

void\* (\*getUserData)(ArkUI\_NodeHandle node)

**Description**

Obtains the custom data stored on a component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | Custom data. |

#### \[h2\]setLengthMetricUnit()

int32\_t (\*setLengthMetricUnit)(ArkUI\_NodeHandle node, ArkUI\_LengthMetricUnit unit)

**Description**

Sets the unit of measurement for a component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Component for which you want to set the unit. |
| [ArkUI\_LengthMetricUnit](../../header-files/native-type-h/document.md#arkui_lengthmetricunit) unit | Unit type [ArkUI\_LengthMetricUnit](../../header-files/native-type-h/document.md#arkui_lengthmetricunit). The default value is **ARKUI\_LENGTH\_METRIC\_UNIT\_DEFAULT**. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]getParent()

ArkUI\_NodeHandle (\*getParent)(ArkUI\_NodeHandle node)

**Description**

Obtains the parent node.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) | Pointer to the node, or **NULL** if the node is not found. |

#### \[h2\]removeAllChildren()

int32\_t (\*removeAllChildren)(ArkUI\_NodeHandle parent)

**Description**

Removes all child nodes from the parent component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) parent | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
