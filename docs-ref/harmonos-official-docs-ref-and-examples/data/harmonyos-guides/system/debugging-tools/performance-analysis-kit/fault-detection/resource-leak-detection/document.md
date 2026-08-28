# Resource Leak Detection

#### Overview

Resource leaks occur when resources such as handles, threads, and memory are not correctly released during application running. As a result, the resources are occupied for a long time and cannot be used by other applications. If a type of resources is used up, the system may freeze or restart. To address resource leak problems, the system provides the resource leak detection and determination, maintenance and debugging logs, and log reporting capabilities for you to locate faults. The following describes [resource leak detection](#section19499182961220) and [resource leak log specifications](#section166893320117).

#### Basic Concepts

Resource leaks consist of the following types: memory leaks, handle leaks, and thread leaks. The system periodically samples the resource usage of the process to detect these leaks. If the resource usage exceeds the threshold, the system captures the corresponding maintenance and debugging information and reports a leak event. You can use the HiAppEvent module to subscribe to resource leak events. For details, see [Resource Leak Events](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/resource-leak-events/document.md).

#### Principles

The following table lists the resource leak detection methods.

| 
Leak Type

 | 

Detection Mechanism

 |
| :-: | :-: |
| 

Handle leak (FD\_LEAK)

 | 

Traverse the processes every 60 seconds to obtain the total number of FDs. If the number of FDs exceeds the threshold (**5000**), detailed handle information is captured and a handle leak is reported.

 |
| 

Thread leak (THREAD\_LEAK)

 | 

Traverse the processes every 60 seconds to obtain the total number of threads. If the number of threads exceeds the threshold (**700**), thread names are captured and a thread leak is reported.

 |
| 

Memory leak (MEMORY\_LEAK)

 | 

JS leak (JS\_LEAK)

 | 

Insert instrumentation code within the JVM. When the heap usage exceeds 85% or out of memory (OOM) is triggered, a heap dump is captured and a JS leak is reported.

 |
| 

Native memory leak (PSS\_MEMORY)

 | 

Monitor the application dynamic peak memory every 200 seconds. If the dynamic peak memory exceeds twice that of the average dynamic peak memory of applications, a memory leak is reported and memory control is triggered.

 |
| 

ashmem, ION and GPU memory leak (KERNEL\_MEMORY)

 | 

If the anonymous shared memory (ashmem), ION or GPU memory usage exceeds the baseline value, a memory leak is reported and maintenance and debugging information is captured.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/EU8eUYYpTZee5d216aiJHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E528B2B3EBFEB3A361B38172789AAD79FC789C4ABFF0640ECE8010C973C6B708)

