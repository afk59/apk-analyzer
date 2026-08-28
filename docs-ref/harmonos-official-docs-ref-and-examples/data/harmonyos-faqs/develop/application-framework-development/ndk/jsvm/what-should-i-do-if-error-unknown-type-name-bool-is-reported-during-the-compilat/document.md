# What should I do if "error: unknown type name '\_Bool'" is reported during the compilation of an HAP project?

**Symptom**

When a HAP project is built, the compilation tool reports "error: unknown type name '\_Bool'", which indicates that the \_Bool type cannot be found.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/bTRGLCSGRmOgK8jYeLTKmA/en-us_image_0000002229603937.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062547Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FC7C6AAED72EE5A006706A5CDA0EE219D504223B1A5969E7C3F26F1F9ECFC72)

**Possible Causes**

JSVM-API is based on C-API of the C99 standard. Pay attention to compatibility when using JSVM-API in C++ projects.

The default setting of Clang++ (the C++ compilation toolchain) provided by the current SDK version is **\-std=gnu++14**. If **\-std=c++xx** is specified, the default setting will be overwritten, and Clang specifies the compilation macros of strict ANSI, which correspond to C90 and does not include any GNU C extension. As a result, \_Bool introduced by C99 cannot be found. The **\-std=gnu++xx** option enables GNU C extension support and does not generate compilation errors.

**Solution**

Check whether the **\-std=c++xx** series options (such as 11, 14, and 17) are added to the build options.

If yes, the following solutions can be used to solve this problem:

1.  If the C++ version is C++14 or earlier, you can remove the **\-std=c++xx** option. The default configuration of the compilation toolchain provided by DevEco Studio is **\-std=gnu++14**.
2.  If the C++ version must be specified, change **\-std=c++_xx_** to **\-std=gnu++_xx_**.
3.  You can also add the **\-U\_\_STRICT\_ANSI\_\_** option to the CMakeLists.txt file to solve this problem.
