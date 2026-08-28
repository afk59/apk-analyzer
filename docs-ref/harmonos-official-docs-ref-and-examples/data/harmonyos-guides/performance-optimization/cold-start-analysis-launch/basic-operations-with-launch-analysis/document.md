# Basic Operations with Launch Analysis

Startup speed is an important indicator during app/atomic service development. To identify bottlenecks in app startup time and speed up cold start, you can use the launch analysis provided by DevEco Profiler to capture and analyze key data during the startup and identify the cause of slow startup. The launch analysis task integrates the functionalities of the time, CPU, Frame, and network analysis tasks, so you can compare the usage of other resources in the selected period when analyzing the launch duration.

This topic describes only the Launch lane. For details about the integrated time, CPU, Frame, and network analysis tasks, see the corresponding topics.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/NYUtF5LkR_OLFD3qCa-ZNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52C0335BBD656BD0F027BE99A07A452B1C965C35A09698E6C6FDC278100C516E)

-   Launch analysis cannot be performed for release apps that cannot be started by commands.
-   Recording for the launch analysis can be performed when the device screen is locked.

#### Switching Between Launch Modes

The launch mode can be either ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/BLJqnSzTSju5UAeq8JVlLg/en-us_image_0000002532749931.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E151449F8A2401A478B48084F0A41AF6A12A5DC6221C7F91A45BFC8753E0F91 "Click to enlarge") automatic or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/RiHIL-XaSKCpQNH6A5sQZg/en-us_image_0000002500910060.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4D6C6D43BFCD7716ACC9D7DC3B890307B470E854A4D8D2149EAE21D3CA0E4E6 "Click to enlarge") manual. You can toggle between these modes by simply clicking the corresponding icon.

-   In automatic launch mode, when you use the Launch template and start recording, the selected app will be restarted automatically.
-   In manual launch mode, starting the recording will only terminate the selected app. You will then need to manually start the app when prompted.

#### Checking the Duration of Each Startup Phase

1.  Create a launch analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md). Alternatively, click **Open File** in the session area and import historical data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/TCKz-QHASvuqw4XSshT0yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74EC9EA8DDC82C14173986888BB3652133781717B602B243F9F0D732E8122AFC)
    
    -   In the task analysis window, you can hold **Ctrl** and scroll the mouse wheel to zoom in to or out of the timeline, and hold **Shift** and scroll the mouse wheel to move the timeline leftwards or rightwards. Alternatively, you can press **W** or **S** to zoom in to or zoom out of the timeline, and press **A** or **D** to move the timeline leftwards or rightwards.
    -   You can hover the pointer over any position in the lane and press **M** to add a single-point marker.
    -   You can rectangle select a time period and press **Shift+M** to add a time period marker.
    -   In the task analysis window, you can press **Ctrl+,** to select a single-point marker forward, and press **Ctrl+.** to select a single-point marker backward.
    -   In the task analysis window, you can press **Ctrl+\[** to select a time period marker forward, and press **Ctrl+\]** to select a time period marker backward.
    -   Offline symbol parsing is available in launch analysis tasks. For details, see [Offline Symbol Parsing](../../basic-time-analysis-time/document.md#section186881175012).
    -   Animation profiling is available in launch analysis tasks. For details, see [Enhancing Animation Performance](../../janky-frames-analysis/frame-analysis/document.md#section258014238619).
    
    Before starting capture in the launch analysis task, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/aD2d1bG4QNCE3bU33MSf_g/en-us_image_0000002532749927.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A3EF4DCF1A940A3878A10531580CE592A40E26C9AB227E02C44F5E3FE9F4AE9 "Click to enlarge") to specify the lane to capture. The Launch lane displays the duration distribution of each phase in the launch process.
    
2.  Click a phase or select multiple phases on the Launch lane. On the **Details** tab, you can view the duration statistics of the selected phases.
    
    Expand the statistics of each phase to view its duration information. Click the redirection button to switch to the trace task of the related thread.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/p5AkiANWRsmtlLBBmxKj-g/en-us_image_0000002500910052.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9ACB76E869F42CFBBE917A1BA664850E9D282F6EDF0C01ED38081C20F784F05 "Click to enlarge")
    