1\. The thresholds and baselines in the table are defaults. If you want to set a baseline value, use the [hidebug.setAppResourceLimit](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V5/js-apis-hidebug-V5#hidebugsetappresourcelimit12) API. You are advised to call this API in the development phase instead of the release phase.

2\. VM memory usage = **heapUsed**/**totalHeap**

**heapUsed**: size of the heap used by the current VM, in KB. You can obtain the value using [hidebug.getAppVMMemoryInfo()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hidebug#hidebuggetappvmmemoryinfo12).

**totalHeap**: total size of the heap of the current VM, in KB. You can obtain the value using [hidebug.getAppVMMemoryInfo()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hidebug#hidebuggetappvmmemoryinfo12).

3\. If the application reports a **JS\_ERROR** or **CPP\_CRASH** fault and the error message contains **OutOfMemory**, refer to [Analyzing Resource Leaks](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-stability-leak-way#section728319329442) to locate the fault.

#### Constraints

1\. Maintenance and debugging functionalities such as handle leak call stack, native memory leak call stack, and JS leak memory snapshot are disabled by default in the [nolog version](../../performance-analysis-kit-terminology/document.md#nolog-version) due to high overhead.

2\. If you want to obtain the JS memory leak snapshot of the nolog version, you can subscribe to the JS memory snapshot of the nolog version by referring to [Subscribing to Resource Leak Events (ArkTS)](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/resource-leak-events/subscribing-to-resource-leak-events-arkts/document.md).

#### Obtaining Logs

Resource leak logs are managed by the **LeakDetector** module and can be obtained in any of the following ways:

-   Method 1: Use [DevEco Testing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/devecotesting-V5) to obtain logs.
    
    DevEco Testing collects resource leak logs in **/data/log/reliability/resource\_leak/** of the device and displays the logs by process name, fault, and time.
    
    | 
    Leak Type
    
     | 
    
    Log File Name
    
     |
    | :-: | :-: |
    | 
    
    Handle leak (FD\_LEAK)
    
     | 
    
    \[pid\]\_fd\_leak.txt
    
     |
    | 
    
    Thread leak (THREAD\_LEAK)
    
     | 
    
    \[pid\]\_thread\_leak.txt
    
     |
    | 
    
    Memory leak (MEMORY\_LEAK)
    
     | 
    
    JS leak (JS\_LEAK)
    
     | 
    
    memleak-js-\[process\_name\]-\[pid\]-\[tid\]-\[timestamp\].rawheap
    
     |
    | 
    
    Native memory leak (PSS\_MEMORY)
    
     | 
    
    memleak-native-\[process\_name\]-\[pid\]-sample.txt
    
    memleak-native-\[process\_name\]-\[pid\]-smaps.txt
    
    memleak-native-\[process\_name\]-\[pid\]-\[timestamp\].txt
    
     |
    | 
    
    ashmem, ION and GPU memory leak (KERNEL\_MEMORY)
    
     | 
    
    memleak-kernel-\[module\]-0-sample.txt
    
    memleak-kernel-\[module\]-0-\[timestamp\].txt
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/ydDrLlDUSaOI_FIGnirtwQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBB4EA80A138E62599F24CF669121CF97DF22D78FEF0DCA94E46F91BC65726DA)
    
    1\. To open the native memory leak call stack (**memleak-native-\[process\_name\]-\[pid\]-\[timestamp\].txt**) in DevEco Studio, change the file name extension to **.nas** and use DevEco Studio of the latest version.
    
    2\. The JS leak maintenance and debugging log file (**memleak-js-\[process\_name\]-\[pid\]-\[tid\]-\[timestamp\].rawheap**) is a binary memory snapshot file. You need to use [rawheap-translator](../../../debugging-commands/command-line-utilities/rawheap-translator/document.md) to convert the file to a **.heapsnapshot** file and open the file using DevEco Studio or a browser. For details, see [Importing Heap Snapshots Offline](../../../../../performance-optimization/memory-leak-analysis-snapshot/basic-operations-with-memory-snapshot-analysis/document.md#section6760173514388).
    
-   Method 2: Use DevEco Studio to collect logs.
    
    The **profiler** module of DevEco Studio provides two log collecting modes: **[Allocation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-insight-session-allocations-V5)** (obtain the native call stack profiler) and **[Snapshot](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-insight-session-snapshot-V5)** (obtain JS heap dumps).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/W5i3cI7bSKSlQ7Y4Twf5bg/en-us_image_0000002497916886.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F39F8534E330A9E605BE1D5F2CAD131FE030B2ADAA3E6663F7684A9546AF5D3)
    

-   Method 3: Use HiAppEvent APIs to subscribe to resource leak events.
    
    HiAppEvent provides APIs to subscribe to various fault logs. For details, see [Introduction to HiAppEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/hiappevent-intro-V5). For details about how to subscribe to resource leak events, see [Resource Leak Event Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/hiappevent-watcher-resourceleak-events-V5). Resource leak logs are stored in **/data/storage/el2/log/resourcelimit/** and named in **RESOURCE\_OVERLIMIT\_\[TIMESTAMP\]\_\[PID\].log** format. The log content identifies the file type.
    

#### Specifications of Handle Leak Logs

Fault log: **\[pid\]\_fd\_leak.txt** (Method 1) or **RESOURCE\_OVERLIMIT\_\[TIMESTAMP\]\_\[PID\].log** (Method 3).

## Log Header Information

| 
Field

 | 

Description

 |
| :-- | :-- |
| 

time

 | 

Fault occurrence time.

 |
| 

pid

 | 

PID of the failed process, which can be used to search for related process information in the HiLog logs.

 |
| 

process

 | 

Application bundle name.

 |
| 

leaked fd nums

 | 

Number of leaked FDs (using snapshot).

 |

time: 2024/06/27 11:55:28
pid: 1380
process: process1
leaked fd nums: 1831

## Detailed Handle Type Information

-   **Leaked fd Top 10**: Lists the leaked FDs by the number of handles. The first column indicates the number of leaked handles, and the second column indicates the leak type. As shown in the following example, the ashmem leak ranks No.1 due to 1337 handles.
    
    FdCount FileDescriptor
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    Leaked fd Top 10:
    1337 ashmem
    259 socket
    119 dmabuf
    48 eventfd
    42 sync\_file
    17 eventpoll
    3 /sys/kernel/debug/tracing/trace\_marker
    3 /dev/null
    2 /dev/hvgr0
    
-   **Dir Type Top 10**: Lists the leaks by directory. It is hard to identify the specific leak in **Leaked fd Top 10**. However, as indicated by the following example, FDs leak in **/data/storage/el2/database/rdb**, which indicates a database leak.
    
    Dir Type Top 10:
    6175 /data/storage/el2/database/rdb
    5 /dev/urandom
    3 /sys/kernel/debug/tracing/trace\_marker
    3 /dev/null
    1 anon\_inode:\[signalfd\]
    1 /dev/binder
    1 /proc/
    1 /system/app/PhoneClone/PhoneClone.hap
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/q-Kn2batTLGHFeH0aJN3mA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6FFD4F9A6D3FE463EB0D34ADABF2A8C8F36F01937500CD11AC91E357CB49612)
    
    If handles in **Dir Type Top 10** and **Leaked fd Top 10** are unknown, the maintenance and debugging capability does not have the permission to obtain the handles of the leaked processes.
    

## Maintenance and Debugging Information About Special Handles

If **Leaked fd Top 10** contains information about the ashmem, socket, pipe, sync\_file, or dmabuf type and the number of handles of this type exceeds 1000, detailed maintenance and debugging information about the entire system is also provided. The details are as follows:

