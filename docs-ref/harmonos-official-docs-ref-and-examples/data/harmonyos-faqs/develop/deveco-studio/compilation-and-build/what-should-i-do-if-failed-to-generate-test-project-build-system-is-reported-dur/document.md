# What should I do if "Failed to generate test project build system" is reported during build?

**Symptom**

When multiple native modules are being built, "Failed to generate test project build system." is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/3QxzJbG4Q1ewMFt9jBLdqg/en-us_image_0000002194158584.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A7DED3A961CEF843145A755DAB90778B7CFAA1C3DC83180F601C7D79D4D47B3)

**Solution**

Delete the .cxx folder under the module that reports the error, select the module to be built, and run the **Make Module {moduleName}** command to build the module separately. Do not build multiple modules at the same time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Px0VVDk2Qqis2QiibSBjQw/en-us_image_0000002229758457.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E92C4D5B626590443D79480C4631FDE737FD7D9073C286DB82B484895BBB48A)
