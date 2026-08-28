# What should I do if the type of the output operator is incorrect for the OMG offline model?

In the Caffe network, some layers of the same type have different computing functions. For example, at the **DetectionOutput** layer, you need to specify the detection operator types such as **FSRDetectionOutput** and **SSDDetectionOutput** through operator mapping. Otherwise, the OMG fails to generate the offline model. To avoid errors, use either of the following solutions:

-   Solution 1: Add the **\--op\_name\_map** parameter to the OMG command. For details, please refer to the settings of the **op\_name\_map** parameter in [OMG Parameters](../../model-conversion/offline-model-conversion/omg-parameters/document.md).
-   Solution 2: In the proto model file of the original network, specify the output operator type as **SSDDetectionOutput**, as shown in the following figure.

**Figure 1** Output operator type before modification (left) and after modification (right)  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/4k3C5EtgTSSzGvqyTolL-w/en-us_image_0000002528408567.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A8CE6E90B6C4B21D3DA17EC9A487FC2410D802C5C79D951BE9E919020AD3C6E "Click to enlarge")