-   **Handle of the ashmem type**
    
    If the top 1 handle type is ashmem, detailed ashmem information of the entire system is captured, as listed in the following table.
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Process\_name
    
     | 
    
    Bundle name of the application process that holds the ashmem block.
    
     |
    | 
    
    Process\_ID
    
     | 
    
    PID of the failed process, which can be used to search for related process information in the HiLog logs.
    
     |
    | 
    
    Fd
    
     | 
    
    Handle held by the process.
    
     |
    | 
    
    Applicant\_Pid
    
     | 
    
    PID of the process that applies for the ashmem block. Based on this PID, you can identify the source of the ashmem block.
    
     |
    | 
    
    Ashmem\_name
    
     | 
    
    Name of the ashmem block, which is set by using the corresponding API. It is used to determine the storage resource type and point to different domains.
    
     |
    | 
    
    Size
    
     | 
    
    Size of the ashmem block, in bytes.
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/2xn2LxyoTQiuGdu7Ij9OqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F2962B7D159A2CE736BFB2D65A3103BC5357D5DC437484D634391A723F4BCDC)
    
    APIs for setting the ashmem memory:
    
    [JS API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#setmemorynamesync13): **setMemoryNameSync**
    
    [Native API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_setmemoryname): **OH\_PixelmapNative\_SetMemoryName**
    
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    LOGGER\_MEMCHECK\_ASHMEM\_INFO
    Process ashmem detail info:
    ---------------------------------------------------------------------------------
    Process\_name Process\_ID Fd Cnode\_idx Applicant\_Pid Ashmem\_name Size
    process1 781 18 328233 781 dev/ashmem/PolicyVolumeMap 384
    ...........
    ...........
    
-   **Handle of the socket type**
    
    If the top 1 handle type is socket, detailed information about the socket memory of the entire device is captured, as listed in the following table.
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    ProcessName
    
     | 
    
    Bundle name of the application process that holds the socket block.
    
     |
    | 
    
    ProcessID
    
     | 
    
    PID of the failed process, which can be used to search for related process information in the HiLog logs.
    
     |
    | 
    
    Fd
    
     | 
    
    Handle held by the process.
    
     |
    | 
    
    inode
    
     | 
    
    Information about file system object.
    
     |
    | 
    
    PeerTid
    
     | 
    
    TID of the peer end connected via the socket (the value is **0** for a connectionless socket).
    
     |
    
    Process socket info:
    ----------------------------------------------------
    ProcessName ProcessID Fd inode PeerTid
    process1   6874   3   0    0
    ........
    .........
    
-   **Handle of the pipe type**
    
    If the top 1 handle type is pipe, detailed information about the pipe memory of the entire device is captured, as listed in the following table.
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    ProcessName
    
     | 
    
    Bundle name of the application process that holds the pipe block.
    
     |
    | 
    
    ProcessID
    
     | 
    
    PID of the failed process, which can be used to search for related process information in the HiLog logs.
    
     |
    | 
    
    Fd
    
     | 
    
    Handle held by the process.
    
     |
    | 
    
    PipeName
    
     | 
    
    Pipe name.
    
     |
    | 
    
    inode
    
     | 
    
    Information about file system object.
    
     |
    | 
    
    MaxUsage
    
     | 
    
    Maximum usage.
    
     |
    | 
    
    NumAccounted
    
     | 
    
    Accumulated usage.
    
     |
    | 
    
    RingSize
    
     | 
    
    Size of the ring buffer, in KB.
    
     |
    
    Process pipe info:
    ------------------------------------
    ProcessName ProcessID Fd PipeName inode MaxUsage NumAccounted RingSize
    process1 629 7 / 11 16 16 16
    process1 629 8 / 11 16 16 16
    ........
    
-   **Handle of the sync\_file type**
    
    If the top 1 handle type is sync\_file, detailed information about sync\_file of the entire device is captured, as listed in the following table.
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    ProcessName
    
     | 
    
    Bundle name of the application process that holds the sync\_file block.
    
     |
    | 
    
    ProcessID
    
     | 
    
    PID of the failed process, which can be used to search for related process information in the HiLog logs.
    
     |
    | 
    
    Fd
    
     | 
    
    Handle held by the process.
    
     |
    | 
    
    FenceName
    
     | 
    
    Name of sync\_file.
    
     |
    | 
    
    inode
    
     | 
    
    Information about file system object.
    
     |
    | 
    
    FenceNum
    
     | 
    
    Number of fences.
    
     |
    | 
    
    TimelineName
    
     | 
    
    Timeline name of the fence.
    
     |
    | 
    
    DriverName
    
     | 
    
    Driver name.
    
     |
    | 
    
    Status
    
     | 
    
    Status of the fence.
    
     |
    | 
    
    Timestamp
    
     | 
    
    Timestamp of the fence.
    
     |
    
    Process fence info:
    ----------------------------------------------------
    ProcessName ProcessID Fd FenceName inode FenceNum TimelineName DriverName Status Timestamp
    process1 1309 25 NULL 4186 1 0:online\_composer\_gfx\_primary ukmd\_release\_fence\_2941430 1 91607485502500
    process1 1309 26 NULL 4186 1 0:online\_composer\_gfx\_primary ukmd\_release\_fence\_2941430 1 91607485502500
    ........
    
-   **Handle of the dmabuf type**
    
    If the top 1 handle type is dmabuf (ION memory), detailed information about the dmabuf of the entire device is captured, as listed in the following table.
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Process name
    
     | 
    
    Bundle name of the application process that holds the **ION** block.
    
     |
    | 
    
    Process ID
    
     | 
    
    PID of the failed process, which can be used to search for related process information in the HiLog logs.
    
     |
    | 
    
    Fd
    
     | 
    
    Handle held by the process.
    
     |
    | 
    
    size
    
     | 
    
    Buffer size, in bytes.
    
     |
    | 
    
    magic
    
     | 
    
    Unique ID of the buffer. If the values of **magic** are the same, the same buffer is pointed to.
    
     |
    | 
    
    buf->pid
    
     | 
    
    PID of the process that requests the buffer.
    
     |
    | 
    
    buf->task\_comm
    
     | 
    
    Name of the process that applies for the buffer.
    
     |
    
    Process dma\_heap info:
    ----------------------------------------------------
        Process name       Process ID               fd             size            magic         buf->pid   buf->task\_comm
        process1              971               23          3145728               36              971       process2
        process1              971               24          1048576               38              971       process2
       ........
    

## Handle Stack Information

When a handle leak occurs, the system calls such as **pipe** and **open** of the process are hooked for 10 minutes to capture call stacks, which are sorted by type. Each line in the following example is a call stack. The stacks are called from right to left. The number following **num** indicates the total number of call stacks, and the list following **bt** indicates the specific call stacks. You can use [addr2line](https://llvm.org/docs/CommandGuide/llvm-symbolizer.html) to parse a stack to specific functions.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
LOGGER\_MEMCHECK\_FD\_STACK\_INFO
pid: 12326
get stack time: 2024/06/17 19:16:48
==============================FdTrack Stack==============================
Generated by HiviewDFX @OpenHarmony
==============================Sorted by num==============================
num 8272 bt \[/system/lib64/libfdleak\_tracker.so+0x1fb58\] \[/system/lib/ld-musl-aarch64.so.1+0x1d3154\] \[/system/lib/ld-musl-aarch64.so.1+0x148940\] \[/system/lib64/platformsdk/libuv.so+0x1ab30\] \[/system/lib64/platformsdk/libuv.so+0x1cbd0\] \[/system/lib64/module/file/libfs.z.so+0x17109c\] \[/system/lib64/module/file/libfs.z.so+0x170af4\] \[/system/lib64/module/file/libfs.z.so+0x1701c8\] \[/system/lib64/platformsdk/libace\_napi.z.so+0x34828\] 
num 3968 bt \[/system/lib64/libfdleak\_tracker.so+0x1fb58\] \[/system/lib/ld-musl-aarch64.so.1+0x1d3154\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4ac64\] \[/system/lib64/platformsdk/libbackup\_kit\_inner.z.so+0x532d4\] \[/system/lib64/platformsdk/libbackup\_kit\_inner.z.so+0x4f8fc\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x38420\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4e99c\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4eb34\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4edc8\] 
num 3968 bt \[/system/lib64/libfdleak\_tracker.so+0x1fb58\] \[/system/lib/ld-musl-aarch64.so.1+0x1d3154\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4ac64\] \[/system/lib64/platformsdk/libbackup\_kit\_inner.z.so+0x532b0\] \[/system/lib64/platformsdk/libbackup\_kit\_inner.z.so+0x4f8fc\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x38420\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4e99c\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4eb34\] \[/system/lib64/platformsdk/libipc\_core.z.so+0x4edc8\] 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/6VS-B9c4Q6-dycFSLMl8hA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3017B8939E6027BDF390CDAA01F936951C665DFDED5C8A19ACD2A766AEB565C1)

1\. All the call stacks that apply for handles within 10 minutes are collected, including the closed call stacks.

2\. Stack information is available only in the log version. If **Developer options** is not enabled in the nolog version, stack information is not captured. If stack information is not captured, enable **System resource leak log** in **Developer options** and restart the device to capture stack information.

#### Thread Leak Log Specifications

Fault log: **\[pid\]\_thread\_leak.txt** (**Method 1**) or **RESOURCE\_OVERLIMIT\_\[TIMESTAMP\]\_\[PID\].log** (**Method 3**).

## Log Header Information

| 
Field

 | 

Description

 |
| :-- | :-- |
| 

time

 | 

Time when thread leak is detected.

 |
| 

pid

 | 

PID of the failed process, which can be used to search for related process information in the HiLog logs.

 |
| 

vss

 | 

All the address spaces that are accessible to a process, including the part that has not yet resided in memory. (Unit: KB)

 |
| 

rss

 | 

Memory size actually occupied by a process, including the total memory size of the shared library used by the process. (Unit: KB)

 |
| 

process

 | 

Bundle name of the faulty application.

 |
| 

summary

 | 

Total number of process threads when a leak is identified.

 |

time: 2024/06/27 03:45:19
pid: 41897
vss: 12783644
rss: 2229352
process: process1
summary: 879

## Thread Leak Information

-   **Top 10 Thread Name**: lists the top 10 thread leaks by thread name. The first column indicates the number of leaked threads, and the second column indicates the thread name. If the thread name is not specified when a thread is created, the thread name is the same as the process name.
    
    Top 10 Thread Name:
    913 process1
    3 gpu-work-client
    2 OS\_Actor\_402
    1 IPC\_11\_13795
    1 IPC\_12\_13796
    1 IPC\_13\_13797
    

-   **Thread startup information**: provides information about the thread startup time.
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    tid
    
     | 
    
    ID of the thread that is not released when a leak is detected.
    
     |
    | 
    
    thread\_name
    
     | 
    
    Name of the thread that is not released.
    
     |
    | 
    
    start\_time(jiffies)
    
     | 
    
    Time when the thread is created.
    
     |
    
    \======================================================
    tid thread\_name start\_time(jiffies)
    221 process1 4688297
    240 IPC\_3\_4318 3081382
    ...
    ...
    

-   **Thread snapshot**: provides the call stack of the thread when a leak occurs. In the call stack, you can view the task executed on the thread to infer the reason why the thread does not exit. For example, **\_\_pthread\_cond\_timedwait** indicates that the thread is waiting to be woken up.
    
    \======================================================
    Result: 0 ( no error )
    Timestamp:2024-06-27 03:45:20.000
    Pid:41897
    Uid:1013
    Process name:process1
    Tid:1527, Name:xxx
    #00 pc 00000000001b6464 /system/lib/ld-musl-aarch64.so.1(\_\_timedwait\_cp+192)(98dc7600a0fc62125e291b93ca336154)
    #01 pc 00000000001b8468 /system/lib/ld-musl-aarch64.so.1(\_\_pthread\_cond\_timedwait+188)(98dc7600a0fc62125e291b93ca336154)
    #02 pc 00000000000c108c /system/lib64/libc++.so(std::\_\_h::condition\_variable::wait(std::\_\_h::unique\_lock<std::\_\_h::mutex>&)+20)(9cbc937082b3d7412696099dd58f4f78242f9512)
    #03 pc 000000000024654c /system/lib64/platformsdk/xxx.so(mindspore::Worker::WaitUntilActive()+204)(534ce78b66262dc14658c35fa018662f)
    #04 pc 000000000023da14 /system/lib64/platformsdk/xxx.so(mindspore::ActorWorker::RunWithSpin()+256)(534ce78b66262dc14658c35fa018662f)
    #05 pc 000000000023edb0 /system/lib64/platformsdk/xxx.so(void\* std::\_\_h::\_\_thread\_proxy\[abi:v15004\]<std::\_\_h::tuple<std::\_\_h::unique\_ptr<std::\_\_h::\_\_thread\_struct, std::\_\_h::default\_delete<std::\_\_h::\_\_thread\_struct>>, void (mindspore::ActorWorker::\*)(), mindspore::ActorWorker\*>>(void\*)+60)(534ce78b66262dc14658c35fa018662f)
    #06 pc 00000000001baac0 /system/lib/ld-musl-aarch64.so.1(start+236)(98dc7600a0fc62125e291b93ca336154)
    ........
    

#### JS Memory Leak Log Specifications

Fault log: **memleak-js-\[process\_name\]-\[pid\]-\[tid\]-\[timestamp\].rawheap** (**Method 1**) or **RESOURCE\_OVERLIMIT\_\[TIMESTAMP\]\_\[PID\].log** (**Method 3**)

This file records object details. To view the **.rawheap** file, use [rawheap-translator](../../../debugging-commands/command-line-utilities/rawheap-translator/document.md) to convert the file into a **.heapsnapshot** file, and then use DevEco Studio or a browser to open the **.heapsnapshot** file. For details, see [Analyzing Snapshot Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V13/ide-arkts-memory-leak-analysis-V13).

#### Native Memory Leak Log Specifications

Fault log: **RESOURCE\_OVERLIMIT\_\[TIMESTAMP\]\_\[PID\].log** (Method 3) or **memleak-native-\[process\_name\]-\[pid\]-sample.txt** (Method 1).

## Memory Sampling

The **memleak-native-\[process\_name\]-\[pid\]-sample.txt** file contains the process ID, process name, baseline value, and memory sampling information, in which you can view the memory change.

| 
Field

 | 

Description

 |
| :-- | :-- |
| 

SoftThreshold

 | 

Process threshold set by the system (or set by the application using **setAppResourceLimit()**), in KB. If the application memory usage exceeds the threshold for five consecutive times, a memory leak event is reported.

 |
| 

HardThreshold

 | 

Process hard threshold set by the system, in KB. If the application memory usage exceeds the hard threshold for two consecutive times, a memory leak event is reported.

 |
| 

PSS

 | 

Proportional resident memory size, in KB. The memory size of the shared library is evenly allocated based on the number of processes. The PSS usage of a process is accurately calculated at the time marked with an asterisk (\*).

 |
| 

Offset

 | 

Offset of the allocation of the shared library, in KB. You can estimate the PSS value without asterisks (\*) by using the following formula: **RSS** + **Offset** = **PSS**.

 |
| 

RSS

 | 

Total resident memory size of the process in the physical memory (including the total memory occupied by the shared library), in KB.

 |
| 

SwapPSS

 | 

Total memory size that is written to the swap space by the process, in KB.

 |
| 

TotalPSS

 | 

Total PSS usage of the process, in KB.

 |
| 

AvcMem

 | 

Memory created by the process when the process creates a codec instance through **Avcodec\_service**. The memory is reported by **Avcodec\_service** to HiView for statistics collection. The unit is KB.

 |
| 

MediaMem

 | 

Memory created by the process through the **Media\_service** API. The memory is reported by **Media\_service** to HiView for statistics collection. The unit is KB.

 |
| 

GPU

 | 

GPU memory used by the process, in KB.

 |
| 

ION

 | 

ION memory used by the process, in KB.

 |
| 

TotalMem

 | 

Total memory size used by the process, in KB. **TotalMem** = **TotalPSS** + **ION** + **GPU** + **AvcMem** + **MediaMem**.

 |
| 

Level

 | 

Leak level of the process.

 |
| 

RunningTime

 | 

Current lifecycle of the process, in seconds.

 |
| 

Realtime

 | 

Real time of the sampling.

 |

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
/\*                  \*\*\*\*\* READ ME \*\*\*\*\*                      \*
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
/\*                 RSS: Resident Set Size                    \*
/\*                 PSS: Proportional Set Size                \*
/\*                 RSS + Offset = PSS                        \*
/\*                 TotalPSS = PSS + SwapPSS                  \*
/\*   TotalMem = TotalPSS + Av\_Mem + Media\_Mem + ION + GPU    \*
/\*                 \*\*\*\*\* Two Modes \*\*\*\*\*                     \*
/\*      Estimate Mode: RSS & SwapPSS is real                 \*
/\*      Real Mode(Realtime with \*): everything is real       \*
/\*      Media\_rss:apply mem through media\_service            \*
/\*      Avc\_rss:apply mem through avcodec\_service            \*
/\*    ~ means negligible memory(safe to ignore in analysis)  \*
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
/\*                   \*\*\*\*\* Attention \*\*\*\*\*                   \*
/\*    Formulas about TotalMem and sub-items may change,      \*
/\*    please reference current annotation formula            \*
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

pid: XXXX
processName: XXXXXX
SoftThreshold: 3500(KB)
HardThreshold: 1024000(KB)

Index   RSS(KB)     Offset(KB)  PSS(KB)     SwapPSS(KB)     TotalPSS(KB)     MediaMem(KB)   AvcMem(KB)    GPU(KB)       ION(KB)       TotalMem(KB)     Level   RunningTime(s)     Realtime
1       14668       0           14668       5500            20168            ~              ~             ~             ~             20168            W       112             2025/04/23 12:28:02
2       12732       0           12732       5476            18208            ~              ~             ~             ~             18208            W       352             2025/04/23 12:32:01
3       13560       0           13560       5456            19016            ~              ~             ~             ~             19016            W       592             2025/04/23 12:36:02
4       13576       0           13576       5440            19016            ~              ~             ~             ~             19016            W       832             2025/04/23 12:40:02
5       13576       0           13576       5440            19016            ~              ~             ~             ~             19016            W       1072            2025/04/23 12:44:02
6       13584       -8320       5264        5440            10704            ~              ~             ~             ~             10704            W       1072            \*2025/04/23 12:44:02
7       12984       -8320       4664        5084            9748             ~              ~             ~             ~             9748             W       1312            2025/04/23 12:48:02

## Memory Maintenance and Debugging

Log file: **memleak-native-\[process\_name\]-\[pid\]-smaps.txt**

| 
Field

 | 

Description

 |
| :-- | :-- |
| 

RealPssMemory

 | 

PSS value collected at **realtime**, in KB.

 |
| 

LOGGER\_MEMCHECK\_MEMINFO

 | 

Memory information of the device, including **MemTotal** and **MemFree**.

 |
| 

LOGGER\_MEMCHECK\_SMAPS\_INFO

 | 

smaps information of the process.

 |
| 

LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO

 | 

Information about two jemalloc allocations of the process (the interval between the two records is 5 minutes). The system captures the memory stack based on this information.

 |
| 

LOGGER\_MEMCHECK\_DETIAL\_INFO

 | 

jemalloc snapshot details of the process.

 |

Generated by HiviewDFX @OpenHarmony
LOGGER\_MEMCHECK\_GERNAL\_INFO
 pidNumber: 2017
 processName: process1
 PidStartTime: 1602
 RealPssMemory: 83505

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
LOGGER\_MEMCHECK\_MEMINFO
MemTotal:                             11332540 kB
MemFree:                               1686056 kB
......

LOGGER\_MEMCHECK\_SMAPS\_INFO
-------------------------------\[memory\]-------------------------------
                                    Shared      Shared      Private     Private                                                     
Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts                        Name
2048        0           0           0           0           0           0           0           0           1                             /dev/\_\_parameters\_\_/param\_sec\_dac         
.......

LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO

            size       allocated         nmalloc         ndalloc

               8           17384          511848          509675
              16          129376          338438          330352
              32         1138816         1026155          990567
              48         3161808         1322095         1256224
              64         1869376          908151          878942
......

\*\*\*\*\*\*\*\*\*\*\*\* endl \*\*\*\*\*\*\*\*\*\*\*\*

LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO

            size       allocated         nmalloc         ndalloc

               8           17384          511848          509675
              16          129376          338438          330352
              32         1138816         1026155          990567
              48         3161808         1322095         1256224
              64         1869376          908151          878942
......

\*\*\*\*\*\*\*\*\*\*\*\* endl \*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
LOGGER\_MEMCHECK\_PROC\_INFO
ASHMEM\_PROCESS\_INFO
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
Process\_name Process\_ID Fd Cnode\_idx Applicant\_Pid Ashmem\_name Virtual\_size Physical\_size magic
XXXXX           816             22      328234  816     dev/ashmem/PolicyVolumeMap      541             4096            7
\*\*\*\*\*\*\*\*\*\*\*\* endl \*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
LOGGER\_MEMCHECK\_DETIAL\_INFO
allocated         nmalloc   (#/sec)         ndalloc   (#/sec)       nrequests   (#/sec)           nfill   (#/sec)          nflush   (#/sec)
small:                      183785560        12591759       619        10371251       510         1289491        63         1313204        64          956094        47
large:                       31059968            3359         0            2946         0            3359         0            3359         0               0         0
total:                      214845528        12595118       619        10374197       510         1292850        63         1316563        64          956094        47

......

bins:           size ind    allocated      nmalloc (#/sec)      ndalloc (#/sec)    nrequests   (#/sec)  nshards      curregs     curslabs  nonfull\_slabs regs pgs   util       nfills (#/sec)     nflushes (#/sec)       nslabs     nreslabs (#/sec)      n\_lock\_ops (#/sec)       n\_waiting (#/sec)      n\_spin\_acq (#/sec)  n\_owner\_switch (#/sec)   total\_wait\_ns   (#/sec)     max\_wait\_ns  max\_n\_thds
8   0       198920       163820       8       138955       6       119703         5        1        24865           56             19  512   1  0.867         6526       0         4008       0           96        26995       1           10990       0               0       0               0       0            1226       0               0         0               0           0
16   1      1802688      1143707      56      1031039      50       221165        10        1       112668          563            309  256   1  0.781       105471       5        82548       4         1942        80503       3          191126       9               0       0              14       0            4316       0               0         0               0           0
32   2      9954560      1867465      91      1556385      76       267993        13        1       311080         2614            503  128   1  0.929       177825       8       136745       6         7713       176923       8          325128      15               2       0              52       0            8139       0               0         0               0           1
48   3     35382816      3763756     185      3026614     148       300952        14        1       737142         2953            220  256   3  0.975       371881      18       283650      13        12022        60637       2          667997      32               2       0              17       0            2725       0               0         0               0           1
......

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/L6RZPxEqSkSnNoQVq3yisA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B66B5A260F8E17E5C6898E79D45DA11906D5D41A52FCA4054EA119E4E6CDAA7)

**LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO** and **LOGGER\_MEMCHECK\_DETIAL\_INFO** are jemalloc snapshots of a process. The differences are as follows:

1\. **LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO**: The maintenance and debugging sampling is performed twice consecutively at an interval of 5 minutes. The content contains four columns of memory application information, including **size**, **allocated**, **nmalloc**, and **ndalloc**.

2\. **LOGGER\_MEMCHECK\_DETIAL\_INFO**: The maintenance and debugging sampling is performed only once. The content contains complete jemalloc information of the process.

## Memory Stack

Stack information log file: **memleak-native-\[process\_name\]-\[pid\]-\[timestamp\].txt**

-   The 15-minute process memory trace captured after the leak is detected can be loaded to DevEco Studio for parsing by clicking **Open File**, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/UD0GC-kbTuWzbyFUt6fRLw/en-us_image_0000002529596883.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B8EEBC9B56A0E880B32E9DE23DCB338D6B012F00988066A534342BD3871A541)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/p2P4OKMISRuYJcE0N13ccA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA100768E7F1A44954823D17134803349BF8F1F10E6FC923D7B3679645D0B2A4)
    
    To open the **memleak-native-\[process\_name\]-\[pid\]-\[timestamp\].txt** file in DevEco Studio, change the file name extension to **.nas**.
    
