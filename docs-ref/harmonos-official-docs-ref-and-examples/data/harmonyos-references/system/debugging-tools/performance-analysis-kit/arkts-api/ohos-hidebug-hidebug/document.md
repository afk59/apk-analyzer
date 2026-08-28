# @ohos.hidebug (HiDebug)

HiDebug provides multiple methods for debugging and profiling applications. With these methods, you can obtain memory, CPU, GPU, and GC data, collect process trace and profiler data, and dump VM heap snapshots. Since most APIs of this module are both performance-consuming and time-consuming, and are defined based on the HiDebug module, you are advised to use these APIs only during the application debugging and profiling phases. If the APIs are required in other scenarios, evaluate the impact of the APIs on application performance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/PGb8FMMNRvG5kpL7BxpLTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E916224E1F198E3862A02712FDB5DFFDBE35502F4857FCB5587FAE23075ADBF)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { hidebug } from '@kit.PerformanceAnalysisKit';

#### hidebug.getNativeHeapSize

getNativeHeapSize(): bigint

Obtains the total number of bytes occupied by the total space (**uordblks** + **fordblks**, which are obtained from **mallinfo**) held by a process, which is measured by the memory allocator.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Size of the memory occupied by the total space held by the process, in bytes. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapSize: bigint = hidebug.getNativeHeapSize();

#### hidebug.getNativeHeapAllocatedSize

getNativeHeapAllocatedSize(): bigint

Obtains the total number of bytes occupied by the total allocated space (**uordblks**, which is obtained from **mallinfo**) held by a process, which is measured by the memory allocator.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Size of the memory occupied by the total allocated space held by the process, in bytes. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapAllocatedSize: bigint = hidebug.getNativeHeapAllocatedSize();

#### hidebug.getNativeHeapFreeSize

getNativeHeapFreeSize(): bigint

Obtains the total number of bytes occupied by the total free space (**fordblks**, which is obtained from **mallinfo**) held by a process, which is measured by the memory allocator.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Size of the memory occupied by the total free space held by the process, in bytes. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize();

#### hidebug.getPss

getPss(): bigint

Obtains the size of the physical memory actually used by the application process. This API is implemented by summing up the values of **Pss** and **SwapPss** in the **/proc/{pid}/smaps\_rollup** node.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/8a6eWzogS7u3ZXkawmOJ2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83D911D1376C5491A4B60B89159E8D521B9E1AAFD923B572EA829ADD113485DB)

Reading the **/proc/{pid}/smaps\_rollup** node is time-consuming. Therefore, you are advised not to use this API in the main thread. You can use this API in the asynchronous thread started by calling [@ohos.taskpool](../../../../../application-framework/arkts/arkts-apis/ohos-taskpool-starting-the-task-pool/document.md) or [@ohos.worker](../../../../../application-framework/arkts/arkts-apis/ohos-worker-starting-the-worker/document.md) to avoid frame freezing.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Size of the physical memory actually used by the application process, in KB. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let pss: bigint = hidebug.getPss();

#### hidebug.getVss11+

getVss(): bigint

Obtains the virtual set size used by the application process. This API is implemented by multiplying the value of **size** (number of memory pages) in the **/proc/{pid}/statm** node by the page size (4 KB per page).

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Virtual set size used by the application process, in KB. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let vss: bigint = hidebug.getVss();

#### hidebug.getSharedDirty

getSharedDirty(): bigint

Obtains the size of the shared dirty memory of a process. This API is implemented by reading the value of **Shared\_Dirty** in the **/proc/{pid}/smaps\_rollup** node.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/5Pd4lQv5Rzq65p2exOP0pA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CAAF4AAC38091A873B1707BA8E9FD0D2052A1890F5815086971066CFE7166EB)

Reading the **/proc/{pid}/smaps\_rollup** node is time-consuming. Therefore, you are advised not to use this API in the main thread. You can use this API in the asynchronous thread started by calling [@ohos.taskpool](../../../../../application-framework/arkts/arkts-apis/ohos-taskpool-starting-the-task-pool/document.md) or [@ohos.worker](../../../../../application-framework/arkts/arkts-apis/ohos-worker-starting-the-worker/document.md) to avoid frame freezing.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Size of the shared dirty memory of the process, in KB. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let sharedDirty: bigint = hidebug.getSharedDirty();

#### hidebug.getPrivateDirty9+

getPrivateDirty(): bigint

Obtains the size of the private dirty memory of a process. This API is implemented by reading the value of **Private\_Dirty** in the **/proc/{pid}/smaps\_rollup** node.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/YArCZM8NQVSXRFAdnuGhyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FF31EEB79E3E4E5612F85B578CC1C9943B1BE7476DFCE8447A938AD981F42A2)

Reading the **/proc/{pid}/smaps\_rollup** node is time-consuming. Therefore, you are advised not to use this API in the main thread. You can use this API in the asynchronous thread started by calling [@ohos.taskpool](../../../../../application-framework/arkts/arkts-apis/ohos-taskpool-starting-the-task-pool/document.md) or [@ohos.worker](../../../../../application-framework/arkts/arkts-apis/ohos-worker-starting-the-worker/document.md) to avoid frame freezing.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Size of the private dirty memory of the process, in KB. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let privateDirty: bigint = hidebug.getPrivateDirty();

#### hidebug.getCpuUsage9+

getCpuUsage(): number

Obtains the CPU usage of a process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/IpRpn0KQRVWhlHcgLd3bfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BE18A20AA42AFFB9DD6D7C5F1C80B439571D117584F87311EDC636697DCF84A)

