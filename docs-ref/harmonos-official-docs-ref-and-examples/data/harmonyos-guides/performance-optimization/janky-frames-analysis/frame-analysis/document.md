# Frame Analysis

During app/atomic service development, if jank occurs, such as unsmooth form sliding, slow page interaction, and choppy animations, you can use frame analysis provided by DevEco Profiler to capture and analyze key data and identify the cause of jank. The frame analysis task integrates the functionalities of time, CPU, and network analysis tasks, so you can compare the resource usage in the selected period when analyzing jank data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/gjESHZoYTQyc4cgzkphG6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F175D585788ACAD2BB5AED8828DAA59ED84A63432193F99B803FEEF8F91B6A89)

-   In the task analysis window, you can hold **Ctrl** and scroll the mouse wheel to zoom in to or out of the timeline, and hold **Shift** and scroll the mouse wheel to move the timeline leftwards or rightwards. Alternatively, you can press **W** or **S** to zoom in to or zoom out of the timeline, and press **A** or **D** to move the timeline leftwards or rightwards.
-   You can hover the pointer over any position in the lane and press **M** to add a single-point marker.
-   You can rectangle select a time period and press **Shift+M** to add a time period marker.
-   In the task analysis window, you can press **Ctrl+,** to select a single-point marker forward, and press **Ctrl+.** to select a single-point marker backward.
-   In the task analysis window, you can press **Ctrl+\[** to select a time period marker forward, and press **Ctrl+\]** to select a time period marker backward.
-   Offline symbol parsing is available in frame analysis tasks. For details, see [Offline Symbol Parsing](../../basic-time-analysis-time/document.md#section186881175012).
-   Frame analysis includes the Energy lane. For details, see [Locating Energy Consumption Issues](../../energy-consumption-diagnosis-energy-analysis/document.md#section889733410010).

#### Checking GPU Usage

1.  Create a Frame analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md). Alternatively, click **Open File** in the session area and import historical data.
2.  Expand the Frame lane, which displays the GPU usage of the current device. The sub-lane displays the frame data on the app and Render Service.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/u6KmrPEeQaqza0Rxdda1aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F096956303DF98FB356971FEDAA20BB7E3DF1CA4A01542E5E40C42DD022D01F7)
    
    -   During frame rendering, the app submits a rendering request to Render Service, which submits the request to the hardware for compositing and rendering. This means that frames on the app are associated with those on Render Service. However, they are not always in a one-to-one association, since frames from multiple apps or multiple frames from the same app may be submitted to the same frame on Render Service.
    -   The expected duration required for frame rendering is related to the frame rate. Generally, the frame rate is 60, and the corresponding Vsync period is 16.6 ms. That is, the frame rendering duration on the app or Render Service must be within 16.6 ms. If the actual end time of frame rendering is later than the expected end time, the frame is considered frozen.
    -   In the RS Frame and App Frame lanes, frames that are rendered normally are displayed in green; janky frames are displayed in red.
    -   For details about the ArkTS Callstack, Callstack, and CPU Core lanes, see [Basic Time Analysis: Time](../../basic-time-analysis-time/document.md) and [CPU Activity Analysis](../../cpu-activity-analysis/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/z91kR2KQTD2HdqU_pwiNPg/en-us_image_0000002500910174.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7525EAC0C4387A1BC75CA78E0D1C7612AB39EA4FA5D55387E5BB820AD21CD3E8 "Click to enlarge")
    

#### Checking Frame Data Statistics of All Processes

1.  Drag the mouse on the timeline to select a time period.
2.  Rectangle select the main lane.
    
    On the **Statistics** tab, frame information in the selected period is displayed by process. The information includes the jank rate, number of jank times, maximum number of consecutive jank times, maximum jank duration, average jank duration, and average normal duration.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/BYuT99zqSzmUBe3_Bp0qmQ/en-us_image_0000002500910170.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F87E9D097010AB1075CD587C19854208E728DB41FA35BBE25908D7A3C44F14F5 "Click to enlarge")
    
