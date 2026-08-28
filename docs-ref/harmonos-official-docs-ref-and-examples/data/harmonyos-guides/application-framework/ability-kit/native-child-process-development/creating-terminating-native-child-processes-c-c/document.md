# Creating/Terminating Native Child Processes (C/C++)

This module provides two methods for creating a [native child process](../../ability-kit-terminology/document.md#native-child-process) and one method for terminating a child process.

-   [Creating a Native Child Process That Supports IPC](#creating-a-native-child-process-that-supports-ipc): Create a child process and establish an inter-process communication (IPC) channel between the parent and child processes. This method applies to scenarios where the parent and child processes require IPC. Its usage depends on [IPC Kit](../../../ipc-kit/ipc-and-rpc-development-c-c/document.md).
-   [Creating a Native Child Process That Supports Pass-by-Parameter](#creating-a-native-child-process-that-supports-pass-by-parameter): Create a child process and pass the string and FD handle parameters to the child process. This method applies to scenarios where parameters need to be passed to child processes.
-   [Terminating a Child Process](#terminating-a-child-process): Terminate a [native child process](../../ability-kit-terminology/document.md#native-child-process) or an [ArkTS child process](../../ability-kit-terminology/document.md#arkts-child-process) created by the current process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/i0zKzc51SXuddOp-3Dus_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061919Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29CF3365032D8BCD1025EA5E897A180FF112C022C5F4D7E11676518D3A38C134)

The created child process will exit when the parent process exits and cannot run independently.

#### Creating a Native Child Process That Supports IPC

## When to Use

This topic describes how to create a native child process in the main process and establish an IPC channel between the main process and child process. It makes multi-process programming at the native layer easier.

## Available APIs

| Name | Description |
| :-- | :-- |
| int [OH\_Ability\_CreateNativeChildProcess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_createnativechildprocess) (const char \*libName, [OH\_Ability\_OnNativeChildProcessStarted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_onnativechildprocessstarted) onProcessStarted) | Creates a child process, loads a specified dynamic link library, and returns the startup result asynchronously through the **onProcessStarted** callback function in the parameter. The callback function runs on a separate thread. If access to shared resources is required, thread synchronization must be implemented. Due to system limitations on the number of callback threads for a single process, you are advised not to perform highly time-consuming operations within the callback function. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/IgtzGsk0RQS-vO_hvDUVxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061919Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B4E71B996AF06B37D8A995836ECB4DC9E2D6B8AF30994998F3FEEE96924AD45)

Starting from API version 14, 2-in-1 devices and tablets are supported. In API version 13 and earlier versions, only 2-in-1 devices are supported.

Starting from API version 15, a single process supports a maximum of 50 native child processes. In API version 14 and earlier versions, a single process supports only one native child process.

## How to Develop

This section describes how to use the C APIs provided by Ability Kit to create a native child process and establish an IPC channel between the main process and child process based on an existing native application development project.

**Linking Dynamic Libraries**

libipc\_capi.so
libchild\_process.so

**Including Header Files**

#include <IPCKit/ipc\_kit.h>
#include <AbilityKit/native\_child\_process.h>

1.  (Child process) Implement necessary export functions.
    
    In the child process, implement and export the functions **NativeChildProcess\_OnConnect** and **NativeChildProcess\_MainProc**. (It is assumed that the code file is named **ChildProcessSample.cpp**.) The **OHIPCRemoteStub** object returned by **NativeChildProcess\_OnConnect** is responsible for IPC with the main process. For details, see the [IPC development guide (C/C++)](../../../ipc-kit/ipc-and-rpc-development-c-c/document.md).
    
    After the child process is started, **NativeChildProcess\_OnConnect** is invoked to obtain an IPC stub object, and then **NativeChildProcess\_MainProc** is called to transfer the control right of the main thread. After the second function is returned, the child process exits.
    
    #include <IPCKit/ipc\_kit.h>
    // ...
    #include <IPCKit/ipc\_cremote\_object.h>
    #include <IPCKit/ipc\_cparcel.h>
    #include <IPCKit/ipc\_error\_code.h>
    
    class IpcCapiStubTest {
    public:
        explicit IpcCapiStubTest();
        ~IpcCapiStubTest();
        OHIPCRemoteStub \*GetRemoteStub();
        static int OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData);
    
    private:
        OHIPCRemoteStub \*stub\_{nullptr};
    };
    
    IpcCapiStubTest::IpcCapiStubTest()
    {
        // Create a stub object.
        stub\_ = OH\_IPCRemoteStub\_Create("testIpc", &IpcCapiStubTest::OnRemoteRequest, nullptr, this);
    }
    
    IpcCapiStubTest::~IpcCapiStubTest()
    {
        if (stub\_ != nullptr) {
            OH\_IPCRemoteStub\_Destroy(stub\_);
        }
    }
    
    OHIPCRemoteStub \*IpcCapiStubTest::GetRemoteStub() { return stub\_; }
    
    int IpcCapiStubTest::OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData)
    {
        return OH\_IPC\_SUCCESS;
    }
    
    IpcCapiStubTest g\_ipcStubObj;
    
    extern "C" {
    OHIPCRemoteStub \*NativeChildProcess\_OnConnect()
    {
        // ipcRemoteStub points to the IPC stub object implemented by the child process. The object is used to receive and respond to IPC messages from the main process.
        // The child process controls its lifecycle according to the service logic.
        return g\_ipcStubObj.GetRemoteStub();
    }
    
    void NativeChildProcess\_MainProc()
    {
        // Equivalent to the Main function of the child process. It implements the service logic of the child process.
        // ...
        // After the function is returned, the child process exits.
    }
    
    } // extern "C"
    
2.  (Child process) Compile a dynamic link library.
    
    Modify the **CMakeList.txt** file, compile the file into a dynamic link library (named **libchildprocesssample.so** in this example), and add the dependency of the dynamic link library of IPC Kit.
    
    add\_library(childprocesssample SHARED
        # Source code file that implements the necessary export functions
        ChildProcessSample.cpp
        
        # Other source code files
        # ...
    )
    
    target\_link\_libraries(childprocesssample PUBLIC
        # Add the dependency of the dynamic link library of IPC Kit.
        libipc\_capi.so
        
        # Dependencies of other dynamic link libraries
        # ...
    )
    
3.  (Main process) Implement the child process startup result callback.
    
    #include <IPCKit/ipc\_kit.h>
    #include <AbilityKit/native\_child\_process.h>
    // ···
    static void OnNativeChildProcessStarted(int errCode, OHIPCRemoteProxy \*remoteProxy)
    {
        if (errCode != NCP\_NO\_ERROR) {
            // Exception handling when the child process is not started normally
            // ...
            return;
        }
    
        // Save the remoteProxy object for IPC with the child process based on the APIs provided by IPC Kit.
        // You are advised to transfer time-consuming operations to an independent thread to avoid blocking the callback thread for a long time.
        // When the IPC object is no longer needed, call OH\_IPCRemoteProxy\_Destroy to release it.
        // ···
    }
    
    The second parameter **OHIPCRemoteProxy** in the callback function is used to establish an IPC channel with the **OHIPCRemoteStub** object returned by the **NativeChildProcess\_OnConnect** method implemented by the child process. For details, see the [IPC development guide (C/C++)](../../../ipc-kit/ipc-and-rpc-development-c-c/document.md). When the **OHIPCRemoteProxy** object is no longer needed, call [OH\_IPCRemoteProxy\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ipc-cremote-object-h#oh_ipcremoteproxy_destroy) to release it.
    
4.  (Main process) Start the native child process.
    
    Call the API to start the native child process. Note that the return value **NCP\_NO\_ERROR** only indicates that the native child process startup logic is successfully called. The actual startup result is asynchronously notified through the callback function specified in the second parameter. Note that **a child process can be created only on the main process.**
    
    #include <IPCKit/ipc\_kit.h>
    #include <AbilityKit/native\_child\_process.h>
    // ···
    static void OnNativeChildProcessStarted(int errCode, OHIPCRemoteProxy \*remoteProxy)
    {
        if (errCode != NCP\_NO\_ERROR) {
            // Exception handling when the child process is not started normally
            // ...
            return;
        }
    
        // Save the remoteProxy object for IPC with the child process based on the APIs provided by IPC Kit.
        // You are advised to transfer time-consuming operations to an independent thread to avoid blocking the callback thread for a long time.
        // When the IPC object is no longer needed, call OH\_IPCRemoteProxy\_Destroy to release it.
        // ...
        // ···
    }
    
    void CreateNativeChildProcess()
    {
        // The first parameter libchildprocesssample.so indicates the name of the dynamic link library that implements the necessary export functions of the child process.
        int32\_t ret = OH\_Ability\_CreateNativeChildProcess("libchildprocesssample.so", OnNativeChildProcessStarted);
        if (ret != NCP\_NO\_ERROR) {
            // Exception handling when the child process is not started normally
            // ...
        }
        g\_result = ret;
    }
    
5.  (Main process) Add build dependencies.
    
    Modify the **CMaklist.txt** file to add the dependencies. The following assumes that the main process is implemented in the library file named **libmainprocesssample.so**. (The implementation of the main process and child processes can be compiled to the same dynamic link library file.)
    
    target\_link\_libraries(mainprocesssample PUBLIC
        # Add dependencies of the dynamic link library of IPC Kit and Ability Kit.
        libipc\_capi.so
        libchild\_process.so
        
        # Dependencies of other dynamic link libraries
        # ...
    )
    

#### Creating a Native Child Process That Supports Pass-by-Parameter

## When to Use

This section describes how to create a native child process and pass parameters to it.

## Available APIs

| Name | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#ability_nativechildprocess_errcode) [OH\_Ability\_StartNativeChildProcess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_startnativechildprocess) (const char \*entry, [NativeChildProcess\_Args](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativechildprocess-args) args, [NativeChildProcess\_Options](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativechildprocess-options) options, int32\_t \*pid) | Starts a child process and returns its PID. |

## How to Develop

**Linking Dynamic Libraries**

libchild\_process.so

**Including Header Files**

#include <AbilityKit/native\_child\_process.h>

1.  (Child process) Implement necessary export functions.
    
    In the child process, implement and export the entry function [NativeChildProcess\_Args](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativechildprocess-args). (It is assumed that the code file is named **ChildProcessSample.cpp**.) After the child process is started, the entry function is invoked. After the second function is returned, the child process exits.
    
    #include <AbilityKit/native\_child\_process.h>
    extern "C" {
    /\*\*
     \* Entry function of a child process, which implements the service logic of the child process.
     \* The function name can be customized and is specified when the main process calls the OH\_Ability\_StartNativeChildProcess method. In this example, the function name is Main.
     \* After the function is returned, the child process exits.
     \*/
    void Main(NativeChildProcess\_Args args)
    {
        // Obtain the input entryPrams.
        char \*entryParams = args.entryParams;
        // Obtain the input FD list.
        NativeChildProcess\_Fd \*current = args.fdList.head;
        while (current != nullptr) {
            char \*fdName = current->fdName;
            int32\_t fd = current->fd;
            current = current->next;
            // Implement the service logic.
        }
    }
    } // extern "C"
    
2.  (Child process) Compile a dynamic link library.
    
    Modify the **CMakeList.txt** file, compile the file into a dynamic link library (named **libchildprocesssample.so** in this example), and add the dependency of the dynamic link library of Ability Kit.
    
    add\_library(childprocesssample SHARED
        # Source code file that implements the necessary export functions
        ChildProcessSample.cpp
        
        # Other source code files
        # ...
    )
    
    target\_link\_libraries(childprocesssample PUBLIC
        # Add the dependency of the dynamic link library of Ability Kit.
        libchild\_process.so
    
        # Dependencies of other dynamic link libraries
        # ...
    )
    
3.  (Main process) Start the native child process.
    
    Call the API to start the native child process. The return value **NCP\_NO\_ERROR** indicates that the native child process is successfully started.
    
    #include <AbilityKit/native\_child\_process.h>
    #include <cstdlib>
    #include <cstring>
    #include <fcntl.h>
    // ...
    int32\_t g\_fdNameMaxLength = 20;
    
    void StartNativeChildProcess()
    {
        // ...
        NativeChildProcess\_Args args;
        // Set entryParams. The maximum amount of data that can be passed is 150 KB.
        const size\_t entryParamsSize = 10;
        args.entryParams = (char \*)malloc(sizeof(char) \* entryParamsSize);
        if (args.entryParams != nullptr) {
            (void)strlcpy(args.entryParams, "testParam", entryParamsSize);
        }
    
        // Insert a node to the head node of the linked list.
        args.fdList.head = (NativeChildProcess\_Fd \*)malloc(sizeof(NativeChildProcess\_Fd));
        // FD keyword, which contains a maximum of 20 characters.
        args.fdList.head->fdName = (char \*)malloc(sizeof(char) \* g\_fdNameMaxLength);
        if (args.fdList.head->fdName != nullptr) {
            (void)strlcpy(args.fdList.head->fdName, "fd1", g\_fdNameMaxLength);
        }
        // Obtain the FD logic.
        int32\_t fd = open("/data/storage/el2/base/haps/entry/files/test.txt", O\_RDWR | O\_CREAT, 0644);
        args.fdList.head->fd = fd;
        // Insert only one FD record. You can insert a maximum of 16 FD records to the linked list as required.
        args.fdList.head->next = NULL;
        NativeChildProcess\_Options options = {.isolationMode = NCP\_ISOLATION\_MODE\_ISOLATED};
    
        // The first parameter libchildprocesssample.so:Main indicates the name of the dynamic link library file that implements the Main method of the child process and the name of the entry method.
        int32\_t pid = -1;
        Ability\_NativeChildProcess\_ErrCode ret =
            OH\_Ability\_StartNativeChildProcess("libchildprocesssample.so:Main", args, options, &pid);
        if (ret != NCP\_NO\_ERROR) {
            // Release the memory space in NativeChildProcess\_Args to prevent memory leakage.
            // Exception handling when the child process is not started normally
            // ...
        }
    
        // Other logic
    // ...
    
        // Release the memory space in NativeChildProcess\_Args to prevent memory leakage.
    }
    
4.  (Main process) Add build dependencies.
    
    Modify the **CMaklist.txt** file to add the dependencies. The following assumes that the main process is implemented in the library file named **libmainprocesssample.so**. (The implementation of the main process and child processes can be compiled to the same dynamic link library file.)
    
    target\_link\_libraries(mainprocesssample PUBLIC
        # Add the dependency of the dynamic link library of Ability Kit.
        libchild\_process.so
        
        # Dependencies of other dynamic link libraries
        # ...
    )
    

#### Child Threads Obtaining Startup Parameters

## When to Use

Starting from API version 17, child processes can obtain startup parameters.

## Available APIs

| Name | Description |
| :-- | :-- |
| [NativeChildProcess\_Args](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativechildprocess-args)\* [OH\_Ability\_GetCurrentChildProcessArgs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_getcurrentchildprocessargs)() | Returns startup parameters of a child process. |

## How to Develop

**Linking Dynamic Libraries**

libchild\_process.so

**Including Header Files**

#include <AbilityKit/native\_child\_process.h>

**Obtaining Startup Parameters**

After a child process is created through [OH\_Ability\_StartNativeChildProcess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_startnativechildprocess), it can call [OH\_Ability\_GetCurrentChildProcessArgs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_getcurrentchildprocessargs)() to obtain the startup parameters [NativeChildProcess\_Args](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativechildprocess-args) from any .so file or child thread, facilitating operations on related file descriptors.

#include <AbilityKit/native\_child\_process.h>
#include <thread>

extern "C" {
void ThreadFunc()
{
    // Obtain startup parameters of the child process.
    NativeChildProcess\_Args \*args = OH\_Ability\_GetCurrentChildProcessArgs();
    // If the startup parameters fail to be obtained, nullptr is returned.
    if (args == nullptr) {
        return;
    }
    // Obtain the value of entryPrams in the startup parameters.
    char \*entryParams = args->entryParams;
    // Obtain the FD list.
    NativeChildProcess\_Fd \*current = args->fdList.head;
    while (current != nullptr) {
        char \*fdName = current->fdName;
        int32\_t fd = current->fd;
        current = current->next;
        // Implement the service logic.
    }
}

/\*\*
 \* Entry function of a child process, which implements the service logic of the child process.
 \* args is the startup parameters of the child process.
 \*/
void Main(NativeChildProcess\_Args args)
{
    // Implement the service logic.

    // Create a thread.
    std::thread tObj(ThreadFunc);
}

} // extern "C"

#### Terminating a Child Process

## When to Use

Starting from API version 22, you can terminate a [native child process](../../ability-kit-terminology/document.md#native-child-process) or an [ArkTS child process](../../ability-kit-terminology/document.md#arkts-child-process) created by the current process based on the input PID.

## Available APIs

| Name | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#ability_nativechildprocess_errcode) [OH\_Ability\_KillChildProcess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_killchildprocess)(int32\_t pid) | Terminates a child process created by the current process. This API can be used to terminate a [native child process](../../ability-kit-terminology/document.md#native-child-process) or an [ArkTS child process](../../ability-kit-terminology/document.md#arkts-child-process). |

## How to Develop

**Including Header Files**

#include <AbilityKit/native\_child\_process.h>

**Terminating a Child Process**

After a child process is created using [native\_child\_process](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h) and [childProcessManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-childprocessmanager) (non-SELF\_FORK mode), the main process can call [OH\_Ability\_KillChildProcess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_killchildprocess)(int32\_t pid) to terminate the child process based on the input PID.

#include <AbilityKit/native\_child\_process.h>
// ...
void KillChildProcess(int32\_t pid)
{
    Ability\_NativeChildProcess\_ErrCode ret = OH\_Ability\_KillChildProcess(pid);
    if (ret != NCP\_NO\_ERROR) {
        // Exception handling when the child process fails to be terminated
    }
    // ...
}
