# native\_child\_process.h

#### Overview

Declares the APIs used to create a native child process and establish an IPC channel between the parent and child processes.

A maximum of 512 child processes can be started through this module and [childProcessManager](../../../arkts-apis/stage-model/ohos-app-ability-childprocessmanager-child-process-management/document.md) (non-SELF\_FORK mode).

**File to include**: <AbilityKit/native\_child\_process.h>

**Library**: libchild\_process.so

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Since**: 12

**Related module**: [ChildProcess](../../modules/childprocess/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NativeChildProcess\_Fd](../../structs/nativechildprocess-fd/document.md) | NativeChildProcess\_Fd | Describes the information about the file descriptor passed to the child process. |
| [NativeChildProcess\_FdList](../../structs/nativechildprocess-fdlist/document.md) | NativeChildProcess\_FdList | Describes the list of file descriptors passed to the child process. A maximum of 16 file descriptors are supported. |
| [NativeChildProcess\_Options](../../structs/nativechildprocess-options/document.md) | NativeChildProcess\_Options | Describes the options used by the child process. |
| [NativeChildProcess\_Args](../../structs/nativechildprocess-args/document.md) | NativeChildProcess\_Args | Describes the parameters passed to the child process. |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md) | Ability\_ChildProcessConfigs | Describes the configuration information about a child process, including the child process name and the sharing mode of the data sandbox and network environment. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | Ability\_NativeChildProcess\_ErrCode | Defines an enum for the error codes used by the native child process module. |
| [NativeChildProcess\_IsolationMode](#nativechildprocess_isolationmode) | NativeChildProcess\_IsolationMode | Enumerates the sharing modes available for the data sandbox and network environment of a native child process. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Ability\_ChildProcessConfigs\* OH\_Ability\_CreateChildProcessConfigs()](#oh_ability_createchildprocessconfigs) | \- | Creates a child process configuration object. When this object is no longer needed, call [OH\_Ability\_DestroyChildProcessConfigs](#oh_ability_destroychildprocessconfigs) to destroy the object to prevent memory leakage. |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_DestroyChildProcessConfigs(Ability\_ChildProcessConfigs\* configs)](#oh_ability_destroychildprocessconfigs) | \- | Destroys a child process configuration object and releases its memory. After this function is called, do not use the destroyed object. |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetIsolationMode(Ability\_ChildProcessConfigs\* configs, NativeChildProcess\_IsolationMode isolationMode)](#oh_ability_childprocessconfigs_setisolationmode) | \- | Sets the sharing mode of the data sandbox and network environment for a child process configuration object. For details, see [NativeChildProcess\_IsolationMode](#nativechildprocess_isolationmode). This setting takes effect only when [OH\_Ability\_StartNativeChildProcessWithConfigs](#oh_ability_startnativechildprocesswithconfigs) or [OH\_Ability\_CreateNativeChildProcessWithConfigs](#oh_ability_createnativechildprocesswithconfigs) is called. |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetProcessName(Ability\_ChildProcessConfigs\* configs,const char\* processName)](#oh_ability_childprocessconfigs_setprocessname) | \- | Sets the process name in a child process configuration object. |
| [typedef void (\*OH\_Ability\_OnNativeChildProcessStarted)(int errCode, OHIPCRemoteProxy \*remoteProxy)](#oh_ability_onnativechildprocessstarted) | OH\_Ability\_OnNativeChildProcessStarted | Creates a child process based on a child process configuration object and loads the specified DLL file. The startup result is asynchronously communicated to the caller via a callback. The callback runs in a separate thread. You must ensure thread synchronization and avoid time-consuming operations to prevent delays. |
| [int OH\_Ability\_CreateNativeChildProcess(const char\* libName,OH\_Ability\_OnNativeChildProcessStarted onProcessStarted)](#oh_ability_createnativechildprocess) | \- | 
Creates a child process, loads the specified Dynamic Link Library (DLL) file, and returns the startup result asynchronously through a callback parameter. The callback notification is an independent thread. When implementing the callback function, pay attention to thread synchronization and do not perform time-consuming operations to avoid long-time blocking. The DLL specified must implement and export the following functions:

1\. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()

2\. void NativeChildProcess\_MainProc()

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_CreateNativeChildProcess(libName, onProcessStartedCallback)

Child process:

2\. dlopen(libName)

3\. dlsym("NativeChildProcess\_OnConnect")

4\. dlsym("NativeChildProcess\_MainProc")

5\. ipcRemote = NativeChildProcess\_OnConnect()

6\. NativeChildProcess\_MainProc()

Parent process:

7\. onProcessStartedCallback(ipcRemote, errCode)

Child process:

8\. The child process exits after the NativeChildProcess\_MainProc() function is returned.

**Device behavior differences**: For API version 13 and earlier, this function can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned. Starting from API version 14, this function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

Note: In API version 14 and earlier versions, a single process supports only one native child process. Starting from API version 15, a single process supports a maximum of 50 native child processes.

 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_CreateNativeChildProcessWithConfigs(const char\* libName,Ability\_ChildProcessConfigs\* configs, OH\_Ability\_OnNativeChildProcessStarted onProcessStarted)](#oh_ability_createnativechildprocesswithconfigs) | \- | 

Creates a child process based on a child process configuration object and loads the specified DLL file. The startup result is asynchronously communicated to the caller via a callback. The callback runs in a separate thread. You must ensure thread synchronization and avoid time-consuming operations to prevent delays. The DLL specified must implement and export the following functions:

1\. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()

2\. void NativeChildProcess\_MainProc()

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_CreateNativeChildProcessWithConfigs(libName, configs, onProcessStartedCallback)

Child process:

2\. dlopen(libName)

3\. dlsym("NativeChildProcess\_OnConnect")

4\. dlsym("NativeChildProcess\_MainProc")

5\. ipcRemote = NativeChildProcess\_OnConnect()

6\. NativeChildProcess\_MainProc()

Parent process:

7\. onProcessStartedCallback(ipcRemote, errCode)

Child process:

8.

The child process exits after the NativeChildProcess\_MainProc() function is returned.

**Device behavior differences**: This function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_StartNativeChildProcess(const char\* entry, NativeChildProcess\_Args args,NativeChildProcess\_Options options, int32\_t \*pid)](#oh_ability_startnativechildprocess) | \- | 

Starts a child process and loads the specified Dynamic Link Library (DLL) file. The specified DLL must implement and export a function that accepts **NativeChildProcess\_Args** as its parameter (you can customize the function name). The following is an example:

1\. void Main(NativeChildProcess\_Args args);

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_StartNativeChildProcess(entryPoint, args, options)

Child process:

2\. dlopen(libName)

3\. dlsym("Main")

4\. Main(args)

5\. The child process exits after the Main(args) function returns.

**Device behavior differences**: For API version 13 and earlier, this function can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned. Starting from API version 14, this function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

 |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_StartNativeChildProcessWithConfigs(const char\* entry, NativeChildProcess\_Args args, Ability\_ChildProcessConfigs\* configs, int32\_t \*pid)](#oh_ability_startnativechildprocesswithconfigs) | \- | 

Starts a native child process based on the child process configuration object, loads the specified DLL file, and calls the entry function. Arguments can be passed to the child process. The specified DLL must implement and export a function that accepts **NativeChildProcess\_Args** as its parameter (you can customize the function name). The following is an example:

1\. void Main(NativeChildProcess\_Args args);

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_StartNativeChildProcessWithConfigs(entryPoint, args, configs, &pid)

Child process:

2\. dlopen(libName)

3\. dlsym("Main")

4\. Main(args)

5\. The child process exits after the Main(args) function returns.

**Device behavior differences**: This function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

 |
| [NativeChildProcess\_Args\* OH\_Ability\_GetCurrentChildProcessArgs()](#oh_ability_getcurrentchildprocessargs) | \- | Obtains the startup parameters of the child process. |
| [typedef void (\*OH\_Ability\_OnNativeChildProcessExit)(int32\_t pid, int32\_t signal)](#oh_ability_onnativechildprocessexit) | OH\_Ability\_OnNativeChildProcessExit | Obtains the exit information of the child process. |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_RegisterNativeChildProcessExitCallback(OH\_Ability\_OnNativeChildProcessExit onProcessExit)](#oh_ability_registernativechildprocessexitcallback) | \- | Registers a callback to listen for child process exit. The registered callback function is triggered only when the child process started by calling [OH\_Ability\_StartNativeChildProcess](#oh_ability_startnativechildprocess), [OH\_Ability\_StartNativeChildProcessWithConfigs](#oh_ability_startnativechildprocesswithconfigs), or [childProcessManager.startNativeChildProcess in @ohos.app.ability.childProcessManager](../../../arkts-apis/stage-model/ohos-app-ability-childprocessmanager-child-process-management/document.md#childprocessmanagerstartnativechildprocess13) exits. If the same callback function is registered repeatedly, only one of them is kept. |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_UnregisterNativeChildProcessExitCallback(OH\_Ability\_OnNativeChildProcessExit onProcessExit)](#oh_ability_unregisternativechildprocessexitcallback) | \- | Unregisters the callback used to listen for child process exit. |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetIsolationUid(Ability\_ChildProcessConfigs\* configs, bool enableIsolationUid)](#oh_ability_childprocessconfigs_setisolationuid) | \- | Sets whether the child process uses an independent UID. This setting takes effect only when **NativeChildProcess\_IsolationMode** is set to **NCP\_ISOLATION\_MODE\_ISOLATED**. |
| [Ability\_NativeChildProcess\_ErrCode OH\_Ability\_KillChildProcess(int32\_t pid)](#oh_ability_killchildprocess) | \- | Terminates a child process created by the current process. |

#### Enum Description

#### \[h2\]Ability\_NativeChildProcess\_ErrCode

enum Ability\_NativeChildProcess\_ErrCode

**Description**

Defines an enum for the error codes used by the native child process module.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NCP\_NO\_ERROR = 0 | Operation successful. |
| NCP\_ERR\_INVALID\_PARAM = 401 | Invalid parameter. |
| NCP\_ERR\_NOT\_SUPPORTED = 801 | Creating a native child process is not supported. |
| NCP\_ERR\_INTERNAL = 16000050 | Internal error. |
| NCP\_ERR\_BUSY = 16010001 | A new child process cannot be created during the startup of another native child process. You can try again after the child process is started. This function is deprecated since API version 15. |
| NCP\_ERR\_TIMEOUT = 16010002 | Starting the native child process times out. |
| NCP\_ERR\_SERVICE\_ERROR = 16010003 | Server error. |
| NCP\_ERR\_MULTI\_PROCESS\_DISABLED = 16010004 | The multi-process mode is disabled. A child process cannot be started. |
| NCP\_ERR\_ALREADY\_IN\_CHILD = 16010005 | A process cannot be created in a child process. |
| NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED = 16010006 | The number of native child processes reaches the maximum. |
| NCP\_ERR\_LIB\_LOADING\_FAILED = 16010007 | The child process fails to load the DLL because the file does not exist or the corresponding method is not implemented or exported. |
| NCP\_ERR\_CONNECTION\_FAILED = 16010008 | The child process fails to call the OnConnect method of the DLL. An invalid IPC object pointer may be returned. |
| NCP\_ERR\_CALLBACK\_NOT\_EXIST = 16010009 | 
The parent process calls the **OH\_Ability\_UnregisterNativeChildProcessExitCallback** function to unregister a callback function, but the callback function is not found.

**Since**: 20

 |
| NCP\_ERR\_INVALID\_PID = 16010010 | 

The specified PID does not exist, does not belong to a child process of the current process, or belongs to a child process started in SELF\_FORK mode by calling [childProcessManager.startChildProcess](../../../arkts-apis/stage-model/ohos-app-ability-childprocessmanager-child-process-management/document.md#childprocessmanagerstartchildprocess).

**Since**: 22

 |

#### \[h2\]NativeChildProcess\_IsolationMode

enum NativeChildProcess\_IsolationMode

**Description**

Enumerates the sharing modes available for the data sandbox and network environment of a native child process.

**Since**: 13

| Value | Description |
| :-- | :-- |
| NCP\_ISOLATION\_MODE\_NORMAL = 0 | In normal mode, the parent and child processes share the same sandbox or network environment. |
| NCP\_ISOLATION\_MODE\_ISOLATED = 1 | In isolated mode, the parent and child processes each have their own separate sandbox and network environment. |

#### Function Description

#### \[h2\]OH\_Ability\_CreateChildProcessConfigs()

Ability\_ChildProcessConfigs\* OH\_Ability\_CreateChildProcessConfigs()

**Description**

Creates a child process configuration object. When this object is no longer needed, call [OH\_Ability\_DestroyChildProcessConfigs](#oh_ability_destroychildprocessconfigs) to destroy the object to prevent memory leakage.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md)\* | 
Pointer to the [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md) object: The call is successful.

nullptr: An internal error occurs or memory allocation fails.

 |

#### \[h2\]OH\_Ability\_DestroyChildProcessConfigs()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_DestroyChildProcessConfigs(Ability\_ChildProcessConfigs\* configs)

**Description**

Destroys a child process configuration object and releases its memory. After this function is called, do not use the destroyed object.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md)\* configs | Pointer to a child process configuration object. After this function is called, the object pointer becomes invalid. Do not use the pointer. nullptr is allowed, which does not trigger any operation. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: An input parameter is nullptr.

 |

#### \[h2\]OH\_Ability\_ChildProcessConfigs\_SetIsolationMode()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetIsolationMode(Ability\_ChildProcessConfigs\* configs, NativeChildProcess\_IsolationMode isolationMode)

**Description**

Sets the sharing mode of the data sandbox and network environment for a child process configuration object. For details, see [NativeChildProcess\_IsolationMode](#nativechildprocess_isolationmode). This setting takes effect only when [OH\_Ability\_StartNativeChildProcessWithConfigs](#oh_ability_startnativechildprocesswithconfigs) or [OH\_Ability\_CreateNativeChildProcessWithConfigs](#oh_ability_createnativechildprocesswithconfigs) is called.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md)\* configs | Pointer to a child process configuration object. The value cannot be nullptr. |
| [NativeChildProcess\_IsolationMode](#nativechildprocess_isolationmode) isolationMode | Sharing mode of the data sandbox and network environment. For details, see **NativeChildProcess\_IsolationMode**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: The parameter **configs** is nullptr.

 |

#### \[h2\]OH\_Ability\_ChildProcessConfigs\_SetIsolationUid()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetIsolationUid(Ability\_ChildProcessConfigs\* configs, bool isolationUid)

**Description**

Sets whether the child process uses an independent UID. For example, in browser security hardening scenarios, you can isolate the UIDs of the main process and its child processes.

This setting takes effect only when **NativeChildProcess\_IsolationMode** is set to **NCP\_ISOLATION\_MODE\_ISOLATED**. If this function is not called to set **isolationUid**, the default value is **false**, meaning the child process will share the same UID as the main process.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md)\* configs | Pointer to a child process configuration object. The value cannot be nullptr. |
| bool isolationUid | Whether the child process uses an independent UID. **true** if the child process uses an independent UID; **false** if the child process and the main process share the same UID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: The parameter **configs** is nullptr.

 |

#### \[h2\]OH\_Ability\_ChildProcessConfigs\_SetProcessName()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_ChildProcessConfigs\_SetProcessName(Ability\_ChildProcessConfigs\* configs,const char\* processName)

**Description**

Sets the process name in a child process configuration object.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md)\* configs | Pointer to a child process configuration object. The pointer cannot be null. |
| const char\* processName | Pointer to the process name, which must be a non-empty string accepting only letters, digits, and underscores (\_). The string contains a maximum of 64 characters. The final process name is in the format of {bundleName}:{processName}. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: The input parameter **configs** is nullptr, or **processName** contains characters other than letters, digits, and underscores (\_).

 |

#### \[h2\]OH\_Ability\_OnNativeChildProcessStarted()

typedef void (\*OH\_Ability\_OnNativeChildProcessStarted)(int errCode, OHIPCRemoteProxy \*remoteProxy)

**Description**

Defines a callback function for notifying the child process startup result.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int errCode | 
Error code returned by the callback function.

[NCP\_NO\_ERROR](#ability_nativechildprocess_errcode): The child process is created successfully.

[NCP\_ERR\_LIB\_LOADING\_FAILED](#ability_nativechildprocess_errcode): Loading the DLL file fails or the necessary export function is not implemented in the DLL.

[NCP\_ERR\_CONNECTION\_FAILED](#ability_nativechildprocess_errcode): The **OnConnect** method implemented in the DLL does not return a valid IPC stub pointer.

For details, see [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode).

 |
| [OHIPCRemoteProxy](../../../../ipc-kit/c-apis/structs/ohipcremoteproxy/document.md) \*remoteProxy | Pointer to the IPC object of the child process. If an exception occurs, the value may be nullptr. The pointer must be released by calling [OH\_IPCRemoteProxy\_Destroy](../../../../ipc-kit/c-apis/header-files/ipc-cremote-object-h/document.md#oh_ipcremoteproxy_destroy) when it is no longer needed. |

**Reference**

[OH\_IPCRemoteProxy\_Destroy](../../../../ipc-kit/c-apis/header-files/ipc-cremote-object-h/document.md#oh_ipcremoteproxy_destroy)

#### \[h2\]OH\_Ability\_CreateNativeChildProcess()

int OH\_Ability\_CreateNativeChildProcess(const char\* libName,OH\_Ability\_OnNativeChildProcessStarted onProcessStarted)

**Description**

Creates a child process, loads the specified Dynamic Link Library (DLL) file, and returns the startup result asynchronously through a callback parameter. The callback notification is an independent thread. When implementing the callback function, pay attention to thread synchronization and do not perform time-consuming operations to avoid long-time blocking.

The DLL specified must implement and export the following functions:

1\. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()

2\. void NativeChildProcess\_MainProc()

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_CreateNativeChildProcess(libName, onProcessStartedCallback)

Child process:

2\. dlopen(libName)

3\. dlsym("NativeChildProcess\_OnConnect")

4\. dlsym("NativeChildProcess\_MainProc")

5\. ipcRemote = NativeChildProcess\_OnConnect()

6\. NativeChildProcess\_MainProc()

Parent process:

7\. onProcessStartedCallback(ipcRemote, errCode)

Child process:

8\. The child process exits after the NativeChildProcess\_MainProc() function is returned.

**Device behavior differences**: For API version 13 and earlier, this function can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned. Starting from API version 14, this function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/EAM0hwu9QeOBT9DSgY-6OA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062213Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB2AEBB8EF2C916BA45F4A73DBB61FC94722D2550DE5EDC79146EE0970AB13E4)

In API version 14 and earlier versions, a single process supports only one native child process. Starting from API version 15, a single process supports a maximum of 50 native child processes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* libName | Pointer to the name of the DLL file loaded in the child process. The value cannot be nullptr. |
| [OH\_Ability\_OnNativeChildProcessStarted](#oh_ability_onnativechildprocessstarted) onProcessStarted | Pointer to the callback function for notifying the child process startup result. The value cannot be nullptr. For details, see [OH\_Ability\_OnNativeChildProcessStarted](#oh_ability_onnativechildprocessstarted). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
[NCP\_NO\_ERROR](#ability_nativechildprocess_errcode): The call is successful, but the actual startup result is notified by the callback function.

[NCP\_ERR\_INVALID\_PARAM](#ability_nativechildprocess_errcode): The dynamic library name or callback function pointer is invalid.

[NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode): The device does not support the creation of native child processes.

[NCP\_ERR\_MULTI\_PROCESS\_DISABLED](#ability_nativechildprocess_errcode): Multi-process mode is disabled on the device.

[NCP\_ERR\_ALREADY\_IN\_CHILD](#ability_nativechildprocess_errcode): A process cannot be created in a child process.

[NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED](#ability_nativechildprocess_errcode): The number of native child processes reaches the maximum.

For details, see [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode).

 |

**Reference**

[OH\_Ability\_OnNativeChildProcessStarted](#oh_ability_onnativechildprocessstarted)

#### \[h2\]OH\_Ability\_CreateNativeChildProcessWithConfigs()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_CreateNativeChildProcessWithConfigs(const char\* libName,Ability\_ChildProcessConfigs\* configs, OH\_Ability\_OnNativeChildProcessStarted onProcessStarted)

**Description**

Creates a child process based on a child process configuration object and loads the specified DLL file. The startup result is asynchronously communicated to the caller via a callback. The callback runs in a separate thread. You must ensure thread synchronization and avoid time-consuming operations to prevent delays.

The DLL specified must implement and export the following functions:

1\. OHIPCRemoteStub\* NativeChildProcess\_OnConnect()

2\. void NativeChildProcess\_MainProc()

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_CreateNativeChildProcessWithConfigs(libName, configs, onProcessStartedCallback)

Child process:

2\. dlopen(libName)

3\. dlsym("NativeChildProcess\_OnConnect")

4\. dlsym("NativeChildProcess\_MainProc")

5\. ipcRemote = NativeChildProcess\_OnConnect()

6\. NativeChildProcess\_MainProc()

Parent process:

7\. onProcessStartedCallback(ipcRemote, errCode)

Child process:

8\. The child process exits after the NativeChildProcess\_MainProc() function is returned.

**Device behavior differences**: This function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* libName | Pointer to the name of the DLL file loaded in the child process. The value cannot be nullptr. |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md)\* configs | Pointer to a child process configuration object. The value cannot be nullptr. |
| [OH\_Ability\_OnNativeChildProcessStarted](#oh_ability_onnativechildprocessstarted) onProcessStarted | Pointer to the callback function for notifying the child process startup result. The value cannot be nullptr. For details, see **OH\_Ability\_OnNativeChildProcessStarted**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: An input parameter is invalid.

**NCP\_ERR\_NOT\_SUPPORTED**: The device does not support the creation of native child processes.

**NCP\_ERR\_MULTI\_PROCESS\_DISABLED**: Multi-process mode is disabled on the device, and the child process cannot be started.

**NCP\_ERR\_ALREADY\_IN\_CHILD**: A process cannot be created in a child process.

**NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED**: The maximum number of native child processes has been reached.

For details about the error codes, see **Ability\_NativeChildProcess\_ErrCode**.

 |

**Reference**

[OH\_Ability\_OnNativeChildProcessStarted](#oh_ability_onnativechildprocessstarted)

#### \[h2\]OH\_Ability\_StartNativeChildProcess()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_StartNativeChildProcess(const char\* entry, NativeChildProcess\_Args args,NativeChildProcess\_Options options, int32\_t \*pid)

**Description**

Starts a native child process, loads the specified DLL file, and calls the entry function. The specified DLL must implement and export a function that accepts [NativeChildProcess\_Args](../../structs/nativechildprocess-args/document.md) as its parameter (you can customize the function name). Arguments can be passed to the child process. The ArkTS basic runtime environment cannot be created in the child process.

The following is an example:

void Main(NativeChildProcess\_Args args);

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_StartNativeChildProcess(entryPoint, args, options)

Child process:

2\. dlopen(libName)

3\. dlsym("Main")

4\. Main(args)

5\. The child process exits after the Main(args) function returns.

**Device behavior differences**: For API version 13 and earlier, this function can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned. Starting from API version 14, this function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* entry | Pointer to the dynamic library and entry function to be loaded by the child process, for example, **libEntry.so:Main**. The value cannot be **nullptr**. |
| [NativeChildProcess\_Args](../../structs/nativechildprocess-args/document.md) args | Parameters passed to the child process. |
| [NativeChildProcess\_Options](../../structs/nativechildprocess-options/document.md) options | Child process options. |
| int32\_t \*pid | Pointer to the ID of the child process. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: The dynamic library name or callback function pointer is invalid.

**NCP\_ERR\_NOT\_SUPPORTED**: The device does not support the creation of native child processes.

**NCP\_ERR\_ALREADY\_IN\_CHILD**: Multi-process mode is disabled on the device.

**NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED**: The maximum number of native child processes has been reached.

For details about the error codes, see **Ability\_NativeChildProcess\_ErrCode**.

 |

**Reference**

[OH\_Ability\_OnNativeChildProcessStarted](#oh_ability_onnativechildprocessstarted)

#### \[h2\]OH\_Ability\_StartNativeChildProcessWithConfigs()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_StartNativeChildProcessWithConfigs(const char\* entry, NativeChildProcess\_Args args, Ability\_ChildProcessConfigs\* configs, int32\_t \*pid)

**Description**

Starts a native child process based on the child process configuration object, loads the specified DLL file, and calls the entry function. Arguments can be passed to the child process. The specified DLL must implement and export a function that accepts [NativeChildProcess\_Args](../../structs/nativechildprocess-args/document.md) as its parameter (you can customize the function name).

The following is an example:

void Main(NativeChildProcess\_Args args);

The processing logic sequence is shown in the following pseudocode:

Parent process:

1\. OH\_Ability\_StartNativeChildProcessWithConfigs(entryPoint, args, configs, &pid)

Child process:

2\. dlopen(libName)

3\. dlsym("Main")

4\. Main(args)

5\. The child process exits after the Main(args) function returns.

**Device behavior differences**: This function can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code [NCP\_ERR\_NOT\_SUPPORTED](#ability_nativechildprocess_errcode) is returned.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* entry | Pointer to the symbol and entry function of the DDL called in the child process, separated by a colon (:), for example, **libentry.so:Main**. The value cannot be nullptr. |
| [NativeChildProcess\_Args](../../structs/nativechildprocess-args/document.md) args | Parameters passed to the child process. |
| [Ability\_ChildProcessConfigs](../../structs/ability-childprocessconfigs/document.md)\* configs | Pointer to a child process configuration object. |
| int32\_t \*pid | Pointer to the ID of the child process. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: An input parameter is invalid.

**NCP\_ERR\_NOT\_SUPPORTED**: The device does not support the creation of native child processes.

**NCP\_ERR\_ALREADY\_IN\_CHILD**: A process cannot be created in a child process.

**NCP\_ERR\_MAX\_CHILD\_PROCESSES\_REACHED**: The maximum number of native child processes has been reached.

For details about the error codes, see **Ability\_NativeChildProcess\_ErrCode**.

 |

#### \[h2\]OH\_Ability\_GetCurrentChildProcessArgs()

NativeChildProcess\_Args\* OH\_Ability\_GetCurrentChildProcessArgs()

**Description**

Used by a child process, after being started by calling [OH\_Ability\_StartNativeChildProcess](#oh_ability_startnativechildprocess), to obtain the startup parameter [NativeChildProcess\_Args](../../structs/nativechildprocess-args/document.md) from any .so file or child thread.

**Since**: 17

**Returns**

| Type | Description |
| :-- | :-- |
| [NativeChildProcess\_Args](../../structs/nativechildprocess-args/document.md)\* | Pointer to the startup parameters of the child process. |

#### \[h2\]OH\_Ability\_OnNativeChildProcessExit()

typedef void (\*OH\_Ability\_OnNativeChildProcessExit)(int32\_t pid, int32\_t signal)

**Description**

Defines a callback to listen for child process exit.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t pid | Pointer to the ID of the child process. |
| int32\_t signal | Signal for child process exit. |

**See**

[OH\_Ability\_RegisterNativeChildProcessExitCallback](#oh_ability_registernativechildprocessexitcallback)

[OH\_Ability\_UnregisterNativeChildProcessExitCallback](#oh_ability_unregisternativechildprocessexitcallback)

#### \[h2\]OH\_Ability\_RegisterNativeChildProcessExitCallback()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_RegisterNativeChildProcessExitCallback(OH\_Ability\_OnNativeChildProcessExit onProcessExit)

**Description**

Registers a callback function for detecting abnormal exit of a native child process. The registered callback function is triggered only when the child process started by calling [OH\_Ability\_StartNativeChildProcess](#oh_ability_startnativechildprocess), [OH\_Ability\_StartNativeChildProcessWithConfigs](#oh_ability_startnativechildprocesswithconfigs), or [childProcessManager.startNativeChildProcess in @ohos.app.ability.childProcessManager](../../../arkts-apis/stage-model/ohos-app-ability-childprocessmanager-child-process-management/document.md#childprocessmanagerstartnativechildprocess13) exits. If the same callback function is registered multiple times, the callback function is executed only once when the child process exits.

The parameter must implement the entry function [OH\_Ability\_OnNativeChildProcessExit](#oh_ability_onnativechildprocessexit). For details, see [Registering the Native Child Process Exit Callback Function](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/capi-nativechildprocess-exit-info).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Ability\_OnNativeChildProcessExit](#oh_ability_onnativechildprocessexit) onProcessExit | Entry point of the callback function to be called when the child process exits. The value cannot be nullptr. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: An input parameter is invalid.

**NCP\_ERR\_INTERNAL**: An internal error occurs.

For details, see **Ability\_NativeChildProcess\_ErrCode**.

 |

#### \[h2\]OH\_Ability\_UnregisterNativeChildProcessExitCallback()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_UnregisterNativeChildProcessExitCallback(OH\_Ability\_OnNativeChildProcessExit onProcessExit)

**Description**

Unregisters the callback used to listen for child process exit.

The parameter must implement the entry function [OH\_Ability\_OnNativeChildProcessExit](#oh_ability_onnativechildprocessexit). For details, see [Unregistering the Native Child Process Exit Callback Function](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/capi-nativechildprocess-exit-info).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Ability\_OnNativeChildProcessExit](#oh_ability_onnativechildprocessexit) onProcessExit | Entry point of the callback function to be called when the child process exits. The value cannot be nullptr. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_INVALID\_PARAM**: An input parameter is invalid.

**NCP\_ERR\_INTERNAL**: An internal error occurs.

**NCP\_ERR\_CALLBACK\_NOT\_EXIST**: The callback function is not found.

For details, see **Ability\_NativeChildProcess\_ErrCode**.

 |

#### \[h2\]OH\_Ability\_KillChildProcess()

Ability\_NativeChildProcess\_ErrCode OH\_Ability\_KillChildProcess(int32\_t pid)

**Description**

Terminates a child process created by the current process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/ysAAyq0sTmGc2Jald8hNew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062213Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=354EFE85762B6E2F13C77643C8AA06B78661CE0A4091D63BCC3B2CBA12F38F75)

This function cannot be used to terminate a child process started in SELF\_FORK mode by calling [childProcessManager.startChildProcess](../../../arkts-apis/stage-model/ohos-app-ability-childprocessmanager-child-process-management/document.md#childprocessmanagerstartchildprocess).

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t pid | PID of the child process to terminate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](#ability_nativechildprocess_errcode) | 
**NCP\_NO\_ERROR**: The call is successful.

**NCP\_ERR\_SERVICE\_ERROR**: Server error.

**NCP\_ERR\_INVALID\_PID**: The input PID is invalid.

For details, see **Ability\_NativeChildProcess\_ErrCode**.

 |
