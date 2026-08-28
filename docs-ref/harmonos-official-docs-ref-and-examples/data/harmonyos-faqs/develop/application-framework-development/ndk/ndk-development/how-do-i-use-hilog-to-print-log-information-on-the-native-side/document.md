# How do I use HiLog to print log information on the native side?

1\. Add the link to **libhilog\_ndk.z.so** in **CMakeLists.txt**.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)

2\. Include the **hilog** header file in the source file, and define the **domain** and **tag** macros.

#include "hilog/log.h"
#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x3200 // Global domain macro, identifying the business domain
#define LOG\_TAG "MY\_TAG"  // Global tag macro, identifying module log tags

3\. Print logs, for example, print ERROR logs.

Note that the printed content can be displayed only after {public} is added. If {public} is not added, {private} is used by default.

int a = 5, b = 10;
OH\_LOG\_ERROR(LOG\_APP, "Pure a:%{public}d b:%{private}d.", a, b);

Result:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/7EpuVwVtQ96RqMYYFTGZ_w/en-us_image_0000002194318320.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2467C8A3EB0F25853F7451969A18F81EFA71121A61A6BF71A6B0468EAC0A474 "Click to enlarge")

**Reference**

[Using HiLog (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hilog-guidelines-ndk)
