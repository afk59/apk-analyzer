# What should I do if "Provision number exceeds limit" is displayed during automatic signing of a HarmonyOS application?

**Symptom**

When the automatic signing function is used to sign a HarmonyOS application, the error message "Provision number exceeds limit" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/DORDeVoPSxKQRiVz26MBug/en-us_image_0000002194318424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CB9B23B8551FD4CF17941835CEC931F15803B953D37CA8470842F81B577DD6A)

**Solution**

AppGallery Connect limits the use of automatic signing to a maximum of 150 times per developer account within a 30-day period.

To resolve this issue, try the following methods:

-   Method 1: Use the same set of signing files for applications with the same BundleName on a device. Do not sign the applications repeatedly.
-   Method 2: Log in with another developer account and sign the app.
-   Method 3: Wait until the signing limit is reset, and then try again.
