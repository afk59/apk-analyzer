# How do I resolve the "Failed to generate NAPI, check the napi\_init.cpp file and try again." error when using the Node-API generation feature?

**Symptom**

An error occurs for generating glue code when you right-click a function and choose **Generate...** > **NAPI** from the shortcut menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/TBMSbfj4Ra-m_-V9PLdKDA/en-us_image_0000002229604349.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=709B4EDD31129B180CA2FF27854C09212E387A7CBEDFA55C1E9379E2EDC165B8)

**Solution**

Make sure the **napi\_property\_descriptor** variable is properly initialized in the **Init** function of the **napi\_init.cpp** file. If the variable is not initialized, add **napi\_property\_descriptor desc\[\] = {};** and generate the Node-API again.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/itXeb_3wRMqshNWVjOdhsg/en-us_image_0000002194318564.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F381EE9D950D53CEE04F1BF521C840BC3EBC91A4D004B9E5E159C28C039969DF)
