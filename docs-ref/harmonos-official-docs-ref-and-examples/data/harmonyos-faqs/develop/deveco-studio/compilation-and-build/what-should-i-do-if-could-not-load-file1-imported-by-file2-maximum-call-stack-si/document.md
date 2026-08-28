# What should I do if "Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded" is reported during compilation?

**Symptom**

The stage model project fails to be compiled and built, and "ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded" is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/FESw_icETdyMcf1rkWGxBg/en-us_image_0000002229758241.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E77E4F40EFE6ECE885CBB7486BB29CA9CB20EA0D23C6240436043EBDB0151F6)

**Solution**

This issue occurs because **file1** is located outside the current project. The procedure is as follows:

1.  Right-click the project and choose **New** > **Module...** from the shortcut menu.
2.  Select the **Static Library** template.
3.  Add the HAR reference to **dependencies** in **build-profile.json**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/giF69I3-TkmuU-knffkBZQ/en-us_image_0000002194158380.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DF6790224E98DAD794483546AFAB6287C23E646A54F652E28CCEA26DF62978E)
