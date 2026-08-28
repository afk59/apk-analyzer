# Basic Time Analysis: Time

#### Function Execution Time Analysis and Optimization

During app/atomic service development, if performance problems such as janky frames and slow loading occur, check the execution time of functions. Time analysis tasks provided by DevEco Profiler can display call stacks based on the CPU usage of processes in hotspot areas and supports redirection to the code line.

After device connection is complete, perform the following steps to carry out time analysis:

1.  Build the app with symbol information. In the [module-level build-profile.json5 file](../../building-an-app/configuration-files/module-level-build-profile-json5-file/document.md), add the **strip** field and set it to **false**. (This setting ensures that the symbol table and debugging information in the .so file of the module are preserved. Without the symbol table and debugging information, function names may be missing in the captured data, and the ArkTS Callstack lane may fail to be associated with the native call stack.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/TGbut4CaQGWbN6cOhYULnA/en-us_image_0000002532750549.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86F1494EE4ED83744FAAAB7270D8475D7C998D5D270FFBED2DF2BCC1A49A7631 "Click to enlarge")
    
2.  Create a time analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md). Alternatively, click **Open File** in the session area and import historical data.
    
    Before starting capture in the time analysis task, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/sa3-gytjSgi_tD-97KxYBw/en-us_image_0000002501070532.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=592166C71B7FBA81A33B8E285336E0EBDC75EF61ABB17F38D4A3074060D033F8 "Click to enlarge") to specify the lane to capture.
    
    -   **User Trace**: custom trace lane, which displays the running status of trace tasks that you have customized using the **hiTraceMeter** interface in the current period based on the timeline.
    -   **ArkTS Callstack**: lane for ARK Runtime function calls, which displays the CPU usage, VM execution status, current call stack name, and call type based on the timeline. Due to privacy and security policies, this lane is not available for apps that have been released on AppGallery.
        
        In terms of programming language, call stacks are classified into ArkTS, Node-API, and native. In terms of ownership, call stacks are classified into developer code and system code. DevEco Profiler provides the following call stack types:
        
        -   ArkTS: The app is running the ArkTS code.
        -   Node-API: The app is running the Node-API code.
        -   Native: The app is running the native code.
            
            For each type, the bright color indicates that the code belongs to the developer, and the gray color indicates that the code belongs to the system.
            
    -   **Callstack**: lane for ArkTS and native hybrid calls, which displays the CPU usage of each thread and the hybrid call stack in the current period based on the timeline. The native call stacks are further classified into developer native code and system ArkTS or native code. Due to privacy and security policies, this lane is not available for apps that have been released on AppGallery.
        
        The Callstack lane collects data based on the sampling mode. The default sampling interval is 500 microseconds. For functions with an execution time of less than 500 microseconds, the timing data in the Details area may exhibit measurement inaccuracies. To obtain more reliable data, trigger the function multiple times during profiling. If it consistently accounts for a significant portion of the total execution time (high time percentage), it can be identified as a hot spot function.
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/O8-hrmx0RMW72Lq84hh7Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5511AACBC8F5DA8C808E645B8D1D70FB592AD8D5AFBDEA857243A03480E1174D)
    
    -   In the task analysis window, you can hold **Ctrl** and scroll the mouse wheel to zoom in to or out of the timeline, and hold **Shift** and scroll the mouse wheel to move the timeline leftwards or rightwards. Alternatively, you can press **W** or **S** to zoom in to or zoom out of the timeline, and press **A** or **D** to move the timeline leftwards or rightwards.
    -   You can hover the pointer over any position in the lane and press **M** to add a single-point marker.
    -   You can rectangle select a time period and press **Shift+M** to add a time period marker.
    -   In the task analysis window, you can press **Ctrl+,** to select a single-point marker forward, and press **Ctrl+.** to select a single-point marker backward.
    -   In the task analysis window, you can press **Ctrl+\[** to select a time period marker forward, and press **Ctrl+\]** to select a time period marker backward.
    -   You can hover the mouse pointer over any position in the ArkTS Callstack or Callstack lane to view the CPU usage at the corresponding time point.
    -   You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/hWQYEvmOSEW4CSgkTKiHrA/en-us_image_0000002501070524.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5365CFAD92F48DED997478AD3DC9AFC82D3E202CE22B51B1343C5CB1A6AC6657 "Click to enlarge") next to a lane name to pin it on top.
    -   Time analysis includes the Energy lane. For details, see [Energy Consumption Diagnosis: Energy Analysis](../energy-consumption-diagnosis-energy-analysis/document.md).
    
