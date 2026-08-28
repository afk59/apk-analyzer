# How do I resolve the "Could not find usage of napi\_module\_register in napi\_init.cpp." error when using the Node-API generation feature?

**Symptom**

An error occurs for generating glue code when you right-click a function and choose **Generate...** > **NAPI** from the shortcut menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/GAiDqtuySvWSAIAk87mpQg/en-us_image_0000002229758437.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF8F5F94A7F1B88B969084F1547FA27C4F8C6F4AA8C9A391121C2313CFEE419F)

**Solution**

Make sure the **napi\_module\_register** function is correctly called within the **RegisterEntryModule** function in the **napi\_init.cpp** file. The parameter type of **napi\_module\_register** is **napi\_module\***. The following figure shows the sample code for **napi\_module** initialization. Then, generate the Node-API again.

The field meanings are as follows:

**nm\_version**: Node-API module version.

**nm\_flags**: module attribute flag.

**nm\_filename**: file name of the Node-API module.

**nm\_register\_func**: registration function.

**nm\_modname**: module name.

**nm\_priv**: pointer to private data.

**reserved**: reserved field.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ySr78lLyTIOSQaDVVykVSQ/en-us_image_0000002519864254.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=561D0EB1A7957D0BBC69B368FCB3C348F4BB7603E1F9D57E8C30540D2CAA8A3C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uOtdmf6gQWmNArCGPJkqGQ/en-us_image_0000002229603969.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5B01E2295417A3E6B9F4713039F886E290821F74AF69BE5FE080881DB8F2EE4)
