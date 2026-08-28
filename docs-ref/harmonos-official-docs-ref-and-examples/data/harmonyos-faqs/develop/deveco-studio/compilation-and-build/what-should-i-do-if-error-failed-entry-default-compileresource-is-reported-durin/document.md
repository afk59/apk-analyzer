# What should I do if "ERROR: Failed:entry:default@CompileResource" is reported during compilation?

**Symptom**

When the HAP module that depends on the HSP is built, the error "ERROR: Failed :entry:default@CompileResource" is reported, indicating that a resource file does not exist. However, the resource file actually exists in the HSP.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/FHQyPA7fQYyVCzmxFyaJPA/en-us_image_0000002194318592.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E81D9E88463DB69ABC1BAF557F1A4D5972E59BD93CB9D689EF69B9727B9B166C)

**Possible Causes**

The **module.json5** file of the HSP declares configuration items such as permission request and references the resource files from the HSP. During the build, the HSP resource configuration is merged into the HAP. However, the HAP cannot directly access the HSP resource file during the running.

**Solution**

-   Search for the corresponding resources in each **module.json5** file of the referenced HSP and check where the resources come from.
-   Add corresponding resources to the referencing HAP or **appScope**.
-   Declare the same content in the **module.json5** file of the referencing HAP. In this way, the content in the referencing HAP is preferentially used during combination conflicts. As shown in the preceding figure, the error is caused by the HSP permission declaration. Request the same permission in the referencing HAP to avoid content combination with the HSP.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ctJOdrSUR9eeEcvuj4iO8Q/en-us_image_0000002229758857.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79D40C9009A6B5BDEF182419A2D3F222566216C6D2F783CEB77F39B2B4FB263A)
