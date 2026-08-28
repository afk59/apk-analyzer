# Performance Profiling Procedure

#### Procedure Overview

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/x71t4h6PSV6C9NcbybWscw/en-us_image_0000002532670163.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC36B2EEA8384D931086A5EB08883F6B74E56E4583F8BC686F782FBD541979DD)

Your app may have performance problems if its running status cannot meet expectations. Performance profiling is an iterative process. During app development, you need to observe the app running behavior to identify performance bottlenecks, demarcate and locate performance problems based on runtime data, locate root causes, rectify code, re-run DevEco Profiler, and verify improvements. You need to keep refining until the expected performance is achieved. This procedure also applies to DevEco Profiler. When using DevEco Profiler, follow the procedure below:

1.  Use Realtime Monitor to monitor the device resource usage, identify potential performance bottlenecks and hotspot areas, for example, high CPU usage or unexpected memory usage increase.
2.  Create an in-depth task to analyze and locate the root causes of the performance problems based on detailed app running data, such as function calls and memory objects.
3.  Optimize the code based on the analysis result.
4.  Use Realtime Monitor again to check whether the usage of each resource meets the expectation, thereby verifying the effectiveness of code modification.
