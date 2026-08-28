# Network Diagnosis: Network

DevEco Profiler provides a network template to help you inspect the HTTP stack network and network traffic information during app running, facilitating network optimization. The request duration is divided into the following five phases: DNS resolution, TCP connection, TLS connection, request waiting, and response receiving. The duration in each phase is displayed, allowing for targeted optimization of latency issues. In addition, the details display the information carried in each request, including the request, response, header, body, and cookie information, facilitating network fault locating.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/xG7_Qu8gSVuZUUmX9JuwkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=847A6089C1AD99EF51DCA0389210B729010BFEB6C87EC8CA1EEE9A1B37425E66)

-   The network analysis task only supports the recording and optimization for request-type APIs in Network Kit.
-   Due to privacy and security policies, network analysis is not available for apps that have been released on AppGallery.

#### Viewing Network Traffic Consumption

1.  Click the Network Traffic lane to display the network traffic consumption during the recording. In the data area below the lane, click the **Summary** and **Details** tabs to inspect the respective statistics. On the **Summary** tab page, check the aggregated traffic statistics for each network interface, including the average downlink traffic, total downlink traffic, number of downlink data packets, average uplink traffic, total uplink traffic, and number of uplink data packets. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/6xqI-bEbScGZNWRbsHlUlA/en-us_image_0000002532749843.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEB9EAB3674761830230D59E59A156E4A2EF32DD94A000E479FEB46BC49302D6 "Click to enlarge") 
2.  Switch to the **Details** tab to view the list of network data records sorted in chronological order. Each record includes the timestamp, duration, downlink traffic, number of downlink traffic packets, network data type, uplink traffic, and number of uplink traffic packets. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/9GgSXtKIQQyT-gDDFRSxZw/en-us_image_0000002500909982.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95F26930060C0ED404D412874F0638222F0502B7D8839162C92D064A06F2750C "Click to enlarge") 

#### Viewing Network Request Durations by Phase

1.  Create a Network analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md). Alternatively, click **Open File** in the session area and import historical data.
2.  After recording ends, wait for data processing to complete. Click the Network Request lane. Inspect changes in network requests that occur during the recording in the data area below the lane. In the **Summary** panel, check the network request durations by domain, including the domain name, thread name, request count, average duration, maximum duration, and the average and maximum durations for each phase.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/uKn4F0jdRZKv4MlSUzI4Zg/en-us_image_0000002500909980.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A9B68ABF8497D3F8E72A483398A718EFAD4B7698BAAF32B8C24F2CB763E0468 "Click to enlarge")
    
3.  Select a domain. The **Details** panel displays the durations of all network requests for that domain, including the request ID, thread name, request URL, redirect URL, IP address, total duration, DNS resolution duration, TCP connection duration, TLS connection duration, request waiting duration, response receiving duration, request type, status code, and the protocol version used.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/GmOfq8P9Td6UIKKygyMEJQ/en-us_image_0000002501069820.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7D537FABDD218F8504F0A494798616A2DBA6EB18796171F21FB3D7B86376919 "Click to enlarge")
    
4.  Select an entry in the **Details** panel, and the lane will display its time-consuming block with a dashed frame. In addition, the **More** panel on the right displays the Request Headers, Response Headers, and Response Body of the request.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/l9xWONjLRYOkVPw1onaKhQ/en-us_image_0000002500909976.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3F442E066DB5318894C02E99295A94FB38B12067F72F889D059AA40586567CE "Click to enlarge")
    
5.  Locate network requests that may cause network stuttering, and select its time-consuming block to view the time consumption of each phase of the request.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/MtQy_0jtQ-W4Lr8oLSNQ_Q/en-us_image_0000002501069826.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6614C0641A578C36C936999EFD55117BF08F173CDC85B300A264FE43E4315576 "Click to enlarge")
    

#### Analyzing Network-related Issues During Startup

You can use network analysis tasks in DevEco Profiler to identify and resolve network-related issues that occur during app startup.

The way DevEco Profiler handles an analysis task depends on whether the app is already running:

-   If you select an app that is not started yet, DevEco Profiler automatically starts the app to capture data when the task starts. After the capture is complete, the task enters the parsing phase.
-   If the app is running, DevEco Profiler stops it first when the analysis task starts, and then starts it again to capture data. Once data capture is complete, the task enters the parsing phase.

To start an analysis task, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/xtKs7T1HQf27pl0N9pDjxw/en-us_image_0000002532669903.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B6BB3FA78B8383FF3E26E1EC6681C447150050521EEC3A2283645270D38A98D "Click to enlarge") next to the desired task in the task list.

After the analysis is complete, the data types displayed and processing methods used are consistent, regardless of the app's initial state (running or not).