3.  Click the redirect button of a process in the **Statistics** list. The frame list corresponding to the process is displayed on the **Frame List** panel. The start time, total duration, GPU duration, and jank type of each frame are displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/dKvbA-CSR2-oYt7Unn8JnQ/en-us_image_0000002501070002.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D847EC491AE2B7579CADF5B721CA06D7C97FF7898ECA75E07B0A866395D7EBBF "Click to enlarge")
    
4.  Click any frame in the **Frame List** list. More key information about the frame is displayed in the **More** area on the right. You can learn about the expected start time and expected duration of the frame. You can also click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/jAkhQCYZS3ivSbZ7SASMBw/en-us_image_0000002532750029.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41F6912FEC20C91080A7C11F0D68172B05B921B443796B67D9774FF207345695 "Click to enlarge") to navigate to the associated slice.

#### Viewing the Layout of a Specified Frame Page

Since DevEco Studio 5.1.0 Release, you can view the layout information of a specified frame page in the latest recording session.

Currently, this feature is not supported on wearables.

1.  Click any frame in the RS Frame or App Frame sub-lane. In the **Details** panel, click **Open Layout** or **Download Layout**: **Open Layout** opens the corresponding .arkli file directly in ArkUI Inspector; **Download Layout** downloads the .arkli file to a specified folder, which you can later import into ArkUI Inspector to view the layout details.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/YOYaRNszTSq6Op94nNNWSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D902AB3F1E26509F6568BBBC8B109A2654FEABE4C59C1DB389A9FD1282B92E1)
    
    Before clicking **Download Layout** or **Open Layout**, make the app is running in the foreground to accurately capture full rendering data and generate the .arkli file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/tY6LsDDEQJOJeyJ1U-WLwg/en-us_image_0000002501069996.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4ACE364A59F07E08BA8E84F26E03B99B79617ED2412A3B5E08297B5C592E22D5 "Click to enlarge")
    
2.  In ArkUI Inspector, inspect the component hierarchy and attributes, including but not limited to the following:
    
    -   **BackgroundFilter**: background filter.
    -   **nodeGroup**: node group type. The value **0** indicates a node that is not part of any node group, **1** indicates a node group marked by an animation, **2** indicates a node group marked by UI, **4** indicates a node group marked by the user, and **8** indicates a node group marked by a foreground filter.
    -   **nodeGroupReuseCache**: cache usage. The value **0** indicates that the cache is being generated or no cache is needed, and **1** indicates that the cache is being reused.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ABcPkvNGRJikOTEqdYDIxg/en-us_image_0000002532670081.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF6C365A28F2A09BE824EF5D81E447314265ED078FCFD8C582E3A4B39C1A06D2 "Click to enlarge")
    

#### Checking Frame Data Statistics of a Process

1.  Drag the mouse on the timeline to select a time period.
2.  Select a sub-lane (for example, a lane with the RS Frame tag).
    
    The **Details** panel in the lower part displays the RS frame statistics in the selected period, including the start time, total duration, GPU duration, and jank type of each frame.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Ud8wjIcDSUOs99wqClnbvA/en-us_image_0000002501070008.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61ED49EDB3E089414DF71C5937BF150C84043FF52DCCC45F2591678F05EB9991 "Click to enlarge")
    
3.  Click any frame in the list. More key information about the frame is displayed in the **More** area on the right. You can learn about the expected start time and expected duration of the frame. You can also click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/smQYgUi9RDGfoymH3WdhZw/en-us_image_0000002500910144.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCA5172FA3A3327526315CEF936D09F38A3A0C73B33ABE8CEEFDA5E20A29B36A "Click to enlarge") to navigate to the associated slice.

#### Checking Frame Information

Select a frame in a sub-lane (for example, a lane with the App Frame tag). Above this sub-lane is the most time-consuming non-UI function, and below it is the UI main thread lane.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/54Id_jfrR8SV5dMOphgmZA/en-us_image_0000002501070000.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6E13EB82B12C75C1A27C1B86CF12A7F4C85B5298AF3EA5D134842EBE093DA88 "Click to enlarge")

