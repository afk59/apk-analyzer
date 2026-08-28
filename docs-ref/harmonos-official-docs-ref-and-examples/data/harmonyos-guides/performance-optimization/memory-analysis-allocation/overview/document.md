# Overview

During app development, memory problems may occur due to incorrect API usage, delayed variable release, and frequent memory allocation and release. DevEco Profiler provides Allocation for basic memory analysis. With Allocation, you can analyze the memory allocation and usage of your app/atomic service at runtime, identify and locate issues such as memory leak, jitter, and overflow, and optimize the memory usage.

Since DevEco Studio 6.0.2 Beta1, Allocation analysis tasks support recording of the Graphic Memory lane.

After device connection is complete, perform the following steps to carry out memory analysis:

1.  Build the app with symbol information. In the [module-level build-profile.json5 file](../../../building-an-app/configuration-files/module-level-build-profile-json5-file/document.md), add the **strip** field and set it to **false**. (This setting ensures that the symbol table and debugging information in the .so file of the module are preserved. Without the symbol table and debugging information, function names may be missing in the captured data.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/XhXzY3bhQQ-NPg_H47epOA/en-us_image_0000002532750041.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7264370DC6F2BF4B284177CA2407D7AF01F9FDF312AA77EF81B0E586AA32A555 "Click to enlarge")
    