-   Select **All Heap** to display the captured memory information, which records the stacks of system calls (such as **malloc**) hooked. Native logs display the call stack in the so. file and offset address (each line indicates the call stack of a memory allocation behavior). Further analysis is required based on the symbol table.
    
    Click **Call Trees** to view the call stack of the captured process. Select **Created & Existing** to sort the memory blocks based on the proportion of unreleased memory. You can view the detailed process call information and preferentially check the stack with high memory usage.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/b2ylKXZ7QumIqMG20qpRBw/en-us_image_0000002529716857.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6590E181EA2DF7BB4151C808060C271BF6F59DB85F02ACDDE673565385DBEC0C "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/UvhfQwMrTqqksYty_qCnYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F565FF9A2574CD8CCB407A296C6B28D0B3058569FFF4EF61735B524BC3097372)
    
    1\. As shown in **Created & Existing**, since only the stack information and memory requests within 15 minutes are captured, the leaks of some stacks may not be large or much smaller than the detected peak memory usages. Actually, the leak accumulates over a long time period, which is measured in dozens or even hundreds of hours. As a result, the size of the reported leak is large.
    
-   Select **All Anonymous VM** to display the stack information of the hooked **mmap** system call.
    
    If you select **Created & Existing**, the memory that is requested but not released of the hooked call is captured. The longer the length, the more the remaining memory is occupied. Check the longer process first.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/LxmqGvgKRDuFIYbWuI1t_w/en-us_image_0000002497756910.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF81F84AFC2A7C039973CC38FA5AC7F3E643163A5A1152314505590EC7826D1B "Click to enlarge")
    