The details panel in the lower part displays the key information about the frame, such as the VSync ID, start time, and duration. The Non UI area displays the functions that consume the most time in non-UI scenarios, including the start time, end time, duration, and function name.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/-wRNEpkHQkGIXF75I7reSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5B5891731135C2A2014C72DD8D1FA43B58DC335B5B74E6FF4D0FF75773C207C)

-   After an object is selected, DevEco Profiler automatically associates the slices related to the object with arrows.
-   If the frame exceeds the expected end time, two lines are displayed, corresponding to the expected start time and expected end time. The two lines are used for association analysis of traces or function sampling.
-   If you hover the mouse pointer over a frame, a tooltip is displayed, showing the jank information of the frame.
-   The following jank types are available: **No Jank** (no frame freezing), **AppDeadlineMissed** (frame freezing on the app), and **RenderDeadlineMissed** (frame freezing on Render Service).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/qPR9GBdOScu43kmB5kihgw/en-us_image_0000002532750027.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D347F4C766BDEB781D54BDA2D495E1E17C3335DB79C3A0410AF01CD409AD7B4E "Click to enlarge")

#### Inspecting Frame Loss and Stuttering in Scenarios Where the Screen Frame Rate Dynamically Changes

Leverage the Lost Frames and Hitch Time sub-lanes to pinpoint and refine issues related to frame loss and stuttering.

-   Hitch Time: displays the duration of stuttering within a specific time frame. It is calculated by subtracting the expected time for a single frame from the interval between the rendering of two sequential frames. If the result exceeds 70% of the expected time for a single frame, it is flagged as stuttering.
-   Lost Frames: displays the number of frames lost within a certain time frame. The frame loss data is rounded to the nearest whole number for analysis.

1.  Create a Frame analysis task, and capture related data. If there is any frame loss or stuttering, rectangular graphs are displayed on the corresponding timestamps in the Lost Frames and Hitch Time sub-lanes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/pkkN-bq1QZ6C9aV3c-ln2w/en-us_image_0000002501070016.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4965EC636D9AEBC840E43BD331F4C9A8D0DF9B4FEDB268907064E9546FBDB82A "Click to enlarge")
    
2.  Click a specific time point, and you can view detailed information displaying the number of lost frames and the stuttering time for that period.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/FcCF1Ax_S4yR6K2RNoousg/en-us_image_0000002532670087.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A015B5D7BBB0B75F5069611E539F898D77E90D4BBFAE47BFFB0CC2C9E912B12 "Click to enlarge")
    

#### Enhancing Animation Performance

Animation smoothness is crucial for a positive user experience in apps. To help you optimize animations for a smoother experience, DevEco Profiler provides profiling for animations.

Hover the mouse pointer over an animation. The detailed information about the animation is displayed, including the response latency, animation duration, completion latency, expected frame rate, and FPS.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/qgps3dvPTDqhlgNMZFlS3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEFE85C59EC04EECE499B1AA7AFD6476D1438DDCF26220AA5B18F0513C77A3C2)

-   Response latency: displayed in green if the latency is less than or equal to 85 ms; displayed in light green if the latency is greater than 85 and less than or equal to 150 ms; displayed in light red if the latency is greater than 150 and less than or equal to 250 ms; displayed in dark red if the latency is greater than 250 ms.
-   Expected frame rate: highest frame rate at which the system operates smoothly, such as 60 Hz, 90 Hz, or 120 Hz. In smart refresh rate mode, the expected frame rate is not displayed.
-   Animation duration: displayed in green if the FPS is greater than the target frame rate; displayed in dark red if the FPS is less than the target frame rate. In smart refresh rate mode, where the frame rate is variable, the color is gray. The target frame rate is related to the expected frame rate. Typically, the expected frame rate is 60 Hz, and the target frame rate is calculated as 60 Hz x 91.7%.
-   Completion latency: displayed in dark red if either the response latency or the animation duration is in dark red.
-   In the launch template, after you click a launch animation record in the detail panel of the Frame lane, the **Animation Data List** information for the animation frame is displayed in the **More** area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/OnyLrG0vSw-CYfB2a9W4Kw/en-us_image_0000002501069988.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADB6B798507F107F596605B3CA5C3C6DE1AF044AC3AC6ADE4F5D576607AA8A6E "Click to enlarge")