2.  Create an Allocation analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md). Alternatively, click **Open File** in the session area and import historical data.
    
    Allocation analysis tasks support recording of the **Memory lane**, **ArkTS Allocation lane**, **Native Allocation lane**, and **Graphic Memory lane**. Before recording, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/eY2n3uPzTq-EyR6xNRzkWw/en-us_image_0000002501070024.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E9099BEE3816F96A8F835E91E6B193E7D4BCD525FB1AB49DC24D8FB649C481E "Click to enlarge") to select the desired lanes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Rbe5WSbiRdeS9IQE_BG9aw/en-us_image_0000002532750045.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3AF37BB15CF3A450E0D09A0FEE805ADE588E5B29F981E6D7A7F2D67196B814C "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Wo-MGxCvTsKgseqmXVSsdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B6BC93519C0684010F720D17375E5C1E0073049C2ABC9A8BC3E2F816EC39EA7)
    
    -   In the task analysis window, you can hold **Ctrl** and scroll the mouse wheel to zoom in to or out of the timeline, and hold **Shift** and scroll the mouse wheel to move the timeline leftwards or rightwards. Alternatively, you can press **W** or **S** to zoom in to or zoom out of the timeline, and press **A** or **D** to move the timeline leftwards or rightwards.
    -   You can hover the pointer over any position in the lane and press **M** to add a single-point marker.
    -   You can rectangle select a time period and press **Shift+M** to add a time period marker.
    -   In the task analysis window, you can press **Ctrl+,** to select a single-point marker forward, and press **Ctrl+.** to select a single-point marker backward.
    -   In the task analysis window, you can press **Ctrl+\[** to select a time period marker forward, and press **Ctrl+\]** to select a time period marker backward.
    -   Allocation analysis supports offline symbol parsing. For details, see [Offline Symbol Parsing](../../basic-time-analysis-time/document.md#section186881175012).
    -   During capture, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/q-ZCN5wHT1eYbiVLhj4Onw/en-us_image_0000002500910180.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9ECCCA8A3A691FC058B9228B631CDD4F509F564B9F9050995B0396856D375387 "Click to enlarge") in the upper left corner of the analysis task window to start memory reclamation.
    -   If a memory space occupied by a process of an ARK VM object is no longer accessed by the object in subsequent operations, the space is automatically returned to the system, reducing possible program errors and unnecessary memory loss.
    
    -   **Memory**: displays the physical memory usage of the current process. The following memory types are provided:
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/I4D0lGZxScibNUlwxppYbA/en-us_image_0000002532750061.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA796B03527268DA248EEF272709B5C318346B7616A308EABE6DE4A1C7168261) PSS: sum of the memory exclusively occupied by a process and the proportionally allocated memory occupied by shared libraries.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/PbcOg70QQCSeyB8XaCd6PQ/en-us_image_0000002501070026.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A94FDE18A09F191121A81164057F04933F07519E4A3DB9F5C3139DC4A5088323) RSS: sum of the memory exclusively occupied by a process and the memory occupied by related shared libraries.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/r-SErhWrQfOP-Y6_SVN7Nw/en-us_image_0000002532750059.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF197344B1D82754B8F23EF09B74A83A0929C483FE009E9CBB1BF69BF3D45446) USS: memory exclusively occupied by a process.
        
        By default, only PSS statistics are displayed. To view USS or RSS statistics, select the related data type in the upper right corner of the Memory lane.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/W1cEOgJSQ5-VCd87PHTOEg/en-us_image_0000002501070014.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE0212D00BB6971E69932E30348DDF77E101FC4FA289DF1893DEE5B34D73FE22)
        
        Expand the Memory lane. The sub-lane displays the memory information of each dimension based on the memory type. The dimensions include ArkTS Heap, Native Heap, GL, Graph, Guard, AnonPage Other, FilePage Other, Dev, Stack, .hap, .so, and .ttf. By default, five sub-lanes are displayed. To display other sub-lanes, click **options** in the main lane and select them.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/go-pBYR1QQmiv4KqPpJZuw/en-us_image_0000002501070028.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A3C869A840512B30688F9806ACD159BCCA55722FFE52F921F6FBD57A17C8394 "Click to enlarge")
        
        -   **ArkTS Heap**: memory usage of the ArkTS heap.
        -   **Native Heap**: heap memory used by the native layer (mainly C/C++ code of the .so libraries on which the app depends) allocated with **new/malloc**.
        -   **GL**: texture memory used by the app; **RS**: texture memory plus graphics rendering memory.
        -   **Graph**: DMA memory usage of the process, including DMA buffers directly allocated through APIs and those allocated through **allocator\_host**, counted according to deduplication rules.
        -   **Guard**: memory occupied by the protection section.
        -   **AnonPage Other**: memory occupied by other anonymous pages (not starting with **heap**, **anon:native\_heap**, or **anon:ArkTS heap**).
        -   **FilePage Other**: memory occupied by pages that are not mapped to the .so, .db, or .ttf files.
        -   **Dev**: memory occupied by the files that are named with the **/dev** prefix and loaded by processes.
        -   **Stack**: stack memory.
        -   **.hap**: memory occupied by .hap files loaded by processes.
        -   **.so**: memory occupied by the **.so** dynamic library files loaded by processes.
        -   **.ttf**: memory occupied by the **.ttf** font files loaded by processes.
    -   **ArkTS Allocation**: displays memory allocation information of ARK VMs. The lane is not displayed by default. To record the lane data, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/aq4Tbq_QRAakIJntco-ozQ/en-us_image_0000002501070032.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06D4138EE2EB4F38F43EC1F3AE5D517975AD473EEA83FEACD9FD58DBC7B7EC52 "Click to enlarge") in the upper left corner and select **ArkTS Allocation**. Due to privacy and security policies, this lane is not available for apps that have been released on AppGallery. This lane will be taken offline. You are advised to use the snapshot template to analyze ArkTS memory leaks.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/IqaOaD9ATnamGaZQTmJs1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9EFC983D4E0799137AC482CED083D5E231DABC030C6973D8855554694B11BC8)
        
        Due to the potential significant performance overhead that could cause lag or freezing issues, simultaneous recording of both the ArkTS Allocation and Native Allocation lanes, or the ArkTS Allocation and Graphic Memory lanes, is currently not supported.
        
    -   **Native Allocation**: displays native memory allocation information, including static statistics, allocated stacks, and native memory consumed by function stacks at each layer. Due to privacy and security policies, this lane is not available for apps that have been released on AppGallery.
        
        Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/VWExGRhCSPqNTgYzpDM2dw/en-us_image_0000002532670091.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA6911EA821FA89168AD9DAD5270DEC85EDFEBF8DAB683F2E524692706D89750 "Click to enlarge") in the toolbar to configure various settings related to memory allocation tracking.
        
        -   **Statistics Mode**: specifies whether to collect data in statistics mode, which is enabled by default. When enabled, data is aggregated from the device and returned at intervals specified in **Sampling Interval**. When disabled (non-statistics mode), data is returned from the device in real time after each memory allocation.
        -   **Sampling Interval**: specifies the interval at which data is collected. It only needs to be configured in statistics mode, with a configurable range of 1s to 3600s and a default value of 10s.
        -   **Native Allocation Filter Size**: specifies the minimum trace memory. The value ranges from 0 to 65535 bytes, and the default value is 1024 bytes.
        -   **Backtrace Mode**: specifies the backtrace mode of the memory allocation stack. Currently, two backtrace modes are available: FP (default) and DWARF. FP backtracking links stack frames via the frame pointer (FP register) to directly traverse the call chain. DWARF backtracking performs stack backtracking based on DWARF debugging information generated by the compiler. FP backtracking offers better performance but may fail in certain specific scenarios (for example, control over the compilation parameters of .so files). In such cases, DWARF backtracking can be tried as an alternative.
        -   **Record JS Stack**: specifies whether to enable JavaScript backtracking. When this feature is enabled, the system will automatically backtrack from the native layer to the JavaScript layer, completing stack stitching from native to JavaScript. This is suitable for scenarios where ArkTS/JavaScript code calls native code.
        -   **JS Backtrace Depth**: specifies the JavaScript backtrace depth. The value ranges from 1 to 128. The default value is **10**.
        -   **Native Backtrace Depth**: specifies the native backtrace depth. The value ranges from 5 to 100. The default value is **10**.
        -   **Backtrace Stack**: specifies the backtrace depth. This parameter is available only when **Backtrace Mode** is set to **DWARF**. Its value indicates the backtrace depth of both JavaScript and native. The value ranges from 5 to 100. The default value is **20**.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/6t0tQ6V6TmOW2euJwtCERQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9725F834611A383E1252B46E8EB54A9C72F0994508182B3DECCC341315C61A0)
            
            -   A smaller minimum trace memory and a larger backtrace depth may even cause frame freezing in DevEco Profiler. Therefore, set them based on your project requirements.
            -   Statistics mode is designed for scenarios where individual memory allocations are not of primary interest, and its focus is on monitoring the app's memory usage changes over an extended period. It merges and aggregates data within a specified sampling interval to reduce the amount of data processed, thereby increasing recording efficiency and duration. The value set for **Sampling Interval** is an approximate value, meaning that statistics will be aggregated as close as possible to this interval, with some deviation. The deviation does not exceed 1 second, and this deviation does not affect the accuracy of memory allocation.
            -   In the statistics mode, the recording end time must be an integer multiple of the sampling interval. For example, if the sampling interval is 10s, you are advised to stop recording at 11s+, 21s+, and so on. This leaves a margin for the system to process and transmit data.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/AglkSx5FRRqsnuvz7aLF8g/en-us_image_0000002521391564.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F388C0255062EB79E13531555045DE8CD4309F8943A7D0E66A3FCDEBA496F41B "Click to enlarge")
            
    -   The Graphic Memory lane displays memory allocation information related to graphics rendering. Due to privacy and security policies, this lane is not available for apps that have been released on AppGallery.
        
        Expanding the main lane reveals three sub-lanes: Vulkan, OpenGL ES, and OpenCL. The Vulkan sub-lane displays memory allocation data of the GPU\_VK type; the OpenGL ES sub-lane displays memory allocation data of the GPU\_GLES type; the OpenCL sub-lane displays memory allocation data of the GPU\_CL type.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/8bGKoUOuRCGEN5LCsr275g/en-us_image_0000002500910176.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A75D3A74385A6F34FDA2C96C698B5D68E840E0C22E426E6DDC452F437FB01CBD "Click to enlarge")
        
    
