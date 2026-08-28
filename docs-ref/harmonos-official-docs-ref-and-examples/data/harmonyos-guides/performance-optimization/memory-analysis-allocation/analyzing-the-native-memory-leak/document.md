# Analyzing the Native Memory Leak

This section explains how to identify potential native memory leaks in an app and determine their root causes using the Native Allocation lane.

#### Identifying Memory Issues

1.  Use the real-time monitoring feature to observe the app's memory usage. (For details, see [Real-Time Monitoring for Problem Demarcating](../../using-deveco-profiler/real-time-monitoring-for-problem-demarcating/document.md).) Interact with the app and observe the memory usage changes. If the memory usage remains stable or returns to a normal level after a temporary increase, the app likely does not have a memory leak. If the memory usage continues to increase and does not return to a baseline level, or grows significantly beyond expectations, a memory leak is probable.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/OpGr7NDfQMyhu1k4HC0zig/en-us_image_0000002532749749.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD2DBA573AFFCA64D2D4E054308262E1DA407B125D74E7E998D902FBB3776D28 "Click to enlarge")
    
2.  Once a memory anomaly is suspected, use the Memory lane in either the Allocation or Snapshot template to capture detailed data and analyze memory trends in the affected scenario.
3.  Create an analysis task, and then deselect all lanes except the Memory lane to reduce overhead.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/PcYhRyrLTxq4cFFO3YCxug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A155442DD16E016E3AE8032CBA23E3166C4224E67698515DB1FFC22C009D762)
    
    Additional lanes (for example, memory allocation or object tracking) may interfere with accurate preliminary diagnosis.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/-0yRQkAdQ9GNunFoeMTuEQ/en-us_image_0000002532669809.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59CB4DFA5AE1CE3EBD79120F210DC867C6059CD72E5305ABDD0FD8D9A2939B5B)
    
4.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/4_tOQbUxSxOSH3mOoBsjrw/en-us_image_0000002500909900.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E9BB3C67EBE14B3F4E974E7F46E6D3257A0D9E85FF727DF05F7669F7C4059D2 "Click to enlarge") to start recording.
5.  During recording, continuously perform app operations in the suspected scenario to help reproduce the issue.
6.  To stop recording, click the stop or pause button, as shown in the figure below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/m9gBZJjaS1mPjHrGvcR6uA/en-us_image_0000002501069748.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=516429A1278E2C97B7694857A157CB32710EEFF36F89F97C234B558E59E6A8AC "Click to enlarge")
    
7.  After the recording is complete, expand the Memory lane. **ArkTS Heap** indicates the memory managed by the ARK VM. A significant increase here may indicate a leak in ARK VM heap memory. **Native Heap** indicates the memory allocated through native APIs or C/C++ code. This memory must be manually managed by developers. A significant increase suggests a native memory leak.
    
    Use the [Snapshot template](../../memory-leak-analysis-snapshot/basic-operations-with-memory-snapshot-analysis/document.md) for deeper analysis of ArkTS heap issues, and the [Allocation template](#section776643810160) for native heap issues.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/hWgYC9kfQDa3ievh6B0byQ/en-us_image_0000002532669803.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=044F34D18B6D9BA998B2F6420E8A6FC6F46C42E5B21EF4576D9B7BC842775940 "Click to enlarge")
    

#### Using the Allocation Template to Analyze Native Memory Issues

## Recording Allocation Data

1.  Connect the device and click the app selection box to select the target app. Select the **Allocation** template, and click **Create Session** or double-click the **Allocation** icon to create an allocation session.
2.  Click the triangle button to start recording.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/jGniN6QYQKK1afnf9pE3tg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F101FBB70DFD5B921DAE295F1C65A092A326FC155BACE8F6395A87F523CCB61)
    
    To analyze the launch memory, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Fr-P2KWdQ82hb2YEgMdB1A/en-us_image_0000002500909894.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21C47F64BF3C54EE5CB2D5DFA4B462B17F5CFAD2C87630C0A931BC8C3BAA2047 "Click to enlarge") next to the allocation task.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/vvBwTp47Tly0jVzATeBqyg/en-us_image_0000002501069742.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58B0739309AB0ADBBC403DE296A850FAA55AAB3D2D38A822B1BEAE895B49C309 "Click to enlarge")
    
3.  Operate the app to reproduce the issue. After the issue is reproduced, click the square button in the following figure or the stop button on the left to stop recording.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/WUJodNFtShSmFNEFj2hrIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AC7CA1FB5D35747977DD634F7EABC62BF3CAC3F2E4FA12FEED6CD7BA7733F14)
    
    By default, the statistics mode is used for data collection, where the tool delivers better collection performance and lower load.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/wtRpqqpjTIGZrqulYJy-SA/en-us_image_0000002532749759.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6196733013BE6DC22F0856DF40F112800546B8D27F516C2466DC184147A4EA33 "Click to enlarge")
    

## Analyzing Native Data

1.  Select the Native Allocation lane or sub-lane. The All Heap and All Anonymous VM sub-lanes indicate the memory allocated by the **malloc** and **mmap** functions, respectively.

2.  On the **Statistics** tab page in the details area, select **Created & Existing**.
    
    -   **All Allocations**: indicates all memory allocation information within the selected time range.
    -   **Created & Existing**: indicates the memory that is allocated after the start of the selected range and not released before the end of the selected range.
    -   **Created & Released**: indicates the memory that is allocated after the start of the selected range and released before the end of the selected range.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/epCspayzSlKqsYEtIcL-3w/en-us_image_0000002532749751.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A975642B4F2B8AE08370A996A434A03F9D8F7D6AF355B75A528A874474CD0F04 "Click to enlarge")
    
3.  Switch to the **Call Trees** tab and select **Created & Existing** to view detailed memory allocation stack information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Ti9YSc0cSlSNUYztKc1svg/en-us_image_0000002532749765.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51428E8FD68C73ECD36402DC673C053D5ED70B03B9CBAE7001318C75FE6CE618 "Click to enlarge")
    
4.  Prioritize searching the memory allocation stack information for symbol names that are strongly related to the service code. These symbol names will appear in a bright color in the **Category** column. As shown in the figure above, the main leak sources lie on the service code. Conduct analysis based on the service code.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/eH7tsU2pSIqXbbIw9BhbYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23306A8245FE5E9B72490D9397D611360D32F2C2DB1AC25F7A4B222ECEE780EE)
    
    -   In the **Category** column, the bright color indicates the developer call stack, and the gray color indicates the system call stack.
    -   Most of the stack frames are native stacks. Except for the .so files compiled by the app and .so files containing the API information, the other system libraries display only the .so library and function offset information. To view this information, import the .so library with symbols of the corresponding version. For details, see [Offline Symbol Parsing](../../introduction-to-deveco-profiler/data-area/document.md#section11376118192614).