#### Checking the Component Animation Information

Since DevEco Studio 6.0.0.828, the Component Animation sub-lane is added to the Frame lane to display various animation types in the app from the perspective of components, including attribute animation (**animation**), explicit animation (**animateTo**), and keyframe animation (**keyframeAnimateTo**) and page transition (**pageTransition**).

In the **Details** tab, you can view detailed information for each animation, including start/end time, frame rate, animation curve type, and the component properties affected by the animation.

Click an animation in the list. The **More** area on the right displays the property change process of the component affected by the animation. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/RSdBg-HwRF-OUMHvjXfbcg/en-us_image_0000002501070010.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71666FA97FA3A86DB40C41480824D5BA8502276F613D758EF4B8AF28A791F7F1 "Click to enlarge")

#### Checking the Frame Rate of a Component

You can use the Display Vsync and DisplaySync\_cb (tid) sub-lanes in the Frame lane to detect the variable frame rate.

-   Display Vsync: displays the screen refresh rate in the selected time period. The distribution statistics of VSync signals in the period are collected by the following categories: ≤ 30 Hz, 30–60 Hz, 60–90 Hz, and > 90 Hz. The statistical items include the distribution ratio, minimum/maximum/average duration, and average Hz of each category in the selected period. When the underlying system adjusts the frame rate, the information is updated automatically. This helps you know whether the VSync changes meet your expectations. This lane supports data collection only on devices equipped with a hardware screen.
-   DisplaySync\_cb (tid): displays the frame rate of a component, for example, **DisplaySync** or **XComponent**. The frame rate is variable in different scenarios during debugging. Therefore, you need to check whether the actual system performance meets the expectation. This is especially true for rendering of **DisplaySync**, which is executed in the UI main thread. Simultaneous rendering requests will be queued in the UI main thread, and any delay affects the rendering of other components, causing UI frame freezing.
    
    As shown in the following figure, in vsync2 and vsync4, the component rendering in the VSync period takes a long time, squeezing the rendering time of the next Vsync period and causing frame loss.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/6Cm_E-moQaysyZuQmGHQ7Q/en-us_image_0000002532750021.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=034BCA5F033E4C0867997BA5C0E6ACE14DDBD48D33F9256BE41B16C2648F318A "Click to enlarge")
    

1.  Select the Display Vsync lane and drag the mouse on the timeline to select a time period.
2.  On the details panel, view the screen refresh rate, maximum duration, minimum duration, average duration, and average number of frames in the selected period.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Jste31q1QFafJxxHG92egg/en-us_image_0000002532750039.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=772EA7ADA68FEAAB582AC2A11DC0864B67876AFE2CB5E7C8C3E0051EAED706B8 "Click to enlarge")
    
3.  Click the Display Vsync lane to view the time consumption and frame rate of the current frame.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/fIDjfkB4QOmYar6oV1V4zA/en-us_image_0000002532670089.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B07503B29218BBE6E6037F2EA2833AE9F9AB56C0AB22D92F0757498A52D47611 "Click to enlarge")
    
4.  Rectangle select the DisplaySync\_cb lane to view the frame rate and rendering time of the component on the app side.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/fhJRGIHcT5aCoUSQrH6s9Q/en-us_image_0000002532670085.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90418E7BBA9D050FCC709013A1779769C7CEA368330AE4941748F118CBF398A1 "Click to enlarge")
    
5.  If frame loss occurs in the component, the DisplaySync\_cb lane displays the frame loss information in red.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/N8TB3k6WR7e6pb4VmxB43w/en-us_image_0000002500910148.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AE3C701E99ADAE32302D25F88E1E77E53ED95FF3569138B5C29455BEB63FC27 "Click to enlarge")
    

#### Viewing Frame Rate Statistics

You can use the fps mark in the App Frame and RS Frame sub-lanes of the Frame lane. You can also use the Filter button in the RS lane to filter ArkWeb data.