3.  On the ArkTS Callstack lane and ArkTS Callstack sub-lane, hold down the left mouse button and drag the mouse to rectangle select a time period.
    
    The **Details** panel displays the execution time distribution of the function stack in the selected period. The **Heaviest Stack** area displays the complete call stack with the largest duration of the selected node on the **Details** panel.
    
    The execution time distribution of the function stack can be displayed in either of the following modes:
    
    -   Call tree mode (default): This mode provides a hierarchical view of function calls with detailed metrics. **Weight** indicates the total execution time of the function, including its subfunctions. **Self** indicates the execution time of the function itself (excluding time spent in subfunctions). **Average Duration** indicates the average execution time of the function itself per call. **Category** indicates the type of the function call.
    -   Flame chart mode: This mode visualizes the call stack as a flame chart. You can enable this mode by turning on the **Flame Chart** switch in the lower part of the page. The horizontal axis represents the function execution duration, and the vertical axis represents the call stack depth.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/tq4-EbO_QOuY7VpBqoZGeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42620F431F83B605328D8D3BE0577175ADF3AAA5D056FE00000B8F392DEC7074)
        
        -   The bar blocks of the flame chart support search. Bar blocks that do not match the search criteria are dimmed.
        -   You can hold **Ctrl** and scroll the mouse wheel, or click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/PxGEpBybSMStS__w8coKrQ/en-us_image_0000002532750561.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6E90CA66A8FB2C3B4B649CE08678809B74FF638456E85A4631AC7D52D5EED59) or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/nKviN4KgSbaX8zu_Ls_Lkw/en-us_image_0000002500910684.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD365F5F1C45E6198C3775CA9C7870094C6E4CCD7A2726F97929BCAFCDD6BCDB) in the upper right corner of the area to zoom in to or zoom out of the timeline of the flame chart. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/kGFtvqTuTcCaPkGpTq0UEg/en-us_image_0000002501070530.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B0848112CF60136FAF75C765B44F95B6663E078E9D1E51E74EB98A746D4788C) to restore the timeline to the initial scale.
        -   You can hold **Shift** and scroll the mouse wheel to adjust the visible area horizontally. You can scroll the mouse wheel alone to adjust the visible area vertically.
        -   You can select a node and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/7V8ttWeaTu6kXmL_WLEiCw/en-us_image_0000002500910692.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=914E65918C2EEBAD96B714576103F8F47E0F2415BF24A83F3DB78B803139F465 "Click to enlarge") in the upper right corner to add a breadcrumb. Once the breadcrumb is added, the node becomes the root node, with its time consumption percentage set to 100%. The time consumption percentages of its child nodes are recalculated relative to this root node.
        -   You can hold **Alt** and left-click a node in the frame chart to move the node to the left bottom and zoom in to 100%. The subordinate nodes on the node are zoomed in accordingly.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/L9refjn1R8u5QXzMspz0fw/en-us_image_0000002501070538.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=943DC84DAC53D0CB2F42A202E72C79E43CF7DD52B7F3A409E4DF5422C6DD182B "Click to enlarge")
        
    -   Click **Unfold CallStack** on the ArkTS Callstack or Callstack sub-lane to display the function call stack in an ice cone chart on the timeline. The sequence of entries in the call stack strictly corresponds to the chronological order of actual function calls.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/qx64MpLtSZqLV9iEOFfztQ/en-us_image_0000002501070526.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D10E4FE99B394E8F5C21F93D0860B80F41652CD800E5846069BB7A03A0B65EA "Click to enlarge")
        
    
4.  On the Callstack lane, hold down the left mouse button and drag the mouse to rectangle select a time period.
    
    -   The **Summary** list displays the maximum, minimum, and average CPU usage of all native threads in the selected period.
    -   The **Callstack** list displays the function hotspots of all native threads in the selected period.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/qJySQNWVSHqFCaZ1Amrh_g/en-us_image_0000002532670607.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=740BE1132B8F484B8F4D250C3557D7DB312281621B4EAB05617E86A85FC308C3 "Click to enlarge")
    
    -   Hover over a node to reveal the option to set it as the root node. Click this option to add a breadcrumb, where the selected node is the root node, with the time consumption ratio set to 100%, and the time consumption ratios of its child nodes are recalculated relative to this new root node.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/bmIkqCzkRiGfAbAyRSKrWQ/en-us_image_0000002532750563.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2E648DA57C2BD121E19D32F387A57BF22F1A01E09E209D7D2A9304A9FB7E3EA "Click to enlarge")
    
5.  On the Callstack sub-lane, hold down the left mouse button and drag the mouse to rectangle select a time period.
    
    -   The **Top Down** tab displays the execution time distribution of the function stack in the selected period. The **Heaviest Stack** area displays the complete call stack with the largest duration of the selected node on the **Details** panel.
    -   The **Bottom UP** tab displays the function list. Expanding any function node allows you to view its callers and the execution time of each caller.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/hTaTcz_3TaeVg0KRzncXlw/en-us_image_0000002500910694.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99B7DB22AC7448262DD6DFA24A560DA02BD1033F3CD6726631A72C1D3BCC69C7 "Click to enlarge")
    
