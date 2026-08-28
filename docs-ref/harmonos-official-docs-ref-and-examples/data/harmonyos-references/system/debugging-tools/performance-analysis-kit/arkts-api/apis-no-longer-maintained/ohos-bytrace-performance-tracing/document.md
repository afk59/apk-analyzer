# @ohos.bytrace (Performance Tracing)

The **bytrace** module implements performance tracing for processes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/4saYlMBpRKi283S1sWzEcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CFBE428639C0A826E42396B78EEC0D1E423A8C61267E1650F61C84B95DB26BE)

-   The APIs provided by this module are deprecated since API version 8. You are advised to use the new APIs [@ohos.hiTraceMeter](../../ohos-hitracemeter-performance-tracing/document.md) instead.
-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bytrace } from '@kit.PerformanceAnalysisKit';

#### bytrace.startTrace

startTrace(name: string, taskId: number, expectedTime?: number): void

Marks the start of a timeslice trace task.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/wEXRn9_SRLWICMrqPJUwNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77180B15EA08A2084730D044B650970999D551632CE502A51B1697EC66C288AE)

If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be performed multiple times concurrently, different task IDs must be specified in **startTrace**. If the trace tasks with the same name are not performed at the same time, the same task ID can be used. For details, see the bytrace.finishTrace example.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of a timeslice trace task. |
| taskId | number | Yes | ID of a timeslice trace task. |
| expectedTime | number | No | Expected duration of the trace, in ms. This parameter is optional and is left blank by default. |

**Example**

bytrace.startTrace("myTestFunc", 1);
bytrace.startTrace("myTestFunc", 1, 5); // The expected duration of the trace is 5 ms.

#### bytrace.finishTrace

finishTrace(name: string, taskId: number): void

Marks the end of a timeslice trace task.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/GvCzzt52Q7K6tfnEDV1Nfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=620054B4B344FC2EC028515F71831A52C2794A2B106F94B0BB3A9F0F9238368C)

To stop a trace task, the values of name and task ID in **finishTrace** must be the same as those in **startTrace**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of a timeslice trace task. |
| taskId | number | Yes | ID of a timeslice trace task. |

**Example**

bytrace.finishTrace("myTestFunc", 1);

// Start trace tasks with the same name concurrently.
bytrace.startTrace("myTestFunc", 1);
// Service flow...
bytrace.startTrace("myTestFunc", 2);  // The second trace task starts while the first task is still running. The first and second tasks have the same name but different task IDs.
// Service flow...
bytrace.finishTrace("myTestFunc", 1);
// Service flow...
bytrace.finishTrace("myTestFunc", 2);

// Start trace tasks with the same name in serial mode.
bytrace.startTrace("myTestFunc", 1);
// Service flow...
bytrace.finishTrace("myTestFunc", 1);  // The first trace task ends.
// Service flow...
bytrace.startTrace("myTestFunc", 1);   // The second trace task starts after the first task ends. The two tasks have the same name and task ID.
// Service flow...
bytrace.finishTrace("myTestFunc", 1);

#### bytrace.traceByValue

traceByValue(name: string, count: number): void

Defines a numeric variable that indicates the number of timeslice trace tasks.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the numeric variable. |
| count | number | Yes | Value of the numeric variable. |

**Example**

let traceCount = 3;
bytrace.traceByValue("myTestCount", traceCount);
traceCount = 4;
bytrace.traceByValue("myTestCount", traceCount);
// Service flow...
