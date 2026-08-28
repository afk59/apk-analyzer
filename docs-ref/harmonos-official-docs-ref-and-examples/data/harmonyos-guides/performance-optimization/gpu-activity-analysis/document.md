# GPU Activity Analysis

Since DevEco Studio 6.0.0 Beta3, DevEco Profiler provides a GPU template to display detailed information about the usage of GPU hardware modules. This information helps identify the root causes of low GPU utilization and performance bottlenecks in executing graphical and computational workloads.

#### Constraints

-   Currently, this feature is available only in the Chinese mainland.
-   Only phones are supported.

#### Procedure

1.  Create a GPU analysis task, and capture related data. For details, see [In-depth Capture for Problem Locating](../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md).
    
    Before starting capture in the GPU analysis task, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/WcMIlofBSNWDmqSjnaGyMA/en-us_image_0000002532750075.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AD15D17C21726B663BA4B832DC80FAB1084C3A96F7F5BE5291BBFA8E7461D1C "Click to enlarge") to specify the lane to capture. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/LdHdtscqRIy_yVVHyAD6nQ/en-us_image_0000002500910208.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B13CEF8C1B68CEA01A3C5D4F991A8A9FA49FBA00C5FA69B5FD27EEE1AC77C533 "Click to enlarge") on the toolbar to set the sampling interval, ranging from 1 ms to 1000 ms. The default interval is 10 ms.
    
2.  The Counters lane displays the GPU usage of the current device. For details about the ArkTS Callstack, Callstack, and CPU Core lanes, see [Basic Time Analysis: Time](../basic-time-analysis-time/document.md) and [CPU Activity Analysis](../cpu-activity-analysis/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Au-mPAboQMqVIxtQ8vTkPg/en-us_image_0000002500910206.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D02B56BA99E57E6FA2D3B2D88AAE652148B90396594FBD02A8FEA7FFD6B67B93 "Click to enlarge")
    
3.  Expand the Counters lane. The sub-lanes display GPU activity information, including counters\_gather, the frequency of executing commands on the GPU, and the duration of command execution. For details about the sub-lanes except counters\_gather, see [GPU Counters](https://developer.huawei.com/consumer/en/doc/Tools-Guides/gpu-counters-0000001886127538).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/xadgaRApTcaGWmir9UhdtQ/en-us_image_0000002532750079.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53851B7FBD2B1512D70A1D1872A277460D75EA3E318CE80F10ED9CF54E5E87C9 "Click to enlarge")
    
4.  The counters\_gather lane displays the usage of each CPU core by the thread. Click a time slice in the running status. The running details of the thread in the time slice are displayed, including the start time, duration, running status, frequency, thread priority, process to which the thread belongs, thread to which the thread belongs, thread's previous runtime status, and thread's next runtime status. You can navigate to the thread's previous or next runtime status.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/PgeFXQK1Tf2M6R4CoPjc-A/en-us_image_0000002532750077.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD3B7D1AE3C6FEB18544A80EAEF3CB9C8FF959310E1E661CBF1CB67CFA908D1C "Click to enlarge")
    
5.  Rectangle select the counters\_gather lane to view the statistics in this time slice, including the thread status, CPU single-thread usage, and thread load data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/a3ONkye9Txic7aLIpvWHRg/en-us_image_0000002532670129.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C2CDFA2164A9A5F599EAA5FE723FECEA4283ED627EFB7C69B0F226C05316466 "Click to enlarge")