3.  Switch to the **Load ETS Files** tab to view the loading status of ETS files during cold start. This feature is available since DevEco Studio 6.0.0 Beta1. The fields are described as follows:
    
    -   **Category**: whether the ETS file is used during app launch.
    -   **Weight**: total time taken to load the child node files (excluding the ETS file itself) of the ETS file.
    -   **Self**: time taken to load the ETS file.
    -   **Import Count**: number of times that the ETS file is imported by other files.
    -   **File Name**: name of the ETS file.
    -   **Path**: path of the build product of the ETS file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/dobnZ9LpS36X4Tkc7zxGrA/en-us_image_0000002532749929.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38B2FE120B5390B54125DA6701D29A399ADF72C8D7E8601D45E193E22F894306 "Click to enlarge")
    
4.  Click the **TOP Redundant** tab to view the information about the top 100 redundant ETS files loaded during the cold start. If a file name in the **File Name** column is displayed in blue, double-clicking it quickly navigates to the corresponding project source file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/RuNwyhoTRZCxj70zZcj7ww/en-us_image_0000002532669977.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD2C5F51EB574D77DC3CD044A07175ABD699CFFC8B12840A2A08A8F793443A67 "Click to enlarge")
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/mTLGlRdSQ-qCzSYN8VCSlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51182659804B050443C15E20B635DF8B8FB1CF6AA49880123B670B8BBE5ADA8B)

For apps that have been released on AppGallery, you cannot view the ETS file loading information during cold start on the **Load ETS Files** or **TOP Redundant** tab.

#### Checking the Time Used to Load a Static Resource Library

1.  Expand the Launch lane. The Static Initialization sub-lane displays the duration required for loading each static resource library during the startup.
2.  Click a static resource library or select multiple static resource libraries. The duration statistics of the selected objects are displayed on the details panel.
    
    For a task that fails to complete loading within the expected time, you can click the redirection button to switch to the thread trace task for in-depth analysis.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/lzOllwHkRtC2uANN_Q-LdA/en-us_image_0000002501069902.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=438899F26B2DC6347FB426D7498EA7BF3E9B56D3B8AA3C0EA5E28567E7891E83 "Click to enlarge")
    

#### Checking the Main Thread Running Status on a CPU Core

1.  Expand the Launch lane. The Running CPU Cores sub-lane displays the CPU core on which the main thread runs during the startup.
2.  Click a process or select multiple processes. The running statistics of the selected objects are displayed on the details panel.
    
    Click the redirection button of a CPU core to go to the CPU Core lane to view detailed scheduling information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ZUGvLyunSaG1jF_Gr8IbNQ/en-us_image_0000002532749933.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B13570AAD90A61BE27FDFFF025C2231E4771ED295AC393F231635E2C5567A119 "Click to enlarge")
    

#### Checking the Thread Trace Data During the Startup

1.  Expand the Launch lane. In addition to Static Initialization and Running CPU Cores, there are key thread status and trace data during the startup.
2.  Click a slice or select multiple slices to view the details.
    
    -   The **Details** tab page displays the selected objects in a tree, including the task name, start time, and duration.
    -   The **Thread States** tab page displays thread status statistics.
    -   The **Thread Usage** tab page displays the thread usage.
    -   The **Slice List** tab page displays the slice statistics of the selected objects.
    -   The **Load Statistics** tab page displays the medium and heavy load information of the selected objects.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/BbzJxM3NTkqawu4Tb-tBTQ/en-us_image_0000002500910056.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DD2D8E88B6D6FD29031CED7876334163800A3CB6EC9227F11F92294A3E57322 "Click to enlarge")
