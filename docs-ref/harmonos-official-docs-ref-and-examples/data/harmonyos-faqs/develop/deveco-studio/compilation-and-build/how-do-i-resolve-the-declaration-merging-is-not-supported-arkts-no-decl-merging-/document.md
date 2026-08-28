# How do I resolve the "Declaration merging is not supported (arkts-no-decl-merging)" or "Cannot redeclare block-scoped variable 'xxx'" error?

**Symptom**

When the same variable, interface, or enum is declared in different files, DevEco Studio does not flag an issue. However, an error occurs during compilation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/fKMwd6R4QvmcG8uPpoNH_Q/en-us_image_0000002229604153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95390FAAA0E9D83D6D8434013EA25233C9799955AB1F711A081C8EA83AAC9CA8)

**Solution**

If a file does not contain the **export** keyword, it is considered part of the global namespace.
