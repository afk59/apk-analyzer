# Loading and Frame Loss Analysis: ArkWeb

During the app development process, incorporating **WebView** into the app can enhance development efficiency, but this may lead to issues such as ArkWeb loading and frame loss. The ArkWeb analysis template in DevEco Profiler allows you to pinpoint the phase where issues occur based on key trace points in the ArkWeb execution process. If the issue occurs during the rendering phase, you can further analyze the frame loss issue by drawing on H:RosenWeb data, thread running status, and frame rendering process tracing data.

#### ArkWeb Loading Analysis

1.  Start an ArkWeb session and complete a recording. During the recording, trigger web-related scenarios.
    
2.  Demarcate the phase when the web issue occurs and analyze the web loading issue.
    
    Based on the key trace points, the web page loading process is divided into five phases: Click Event, Component Initialization, Primary Resource Download, Sub-resource Download, and Render And Output.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Neg1clirQJibRZN9mHN7aA/en-us_image_0000002501070510.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D33330A78DE24614D81755A93454EB6B3CA38516216C63D247DCC564AFE0559E "Click to enlarge")
    
3.  In the details area, you can jump to the lane where the key trace is located to further analyze the loading problem.
    
    Rectangle select a period to view the key trace points that delineate the phases of the lane, and you can associate the trace information with the corresponding thread information.
    

#### ArkWeb Frame Loss Analysis

1.  The ArkWeb sub-lane aggregates the trace information of web-related threads. By analyzing the trace points of key functions in the web rendering process, you can gain insight into the execution process of each frame. The aggregated information is as follows:
    
    -   H:RosenWeb: records the amount of data to be submitted to the Render Service for unified rendering.
    -   Compositor: handles CPU instruction synthesis for layers and manages dynamic effects as the composition thread.
    -   CompositorGpuTh: retrieves rendering results from the GPU and sends synthesized buffers to the graphics subsystem for rendering execution.
    -   Chrome\_InProcGpu: performs rasterization.
    -   VsyncGenerator: generates VSync signals at regular intervals on the graphics side and notifies rendering or animation threads to prepare for next-frame rendering.
    -   VSync-webview: receives VSync signals from the graphics side and triggers WebView page rendering or redrawing based on these signals.
    -   VizCompositorTh: listens for drawing signals, requests Web-specific VSync signals from the graphics system, and triggers system Web-related drawing or execution.
    -   Web app render threads: have names ending with :render and handle graphical rendering tasks, including HTML/CSS parsing and layered layout and drawing.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/EgK_t0i2RJGgM4WuIBV_uw/en-us_image_0000002500910676.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA9D30CE10BB0034AC39EDEF043182BA307B6150048526393A87FE18208BF210 "Click to enlarge")
    
2.  To detect frame loss, you can use the H:RosenWeb and Present Fence lanes. H:RosenWeb indicates the volume of data pending submission to the Render Service. In normal cases, each data chunk is submitted to the hardware for display, that is, the **H:Waiting for Present Fence** trace point on the Present Fence lane. If no such trace point is found for a data chunk on the Present Fence lane, frame loss may occur.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/kTgoK_35S4KeM-B3-ydvww/en-us_image_0000002532670585.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FE28E575DE4F9A3D75DB365B55F24672C92BA6EEBC4AB67C032D0837FACF173 "Click to enlarge")
    

3.  In the sub-lane of ArkWeb, the Web app render thread provides the capability to analyze the specific duration of each phase in sub-resource loading. Switch to the **Sub Resource** tab to view details,
    
    including the uniform resource locator (URL), cache type, whether it is a local resource replacement, resource request time (ns), queue time (ns), stall time (ms), DNS resolution time (ms), connection time (ms), SSL connection time (ms), server response time (ms), download time (ms), transmission time (ms), request method, status code, resource size before encoding, resource size after encoding, and HTTP version.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/t_B7EeSCQ7aFGbIQr4XcUw/en-us_image_0000002501070514.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=268628F41AD710B6F370B577FF78BA84405E016C4AB863154442DB9104475B2D "Click to enlarge")
    
4.  Click on a row to view the corresponding cache information for that URL, including the cache lifetime, last modified time, expiration time, cache directives, unique resource identifier, and whether the resource has expired.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/H77j8Ek1TYWAsEFqFWEGhg/en-us_image_0000002532670587.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D93F544509767EC7718D5DF26016405A361C76C63C82771CCB5951FE947020D4 "Click to enlarge")
