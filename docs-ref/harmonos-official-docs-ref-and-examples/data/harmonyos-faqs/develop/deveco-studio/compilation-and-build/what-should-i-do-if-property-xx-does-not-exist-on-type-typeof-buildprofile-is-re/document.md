# What should I do if "Property 'XX' does not exist on type 'typeof BuildProfile'." is reported during compilation?

**Symptom**

The custom parameter **BuildProfileFields** that is not defined in the HAP is used in the APIs externally provided by the local HSP module. HAP references the API in the HSP module. As a result, the compilation fails, and the error "Property 'XX' does not exist on type 'typeof BuildProfile'" is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/QTrdSVRJToi98xzB9B-J3A/en-us_image_0000002194158808.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50C6B9D56FF187B95FD3E765E3165923A06638B60B3BE55AB812C0C52B578D3D)

**Solution**

You can resolve this issue using two methods:

-   Configure the same custom parameter **BuildProfileFields** in the HAP as in the HSP.
-   In the project-level **build-profile.json5** file, configure the custom parameter **BuildProfileFileds** to match that of the HSP. This applies the HSP module configuration globally across the project.