This API involves cross-process communication and takes a long time. To avoid performance problems, you are advised not to call this API in the main thread.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| number | CPU usage of a process. For example, if the CPU usage is **50%**, **0.5** is returned. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let cpuUsage: number = hidebug.getCpuUsage();

#### hidebug.getServiceDump9+

getServiceDump(serviceid: number, fd: number, args: Array<string>): void

Obtains system service information.

**Required permissions**: ohos.permission.DUMP (available only for system applications)

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serviceid | number | Yes | Service ID used to obtain system service information. |
| fd | number | Yes | File descriptor to which data is written by the API. |
| args | Array<string> | Yes | Parameter list of the **Dump** API of the system service. The maximum length of a string is 254. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HiDebug Error Codes](../../error-codes/hidebug-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | the parameter check failed,Possible causes:1.the parameter type error 2.the args parameter is not string array. |
| 11400101 | ServiceId invalid. The system ability does not exist. |

**Example**:

import { fileIo } from '@kit.CoreFileKit';
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileFd = -1;
try {
  // Obtain the context from the component and ensure that the return value of this.getUiContext().getHostContext() is UIAbilityContext.
  let path: string = this.getUIContext().getHostContext()!.filesDir + "/serviceInfo.txt";
  console.info("output path: " + path);
  fileFd = fileIo.openSync(path, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE).fd;
  let serviceId: number = 10;
  let args: Array<string> = new Array("allInfo");
  hidebug.getServiceDump(serviceId, fileFd, args);
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

if (fileFd >= 0) {
  fileIo.closeSync(fileFd);
}

#### hidebug.startJsCpuProfiling9+

startJsCpuProfiling(filename: string): void

Starts the VM profiling method. **startJsCpuProfiling(filename: string)** and **stopJsCpuProfiling()** are called in pairs. **startJsCpuProfiling(filename: string)** always occurs before **stopJsCpuProfiling()**. You are advised not to call either of these methods repeatedly. Otherwise, an exception may occur.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filename | string | Yes | Custom file name of the sampling data. The .json file is generated in the **files** directory of the application based on the specified file name. The maximum length of a string is 128. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | the parameter check failed,Parameter type error. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.startJsCpuProfiling("cpu\_profiling");
  // ...
  hidebug.stopJsCpuProfiling();
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.stopJsCpuProfiling9+

stopJsCpuProfiling(): void

Stops the VM profiling method. **stopJsCpuProfiling()** and **startJsCpuProfiling(filename: string)** are called in pairs. **startJsCpuProfiling()** always occurs before **stopJsCpuProfiling()**. You are advised not to call either of these methods repeatedly. Otherwise, an exception may occur.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.startJsCpuProfiling("cpu\_profiling");
  // ...
  hidebug.stopJsCpuProfiling();
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.dumpJsHeapData9+

dumpJsHeapData(filename: string): void

Dumps VM heap data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/zwR3lLWhSjW0zbabIqU2Nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A0B8063EF796A903FFEC36B3F57523AE7C5B2DEEE7A5D25E08BE7CA3D7549F7)

Exporting the VM heap is time-consuming, and this API is a synchronous API. Therefore, you are advised not to call this API in the release version. Otherwise, the application screen may freeze, affecting user experience.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filename | string | Yes | User-defined name of the VM heap data output file. The .heapsnapshot file is generated in the **files** directory of the application based on the specified file name. The maximum length of a string is 128. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | the parameter check failed, Parameter type error. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.dumpJsHeapData("heapData");
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.startProfiling(deprecated)

startProfiling(filename: string): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/No9DlTm-R2WhPYwxKlSv6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=779CC4BB214B9F9019F8FE53D2407FA12AA098DC9C1E24E59C18D666BAC8ECF0)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hidebug.startJsCpuProfiling](#hidebugstartjscpuprofiling9) instead.

Starts the VM profiling method. **startProfiling(filename: string)** and **stopProfiling()** are called in pairs. **startProfiling(filename: string)** always occurs before **stopProfiling()**. You are advised not to call either of these methods repeatedly. Otherwise, an exception may occur.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filename | string | Yes | Custom file name of the sampling data. The .json file is generated in the **files** directory of the application based on the specified file name. The maximum length of a string is 128. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.startProfiling("cpuprofiler-20220216");
// code block
// ...
// code block
hidebug.stopProfiling();

#### hidebug.stopProfiling(deprecated)

stopProfiling(): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/gFN5LdsgQPmp4hFqM97lwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8112FDDD2A668614B97DB60C6F079489C33D29D867525ADF3F46C3686B0D09D2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hidebug.stopJsCpuProfiling](#hidebugstopjscpuprofiling9) instead.

Stops the VM profiling method. **stopProfiling()** and **startProfiling(filename: string)** are called in pairs. **startProfiling(filename: string)** always occurs before **stopProfiling()**. You are advised not to call either of these methods repeatedly. Otherwise, an exception may occur.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.startProfiling("cpuprofiler-20220216");
// code block
// ...
// code block
hidebug.stopProfiling();

#### hidebug.dumpHeapData(deprecated)

dumpHeapData(filename: string): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/orZB0BiiTr-3JJ7kefO0aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D537B63C4D4F056AA96FBD67F9C15EC7C77A8465D7E76DB69D6E091EA4B198C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hidebug.dumpJsHeapData](#hidebugdumpjsheapdata9) instead.

Dumps the VM heap data and generates the **filename.heapsnapshot** file.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filename | string | Yes | User-defined heap file name. The .heapsnapshot file is generated in the **files** directory of the application based on the specified file name. The maximum length of a string is 128. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.dumpHeapData("heap-20220216");

#### hidebug.getAppVMMemoryInfo12+

getAppVMMemoryInfo(): VMMemoryInfo

Obtains VM memory information.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| [VMMemoryInfo](#vmmemoryinfo12) | VM memory information. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let vmMemory: hidebug.VMMemoryInfo = hidebug.getAppVMMemoryInfo();
console.info(\`totalHeap = ${vmMemory.totalHeap}, heapUsed = ${vmMemory.heapUsed},\` +
  \`allArraySize = ${vmMemory.allArraySize}\` );

#### hidebug.getAppVMObjectUsedSize21+

getAppVMObjectUsedSize(): bigint

Obtains the VM memory size occupied by ArkTS objects.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | VM memory size occupied by ArkTS objects, in KB. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(\`getAppVMObjectUsedSize = ${hidebug.getAppVMObjectUsedSize()}\`);

#### hidebug.getAppThreadCpuUsage12+

getAppThreadCpuUsage(): ThreadCpuUsage\[\]

Obtains the CPU usage of application threads.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/QtoIE5y3TKiAJC-Kyjk6AA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F129AD704ACC879A051AD8BAD2330C577BC3AB1684334448C03E8286EAF032D)

This API involves cross-process communication and takes a long time. To avoid performance problems, you are advised not to call this API in the main thread.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| [ThreadCpuUsage](#threadcpuusage12)\[\] | CPU usage of all threads of the current application process. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let appThreadCpuUsage: hidebug.ThreadCpuUsage\[\] = hidebug.getAppThreadCpuUsage();
for (let i = 0; i < appThreadCpuUsage.length; i++) {
  console.info(\`threadId=${appThreadCpuUsage\[i\].threadId}, cpuUsage=${appThreadCpuUsage\[i\].cpuUsage}\`);
}

#### hidebug.startAppTraceCapture12+

startAppTraceCapture(tags: number\[\], flag: TraceFlag, limitSize: number): string

Starts automatic trace collection in a specified scope. This API is a supplement to the [HiTrace](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hitrace) module. The performance consumption during trace collection increases with the collection scope. Therefore, before using this API, you are advised to run the **hitrace** command to capture trace logs and select the key scope of trace collection to improve the API performance.

**startAppTraceCapture()** and [stopAppTraceCapture()](#hidebugstopapptracecapture12) must be called in pairs. Repeat calling of **startAppTraceCapture()** will cause exceptions. Trace collection consumes a lot of performance resources. Therefore, call **stopAppTraceCapture()** immediately after trace collection is complete.

When an application calls **startAppTraceCapture()** to collect trace data and the size of the data exceeds the value of **limitSize**, the system automatically calls **stopAppTraceCapture()** to stop trace collection. Therefore, if **limitSize** is set improperly, the generated trace data is insufficient for fault analysis. Therefore, you need to evaluate the value of **limitSize** as required.

Evaluation method: limitSize = Expected trace collection duration x Unit trace traffic.

Expected trace collection duration: You can determine the duration based on the fault scenario. The unit is second.

Unit trace traffic: Size of trace data generated by an application per second, in KB/s. The recommended value is 300 KB/s. You are advised to use the actual value of your application.

To obtain the unit trace traffic of an application, you can call **startAppTraceCapture()** with **limitSize** set to the maximum value 500 MB. After **N** seconds, call **stopAppTraceCapture()** to stop the collection and check the size **S** (KB) of the trace data. The unit trace traffic is **S**/**N** (KB/s).

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tags | number\[\] | Yes | Scope for trace collection. For details, see [tags](#hidebugtags12). |
| flag | TraceFlag | Yes | For details, see [TraceFlag](#traceflag12). |
| limitSize | number | Yes | Limit on the trace file size, in bytes. The maximum size of a single file is 500 MB. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Trace file path. (The API returns the actual physical path. If the path needs to be accessed in the application, convert the path by referring to [Mappings Between Application Sandbox Paths and Physical Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#mappings-between-application-sandbox-paths-and-physical-paths).) |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HiDebug Trace Error Codes](../../error-codes/hidebug-trace-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid argument, Possible causes:1.The limit parameter is too small 2.The parameter is not within the enumeration type 3.The parameter type error or parameter order error. |
| 11400102 | Capture trace already enabled. |
| 11400103 | No write permission on the file. |
| 11400104 | Abnormal trace status. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tags: number\[\] = \[hidebug.tags.ABILITY\_MANAGER, hidebug.tags.ARKUI\];
let flag: hidebug.TraceFlag = hidebug.TraceFlag.MAIN\_THREAD;
let limitSize: number = 1024 \* 1024;

try {
  let fileName: string = hidebug.startAppTraceCapture(tags, flag, limitSize);
  // code block
  // ...
  // code block
  hidebug.stopAppTraceCapture();
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.stopAppTraceCapture12+

stopAppTraceCapture(): void

Stops application trace collection. Use [startAppTraceCapture()](#hidebugstartapptracecapture12) to start collection before calling this API. If this API is called before trace collection or it is repeatedly called, an exception will occur.

If **startAppTraceCapture ()** is called without a properly specified **limitSize**, the size of the generated trace may exceed the **limitSize** value, causing the system to automatically call **stopAppTraceCapture()**. In this case, if **stopAppTraceCapture()** is called again, an error code 11400105 will be displayed.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Error codes**

For details about the error codes, see [HiDebug Trace Error Codes](../../error-codes/hidebug-trace-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 11400104 | The status of the trace is abnormal. |
| 11400105 | No capture trace running. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tags: number\[\] = \[hidebug.tags.ABILITY\_MANAGER, hidebug.tags.ARKUI\];
let flag: hidebug.TraceFlag = hidebug.TraceFlag.MAIN\_THREAD;
let limitSize: number = 1024 \* 1024;
try {
  let fileName: string = hidebug.startAppTraceCapture(tags, flag, limitSize);
  // code block
  // ...
  // code block
  hidebug.stopAppTraceCapture();
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.getAppMemoryLimit12+

getAppMemoryLimit(): MemoryLimit

Obtains the memory limit of an application process.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| [MemoryLimit](#memorylimit12) | Memory limit of the application process. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let appMemoryLimit:hidebug.MemoryLimit = hidebug.getAppMemoryLimit();

#### hidebug.getSystemCpuUsage12+

getSystemCpuUsage(): number

Obtains the CPU usage of the system.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Mdi_aYubRROHipn6F9lYYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7283903BAC6558898FB667BB1252F2F2FDFDD59A069EE9BB8FEA9013B79449C8)

This API involves cross-process communication and takes a long time. To avoid performance problems, you are advised not to call this API in the main thread.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| number | CPU usage of the system. For example, if the CPU usage is **50%**, **0.5** is returned. |

**Error codes**

For details about the error codes, see [HiDebug CPU Usage Error Codes](../../error-codes/hidebug-cpuusage-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 11400104 | The status of the system CPU usage is abnormal. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(\`getSystemCpuUsage: ${hidebug.getSystemCpuUsage()}\`)
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.setAppResourceLimit12+

setAppResourceLimit(type: string, value: number, enableDebugLog: boolean): void

Sets the number of FDs, number of threads, JS memory, or native memory limit of the application.

This API is used to construct a memory leak. For details, see [Subscribing to Resource Leak Events (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts) and [Subscribing to Resource Leak Events (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-ndk).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/KXhatxTyTU2uEAPDfTsWeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E2CD5FBC768F1232F359D430D2A971EE09A91D278BD458C9AD080D895E494B2)

This API is valid only when the **Developer options** is enabled.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Types of leak resources:

\- pss\_memory (native memory)

\- js\_heap (JavaScript heap memory)

\- fd (file descriptor)

\- thread (thread)

 |
| value | number | Yes | 

Value range of the maximum values of the leak resource types:

\- pss\_memory: **\[1024, 4 × 1024 × 1024\]** (Unit: KB)

\- js\_heap: **\[85, 95\]** (85% to 95% of the upper size limit of the JS heap memory)

\- fd: **\[10, 10000\]**

\- thread: **\[1, 1000\]**

 |
| enableDebugLog | boolean | Yes | 

Whether to enable external debugging logs. Enable external debugging logs only in the grayscale version (test version released to a small number of users before the official version is released). Collecting debugging logs occupies a large number of CPU and memory resources, which may cause application smoothness problems.

The value **true** means to enable external debugging logs, and false means the opposite.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HiDebug Error Codes](../../error-codes/hidebug-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid argument, Possible causes:1.The limit parameter is too small 2.The parameter is not in the specified type 3.The parameter type error or parameter order error. |
| 11400104 | Set limit failed due to remote exception. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let type: string = 'js\_heap';
let value: number = 85;
let enableDebugLog: boolean = false;
try {
  hidebug.setAppResourceLimit(type, value, enableDebugLog);
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.getAppNativeMemInfo12+

getAppNativeMemInfo(): NativeMemInfo

Obtains the memory information of the application process. This API is implemented by reading data from the **/proc/{pid}/smaps\_rollup and /proc/{pid}/statm** node.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/QmwLDAA9Q4-4D7JEUD6xng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=099B9B5AB3E17DCCFC60345AC405F079DFCC887D3A0B02E8B983DCDC872FA738)

Reading the **/proc/{pid}/smaps\_rollup** node takes a long time. You are advised to use the asynchronous API [hidebug.getAppNativeMemInfoAsync](#hidebuggetappnativememinfoasync20) to avoid frame loss or frame freezing.

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeMemInfo](#nativememinfo12) | Memory information of the application process. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfo();
console.info(\`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, \` +
  \`sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, \` +
  \`sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}\`);

#### hidebug.getAppNativeMemInfoAsync20+

getAppNativeMemInfoAsync(): Promise<NativeMemInfo>

Obtains the memory information of application processes by reading the data of the **/proc/{pid}/smaps\_rollup** and **/proc/{pid}/statm** nodes. This API uses a promise to return the result.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NativeMemInfo](#nativememinfo12)\> | Promise used to return the application process memory information. |

**Example**:

hidebug.getAppNativeMemInfoAsync().then((nativeMemInfo: hidebug.NativeMemInfo)=>{
  console.info(\`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, \` +
    \`sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, \` +
    \`sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}\`);
});

#### hidebug.getAppNativeMemInfoWithCache20+

getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo

Obtains the memory information of the application process. This API uses the cache mechanism and has higher performance than the **getAppNativeMemInfo** API. The cache is valid for 5 minutes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/f8UNldmcQj-___i15ZpqeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CB274BDB700EBEF27B632DED05A442A25F2AD8E82AD9B89AC91646E19C54B16)

Reading **/proc/{pid}/smaps\_rollup** is time-consuming. Therefore, you are advised not to use this API in the main thread. You can use @ohos.taskpool or @ohos.worker to enable asynchronous threads to avoid application freezing.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| forceRefresh | boolean | No | 
Whether to ignore the cache validity and forcibly update the cache value. The default value is **false**.

The value **true** means to directly obtain the current memory data and update the cache value.

The value **false** means to directly return the cache value if the cache is valid and obtain the current memory data and update the cache value if the cache is invalid.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeMemInfo](#nativememinfo12) | Memory information of the application process. |

**Example**:

let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfoWithCache();
console.info(\`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, \` +
  \`sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, \` +
  \`sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}\`);

#### hidebug.getSystemMemInfo12+

getSystemMemInfo(): SystemMemInfo

Obtains system memory information. This API is implemented by reading data from the **/proc/meminfo** node.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| [SystemMemInfo](#systemmeminfo12) | System memory information. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let systemMemInfo: hidebug.SystemMemInfo = hidebug.getSystemMemInfo();

console.info(\`totalMem: ${systemMemInfo.totalMem}, freeMem: ${systemMemInfo.freeMem}, \` +
  \`availableMem: ${systemMemInfo.availableMem}\`);

#### hidebug.getVMRuntimeStats12+

getVMRuntimeStats(): GcStats

Obtains the system [GC](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gc-introduction) statistics.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| [GcStats](#gcstats12) | System GC statistics. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let vMRuntimeStats: hidebug.GcStats = hidebug.getVMRuntimeStats();
console.info(\`gc-count: ${vMRuntimeStats\['ark.gc.gc-count'\]}\`);
console.info(\`gc-time: ${vMRuntimeStats\['ark.gc.gc-time'\]}\`);
console.info(\`gc-bytes-allocated: ${vMRuntimeStats\['ark.gc.gc-bytes-allocated'\]}\`);
console.info(\`gc-bytes-freed: ${vMRuntimeStats\['ark.gc.gc-bytes-freed'\]}\`);
console.info(\`fullgc-longtime-count: ${vMRuntimeStats\['ark.gc.fullgc-longtime-count'\]}\`);

#### hidebug.getVMRuntimeStat12+

getVMRuntimeStat(item: string): number

Obtains the specified system [GC](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gc-introduction) statistics based on parameters.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| item | string | Yes | 
Type of the statistics to obtain. The following statistics can be obtained:

**"ark.gc.gc-count"**: number of GC times of the current thread.

**"ark.gc.gc-time"**: total GC duration triggered by the current thread, in milliseconds.

**"ark.gc.gc-bytes-allocated"**: size of the Ark VM memory allocated to the current thread, in bytes.

**"ark.gc.gc-bytes-freed"**: memory freed by GC of the current thread, in bytes.

**"ark.gc.fullgc-longtime-count"**: number of longtime full GC times triggered by the current thread.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | System GC statistics returned based on the input parameters. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Possible causes:1. Invalid parameter, a string parameter required. 2. Invalid parameter, unknown property. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(\`gc-count: ${hidebug.getVMRuntimeStat('ark.gc.gc-count')}\`);
  console.info(\`gc-time: ${hidebug.getVMRuntimeStat('ark.gc.gc-time')}\`);
  console.info(\`gc-bytes-allocated: ${hidebug.getVMRuntimeStat('ark.gc.gc-bytes-allocated')}\`);
  console.info(\`gc-bytes-freed: ${hidebug.getVMRuntimeStat('ark.gc.gc-bytes-freed')}\`);
  console.info(\`fullgc-longtime-count: ${hidebug.getVMRuntimeStat('ark.gc.fullgc-longtime-count')}\`);
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### MemoryLimit12+

Defines the memory limit of the application process.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rssLimit | bigint | No | No | Limit on the physical memory size of the application process, in KB. Currently, the system does not limit the physical memory size of the process. However, the available physical memory of the process cannot exceed the maximum physical memory of the device. You can call [hidebug.getSystemMemInfo](#hidebuggetsystemmeminfo12) to obtain the physical memory usage of the device. |
| vssLimit | bigint | No | No | Limit on the virtual memory size, in KB. |
| vmHeapLimit | bigint | No | No | Limit on the JS VM heap size of the calling thread, in KB. |
| vmTotalHeapSize | bigint | No | No | Limit on the JS heap memory size of the process, in KB. |

#### VMMemoryInfo12+

Describes the VM memory information.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| totalHeap | bigint | No | No | Total heap size of the current VM, in KB. |
| heapUsed | bigint | No | No | Heap size used by the current VM, in KB. |
| allArraySize | bigint | No | No | Size of all array objects of the current VM, in KB. |

#### ThreadCpuUsage12+

Describes the CPU usage of a thread.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| threadId | number | No | No | Thread ID. |
| cpuUsage | number | No | No | CPU usage of the thread. |

#### hidebug.tags12+

Enumerates the tags used in trace collection. You can use the [HiTrace](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hitrace) commands to capture the trace data of a specified tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/fLCxs8Z5QJSvuBEeRqJskg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FFBA7C67ABDB488C86002B1C9848BB24065CBF8AAC2751F9CFB090056E010A7)

The following tag values are defined by the system and may change with the version upgrade. To avoid compatibility issues after the upgrade, use the tag names instead of the tag values in application development.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Description |
| :-- | :-- | :-- | :-- |
| ABILITY\_MANAGER | number | Yes | Capability management. The corresponding HiTrace command is **tagName:ability**. |
| ARKUI | number | Yes | ArkUI development framework. The corresponding HiTrace command is **tagName:ace**. |
| ARK | number | Yes | JSVM VM. The corresponding HiTrace command is **tagName:ark**. |
| BLUETOOTH | number | Yes | Bluetooth. The corresponding HiTrace command is **tagName:bluetooth**. |
| COMMON\_LIBRARY | number | Yes | Common library subsystem. The corresponding HiTrace command is **tagName:commonlibrary**. |
| DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER | number | Yes | Distributed hardware device management. The corresponding HiTrace command is **tagName:devicemanager**. |
| DISTRIBUTED\_AUDIO | number | Yes | Distributed audio. The corresponding HiTrace command is **tagName:daudio**. |
| DISTRIBUTED\_CAMERA | number | Yes | Distributed camera. The corresponding HiTrace command is **tagName:dcamera**. |
| DISTRIBUTED\_DATA | number | Yes | Distributed data management. The corresponding HiTrace command is **tagName:distributeddatamgr**. |
| DISTRIBUTED\_HARDWARE\_FRAMEWORK | number | Yes | Distributed hardware framework. The corresponding HiTrace command is **tagName:dhfwk**. |
| DISTRIBUTED\_INPUT | number | Yes | Distributed input. The corresponding HiTrace command is **tagName:dinput**. |
| DISTRIBUTED\_SCREEN | number | Yes | Distributed screen. The corresponding HiTrace command is **tagName:dscreen**. |
| DISTRIBUTED\_SCHEDULER | number | Yes | Distributed scheduler. The corresponding HiTrace command is **tagName:dsched**. |
| FFRT | number | Yes | FFRT task. The corresponding HiTrace command is **tagName:ffrt**. |
| FILE\_MANAGEMENT | number | Yes | File management system. The corresponding HiTrace command is **tagName:filemanagement**. |
| GLOBAL\_RESOURCE\_MANAGER | number | Yes | Global resource management. The corresponding HiTrace command is **tagName:gresource**. |
| GRAPHICS | number | Yes | Graphics module. The corresponding HiTrace command is **tagName:graphic**. |
| HDF | number | Yes | HDF subsystem. The corresponding HiTrace command is **tagName:hdf**. |
| MISC | number | Yes | MISC module. The corresponding HiTrace command is **tagName:misc**. |
| MULTIMODAL\_INPUT | number | Yes | Multi-modal input module. The corresponding HiTrace command is **tagName:multimodalinput**. |
| NET | number | Yes | Network. The corresponding HiTrace command is **tagName:net**. |
| NOTIFICATION | number | Yes | Notification module. The corresponding HiTrace command is **tagName:notification**. |
| NWEB | number | Yes | Nweb. The corresponding HiTrace command is **tagName:nweb**. |
| OHOS | number | Yes | OHOS. The corresponding HiTrace command is **tagName:ohos**. |
| POWER\_MANAGER | number | Yes | Power management. The corresponding HiTrace command is **tagName:power**. |
| RPC | number | Yes | RPC. The corresponding HiTrace command is **tagName:rpc**. |
| SAMGR | number | Yes | System capability management. The corresponding HiTrace command is **tagName:samgr**. |
| WINDOW\_MANAGER | number | Yes | Window management. The corresponding HiTrace command is **tagName:window**. |
| AUDIO | number | Yes | Audio module. The corresponding HiTrace command is **tagName:zaudio**. |
| CAMERA | number | Yes | Camera module. The corresponding HiTrace command is **tagName:zcamera**. |
| IMAGE | number | Yes | Image module. The corresponding HiTrace command is **tagName:zimage**. |
| MEDIA | number | Yes | Media module. The corresponding HiTrace command is **tagName:zmedia**. |

#### NativeMemInfo12+

Describes memory information of the application process.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pss | bigint | No | No | Size of the occupied physical memory (including the proportionally allocated memory occupied by the shared library), in KB. The value of this parameter is obtained by summing up the values of **Pss** and **SwapPss** in the **/proc/{pid}/smaps\_rollup** node. |
| vss | bigint | No | No | Size of the occupied virtual memory (including the memory occupied by the shared library), in KB. The value of this parameter is obtained by multiplying the value of **size** in the **/proc/{pid}/statm** node by **4**. |
| rss | bigint | No | No | Size of the occupied physical memory (including the memory occupied by the shared library), in KB. The value of this parameter is obtained by reading the value of **Rss** in the **/proc/{pid}/smaps\_rollup** node. |
| sharedDirty | bigint | No | No | Size of the shared dirty memory, in KB. The value of this parameter is obtained by reading the value of **Shared\_Dirty** in the **/proc/{pid}/smaps\_rollup** node. |
| privateDirty | bigint | No | No | Size of the private dirty memory, in KB. The value of this parameter is obtained by reading the value of **Private\_Dirty** in the **/proc/{pid}/smaps\_rollup** node. |
| sharedClean | bigint | No | No | Size of the shared clean memory, in KB. The value of this parameter is obtained by reading the value of **Shared\_Clean** in the **/proc/{pid}/smaps\_rollup** node. |
| privateClean | bigint | No | No | Size of the private clean memory, in KB. The value of this parameter is obtained by reading the value of **Private\_Clean** in the **/proc/{pid}/smaps\_rollup** node. |

#### SystemMemInfo12+

Describes the system memory information, including the total memory, free memory, and available memory.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| totalMem | bigint | No | No | Total memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemTotal** in the **/proc/meminfo** node. |
| freeMem | bigint | No | No | Free memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemFree** in the **/proc/meminfo** node. |
| availableMem | bigint | No | No | Available memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemAvailable** in the **/proc/meminfo** node. |

#### TraceFlag12+

Describes types of trace collection threads, including the main thread and all threads.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Value | Description |
| :-- | :-- | :-- |
| MAIN\_THREAD | 1 | The main thread of the application. |
| ALL\_THREADS | 2 | All threads of the application. |

#### GcStats12+

type GcStats = Record<string, number>

Describes the key-value pair used to store GC statistics. This type does not support multi-thread operations. If this type is operated by multiple threads at the same time in an application, use a lock for it.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Type | Description |
| :-- | :-- |
| Record<string, number> | 
Key-value pair format used to store GC statistics. It contains the following information:

**"ark.gc.gc-count"**: number of GC times of the current thread.

**"ark.gc.gc-time"**: total GC duration triggered by the current thread, in milliseconds.

**"ark.gc.gc-bytes-allocated"**: size of the Ark VM memory allocated to the current thread, in bytes.

**"ark.gc.gc-bytes-freed"**: memory freed by GC of the current thread, in bytes.

**"ark.gc.fullgc-longtime-count"**: number of longtime full GC times triggered by the current thread.

 |

#### JsRawHeapTrimLevel20+

Enumerates the trimming levels of the heap snapshot.

**TRIM\_LEVEL\_2** takes a longer time than **TRIM\_LEVEL\_1**. The threshold for screen freezing is 6 seconds. With **TRIM\_LEVEL\_1**, the trim duration stays below this threshold. Upon switching to **TRIM\_LEVEL\_2**, the duration may exceed 6s, triggering an **APP\_FREEZE** (screen freeze event) and causing the system to kill the application; the trim level then reverts to **TRIM\_LEVEL\_1**.

You are advised to use **TRIM\_LEVEL\_1** to ensure application stability and use \*\*TRIM\_LEVEL\_2 \*\*only when more complete trimming is required.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Value | Description |
| :-- | :-- | :-- |
| TRIM\_LEVEL\_1 | 0 | Level 1 trimming, mainly used for strings. |
| TRIM\_LEVEL\_2 | 1 | Level 2 trimming, which reduces the size of the object address identifier from 8 bytes to 4 bytes. |

#### hidebug.isDebugState12+

isDebugState(): boolean

Obtains the debugging state of an application process.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the Ark or native layer of the application process is in the debugging state. The value **true** indicates that the layer is in the debugging state, and **false** indicates the opposite. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(\`isDebugState = ${hidebug.isDebugState()}\`)

#### hidebug.getGraphicsMemory14+

getGraphicsMemory(): Promise<number>

Obtains the total GPU memory size (**gl** + **graph**) of the application. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the total GPU memory size of the application, in KB. |

**Error codes**

For details about the error codes, see [HiDebug Error Codes](../../error-codes/hidebug-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 11400104 | Failed to get the application memory due to a remote exception. |

**Example**:

import { hidebug, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemory().then((ret: number) => {
  console.info(\`graphicsMemory: ${ret}\`)
}).catch((error: BusinessError) => {
  console.error(\`error code: ${error.code}, error msg: ${error.message}\`);
})

#### hidebug.getGraphicsMemorySync14+

getGraphicsMemorySync(): number

Obtains the total GPU memory size (GL + graph) of an application in synchronous mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/XOUQM8lVR4OBEW5DPKK_KQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3860AC359E2050F7ED1675D99957FEDB420502061DF578B87B383DB8934DEAF7)

This API involves multiple cross-process communications, which may take seconds. To avoid performance problems, you are advised to use the asynchronous API **getGraphicsMemory** instead of this API in the main thread.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total size of the application's GPU memory, in KB. |

**Error codes**

For details about the error codes, see [HiDebug Error Codes](../../error-codes/hidebug-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 11400104 | Failed to get the application memory due to a remote exception. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(\`graphicsMemory: ${hidebug.getGraphicsMemorySync()}\`)
} catch (error) {
  console.error(\`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}\`);
}

#### hidebug.getGraphicsMemorySummary21+

getGraphicsMemorySummary(interval?: number): Promise<GraphicsMemorySummary>

Obtains the GPU memory data of an application. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interval | number | No | 
Validity period of the cached GPU memory data, in seconds. Default value: **300** The value ranges from 2 to 3600. If the input value is out of the value range, the default value will be used.

If the cached GPU memory data exists for a period longer than the value of this parameter, the latest GPU memory data is obtained and the cache value is updated. Otherwise, the cache value is directly obtained.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GraphicsMemorySummary](#graphicsmemorysummary21)\> | Promise used to return the GPU memory data of the application. |

**Error codes**

For details about the error codes, see [HiDebug Error Codes](../../error-codes/hidebug-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 11400104 | Failed to get the application memory due to a remote exception. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemorySummary().then((ret: hidebug.GraphicsMemorySummary) => {
  console.info(\`get graphicsMemory gl: ${ret.gl} graph: ${ret.graph}.\`)
}).catch((error: BusinessError) => {
  console.error(\`error code: ${error.code}, error msg: ${error.message}.\`);
})

#### hidebug.dumpJsRawHeapData18+

dumpJsRawHeapData(needGC?: boolean): Promise<string>

Dumps the original VM heap snapshot for the current thread and generates a .rawheap file. You can use [rawheap-translator](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/rawheap-translator) to convert the generated file into a .heapsnapshot file for parsing. This API uses a promise to return the generated file path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/vXuH6NDuQpiOAkabs9lkjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11CAE4BDA09048B8AAD04594189F306AE57EA71C2D9A124A18984A1D44DD8744)

This API is resource-consuming. Therefore, the calling frequency and times are strictly limited. You need to delete the files immediately after processing them.

You are advised to use this API only in the grayscale version of an application.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| needGC | boolean | No | Whether GC is required before storing heap snapshots. The value **true** indicates that GC is required, and **false** indicates the opposite. The default value is **true**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Path of the generated snapshot file. ([Application Sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#application-file-directory-and-application-file-path)) |

**Error codes**

For details about the error codes, see [HiDebug Error Codes](../../error-codes/hidebug-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 11400106 | Quota exceeded. |
| 11400107 | Fork operation failed. |
| 11400108 | Failed to wait for the child process to finish. |
| 11400109 | Timeout while waiting for the child process to finish. |
| 11400110 | Disk remaining space too low. |
| 11400111 | Napi interface call exception. |
| 11400112 | Repeated data dump. |
| 11400113 | Failed to create dump file. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
hidebug.dumpJsRawHeapData().then((filePath: string) => {
  console.info(\`dumpJsRawHeapData success and generated file path is ${filePath}\`)
}).catch((error: BusinessError) => {
  console.error(\`error code: ${error.code}, error msg: ${error.message}\`);
})

#### hidebug.enableGwpAsanGrayscale20+

enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void

Enables GWP-ASan to detect illegal behaviors in heap memory usage.

This API is used to dynamically configure and enable GWP-ASan to adapt to the custom GWP-ASan detection policy. The configuration takes effect after the application is restarted.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/mJccszLtQPCjzxdD8lYC8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0777A2BBADD81DD1F173D7B88C77EE2FFE0BA19F815500E727BF9CEFCC1C2E02)

1.  If the number of GWP-ASan applications configured using this API exceeds the quota during device running, this API fails to be called and an error code is thrown. Use **try-catch** to capture exceptions to prevent the application from exiting abnormally.
2.  After the device restarts, the GWP-ASan parameters set by this API are invalid.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GwpAsanOptions](#gwpasanoptions20) | No | GWP-ASan configuration items. If this parameter is not set, the default parameter is used. |
| duration | number | No | GWP-ASan duration, in days. The default value is 7. The value must be a positive integer greater than 0. |

**Error codes**

For details about the error codes, see [HiDebug Error Codes](../../error-codes/hidebug-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 11400114 | The number of GWP-ASAN applications of this device overflowed after last boot. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: hidebug.GwpAsanOptions = {
  alwaysEnabled: true,
  sampleRate: 2500,
  maxSimutaneousAllocations: 5000,
};
let duration: number = 4;

try {
  hidebug.enableGwpAsanGrayscale(options, duration);
  console.info(\`Succeeded in enabling GWP-ASan.\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed to enable GWP-ASan. Code: ${err.code}, message: ${err.message}\`);
}

#### GwpAsanOptions20+

Enumerates the GWP-ASan configuration items. You can configure whether to enable GWP-Asan, the sampling frequency, and the maximum number of allocated slots.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alwaysEnabled | boolean | No | Yes | 
The value **true** means to enable GWP-ASan 100%.

The value **false** means to enable GWP-ASan at a probability of 1/128.

The default value is **false**.

 |
| sampleRate | number | No | Yes | 

Sampling rate of GWP-ASan. The default value is **2500**. The value must be a positive integer greater than 0. If the value is a decimal, it is rounded up.

GWP-Asan performs sampling on the allocated memory at a probability of 1/**sampleRate**.

You are advised to set this parameter to a value greater than or equal to 1000. If the value is too small, the performance is affected.

 |
| maxSimutaneousAllocations | number | No | Yes | 

Maximum number of allocated slots. The default value is **1000**. The value must be a positive integer greater than 0. If the value is a decimal, it is rounded up.

When the slots are used up, the newly allocated memory is no longer monitored.

After the used memory is released, the slots occupied by the memory are automatically reused to facilitate subsequent memory monitoring.

You are advised to set this parameter to a value less than or equal to 20000. If the value is too large, the VMA may break down.

 |

#### hidebug.disableGwpAsanGrayscale20+

disableGwpAsanGrayscale(): void

Disables GWP-ASan. This API is used to cancel the custom configuration and restore the default parameter [GwpAsanOptions](#gwpasanoptions20).

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.disableGwpAsanGrayscale();

#### hidebug.getGwpAsanGrayscaleState20+

getGwpAsanGrayscaleState(): number

Obtains the number of remaining days for enabling GWP-ASan.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of remaining days for enabling GWP-ASan. If GWP-Asan is disabled, **0** is returned. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

let remainDays: number = hidebug.getGwpAsanGrayscaleState();
console.info(\`remainDays: ${remainDays}\`);

#### hidebug.setJsRawHeapTrimLevel20+

setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void

Sets the trimming level of the original heap snapshot stored by the current process. Using **TRIM\_LEVEL\_2** for this API can effectively reduce the size of the heap snapshot file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/WzyHjTUZTfqplcPXRe-XuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9AF49193BAA6189D7A8D1E7EBA17E9091543708015B4B03494B76804CE48910)

The default trimming level is **TRIM\_LEVEL\_1**. If **TRIM\_LEVEL\_2** is set, you need to use [rawheap-translator](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/rawheap-translator) since API version 20 to convert the .rawheap file to the .heapsnapshot file. Otherwise, the conversion may fail.

This API affects the result of [dumpJsRawHeapData](#hidebugdumpjsrawheapdata18).

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| level | [JsRawHeapTrimLevel](#jsrawheaptrimlevel20) | Yes | Trimming level for storing heap snapshots. The default value is **TRIM\_LEVEL\_1**. |

**Example**:

import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.setJsRawHeapTrimLevel(hidebug.JsRawHeapTrimLevel.TRIM\_LEVEL\_2);

#### GraphicsMemorySummary21+

Describes the GPU memory data of an application, including the GL and Graph parts.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| gl | number | No | No | GL memory size (memory occupied by RenderService for loading required resources, such as images and textures), in KB. |
| graph | number | No | No | Graph memory size (DMA memory usage of the process), in KB, including the DMA buffers obtained directly through the API and those obtained through **allocator\_host**. |
