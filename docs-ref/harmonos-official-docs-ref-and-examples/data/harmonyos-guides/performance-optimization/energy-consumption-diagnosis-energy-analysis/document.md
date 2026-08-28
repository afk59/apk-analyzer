# Energy Consumption Diagnosis: Energy Analysis

Since DevEco Studio 5.1.0 Release, DevEco Profiler provides the Energy template that helps diagnose and optimize energy usage during app running. This template offers insights into the following: energy consumption of different components, device temperature, and abnormal energy consumption frames. This template integrates the functionalities of frame, time, and CPU analysis tasks, so you can compare the resource usage in the selected period when analyzing energy consumption.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/L1H9h4d6S-iHEoEOMY4U8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B503D9482E7894C9848FD1ACFC10480DF5E32DAFC6483F741F41BCA0F724B4BD)

Currently, the Energy template cannot be used to analyze app performance on TVs.

#### Locating Energy Consumption Issues

1.  Create an Energy analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md). Alternatively, click **Open File** in the session area and import historical data.
2.  After recording ends, wait for data processing to complete. By default, three energy consumption-related lanes will be displayed: Energy Anomaly, Temperature, and Energy.
    
    -   Energy Anomaly lane: highlights abnormal frames related to energy consumption. Currently, this lane cannot be used for app performance analysis on wearables.
    -   Temperature lane: displays the temperature of the entire system. Currently, this lane cannot be used for app performance analysis on 2-in-1 devices.
    -   Energy lane: displays the energy consumption of each component and the current of the entire system.
    
3.  Click the Temperature lane and hover the pointer over the lane to view the temperature and temperature level in the corresponding time period. This helps you determine whether the temperature increases significantly and further locate the energy consumption issues. The **Temperature Detail** panel displays the average temperature, maximum temperature, and minimum temperature in the selected range. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/9QaRAwdJRcSjlY_XHvAdsQ/en-us_image_0000002501069922.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0220CDDBBBF0784AA9217A5072F8E8577E0E6A0629F4E0432C49926FFEE1F582 "Click to enlarge") 
4.  Click the Energy lane to view the power consumption of different components, including CPU, display, GPU, location, camera, Bluetooth, flashlight, audio, Wi-Fi, and modem. \*Device indicates the current consumption of the entire system.
    
    Rectangle select a section in the Energy lane to analyze energy usage for the selected period. Further analysis can be performed based on the consumption of different components and the call stack information of the Callstack lane.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/lDq1cgJ0SMuB0YhJhgERhQ/en-us_image_0000002501069916.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B3843C951CEBE123C8FB39518C62FC5D4CF3A51CDE016448E361C0E0014416B "Click to enlarge")
    
5.  Click the Energy Anomaly lane and hover the mouse over it to view the number of rendering frames with empty runs (RS Empty Run), the number of frames where dynamic system synthesizer (DSS) fails to be called for synthesis, leading to direct GPU rendering and thus energy consumption deterioration (GPU Consumption), and the number of abnormal high CPU load occurrences (High CPU Load). View the **Details** panel below for details of energy consumption anomalies within the selected range, including the anomaly type, start time, end time, and number of energy consumption anomalies.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/YRhj_-ZXTTOZj98l35ACqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF044F894ECA7D74426120E286EC79182C2B9B480D557E73EA650633E07A550A)
    
    Currently, 2-in-1 devices do not support RS Empty Run and GPU Consumption.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/PL2STcNFQ3CgnGcmBIQjmw/en-us_image_0000002500910076.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EE5B7628E0124469879CA2CE8E997A8BBB035A9C7C01481C2AA75176B4F861A "Click to enlarge")
    
6.  Click the corresponding anomaly type data (RS Empty Run and GPU Consumption), and the **More** panel on the right displays information of such anomaly frames, including frame ID, RS VSyncId, and frame duration. Click the jump button on the right to navigate to the corresponding specific frame in the Frame lane. You can refer to [Viewing the Layout of a Specified Frame Page](../janky-frames-analysis/frame-analysis/document.md#section58691959194312) to check the layout of page components in detail and identify components with energy consumption issues.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/2ahx_J6aT9ul1nq2dnNsJQ/en-us_image_0000002532749947.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC62128E32D1AD1569EAD070073D523F534F9C0E5C195985493FCD9F1B16CC0B "Click to enlarge")
    
7.  Click the CPU high load anomaly data, and the **More** panel on the right displays information of such anomaly frames, including process ID, thread ID, and load value. Click the jump button on the right to navigate to the corresponding thread call stack.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/XjLHPttfQ9meXv55Lxe7xg/en-us_image_0000002532749955.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90E2AC6073667937031FA203765E3D4BE07DFE5DC835D1423C8603932063AFEA "Click to enlarge")
