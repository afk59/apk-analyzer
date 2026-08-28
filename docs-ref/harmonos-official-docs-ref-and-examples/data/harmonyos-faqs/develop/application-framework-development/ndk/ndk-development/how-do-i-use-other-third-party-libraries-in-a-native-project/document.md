# How do I use other third-party libraries in a native project?

1\. Place the .so library file in the **entry/libs/arm64-v8a/** directory of the native project, and place the header files of the library in the **entry/src/main/cpp** directory. You can add a folder in the **cpp** directory to store the header files of the third-party libraries.

2\. In the **CMakeLists.txt** file, add the link to the .so library.

3\. Include the header file of the third-party library to the **.cpp** file.

Example:

Integrate the third-party library curl to a native project.

1\. Place the curl library (**libcurl.so**) in the **entry/libs/** directory of the native project, and place the **include** directory that contains the header files generated after the porting in the **entry/src/main/cpp** directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7pHAaKdXQ7mD1ICySN3X2Q/en-us_image_0000002194158760.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=977B220C23CF58DC30168D9EE21AF393F0BABC0CA330C70976BB4418EE1056F9 "Click to enlarge")

2\. In the **CMakeLists.txt** file, link the curl library.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/9uWFSbxPT3u1vFah6UQFRQ/en-us_image_0000002194158764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=856A1D5256BC6B966801E398EA804DF3EAECA8C19A9B199BC5FAFDD3BE8857A0 "Click to enlarge")

3\. Include the header file **curl.h** to the **.cpp** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/RnVQaD28TqCwWcyMXkXuFQ/en-us_image_0000002229758629.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94F0EA7155F8A2B0555B13011C0D27869ED53D944F1CBE1B3F32DDCE9A5DB9F0 "Click to enlarge")

**Reference**

[Building an NDK Project with Prebuilt Libraries](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/build-with-ndk-prebuilts)
