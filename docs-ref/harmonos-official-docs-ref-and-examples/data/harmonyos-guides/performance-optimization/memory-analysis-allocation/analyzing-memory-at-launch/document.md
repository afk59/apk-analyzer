# Analyzing Memory at Launch

The memory usage of apps/atomic services during startup is a concern for profiling. To optimize the memory usage during the startup, you can use the allocation analysis task.

DevEco Profiler's processing varies according to the app running status:

-   If you select an app that is not started yet, DevEco Profiler automatically starts the app to capture data when the task starts. After the capture is complete, the task enters the parsing phase.
-   If a running app is selected, when the analysis task starts, DevEco Profiler stops the app and then starts it again to capture data. After the capture is complete, the task enters the parsing phase.

To start an allocation analysis task, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/SUF1PPKQTjqH5YmuLs-FmQ/en-us_image_0000002532669965.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C224BC9DB92D56F30EE513F5455669DA9C6E0FDB780A21CD91C50EA21E59FF50 "Click to enlarge") next to the task in the task list.

After the analysis is complete, the data types displayed and processing methods used are consistent, regardless of the app's initial state (running or not). For details, see [Overview](../overview/document.md) and [Filtering Memory Analysis Data](../filtering-memory-analysis-data/document.md).
