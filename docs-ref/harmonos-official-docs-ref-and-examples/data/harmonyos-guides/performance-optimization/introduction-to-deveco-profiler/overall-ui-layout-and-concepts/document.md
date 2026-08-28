# Overall UI Layout and Concepts

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/t0nWImsGT_-7-mLj3JB1ZA/en-us_image_0000002532750255.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=199EEDF66C054FA6882951D27598DCCB1440FF9DF50BD5B157833FBAA3F9E328 "Click to enlarge")

The UI of DevEco Profiler is divided into two areas:

① [Session area](../session-area/document.md): manages profiling sessions. This area provides Realtime Monitor to help you identify problem scenarios and preliminarily demarcate the problem. In this area, you can select the target device, app, and process. The created analysis tasks are displayed in a list in the lower part.

A session is an independent and complete performance data unit, which is obtained through one-shot capture. Data in the same session can be associated with each other after being processed by the tool. Data in different sessions cannot be associated because they are collected in different time periods. Realtime Monitor is a session in essence, which is created by the real-time monitoring scenario template. When collecting data in a session, ensure that the scenario is completely reproduced before ending the capture.

The session area also provides scenario-specific analysis task types, such as Frame and Launch, to help you collect and display more detailed data. The collected data reflects the app running status in the corresponding scenario.

② [Data area](../data-area/document.md): displays performance data in a visualized manner. The data area contains the toolbar, timeline, lanes, and details, and displays tuning details in lanes.
