# Parallelizing UI Page Building Using Multi-threaded NDK APIs

#### Overview

In versions earlier than API version 22, UI component creation and attribute setting must be performed in the application's UI thread. This means that when using NDK APIs, you must submit component creation and attribute setting tasks to the UI thread for execution. This limits both the flexibility of component creation and application performance.

As application functionality grows increasingly complex, numerous UI components need to be dynamically created on application pages. Executing all these component creation tasks in a single UI thread leads to slow application startup, animation frame drops, and page freezes, directly impacting user experience.

To address these issues, multi-threaded support has been introduced to NDK APIs starting from API version 22. This enhancement provides the following benefits:

-   **Simplified calling process**: You no longer need to switch threads or submit component creation tasks through task queues. Instead, you can directly call APIs for creating components and setting attributes from any thread, reducing thread context switches and simplifying interaction logic between the UI framework and the application.
    
-   **Optimized performance and experience**: Component creation and attribute setting APIs can be called concurrently across multiple threads, fully utilizing the device's multi-core CPU and reducing overall page creation time. The UI thread can then focus on animation rendering and user input, ensuring smooth UI interactions.
    
-   **Enhanced flexibility for future expansion**: The capability to call component creation and attribute setting APIs from multiple threads not only resolves current performance bottlenecks but also provides room for developing more complex and demanding UI pages in the future, allowing for greater design flexibility.
    

In summary, multi-threaded NDK APIs deliver a high-performance UI page creation experience in complex service scenarios.

#### Using Multi-threaded NDK APIs

-   Before using multi-threaded NDK APIs, it is recommended that you read the [NDK API overview](../ndk-based-ui-development-overview/document.md) document to master the basic concepts and foundational knowledge required for using NDK APIs.
    
