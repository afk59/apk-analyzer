# CPU Activity Analysis

You can use CPU analysis tasks to monitor the real-time CPU usage and thread status while your app/atomic service is running. In this way, you can learn about the CPU resource consumption over a specified period and examine critical system trace points (including those of the graphics system and application service framework) to perform more targeted optimization.

#### Checking CPU Usage

1.  Create a CPU analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md). Alternatively, click **Open File** in the session area and import historical data.
    
    Before starting capture in the CPU analysis task, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/-WaKVwY0R_6ciFtkHIrR_Q/en-us_image_0000002532750089.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09825CAB5FB1AA9906CE4E9E860B6E11B3A13D93B4C0965098321589E2986F40 "Click to enlarge") to specify the lane to capture.
    
2.  Operate the CPU Core lane to display the desired CPU usage information of the target app/atomic service.
    
    You can select either of the following from the drop-down list on the right of **CPU Core**.
    
    -   **Slice and Frequency**: Each sub-lane consists of the time slice and frequency. The time slice displays the processes and threads that occupy the CPU core.
    -   **Usage and Frequency**: Each sub-lane consists of the CPU core usage and frequency.
    
    You can rectangle select the main lane to collect statistics on the CPU usage in the selected period. You can query the process statistics in multiple time slices, status statistics by thread, thread status statistics, and data statistics of all time slices.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/TrMwZ-LxRouCCQ-dPa2FXQ/en-us_image_0000002500910212.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A477FF80F3B0B7426760A8C1471433072027B504EB79A9C29C614EA2B3190C8E "Click to enlarge")
    
3.  Expand the main lane. The sub-lane displays the scheduling information, frequency, and usage of each CPU core.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/tPJau8PFQA2hugwHDJeS1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52167F24977DC2CDA1A03D14CD0ABB25DB1F6E0B5EBD1DFC9EE4890F81A68932)
    
    When you hover the mouse pointer over a time slice, the time slices of different processes are dimmed, helping you determine the association between time slices.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/JkwpMHCtTjeTsXaiG4VqNg/en-us_image_0000002532750083.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D8C438A3E4725308596FF17E80E7B653E8F12F9E013D67C40C9144266962E3D "Click to enlarge")
    
4.  Specify a time slice and view the statistics.
    
    -   Click a time slice to query the basic running information and scheduling delay in this time slice.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/cwyJxw0dT-e1GNQ22r4Kwg/en-us_image_0000002500910220.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44201C1B6E127FC39822093EA2F61F030400F03F1E64C70541B34EFF8E412B91 "Click to enlarge")
        
    -   Rectangle select multiple time slices to view process statistics in these time slices and data statistics in all time slices.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/D3QdTaCUSMW26u9DEOY73A/en-us_image_0000002501070068.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=434234498708B8E7CEF80A4ACF963FC82B4B2C16581EC72C991E9DC9F87C0F0F "Click to enlarge")
        
    -   When **View Integrated Scheduling Chain** is enabled, you can click a node in the CPU time slice lane to view the complete scheduling chain of a CPU running thread.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/jUwUsgjrTDmnhV40VrZdmQ/en-us_image_0000002532750091.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43E2FA7B2208B5ED567C463AF57397C522F97C234AA74D87B25D10729B755B6F "Click to enlarge")
        
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/xomrkPsTQAyFEaB13t7f6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2429A6AB3E52D0475DADFADCDF1BE3B70A4C5A25415351E2A5E7195D121BEB6A)

-   In the task analysis window, you can hold **Ctrl** and scroll the mouse wheel to zoom in to or out of the timeline, and hold **Shift** and scroll the mouse wheel to move the timeline leftwards or rightwards. Alternatively, you can press **W** or **S** to zoom in to or zoom out of the timeline, and press **A** or **D** to move the timeline leftwards or rightwards.
-   You can hover the pointer over any position in the lane and press **M** to add a single-point marker.
-   You can rectangle select a time period and press **Shift+M** to add a time period marker.
-   In the task analysis window, you can press **Ctrl+,** to select a single-point marker forward, and press **Ctrl+.** to select a single-point marker backward.
-   In the task analysis window, you can press **Ctrl+\[** to select a time period marker forward, and press **Ctrl+\]** to select a time period marker backward.
-   Energy analysis is available in CPU analysis tasks. For details, see [Energy Consumption Diagnosis: Energy Analysis](../energy-consumption-diagnosis-energy-analysis/document.md).