#### Log Specifications of ashmem, ION, GPU, and GPU\_RS Memory Leaks

## Memory Sampling

-   Log file: **memleak-kernel-\[module\]-0-sample.txt** (Method 1) or **RESOURCE\_OVERLIMIT\_\[TIMESTAMP\]\_\[PID\].log** (Method 3).
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    memoryName
    
     | 
    
    Kernel memory. If memory leaks occur in a process (the system baseline is exceeded), the name of the process is displayed. If the value of **memoryName** is **ashmem**, **gpu** or **ion**, no memory leak occurs.
    
     |
    | 
    
    softThreshold
    
     | 
    
    Soft threshold, in KB. When the soft threshold is exceeded for more than eight sampling periods (more than 30 minutes), a memory leak is identified.
    
     |
    | 
    
    hardThreshold
    
     | 
    
    Hard threshold, in KB. Once the hard threshold is exceeded, a memory leak is identified.
    
     |
    | 
    
    topMemory
    
     | 
    
    Peak value of the detected kernel memory usage, in KB.
    
     |
    | 
    
    LOGGER\_MEMCHECK\_MEMINFO
    
     | 
    
    Overview of the device memory information.
    
     |
    | 
    
    LOGGER\_MEMCHECK\_PROC\_INFO
    
     | 
    
    Information about the ashmem, ION, or GPU memory leak node. (The content varies according to the leak type.)
    
     |
    | 
    
    LOGGER\_PROCESS\_DMABUF\_INFO
    
     | 
    
    Special node content obtained when the ION memory leak occurs, which contains more memory block usage information.
    
     |
    | 
    
    LOGGER\_MEMCHECK\_RENDER\_SERVICE\_MEM
    
     | 
    
    Memory usage of the **Render\_service** process.
    
     |
    
    memoryName:gpu
    softThreshold:2300(MB)
    hardThreshold:3450(MB)
    topMemory:4876824(KB)
    time(s) kernelMemory(KB)realtime
    247681  4876824         2024/06/24 08:27:52
    