6.  (Optional) On the **Details** panel, double-click the target node (for example, a time-consuming node) to switch to the source code. This frees you from locating the code by path.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ZE3RKVxoRemcd7uKETbBcA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0858D13AB39CBFEE566A05F4E694FD074440687897FAAB406A3FFFD5D31B4B7)
    
    -   Currently, DevEco Profiler does not support redirection to the native code on the user side for a release app.
    -   Statically linked system libraries do not support source code redirection. For example, libunwind.a is integrated through static linking, which means that while its symbols may appear in the call stack as if they were defined by the user, navigating to the source code is not available.
    

#### Hotspot Analysis of Multi-Instance Functions

During app development, you may use the Worker thread or TaskPool to process time-consuming operations. Like the main thread, these threads may encounter performance problems and require profiling. The main thread and every Work thread or TaskPool worker thread correspond to an ARK instance. By connecting to these ARK instances, you can enable performance sampling to obtain more comprehensive sampling information.

-   In the main lane, you can view the CPU usage of the selected process. After you rectangle select a time period, the function call stack information of all ARK instances captured in the period is displayed.
-   After you rectangle select a sub-lane, the function call stack information of the ARK instance captured in the period is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/rp2Hii2pRFSpav7Jac4gNg/en-us_image_0000002532670605.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F6B77180B4220C6E8DC6B83256B12E0E4146EA7ED4BEA2C8ABA9FA3B3DB4F32 "Click to enlarge")

#### Offline Symbol Parsing

DevEco Profiler offers offline symbol parsing, which parses the symbol addresses in a .so library into specific function names to make function locating easier.

For the sampled data with the .so library path and offset address, as shown in the figure below, import the so. library that carries symbols for parsing to supplement the missing symbols in the release .so library (including the system .so libraries, user-compiled .so libraries, and third-party libraries).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/yhwEFJ7dR4mEiT5yKgqVtQ/en-us_image_0000002532670593.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=330C61A5E3F0270B255797234DB1CF7A7F920A6267CCAB23A397CF3AACD505BC "Click to enlarge")

You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/JXX-CKKCQ0Kjt3iyez2rug/en-us_image_0000002532670601.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7405AA052B68EAAA0139E51C471A25D0A0947720CD36788DDBAFC81FEB3E23F "Click to enlarge") on the toolbar to import a .so library that contains debugging information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/dfW5YlIST0Kzru7t5hDP5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AFE544E78BB0BDA632FAC8EF1DB7E27872BB597CB27DB56831A5F37E9A8D8BA)

-   When importing the .so library that carries symbols, ensure that the optimization level (such as -O1, -O2, -O3) is the same as that of the .so library of the release version. You can view or configure the optimization level in the **CMakeLists.txt** file.
-   When importing the .so library that carries symbols, ensure that the compilation options are the same as those of the .so library of the release version. This helps prevent inconsistent start addresses of the .so library from affecting parsing correctness.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/uCIs4JQhTXqOmKCB1_4kRQ/en-us_image_0000002501070528.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=575ECB91D3E6160D806C8C01E5DD9E84243B606545D4B73393565D8F32B06B1A "Click to enlarge")

#### User Trace Query

The time analysis task based on sampling analysis is better than asynchronous scheduling in analyzing synchronization performance problems. To analyze issues such as asynchronous scheduling delay, you can customize traces in the ArkTS code. When an app/atomic service triggers traces during time analysis, DevEco Profiler parses the trace data and displays the data in the form of task blocks in the User Trace lane.

You can hold down the left mouse button on a User Trace sub-lane and drag the mouse to rectangle select a time period. The traced information in the selected period is displayed.

You can also click the **options** drop-down menu for the User Trace lane to set whether the data display is based on the task name or thread ID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PADvCagtQlOlJOUkzoU2fQ/en-us_image_0000002532670595.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43485460E67FCC12BD039F443A7D45067A3B6A7A31B697630D5BB368235EB39C)

-   The **Statistics** tab page displays the trace task statistics of the current lane in the selected period, including the task name, number of times that the task is executed, average duration, maximum duration, and minimum duration. Based on the statistics, you can know the execution frequency and duration deviation of the trace tasks.
-   The **User Trace** tab page lists all the tasks in the selected period, including the task ID, name, start time, end time, and duration.

You can click any task block in a User Trace sub-lane. The details about the task block are displayed on the details panel.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/d7JxN0RlSO6XR1eJYMw1Wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=403503C8A8978882112E80E4D682CCC8FC4C079D386036EE50CB39D0A200E6CF)

You can view user trace information in the Frame and Network analysis task.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/BHFJBP9wQw2DjWZ7tNys5g/en-us_image_0000002532670599.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BD89C774929B2916D2E810DAC7D69E2CDE253171447A528894892D72D5827CB "Click to enlarge")
