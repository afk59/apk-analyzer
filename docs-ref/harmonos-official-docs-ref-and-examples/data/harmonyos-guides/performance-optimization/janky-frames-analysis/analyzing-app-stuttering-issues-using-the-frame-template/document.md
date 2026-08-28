# Analyzing App Stuttering Issues Using the Frame Template

This section describes how to determine whether an app has janky frames, and then analyze the app's runtime logic using call stacks and trace information to identify the root causes.

For details about the basic operations related to app stuttering analysis, see [Frame Analysis](../frame-analysis/document.md).

#### Analysis Steps

To analyze app stuttering issues:

1.  Check whether janky frames exist.
2.  If janky frames exist, further pinpoint the issue based on the call stack and trace information.

#### Analyzing Frame Data

## Determining Whether Janky Frames Exist

1.  Select the Frame lane. The **Statistics** area in the lower part of the window displays the frame information in the selected time range by process. If **Jank Count** is greater than 0, janky frames exist.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Uuqyrg2QR_Cc1jRLKFjOHA/en-us_image_0000002500910372.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9A08EB238146E4A50AB00CC7676619E163ED8A792F0A6D11FA163C677C4C656 "Click to enlarge")
    
2.  Find the process with janky frames in the **Statistics** tab, and click the jump button next to the process name to go to the **Frame List** tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/rC5pzEU3RCqbeQaAc9qnew/en-us_image_0000002500910376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F48926077DAA7009C0699F921A421F28F3C65C6215DCC87DD48788D3948C630 "Click to enlarge")
    
3.  On the **Frame List** tab, sort the process's frames by **Jank Type** in ascending order. You can click any janky frame on this tab to jump directly to that frame, and the frame will be selected in the lane.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/uy5duiBgSgi-V_PlPwnO2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5485B8C45FEAFDE0AD306D5ED12E7C80AF9655BC7426E244D1CE738D17F9E40E)
    
    -   In the RS Frame and App Frame lanes, frames that are rendered normally are displayed in green; janky frames are displayed in red.
    -   **AppDeadlineMissed** indicates app-side frame stuttering.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/NmhV4L-WSIeQBCk9CxuqFw/en-us_image_0000002532750243.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E215250A132B2D3FD706ABEDB96D557E0C58ADFCD055379E86AEDAA05E2734CB "Click to enlarge")
    
4.  Click the janky frame. The **Details** panel in the lower part of the window displays key information about this frame. Click the jump button in front of the app process on the right to navigate to the app process trace.
    
    -   **Expected Duration**: expected duration for rendering a frame. It is related to the frame rate. For example, if the frame rate is 120, and the corresponding Vsync period is 8.3 ms. That is, the frame rendering duration on the app or Render Service must be within 8.3 ms.
    -   **Actual Duration**: actual duration for rendering a frame.
    
    As shown in the following figure, the expected frame rendering duration is 8 ms 330 μs, and the actual duration is 44 ms 54 μs, which far exceeds the expected duration. Thus, this frame is identified as a janky frame.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/BoQrfnsiRN6jkXCr-0xulw/en-us_image_0000002500910378.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF477243860AF8BC67AF76C4DC11F1E413BFB6D0ACD3446EE2392B72FDAC46F7 "Click to enlarge")
    
5.  Select the time range of the abnormal frame and conduct further analysis to locate the root causes based on the ArkTS Callstack lane, Callstack lane, and trace information.

## Analyzing Application Stuttering

1.  Locate and select the abnormal frame to analyze. Check the ArkTS Callstack lane to analyze time-consuming functions on the ArkTS side. Prioritize the main thread call stack, that is, the ArkVM sub-lane where the thread ID matches the process ID. Here, you can view the execution duration of some methods on the ArkTS side.
2.  Check the call stack in the figure below. Except for **(program)**, the execution time of all other entries in the call stack is within the expected frame rendering duration—8.3 ms (since the optimized device runs at 120 fps). Thus, the key focus for analyzing this janky frame is the execution time of **(program)**.
    
    **(program)** indicates that the program has entered a phase of pure native code execution. During this phase, no ArkTS code runs, nor are there any instances of ArkTS calling native code or native code calling ArkTS. As such, it is generally difficult to derive effective information from this phase, and you need to switch to the Callstack lane to view specific call stack details.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/a8vtD1b7TqeTjijHpQZNOw/en-us_image_0000002500910374.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E97D59A9F3B93B5E933D854A420FD578B8D206CD9AF115C8A5A71E5648EA2A8B "Click to enlarge")
    
3.  Switch to the Callstack lane and check the main thread sub-lane (where the thread ID matches the process ID). Scroll to observe the function call stack with the largest proportion in the **%** column of the **Heaviest Stack** area below. In the **Category** column, bright colors represent the developer call stacks, while gray represents the system call stacks. It can be seen that the time spent in the figure below is mainly in system-side .so files, and the specific cause of the abnormality cannot be identified. Next, further analyze the app process trace information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/pfHTspEVRS-Lt9uUduLCTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC4F9B1FABDC505AEEDEA0E0DD506C5331B33C2F3D39574DCB688FC8259E0734)
    
    You can also click **Call Trees** at the bottom to hide system call stacks, reducing interfering information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/NpJulrlmQdq3FX-vU3u3vw/en-us_image_0000002532750245.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55C84F8D2EFF968C77466B66D3AC79F9C8CB9C1DDCB8C8710643E1B8C0F0A549 "Click to enlarge")
    
4.  Switch to the Process lane and view the main thread (whose thread ID is the same as the process ID).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/D830CIJ9Tz-53w6xnYEoEQ/en-us_image_0000002557362621.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=339648F54B48A1D481AF1A7A2A20191DFFB77B6E9420EB3792041F9298DE25D8 "Click to enlarge")
    
5.  The trace statistics list in the **Details** area at the bottom of the window displays time-consuming traces. By expanding the trace with the longest duration layer by layer, you can pinpoint that the primary performance bottleneck stems from three H:CreateImagePixelMap operations. Next, analyze the time consumption of the three **H:CreateImagePixelMap** operations.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/gNZcwR9NQwqK85bFE9R7EQ/en-us_image_0000002501070224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0ABE9DEB61CC1836E56CB305AD475367B5C336DC2ED5A2D09E0C014B1B25913 "Click to enlarge")
    
6.  **H:CreateImagePixelMap** is related to image loading. By checking the service code, it can be seen that this is due to the synchronous loading of network images. You are advised to change the loading mode to asynchronous.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/90ESyiL3Q_ibXwfyaZgmOw/en-us_image_0000002532750251.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=626C2BFE83CF7B2A68A6B94BD79B32F8F05D356FF0297B02F358B21EED3B0DED "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/ZqpTBbMbRIOu3XRS5Y3GYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=900559B36A1F5E08D1374274F034890F7E0EEB16F790A1C38EDF26AD9CB53B5B)
    
    Generally, the image loading process is performed asynchronously to avoid blocking the main thread and to streamline UI interaction. Synchronous loading is not recommended when the image loading takes a long time.
