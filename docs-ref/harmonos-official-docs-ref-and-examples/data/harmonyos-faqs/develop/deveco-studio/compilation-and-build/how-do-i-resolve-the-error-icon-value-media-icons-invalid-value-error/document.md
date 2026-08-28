# How do I resolve the "Error: 'icon' value \`$media:icons\` invalid value." error?

**Symptom**

Compilation error:

ERROR: Failed :entry:default@CompileResource...
ERROR: Tools execution failed.
Error: ref \`$media:icons\` don't be defined.
Error: 'icon' value \`$media:icons\` invalid value.
at D:\\project\\process\_profile\\default\\module.json
Detail: Please check the message from tools.

**Possible Causes**

When a referenced resource does not exist, the file path indicated by the compilation error is the build directory.

**Common Scenarios**

1.  The resource file is not added.
2.  The resource file is deleted accidentally.

**Solution**

Search globally for the resource ID indicated by the error by clicking the search button in the upper right corner to check whether the erroneous resource exists.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/1xWJSrJlSyicMBjRrKAIbQ/en-us_image_0000002262335589.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=168ED97244956CC0D81638DB2833BF31E2755C44DE7B61BE612D7E1A15753CC8 "Click to enlarge")
