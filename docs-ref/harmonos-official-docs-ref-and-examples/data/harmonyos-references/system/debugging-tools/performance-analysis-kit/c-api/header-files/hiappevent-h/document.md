# hiappevent.h

#### Overview

The **HiAppEvent** module provides event subscription and event logging function definitions. Before performing application event logging, you must construct a parameter list object to store the input event parameters and specify the event domain, event name, and event type.

Event domain: domain associated with the application event.

Event name: name of the application event.

Event type: fault, statistics, security, or behavior.

Parameter list: a linked list used to store event parameters. Each parameter consists of a parameter name and a parameter value.

**File to include**: <hiappevent/hiappevent.h>

**Library**: libhiappevent\_ndk.z.so

**System capability**: SystemCapability.HiviewDFX.HiAppEvent

**Since**: 8

**Related module**: [HiAppEvent](../../modules/hiappevent/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiAppEvent\_AppEventInfo](../../structs/hiappevent-appeventinfo/document.md) | HiAppEvent\_AppEventInfo | Defines the information about a single event, including the domain, name, type, and custom parameter list in JSON string format. |
| [HiAppEvent\_AppEventGroup](../../structs/hiappevent-appeventgroup/document.md) | HiAppEvent\_AppEventGroup | Defines the information about an event group, including its name, the array of event information grouped by name, and the length of the event array. |
| [ParamListNode\*](../../structs/paramlistnode/document.md) | ParamList | Defines the event parameter list node. |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md) | HiAppEvent\_Watcher | Defines the watcher for application events. |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md) | HiAppEvent\_Processor | Defines a processor for application events. |
| [HiAppEvent\_Config](../../structs/hiappevent-config/document.md) | HiAppEvent\_Config | Defines the configuration object used to set the conditions for triggering system events. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiAppEvent\_ErrorCode](#hiappevent_errorcode) | HiAppEvent\_ErrorCode | Enumerates the error codes used in the HiAppEvent module. |
| [EventType](#eventtype) | \- | Enumerates the event types. You are advised to select different event types based on application scenarios. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_HiAppEvent\_OnReceive)(const char\* domain, const struct HiAppEvent\_AppEventGroup\* appEventGroups, uint32\_t groupLen)](#oh_hiappevent_onreceive) | OH\_HiAppEvent\_OnReceive | Passes event content to the caller. **Note**: The lifecycle of the object pointed by the pointer in the callback is limited to the callback function. Do not use the pointer outside of the callback function. If the information needs to be cached, perform a deep copy of the content pointed by the pointer. |
| [typedef void (\*OH\_HiAppEvent\_OnTrigger)(int row, int size)](#oh_hiappevent_ontrigger) | OH\_HiAppEvent\_OnTrigger | 
Invoked if the event received by the watcher meets the conditions specified by **OH\_HiAppEvent\_SetTriggerCondition**. When the **OH\_HiAppEvent\_OnReceive** callback is not set in the watcher, the event received by the watcher will be saved.

After the callback is complete, if a newly saved event meets the specified condition, the callback is invoked again.

 |
| [typedef void (\*OH\_HiAppEvent\_OnTake)(const char\* const \*events, uint32\_t eventLen)](#oh_hiappevent_ontake) | OH\_HiAppEvent\_OnTake | Passes the events received by the watcher to the caller when **OH\_HiAppEvent\_TakeWatcherData** is used to obtain the events. Note: The lifecycle of the object pointed by the pointer in the callback is limited to the callback function. Do not use the pointer outside of the callback function. If the information needs to be cached, perform a deep copy of the content pointed by the pointer. |
| [ParamList OH\_HiAppEvent\_CreateParamList(void)](#oh_hiappevent_createparamlist) | \- | 

Creates a pointer to a parameter list object.

Note: If the created pointer to a parameter list object is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyParamList](#oh_hiappevent_destroyparamlist).

 |
| [void OH\_HiAppEvent\_DestroyParamList(ParamList list)](#oh_hiappevent_destroyparamlist) | \- | Destroys a pointer to a parameter list object and releases its allocated memory. |
| [ParamList OH\_HiAppEvent\_AddBoolParam(ParamList list, const char\* name, bool boolean)](#oh_hiappevent_addboolparam) | \- | Adds an event parameter of the Boolean type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddBoolArrayParam(ParamList list, const char\* name, const bool\* booleans, int arrSize)](#oh_hiappevent_addboolarrayparam) | \- | Adds an event parameter of the Boolean array type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt8Param(ParamList list, const char\* name, int8\_t num)](#oh_hiappevent_addint8param) | \- | Adds an event parameter of the int8\_t type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt8ArrayParam(ParamList list, const char\* name, const int8\_t\* nums, int arrSize)](#oh_hiappevent_addint8arrayparam) | \- | Adds an event parameter of the int8\_t array type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt16Param(ParamList list, const char\* name, int16\_t num)](#oh_hiappevent_addint16param) | \- | Adds an event parameter of the int16\_t type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt16ArrayParam(ParamList list, const char\* name, const int16\_t\* nums, int arrSize)](#oh_hiappevent_addint16arrayparam) | \- | Adds an event parameter of the int16\_t array type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt32Param(ParamList list, const char\* name, int32\_t num)](#oh_hiappevent_addint32param) | \- | Adds an event parameter of the int32\_t type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt32ArrayParam(ParamList list, const char\* name, const int32\_t\* nums, int arrSize)](#oh_hiappevent_addint32arrayparam) | \- | Adds an event parameter of the int32\_t array type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt64Param(ParamList list, const char\* name, int64\_t num)](#oh_hiappevent_addint64param) | \- | Adds an event parameter of the int64\_t type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddInt64ArrayParam(ParamList list, const char\* name, const int64\_t\* nums, int arrSize)](#oh_hiappevent_addint64arrayparam) | \- | Adds an event parameter of the int64\_t array type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddFloatParam(ParamList list, const char\* name, float num)](#oh_hiappevent_addfloatparam) | \- | Adds an event parameter of the float type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddFloatArrayParam(ParamList list, const char\* name, const float\* nums, int arrSize)](#oh_hiappevent_addfloatarrayparam) | \- | Adds an event parameter of the float array type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddDoubleParam(ParamList list, const char\* name, double num)](#oh_hiappevent_adddoubleparam) | \- | Adds an event parameter of the Double type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddDoubleArrayParam(ParamList list, const char\* name, const double\* nums, int arrSize)](#oh_hiappevent_adddoublearrayparam) | \- | Adds an event parameter of the double array type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddStringParam(ParamList list, const char\* name, const char\* str)](#oh_hiappevent_addstringparam) | \- | Adds a parameter of the string type to the parameter list. |
| [ParamList OH\_HiAppEvent\_AddStringArrayParam(ParamList list, const char\* name, const char \* const \*strs, int arrSize)](#oh_hiappevent_addstringarrayparam) | \- | Adds a parameter of the string array type to the parameter list. |
| [int OH\_HiAppEvent\_Write(const char\* domain, const char\* name, enum EventType type, const ParamList list)](#oh_hiappevent_write) | \- | Logs application events whose parameters are of the list type. Before application event logging, use this API to verify parameters of the events. If the verification is successful, the API writes the events to the event file. |
| [bool OH\_HiAppEvent\_Configure(const char\* name, const char\* value)](#oh_hiappevent_configure) | \- | Configures the application event logging function. This function is used to configure the event logging function and the storage quota of the event file directory. |
| [HiAppEvent\_Watcher\* OH\_HiAppEvent\_CreateWatcher(const char\* name)](#oh_hiappevent_createwatcher) | \- | 

Creates a watcher for application events.

Note: If a created watcher is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyWatcher](#oh_hiappevent_destroywatcher).

 |
| [void OH\_HiAppEvent\_DestroyWatcher(HiAppEvent\_Watcher\* watcher)](#oh_hiappevent_destroywatcher) | \- | Destroys a created watcher. Note: If a created watcher is no longer used, destroy it to release memory to prevent memory leaks. After the watcher is destroyed, set its pointer to null. |
| [int OH\_HiAppEvent\_SetTriggerCondition(HiAppEvent\_Watcher\* watcher, int row, int size, int timeOut)](#oh_hiappevent_settriggercondition) | \- | 

Sets the trigger condition of the **OH\_HiAppEvent\_OnTrigger** callback.

You can set the trigger condition by the number and size of new events received by the watcher, and **onTrigger** timeout interval. Ensure that at least one of the trigger conditions is set on the caller side.

 |
| [int OH\_HiAppEvent\_SetAppEventFilter(HiAppEvent\_Watcher\* watcher, const char\* domain, uint8\_t eventTypes, const char\* const \*names, int namesLen)](#oh_hiappevent_setappeventfilter) | \- | Sets the type of events to listen for. This function can be called repeatedly. You can add multiple filtering conditions instead of replacing them. The watcher will receive notifications of events that meet any of the filtering conditions. |
| [int OH\_HiAppEvent\_SetWatcherOnTrigger(HiAppEvent\_Watcher\* watcher, OH\_HiAppEvent\_OnTrigger onTrigger)](#oh_hiappevent_setwatcherontrigger) | \- | 

Sets the **onTrigger** callback.

If **OnReceive** is not set or is set to **nullptr**, the application events received by the watcher will be saved. If the saved application events meet the trigger conditions of the **onTrigger** callback, the **onTrigger** callback will be called.

 |
| [int OH\_HiAppEvent\_SetWatcherOnReceive(HiAppEvent\_Watcher\* watcher, OH\_HiAppEvent\_OnReceive onReceive)](#oh_hiappevent_setwatcheronreceive) | \- | Sets the **onReceive** callback. When the listener detects the corresponding event, the onReceive callback is called. |
| [int OH\_HiAppEvent\_TakeWatcherData(HiAppEvent\_Watcher\* watcher, uint32\_t eventNum, OH\_HiAppEvent\_OnTake onTake)](#oh_hiappevent_takewatcherdata) | \- | Obtains the event saved by the watcher. |
| [int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher\* watcher)](#oh_hiappevent_addwatcher) | \- | 

Adds a watcher. Once a watcher is added, it starts to listen for system messages.

Note: The **OH\_HiAppEvent\_AddWatcher** API involves I/O operations. In performance-sensitive service scenarios, you need to determine whether to call this API in the main thread or a child thread based on the actual service requirements.

The name passed to the **OH\_HiAppEvent\_AddWatcher** API should be unique. If the same name is passed, the previous subscription will be overwritten.

 |
| [int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher\* watcher)](#oh_hiappevent_removewatcher) | \- | Removes a watcher. Once a watcher is removed, it stops listening for system messages. Note: This API only enables the watcher to stop listening for system messages. It does not destroy the watcher. The watcher still resides in the memory until the OH\_HiAppEvent\_DestroyWatcher API is called. |
| [void OH\_HiAppEvent\_ClearData()](#oh_hiappevent_cleardata) | \- | Clears the events saved by all watchers. |
| [HiAppEvent\_Processor\* OH\_HiAppEvent\_CreateProcessor(const char\* name)](#oh_hiappevent_createprocessor) | \- | 

Creates a processor for application events.

Note: If a created processor is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyProcessor](#oh_hiappevent_destroyprocessor).

 |
| [int OH\_HiAppEvent\_SetReportRoute(HiAppEvent\_Processor\* processor, const char\* appId, const char\* routeInfo)](#oh_hiappevent_setreportroute) | \- | Sets the report route for the processor. |
| [int OH\_HiAppEvent\_SetReportPolicy(HiAppEvent\_Processor\* processor, int periodReport, int batchReport, bool onStartReport, bool onBackgroundReport)](#oh_hiappevent_setreportpolicy) | \- | Sets the report policy for the processor. |
| [int OH\_HiAppEvent\_SetReportEvent(HiAppEvent\_Processor\* processor, const char\* domain, const char\* name, bool isRealTime)](#oh_hiappevent_setreportevent) | \- | Sets the report event for the processor. |
| [int OH\_HiAppEvent\_SetCustomConfig(HiAppEvent\_Processor\* processor, const char\* key, const char\* value)](#oh_hiappevent_setcustomconfig) | \- | Sets the custom extension parameters of the processor. |
| [int OH\_HiAppEvent\_SetConfigId(HiAppEvent\_Processor\* processor, int configId)](#oh_hiappevent_setconfigid) | \- | Sets the configuration ID of the processor. |
| [int OH\_HiAppEvent\_SetConfigName(HiAppEvent\_Processor\* processor, const char\* configName)](#oh_hiappevent_setconfigname) | \- | Sets the configuration name of the processor. |
| [int OH\_HiAppEvent\_SetReportUserId(HiAppEvent\_Processor\* processor, const char\* const \* userIdNames, int size)](#oh_hiappevent_setreportuserid) | \- | Sets the report user ID of the processor. |
| [int OH\_HiAppEvent\_SetReportUserProperty(HiAppEvent\_Processor\* processor, const char\* const \* userPropertyNames, int size)](#oh_hiappevent_setreportuserproperty) | \- | Sets the report user property of the processor. |
| [int64\_t OH\_HiAppEvent\_AddProcessor(HiAppEvent\_Processor\* processor)](#oh_hiappevent_addprocessor) | \- | Adds a processor. You can add a processor to migrate event data to the cloud. You can preset the implementation of the processor on the device and set its properties based on its constraints. Note that the configuration information of **Processor** must be provided by the data processor. Yet, as no data processor is preset in the device for interaction for the moment, migrating events to the cloud is unavailable. |
| [void OH\_HiAppEvent\_DestroyProcessor(HiAppEvent\_Processor\* processor)](#oh_hiappevent_destroyprocessor) | \- | Destroys a processor. Note: If a processor is no longer used, destroy it to release memory to prevent memory leaks. After the processor is destroyed, set its pointer to null. |
| [int OH\_HiAppEvent\_RemoveProcessor(int64\_t processorId)](#oh_hiappevent_removeprocessor) | \- | Removes a processor. Once a processor is removed, it stops reporting events. Note: This API only stops the processor reporting events but does not destroy the processor. You can call **OH\_HiAppEvent\_DestroyProcessor** to destroy the processor and release the memory. |
| [HiAppEvent\_Config\* OH\_HiAppEvent\_CreateConfig(void)](#oh_hiappevent_createconfig) | \- | 

Creates a pointer to the configuration object that sets the conditions for triggering system events.

Note: If the created pointer to the configuration object that sets the conditions for triggering system events is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyConfig](#oh_hiappevent_destroyconfig).

 |
| [void OH\_HiAppEvent\_DestroyConfig(HiAppEvent\_Config\* config)](#oh_hiappevent_destroyconfig) | \- | Destroys a configuration object. Note: If a configuration object is no longer used, destroy it to release memory to prevent memory leaks. After the object is destroyed, set its pointer to null. |
| [int OH\_HiAppEvent\_SetConfigItem(HiAppEvent\_Config\* config, const char\* itemName, const char\* itemValue)](#oh_hiappevent_setconfigitem) | \- | Sets the items in the configuration object. |
| [int OH\_HiAppEvent\_SetEventConfig(const char\* name, HiAppEvent\_Config\* config)](#oh_hiappevent_seteventconfig) | \- | 

Sets event configuration parameters.

Configuration items vary depending on events. Currently, only the following events are supported:

**MAIN\_THREAD\_JANK**. (For details about the parameter configuration, see [Main Thread Jank Event Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events#parameters-of-oh_hiappevent_seteventconfig).)

**MAIN\_THREAD\_JANK\_V2**. (For details about the parameter configuration, see [Main Thread Jank Event Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events#parameters-of-oh_hiappevent_seteventconfig).)

 |

#### Enum Description

#### \[h2\]HiAppEvent\_ErrorCode

enum HiAppEvent\_ErrorCode

**Description**

Enumerates the error codes used in the HiAppEvent module.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| HIAPPEVENT\_SUCCESS = 0 | The operation is successful. |
| HIAPPEVENT\_INVALID\_PARAM\_VALUE\_LENGTH = 4 | 
The parameter value length is invalid.

**Since**: 18

 |
| HIAPPEVENT\_PROCESSOR\_IS\_NULL = -7 | 

The processor is null.

**Since**: 18

 |
| HIAPPEVENT\_PROCESSOR\_NOT\_FOUND = -8 | 

The processor is not found.

**Since**: 18

 |
| HIAPPEVENT\_INVALID\_PARAM\_VALUE = -9 | The parameter value is invalid. |
| HIAPPEVENT\_EVENT\_CONFIG\_IS\_NULL = -10 | The event configuration is null. |
| HIAPPEVENT\_OPERATE\_FAILED = -100 | 

The operation failed.

**Since**: 18

 |
| HIAPPEVENT\_INVALID\_UID = -200 | 

The user ID is invalid.

**Since**: 18

 |

#### \[h2\]EventType

enum EventType

**Description**

Enumerates the event types. You are advised to select different event types based on application scenarios.

**Since**: 8

| Enum Item | Description |
| :-- | :-- |
| FAULT = 1 | Fault event. |
| STATISTIC = 2 | Statistics event. |
| SECURITY = 3 | Security event. |
| BEHAVIOR = 4 | Behavior event. |

#### Function Description

#### \[h2\]OH\_HiAppEvent\_OnReceive()

typedef void (\*OH\_HiAppEvent\_OnReceive)(const char\* domain, const struct HiAppEvent\_AppEventGroup\* appEventGroups, uint32\_t groupLen)

**Description**

Passes event content to the caller. Note: The lifecycle of the object pointed by the pointer in the callback is limited to the callback function. Do not use the pointer outside of the callback function. If the information needs to be cached, perform a deep copy of the content pointed by the pointer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* domain | Domain of the received application event. |
| [const struct HiAppEvent\_AppEventGroup](../../structs/hiappevent-appeventgroup/document.md)\* appEventGroups | Event group array. |
| uint32\_t groupLen | Length of the event group array. |

#### \[h2\]OH\_HiAppEvent\_OnTrigger()

typedef void (\*OH\_HiAppEvent\_OnTrigger)(int row, int size)

**Description**

Invoked if the event received by the watcher meets the conditions specified by **OH\_HiAppEvent\_SetTriggerCondition**. When the **OH\_HiAppEvent\_OnReceive** callback is not set in the watcher, the event received by the watcher will be saved.

After the callback is complete, if a newly saved event meets the specified condition, the callback is invoked again.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int row | Number of events newly received by the watcher. |
| int size | Total size of events newly received by the watcher. The size of a single event is the length of the JSON string converted from the event. |

#### \[h2\]OH\_HiAppEvent\_OnTake()

typedef void (\*OH\_HiAppEvent\_OnTake)(const char\* const \*events, uint32\_t eventLen)

**Description**

Passes the events received by the watcher to the caller when **OH\_HiAppEvent\_TakeWatcherData** is used to obtain the events. Note: The lifecycle of the object pointed by the pointer in the callback is limited to the callback function. Do not use the pointer outside of the callback function. If the information needs to be cached, perform a deep copy of the content pointed by the pointer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* const \*events | Event array in JSON string format. |
| uint32\_t eventLen | Size of the event array. |

#### \[h2\]OH\_HiAppEvent\_CreateParamList()

ParamList OH\_HiAppEvent\_CreateParamList(void)

**Description**

Creates a pointer to a parameter list object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/n7Umi1nIQ3GXc1mh5ikiug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72D395671D7FBA24B21ACD79D1DF5FA32A74D78004D87743840234178FA9DF66)

If the created pointer to a parameter list object is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyParamList](#oh_hiappevent_destroyparamlist).

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list object. |

#### \[h2\]OH\_HiAppEvent\_DestroyParamList()

void OH\_HiAppEvent\_DestroyParamList(ParamList list)

**Description**

Destroys a pointer to a parameter list object and releases its allocated memory.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list object. |

#### \[h2\]OH\_HiAppEvent\_AddBoolParam()

ParamList OH\_HiAppEvent\_AddBoolParam(ParamList list, const char\* name, bool boolean)

**Description**

Adds an event parameter of the Boolean type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| bool boolean | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddBoolArrayParam()

ParamList OH\_HiAppEvent\_AddBoolArrayParam(ParamList list, const char\* name, const bool\* booleans, int arrSize)

**Description**

Adds an event parameter of the Boolean array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const bool\* booleans | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt8Param()

ParamList OH\_HiAppEvent\_AddInt8Param(ParamList list, const char\* name, int8\_t num)

**Description**

Adds an event parameter of the int8\_t type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| int8\_t num | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt8ArrayParam()

ParamList OH\_HiAppEvent\_AddInt8ArrayParam(ParamList list, const char\* name, const int8\_t\* nums, int arrSize)

**Description**

Adds an event parameter of the int8\_t array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const int8\_t\* nums | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt16Param()

ParamList OH\_HiAppEvent\_AddInt16Param(ParamList list, const char\* name, int16\_t num)

**Description**

Adds an event parameter of the int16\_t type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| int16\_t num | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt16ArrayParam()

ParamList OH\_HiAppEvent\_AddInt16ArrayParam(ParamList list, const char\* name, const int16\_t\* nums, int arrSize)

**Description**

Adds an event parameter of the int16\_t array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const int16\_t\* nums | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt32Param()

ParamList OH\_HiAppEvent\_AddInt32Param(ParamList list, const char\* name, int32\_t num)

**Description**

Adds an event parameter of the int32\_t type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| int32\_t num | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt32ArrayParam()

ParamList OH\_HiAppEvent\_AddInt32ArrayParam(ParamList list, const char\* name, const int32\_t\* nums, int arrSize)

**Description**

Adds an event parameter of the int32\_t array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const int32\_t\* nums | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt64Param()

ParamList OH\_HiAppEvent\_AddInt64Param(ParamList list, const char\* name, int64\_t num)

**Description**

Adds an event parameter of the int64\_t type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| int64\_t num | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddInt64ArrayParam()

ParamList OH\_HiAppEvent\_AddInt64ArrayParam(ParamList list, const char\* name, const int64\_t\* nums, int arrSize)

**Description**

Adds an event parameter of the int64\_t array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const int64\_t\* nums | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddFloatParam()

ParamList OH\_HiAppEvent\_AddFloatParam(ParamList list, const char\* name, float num)

**Description**

Adds an event parameter of the float type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| float num | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddFloatArrayParam()

ParamList OH\_HiAppEvent\_AddFloatArrayParam(ParamList list, const char\* name, const float\* nums, int arrSize)

**Description**

Adds an event parameter of the float array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const float\* nums | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddDoubleParam()

ParamList OH\_HiAppEvent\_AddDoubleParam(ParamList list, const char\* name, double num)

**Description**

Adds an event parameter of the Double type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| double num | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddDoubleArrayParam()

ParamList OH\_HiAppEvent\_AddDoubleArrayParam(ParamList list, const char\* name, const double\* nums, int arrSize)

**Description**

Adds an event parameter of the double array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const double\* nums | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddStringParam()

ParamList OH\_HiAppEvent\_AddStringParam(ParamList list, const char\* name, const char\* str)

**Description**

Adds a parameter of the string type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const char\* str | Value of the parameter to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_AddStringArrayParam()

ParamList OH\_HiAppEvent\_AddStringArrayParam(ParamList list, const char\* name, const char \* const \*strs, int arrSize)

**Description**

Adds a parameter of the string array type to the parameter list.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) list | Pointer to the parameter list to which parameters need to be added. |
| const char\* name | Name of the parameter to be added. |
| const char \* const \*strs | Value of the parameter to be added. |
| int arrSize | Size of the parameter array to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ParamList](../../structs/paramlistnode/document.md) | Pointer to the parameter list that contains the parameters added. |

#### \[h2\]OH\_HiAppEvent\_Write()

int OH\_HiAppEvent\_Write(const char\* domain, const char\* name, enum EventType type, const ParamList list)

**Description**

Logs application events whose parameters are of the list type. Before application event logging, use this API to verify parameters of the events. If the verification is successful, the API writes the events to the event file.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* domain | 
Event domain. You can customize event domains as required.

The value is a string that contains a maximum of 32 characters, including digits (0 to 9), letters (a to z), and underscore (\_). It must start with a letter and cannot end with an underscore (\_).

 |
| const char\* name | 

Event name. You can customize event names as required.

The value is a string that contains a maximum of 48 characters, including digits (0 to 9), letters (a to z), underscore (\_), and dollar sign ($). It must start with a letter or dollar sign ($) and end with a digit or letter.

 |
| enum EventType type | Event type. For details, see [EventType](#eventtype). |
| [const ParamList](../../structs/paramlistnode/document.md) list | 

List of event parameters, each of which consists of a parameter name and a parameter value. The specifications are as follows:

1.

The value is a string that contains a maximum of 32 characters, including digits (0 to 9), letters (a to z), underscore (\_), and dollar sign ($). It must start with a letter or dollar sign ($) and end with a digit or letter.

2\. The parameter value can be a string, number, Boolean, or array. The length of a string must be less than 8 × 1024 characters. If this limit is exceeded, excess characters will be truncated.

The element type of an array parameter can only be a string, number, or Boolean, and the number of elements must be less than 100. If this limit is exceeded, excess elements will be discarded.

3\. The maximum number of parameters is 32. If this limit is exceeded, excess parameters will be discarded.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
If the event parameters are successfully verified, **0** is returned and the event is written into the event file.

If an event contains invalid parameters, a positive value is returned. The event is written into the event file after the invalid parameters are discarded.

If the event parameter fails to be verified, a negative value is returned and the event is not written to the event file.

**0**: Parameter verification successful.

**\-1**: Invalid event name.

**\-4**: Invalid event domain name.

**\-99**: Application event logging disabled.

**1**: Invalid event parameter name.

**4**: Invalid event parameter string length.

**5**: Invalid number of event parameters.

**6**: Invalid event parameter array length.

**8**: Duplicate event parameter name.

 |

#### \[h2\]OH\_HiAppEvent\_Configure()

bool OH\_HiAppEvent\_Configure(const char\* name, const char\* value)

**Description**

Configures the application event logging function. This function is used to configure the event logging function and the storage quota of the event file directory.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* name | Configuration item name The value can be [DISABLE](../hiappevent-cfg-h/document.md#disable) or [MAX\_STORAGE](../hiappevent-cfg-h/document.md#max_storage). |
| const char\* value | 
Configuration item value. If the configuration item name is [DISABLE](../hiappevent-cfg-h/document.md#disable), the value can be **true** or **false**.

If the configuration item name is [MAX\_STORAGE](../hiappevent-cfg-h/document.md#max_storage), the quota value can contain only digits and the unit character. The unit character can be **b**|**k**|**kb**|**m**|**mb**|**g**|**gb**|**t**|**tb**, which is case insensitive.

The quota value must start with a digit. You can determine whether to pass the unit. If the unit is left empty, **b** (that is, byte) is used by default.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Configuration result. The value **true** indicates that the configuration is successful, and the value **false** indicates the opposite. |

#### \[h2\]OH\_HiAppEvent\_CreateWatcher()

HiAppEvent\_Watcher\* OH\_HiAppEvent\_CreateWatcher(const char\* name)

**Description**

Creates a watcher for application events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/QiSsq9JLTvCwdnJtcGJCiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E92D692B78F754EFBD9A82328447ED1DB2170C91F1799AE7AF3D2C6C2510706)

If a created watcher is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyWatcher](#oh_hiappevent_destroywatcher).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* name | Watcher name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* | Pointer to the new watcher if the API is called successfully; **nullptr** if the **name** parameter is invalid. |

#### \[h2\]OH\_HiAppEvent\_DestroyWatcher()

void OH\_HiAppEvent\_DestroyWatcher(HiAppEvent\_Watcher\* watcher)

**Description**

Destroys a created watcher. Note: If a created watcher is no longer used, destroy it to release memory to prevent memory leaks. After the watcher is destroyed, set its pointer to null.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |

#### \[h2\]OH\_HiAppEvent\_SetTriggerCondition()

int OH\_HiAppEvent\_SetTriggerCondition(HiAppEvent\_Watcher\* watcher, int row, int size, int timeOut)

**Description**

Sets the trigger condition of the **OH\_HiAppEvent\_OnTrigger** callback.

You can set the trigger condition by the number and size of new events received by the watcher, and **onTrigger** timeout interval. Ensure that at least one of the trigger conditions is set on the caller side.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |
| int row | 
Row count. If the input value is greater than 0 and the number of newly received events is greater than or equal to the value of this parameter, the configured **onTrigger** callback is called.

If the input value is less than or equal to 0, the number of received events is not used as the condition to trigger the **onTrigger** callback.

 |
| int size | 

Size value. If the input value is greater than 0 and the size of the newly received event is greater than or equal to the value of this parameter, the configured **onTrigger** callback is called. The size of a single event is the length of the JSON string converted from the event.

If the input value is less than or equal to 0, the size of received events is not used as the condition to trigger the **onTrigger** callback.

 |
| int timeOut | 

Timeout value, in seconds. If the input value is greater than 0, the system checks the watcher for newly received events based on the timeout interval. If there are any newly received events, the configured onTrigger callback is triggered.

After the callback is complete, the system checks the watcher for newly received events when the timeout value expires.

If the input value is less than or equal to 0, the timeout interval is not used as the condition to trigger the onTrigger callback.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the API is called successfully; **\-5** if the pointer to an input parameter is null. |

#### \[h2\]OH\_HiAppEvent\_SetAppEventFilter()

int OH\_HiAppEvent\_SetAppEventFilter(HiAppEvent\_Watcher\* watcher, const char\* domain, uint8\_t eventTypes, const char\* const \*names, int namesLen)

**Description**

Sets the type of events to listen for. This function can be called repeatedly. You can add multiple filtering conditions instead of replacing them. The watcher will receive notifications of events that meet any of the filtering conditions.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |
| const char\* domain | Domain of events to be listened for. |
| uint8\_t eventTypes | 
Types of events to be listened for. The bitwise AND matching mode is used. Multiple types of events can be listened for. If the first bit is **1** (the value is **1**), fault events can be listened for.

If the second bit is **1** (the value is **2**), statistics events can be listened for.

If the third bit is **1** (the value is **4**), security events can be listened for.

If the fourth digit is **1** (the value is **8**), events of the listening behavior type can be listened for.

If four digits are **1** (the value is **15**) or 0 (the value is **0**), events of all types can be listened for.

 |
| const char\* const \*names | Array of the event names. |
| int namesLen | Length of the event name array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the API is called successfully; **\-1** if the **names** parameter is invalid; **\-4** if the **domain** parameter is invalid; **\-5** if the pointer to an input parameter is null. |

#### \[h2\]OH\_HiAppEvent\_SetWatcherOnTrigger()

int OH\_HiAppEvent\_SetWatcherOnTrigger(HiAppEvent\_Watcher\* watcher, OH\_HiAppEvent\_OnTrigger onTrigger)

**Description**

Sets the **onTrigger** callback.

If **OnReceive** is not set or is set to **nullptr**, the application events received by the watcher will be saved. If the saved application events meet the trigger conditions of the **onTrigger** callback, the **onTrigger** callback will be called.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |
| [OH\_HiAppEvent\_OnTrigger](#oh_hiappevent_ontrigger) onTrigger | Callback to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the API is called successfully; **\-5** if the pointer to an input parameter is null. |

#### \[h2\]OH\_HiAppEvent\_SetWatcherOnReceive()

int OH\_HiAppEvent\_SetWatcherOnReceive(HiAppEvent\_Watcher\* watcher, OH\_HiAppEvent\_OnReceive onReceive)

**Description**

Sets the **onReceive** callback. When the listener detects the corresponding event, the onReceive callback is called.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |
| [OH\_HiAppEvent\_OnReceive](#oh_hiappevent_onreceive) onReceive | Pointer to the callback function. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the API is called successfully; **\-5** if the pointer to an input parameter is null. |

#### \[h2\]OH\_HiAppEvent\_TakeWatcherData()

int OH\_HiAppEvent\_TakeWatcherData(HiAppEvent\_Watcher\* watcher, uint32\_t eventNum, OH\_HiAppEvent\_OnTake onTake)

**Description**

Obtains the event saved by the watcher.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |
| uint32\_t eventNum | If the input value is less than or equal to **0**, all saved events are obtained. If the input value is greater than **0**, events are sorted by time in descending order and a specified number of saved events are obtained. |
| [OH\_HiAppEvent\_OnTake](#oh_hiappevent_ontake) onTake | Pointer to the callback. The event information is returned through this callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the API is called successfully; **\-5** if the pointer to an input parameter is null; **\-6** if **OH\_HiAppEvent\_AddWatcher** has not been called to add a watcher. |

#### \[h2\]OH\_HiAppEvent\_AddWatcher()

int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher\* watcher)

**Description**

Adds a watcher. Once a watcher is added, it starts to listen for system messages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/fdZVOrY4Tv62PRW0-e9LNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F66B744C9C6AFEBCABC79486995BE9D7D7F27DB6E8532586BA7969F99AE0F7EB)

The **OH\_HiAppEvent\_AddWatcher** API involves I/O operations. In performance-sensitive service scenarios, you need to determine whether to call this API in the main thread or a child thread based on the actual service requirements.

The name passed to the **OH\_HiAppEvent\_AddWatcher** API should be unique. If the same name is passed, the previous subscription will be overwritten.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the API is called successfully; **\-5** if the pointer to an input parameter is null. |

#### \[h2\]OH\_HiAppEvent\_RemoveWatcher()

int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher\* watcher)

**Description**

Removes a watcher. Once a watcher is removed, it stops listening for system messages. Note: This API only enables the watcher to stop listening for system messages. It does not destroy the watcher. The watcher still resides in the memory until the OH\_HiAppEvent\_DestroyWatcher API is called.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Watcher](../../structs/hiappevent-watcher/document.md)\* watcher | Pointer to the watcher (that is, the pointer returned by OH\_HiAppEvent\_CreateWatcher). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the API is called successfully; **\-5** if the pointer to an input parameter is null; **\-6** if **OH\_HiAppEvent\_AddWatcher** has not been called to add a watcher. |

#### \[h2\]OH\_HiAppEvent\_ClearData()

void OH\_HiAppEvent\_ClearData()

**Description**

Clears the events saved by all watchers.

**Since**: 12

#### \[h2\]OH\_HiAppEvent\_CreateProcessor()

HiAppEvent\_Processor\* OH\_HiAppEvent\_CreateProcessor(const char\* name)

**Description**

Creates a processor for application events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/aAGHUFqAQwiiAqP2ekK_4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=132CD28454F1A1F5E9B6BB304C2782395CC648FD04BC34DB79C8F568215AABB8)

If a created processor is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyProcessor](#oh_hiappevent_destroyprocessor).

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* name | Processor name, which can contain only letters, digits, underscores (\_), and dollar signs ($). It cannot start with a digit and cannot exceed 256 characters. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* | Pointer to the new processor if the API is called successfully; **nullptr** if the **name** parameter is invalid. |

#### \[h2\]OH\_HiAppEvent\_SetReportRoute()

int OH\_HiAppEvent\_SetReportRoute(HiAppEvent\_Processor\* processor, const char\* appId, const char\* routeInfo)

**Description**

Sets the report route for the processor.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| const char\* appId | Application ID of the processor. |
| const char\* routeInfo | Server location information. The default value is an empty string. The string length cannot exceed 8 KB. Otherwise, the default value is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE\_LENGTH](#hiappevent_errorcode): Invalid parameter value length.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetReportPolicy()

int OH\_HiAppEvent\_SetReportPolicy(HiAppEvent\_Processor\* processor, int periodReport, int batchReport, bool onStartReport, bool onBackgroundReport)

**Description**

Sets the report policy for the processor.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| int periodReport | Period for reporting events, in seconds. |
| int batchReport | Threshold for reporting events. When the number of events reaches the threshold, an event is reported. |
| bool onStartReport | Whether to report events during startup. **true**: yes; **false**: no. |
| bool onBackgroundReport | Whether to report events after an application switches to the background. **true**: yes; **false**: no. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetReportEvent()

int OH\_HiAppEvent\_SetReportEvent(HiAppEvent\_Processor\* processor, const char\* domain, const char\* name, bool isRealTime)

**Description**

Sets the report event for the processor.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| const char\* domain | Domain of the report event. |
| const char\* name | Name of the report event. |
| bool isRealTime | Whether to report events in real time. The value **true** means to report events in real time, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetCustomConfig()

int OH\_HiAppEvent\_SetCustomConfig(HiAppEvent\_Processor\* processor, const char\* key, const char\* value)

**Description**

Sets the custom extension parameters of the processor.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| const char\* key | Parameter name, which contains a maximum of 32 characters. |
| const char\* value | Parameter value, which contains a maximum of 1024 characters. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE\_LENGTH](#hiappevent_errorcode): Invalid parameter value length.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetConfigId()

int OH\_HiAppEvent\_SetConfigId(HiAppEvent\_Processor\* processor, int configId)

**Description**

Sets the configuration ID of the processor.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| int configId | Configuration ID of the processor, which is a natural number. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetConfigName()

int OH\_HiAppEvent\_SetConfigName(HiAppEvent\_Processor\* processor, const char\* configName)

**Description**

Sets the configuration name of the processor.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| const char\* configName | Configuration name of the data processor, which can contain only letters, digits, underscores (\_), and dollar signs ($). It cannot start with a digit and cannot exceed 256 characters. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE\_LENGTH](#hiappevent_errorcode): Invalid parameter value length.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetReportUserId()

int OH\_HiAppEvent\_SetReportUserId(HiAppEvent\_Processor\* processor, const char\* const \* userIdNames, int size)

**Description**

Sets the report user ID of the processor.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| const char\* const \* userIdNames | Name array of user IDs that can be reported by the processor. |
| int size | Length of the name array of user IDs. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE\_LENGTH](#hiappevent_errorcode): Invalid parameter value length.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetReportUserProperty()

int OH\_HiAppEvent\_SetReportUserProperty(HiAppEvent\_Processor\* processor, const char\* const \* userPropertyNames, int size)

**Description**

Sets the report user property of the processor.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |
| const char\* const \* userPropertyNames | Name array of user properties that can be reported by the processor. |
| int size | Length of the name array of user properties. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE\_LENGTH](#hiappevent_errorcode): Invalid parameter value length.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_AddProcessor()

int64\_t OH\_HiAppEvent\_AddProcessor(HiAppEvent\_Processor\* processor)

**Description**

Adds a processor. You can add a processor to migrate event data to the cloud. You can preset the implementation of the processor on the device and set its properties based on its constraints. Note that the configuration information of **Processor** must be provided by the data processor. Yet, as no data processor is preset in the device for interaction for the moment, migrating events to the cloud is unavailable.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int64\_t | 
Unique ID of the processor is returned when the API is successfully called. The value is greater than 0.

[HIAPPEVENT\_PROCESSOR\_IS\_NULL](#hiappevent_errorcode): The **processor** parameter is empty.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter value.

[HIAPPEVENT\_OPERATE\_FAILED](#hiappevent_errorcode): Failed to find or register the data processor name.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_DestroyProcessor()

void OH\_HiAppEvent\_DestroyProcessor(HiAppEvent\_Processor\* processor)

**Description**

Destroys a processor. Note: If a processor is no longer used, destroy it to release memory to prevent memory leaks. After the processor is destroyed, set its pointer to null.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Processor](../../structs/hiappevent-processor/document.md)\* processor | Pointer to the processor, that is, the pointer returned by **OH\_HiAppEvent\_CreateProcessor**. |

#### \[h2\]OH\_HiAppEvent\_RemoveProcessor()

int OH\_HiAppEvent\_RemoveProcessor(int64\_t processorId)

**Description**

Removes a processor. Once a processor is removed, it stops reporting events. Note: This API only stops the processor reporting events but does not destroy the processor. You can call **OH\_HiAppEvent\_DestroyProcessor** to destroy the processor and release the memory.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t processorId | Unique ID of a processor. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_PROCESSOR\_NOT\_FOUND](#hiappevent_errorcode): Failed to find the processor.

[HIAPPEVENT\_OPERATE\_FAILED](#hiappevent_errorcode): Operation failed.

[HIAPPEVENT\_INVALID\_UID](#hiappevent_errorcode): Invalid user ID.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_CreateConfig()

HiAppEvent\_Config\* OH\_HiAppEvent\_CreateConfig(void)

**Description**

Creates a pointer to the configuration object that sets the conditions for triggering system events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/0cZ93Qj5SsGBfMsfiQx4Xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35B8FDA8EA436466FA56D26BD9BE2ED3F56CF24E936B22568122E6CA90FF6793)

If the created pointer to the configuration object that sets the conditions for triggering system events is no longer used, destroy it by calling [OH\_HiAppEvent\_DestroyConfig](#oh_hiappevent_destroyconfig).

**Since**: 15

**Returns**

| Type | Description |
| :-- | :-- |
| [HiAppEvent\_Config](../../structs/hiappevent-config/document.md)\* | Pointer to the configuration object that sets the conditions for triggering system events. |

#### \[h2\]OH\_HiAppEvent\_DestroyConfig()

void OH\_HiAppEvent\_DestroyConfig(HiAppEvent\_Config\* config)

**Description**

Destroys a configuration object. Note: If a configuration object is no longer used, destroy it to release memory to prevent memory leaks. After the object is destroyed, set its pointer to null.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Config](../../structs/hiappevent-config/document.md)\* config | Pointer to the configuration object, that is, the pointer returned by the **OH\_HiAppEvent\_CreateConfig** API. |

#### \[h2\]OH\_HiAppEvent\_SetConfigItem()

int OH\_HiAppEvent\_SetConfigItem(HiAppEvent\_Config\* config, const char\* itemName, const char\* itemValue)

**Description**

Sets the items in the configuration object.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiAppEvent\_Config](../../structs/hiappevent-config/document.md)\* config | Pointer to the configuration object, that is, the pointer returned by the **OH\_HiAppEvent\_CreateConfig** API. |
| const char\* itemName | Name of the configuration item. |
| const char\* itemValue | Value of the configuration item. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_EVENT\_CONFIG\_IS\_NULL](#hiappevent_errorcode): The input pointer to the configuration object is null.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid configuration item.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |

#### \[h2\]OH\_HiAppEvent\_SetEventConfig()

int OH\_HiAppEvent\_SetEventConfig(const char\* name, HiAppEvent\_Config\* config)

**Description**

Sets event configuration parameters.

Configuration items vary depending on events. Currently, only the following events are supported:

**MAIN\_THREAD\_JANK**. (For details about the parameter configuration, see [Main Thread Jank Event Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events#parameters-of-oh_hiappevent_seteventconfig).)

**MAIN\_THREAD\_JANK\_V2**. (For details about the parameter configuration, see [Main Thread Jank Event Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events#parameters-of-oh_hiappevent_seteventconfig).)

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* name | Name of the system event. |
| [HiAppEvent\_Config](../../structs/hiappevent-config/document.md)\* config | Pointer to the configuration object, that is, the pointer returned by the **OH\_HiAppEvent\_CreateConfig** API. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[HIAPPEVENT\_SUCCESS](#hiappevent_errorcode): Operation successful.

[HIAPPEVENT\_INVALID\_PARAM\_VALUE](#hiappevent_errorcode): Invalid parameter.

For details, see [HiAppEvent\_ErrorCode](#hiappevent_errorcode).

 |
