# Real-Time Monitoring for Problem Demarcating

Monitor the app running status and device resource consumption, so as to preliminarily determine the possible performance problems and the code to be modified.

DevEco Profiler offers Realtime Monitor for comprehensive device resource monitoring, covering system events, exception events, CPU and memory usage, real-time frame rate, GPU usage, temperature, current, power consumption, and network traffic consumption. This helps you preliminarily identify performance bottlenecks and locate the root causes of issues.

#### Configuring and Confirming the Device Environment

Connect the device to your PC using a USB cable and install your app on the device using DevEco Studio. Then, you can perform the following steps to check the real-time resource usage of the app:

1.  [Use a USB cable to connect](../../../coding-and-debugging/running-your-app-on-a-local-real-device/document.md#section171436512424) the real device to the PC.
2.  Open DevEco Profiler in any of the following ways:
    
    -   On the top menu bar of DevEco Studio, choose **View > Tool Windows > Profiler**.
    -   Click **Profiler** on the bottom toolbar of DevEco Studio.
    -   Press Ctrl+Shift+A (double-press Shift in macOS) to enable the search feature and search for **Profiler**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/sRYDiA-CQEivG48SFRY_Kg/en-us_image_0000002500910434.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3F781A93FF3290870B3206E1770D5F6A15E763BFFC2ABBE4569F84056E7A267)
    
3.  Start the app on your device.
4.  In the upper left corner of DevEco Profiler, select the device, app/atomic service, or process to monitor. If your app has more than one main process (for example, Extension or Render process), you need to select the process that you want to monitor.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/K5XO7iV_Sm6Va1AdMOlAcQ/en-us_image_0000002532750301.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50F7736D7A5882F7F0CB31123D5AB130BF2130B1343A18D71A0A3F46B86642DA)
    

#### Identifying Performance Hotspots

On the **Realtime Monitor** page, the usage of each device resource is displayed by time in a lane. Multi-dimensional information, such as system events and CPU usage, is provided to help you identify performance hotspots.

## Panel Overview

-   The left panel is the real-time data display area. This area displays the instantaneous value of each monitoring item. You can view the usage proportion and specific value of each item in a pie chart or dashboard.
-   The right panel displays the change trend of each monitored item over time, using different graphs (such as histograms, bar graphs, and line graphs). It helps you quickly identify performance hotspots.

The **Realtime Monitor** page displays data from various dimensions, including system events, abnormal events, foreground apps, CPU usage, memory usage, frame rate, GPU usage, temperature, current, power consumption, and network traffic consumption, from top to bottom. You can compare and identify the performance hotspots of the app from these dimensions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/4xdO2B_vTWagCOtcFw-isA/en-us_image_0000002532670363.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF2859847ED3D849A006176D071318949814195A06532B2846DABA35EB11C053 "Click to enlarge")

## Introduction to Lanes

1.  System Events lane: displays statistics on the start and end status of system events in the time window Three types of signs are used in the lane.
    -   Diamond: indicates the start of an event.
    -   Square: indicates the end of an event.
    -   Circle: indicates a time point event, which has no duration.
2.  Anomaly lane: displays abnormal events reported by the device.

3.  Foreground Ability lane: displays the ability status of the app/atomic service. When the ability is running in the foreground, the ability name is displayed. If no ability is running in the foreground, **Background** is displayed.
4.  CPU lane: The pie chart on the left displays the CPU usage of the current app/atomic service, CPU usage of other processes, and idle CPU usage in the time window. The lane on the right displays the overall CPU usage in the time window. The blue part indicates the CPU usage of the current app/atomic service, and the gray part indicates the CPU usage of other processes.

5.  Memory lane: The pie chart on the left displays the memory usage of the current app/atomic service, memory usage of other processes, and unused memory in the time window. The lane on the right displays the overall memory usage in the time window. The blue part indicates the memory usage of the current app/atomic service, and the gray part indicates the memory usage of other processes.
    -   **Current Process**: memory usage of the app/atomic service at the current moment.
    -   **Other Processes**: memory usage of other processes. Prior to version 5.1 Release, the cached memory (which is automatically reclaimed by the system) was counted under Other Processes memory.
    -   **Free**: unused memory. Since version 5.1 Release, the cached memory is categorized under Free memory.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/4oxitZCQTziyUeR1wgUd7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E6943783F9E7EE561AB155849D6A226685C4C48A4E8967D11D88D210E6F2066)
        
        The memory usage shown for the current app reflects its proportional set size (PSS) value. For details, see [Memory Analysis: Allocation](../../memory-analysis-allocation/document.md). The PSS value shown here is marginally higher than HiDumper's reported value, due to rounding operations in HiDumper's calculation logic that produce downward-biased results.
        
