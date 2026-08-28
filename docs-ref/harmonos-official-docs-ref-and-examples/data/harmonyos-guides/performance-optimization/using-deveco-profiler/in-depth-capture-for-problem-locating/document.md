# In-depth Capture for Problem Locating

#### Creating an Analysis Task and Performing Capture

You can select an analysis task specific to the performance problem scenario to perform in-depth analysis on your app/atomic service. Currently, the following scenarios are supported:

-   Frame: used to deeply analyze the causes of janky frames of an app/atomic service.
-   Launch: used to analyze the start time of an app/atomic service, the duration of each phase in the startup period, and the running status of core threads. It helps you identify startup bottlenecks.
-   Snapshot: used to take ArkTS heap memory snapshots for multiple times and analyze the differences between a single memory snapshot or multiple memory snapshots. It can be used to locate ArkTS memory problems.
-   Allocation: used to analyze the memory usage of an app/atomic service, collect memory data in depth, display memory trends of different categories, and provide call stack traces of memory instance allocation. It is suitable for in-depth analysis of memory problems.
-   ArkUI: used to identify frame freezing and frame loss issues caused by page layout, component time consumption, and state variable update.
-   Energy: used to analyze energy consumption exceptions of apps or atomic services.
-   ArkWeb: used to locate web app loading and frame loss issues.
-   Network: used to diagnose HTTP stack network information and analyze the time consumed by network request segments.
-   Concurrency: used to gain real-time visibility into how concurrent and parallel processes are executing and help optimize code.
-   Time: used to analyze the function execution efficiency, capture the function call stack and the time consumed by each frame, and display the cross-language call stack from ArkTS to native code. It is used to analyze typical native API problems.
-   CPU: used to collect CPU core data and display the CPU usage of the app/atomic service, scheduling information of each CPU core time slice, frequency and usage of each CPU core, CPU usage of each process, thread status, and trace information.

1.  Select a scenario template and create a session.
    
    DevEco Profiler provides scenario-specific analysis task types, including Frame, Launch, Snapshot, Allocation, ArkUI, Energy, ArkWeb, Network, Concurrency, Time, and CPU.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/WNy6sIzGRyG5vi1-feHpRQ/en-us_image_0000002500910026.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BAC0438A0881181162BD5984E79A0BC22AAEDBF7EB489D4119FDBFFA5541702): Select a device from the device list.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/iqaoH7_cTIug7TzbRbfytQ/en-us_image_0000002500910012.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74D86168800CC5FF12A93322E72104583930403399CE0A81F79A37DDCD2B74D8): Select the target app from the process list. The app can be either running or not running, but it must be one installed on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/m8-q_Z4KR4GxNBdFufmHkw/en-us_image_0000002501069854.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4FCFEA358F9EB53654B2FD1402AEA99BBA3C6DF8DAED98DA6DD5E0332639F21): In the task creation area, select the desired task type and click **Create Session**. The analysis task is created and displayed in the task list in the left pane.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/6_tD4EUETlunCw4-3sIODA/en-us_image_0000002501069850.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=990AC09A03731C4B1075B8C9D8281B4FB0EFB3FFABF7DEFDD3F6BAE7B82B0584): The profiling details panel is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Z-z7_AeRTdmYDK640IB44Q/en-us_image_0000002500910022.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FF48F5F02735F19C0069994782FDD65FECAF9DF604FE68317E13253986DCE3B "Click to enlarge")
    
2.  Configure and confirm the session environment.
    
    In the capture details panel on the right, there are many small icons on the toolbar. You can move the mouse pointer over the icons to learn about the tips. You can also adjust the capture options by selecting options from the drop-down list box in each lane area.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/aS8KFLBlS-OIuodROAcJOw/en-us_image_0000002532749883.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8674632B33E7D208A8F3A1604BE9570845B1314D7B689B67450A5E44B4852551)
    
3.  Start capture.
    
    To start capture, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/laTLSS6ySqKV-2p8TcLHOg/en-us_image_0000002501069862.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=576D9F40E1A98B0F05F215672C5332C5C4952ADB94A81136513CEEE027C2A62C) in the upper left corner of the task window, or click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/4nMCWbVlQ6m2AgDNH6Dw2Q/en-us_image_0000002532669935.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A15C3C1F197EE3F43ECD48C90245822C0C0E7286B0FEEE590F300D48EB16EEE3) in the session list on the left. After the capture is started, the task status changes from initializing to recording. During capture, you cannot change the template. To use another template, stop the current capture and select that template to start a new round of capture.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/hhvQQ4vuRsSvDOmbcbKYAQ/en-us_image_0000002500910006.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C092FC5C1D3EF1F22A32B1AB881155F82C7BF8BF22506686FB4EB43AFE4A76A "Click to enlarge")
    
4.  Reproduce the performance deterioration scenario, and stop capture.
    
    Operate the app on the device to reproduce the app performance problem. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/TRSL2JizT-CuxUKKDia-sw/en-us_image_0000002532669945.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=111012B92209C7DD3930179CD437883977B8B3C8C28450F6DD9CB1288EA0F26B) next to the task to enter the data parsing phase. When the status of all lane tasks changes from analyzing to rendering, the parsing is complete. The profiling details panel on the right displays the detailed profiling content. The parsing process may involve a large amount of data. Wait until the parsing is complete.
    

The ArkTS Callstack, Callstack, Native Allocation, and ArkTS Allocation lanes display **No Data** if there are no values available. You can hover the cursor over the triangular warning icon next to the lane's name to view the cause of the error.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/33pI4dpgRnGsve99C1Q4Uw/en-us_image_0000002532749879.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A05C5F030FD1CD6E2095C2F194D0E3B1CB79D62B2851F4882246A7B0D934AD2)
