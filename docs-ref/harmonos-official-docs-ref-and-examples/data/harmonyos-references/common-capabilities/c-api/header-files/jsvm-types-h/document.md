# jsvm\_types.h

#### Overview

Defines JSVM-API types. JSVM-API is used to provide independent, standard, and complete JS engine capabilities, including managing the engine lifecycle, compiling and running JS code, implementing JS/C++ cross-language calls, and taking snapshots.

**File to import**: <ark\_runtime/jsvm\_types.h>

**Library**: libjsvm.so

**System capability**: SystemCapability.ArkCompiler.JSVM

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [JSVM\_CallbackStruct](../../structs/jsvm-callbackstruct/document.md) | JSVM\_CallbackStruct | Defines the pointer to the data of the native callbacks provided by the user. These functions are exposed to JavaScript via JSVM-API. |
| [JSVM\_HeapStatistics](../../structs/jsvm-heapstatistics/document.md) | JSVM\_HeapStatistics | Stores statistics about JavaScript heap memory usage. |
| [JSVM\_InitOptions](../../structs/jsvm-initoptions/document.md) | JSVM\_InitOptions | Defines options for initializing a JavaScript VM. |
| [JSVM\_CreateVMOptions](../../structs/jsvm-createvmoptions/document.md) | JSVM\_CreateVMOptions | Defines options for creating a JavaScript VM. |
| [JSVM\_VMInfo](../../structs/jsvm-vminfo/document.md) | JSVM\_VMInfo | Defines JavaScript VM information. |
| [JSVM\_PropertyDescriptor](../../structs/jsvm-propertydescriptor/document.md) | JSVM\_PropertyDescriptor | Defines property descriptor. |
| [JSVM\_ExtendedErrorInfo](../../structs/jsvm-extendederrorinfo/document.md) | JSVM\_ExtendedErrorInfo | Defines extended error information. |
| [JSVM\_TypeTag](../../structs/jsvm-typetag/document.md) | JSVM\_TypeTag | Defines the type tag, which is stored as a 128-bit value of two unsigned 64-bit integers. As a UUID, it can tag JavaScript objects to ensure that their types remain unchanged. |
| [JSVM\_PropertyHandlerConfigurationStruct](../../structs/jsvm-propertyhandlerconfigurationstruct/document.md) | JSVM\_PropertyHandlerConfigurationStruct | Defines a struct for triggering the corresponding callback when the getter, setter, deleter, or enumerator of an object is executed. |
| [JSVM\_ScriptOrigin](../../structs/jsvm-scriptorigin/document.md) | JSVM\_ScriptOrigin | Defines the original information about a JavaScript code segment, such as the source map path, source file name, and start line/column number in the source file. |
| [JSVM\_CompileOptions](../../structs/jsvm-compileoptions/document.md) | JSVM\_CompileOptions | JSVM compilation options, which includes the content and ID. |
| [JSVM\_CodeCache](../../structs/jsvm-codecache/document.md) | JSVM\_CodeCache | Address and size of the JSVM code cache. |
| [JSVM\_PropertyHandler](../../structs/jsvm-propertyhandler/document.md) | JSVM\_PropertyHandler | Defines the pointer to the callback function triggered when a class is called as a function, and the pointer collection of the callback function triggered when an instance object property is accessed. |
| [JSVM\_DefineClassOptions](../../structs/jsvm-defineclassoptions/document.md) | JSVM\_DefineClassOptions | Defines class options. |
| [JSVM\_VM\_\_\*](../../structs/jsvm-vm/document.md) | JSVM\_VM | Defines a JavaScript VM instance. |
| [JSVM\_VMScope\_\_\*](../../structs/jsvm-vmscope/document.md) | JSVM\_VMScope | Defines the JavaScript VM scope. |
| [JSVM\_EnvScope\_\_\*](../../structs/jsvm-envscope/document.md) | JSVM\_EnvScope | Defines the environment scope of the current VM instance. The environment is available to the VM instance of the thread only after the thread enters **JSVM\_EnvScope** of the environment through **OH\_JSVM\_OpenEnvScope**. |
| [JSVM\_Script\_\_\*](../../structs/jsvm-script/document.md) | JSVM\_Script | Defines the JavaScript code. |
| [JSVM\_Env\_\_\*](../../structs/jsvm-env/document.md) | JSVM\_Env | Defines the context of a specific VM state. It needs to be passed as a parameter when the native function is called and passed to any subsequent JSVM-API nested call. |
| [JSVM\_CpuProfiler\_\_\*](../../structs/jsvm-cpuprofiler/document.md) | JSVM\_CpuProfiler | Defines a JavaScript CPU profiler. |
| [JSVM\_Value\_\_\*](../../structs/jsvm-value/document.md) | JSVM\_Value | Defines the JavaScript value. |
| [JSVM\_Data\_\_\*](../../structs/jsvm-data/document.md) | JSVM\_Data | Defines the JavaScript data. |
| [JSVM\_Ref\_\_\*](../../structs/jsvm-ref/document.md) | JSVM\_Ref | Defines the reference to the JavaScript value. |
| [JSVM\_HandleScope\_\_\*](../../structs/jsvm-handlescope/document.md) | JSVM\_HandleScope | Defines the scope of the JavaScript value. It is used to control and modify the lifecycle of an object created in a specific scope. Typically, the JSVM-API value is created in the context of **JSVM\_HandleScope**. When the native method is called from JavaScript, the default **JSVM\_HandleScope** exists. If the user does not explicitly create a new **JSVM\_HandleScope**, the JSVM-API value is created in the default **JSVM\_HandleScope**. For any code call other than native method execution (for example, libuv callback), the module needs to create a scope before calling any function that may create a JavaScript value. **JSVM\_HandleScope** is created using **OH\_JSVM\_OpenHandleScope** and destroyed using **OH\_JSVM\_CloseHandleScope**. Closing the scope indicates to the GC that all **JSVM\_Values** created during the lifecycle of **JSVM\_HandleScope** will no longer be referenced from the stack frame of the current heap. |
| [JSVM\_EscapableHandleScope\_\_\*](../../structs/jsvm-escapablehandlescope/document.md) | JSVM\_EscapableHandleScope | Defines a special type of handle scope, which is used to return the value created in a specific handle scope to the parent scope. |
| [JSVM\_CallbackInfo\_\_\*](../../structs/jsvm-callbackinfo/document.md) | JSVM\_CallbackInfo | Defines an opaque data type passed to the callback. It can be used to obtain additional information about the context in which the function is called. |
| [JSVM\_Deferred\_\_\*](../../structs/jsvm-deferred/document.md) | JSVM\_Deferred | Defines the deferred object. |
| [JSVM\_PropertyHandlerConfigurationStruct\*](../../structs/jsvm-propertyhandlerconfigurationstruct--00020177/document.md) | JSVM\_PropertyHandlerCfg | Defines the pointer type of the struct that contains the property handler. |
| [JSVM\_CallbackStruct\*](../../structs/jsvm-callbackstruct--00020177/document.md) | JSVM\_Callback | Defines the pointer types of the native functions provided by user. These functions are exposed to JavaScript via JSVM-API. |
| [JSVM\_CompileProfile](../../structs/jsvm-compileprofile/document.md) | JSVM\_CompileProfile | Defines the compilation sampling file transferred together with **JSVM\_COMPILE\_COMPILE\_PROFILE**. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [JSVM\_PropertyAttributes](#jsvm_propertyattributes) | JSVM\_PropertyAttributes | Enumerates the behaviors of controlling JavaScript object properties. |
| [JSVM\_ValueType](#jsvm_valuetype) | JSVM\_ValueType | Enumerates **JSVM\_Value** types. |
| [JSVM\_TypedarrayType](#jsvm_typedarraytype) | JSVM\_TypedarrayType | Enumerates **TypedArray** types. |
| [JSVM\_Status](#jsvm_status) | JSVM\_Status | Enumerates complete status codes indicating whether the JSVM-API call is successful or failed. |
| [JSVM\_KeyCollectionMode](#jsvm_keycollectionmode) | JSVM\_KeyCollectionMode | Enumerates ranges of properties to be searched for. |
| [JSVM\_KeyFilter](#jsvm_keyfilter) | JSVM\_KeyFilter | Enumerates key filters. You can use OR to construct a composite filter. |
| [JSVM\_KeyConversion](#jsvm_keyconversion) | JSVM\_KeyConversion | Enumerates key conversion options. |
| [JSVM\_MemoryPressureLevel](#jsvm_memorypressurelevel) | JSVM\_MemoryPressureLevel | Enumerates memory pressure levels. |
| [JSVM\_CompileMode](#jsvm_compilemode) | JSVM\_CompileMode | JSVM compilation mode. |
| [JSVM\_CompileOptionId](#jsvm_compileoptionid) | JSVM\_CompileOptionId | ID of a JSVM compilation option. |
| [JSVM\_RegExpFlags](#jsvm_regexpflags) | JSVM\_RegExpFlags | Enumerates regular expression flags. They can be used to enable a set of flags. |
| [JSVM\_InitializedFlag](#jsvm_initializedflag) | JSVM\_InitializedFlag | Enumerates the initialization modes of flags. |
| [JSVM\_WasmOptLevel](#jsvm_wasmoptlevel) | JSVM\_WasmOptLevel | Enumerates WebAssembly optimization levels. |
| [JSVM\_CacheType](#jsvm_cachetype) | JSVM\_CacheType | Enumerates cache types. |
| [JSVM\_MicrotaskPolicy](#jsvm_microtaskpolicy) | JSVM\_MicrotaskPolicy | Enumerates JSVM microtask execution policies. |
| [JSVM\_TraceCategory](#jsvm_tracecategory) | JSVM\_TraceCategory | Enumerates categories of the JSVM internal trace events. |
| [JSVM\_CBTriggerTimeForGC](#jsvm_cbtriggertimeforgc) | JSVM\_CBTriggerTimeForGC | Enumerates the timings when the callback is triggered. |
| [JSVM\_GCType](#jsvm_gctype) | JSVM\_GCType | Enumerates GC types. |
| [JSVM\_GCCallbackFlags](#jsvm_gccallbackflags) | JSVM\_GCCallbackFlags | Enumerates GC callback flags. |
| [JSVM\_PromiseRejectEvent](#jsvm_promiserejectevent) | JSVM\_PromiseRejectEvent | Enumerates reject events for a promise. |
| [JSVM\_MessageErrorLevel](#jsvm_messageerrorlevel) | JSVM\_MessageErrorLevel | Enumerates error message levels. |
| [JSVM\_DefineClassOptionsId](#jsvm_defineclassoptionsid) | JSVM\_DefineClassOptionsId | Enumerates definition modes for a class. |
| [JSVM\_DebugOption](#jsvm_debugoption) | JSVM\_DebugOption | Enumerates debugging options. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (JSVM\_CDECL\* JSVM\_Finalize)(JSVM\_Env env,void\* finalizeData,void\* finalizeHint)](#jsvm_finalize) | JSVM\_CDECL\* JSVM\_Finalize | Defines a pointer to the **JSVM\_Finalize** function. It is passed in when a native object or data is associated with a JavaScript object, and is called when the associated JavaScript object is reclaimed by the GC to execute the native cleanup action. |
| [typedef bool (JSVM\_CDECL\* JSVM\_OutputStream)(const char\* data,int size,void\* streamData)](#jsvm_outputstream) | JSVM\_CDECL\* JSVM\_OutputStream | Defines a pointer to the callback of the ASCII output stream. **data** indicates the pointer to the output data. **size** indicates the size of the output data. **void** is a null pointer that points to the end of the stream. **streamData** indicates the pointer passed to the API function together with the callback. The API function generates data to the output stream. |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForGC)(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void\* data)](#jsvm_handlerforgc) | JSVM\_CDECL\* JSVM\_HandlerForGC | Defines a pointer to the handler for GC callback. |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForOOMError)(const char\* location,const char\* detail,bool isHeapOOM)](#jsvm_handlerforoomerror) | JSVM\_CDECL\* JSVM\_HandlerForOOMError | Defines a pointer to the handler for OOM-Error callback. |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForFatalError)(const char\* location,const char\* message)](#jsvm_handlerforfatalerror) | JSVM\_CDECL\* JSVM\_HandlerForFatalError | Defines a pointer to the handler for Fatal-Error callback. |
| [typedef void (JSVM\_CDECL\* JSVM\_HandlerForPromiseReject)(JSVM\_Env env, JSVM\_PromiseRejectEvent rejectEvent, JSVM\_Value rejectInfo)](#jsvm_handlerforpromisereject) | JSVM\_CDECL\* JSVM\_HandlerForPromiseReject | Defines a pointer to the handler for Promise-Reject callback. |

#### \[h2\]Variables

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| uint16\_t | char16\_t | 
Create an alias, **char16\_t**, for **uint16\_t**.

This code ensures that the **char16\_t** type is available in all target compilation environments, even in some old environments that do not support it. **char16\_t** is a new basic data type introduced in C++11. It is used to store 16-bit characters and represent UTF-16-encoded characters.

If the compiler does not recognize **char16\_t**, manually define a custom type whose underlying implementation is a 16-bit unsigned integer. Prerequisite: The current compiler is not a C++ compiler.|| It is a Microsoft Visual C++ compiler with a version earlier than Visual Studio 2015 (exclusive).

 |

#### Enum Description

#### \[h2\]JSVM\_PropertyAttributes

enum JSVM\_PropertyAttributes

**Description**

Enumerates the behaviors of controlling JavaScript object properties.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_DEFAULT = 0 | No explicit attribute set on the property. |
| JSVM\_WRITABLE = 1 << 0 | Writable property. |
| JSVM\_ENUMERABLE = 1 << 1 | Enumerable property. |
| JSVM\_CONFIGURABLE = 1 << 2 | Configurable property. |
| JSVM\_NO\_RECEIVER\_CHECK = 1 << 3 | Receiver used to mark the local methods does not need to be checked. If **JSVM\_NO\_RECEIVER\_CHECK** is not set, the method accepts only the instance of the defined class as the receiver. Otherwise, an exception "TypeError: illegal call" is thrown to the JSVM. |
| JSVM\_STATIC = 1 << 10 | Static property of the class, instead of the default instance property. Used only by **OH\_JSVM\_DefineClass**. |
| JSVM\_DEFAULT\_METHOD = JSVM\_WRITABLE | JSVM\_CONFIGURABLE | Configurable, writable, but not enumerable property, like a method of a JavaScript class. |
| JSVM\_METHOD\_NO\_RECEIVER\_CHECK = JSVM\_DEFAULT\_METHOD | JSVM\_NO\_RECEIVER\_CHECK | Class method whose receiver does not need to be checked. |
| JSVM\_DEFAULT\_JSPROPERTY = JSVM\_WRITABLE | JSVM\_ENUMERABLE | JSVM\_CONFIGURABLE | Writable, enumerable, and configurable property, like a property set by value assignment in JavaScript. |
| JSVM\_JSPROPERTY\_NO\_RECEIVER\_CHECK = JSVM\_DEFAULT\_JSPROPERTY | JSVM\_NO\_RECEIVER\_CHECK | Object property whose receiver does not need to be checked. |

#### \[h2\]JSVM\_ValueType

enum JSVM\_ValueType

**Description**

Enumerates **JSVM\_Value** types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_UNDEFINED | Undefined. |
| JSVM\_NULL | Null. |
| JSVM\_BOOLEAN | Boolean. |
| JSVM\_NUMBER | Number. |
| JSVM\_STRING | String. |
| JSVM\_SYMBOL | Symbol. |
| JSVM\_OBJECT | Object. |
| JSVM\_FUNCTION | Function. |
| JSVM\_EXTERNAL | External. |
| JSVM\_BIGINT | BigInt. |

#### \[h2\]JSVM\_TypedarrayType

enum JSVM\_TypedarrayType

**Description**

Enumerates **TypedArray** types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_INT8\_ARRAY | int8 type. |
| JSVM\_UINT8\_ARRAY | uint8 type. |
| JSVM\_UINT8\_CLAMPED\_ARRAY | Fixed uint8 type. |
| JSVM\_INT16\_ARRAY | int16 type. |
| JSVM\_UINT16\_ARRAY | uint16 type. |
| JSVM\_INT32\_ARRAY | int32 type. |
| JSVM\_UINT32\_ARRAY | uint32 type. |
| JSVM\_FLOAT32\_ARRAY | float32 type. |
| JSVM\_FLOAT64\_ARRAY | float64 type. |
| JSVM\_BIGINT64\_ARRAY | bigint64 type. |
| JSVM\_BIGUINT64\_ARRAY | biguint64 type. |

#### \[h2\]JSVM\_Status

enum JSVM\_Status

**Description**

Enumerates complete status codes indicating whether the JSVM-API call is successful or failed.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_OK | Successful. |
| JSVM\_INVALID\_ARG | Invalid argument. |
| JSVM\_OBJECT\_EXPECTED | Object expected. |
| JSVM\_STRING\_EXPECTED | String expected. |
| JSVM\_NAME\_EXPECTED | Name expected. |
| JSVM\_FUNCTION\_EXPECTED | Function expected. |
| JSVM\_NUMBER\_EXPECTED | Number expected. |
| JSVM\_BOOLEAN\_EXPECTED | Boolean expected. |
| JSVM\_ARRAY\_EXPECTED | Array expected. |
| JSVM\_GENERIC\_FAILURE | Generic failure. |
| JSVM\_PENDING\_EXCEPTION | Pending exception. |
| JSVM\_CANCELLED | Canceled. |
| JSVM\_ESCAPE\_CALLED\_TWICE | Escape called twice. |
| JSVM\_HANDLE\_SCOPE\_MISMATCH | Handle scope mismatch. |
| JSVM\_CALLBACK\_SCOPE\_MISMATCH | Callback scope mismatch. |
| JSVM\_QUEUE\_FULL | Full queue. |
| JSVM\_CLOSING | Closing. |
| JSVM\_BIGINT\_EXPECTED | BigInt expected. |
| JSVM\_DATE\_EXPECTED | Date expected. |
| JSVM\_ARRAYBUFFER\_EXPECTED | ArrayBuffer expected. |
| JSVM\_DETACHABLE\_ARRAYBUFFER\_EXPECTED | Detachable array buffer expected. |
| JSVM\_WOULD\_DEADLOCK | Would be in deadlock. |
| JSVM\_NO\_EXTERNAL\_BUFFERS\_ALLOWED | No external buffers allowed. |
| JSVM\_CANNOT\_RUN\_JS | Cannot run JavaSript. |
| JSVM\_INVALID\_TYPE | 
Invalid type.

**Since**: 18

 |
| JSVM\_JIT\_MODE\_EXPECTED | 

JIT mode expected.

**Since**: 18

 |

#### \[h2\]JSVM\_KeyCollectionMode

enum JSVM\_KeyCollectionMode

**Description**

Enumerates ranges of properties to be searched for.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_KEY\_INCLUDE\_PROTOTYPES | Properties on the prototype chain of the object are included. |
| JSVM\_KEY\_OWN\_ONLY | Only the object's own properties are included. |

#### \[h2\]JSVM\_KeyFilter

enum JSVM\_KeyFilter

**Description**

Enumerates key filters. You can use OR to construct a composite filter.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_KEY\_ALL\_PROPERTIES = 0 | Key of all properties. |
| JSVM\_KEY\_WRITABLE = 1 | Writable key. |
| JSVM\_KEY\_ENUMERABLE = 1 << 1 | Enumerable key. |
| JSVM\_KEY\_CONFIGURABLE = 1 << 2 | Configurable key. |
| JSVM\_KEY\_SKIP\_STRINGS = 1 << 3 | Key that skips strings. |
| JSVM\_KEY\_SKIP\_SYMBOLS = 1 << 4 | Key that skips symbols. |

#### \[h2\]JSVM\_KeyConversion

enum JSVM\_KeyConversion

**Description**

Enumerates key conversion options.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_KEY\_KEEP\_NUMBERS | Returns the numbers of integer indexes. |
| JSVM\_KEY\_NUMBERS\_TO\_STRINGS | Converts integer indexes to strings. |

#### \[h2\]JSVM\_MemoryPressureLevel

enum JSVM\_MemoryPressureLevel

**Description**

Enumerates memory pressure levels.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_NONE | No pressure. |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_MODERATE | Moderate pressure. |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_CRITICAL | Critical pressure. |
| JSVM\_MEMORY\_PRESSURE\_LEVEL\_LOW\_MEMORY | 
The system is notified that the memory is insufficient and garbage collection is triggered immediately.

**Since**: 22

 |

#### \[h2\]JSVM\_CompileMode

enum JSVM\_CompileMode

**Description**

Defines an enum for the compilation modes when **id** is **JSVM\_COMPILE\_MODE**.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| JSVM\_COMPILE\_MODE\_DEFAULT | Default compilation mode. |
| JSVM\_COMPILE\_MODE\_CONSUME\_CODE\_CACHE | Mode that consumes the code cache. |
| JSVM\_COMPILE\_MODE\_EAGER\_COMPILE | Eager compilation mode. |
| JSVM\_COMPILE\_MODE\_PRODUCE\_COMPILE\_PROFILE | Mode that generates the compilation profile. |
| JSVM\_COMPILE\_MODE\_CONSUME\_COMPILE\_PROFILE | Mode that consumes the compilation profile. |

#### \[h2\]JSVM\_CompileOptionId

enum JSVM\_CompileOptionId

**Description**

Defines an enum for **id** in **JSVM\_CompileOptions**. Each **id** corresponds to a **content** value. The value **JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP** is a Boolean, and is valid only when **sourceMapUrl** in **JSVM\_ScriptOrigin** is not empty.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| JSVM\_COMPILE\_MODE | JSVM compilation mode. |
| JSVM\_COMPILE\_CODE\_CACHE | JSVM code cache. |
| JSVM\_COMPILE\_SCRIPT\_ORIGIN | JSVM script origin. |
| JSVM\_COMPILE\_COMPILE\_PROFILE | JSVM compilation profile. |
| JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP | Source map enablement status of JSVM. |

#### \[h2\]JSVM\_RegExpFlags

enum JSVM\_RegExpFlags

**Description**

Enumerates regular expression flags. They can be used to enable a set of flags.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| JSVM\_REGEXP\_NONE = 0 | None mode. |
| JSVM\_REGEXP\_GLOBAL = 1 << 0 | Global mode. |
| JSVM\_REGEXP\_IGNORE\_CASE = 1 << 1 | Ignore Case mode. |
| JSVM\_REGEXP\_MULTILINE = 1 << 2 | Multiline mode. |
| JSVM\_REGEXP\_STICKY = 1 << 3 | Sticky mode. |
| JSVM\_REGEXP\_UNICODE = 1 << 4 | Unicode mode. |
| JSVM\_REGEXP\_DOT\_ALL = 1 << 5 | dotAll mode. |
| JSVM\_REGEXP\_LINEAR = 1 << 6 | Linear mode. |
| JSVM\_REGEXP\_HAS\_INDICES = 1 << 7 | Has Indices mode. |
| JSVM\_REGEXP\_UNICODE\_SETS = 1 << 8 | Unicode Sets mode. |

#### \[h2\]JSVM\_InitializedFlag

enum JSVM\_InitializedFlag

**Description**

Enumerates the initialization modes of flags.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| JSVM\_ZERO\_INITIALIZED | Flags are initialized to 0. |
| JSVM\_UNINITIALIZED | No initialization. |

#### \[h2\]JSVM\_WasmOptLevel

enum JSVM\_WasmOptLevel

**Description**

Enumerates WebAssembly optimization levels.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| JSVM\_WASM\_OPT\_BASELINE = 10 | Baseline optimization level. |
| JSVM\_WASM\_OPT\_HIGH = 20 | High optimization level. |

#### \[h2\]JSVM\_CacheType

enum JSVM\_CacheType

**Description**

Enumerates cache types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| JSVM\_CACHE\_TYPE\_JS | JavaScript cache, which is generated by **OH\_JSVM\_CreateCodeCache**. |
| JSVM\_CACHE\_TYPE\_WASM | WebAssembly cache, which is generated by **OH\_JSVM\_CreateWasmCache**. |

#### \[h2\]JSVM\_MicrotaskPolicy

enum JSVM\_MicrotaskPolicy

**Description**

Enumerates JSVM microtask execution policies.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_MICROTASK\_EXPLICIT = 0 | Microtasks are executed after the **OH\_JSVM\_PerformMicrotaskCheckpoint** method is called. |
| JSVM\_MICROTASK\_AUTO | Microtasks are automatically executed when the JS call stack is 0. This policy is used by default. |

#### \[h2\]JSVM\_TraceCategory

enum JSVM\_TraceCategory

**Description**

Enumerates categories of the JSVM internal trace events.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_TRACE\_VM | Collects the calls of main JSVM APIs, for example, executing JS scripts. |
| JSVM\_TRACE\_COMPILE | Collects the calls of compilation APIs, for example, background compilation. |
| JSVM\_TRACE\_EXECUTE | Collects the calls of APIs related to the running status, for example, task interruption and microtasks. |
| JSVM\_TRACE\_RUNTIME | Collects information about the external function calls. |
| JSVM\_TRACE\_STACK\_TRACE | Collects stack trace information from the JSVM. |
| JSVM\_TRACE\_WASM | Collects the calls of main WASM APIs, for example, compiling and instantiating WASM modules. |
| JSVM\_TRACE\_WASM\_DETAILED | Collects detailed WASM API calls, for example, background compilation and jumpboard compilation. |

#### \[h2\]JSVM\_CBTriggerTimeForGC

enum JSVM\_CBTriggerTimeForGC

**Description**

Enumerates the timings when the callback is triggered.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_CB\_TRIGGER\_BEFORE\_GC | A callback function is triggered before GC. |
| JSVM\_CB\_TRIGGER\_AFTER\_GC | A callback function is triggered after GC. |

#### \[h2\]JSVM\_GCType

enum JSVM\_GCType

**Description**

Enumerates GC types.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_GC\_TYPE\_SCAVENGE = 1 << 0 | The GC algorithm is Scavenge. |
| JSVM\_GC\_TYPE\_MINOR\_MARK\_COMPACT = 1 << 1 | The GC algorithm is Minor-Mark-Compact. |
| JSVM\_GC\_TYPE\_MARK\_SWEEP\_COMPACT = 1 << 2 | The GC algorithm is Mark-Sweep-Compact. |
| JSVM\_GC\_TYPE\_INCREMENTAL\_MARKING = 1 << 3 | The GC algorithm is Incremental-Marking. |
| JSVM\_GC\_TYPE\_PROCESS\_WEAK\_CALLBACKS = 1 << 4 | The GC algorithm is Weak-Callbacks. |
| JSVM\_GC\_TYPE\_ALL = JSVM\_GC\_TYPE\_SCAVENGE | JSVM\_GC\_TYPE\_MINOR\_MARK\_COMPACT | JSVM\_GC\_TYPE\_MARK\_SWEEP\_COMPACT | JSVM\_GC\_TYPE\_INCREMENTAL\_MARKING | JSVM\_GC\_TYPE\_PROCESS\_WEAK\_CALLBACKS | All types of GC algorithms are included. |

#### \[h2\]JSVM\_GCCallbackFlags

enum JSVM\_GCCallbackFlags

**Description**

Enumerates GC callback flags.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_NO\_GC\_CALLBACK\_FLAGS | No callback flag. |
| JSVM\_GC\_CALLBACK\_CONSTRUCT\_RETAINED\_OBJECT\_INFOS | Builds reserved object information in the GC callback. |
| JSVM\_GC\_CALLBACK\_FORCED | Forcibly executes the GC callback. |
| JSVM\_GC\_CALLBACK\_SYNCHRONOUS\_PHANTOM\_CALLBACK\_PROCESSING | Synchronously processes ghost object callbacks. |
| JSVM\_GC\_CALLBACK\_COLLECT\_ALL\_AVAILABLE\_GARBAGE | Collects all available garbage objects during GC. |
| JSVM\_GC\_CALLBACK\_COLLECT\_ALL\_EXTERNAL\_MEMORY | Collects all external memory during GC. |
| JSVM\_GC\_CALLBACK\_SCHEDULE\_IDLE\_GARBAGE\_COLLECTION | Schedules GC when idle. |

#### \[h2\]JSVM\_PromiseRejectEvent

enum JSVM\_PromiseRejectEvent

**Description**

Enumerates reject events for a promise.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_PROMISE\_REJECT\_OTHER\_REASONS = 0 | A promise is rejected, but the rejection reason is unknown or unclear. |
| JSVM\_PROMISE\_REJECT\_WITH\_NO\_HANDLER = 1 | A promise is rejected but no handler is available. |
| JSVM\_PROMISE\_ADD\_HANDLER\_AFTER\_REJECTED = 2 | A handler is added after a promise is rejected. |
| JSVM\_PROMISE\_REJECT\_AFTER\_RESOLVED = 3 | Attempts to reject a promise after this promise is resolved. |
| JSVM\_PROMISE\_RESOLVE\_AFTER\_RESOLVED = 4 | Attempts to resolve a promise after this promise is resolved. |

#### \[h2\]JSVM\_MessageErrorLevel

enum JSVM\_MessageErrorLevel

**Description**

Enumerates error message levels.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_MESSAGE\_LOG = (1 << 0) | Logs. |
| JSVM\_MESSAGE\_DEBUG = (1 << 1) | Debugging messages. |
| JSVM\_MESSAGE\_INFO = (1 << 2) | Information. |
| JSVM\_MESSAGE\_ERROR = (1 << 3) | Errors. |
| JSVM\_MESSAGE\_WARNING = (1 << 4) | Warnings. |
| JSVM\_MESSAGE\_ALL = JSVM\_MESSAGE\_LOG | JSVM\_MESSAGE\_DEBUG | JSVM\_MESSAGE\_INFO | JSVM\_MESSAGE\_ERROR | JSVM\_MESSAGE\_WARNING | Information of all levels. |

#### \[h2\]JSVM\_DefineClassOptionsId

enum JSVM\_DefineClassOptionsId

**Description**

Enumerates definition modes for a class.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| JSVM\_DEFINE\_CLASS\_NORMAL | Defines a class in normal mode. |
| JSVM\_DEFINE\_CLASS\_WITH\_COUNT | Reserves a specified number of interfield slots for the created class. Native data can be stored in these slots. |
| JSVM\_DEFINE\_CLASS\_WITH\_PROPERTY\_HANDLER | Sets a listener property for the created class and sets a callback to be invoked when it is called as a function. |

#### \[h2\]JSVM\_DebugOption

enum JSVM\_DebugOption

**Description**

Enumerates debugging options.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| JSVM\_SCOPE\_CHECK | Scope check. |

#### Function Description

#### \[h2\]JSVM\_Finalize()

typedef void (JSVM\_CDECL\* JSVM\_Finalize)(JSVM\_Env env,void\* finalizeData,void\* finalizeHint)

**Description**

Defines a pointer to the **JSVM\_Finalize** function. It is passed in when a native object or data is associated with a JavaScript object, and is called when the associated JavaScript object is reclaimed by the GC to execute the native cleanup action.

**Since**: 11

#### \[h2\]JSVM\_OutputStream()

typedef bool (JSVM\_CDECL\* JSVM\_OutputStream)(const char\* data,int size,void\* streamData)

**Description**

Defines a pointer to the callback of the ASCII output stream. **data** indicates the pointer to the output data. **size** indicates the size of the output data. **void** is a null pointer that points to the end of the stream. **streamData** indicates the pointer passed to the API function together with the callback. The API function generates data to the output stream.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the stream can continue to receive data; returns **false** if the stream is closed. |

#### \[h2\]JSVM\_HandlerForGC()

typedef void (JSVM\_CDECL\* JSVM\_HandlerForGC)(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void\* data)

**Description**

Defines a pointer to the handler for GC callback.

**Since**: 18

#### \[h2\]JSVM\_HandlerForOOMError()

typedef void (JSVM\_CDECL\* JSVM\_HandlerForOOMError)(const char\* location,const char\* detail,bool isHeapOOM)

**Description**

Defines a pointer to the handler for OOM-Error callback.

**Since**: 18

#### \[h2\]JSVM\_HandlerForFatalError()

typedef void (JSVM\_CDECL\* JSVM\_HandlerForFatalError)(const char\* location,const char\* message)

**Description**

Defines a pointer to the handler for Fatal-Error callback.

**Since**: 18

#### \[h2\]JSVM\_HandlerForPromiseReject()

typedef void (JSVM\_CDECL\* JSVM\_HandlerForPromiseReject)(JSVM\_Env env, JSVM\_PromiseRejectEvent rejectEvent, JSVM\_Value rejectInfo)

**Description**

Defines a pointer to the handler for Promise-Reject callback.

**Since**: 18