-   To minimize adaptation costs, the method for obtaining and using multi-threaded NDK APIs remains the same as existing NDK APIs. Simply call the [OH\_ArkUI\_GetModuleInterface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface) API with [ARKUI\_MULTI\_THREAD\_NATIVE\_NODE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#arkui_nativeapivariantkind) as the input parameter to obtain the multi-threaded NDK API set. Example:
    
    ArkUI\_NativeNodeAPI\_1 \*multiThreadNodeAPI = nullptr;
    // Obtain the multi-threaded NDK API set.
    OH\_ArkUI\_GetModuleInterface(ARKUI\_MULTI\_THREAD\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, multiThreadNodeAPI);
    
    if (!multiThreadNodeAPI) {
      return;
    }
    // Call the multi-threaded createNode API in the set to create a UI component.
    auto node = multiThreadNodeAPI->createNode(ARKUI\_NODE\_COLUMN);
    

For the complete list of NDK APIs supporting multi-threading, see [Multi-threaded NDK API Set Specifications](#multi-threaded-ndk-api-set-specifications).

You can use the multi-thread NDK API to create a UI component and set its attributes in any thread. However, the UI component must be mounted to the main UI tree in the UI thread. The following APIs can be used to dispatch and execute multi-thread UI component creation tasks.

-   For tasks that can be executed in non-UI threads (such as component creation and attribute setting), use the OH\_ArkUI\_PostAsyncUITask API to schedule them to the system thread pool, and then submit the component mounting task to the UI thread for execution.
    
-   When creating UI components in custom non-UI threads, use the OH\_ArkUI\_PostUITask API to submit the component mounting task to the UI thread.
    
-   When executing UI-thread-only tasks during multi-threaded UI component creation, use the [OH\_ArkUI\_PostUITaskAndWait](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_postuitaskandwait) API to submit the task to the UI thread. Note that this API may block the calling thread if the UI thread is heavily loaded, potentially affecting multi-threading performance gains. Use this API sparingly.
    

#### Multi-threaded NDK API Adaptation

1.  Multi-threaded NDK APIs are suitable for high-load, performance-sensitive scenarios like page navigation and list scrolling, where UI thread component creation tasks take milliseconds to tens of milliseconds. Split these tasks into subtasks and distribute them across multiple threads for concurrent execution to reduce UI thread load and improve page startup and update smoothness.
    
2.  When creating UI components in your own threads, it is recommended that you limit concurrent threads to no more than four, based on the device's CPU core count, to avoid thread scheduling overhead.
    
3.  Pre-create common component trees in non-UI threads to enhance user experience in performance-sensitive scenarios.
    

#### Multi-threaded NDK API Calling Specifications

UI components are classified into two states: free and attached.

UI components created using the multi-threaded [createNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#createnode) API are in the free state by default and can transition between the free and attached states. UI components created using other methods are initially in the attached state and this state is immutable.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/pVOxwyvGTXyc-KS-p-vQJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0CB8052D833F6F0F384275CA975D807A809AD4A4316FCD4BBF0B40A06E1CF5B)

-   You can use multi-threaded NDK APIs to operate free components in any thread. To ensure normal application functions and thread safety, the following usage constraints must be observed:
    
    -   Do not operate the same free component or component tree in multiple threads at the same time. A free component is lock-free, and stability issues may occur if multiple threads access this component at the same time.
    -   Do not use any NDK APIs other than the APIs from [Multi-threaded NDK API Set Specifications](#multi-threaded-ndk-api-set-specifications) to operate a free component. You must first change the component to the attached state before using NDK APIs in the UI thread. Otherwise, the APIs will function abnormally.
-   To balance performance, the framework side does not perform runtime checks for the above constraints; you must ensure compliance.
    
-   To ensure multi-threaded safety of APIs, some attributes of a free component cannot be read immediately by calling [getAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getattribute) after being set by calling [setAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute). You need to change the component to the attached state before reading the correct attribute values.
    

The UI component state changes from free to attached after the following operations are performed:

-   After the multi-threaded [markDirty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#markdirty), [measureNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#measurenode), or [layoutNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#layoutnode) API is called to mark, measure, or lay out a free component, all other free components in the same component tree are changed to the attached state.
-   After a multi-threaded [component tree operation](#component-tree-operations) API is called to mount a free component as a child component of an attached component, all other free components in the same component tree are changed to the attached state.
-   After a multi-threaded API for [operating a component tree](#component-tree-operations) is called to mount an attached component as a child component of a free component, all other free components in the same component tree are changed to the attached state.

The UI component state changes from attached to free after the following operations are performed:

-   A component is removed from the component tree by using the multi-threaded [component tree operation](#component-tree-operations) API, and this component tree does not contain any attached component whose state cannot be changed. In this case, all components in the component tree are changed to the free state.

According to the preceding state transition rules, all components in each UI component tree are in the same state.

#### Errors and Exceptions of Multi-threaded NDK APIs

For multi-thread NDK API calling specifications, see [Multi-threaded NDK API Set Specifications](#multi-threaded-ndk-api-set-specifications). When calling multi-threaded NDK APIs, you must check the return values. The APIs return the error code [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) in the following situations:

-   An API that does not support multi-threaded operations is called in a non-UI thread.
    
-   A multi-threaded NDK API is called in a non-UI thread to operate an attached component.
    

For common issues during multi-threaded NDK adaptation, see [FAQs About UI Parallelization](../../ui-debugging-and-optimization/ui-development-faqs/faqs-about-ui-parallelization/document.md).

#### Multi-threaded NDK API Set Specifications

The following APIs support multi-threaded calls: [component creation and destruction](#component-creation-and-destruction), [component attribute read/write](#component-attribute-readwrite), [component event registration and deregistration](#component-event-registration-and-deregistration), [component tree operations](#component-tree-operations), and [custom component data read/write](#custom-component-data-readwrite).

The following APIs are UI-thread only: [global event registration and deregistration](#global-event-registration-and-deregistration) and [component measurement and layout](#component-measurement-and-layout).

## Component Creation and Destruction

| API | Description | Non-UI Thread | Multi-thread Specifications |
| :-- | :-- | :-- | :-- |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)(\* [createNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#createnode) )([ArkUI\_NodeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodetype) type) | Creates a free node based on [ArkUI\_NodeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodetype) and returns the free node object pointer. | Supported | Callable from any thread. |
| void(\* [disposeNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#disposenode) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Destroys the node object to which the node pointer points. | Supported | Ineffective if called from a non-UI thread on an attached node. |

## Component Attribute Read/Write

| API | Description | Non-UI Thread | Multi-thread Specifications |
| :-- | :-- | :-- | :-- |
| int32\_t(\* [setAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) attribute, const [ArkUI\_AttributeItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem) \*item) | Sets node attributes. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| const [ArkUI\_AttributeItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem) \*(\* [getAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getattribute) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) attribute) | Obtains node attributes. | Supported | Returns a null pointer if called from a non-UI thread on an attached node. |
| int32\_t(\* [resetAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#resetattribute) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) attribute) | Resets node attributes to default values. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [setLengthMetricUnit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setlengthmetricunit) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_LengthMetricUnit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_lengthmetricunit) unit) | Sets the node unit. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |

## Component Event Registration and Deregistration

| API | Description | Non-UI Thread | Multi-thread Specifications |
| :-- | :-- | :-- | :-- |
| int32\_t(\* [registerNodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) eventType, int32\_t targetId, void \*userData) | Registers an event with a node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| void(\* [unregisterNodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#unregisternodeevent) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) eventType) | Unregisters an event from a node. | Supported | Ineffective if called from a non-UI thread on an attached node. |
| int32\_t(\* [registerNodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodecustomevent) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeCustomEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodecustomeventtype) eventType, int32\_t targetId, void \*userData) | Registers a custom event with a node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| void(\* [unregisterNodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#unregisternodecustomevent) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeCustomEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodecustomeventtype) eventType) | Deregisters a custom event from a node. | Supported | Ineffective if called from a non-UI thread on an attached node. |
| int32\_t(\* [addNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodeeventreceiver) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, void(\*eventReceiver)([ArkUI\_NodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeevent) \*event)) | Registers an event callback function with a node to receive component events generated by the component. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [removeNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removenodeeventreceiver) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, void(\*eventReceiver)([ArkUI\_NodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeevent) \*event)) | Removes the event callback function registered on a node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [addNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodecustomeventreceiver) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, void(\*eventReceiver)([ArkUI\_NodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecustomevent) \*event)) | Registers a custom event callback function with a node to receive custom events (such as layout events and drawing events) generated by the component. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [removeNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removenodecustomeventreceiver) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, void(\*eventReceiver)([ArkUI\_NodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecustomevent) \*event)) | Removes the custom event callback function registered on a node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |

## Component Tree Operations

| API | Description | Non-UI Thread | Multi-thread Specifications |
| :-- | :-- | :-- | :-- |
| int32\_t(\* [addChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addchild) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) parent, [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) child) | Adds a child node to the child node list of a parent node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [removeChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removechild) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) parent, [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) child) | Removes a child node from the child node list of a parent node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [insertChildAfter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#insertchildafter) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) parent, [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) child, [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) sibling) | Inserts a child node after a sibling node in the child node list of a parent node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [insertChildBefore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#insertchildbefore) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) parent, [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) child, [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) sibling) | Inserts a child node before a sibling node in the child node list of a parent node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [insertChildAt](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#insertchildat) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) parent, [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) child, int32\_t position) | Inserts a child node at the specified position in the child node list of a parent node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)(\* [getParent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getparent) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the parent node of a node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| int32\_t(\* [removeAllChildren](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removeallchildren) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) parent) | Removes all child nodes of a node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| uint32\_t(\* [getTotalChildCount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#gettotalchildcount) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the number of child nodes of a node. | Supported | Returns **0** if called from a non-UI thread on an attached node. |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)(\* [getChildAt](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getchildat) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, int32\_t position) | Obtains the pointer to the child node at the specified position. | Supported | Returns a null pointer if called from a non-UI thread on an attached node. |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)(\* [getFirstChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getfirstchild) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the pointer to the first child node of a node. | Supported | Returns a null pointer if called from a non-UI thread on an attached node. |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)(\* [getLastChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getlastchild) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the pointer to the last child node of a node. | Supported | Returns a null pointer if called from a non-UI thread on an attached node. |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)(\* [getPreviousSibling](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getprevioussibling) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the pointer to the previous sibling node of a node. | Supported | Returns a null pointer if called from a non-UI thread on an attached node. |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)(\* [getNextSibling](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getnextsibling) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the pointer to the next sibling node of a node. | Supported | Returns a null pointer if called from a non-UI thread on an attached node. |

## Custom Component Data Read/Write

| API | Description | Non-UI Thread | Multi-thread Specifications |
| :-- | :-- | :-- | :-- |
| int32\_t(\* [setUserData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setuserdata) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, void \*userData) | Sets node data for a node. | Supported | Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if any attempt is made to operate an attached node from a non-UI thread. |
| void \*(\* [getUserData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getuserdata) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the custom data stored on a node. | Supported | Returns a null pointer if called from a non-UI thread on an attached node. |

## Global Event Registration and Deregistration

| API | Description | Non-UI Thread | Multi-thread Specifications |
| :-- | :-- | :-- | :-- |
| void(\* [registerNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeeventreceiver) )(void(\*eventReceiver)([ArkUI\_NodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeevent) \*event)) | Registers a unified entry point for node event callbacks. | Not supported | UI thread only. |
| void(\* [unregisterNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#unregisternodeeventreceiver) )() | Unregisters the unified entry point for node event callbacks. | Not supported | UI thread only. |
| void(\* [registerNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodecustomeventreceiver) )(void(\*eventReceiver)([ArkUI\_NodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecustomevent) \*event)) | Registers a unified entry point for custom node event callbacks. | Not supported | UI thread only. |
| void(\* [unregisterNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#unregisternodecustomeventreceiver) )() | Unregisters the unified entry point for custom node event callbacks. | Not supported | UI thread only. |

## Component Measurement and Layout

| API | Description | Non-UI Thread | Multi-thread Specifications |
| :-- | :-- | :-- | :-- |
| int32\_t(\* [setMeasuredSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setmeasuredsize) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, int32\_t width, int32\_t height) | Sets the width and height for a component after the measurement in the measurement callback function. | Not supported | UI thread only. Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if called from a non-UI thread. |
| int32\_t(\* [setLayoutPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setlayoutposition) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, int32\_t positionX, int32\_t positionY) | Sets the position of a component in the layout callback function. | Not supported | UI thread only. Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if called from a non-UI thread. |
| [ArkUI\_IntSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intsize)(\* [getMeasuredSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getmeasuredsize) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the width and height of a node after measurement. | Not supported | UI thread only. Returns the default value if called from a non-UI thread. |
| [ArkUI\_IntOffset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intoffset)(\* [getLayoutPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getlayoutposition) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node) | Obtains the position of a node after the layout is complete. | Not supported | UI thread only. Returns the default value if called from a non-UI thread. |
| int32\_t(\* [measureNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#measurenode) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_LayoutConstraint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-layoutconstraint) \*Constraint) | Measures a node. You can use the **getMeasuredSize** API to obtain the size after the measurement. The state of all free nodes in the component tree where the node is located is changed to attached. | Not supported | UI thread only. Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if called from a non-UI thread. |
| int32\_t(\* [layoutNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#layoutnode) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, int32\_t positionX, int32\_t positionY) | Lays out a node and specifies the expected position of the node relative to its parent. The state of all free nodes in the component tree where the node is located is changed to attached. | Not supported | UI thread only. Returns [ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) if called from a non-UI thread. |
| void(\* [markDirty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#markdirty) )([ArkUI\_NodeHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) node, [ArkUI\_NodeDirtyFlag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodedirtyflag) dirtyFlag) | Forces the node to be marked for re-measurement, re-layout, or redrawing. The state of all free nodes in the component tree where the node is located is changed to attached. | Not supported | UI thread only. |

#### Example

This example demonstrates how to create buttons in non-UI threads.

Click **CreateNodeTree** to create **Button** components concurrently across multiple non-UI threads, and then mount them to the main UI tree in the UI thread for display. Click **DisposeNodeTree** to unmount and destroy the created components, clearing the page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/7P4JXeW2TXWviTRyYQ7H2Q/en-us_image_0000002537764894.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BDA6236AFD582060A6279148E420CA2F56766ED7C0441313419C083098E6897)

The example shows how to obtain and use multi-threaded NDK APIs, and utilize [OH\_ArkUI\_PostAsyncUITask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_postasyncuitask), [OH\_ArkUI\_PostUITask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_postuitask), and [OH\_ArkUI\_PostUITaskAndWait](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_postuitaskandwait) to distribute component creation and attribute setting tasks across multiple threads.

To simplify programming, **ArkUI\_NodeHandle** is encapsulated as an ArkUINode object on the native side using object-oriented principles, following the [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md) guide.

// index.ets
import { NodeContent } from '@kit.ArkUI';
import entry from 'libentry.so';

@Component
struct CAPIComponent {
  private rootSlot = new NodeContent();

  aboutToAppear(): void {
    // Create native components in multiple threads before page display.
    entry.createNodeTreeOnMultiThread(this.rootSlot, this.getUIContext());
  }

  aboutToDisappear(): void {
    // Release created native components before page destruction.
    entry.disposeNodeTreeOnMultiThread(this.rootSlot);
  }

  build() {
    Column() {
      // Native component mount point.
      ContentSlot(this.rootSlot)
    }
  }
}

@Entry
@Component
struct Index {
  @State isShow: boolean = false;
  @State message: string = "CreateNodeTree";

  build() {
    Flex() {
      Column() {
        Text('CreateNodeTreeOnMultiThread')
          .fontSize(18)
          .fontWeight(FontWeight.Bold)
        Button(this.message)
          .onClick(() => {
            this.isShow = !this.isShow;
            if (this.isShow) {
              this.message = "DisposeNodeTree"
            } else {
              this.message = "CreateNodeTree"
            }
          })
        if (this.isShow) {
          CAPIComponent()
        }
      }.width('100%')
    }.width('100%')
  }
}

// index.d.ts
// entry/src/main/cpp/types/libentry/Index.d.ts
export const createNativeRoot: (content: Object) => void;
export const destroyNativeRoot: () => void;
export const createNodeTreeOnMultiThread: (content1: Object, content2: Object) => void;
export const disposeNodeTreeOnMultiThread: (content1: Object) => void;

\# CMakeLists.txt
# the minimum version of CMake.
cmake\_minimum\_required(VERSION 3.5.0)
project(ndk\_build\_on\_multi\_thread)

set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})

if(DEFINED PACKAGE\_FIND\_FILE)
    include(${PACKAGE\_FIND\_FILE})
endif()

include\_directories(${NATIVERENDER\_ROOT\_PATH}
                    ${NATIVERENDER\_ROOT\_PATH}/include)

add\_library(entry SHARED napi\_init.cpp NativeEntry.cpp NativeModule.h ArkUIBaseNode.h ArkUINode.h ArkUIListNode.h ArkUIListItemNode.h ArkUITextNode.h NormalTextListExample.h CreateNode.h CreateNode.cpp)
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libace\_ndk.z.so libhilog\_ndk.z.so)

// NativeModule.h
#ifndef MYAPPLICATION\_NATIVEMODULE\_H
#define MYAPPLICATION\_NATIVEMODULE\_H

#include <arkui/native\_node.h>
#include <arkui/native\_interface.h>
#include <cassert>

namespace NativeModule {

class NativeModuleInstance {
public:
    static NativeModuleInstance \*GetInstance() {
        static NativeModuleInstance instance;
        return &instance;
    }

    NativeModuleInstance() {
        // Obtain the function pointer struct of the multi-threaded NDK API for subsequent operations.
        OH\_ArkUI\_GetModuleInterface(ARKUI\_MULTI\_THREAD\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, arkUINativeNodeApi\_);
        assert(arkUINativeNodeApi\_);
    }
    // Expose it for use by other modules.
    ArkUI\_NativeNodeAPI\_1 \*GetNativeNodeAPI() { return arkUINativeNodeApi\_; }

private:
    ArkUI\_NativeNodeAPI\_1 \*arkUINativeNodeApi\_ = nullptr;
};
} // namespace NativeModule

#endif // MYAPPLICATION\_NATIVEMODULE\_H

// CreateNode.h
#ifndef MYAPPLICATION\_CREATENODE\_H
#define MYAPPLICATION\_CREATENODE\_H

#include "ArkUINode.h"

#include <js\_native\_api.h>

namespace NativeModule {
// Encapsulate the Button component.
class ArkUIButtonNode: public ArkUINode {
public:
    ArkUIButtonNode() :
        ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI\_NODE\_BUTTON)) {}
    int32\_t SetLabel(ArkUI\_AttributeItem& label\_item) {
        return nativeModule\_->setAttribute(handle\_, NODE\_BUTTON\_LABEL, &label\_item);
    }
    int32\_t SetMargin(ArkUI\_AttributeItem& item) {
        return nativeModule\_->setAttribute(handle\_, NODE\_MARGIN, &item);
    }
};

// Encapsulate the Row component.
class ArkUIRowNode: public ArkUINode {
public:
    ArkUIRowNode() :
        ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI\_NODE\_ROW)) {}
};

// Encapsulate the Scroll component.
class ArkUIScrollNode: public ArkUINode {
public:
    ArkUIScrollNode() :
        ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI\_NODE\_SCROLL)) {}
};

// Encapsulate the Column component.
class ArkUIColumnNode: public ArkUINode {
public:
    ArkUIColumnNode() :
        ArkUINode(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI\_NODE\_COLUMN)) {}
};

// Create components using multiple threads.
napi\_value CreateNodeTreeOnMultiThread(napi\_env env, napi\_callback\_info info);
// Release components created using multiple threads.
napi\_value DisposeNodeTreeOnMultiThread(napi\_env env, napi\_callback\_info info);
} // namespace NativeModule

#endif // MYAPPLICATION\_CREATENODE\_H

// CreateNode.cpp
#include "CreateNode.h"

#include <cstdint>
#include <hilog/log.h>
#include <map>
#include <thread>
#include <napi/native\_api.h>
#include <arkui/native\_node\_napi.h>

namespace NativeModule {
#define FRAMEWORK\_NODE\_TREE\_NUMBER 4 // Number of component trees created in framework threads.
#define USER\_NODE\_TREE\_NUMBER 3 // Number of component trees created in developer threads.
struct AsyncData {
    napi\_env env;
    std::shared\_ptr<ArkUINode> parent = nullptr;
    std::shared\_ptr<ArkUINode> child = nullptr;
    std::string label = "";
};

// Save the mapping between the NodeContent pointer on the ArkTS side and the node tree root node on the native side.
std::map<ArkUI\_NodeContentHandle, std::shared\_ptr<ArkUIBaseNode>> g\_nodeMap;
ArkUI\_ContextHandle g\_contextHandle = nullptr;

// Create a component tree.
void CreateNodeTree(void \*asyncUITaskData) {
    auto asyncData = static\_cast<AsyncData\*>(asyncUITaskData);
    if (!asyncData) {
        return;
    }
    // Create the root node of the component tree.
    auto rowNode = std::make\_shared<ArkUIRowNode>();
    asyncData->child = rowNode;
    
    // Create a button component.
    auto buttonNode1 = std::make\_shared<ArkUIButtonNode>();
    ArkUI\_AttributeItem label\_item = { .string = asyncData->label.c\_str() };
    // Set the label attribute of the button component.
    int32\_t result = buttonNode1->SetLabel(label\_item);
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "Button SetLabel Failed %{public}d", result);
    }
    ArkUI\_NumberValue value\[\] = {{.f32 = 5}, {.f32 = 5}, {.f32 = 5}, {.f32 = 5}};
    ArkUI\_AttributeItem item = {value, 4};
    // Set the margin attribute of the button component.
    result = buttonNode1->SetMargin(item);
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "Button SetMargin Failed %{public}d", result);
    }
    // Set the width attribute of the button component.
    buttonNode1->SetWidth(150);
   
   // Create another button component.
    auto buttonNode2 = std::make\_shared<ArkUIButtonNode>();
    ArkUI\_AttributeItem label\_item2 = { .string = asyncData->label.c\_str() };
    // Set the label attribute of the button component.
    result = buttonNode2->SetLabel(label\_item2);
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "Button SetLabel Failed %{public}d", result);
    }
    ArkUI\_NumberValue value2\[\] = {{.f32 = 5}, {.f32 = 5}, {.f32 = 5}, {.f32 = 5}};
    ArkUI\_AttributeItem item2 = {value2, 4};
    // Set the margin attribute of the button component.
    result = buttonNode1->SetMargin(item2);
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "Button SetMargin Failed %{public}d", result);
    }
    // Set the width attribute of the button component.
    buttonNode2->SetWidth(150);

    // Mount the component to the component tree.
    rowNode->AddChild(buttonNode1);
    rowNode->AddChild(buttonNode2);
}

// Mount the component tree to the main UI tree.
void MountNodeTree(void \*asyncUITaskData) {
    auto asyncData = static\_cast<AsyncData\*>(asyncUITaskData);
    if (!asyncData) {
        return;
    }
    auto parent = asyncData->parent;
    auto child = asyncData->child;
    // Mount the component tree to the main UI tree.
    parent->AddChild(child);
    delete asyncData;
}

void CreateNodeOnFrameworkThread(ArkUI\_ContextHandle contextHandle, std::shared\_ptr<ArkUIColumnNode> parent) {
    for (int i = 0; i < FRAMEWORK\_NODE\_TREE\_NUMBER; i++) {
        // Create the subtree root node on the UI thread to maintain the scroll child order.
        auto columnItem = std::make\_shared<ArkUIColumnNode>();
        parent->AddChild(columnItem);
        AsyncData\* asyncData = new AsyncData();
        asyncData->parent = columnItem;
        asyncData->label = "OnFwkThread";
        // Create a component tree using the framework-provided non-UI thread. After the component tree is created, return to the UI thread and mount the component tree to the main UI tree.
        int32\_t result = OH\_ArkUI\_PostAsyncUITask(contextHandle, asyncData, CreateNodeTree, MountNodeTree);
        if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_PostAsyncUITask Failed %{public}d", result);
            delete asyncData;
        }
    }
}

void CreateNodeOnUserThread(ArkUI\_ContextHandle contextHandle, std::shared\_ptr<ArkUIColumnNode> parent) {
    auto columnItem = std::make\_shared<ArkUIColumnNode>();
    parent->AddChild(columnItem);
    // Create a component tree using the developer-created non-UI thread.
    std::thread userThread(\[columnItem, contextHandle\]() {
        for (int i = 0; i < USER\_NODE\_TREE\_NUMBER; i++) {
            AsyncData\* asyncData = new AsyncData();
            asyncData->parent = columnItem;
            asyncData->label = "OnUserThread1";
            CreateNodeTree(asyncData);
            // After the component tree is created, return to the UI thread and mount the component tree to the main UI tree.
            int32\_t result = OH\_ArkUI\_PostUITask(contextHandle, asyncData, MountNodeTree);
            if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_PostUITask Failed %{public}d", result);
                delete asyncData;
            }
        }
    });
    userThread.detach();
}

void CreateNodeOnUserThreadAndWait(ArkUI\_ContextHandle contextHandle, std::shared\_ptr<ArkUIColumnNode> parent) {
    auto columnItem = std::make\_shared<ArkUIColumnNode>();
    parent->AddChild(columnItem);
    // Create a component tree using the developer-created non-UI thread.
    std::thread userThread(\[columnItem, contextHandle\]() {
        for (int i = 0; i < USER\_NODE\_TREE\_NUMBER; i++) {
            AsyncData\* asyncData = new AsyncData();
            asyncData->parent = columnItem;
            asyncData->label = "OnUserThread2";
            CreateNodeTree(asyncData);
            // After the component tree is created, return to the UI thread and mount the component tree to the main tree. After the mounting is complete, continue to create the remaining components.
            int32\_t result = OH\_ArkUI\_PostUITaskAndWait(contextHandle, asyncData, MountNodeTree);
            if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_PostUITask Failed %{public}d", result);
                delete asyncData;
            }
        }
    });
    userThread.detach();
}

napi\_value CreateNodeTreeOnMultiThread(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = { nullptr, nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Obtain the mount point of the component on the ArkTS side.
    ArkUI\_NodeContentHandle contentHandle;
    int32\_t result = OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_GetNodeContentFromNapiValue Failed %{public}d", result);
        return nullptr;
    }
    
    // Obtain the context object pointer.
    if (!g\_contextHandle) {
        result = OH\_ArkUI\_GetContextFromNapiValue(env, args\[1\], &g\_contextHandle);
        if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_GetContextFromNapiValue Failed %{public}d", result);
            delete g\_contextHandle;
            g\_contextHandle = nullptr;
            return nullptr;
        }
    }
    
    // Create the root node of the component tree on the native side.
    auto scrollNode = std::make\_shared<ArkUIScrollNode>();
    // Mount the root node of the component tree on the native side to the main UI tree.
    result = OH\_ArkUI\_NodeContent\_AddNode(contentHandle, scrollNode->GetHandle());
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_NodeContent\_AddNode Failed %{public}d", result);
        return nullptr;
    }
    // Save the component tree on the native side.
    g\_nodeMap\[contentHandle\] = scrollNode;
    
    auto columnNode = std::make\_shared<ArkUIColumnNode>();
    scrollNode->AddChild(columnNode);
    // Create a component using the framework-provided thread pool.
    CreateNodeOnFrameworkThread(g\_contextHandle,columnNode);
    // Create a component using the developer-created non-UI thread.
    CreateNodeOnUserThread(g\_contextHandle,columnNode);
    CreateNodeOnUserThreadAndWait(g\_contextHandle,columnNode);
    return nullptr;
}

napi\_value DisposeNodeTreeOnMultiThread(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = { nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Obtain the mount point of the component on the ArkTS side.
    ArkUI\_NodeContentHandle contentHandle;
    int32\_t result = OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_GetNodeContentFromNapiValue Failed %{public}d", result);
        return nullptr;
    }
    
    auto it = g\_nodeMap.find(contentHandle);
    if (it == g\_nodeMap.end()) {
        return nullptr;
    }
    auto rootNode = it->second;
    // Unmount the root node of the component tree on the native side from the main UI tree.
    result = OH\_ArkUI\_NodeContent\_RemoveNode(contentHandle, rootNode->GetHandle());
    if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_NodeContent\_RemoveNode Failed %{public}d", result);
        return nullptr;
    }
    // Release the component tree on the native side.
    g\_nodeMap.erase(contentHandle);
    return nullptr;
}
} // namespace NativeModule

// napi\_init.cpp
#include "napi/native\_api.h"
#include "NativeEntry.h"
#include "CreateNode.h"

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    // Bind the native creation and destruction of components.
    napi\_property\_descriptor desc\[\] = {
        {"createNativeRoot", nullptr,
        NativeModule::CreateNativeRoot, nullptr, nullptr,
        nullptr, napi\_default, nullptr},
        
        {"destroyNativeRoot", nullptr,
        NativeModule::DestroyNativeRoot, nullptr, nullptr,
        nullptr, napi\_default, nullptr},
        
        {"createNodeTreeOnMultiThread", nullptr,
        NativeModule::CreateNodeTreeOnMultiThread, nullptr, nullptr,
        nullptr, napi\_default, nullptr},
        
        {"disposeNodeTreeOnMultiThread", nullptr,
        NativeModule::DisposeNodeTreeOnMultiThread, nullptr, nullptr,
        nullptr, napi\_default, nullptr}
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }
