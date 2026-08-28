# hidebug\_type.h

#### Overview

Defines the structs of the HiDebug module.

**File to include**: <hidebug/hidebug\_type.h>

**Library**: libohhidebug.so

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Since**: 12

**Related module**: [HiDebug](../../modules/hidebug/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiDebug\_ThreadCpuUsage](../../structs/hidebug-threadcpuusage/document.md) | HiDebug\_ThreadCpuUsage | Defines the CPU usage of all threads in an application. |
| [HiDebug\_SystemMemInfo](../../structs/hidebug-systemmeminfo/document.md) | HiDebug\_SystemMemInfo | Defines the system memory information. |
| [HiDebug\_NativeMemInfo](../../structs/hidebug-nativememinfo/document.md) | HiDebug\_NativeMemInfo | Defines the local memory information of an application process. |
| [HiDebug\_MemoryLimit](../../structs/hidebug-memorylimit/document.md) | HiDebug\_MemoryLimit | Defines the memory limit of an application process. |
| [HiDebug\_JsStackFrame](../../structs/hidebug-jsstackframe/document.md) | HiDebug\_JsStackFrame | Defines the JS stack frame content. |
| [HiDebug\_NativeStackFrame](../../structs/hidebug-nativestackframe/document.md) | HiDebug\_NativeStackFrame | Defines the native stack frame content. |
| [HiDebug\_StackFrame](../../structs/hidebug-stackframe/document.md) | HiDebug\_StackFrame | Defines the stack frame content. |
| [HiDebug\_MallocDispatch](../../structs/hidebug-mallocdispatch/document.md) | HiDebug\_MallocDispatch | Defines the struct types of the replaceable/restorable **HiDebug\_MallocDispatch** table of the application process. |
| [HiDebug\_GraphicsMemorySummary](../../structs/hidebug-graphicsmemorysummary/document.md) | HiDebug\_GraphicsMemorySummary | Defines the application graphics memory usage details. |
| [HiDebug\_ProcessSamplerConfig](../../structs/hidebug-processsamplerconfig/document.md) | HiDebug\_ProcessSamplerConfig | Defines the sampling configuration. |
| [HiDebug\_Backtrace\_Object\_\_\*](../../structs/hidebug-backtrace-object/document.md) | HiDebug\_Backtrace\_Object | Defines the object used for stack backtracing and stack parsing. |
| [HiDebug\_ThreadCpuUsage\*](../../structs/hidebug-threadcpuusage/document.md) | HiDebug\_ThreadCpuUsagePtr | Defines the pointer to **HiDebug\_ThreadCpuUsage**. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiDebug\_ErrorCode](#hidebug_errorcode) | HiDebug\_ErrorCode | Enumerates the error codes used in the HiDebug module. |
| [HiDebug\_TraceFlag](#hidebug_traceflag) | HiDebug\_TraceFlag | Enumerates the thread types for trace collection. |
| [HiDebug\_StackFrameType](#hidebug_stackframetype) | HiDebug\_StackFrameType | Enumerates the stack frame types. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [HIDEBUG\_TRACE\_TAG\_FFRT](#hidebug_trace_tag_ffrt) (1ULL << 13) | 
Indicates a function flow runtime (FFRT) task.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_COMMON\_LIBRARY](#hidebug_trace_tag_common_library) (1ULL << 16) | 

Indicates the common library subsystem.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_HDF](#hidebug_trace_tag_hdf) (1ULL << 18) | 

Indicates the HDF subsystem.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_NET](#hidebug_trace_tag_net) (1ULL << 23) | 

Indicates the Network.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_NWEB](#hidebug_trace_tag_nweb) (1ULL << 24) | 

Indicates the NWeb.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_AUDIO](#hidebug_trace_tag_distributed_audio) (1ULL << 27) | 

Indicates the distributed audio.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_FILE\_MANAGEMENT](#hidebug_trace_tag_file_management) (1ULL << 29) | 

Indicates the file management.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_OHOS](#hidebug_trace_tag_ohos) (1ULL << 30) | 

Indicates the HarmonyOS OS.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_ABILITY\_MANAGER](#hidebug_trace_tag_ability_manager) (1ULL << 31) | 

Indicates the Ability Manager.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_CAMERA](#hidebug_trace_tag_camera) (1ULL << 32) | 

Indicates the camera module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_MEDIA](#hidebug_trace_tag_media) (1ULL << 33) | 

Indicates the media module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_IMAGE](#hidebug_trace_tag_image) (1ULL << 34) | 

Indicates the image module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_AUDIO](#hidebug_trace_tag_audio) (1ULL << 35) | 

Indicates the audio module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_DATA](#hidebug_trace_tag_distributed_data) (1ULL << 36) | 

Indicates the distributed data management.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_GRAPHICS](#hidebug_trace_tag_graphics) (1ULL << 38) | 

Indicates the graphics module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_ARKUI](#hidebug_trace_tag_arkui) (1ULL << 39) | 

Indicates the ArkUI development framework.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_NOTIFICATION](#hidebug_trace_tag_notification) (1ULL << 40) | 

Indicates the notification module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_MISC](#hidebug_trace_tag_misc) (1ULL << 41) | 

Indicates the MISC module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_MULTIMODAL\_INPUT](#hidebug_trace_tag_multimodal_input) (1ULL << 42) | 

Indicates the multimodal input module.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_RPC](#hidebug_trace_tag_rpc) (1ULL << 46) | 

Indicates a remote procedure call (RPC).

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_ARK](#hidebug_trace_tag_ark) (1ULL << 47) | 

Indicates a JavaScript virtual machine (JSVM).

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_WINDOW\_MANAGER](#hidebug_trace_tag_window_manager) (1ULL << 48) | 

Indicates the window manager.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCREEN](#hidebug_trace_tag_distributed_screen) (1ULL << 50) | 

Indicates the distributed screen.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_CAMERA](#hidebug_trace_tag_distributed_camera) (1ULL << 51) | 

Indicates the distributed camera.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_FRAMEWORK](#hidebug_trace_tag_distributed_hardware_framework) (1ULL << 52) | 

Indicates the distributed hardware framework.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_GLOBAL\_RESOURCE\_MANAGER](#hidebug_trace_tag_global_resource_manager) (1ULL << 53) | 

Indicates the global resource management.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER](#hidebug_trace_tag_distributed_hardware_device_manager) (1ULL << 54) | 

Indicates the distributed hardware device management.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_SAMGR](#hidebug_trace_tag_samgr) (1ULL << 55) | 

Indicates the Samgr (SA).

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_POWER\_MANAGER](#hidebug_trace_tag_power_manager) (1ULL << 56) | 

Indicates the power manager.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCHEDULER](#hidebug_trace_tag_distributed_scheduler) (1ULL << 57) | 

Indicates the distributed scheduler.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_INPUT](#hidebug_trace_tag_distributed_input) (1ULL << 59) | 

Indicates the distributed input.

**Since**: 12

 |
| [HIDEBUG\_TRACE\_TAG\_BLUETOOTH](#hidebug_trace_tag_bluetooth) (1ULL << 60) | 

Indicates the Bluetooth.

**Since**: 12

 |

#### Enum Description

#### \[h2\]HiDebug\_ErrorCode

enum HiDebug\_ErrorCode

**Description**

Enumerates the error codes used in the HiDebug module.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HIDEBUG\_SUCCESS = 0 | Operation successful. |
| HIDEBUG\_INVALID\_ARGUMENT = 401 | Invalid parameter. Possible causes: 1. The parameter value is incorrect. 2. The parameter type is incorrect. |
| HIDEBUG\_TRACE\_CAPTURED\_ALREADY = 11400102 | Repeated collection. |
| HIDEBUG\_NO\_PERMISSION = 11400103 | No file write permission. |
| HIDEBUG\_TRACE\_ABNORMAL = 11400104 | Internal system error. |
| HIDEBUG\_NO\_TRACE\_RUNNING = 11400105 | No trace task is running. |
| HIDEBUG\_INVALID\_SYMBOLIC\_PC\_ADDRESS = 11400200 | 
PC address passed to the symbol parsing function is invalid.

**Since**: 20

 |
| HIDEBUG\_NOT\_SUPPORTED = 11400300 | 

Current device is not supported.

**Since**: 22

 |
| HIDEBUG\_UNDER\_SAMPLING = 11400301 | 

Current process is being sampled.

**Since**: 22

 |
| HIDEBUG\_RESOURCE\_UNAVAILABLE = 11400302 | 

Sampling resources are unavailable.

**Since**: 22

 |

#### \[h2\]HiDebug\_TraceFlag

enum HiDebug\_TraceFlag

**Description**

Enumerates the thread types for trace collection.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HIDEBUG\_TRACE\_FLAG\_MAIN\_THREAD = 1 | Only the main thread of the current application. |
| HIDEBUG\_TRACE\_FLAG\_ALL\_THREADS = 2 | All threads of the application. |

#### \[h2\]HiDebug\_StackFrameType

enum HiDebug\_StackFrameType

**Description**

Enumerates the stack frame types.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| HIDEBUG\_STACK\_FRAME\_TYPE\_JS = 1 | JS stack frame. |
| HIDEBUG\_STACK\_FRAME\_TYPE\_NATIVE = 2 | Native stack frame. |

#### Macro Description

#### \[h2\]HIDEBUG\_TRACE\_TAG\_FFRT

#define HIDEBUG\_TRACE\_TAG\_FFRT (1ULL << 13)

**Description**

Indicates a function flow runtime (FFRT) task.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_COMMON\_LIBRARY

#define HIDEBUG\_TRACE\_TAG\_COMMON\_LIBRARY (1ULL << 16)

**Description**

Indicates the common library subsystem.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_HDF

#define HIDEBUG\_TRACE\_TAG\_HDF (1ULL << 18)

**Description**

Indicates the HDF subsystem.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_NET

#define HIDEBUG\_TRACE\_TAG\_NET (1ULL << 23)

**Description**

Indicates the Network.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_NWEB

#define HIDEBUG\_TRACE\_TAG\_NWEB (1ULL << 24)

**Description**

Indicates the NWeb.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_AUDIO

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_AUDIO (1ULL << 27)

**Description**

Indicates the distributed audio.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_FILE\_MANAGEMENT

#define HIDEBUG\_TRACE\_TAG\_FILE\_MANAGEMENT (1ULL << 29)

**Description**

Indicates the file management.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_OHOS

#define HIDEBUG\_TRACE\_TAG\_OHOS (1ULL << 30)

**Description**

Indicates the HarmonyOS OS.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_ABILITY\_MANAGER

#define HIDEBUG\_TRACE\_TAG\_ABILITY\_MANAGER (1ULL << 31)

**Description**

Indicates the Ability Manager.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_CAMERA

#define HIDEBUG\_TRACE\_TAG\_CAMERA (1ULL << 32)

**Description**

Indicates the camera module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_MEDIA

#define HIDEBUG\_TRACE\_TAG\_MEDIA (1ULL << 33)

**Description**

Indicates the media module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_IMAGE

#define HIDEBUG\_TRACE\_TAG\_IMAGE (1ULL << 34)

**Description**

Indicates the image module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_AUDIO

#define HIDEBUG\_TRACE\_TAG\_AUDIO (1ULL << 35)

**Description**

Indicates the audio module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_DATA

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_DATA (1ULL << 36)

**Description**

Indicates the distributed data management.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_GRAPHICS

#define HIDEBUG\_TRACE\_TAG\_GRAPHICS (1ULL << 38)

**Description**

Indicates the graphics module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_ARKUI

#define HIDEBUG\_TRACE\_TAG\_ARKUI (1ULL << 39)

**Description**

Indicates the ArkUI development framework.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_NOTIFICATION

#define HIDEBUG\_TRACE\_TAG\_NOTIFICATION (1ULL << 40)

**Description**

Indicates the notification module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_MISC

#define HIDEBUG\_TRACE\_TAG\_MISC (1ULL << 41)

**Description**

Indicates the MISC module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_MULTIMODAL\_INPUT

#define HIDEBUG\_TRACE\_TAG\_MULTIMODAL\_INPUT (1ULL << 42)

**Description**

Indicates the multimodal input module.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_RPC

#define HIDEBUG\_TRACE\_TAG\_RPC (1ULL << 46)

**Description**

Indicates a remote procedure call (RPC).

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_ARK

#define HIDEBUG\_TRACE\_TAG\_ARK (1ULL << 47)

**Description**

Indicates a JavaScript virtual machine (JSVM).

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_WINDOW\_MANAGER

#define HIDEBUG\_TRACE\_TAG\_WINDOW\_MANAGER (1ULL << 48)

**Description**

Indicates the window manager.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCREEN

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCREEN (1ULL << 50)

**Description**

Indicates the distributed screen.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_CAMERA

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_CAMERA (1ULL << 51)

**Description**

Indicates the distributed camera.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_FRAMEWORK

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_FRAMEWORK (1ULL << 52)

**Description**

Indicates the distributed hardware framework.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_GLOBAL\_RESOURCE\_MANAGER

#define HIDEBUG\_TRACE\_TAG\_GLOBAL\_RESOURCE\_MANAGER (1ULL << 53)

**Description**

Indicates the global resource management.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER (1ULL << 54)

**Description**

Indicates the distributed hardware device management.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_SAMGR

#define HIDEBUG\_TRACE\_TAG\_SAMGR (1ULL << 55)

**Description**

Indicates the Samgr (SA).

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_POWER\_MANAGER

#define HIDEBUG\_TRACE\_TAG\_POWER\_MANAGER (1ULL << 56)

**Description**

Indicates the power manager.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCHEDULER

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_SCHEDULER (1ULL << 57)

**Description**

Indicates the distributed scheduler.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_INPUT

#define HIDEBUG\_TRACE\_TAG\_DISTRIBUTED\_INPUT (1ULL << 59)

**Description**

Indicates the distributed input.

**Since**: 12

#### \[h2\]HIDEBUG\_TRACE\_TAG\_BLUETOOTH

#define HIDEBUG\_TRACE\_TAG\_BLUETOOTH (1ULL << 60)

**Description**

Indicates the Bluetooth.

**Since**: 12