6.  FPS lane: The dashboard on the left displays the instantaneous frames per second (FPS) of the current device screen. The red, yellow, and green areas indicate whether the frame rate of the screen meets the expected value. The bar chart on the right displays the FPS of the device during each capture. This lane supports data collection only on devices equipped with a hardware screen.

7.  GPU lane: The dashboard on the left displays the instantaneous GPU usage of the current device, and the lane on the right displays the overall GPU usage in the time window.
8.  Temperature lane: The thermometer on the left displays the current device temperature information, and the lane on the right displays the device temperature information and temperature level within the time window, with data being collected every 3 seconds. Currently, this lane cannot be used for app performance analysis on TVs, 2-in-1 devices, or Car devices.

9.  \*Device Current lane: The dashboard on the left displays the maximum current, average current, and latest current of the device, and the lane on the right displays the device current information in the time window. The current measured by this lane may not accurately reflect the actual consumption due to charging and discharging processes. To indicate this limitation, the lane name is marked with an asterisk (\*). To obtain an accurate reading of the current consumption, enable the disable charging option on the device under **Settings** > **System** > **Developer options**. Currently, this lane cannot be used for app performance analysis on TVs.
10.  Energy lane: This lane includes the device's average power consumption percentage of various components (such as CPU, \*display, GPU, location, camera, Bluetooth, flashlight, audio, Wi-Fi, and modem) over a period. You can select multiple apps from the drop-down list box above the legend, and the total power consumption of these apps is displayed in the lane. The bar chart on the right displays the real-time usage of various components within the time window, and the bar color represents the power consumption percentage of each type of component. The display metric measures the screen current under different brightness levels, but it cannot accurately measure the display current for different color intensities. To indicate this limitation, the metric name is marked with an asterisk (\*). Currently, this lane cannot be used for app performance analysis on TVs. The GPU, Location, Camera, and Flashlight power consumption data is not available for wearables. The Location power consumption data is not available for 2-in-1 devices.

11.  Network Traffic lane: The dashboard on the left displays the instantaneous uplink and downlink rates of the current device, and the dashboard on the right displays the total uplink and downlink traffic in the time window. The bar chart on the right displays the real-time network traffic consumption in the time window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/BaLy7mteSUuQI6DkCfr66w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5724EC1FD6D7F4C6972B99D2B8A2682647B85337BD50FD112C025D49803D5DD)

FPS, GPU, Temperature, and \*Device Current lanes display real-time information about the device in use, rather than information about the app/atomic service.

#### Common Operations

In addition to the presentation of the instantaneous value of data in each dimension and the change trend in the time window, the **Realtime Monitor** page provides multiple interaction modes to help you analyze the data more conveniently, quickly, and specifically.

-   Starting or stopping capture
    
    Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/--koJ_9jTySDtjqg5Z1dtA/en-us_image_0000002532670351.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=576C6E9E74C8A97DA9E19FDFA4F383A07FB49DFD808A45C63FBB27FC70CCE884) or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/li7E04xoQmiX5Ttvx5lUtw/en-us_image_0000002532750309.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F82D3A11EF44C5C3BEF87FE5FA66898DDD229D2A2718F7D54EF0E857FCCFA98) on the **Realtime Monitor** tab page in the session area or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/mFJdQWUyS_eG4Q5MKYAzcQ/en-us_image_0000002501070282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20EEF5EA42F3F5A989F473BF16FD2EAD5F516626B02D47947049022835F03F24) or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/gMuwMst-Rr-9J3qMpjHp6A/en-us_image_0000002532750311.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9897E9FD25278682E886CE80324F2C69C70BE2FB08FE97B8ED8B1E5ECCFADA04) on the toolbar to control the session capture status.
    
-   Filtering lanes
    
    Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/IQCOaixWQoq9IgTvuD38mA/en-us_image_0000002532750313.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9659869742CC5C87529AD739C9AD9830B670AD62CBD88B2E1ED13E5E39F3652 "Click to enlarge") on the toolbar to filter lanes. Filtering out the lanes that do not have data captured can reduce the overhead of data collection. However, it also reduces the number of data analysis dimensions.
    
-   Displaying detailed data
    
    When you hover the mouse pointer over a lane, a marked line of the current time point and the tooltips containing the detailed lane data at this time point are displayed. When you hover the pointer over the timeline, the data for that exact moment of all lanes on the **Realtime Monitor** page is displayed via tooltips.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/_WHSjEBQSo6CygqvadS8Nw/en-us_image_0000002501070280.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6135497A3017F594940C334EA85C482955CB1E4529CC7F6FDA081D3592763E8E "Click to enlarge")
    

-   Selecting legends
    
    On the **Realtime Monitor** page, you can select or deselect legends in certain lanes to add or remove data displayed in the lanes. In this way, you can focus on concerned data.
    

By analyzing the multi-dimensional data monitored in real time, you can learn about the app running status and the hotspot areas where performance problems may occur. Next, you can collect more detailed app running data to analyze possible performance problems of the app in detail.