## Memory Maintenance and Debugging

Log file: **memleak-kernel-\[module\]-0-\[timestamp\].txt** (Method 1).

When an ashmem, GPU or ION memory leak is detected, the ashmem, GPU or ION memory information of the entire device is captured. The specifications of ashmem and ION logs are the same as those of ashmem and dmabuf handle leak logs. For details, see ashmem and dmabuf handles.

Log header:

Generated by HiviewDFX @OpenHarmony
LOGGER\_MEMCHECK\_GERNAL\_INFO
memoryName:ion
softThreshold:2800(MB)
hardThreshold:4200(MB)
appHardThreshold:4096(MB)
topMemory:0(KB)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
LOGGER\_MEMCHECK\_MEMINFO
MemTotal:       11738500 kB
MemFree:          116204 kB
MemAvailable:      95232 kB
Buffers:               0 kB

**LOGGER\_MEMCHECK\_PROC\_INFO** in the log file records the memory information based on the memory leak type. The details are as follows:

-   ashmem memory leak:
    
    LOGGER\_MEMCHECK\_PROC\_INFO
    realtime:       2025/05/30 19:52:42
    Process ashmem overview info:
    ---------------------------------------------------------------------------------
    Process\_name Virtual\_size Physical\_size
    Total ashmem  of \[XXXXXX\] virtual size is  541, physical size is 4096
    Total ashmem  of \[XXXXXX\] virtual size is  299008, physical size is 299008
    Total ashmem  of \[XXXXXX\] virtual size is  37574896, physical size is 37470208
    ......
    Process ashmem detail info:
    ---------------------------------------------------------------------------------
    Process\_name    Process\_ID      Fd      Cnode\_idx       Applicant\_Pid   Ashmem\_name     Virtual\_size    Physical\_size   magic
    XXXXX    816     22      328234  816     dev/ashmem/PolicyVolumeMap      541     4096    7
    ......
    ---------------------------------------------------------------------------------
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    LOGGER\_MEMCHECK\_RENDER\_SERVICE\_MEM
    get info realtime:      2025/05/30 19:52:42
    
    -------------------------------\[ability\]-------------------------------
    
    ----------------------------------RenderService----------------------------------
    ......
    
