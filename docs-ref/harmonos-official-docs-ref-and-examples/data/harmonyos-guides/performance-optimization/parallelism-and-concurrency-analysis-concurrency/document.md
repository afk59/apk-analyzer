# Parallelism and Concurrency Analysis: Concurrency

TaskPool (for details, see [@ohos.taskpool (Starting the Task Pool)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-taskpool)) provides a multithreaded environment that helps reduce resource consumption and improve system performance. It eliminates the need for manually managing the lifecycle of thread instances. You can use the **TaskPool** APIs to create background tasks and perform operations on them, for example, executing or canceling a task.

With the Concurrency analysis feature provided by DevEco Profiler, you can record key data for parallelism and concurrency, and analyze performance issues such as the lifecycle, throughput, and latency of tasks. With this template, you can inspect information related to ArkTS asynchronous interfaces, Node-API asynchronous interfaces, TaskPool, and the FFRT concurrency model, as well as the ArkTS callstack, callstack, and process information, allowing you to associate the lifecycle of tasks with specific call stack information.

#### Viewing Task Statistics

1.  Select a specific lane, and use the **options** drop-down list box to filter different processes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/V-ckKaGUTEm0WkIf2I9f3Q/en-us_image_0000002500910470.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F696584CF15A2BBB2BA80B90456906C6C23DCC1C13F626EE4235EA78D0C45717 "Click to enlarge")
    
2.  Select a time range within the sub-lane, and the **Details** panel will display the statistics of parallel and concurrent tasks in the corresponding execution state for that time range.
3.  Click the redirection button next to a task name to jump to the corresponding task lane.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/6zX9s_-pSxKfwvu33pHISQ/en-us_image_0000002532750333.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E29BB73A96502A9CC8C73778329E47E3477E316D56E47B93AD94B412788FEC37 "Click to enlarge")
    

#### Viewing All States of a Task

1.  Select a specific lane, and use the **options** drop-down list box to filter different processes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/zTIcZL1fTIS24ExH9lUX2Q/en-us_image_0000002532670377.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08E27C4065272F170FAB11F6C42B571C265ABDFAB4B60AAB2D60321402BA163D)
    
2.  Select a time range in the sub-lane to view the task status within the selected time range.
3.  Click the redirection button next to the task name to jump to the corresponding thread lane, where you can view the trace file's markers within the execution time range of the task, reflecting the function execution of the thread during that period.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/7k2PlXYXSqOPaYR56h93PQ/en-us_image_0000002500910462.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E23D9B356612B90C8BE316CB415FB3AC0C76F4D44C01FA049073C581A901295F "Click to enlarge")
    
4.  Expand the Async ArkTS lane to view details of ArkTS asynchronous call tasks individually.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/j2-oX_DkTUebHGyfI3d4oQ/en-us_image_0000002500910468.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73F2BBE6738FFE593595D5DC0EEDD70FA746BD941A1AD042B259EB54F278B52C "Click to enlarge")
    
5.  Expand the Async NAPI lane to view details of Node-API asynchronous call tasks individually.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/lTzOhfrhR9yPuzWQLq_Zhg/en-us_image_0000002500910466.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4601F5653673D1B8991E9E753C514CAC72E392B778785F5028031F18A9DB7FE8 "Click to enlarge")
    

#### Viewing a Specific State of a Task

Click an execution node in the Task sub-lane, and the **Details** panel will display detailed information about the task in that specific state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/c1lPf-dqTeGC2XHdamVI8g/en-us_image_0000002501070306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B54898D376CC5FF90A154A1790D2A2948DEFCB8572093E0C3900DC026D3159EA "Click to enlarge")
