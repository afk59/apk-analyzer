# UBSan: Detecting Undefined Behaviors

Undefined behavior in code might seem harmless at first, but it can lead to program crashes or errors as code complexity grows, making the root cause difficult to pinpoint. Undefined Behavior Sanitizer (UBSan) is a tool designed to identify such behavior and assist in resolving runtime errors stemming from undefined behavior.

Below are common instances of undefined behavior:

-   Division by zero
-   Use of unaligned pointers or references
-   Overflow caused by floating-point conversions
-   Accessing null pointers

This feature is supported since DevEco Studio 5.1.0 Release.

#### Constraints

ASan, TSan, UBSan, and HWASan cannot be enabled simultaneously; only one of these sanitizers can be active at a time.

#### Enabling UBSan

You can enable UBSan in either of the following ways:

## Method 1

Choose **Run** > **Edit Configurations** > **Diagnostics** and select **UndefinedBehaviorSanitizer**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/PQY1OyxvQJWp3VKhdeOnQA/en-us_image_0000002532670123.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D93104B46246BE3C423ABFEECD7F18803AA25B483EFD7517E3AB938958AE67C5)

## Method 2

In the module where UBSan needs to be enabled, add build parameters to enable UBSan instrumentation. Specifically, in the **build-profile.json5** file of the module, add the following:

"arguments": "-DOHOS\_ENABLE\_UBSAN=ON"

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/OxzVJBGdQ9C21a5IpaEv1A/en-us_image_0000002501070048.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9635B2912D5D423A0D0C81DED7A9207EB5BBE7CE4D2B2752E760A6C9A1226DC)

#### Using UBSan

1.  Run or debug the app.
2.  When UBSan detects undefined behavior, it displays log information. You can click the provided link in this information to directly navigate to the code causing the undefined behavior. For details about the error types detectable by UBSan, see [Detectable Error Types](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-stability-ubsan-detection#section124211321406).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/T9FntXkPR9WN3_PwSrRmIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=745430759DD1309861B1F9BCD0A6D6C73E616BE1D402B2A93066B7D2A2DB699D)
    
    This direct link to the source code is available regardless of whether the [build mode](../../../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916) is debug or release.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/lbZFh32_QlW-LVXnj8bx4g/en-us_image_0000002532670125.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=182FC0F69F7A5340AAB07F69F679E0140BDC97820BB08FD5998A5709CE130672)