-   ION memory leak:
    
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    LOGGER\_MEMCHECK\_PROC\_INFO
    MM\_DMABUF\_INFO
    realtime: 2025/07/26 14:19:58
    Process pid fd size\_bytes ino exp\_pid exp\_task\_comm buf\_name exp\_name buf\_type 
    process1        1563 71 13926400 25690 11187 allocator\_host 11563 mm\_heap\_helpers xcomponent 
    process1        1563 75 1024000000 21095 11187 allocator\_host 11563 mm\_heap\_helpers NULL 
    process1        1563 77 1024000000 11557 11187 allocator\_host 11563 mm\_heap\_helpers NULL 
    process1        1563 79 1024000000 26747 11187 allocator\_host 11563 mm\_heap\_helpers NULL 
    \*\*\*\*\*\*\*\*\*\*\*\* endl \*\*\*\*\*\*\*\*\*\*\*\*
    
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    LOGGER\_MEMCHECK\_RENDER\_SERVICE\_MEM 
    get info realtime:      2025/05/30 21:17:39
    
    -------------------------------\[ability\]-------------------------------
    
    
    ----------------------------------RenderService----------------------------------
    ......
    
-   GPU/GPU\_RS memory leak:
    
    LOGGER\_MEMCHECK\_PROC\_INFO
    GPU\_PROCESS\_INFO
    render\_service
    ctx\_1       1689       1455 used summary:3362426880 grow:0 driver:10432512 kmd:3260416 jit:131072
    process1
    Channel: xx default device (Total memory: 730594)
      1:                    2 / 2
      6:                    4 / 160
      7:                    6 / 384
      8:                  163 / 20928
      9:                 1573 / 604160
     10:                   48 / 24576
     11:                    2 / 2048
     13:                    2 / 12800
     15:                    4 / 65536
    ......
    
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    LOGGER\_MEMCHECK\_RENDER\_SERVICE\_MEM
    get info realtime:      2025/05/30 21:16:01
    
    -------------------------------\[ability\]-------------------------------
    
    
    ----------------------------------RenderService----------------------------------
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/aiCgeJr1S7C_a1DGb3A-WQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46B45F59A8F1FFADDE1C2AEEA1B7CAB5F14F596EDB2232D54F7C65691B198C68)

1\. Differences between the GPU\_RS memory leak and the GPU memory leak: The GPU memory leak is caused by application self-rendering, while the GPU\_RS memory leak is caused by unified rendering through the **render\_service** process.

2\. In the resource leak information, ION, dmaheap, and dmabuf can be regarded as the same memory type.

3\. The current log specifications may changes in rows, columns, and paragraphs based on version issues and user feedback.