1.  Expand the Frame lane and rectangle select a segment of data.
2.  The fps mark is displayed for the lane, and the frame rate statistics in the selected range are displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/FHlAq-UGQPqB2xWzN0QmGA/en-us_image_0000002532750031.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B9F0B50C28147139AF595E4DA94D73202E567253C8AF49B6E6DE724FAE43BFA "Click to enlarge")
    
3.  Turn on **Only ArkWeb data** to display only data that contains ArkWeb frames.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/r3-COImXTFWzK2bi0uZmAA/en-us_image_0000002532670071.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB3FD6953DF15E6B23C87A844EE2A28080BCB93882DBF6A1F877B3724068C948 "Click to enlarge")
    

#### Identifying Prolonged Decoding and Threshold-Exceeding Serialization or Deserialization Operations

If there are images in the project and jank occurs during decoding or rendering, you can use the Anomaly lane to check whether an alarm indicating slow decoding is generated during decoding in the main thread. If yes, determine the time period when the alarm is generated.

If worker threads of TaskPool or Worker are used in an app, cross-thread object passing is typically triggered, along with serialization and deserialization operations. For operations that exceed a certain threshold in terms of time consumption, the Anomaly lane provides a corresponding warning and indicates the start time and duration of the operation.

1.  Drag the mouse on the timeline to select a time period. When the duration exceeds 50% of the VSync period, a red alarm "Image decoding has exceeded 50% of the VSync time" is displayed in the Anomaly lane.
2.  On the details panel, view the statistics on excessive decoding time, including the type, resource name, count, total duration, minimum duration, average duration, maximum duration, standard duration deviation, source size, and target size.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/rbp8zvNCQsm6649NC2tbDQ/en-us_image_0000002500910160.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=100E7FDDF35A53522C949D21818EE46C69B1FCFB673F4D4B3659A618F6FB5C85 "Click to enlarge")
    
3.  Check the Anomaly lane for warnings on serialization and deserialization operations that exceed the threshold in terms of time consumption. You can click the lane start configuration button in the toolbar to configure the detection threshold, with the default threshold set to 8 ms.
4.  On the details panel, view the statistics on time consumption of serialization and deserialization during the recording period, including the type, count, total duration, minimum duration, average duration, maximum duration, and standard duration deviation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/HvAHJ3htTpmX22yUAW-Kfw/en-us_image_0000002532670065.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9E467228A291D6B577DDD9995482040911CFC4C1C530BA0F71B3C7013E35F8E "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/-VBuWelzTxmdDCP7id-6kQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE29847BE609FDA08C687747B18833555A4E90FE174EDA079733F5D5260195D1)
    
    The Anomaly lane is not available for apps that have been released on AppGallery.
    

#### Viewing User Event Duration

In janky frame scenarios, you can view the event start time, app processing start time, and app processing duration through the User Event lane.

1.  Select the User Event lane and drag the mouse on the timeline to select a time period.
2.  The details panel displays details about user events in the selected period, including the user event ID, event start time (**Input Time**), app processing start time (**Processing Start**), app processing duration (**Duration**), and event type (**User Event Type**).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/HmYcvRRsTdO2ad09Ct8ftw/en-us_image_0000002532670073.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=462030D60AFAD54F035EB2782A5A560592C95C810DEBFCF5555D26230B764C3F "Click to enlarge")
    
3.  Click a bar in the User Event lane. Details about the event are displayed in the **Slice Detail** area.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/7v_U133lTTeJ-tt-aTvgCA/en-us_image_0000002501070018.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24B4D63321E9780D1DCB31D1A4795B40D9F9A30BCB2481BBB715635940C46EE9 "Click to enlarge")
    

For more performance profiling best practices, see [Analyzing Touch Response Latency](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-click-to-click-response-optimization), [Analyzing Touch Completion Latency](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-click-to-complete-delay-analysis), [Analyzing Touch Response Latency of Web Pages](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-web-click-response-delay-analysis), and [Analyzing Loading Completion Latency of Web Pages](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-web-completion-delay-analysis).