#### Querying Process Details

You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/C5WH3E1IShmL95IcY-_B6w/en-us_image_0000002532750087.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE17B755D3C523658E3C3D010851BEB4FB7634A98BC80590DC9D8ED51AD3F6F2 "Click to enlarge") on the toolbar to set whether to use the lite mode. In lite mode, trace data collection is significantly reduced, focusing only on the current process, the launcher process, and the render\_service process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/yLaFXjUUT12W5Q8eC4iLBA/en-us_image_0000002500910222.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F51B44F78BC7362FBED0E9329760E8EAD9CA21B1FD1B1A113AF0C2B8D15E78CA "Click to enlarge")

The process lane displays the usage of each CPU core by the process. Expand the process lane to display the thread list and thread running status of the process.

-   Click a time slice in the running status. The running details of the thread in the time slice are displayed, including the start time, duration, running status, frequency, thread priority, process to which the thread belongs, thread to which the thread belongs, previous thread's runtime status, next thread's runtime status, and the waking thread. You can navigate to the previous or next thread's runtime status and jump to the state where the thread was awakened.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/kkcGPgcvRhKY6OKARS-UiQ/en-us_image_0000002532670137.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90823B097D6BB52910D57A6F62E064B6FF00D3940061260C80FF76407DFA6617 "Click to enlarge")
    
-   Rectangle select multiple time slices to view statistics about threads in different running states in these time slices, including the total duration, maximum duration, minimum duration, average duration, number of threads in the current state, and statistics on medium and high thread load.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/aab7ahQmTsCh_4YWMrQ9dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A027FA92A05D6AFA722B3A2ED402507D14F41132C29DCBD6A32DDC52D40AEFD2)
    
    Data for medium and high load is aggregated every 100 ms. A running duration between 24 ms and 48 ms (inclusive) is recorded as medium load, while a running duration greater than 48 ms is recorded as high load.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/_U3O4q--Sn6JmoyrOY0nzA/en-us_image_0000002532750085.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDEACFCCAE83E2C5EEA93E4578791E88F23CDFA95E218C6B35DC2258A9563502 "Click to enlarge")
    
-   Rectangle select the main lane to view statistical information about the parallelism of the threads under this process during the selected time period. The parallelism data is aggregated every 100 ms. You can inspect the total number of threads running within that 100 ms interval, the total time each thread is in parallel, and the degree of parallelism. Click a row to view the corresponding thread ID and the time period during which the thread runs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/vVamKjpoQt-W2I8-_7TxSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34A0190044FA68C92992D1F81E9C020E00EC3F8F8615E5CA2079097BE3D91202)
    
    The value range of **Parallelism** is \[1, number of CPU cores\]. A smaller value indicates a lower degree of parallelism.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/oKz40UiXQRKy8wPoB2oYxw/en-us_image_0000002500910216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF829FC80FD5BEA2AD11B23F90AC0683F0F0F73CF6722E317327AF2951DB9E84 "Click to enlarge")
    

#### Viewing Trace Details

If a trace task exists, you can view the overlay of the trace task triggered by the current thread in the corresponding thread lane. Select a trace.

-   Click a trace in the lane to view its details, including the name, process, thread, start time, duration, and depth.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/hBYpwkYOQNaNoHC_QuwIxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D85D0E84B1DC50DB824D649C5449C7A912F91F834C0E0B54DF2791DC90BD50D3)
    
    -   If you have customized traces for a thread, you can also view the user trace information.
    -   You can identify the trace type based on the thread name. The thread name corresponding to a system trace is in the format of thread name + thread number, and the thread name corresponding to a user trace is in the format of trace task name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/KRO7OlPhQvCSc8SnfoG3Ww/en-us_image_0000002500910218.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09E2EF5B2D05449B1E8F42936D9A2F8BFD41CC111BE8868265E36765C5092A1C "Click to enlarge")
    
-   Rectangle select multiple traces to view the trace statistics list, including the trace names, total duration of this type of trace, average duration of a single trace, and number of times that this type of trace is triggered within the period.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/SdaHfVZJTI-rSG0uaNh4Eg/en-us_image_0000002501070070.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6465E744A79E485A631669998518B33A27801C0DA2A6DB8090011A8ADDE67A5C "Click to enlarge")