3.  Hold down the left mouse button on a lane and drag the mouse to rectangle select a time period. The **Details** panel displays the memory analysis statistics of the specified type within the period.
    
    -   For the Memory lane:
        -   The **Details** panel of the main lane displays the sum of the PSS of the app memory at each sampling point and the sum of the memory usage of each memory paging state in the selected period.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/OL9f_6EATdWioS09i20NZw/en-us_image_0000002500910188.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B17FB8606BF8B3AEB056A93B47E5396488FAE0F4373316776CEE72EFB295F725 "Click to enlarge")
            
        -   The **Details** panel of a sub-lane displays the sum of the PSS of the lane-specific memory at each sampling point and the actual usage of each memory paging state in the selected period.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/0i_kzjiWQMyjyulXAEOK5A/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82799EAFFBA3C8E063323C7974BB5D89449768A37F214001AA4289B4099DC9A5)
            
            The **Graph** field represents the memory size used by the process under the **/proc/process\_dmabuf\_info** node.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/-sO1ixBbR0eu6JrvFhGA7w/en-us_image_0000002500910172.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0999AE2B2A8509FC508D5D00C17CB3E561A86859198F0BF2C3C7A3B445A23811 "Click to enlarge")
            
    -   For the ArkTS Allocation lane, the total ArkTS memory used by the selected process is displayed. After you rectangle select the lane, the object allocation information of all ARK instances captured in the period is displayed. After you rectangle select a sub-lane, the memory usage of the running object in the period is displayed, including the level, memory size of the object, and memory size associated with the object. This lane will be taken offline. You are advised to use the snapshot template to analyze ArkTS memory leaks.
        
        Objects marked with ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/4r1irl6QR-2Uq7mKvkhYeg/en-us_image_0000002500910178.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3C19B2C5C89A86EEA99C9159861F683B2475690D6A7FD1FCA0756CC6F6D1FD5 "Click to enlarge") on the details panel can be accessed through windows. The released memory in each period is marked in gray, and the unreleased memory is marked in green.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/3wFiNw7aTXORRn4dWBK0TQ/en-us_image_0000002532670113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32C8FFF964340997C9B165755154A73F09DFB615B6DFEDFD769D887B63DB15DC "Click to enlarge")
        
    -   For the Native Allocation or Graphic Memory lane, after a sub-lane is rectangle selected, the specific memory allocation information is displayed, including static statistics and allocation stacks.
        
        -   The **Statistics** tab page displays the static allocation information in the period, including the allocation mode (Malloc or Mmap), total allocated memory size, total allocation times, size of the memory that is not released, number of times that the memory is not released, size of the memory that is released, and number of times that the memory is released.
            
            You can click the redirection button on an object to go to the detailed usage/allocation information about the object. Currently, redirection is not supported in the statistics mode.
            
        -   The **Call Trees** tab page displays the memory allocation stack information of the thread, including the function address or symbol, allocated size, proportion, and function stack frame type. Click a stack frame. The **More** area displays the call stack that has the largest memory related to the stack frame.
        -   The **Allocations List** tab page displays detailed information about memory allocation, including the start address of the memory block, timestamp, status, size, invoked library, functions of the invoked library, and event type (corresponding to the allocation mode on the **Statistics** tab page).
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/6SVnPXT8S3WW3jrIh_YB8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96C99D41ED18C228D898A583A72F6C4BAA8FC4FA70AF30C2EC2F41FBEC8570EB)
            
            **Allocations List** is not available in statistics mode.
            
            Select any object, and all libraries related to that object and its callers are displayed on the right.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/CjS4gpExQWm3SdQJFJi04w/en-us_image_0000002532750055.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=580ABB24675C1E41CBEBB3FE6041557F89A677D124B7BC5CF882E053B73FC94E "Click to enlarge")
            
        
    
4.  (Optional) Based on the analysis result, double-click the call stack that may have issues to navigate to the related code. You can then modify the code as needed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/SmW2PDy-TaypvZN3AYoQYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9E8231FC9CE49B9A749A53272A9D6DCB661E1AAE544DA576AFE6C6F10A6C537)
    
    Currently, DevEco Profiler does not support redirection to the native code on the user side for a release app.
