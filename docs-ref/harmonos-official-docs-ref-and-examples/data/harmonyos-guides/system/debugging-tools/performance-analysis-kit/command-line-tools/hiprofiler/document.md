# hiprofiler

#### Overview

hiprofiler provides the performance profiling capabilities for you to analyze memory and performance issues.

The overall architecture includes the PC side and the device side. The main components are the data display interface on the PC side and the performance tuning service on the device side. The PC and device services use the C/S model. The profiling data on the PC is displayed on the [DevEco Studio](../../../../../environment-setup/downloading-and-installing-deveco-studio/document.md) and [SmartPerf](https://gitcode.com/openharmony/developtools_smartperf_host/releases) pages. The device program consists of multiple parts that run in the system environment. The **hiprofilerd** process communicates with DevEco Studio to provide profiling services. The device also contains the CLI tool (**hiprofiler\_cmd**) and data collection process (**hiprofiler\_plugins**). Based on the Producer-Consumer model, the profiling service controls the data collection process to obtain profiling data and sends the data to DevEco Studio. Currently, plugins such as nativehook, CPU, ftrace, GPU, hiperf, xpower, and memory have been implemented, providing comprehensive profiling capabilities for CPU, GPU, memory, and power consumption.

Benchmarking with profilers in the industry, hiprofiler provides more capabilities, such as [cross-language stack unwinding, power consumption data obtaining, and long-time heap memory stack capturing](#plugin-parameters).

#### Environment Requirements

-   The environment for HarmonyOS Device Connector (hdc) has been set up. For details, see [Environment Setup](../hdc/document.md#environment-setup).
    
-   The devices are properly connected and **hdc shell** is executed.
    

#### Architecture

1.  The PC calls the hiprofiler\_cmd tool on DevEco Studio or SmartPerf.
    
2.  The **hiprofiler\_cmd** process starts the hiprofilerd service and the **hiprofiler\_plugins** process.
    
3.  **hiprofiler\_plugins** enables the corresponding plugin and summarizes the obtained profiling data to the hiprofilerd process.
    
4.  The **hiprofilerd** process stores the profiling data in proto format to a file, or returns it to the PC in real time.
    
5.  The PC parses the data, generates lanes, and displays the obtained profiling data.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/b6V3PzeSQty12ftRRMts1w/en-us_image_0000002537765124.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0EC90E0F4A3AD2EC0F639438F31C900767A5821BEFA6207EB95F44765B45659)

#### Command Syntax

You can use hiprofiler\_cmd to call different plugins and input different parameters for different profiling requirements. The following is an example command:

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
 request\_id: 1
 session\_config {
  buffers {
   pages: 16384
  }
 }
 plugin\_configs {
  plugin\_name: "ftrace-plugin"
  sample\_interval: 1000
  config\_data {
   hitrace\_categories: "binder"
   buffer\_size\_kb: 204800
   flush\_interval\_ms: 1000
   flush\_threshold\_kb: 4096
   trace\_period\_ms: 200
  }
 }
CONFIG

| Command | Description |
| :-- | :-- |
| \-c | After setting this option, you need to place the configuration file in the **/data/local/tmp** directory and input the path. |
| \-o | Sets the custom file save path, which must start with **/data/local/tmp**. If no path is set, the profiling data is saved to **/data/local/tmp/hiprofiler\_data.htrace** by default. If the profiling is performed repeatedly, the file in the original path will be overwritten. |
| \-k | Kills the existing profiling service process. |
| \-s | Starts the profiling service process. |
| \-t | Sets the profiling duration, in seconds. |

After inputting the **hiprofiler\_cmd** parameter, input the plugin configuration information. The configuration information starts with **<<CONFIG** and ends with **CONFIG**. The content in the middle is in JSON format.

The following table describes the **session config** fields.

| Field | Description |
| :-- | :-- |
| buffers | Number of shared memory pages. |
| split\_file | Whether to split a file. The value **true** means to split the file, and **false** means the opposite. |
| split\_file\_max\_size\_mb | Maximum size of each split file when **split\_file** is set to **true**. |

The following table describes the **plugin\_configs** fields.

| Field | Description |
| :-- | :-- |
| plugin\_name | Name of the plugin to enable. |
| sample\_interval | Interval for the plugin to obtain profiling data, in milliseconds. |
| config\_data | 
Parameters of the plugin. The parameters required by each plugin are different. For details, see the **proto** definition of the plugins.

(The code path is **developtools/profiler/protos**.)

 |

Download the generated trace file to the local PC by running the **hdc file recv** command, and then upload the file to SmartPerf or DevEco Studio for parsing.

#### Plugins Supported

| Name | Description | Specifications |
| :-- | :-- | :-- |
| [native hook](#nativehook) | Obtains the call stack information about heap memory allocation. | Only [applications signed by the debug certificate](#applications-signed-by-the-debug-certificate) can be collected. |
| [ftrace plugin](#ftrace-plugin) | Obtains the trace events of kernel logging and the HiTrace logging data. | \- |
| [cpu plugin](#cpu-plugin) | Obtains the CPU usage information of a process, including the process-level and thread-level usage. | \- |
| [gpu plugin](#gpu-plugin) | Obtains the GPU usage information of a process. | \- |
| [xpower plugin](#xpower-plugin) | Obtains the power consumption information of a process. | \- |
| [memory plugin](#memory-plugin) | Obtains the memory usage of a process, primarily the data from its **smaps** node. | \- |
| [diskio plugin](#diskio-plugin) | Obtains the disk space usage of a process. | \- |
| [network profiler](#network-profiler) | Obtains the detailed HTTP/HTTPS request information of a process through process logging. | Only [applications signed by the debug certificate](#applications-signed-by-the-debug-certificate) can be collected. |
| [network plugin](#network-plugin) | Obtains the network traffic statistics of a process. | \- |
| [hisysevent plugin](#hisysevent-plugin) | Obtains the HiSysEvent event data by running the HiSysEvent commands. | \- |
| [hidump plugin](#hidump-plugin) | Obtains the related data by running the SP\_daemon commands. | \- |

#### Applications Signed by the Debug Certificate

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/QFTbqF4AQgOdIDj85r10Ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6666DD575AB3447A1BAD9950828C9610C0D09676771CD6ACB422B79A9E2625CD)

Run the **hdc shell "bm dump -n bundlename | grep appProvisionType"** command to check whether the application specified in the command is a debuggable application. The expected output is **"appProvisionType": "debug"**.

For example, run the following command to check the bundle name **com.example.myapplication**:

hdc shell "bm dump -n com.example.myapplication | grep appProvisionType"

If the application is a debug-type application, the following information is displayed:

"appProvisionType": "debug",

To build a debug application, you need to use a debug certificate for signature. For details about how to request and use the debug certificate, see [Requesting a Debug Certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugcert-0000001914263178).

#### Plugin Parameters

## nativehook

Obtains the call stack information of heap memory allocations (by the **malloc**, **mmap**, **calloc** or **realloc** function), cross-language allocations (for example, native heap memory allocated by the Node-API in ArkTS), and unreleased heap memory due to memory leaks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/-mo37LV9RMaZUa7Qrloj0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=710DB6AC2642B53F358C3F9E51AA6F8A9AE5012DA39211253B37898629CF6171)

After [an application is encrypted](../../../../security/application-encryption/document.md), stack unwinding is limited to the native stack and not supported for the JS stack.

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| fp\_unwind | bool | 
Whether to enable stack unwinding in fp mode. The value **true** means to enable stack unwinding in fp mode.

The value **false** means to enable stack unwinding in dwarf mode.

 | 

The stack unwinding in fp mode is implemented by using the x29 register, in which the function fp always points to the parent function (caller) fp. After stack unwinding, the profiling service calculates the relative PC based on the instruction pointer (IP) and searches for the corresponding mapping in maps for symbolization.

Due to increasingly aggressive compiler optimizations, register reuse and disabled fp can cause stack unwinding in fp mode to fail. In mixed stacks, the fp alone cannot capture all frames, so dwarf is required for more accurate stack rewinding.

The stack unwinding in dwarf mode is to search for the corresponding mapping information in the map table based on the PC register. The performance of dwarf is worse than that of fp because the call stack is parsed level by level in dwarf mode.

Note: fp stack unwinding does not support profiling for non-AArch64 devices.

 |
| statistics\_interval | int | Statistics interval, in seconds. Stacks in a statistics interval are summarized. | The statistics stack capture mode is provided to implement long-term lightweight collection. If profiling performance is a priority and you only need call counts and total stack size, use statistics mode. |
| process\_name | string | Name of the process for which memory profiling is to be performed. | The value must be the same as the process name in the **/proc/** node. |
| startup\_mode | bool | Whether to capture the memory during process startup. By default, the memory during process startup is not captured. | This parameter records the heap memory allocation information during the period from the start of process incubation to the end of optimization. |
| js\_stack\_report | int | 

Whether to enable cross-language stack unwinding.

The value **0** means not to capture the JS stack.

The value **1** means to capture the JS stack.

 | This parameter provides the cross-language stack unwinding feature for the Ark environment. |
| malloc\_free\_matching\_interval | int | Matching interval, in seconds. **malloc** and **free** are matched within the interval. If matched, the stack is not flushed to the disk. | Within the matching interval, the allocated and released call stacks are not recorded, reducing the overhead of the stack capture service process. If this parameter is set to a value greater than 0, you need to set **statistics\_interval** to **0**. |
| offline\_symbolization | bool | 

Whether to enable offline symbolization.

The value **true** means to enable offline symbolization;

the value **false** means the opposite.

 | When offline symbolization is used, the operation of matching symbols based on IP is performed on SmartPerf, reducing process freezes during profiling. However, since the offline symbol table is written into the trace file, the trace file generated under offline symbolization is larger in size than that under online symbolization. |
| sample\_interval | int | Sampling size. | When this parameter is set, the sampling mode is enabled. In sampling mode, malloc allocations smaller than the sampling size are accounted for probabilistically. The larger the call-stack allocation size, the more frequently it occurs and the greater its chance of being sampled. |
| restrace\_tag | string | Type of the GPU memory to be captured. | 

This parameter can be added repeatedly. Currently, this parameter can only be set to **RES\_GPU\_VK**, **RES\_GPU\_GLES\_BUFFER**, **RES\_GPU\_GLES\_IMAGE**, **RES\_GPU\_CL\_BUFFER**, or **RES\_GPU\_CL\_IMAGE**, which are used to specify the GPU memory allocation stack of Vulkan, OpenGL ES, OpenCL, image, and buffer types.

Note: This parameter is supported since API version 21.

 |

**Result analysis**

The fp stack unwinding and cross-language stack unwinding are enabled (green frames denote JavaScript).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/0oBu_8TiSs2Us1iWX1F_-w/en-us_image_0000002537925064.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84F210A45DE83767293DBCF48D0077D69A4DD66B8B731541370DCCF4DFB21D48)

The dwarf stack unwinding and cross-language stack unwinding are enabled (native ->JS -> native stack frames are displayed).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/LeBh9xInSoeUMfPjfuzeww/en-us_image_0000002568684841.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFE09B6048941CF99E3AB8427C18D472153B0FED1DC52389C136C928BC70B026)

Statistics mode is enabled (the stack data is displayed periodically).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/09LWJwL0TqaUUH3kGAMDKw/en-us_image_0000002568764851.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19059F480925FBA31487CA754588B18245E226C758AA3E8436DBF88FBF88A15A)

Non-statistics mode is enabled (the stack data is not displayed periodically).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/gWEsVDCxTHW_YutM_x4N5w/en-us_image_0000002537765126.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6191CAC0F6E1E960A3B4CB9849E8BDB2AA43581B4BA06B794D1E9F49ED117967)

## ftrace-plugin

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| ftrace\_events | string | Captured trace events. | Trace events that record kernel logging. |
| hitrace\_categories | string | Captured HiTrace logging information. | The HiTrace capability is called to obtain data and write the data to a file in proto format. |
| hitrace\_apps | string | Captured HiTrace information process. | When this parameter is set, only the trace information of the corresponding process is recorded. When this parameter is added, binder cannot be added to **hitrace\_categories**. Otherwise, trace data parsing will be abnormal. |
| buffer\_size\_kb | int | Buffer size, in KB. | Cache size required for the **hiprofiler\_plugins** process to read kernel events. The default value **204800** is recommended. |
| flush\_interval\_ms | int | Data collection interval, in ms. | The default value **1000** is recommended. |
| flush\_threshold\_kb | int | Size of the data to refresh. | Data is refreshed to the file once when the threshold is exceeded. It is recommended that you use the default value of SmartPerf. |
| parse\_ksyms | bool | Whether to obtain kernel data. | The value **true** means to obtain kernel data, and **false** means the opposite. |
| trace\_period\_ms | int | Period for reading kernel data. | It is recommended that you use the default value of SmartPerf. |

**Result analysis**

Example:

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 10 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "ftrace-plugin"
  sample\_interval: 1000
  config\_data {
  ftrace\_events: "binder/binder\_transaction"
  ftrace\_events: "binder/binder\_transaction\_received"
  buffer\_size\_kb: 204800
  flush\_interval\_ms: 1000
  flush\_threshold\_kb: 4096
  parse\_ksyms: true
  clock: "boot"
  trace\_period\_ms: 200
  debug\_on: false
  }
}
CONFIG

This command reads the kernel **binder\_transaction** and **binder\_transaction\_received** data. The two fields must be used together to completely display the data at both ends of the binder. After running the command, run the **hdc file recv /data/local/tmp/hiprofiler\_data.htrace** command to export the file to the current directory, and then use SmartPerf to open and parse the file. The following figure shows an example result.

You can click the arrow on the right of **binder transaction** to go to the process or thread on the other end of the binder.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/naNBi4qyQKqu-urNxTTWmg/en-us_image_0000002537925066.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8ED522B193207A262F001883DD25095C51F050722F380BA6309FCFB39D14215)

## memory-plugin

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| report\_sysmem\_vmem\_info | bool | Whether to read virtual memory data. | Data is read from the **/proc/vmstat** node. |
| report\_process\_mem\_info | bool | Whether to obtain the detailed memory data of a process, such as **rss\_shmem**, **rss\_file**, and **vm\_swap**. | Data is read from the **/proc/${pid}/stat** node. |
| report\_smaps\_mem\_info | bool | Whether to obtain the smaps memory information of a process. | Data is read from the **/proc/${pid}/smaps** node. |
| report\_gpu\_mem\_info | bool | Whether to obtain the GPU usage of a process. | Data is read from the **/proc/gpu\_memory** node. |
| parse\_smaps\_rollup | bool | Whether to read smaps statistics from the **smaps\_rollup** node. | Data is read from the **/proc/{pid}/smaps\_rollup** node. The profiling effect (for CPU and memory usage) is better than that of using the **report\_smaps\_mem\_info** parameter. |

The following memory information is displayed:

-   **MemTotal**: total memory size.
-   **MemFree**: free memory size.
-   **Buffers**: buffer size of files.
-   **Cached**: cache size.
-   **Shmem**: size of allocated shared memory.
-   **Slab**: kernel data cache size.
-   **SUnreclaim**: size of unreclaimable slab.
-   **SwapTotal**: total size of the swap space.
-   **SwapFree**: size of the unused swap space.
-   **Mapped**: size of the mapping for devices and files.
-   **VmallocUsed**: size of the used virtual memory.
-   **PageTables**: size of the index table that manages memory paging.
-   **KernelStack**: memory consumed by the kernel.
-   **Active**: size of the buffer or cache page file that is frequently used.
-   **Inactive**: size of the buffer or cache page file that is not frequently used.
-   **Unevictable**: size of the memory page that cannot be released.
-   **VmallocTotal**: total size of the vmalloc virtual memory.
-   **CmaTotal**: total size of the contiguous available memory.
-   **CmaFree**: size of the free available memory.
-   **Zram**: size of the used zRAM.
-   **ZramTotal**: total size of zRAM.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/IOs_X_MOQSifmJ-cdGhMLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=879FD4DE6949D4CB230E7EAFCAA696846881FF07934A37CEB53CB8CDB1AE4322)

The difference between **Active** and **Inactive** is that **Active** contains data that has been used recently while **Inactive** does not. When the physical memory is insufficient and the memory space in use needs to be released, the **Inactive** memory is released first.

**Result analysis**

Run the **hiprofiler\_cmd** command to obtain the memory data.

Example:

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "memory-plugin"
  sample\_interval: 5000
  config\_data {
  report\_process\_tree: true
  report\_sysmem\_mem\_info: true
  sys\_meminfo\_counters: PMEM\_MEM\_TOTAL
  sys\_meminfo\_counters: PMEM\_MEM\_FREE
  sys\_meminfo\_counters: PMEM\_BUFFERS
  sys\_meminfo\_counters: PMEM\_CACHED
  sys\_meminfo\_counters: PMEM\_SHMEM
  sys\_meminfo\_counters: PMEM\_SLAB
  sys\_meminfo\_counters: PMEM\_SWAP\_TOTAL
  sys\_meminfo\_counters: PMEM\_SWAP\_FREE
  sys\_meminfo\_counters: PMEM\_MAPPED
  sys\_meminfo\_counters: PMEM\_VMALLOC\_USED
  sys\_meminfo\_counters: PMEM\_PAGE\_TABLES
  sys\_meminfo\_counters: PMEM\_KERNEL\_STACK
  sys\_meminfo\_counters: PMEM\_ACTIVE
  sys\_meminfo\_counters: PMEM\_INACTIVE
  sys\_meminfo\_counters: PMEM\_UNEVICTABLE
  sys\_meminfo\_counters: PMEM\_VMALLOC\_TOTAL
  sys\_meminfo\_counters: PMEM\_SLAB\_UNRECLAIMABLE
  sys\_meminfo\_counters: PMEM\_CMA\_TOTAL
  sys\_meminfo\_counters: PMEM\_CMA\_FREE
  sys\_meminfo\_counters: PMEM\_KERNEL\_RECLAIMABLE
  sys\_meminfo\_counters: PMEM\_ACTIVE\_PURG
  sys\_meminfo\_counters: PMEM\_INACTIVE\_PURG
  sys\_meminfo\_counters: PMEM\_PINED\_PURG
  report\_sysmem\_vmem\_info: true
  report\_process\_mem\_info: true
  report\_app\_mem\_info: false
  report\_app\_mem\_by\_memory\_service: false
  report\_purgeable\_ashmem\_info: true
  report\_dma\_mem\_info: true
  report\_gpu\_mem\_info: true
  }
}
CONFIG

This command reads the basic memory statistics of the system. After the command is executed, run the **hdc file recv /data/local/tmp/hiprofiler\_data.htrace** command to export the file to the current directory, and then open and parse the file on SmartPerf. The following figure shows an example result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/mUAM7ni6RTSdYCtxV3EBnQ/en-us_image_0000002568684843.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60191C870F42B6CFADDDAFF9A8F27AA17B61CB937539EFD239F7AD813E2C01A0)

Use DevEco Studio to obtain the memory data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/npPrcQJgREW5GpmD5h3YKA/en-us_image_0000002568764853.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58908DEEC719A1B0CD1F0ED191F94BAE0A443EF5DE626253CC51B79DA3D08EBD)

You can go to **DevEco Studio** -> **Profiler** -> **Allocation** and select **Memory** to use the **memory plugin** feature of the profiler. The preceding figure shows the process smaps memory information in the selected time range.

## xpower-plugin

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| bundle\_name | string | Name of the process for which power consumption profiling is required. | The value must be the same as the process name in the **/proc/** node. |
| message\_type | XpowerMessageType | Type of the power consumption data to be obtained. | The data types include **REAL\_BATTERY**, **APP\_STATISTIC**, **APP\_DETAIL**, **COMPONENT\_TOP**, **ABNORMAL\_EVENTS**, and **THERMAL\_REPORT**. |

**Result analysis**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/8h4xP2wDRAizU7lF-_ayEQ/en-us_image_0000002537765128.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2564441A7620BC6EC8D58A4E293827D69958D9FA0F5D41E9D645F7B1B5C49665)

You can go to **DevEco Studio** -> **Profiler** -> **Realtime Monitor** to obtain the power consumption data of related processes.

## gpu-plugin

Obtain the GPU usage information.

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| pid | int | Process ID to profile, which is the same as the process ID in the **/proc/** node. | \- |
| report\_gpu\_info | bool | Whether to display the GPU usage of a specified process. | **true**: display the GPU data of a specified process (PID needs to be set). **false**: do not display the GPU data of a specified process. |

## cpu-plugin

Obtain the CPU usage information.

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| pid | int | Process ID to profile. | The value must be the same as the process ID in the **/proc/** node. |
| report\_process\_info | bool | Whether to display the CPU usage of a specified process. | 
**true**: display the CPU usage of a specified process (PID needs to be set).

**false**: display only the system CPU usage.

 |
| skip\_thread\_cpu\_info | bool | Whether to skip the thread CPU usage data. | 

**true**: do not display the CPU usage of each thread, which reduces the profiling overhead.

**false**: display the CPU usage of each thread.

 |

The following lists the basic CPU information:

-   **Start Time**: start time of the collection.
-   **Duration**: interval between the previous collection and the current collection.
-   **TotalLoad%**: total CPU usage.
-   **UserLoad%**: CPU usage in user mode.
-   **SystemLoad%**: CPU usage in kernel mode.
-   **Process**: process ID.

**Result analysis**

Example:

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "cpu-plugin"
  sample\_interval: 1000
  config\_data {
  report\_process\_info: true
  }
}
CONFIG

This command reads the basic CPU statistics. After the command is executed, run the **hdc file recv /data/local/tmp/hiprofiler\_data.htrace** command to export the file to the current directory, and then open and parse the file on SmartPerf. The following figure shows an example result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/J3yxKiXzTzW1rlxGoVx9gw/en-us_image_0000002537925068.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB54C41ACF5A229893A055533C4CB16A19A92C00D29C1D96F3DCFEF6F024F6E4)

## diskio-plugin

Obtain the disk I/O usage information of the entire device.

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| report\_io\_stats | IoReportType | Disk I/O statistics. | The value is an enum type. Currently, only **IO\_REPORT** is supported. |

When **IO\_REPORT** is set, the following disk I/O information is obtained:

-   **Data Read**: total number of bytes read from the disk to the memory.
-   **Data Read/sec**: number of bytes read from the disk to the memory per second.
-   **Data Write**: total number of bytes written from the memory to the disk.
-   **Data Write/sec**: number of bytes written from the memory to the disk per second.
-   **Reads In**: number of bytes read.
-   **Reads In/sec**: number of bytes read per second.
-   **Write Out**: number of bytes written.
-   **Write Out/sec**: number of bytes written per second.

**Result analysis**

Example:

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "diskio-plugin"
  sample\_interval: 1000
  config\_data {
  report\_io\_stats: IO\_REPORT
  }
}
CONFIG

This command reads the basic disk I/O statistics. After the command is executed, run the **hdc file recv /data/local/tmp/hiprofiler\_data.htrace** command to export the file to the current directory, and then open and parse the file on SmartPerf. The following figure shows an example result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/rZYyvMppQHmMy1-gXII4qA/en-us_image_0000002568684845.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8577E7CBC6EAB8BA9A9C63499F38CDD6436E331270E71103F050B45C2327787)

## hidump-plugin

Obtain the frame rate of an application process.

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| report\_fps | bool | Whether to report the frame rate data. | 
**true**: report the frame rate data of the application process.

**false**: do not report the frame rate data.

 |
| sections | uint32 | Number of times that the frame rate data is reported per second. | The default value is **10**, that is, the frame rate data is reported every 100 ms. |

**Result analysis**

Currently, this plugin only supports trace data parsing on DevEco Studio. SmartPerf is not supported. For details, see the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ENPmA8x6Q2-n9gtoftIUaA/en-us_image_0000002568764855.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6429BE83A4C471F98C0EBCB7E4D0B256B6D3CC29F1DD3D925BC7846D1DAFDF8)

## hisysevent-plugin

Obtain the system event data.

**Parameters**

| Name | Type | Description | Details |
| :-- | :-- | :-- | :-- |
| msg | string | Custom string. | Reserved field. An empty string can be passed. |
| subscribe\_domain | string | Domain to subscribe to. | Used to subscribe to all events in a specific domain. If this field is left empty, all events in all domains are subscribed to. |
| subscribe\_event | string | Event to subscribe to. | Used to subscribe to a specific event. If this field is left empty, all events are subscribed to. |

**Result analysis**

Example:

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "hisysevent-plugin"
  config\_data {
  msg: "hisysevent-plugin"
  subscribe\_domain: ""
  subscribe\_event: ""
  }
}
CONFIG

This command captures information about all hisystem event subscriptions. After the command is executed, run the **hdc file recv /data/local/tmp/hiprofiler\_data.htrace** command to export the file to the current directory, and then open and parse the file on SmartPerf. The following figure shows an example result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/W43SQpCQSR-u3MbbPGGKuA/en-us_image_0000002537765130.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D791884DE135C5132AB8D09CB0034D869FAAB89F7C959AFB2D1231D2933F2A38)

## network-plugin

Obtains the network upload and download data, and collects statistics on network traffic and connection status provided by the network management module.

**Parameters**

| Name | Type | Description | Mandatory | Details |
| :-- | :-- | :-- | :-- | :-- |
| pid | int32 | Process ID. | No | Used to obtain the network data of a specified process. Multiple parameters can be passed in. If this parameter is not specified, the network data of the entire device is captured. |
| startup\_process\_name | string | Name of the process to start. | No | This parameter must be specified for capturing network data of a specified process. |
| restart\_process\_name | string | Name of the process to restart. | No | This parameter must be specified for capturing network data of a specified process after the process restarts. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/NxJlt_GnTmqpkIpM6QxQEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE34A0280ED5FEBAAE21746823EF4112F4B98772B62DE499F72D7645E9BF6AB0)

**startup\_process\_name** and **restart\_process\_name** cannot be both empty.

The following lists the network information:

-   **StartTime**: start time of the collection.
-   **Duration**: interval between the previous collection and the current collection.
-   **Data Received**: total number of received network bytes.
-   **Data Received/sec**: number of received network bytes per second.
-   **Data Send**: total number of sent network bytes.
-   **Data Send/sec**: number of sent network bytes per second.
-   **Packets In**: total number of received network packets.
-   **Packets In/sec**: number of received network packets per second.
-   **Packets Out**: total number of sent network packets.
-   **Packets Out/sec**: number of sent network packets per second.

**Result analysis**

Example:

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "network-plugin"
  sample\_interval: 1000
  config\_data {
  }
}
CONFIG

This command captures network data of the entire device. After the command is executed, run the **hdc file recv /data/local/tmp/hiprofiler\_data.htrace** command to export the file to the current template, and then open and parse the file on SmartPerf. The following figure shows an example result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/xlbvWJSvTLShTbWKbsSZpA/en-us_image_0000002537925070.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66F5251E5F901E8522A5155CBA3E1AB39DCBD7A8C368818B4B5070AD7BFBDC65)

## network profiler

Obtains the network request information of a process, and records each HTTP request as a data point.

**Parameters**

| Name | Type | Description | Mandatory | Details |
| :-- | :-- | :-- | :-- | :-- |
| pid | int32 | Process ID. | No | Used to obtain the network data of a specified process. Multiple parameters can be passed in. If this parameter is not specified, the network data of the entire device is captured. |
| startup\_process\_name | string | Name of the process to start. | No | This parameter must be specified for capturing network data of a specified process. |
| restart\_process\_name | string | Name of the process to restart. | No | This parameter must be specified for capturing network data of a specified process after the process restarts. |
| clock\_id | int | Clock type. | Yes | 
**1**: BOOTTIME, which indicates the monotonically increasing time (including NTP adjustment) after the system starts.

**2**: REALTIME, which indicates the adjustable system real time.

**3**: REALTIME\_COARSE, which indicates the low-precision real time.

**4**: MONOTONIC, which indicates the monotonically increasing time without NTP adjustment.

**5**: MONOTONIC\_COARSE, which indicates the low-precision monotonically increasing time.

**6**: MONOTONIC\_RAW, which indicates the hardware raw monotonically increasing time.

 |
| smb\_pages | int | Number of shared memory pages. | Yes | Size of the shared memory established between the hiprofiler\_plugins process and the profiled process. The recommended value is 16384 pages, that is, 16384 × 4096 = 67108864 bytes (64 MB). |
| flush\_interval | int | Disk flush interval. | No | 

A disk flush is triggered every **flush\_interval** network requests, optimizing the I/O efficiency.

The default value is **1**.

 |
| block | bool | Whether to enable the block mode. | No | 

**true**: Enable the block mode when the shared memory is full, which may affect the performance.

**false**: Discard the excess data when the shared memory is full.

The default value is **false**.

 |

**Result analysis**

Currently, SmartPerf does not support trace data parsing of this plugin. To analyze network data, use the NetWork feature of DevEco Studio Profiler. The reference is as follows:

[Network Diagnosis: Network](../../../../../performance-optimization/network-diagnosis-network/document.md)

#### Common Commands

## Sampling Records of Heap Memory Allocation Call Stack Data

Capture the stack of heap memory allocation operations of the **com.example.insight\_test\_stage** process, and enable fp stack unwinding, offline symbolization, and statistics mode.

$ hiprofiler\_cmd \\
  -c - \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "nativehook"
  sample\_interval: 5000
  config\_data {
  save\_file: false
  smb\_pages: 16384
  max\_stack\_depth: 20
  process\_name: "com.example.insight\_test\_stage"
  string\_compressed: true
  fp\_unwind: true
  blocked: true
  callframe\_compress: true
  record\_accurately: true
  offline\_symbolization: true
  startup\_mode: false
  statistics\_interval: 10
  sample\_interval: 256
  js\_stack\_report: 1
  max\_js\_stack\_depth: 10
  }
}
CONFIG

The collected data is saved to the **/data/local/tmp/hiprofiler\_data.htrace** file, which contains the function call information, thread and dynamic library memory allocation information, call stack count and allocation size required for memory leak analysis. Enabling offline symbolization, fp stack unwinding, and statistics mode can improve the data processing efficiency of the profiling service.

Collect CPU data of the process whose process ID is **1234**. The collection duration is 30s, the sampling period is 1000 ms, the size of the shared memory for transmitting profiling data is 16384 memory pages, and the collected data is saved to the **/data/local/tmp/hiprofiler\_data.htrace** file.

$ hiprofiler\_cmd \\
  -c - \\
  -o /data/local/tmp/hiprofiler\_data.htrace \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
 request\_id: 1
 session\_config {
  buffers {
   pages: 16384
  }
 }
 plugin\_configs {
  plugin\_name: "cpu-plugin"
  sample\_interval: 1000
  config\_data {
   pid: 1234
   report\_process\_info: true
  }
 }
CONFIG

Capture the GPU memory call stack of a specified process. (The latest smartperf release version is required for parsing files. Download link: [smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/releases).)

$ hiprofiler\_cmd \\
  -c - \\
  -t 30 \\
  -s \\
  -k \\
<<CONFIG
request\_id: 1
session\_config {
  buffers {
  pages: 16384
  }
}
plugin\_configs {
  plugin\_name: "nativehook"
  sample\_interval: 5000
  config\_data {
  save\_file: false
  smb\_pages: 16384
  max\_stack\_depth: 20
  pid: 11237
  string\_compressed: true
  fp\_unwind: true
  blocked: true
  callframe\_compress: true
  record\_accurately: true
  offline\_symbolization: true
  startup\_mode: false
  statistics\_interval: 10
  malloc\_disable: true
  memtrace\_enable: true
  restrace\_tag: "RES\_GPU\_VK"
  restrace\_tag: "RES\_GPU\_GLES\_BUFFER"
  restrace\_tag: "RES\_GPU\_GLES\_IMAGE"
  restrace\_tag: "RES\_GPU\_CL\_BUFFER"
  js\_stack\_report: 1
  max\_js\_stack\_depth: 10
  }
}
CONFIG

The **malloc\_disable** parameter is used in the command to filter the native heap stack data. If the **restrace\_tag** parameter does not contain **RES\_GPU\_CL\_IMAGE**, the GPU memory allocation stack of the OpenCL image type is not captured.

#### FAQs

## What should I do if an exception occurs during profiling?

**Symptom**

"Service not started" is displayed when the **hiprofiler\_cmd** command is executed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/julH_TxZTDupAYuZEO5oaw/en-us_image_0000002568684847.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D41895A9FF20DDDDB3843B32E8143C2FA431BE043F141C0824A01080838D0A3)

**Possible Causes and Solution**

If the profiling service is not started, DevEco Studio is being used for profiling or the previous profiling exits frequently. In this case, run the **hiprofiler\_cmd -k** command and then run the profiling command again.

## What should I do if the captured trace file is empty?

**Symptom**

The captured trace file is empty.

**Possible Causes and Solution**

Check whether the generated file is in the **/data/local/tmp/** directory. If the target path is a folder in **/data/local/tmp**, run the **chmod 777** command on the folder. If the application captured by the nativehook or network profiler plugin in the user version is not a [debug-type application](#applications-signed-by-the-debug-certificate), no data can be captured.

## What should I do if the profiling data may be inaccurate?

**Symptom**

The native heap captured by hiprofiler is different from that viewed by hidumper.

**Possible Causes and Solution**

hidumper captures the process-level memory usage, while hiprofiler captures the heap memory data allocated by the user-mode process using basic library functions such as **malloc**, **mmap**, and **realloc**. The **operator new** function also calls **malloc**. Therefore, the native heap information capture by them differs in the thread memory cache, heap memory release delay, and memory used by the loader.

## What should I do if the target process freezes during profiling?

**Symptom**

When the **hiprofiler\_cmd** command is executed, and the fp or dwarf stack unwinding is used, the application process freezes.

**Possible Causes and Solution**

You can change the **config** parameter in the **hiprofiler\_cmd** command as follows:

-   Decrease the values of **max\_stack\_depth** and **max\_js\_stack\_depth** to reduce the stack unwinding depth and the collection of call stack information.
-   Increase the value of **smb\_pages** to increase the shared memory size for profiling data transmission. The default value is 16384 pages, that is, 16384 × 4096 = 67108864 bytes (64 MB). You can change the value to 128 MB.
-   Increase the value of **sample\_interval** to increase the size of the sampling thread stack. The default value is 256. You can change the value to 512.
