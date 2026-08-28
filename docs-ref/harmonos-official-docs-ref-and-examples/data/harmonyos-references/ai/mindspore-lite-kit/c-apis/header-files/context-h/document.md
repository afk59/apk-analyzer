# context.h

#### Overview

Provides context-related APIs for configuring runtime information. These APIs are non-thread-safe.

**File to include**: <mindspore/context.h>

**Library**: libmindspore\_lite\_ndk.so

**System capability**: SystemCapability.Ai.MindSpore

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) | void\* | Defines the pointer to the MindSpore Lite context. |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) | void\* | Defines the pointer to the MindSpore Lite device information. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AI\_API OH\_AI\_ContextHandle OH\_AI\_ContextCreate()](#oh_ai_contextcreate) | Creates a context object. This API must be used together with **OH\_AI\_ContextDestroy**. |
| [OH\_AI\_API void OH\_AI\_ContextDestroy(OH\_AI\_ContextHandle \*context)](#oh_ai_contextdestroy) | Destroys a context object. |
| [OH\_AI\_API void OH\_AI\_ContextSetThreadNum(OH\_AI\_ContextHandle context, int32\_t thread\_num)](#oh_ai_contextsetthreadnum) | Sets the number of runtime threads. |
| [OH\_AI\_API int32\_t OH\_AI\_ContextGetThreadNum(const OH\_AI\_ContextHandle context)](#oh_ai_contextgetthreadnum) | Obtains the number of threads. |
| [OH\_AI\_API void OH\_AI\_ContextSetThreadAffinityMode(OH\_AI\_ContextHandle context, int mode)](#oh_ai_contextsetthreadaffinitymode) | Sets the affinity mode for binding runtime threads to CPU cores, which are classified into large, medium, and small cores based on the CPU frequency. You only need to bind the large or medium cores, but not small cores. |
| [OH\_AI\_API int OH\_AI\_ContextGetThreadAffinityMode(const OH\_AI\_ContextHandle context)](#oh_ai_contextgetthreadaffinitymode) | Obtains the affinity mode for binding runtime threads to CPU cores. |
| [OH\_AI\_API void OH\_AI\_ContextSetThreadAffinityCoreList(OH\_AI\_ContextHandle context, const int32\_t \*core\_list,size\_t core\_num)](#oh_ai_contextsetthreadaffinitycorelist) | 
Sets the list of CPU cores bound to a runtime thread.

For example, if **core\_list** is set to **\[2,6,8\]**, threads run on the 2nd, 6th, and 8th CPU cores.

If [OH\_AI\_ContextSetThreadAffinityMode](#oh_ai_contextsetthreadaffinitymode) and [OH\_AI\_ContextSetThreadAffinityCoreList](#oh_ai_contextsetthreadaffinitycorelist) are called for the same context object,

the **core\_list** parameter of [OH\_AI\_ContextSetThreadAffinityCoreList](#oh_ai_contextsetthreadaffinitycorelist) takes effect, but the **mode** parameter of [OH\_AI\_ContextSetThreadAffinityMode](#oh_ai_contextsetthreadaffinitymode) does not.

 |
| [OH\_AI\_API const int32\_t \*OH\_AI\_ContextGetThreadAffinityCoreList(const OH\_AI\_ContextHandle context, size\_t \*core\_num)](#oh_ai_contextgetthreadaffinitycorelist) | Obtains the list of bound CPU cores. |
| [OH\_AI\_API void OH\_AI\_ContextSetEnableParallel(OH\_AI\_ContextHandle context, bool is\_parallel)](#oh_ai_contextsetenableparallel) | Sets whether to enable parallelism between operators. The setting is ineffective because the feature of this API is not yet available. |
| [OH\_AI\_API bool OH\_AI\_ContextGetEnableParallel(const OH\_AI\_ContextHandle context)](#oh_ai_contextgetenableparallel) | Checks whether parallelism between operators is supported. |
| [OH\_AI\_API void OH\_AI\_ContextAddDeviceInfo(OH\_AI\_ContextHandle context, OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_contextadddeviceinfo) | Attaches the custom device information to the inference context. |
| [OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_DeviceInfoCreate(OH\_AI\_DeviceType device\_type)](#oh_ai_deviceinfocreate) | Creates a device information object. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoDestroy(OH\_AI\_DeviceInfoHandle \*device\_info)](#oh_ai_deviceinfodestroy) | Destroys a device information object. Note: After the device information instance is added to the context, the caller does not need to destroy it manually. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetProvider(OH\_AI\_DeviceInfoHandle device\_info, const char \*provider)](#oh_ai_deviceinfosetprovider) | Sets the name of the provider. |
| [OH\_AI\_API const char \*OH\_AI\_DeviceInfoGetProvider(const OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_deviceinfogetprovider) | Obtains the provider name. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetProviderDevice(OH\_AI\_DeviceInfoHandle device\_info, const char \*device)](#oh_ai_deviceinfosetproviderdevice) | Sets the name of a provider device. |
| [OH\_AI\_API const char \*OH\_AI\_DeviceInfoGetProviderDevice(const OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_deviceinfogetproviderdevice) | Obtains the name of a provider device. |
| [OH\_AI\_API OH\_AI\_DeviceType OH\_AI\_DeviceInfoGetDeviceType(const OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_deviceinfogetdevicetype) | Obtains the device type. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetEnableFP16(OH\_AI\_DeviceInfoHandle device\_info, bool is\_fp16)](#oh_ai_deviceinfosetenablefp16) | Sets whether to enable float16 inference. This function is available only for CPU and GPU devices. |
| [OH\_AI\_API bool OH\_AI\_DeviceInfoGetEnableFP16(const OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_deviceinfogetenablefp16) | Checks whether float16 inference is enabled. This function is available only for CPU and GPU devices. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetFrequency(OH\_AI\_DeviceInfoHandle device\_info, int frequency)](#oh_ai_deviceinfosetfrequency) | Sets the NPU frequency type. This function is available only for NPU devices. |
| [OH\_AI\_API int OH\_AI\_DeviceInfoGetFrequency(const OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_deviceinfogetfrequency) | Obtains the NPU frequency type. This function is available only for NPU devices. |
| [OH\_AI\_API NNRTDeviceDesc \*OH\_AI\_GetAllNNRTDeviceDescs(size\_t \*num)](#oh_ai_getallnnrtdevicedescs) | Obtains the descriptions of all NNRt devices in the system. |
| [OH\_AI\_API NNRTDeviceDesc \*OH\_AI\_GetElementOfNNRTDeviceDescs(NNRTDeviceDesc \*descs, size\_t index)](#oh_ai_getelementofnnrtdevicedescs) | Obtains the pointer to an element in the NNRt device description array. |
| [OH\_AI\_API void OH\_AI\_DestroyAllNNRTDeviceDescs(NNRTDeviceDesc \*\*desc)](#oh_ai_destroyallnnrtdevicedescs) | Destroys the NNRt device description array obtained by [OH\_AI\_GetAllNNRTDeviceDescs](#oh_ai_getallnnrtdevicedescs). |
| [OH\_AI\_API size\_t OH\_AI\_GetDeviceIdFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)](#oh_ai_getdeviceidfromnnrtdevicedesc) | Obtains the NNRt device ID from the specified NNRt device description. Note that this ID is valid only for NNRt devices. |
| [OH\_AI\_API const char \*OH\_AI\_GetNameFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)](#oh_ai_getnamefromnnrtdevicedesc) | Obtains the NNRt device name from the specified NNRt device description. |
| [OH\_AI\_API OH\_AI\_NNRTDeviceType OH\_AI\_GetTypeFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)](#oh_ai_gettypefromnnrtdevicedesc) | Obtains the NNRt device type from the specified NNRt device description. |
| [OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_CreateNNRTDeviceInfoByName(const char \*name)](#oh_ai_creatennrtdeviceinfobyname) | Searches for the NNRt device with the specified name and creates the NNRt device information based on the information about the first found NNRt device. |
| [OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_CreateNNRTDeviceInfoByType(OH\_AI\_NNRTDeviceType type)](#oh_ai_creatennrtdeviceinfobytype) | Searches for the NNRt device with the specified type and creates the NNRt device information based on the information about the first found NNRt device. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetDeviceId(OH\_AI\_DeviceInfoHandle device\_info, size\_t device\_id)](#oh_ai_deviceinfosetdeviceid) | Sets the NNRt device ID. This function is available only for NNRt devices. |
| [OH\_AI\_API size\_t OH\_AI\_DeviceInfoGetDeviceId(const OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_deviceinfogetdeviceid) | Obtains the NNRt device ID. This function is available only for NNRt devices. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetPerformanceMode(OH\_AI\_DeviceInfoHandle device\_info, OH\_AI\_PerformanceMode mode)](#oh_ai_deviceinfosetperformancemode) | Sets the NNRt performance mode. This function is available only for NNRt devices. |
| [OH\_AI\_API OH\_AI\_PerformanceMode OH\_AI\_DeviceInfoGetPerformanceMode(const OH\_AI\_DeviceInfoHandle device\_info)](#oh_ai_deviceinfogetperformancemode) | Obtains the NNRt performance mode. This function is available only for NNRt devices. |
| [OH\_AI\_API void OH\_AI\_DeviceInfoSetPriority(OH\_AI\_DeviceInfoHandle device\_info, OH\_AI\_Priority priority)](#oh_ai_deviceinfosetpriority) | Sets the priority of an NNRt task. This function is available only for NNRt devices. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_DeviceInfoAddExtension(OH\_AI\_DeviceInfoHandle device\_info, const char \*name,const char \*value, size\_t value\_size)](#oh_ai_deviceinfoaddextension) | 

Adds extended configuration in the form of key/value pairs to the device information. This function is available only for NNRt devices.

Currently, only the following 11 keys are supported: {"CachePath": "YourCachePath"}, {"CacheVersion": "YourCacheVersion"}, {"QuantBuffer": "YourQuantBuffer"}, {"ModelName": "YourModelName"}, {"isProfiling": "YourProfilingSwitch"}, {"opLayout": "YourOpLayout"}, {"InputDims": "YourInputDims"}, {"DynamicDims": "YourDynamicDims"}, {"QuantConfigData": "YourQuantConfigData"}, {"BandMode": "YourBandMode"}, and {"NPU\_FM\_SHARED": "YourNPU\_FM\_SHARED"}. You can configure the value of each key based on the actual requirement.

 |

#### Function Description

#### \[h2\]OH\_AI\_ContextCreate()

OH\_AI\_API OH\_AI\_ContextHandle OH\_AI\_ContextCreate()

**Description**

Creates a context object. This API must be used together with **OH\_AI\_ContextDestroy**.

**Since**: 9

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context. |

#### \[h2\]OH\_AI\_ContextDestroy()

OH\_AI\_API void OH\_AI\_ContextDestroy(OH\_AI\_ContextHandle \*context)

**Description**

Destroys a context object.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) \*context | Level-2 pointer to [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md). After the context is destroyed, the context is set to a null pointer. |

#### \[h2\]OH\_AI\_ContextSetThreadNum()

OH\_AI\_API void OH\_AI\_ContextSetThreadNum(OH\_AI\_ContextHandle context, int32\_t thread\_num)

**Description**

Sets the number of runtime threads.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |
| int32\_t thread\_num | Number of runtime threads. The length is subject to system restrictions. |

#### \[h2\]OH\_AI\_ContextGetThreadNum()

OH\_AI\_API int32\_t OH\_AI\_ContextGetThreadNum(const OH\_AI\_ContextHandle context)

**Description**

Obtains the number of threads.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API int32\_t | Number of threads. |

#### \[h2\]OH\_AI\_ContextSetThreadAffinityMode()

OH\_AI\_API void OH\_AI\_ContextSetThreadAffinityMode(OH\_AI\_ContextHandle context, int mode)

**Description**

Sets the affinity mode for binding runtime threads to CPU cores, which are classified into large, medium, and small cores based on the CPU frequency. You only need to bind the large or medium cores, but not small cores.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |
| int mode | Affinity mode. **0**: no affinities; **1**: big cores first; **2**: medium cores first |

#### \[h2\]OH\_AI\_ContextGetThreadAffinityMode()

OH\_AI\_API int OH\_AI\_ContextGetThreadAffinityMode(const OH\_AI\_ContextHandle context)

**Description**

Obtains the affinity mode for binding runtime threads to CPU cores.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API int | Affinity mode. **0**: no affinities; **1**: big cores first; **2**: medium cores first |

#### \[h2\]OH\_AI\_ContextSetThreadAffinityCoreList()

OH\_AI\_API void OH\_AI\_ContextSetThreadAffinityCoreList(OH\_AI\_ContextHandle context, const int32\_t \*core\_list,size\_t core\_num)

**Description**

Sets the list of CPU cores bound to a runtime thread.

For example, if **core\_list** is set to **\[2,6,8\]**, threads run on the 2nd, 6th, and 8th CPU cores.

If [OH\_AI\_ContextSetThreadAffinityMode](#oh_ai_contextsetthreadaffinitymode) and [OH\_AI\_ContextSetThreadAffinityCoreList](#oh_ai_contextsetthreadaffinitycorelist) are called for the same context object,

the **core\_list** parameter of [OH\_AI\_ContextSetThreadAffinityCoreList](#oh_ai_contextsetthreadaffinitycorelist) takes effect, but the **mode** parameter of [OH\_AI\_ContextSetThreadAffinityMode](#oh_ai_contextsetthreadaffinitymode) does not.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |
| const int32\_t \*core\_list | List of bound CPU cores. |
| size\_t core\_num | Number of cores, which indicates the length of **core\_list**. |

#### \[h2\]OH\_AI\_ContextGetThreadAffinityCoreList()

OH\_AI\_API const int32\_t \*OH\_AI\_ContextGetThreadAffinityCoreList(const OH\_AI\_ContextHandle context, size\_t \*core\_num)

**Description**

Obtains the list of bound CPU cores.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |
| size\_t \*core\_num | Number of CPU cores. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API const int32\_t \* | List of bound CPU cores. This list is managed by [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md). The caller does not need to destroy it manually. |

#### \[h2\]OH\_AI\_ContextSetEnableParallel()

OH\_AI\_API void OH\_AI\_ContextSetEnableParallel(OH\_AI\_ContextHandle context, bool is\_parallel)

**Description**

Sets whether to enable parallelism between operators. The setting is ineffective because the feature of this API is not yet available.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |
| bool is\_parallel | Whether parallelism between operators is supported. The value **true** indicates that parallelism between operators is supported, and the value **false** indicates the opposite. |

#### \[h2\]OH\_AI\_ContextGetEnableParallel()

OH\_AI\_API bool OH\_AI\_ContextGetEnableParallel(const OH\_AI\_ContextHandle context)

**Description**

Checks whether parallelism between operators is supported.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API bool | Whether parallelism between operators is supported. The value **true** indicates that parallelism between operators is supported, and the value **false** indicates the opposite. |

#### \[h2\]OH\_AI\_ContextAddDeviceInfo()

OH\_AI\_API void OH\_AI\_ContextAddDeviceInfo(OH\_AI\_ContextHandle context, OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Attaches the custom device information to the inference context.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) context | [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) that points to the context instance. |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

#### \[h2\]OH\_AI\_DeviceInfoCreate()

OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_DeviceInfoCreate(OH\_AI\_DeviceType device\_type)

**Description**

Creates a device information object.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceType](../types-h/document.md#oh_ai_devicetype) device\_type | Device type, which is specified by [OH\_AI\_DeviceType](../types-h/document.md#oh_ai_devicetype). |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

#### \[h2\]OH\_AI\_DeviceInfoDestroy()

OH\_AI\_API void OH\_AI\_DeviceInfoDestroy(OH\_AI\_DeviceInfoHandle \*device\_info)

**Description**

Destroys a device information object. Note: After the device information instance is added to the context, the caller does not need to destroy it manually.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) \*device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

#### \[h2\]OH\_AI\_DeviceInfoSetProvider()

OH\_AI\_API void OH\_AI\_DeviceInfoSetProvider(OH\_AI\_DeviceInfoHandle device\_info, const char \*provider)

**Description**

Sets the name of the provider.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| const char \*provider | Provider name. The string length is subject to system restrictions. |

#### \[h2\]OH\_AI\_DeviceInfoGetProvider()

OH\_AI\_API const char \*OH\_AI\_DeviceInfoGetProvider(const OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Obtains the provider name.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API const char \* | Provider name. |

#### \[h2\]OH\_AI\_DeviceInfoSetProviderDevice()

OH\_AI\_API void OH\_AI\_DeviceInfoSetProviderDevice(OH\_AI\_DeviceInfoHandle device\_info, const char \*device)

**Description**

Sets the name of a provider device.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| const char \*device | Name of the provider device, for example, CPU. The string length is subject to system restrictions. |

#### \[h2\]OH\_AI\_DeviceInfoGetProviderDevice()

OH\_AI\_API const char \*OH\_AI\_DeviceInfoGetProviderDevice(const OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Obtains the name of a provider device.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API const char \* | Name of the provider device. |

#### \[h2\]OH\_AI\_DeviceInfoGetDeviceType()

OH\_AI\_API OH\_AI\_DeviceType OH\_AI\_DeviceInfoGetDeviceType(const OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Obtains the device type.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_DeviceType](../types-h/document.md#oh_ai_devicetype) | Type of the provider device. |

#### \[h2\]OH\_AI\_DeviceInfoSetEnableFP16()

OH\_AI\_API void OH\_AI\_DeviceInfoSetEnableFP16(OH\_AI\_DeviceInfoHandle device\_info, bool is\_fp16)

**Description**

Sets whether to enable float16 inference. This function is available only for CPU and GPU devices.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| bool is\_fp16 | Whether to enable the float16 inference mode. The value **true** means to enable the float16 inference mode, and the value **false** means the opposite. |

#### \[h2\]OH\_AI\_DeviceInfoGetEnableFP16()

OH\_AI\_API bool OH\_AI\_DeviceInfoGetEnableFP16(const OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Checks whether float16 inference is enabled. This function is available only for CPU and GPU devices.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API bool | Whether to enable the float16 inference mode. The value **true** means to enable the float16 inference mode, and the value **false** means the opposite. |

#### \[h2\]OH\_AI\_DeviceInfoSetFrequency()

OH\_AI\_API void OH\_AI\_DeviceInfoSetFrequency(OH\_AI\_DeviceInfoHandle device\_info, int frequency)

**Description**

Sets the NPU frequency type. This function is available only for NPU devices.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| int frequency | NPU frequency type. The value ranges from **0** to **4**. The default value is **3**. Meanings of each value: **0**: auto system adjustment; **1**: low power consumption; **2**: balanced; **3**: high performance; **4**: ultra-high performance. |

#### \[h2\]OH\_AI\_DeviceInfoGetFrequency()

OH\_AI\_API int OH\_AI\_DeviceInfoGetFrequency(const OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Obtains the NPU frequency type. This function is available only for NPU devices.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API int | NPU frequency type. Meanings of each value: **0**: auto system adjustment; **1**: low power consumption; **2**: balanced; **3**: high performance; **4**: ultra-high performance. |

#### \[h2\]OH\_AI\_GetAllNNRTDeviceDescs()

OH\_AI\_API NNRTDeviceDesc \*OH\_AI\_GetAllNNRTDeviceDescs(size\_t \*num)

**Description**

Obtains the descriptions of all NNRt devices in the system.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t \*num | Number of NNRt devices. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) \* | Pointer to the NNRt device description array. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_AI\_GetElementOfNNRTDeviceDescs()

OH\_AI\_API NNRTDeviceDesc \*OH\_AI\_GetElementOfNNRTDeviceDescs(NNRTDeviceDesc \*descs, size\_t index)

**Description**

Obtains the pointer to an element in the NNRt device description array.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) \*descs | NNRt device description array. |
| size\_t index | Index of an array element. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) \* | Pointer to the NNRt device description. |

#### \[h2\]OH\_AI\_DestroyAllNNRTDeviceDescs()

OH\_AI\_API void OH\_AI\_DestroyAllNNRTDeviceDescs(NNRTDeviceDesc \*\*desc)

**Description**

Destroys the NNRt device description array obtained by [OH\_AI\_GetAllNNRTDeviceDescs](#oh_ai_getallnnrtdevicedescs).

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) \*\*desc | Double pointer to the NNRt device description array. After the operation is complete, the content pointed to by **desc** is set to **NULL**. |

#### \[h2\]OH\_AI\_GetDeviceIdFromNNRTDeviceDesc()

OH\_AI\_API size\_t OH\_AI\_GetDeviceIdFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)

**Description**

Obtains the NNRt device ID from the specified NNRt device description. Note that this ID is valid only for NNRt devices.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) \*desc | Pointer to the NNRt device description. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API size\_t | NNRt device ID. |

#### \[h2\]OH\_AI\_GetNameFromNNRTDeviceDesc()

OH\_AI\_API const char \*OH\_AI\_GetNameFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)

**Description**

Obtains the NNRt device name from the specified NNRt device description.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) \*desc | Pointer to the NNRt device description. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API const char \* | NNRt device name. The value is a pointer that points to a constant string, which is held by **desc**. The caller does not need to destroy it separately. |

#### \[h2\]OH\_AI\_GetTypeFromNNRTDeviceDesc()

OH\_AI\_API OH\_AI\_NNRTDeviceType OH\_AI\_GetTypeFromNNRTDeviceDesc(const NNRTDeviceDesc \*desc)

**Description**

Obtains the NNRt device type from the specified NNRt device description.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) \*desc | Pointer to the NNRt device description. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_NNRTDeviceType](../types-h/document.md#oh_ai_nnrtdevicetype) | NNRt device type, which is specified by [OH\_AI\_NNRTDeviceType](../types-h/document.md#oh_ai_nnrtdevicetype). |

#### \[h2\]OH\_AI\_CreateNNRTDeviceInfoByName()

OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_CreateNNRTDeviceInfoByName(const char \*name)

**Description**

Searches for the NNRt device with the specified name and creates the NNRt device information based on the information about the first found NNRt device.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Name of the target NNRt device. The string length is subject to system restrictions. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

#### \[h2\]OH\_AI\_CreateNNRTDeviceInfoByType()

OH\_AI\_API OH\_AI\_DeviceInfoHandle OH\_AI\_CreateNNRTDeviceInfoByType(OH\_AI\_NNRTDeviceType type)

**Description**

Searches for the NNRt device with the specified type and creates the NNRt device information based on the information about the first found NNRt device.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_NNRTDeviceType](../types-h/document.md#oh_ai_nnrtdevicetype) type | NNRt device type, which is specified by [OH\_AI\_NNRTDeviceType](../types-h/document.md#oh_ai_nnrtdevicetype). |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

#### \[h2\]OH\_AI\_DeviceInfoSetDeviceId()

OH\_AI\_API void OH\_AI\_DeviceInfoSetDeviceId(OH\_AI\_DeviceInfoHandle device\_info, size\_t device\_id)

**Description**

Sets the NNRt device ID. This function is available only for NNRt devices.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| size\_t device\_id | NNRt device ID. |

#### \[h2\]OH\_AI\_DeviceInfoGetDeviceId()

OH\_AI\_API size\_t OH\_AI\_DeviceInfoGetDeviceId(const OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Obtains the NNRt device ID. This function is available only for NNRt devices.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API size\_t | NNRt device ID. |

#### \[h2\]OH\_AI\_DeviceInfoSetPerformanceMode()

OH\_AI\_API void OH\_AI\_DeviceInfoSetPerformanceMode(OH\_AI\_DeviceInfoHandle device\_info, OH\_AI\_PerformanceMode mode)

**Description**

Sets the NNRt performance mode. This function is available only for NNRt devices.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| [OH\_AI\_PerformanceMode](../types-h/document.md#oh_ai_performancemode) mode | NNRt performance mode, which is specified by [OH\_AI\_PerformanceMode](../types-h/document.md#oh_ai_performancemode). |

#### \[h2\]OH\_AI\_DeviceInfoGetPerformanceMode()

OH\_AI\_API OH\_AI\_PerformanceMode OH\_AI\_DeviceInfoGetPerformanceMode(const OH\_AI\_DeviceInfoHandle device\_info)

**Description**

Obtains the NNRt performance mode. This function is available only for NNRt devices.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_PerformanceMode](../types-h/document.md#oh_ai_performancemode) | NNRt performance mode, which is specified by [OH\_AI\_PerformanceMode](../types-h/document.md#oh_ai_performancemode). |

#### \[h2\]OH\_AI\_DeviceInfoSetPriority()

OH\_AI\_API void OH\_AI\_DeviceInfoSetPriority(OH\_AI\_DeviceInfoHandle device\_info, OH\_AI\_Priority priority)

**Description**

Sets the priority of an NNRt task. This function is available only for NNRt devices.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| [OH\_AI\_Priority](../types-h/document.md#oh_ai_priority) priority | NNRt task priority, which is specified by [OH\_AI\_Priority](../types-h/document.md#oh_ai_priority). |

#### \[h2\]OH\_AI\_DeviceInfoAddExtension()

OH\_AI\_API OH\_AI\_Status OH\_AI\_DeviceInfoAddExtension(OH\_AI\_DeviceInfoHandle device\_info, const char \*name,const char \*value, size\_t value\_size)

**Description**

Adds extended configuration in the form of key/value pairs to the device information. This function is available only for NNRt devices.

Currently, only the following 11 keys are supported: {"CachePath": "YourCachePath"}, {"CacheVersion": "YourCacheVersion"}, {"QuantBuffer": "YourQuantBuffer"}, {"ModelName": "YourModelName"}, {"isProfiling": "YourProfilingSwitch"}, {"opLayout": "YourOpLayout"}, {"InputDims": "YourInputDims"}, {"DynamicDims": "YourDynamicDims"}, {"QuantConfigData": "YourQuantConfigData"}, {"BandMode": "YourBandMode"}, and {"NPU\_FM\_SHARED": "YourNPU\_FM\_SHARED"}. You can configure the value of each key based on the actual requirement.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) device\_info | [OH\_AI\_DeviceInfoHandle](../../structs/oh-ai-deviceinfohandle/document.md) that points to the device information instance. |
| const char \*name | Key in an extended key/value pair. The value is a C string. The value contains up to 128 characters. |
| const char \*value | Start address of the value in an extended key/value pair. The string length is subject to system restrictions. |
| size\_t value\_size | Length of the value in an extended key/value pair. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |
