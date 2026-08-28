# Process Model (FA Model)

The process model is shown below.

-   All PageAbility, ServiceAbility, DataAbility, and FormAbility components of an application (with the same bundle name) run in the same process, which is **Main process** in green in the figure.
    
-   WebView has an independent render process, which is **Render process** in yellow in the figure.
    

**Figure 1** Process model

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/UjoPCCWlSCGnZ6RtHjknjw/en-us_image_0000002537924308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061918Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36FA5F0CC07D673A4F99695B66491128940E0BE6625B257FDFD35CA9EFDEC5A3)

The system provides the following inter-process communication (IPC) mechanism:

Common events: This mechanism is used in one-to-many communication scenarios. Multiple subscribers may receive events at the same time.
