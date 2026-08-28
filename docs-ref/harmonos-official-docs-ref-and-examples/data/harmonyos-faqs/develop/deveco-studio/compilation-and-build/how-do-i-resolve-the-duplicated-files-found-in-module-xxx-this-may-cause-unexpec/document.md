# How do I resolve the "Duplicated files found in module xxx. This may cause unexpected errors at runtime." error?

**Symptom**

During compilation and build, an error occurs: "Duplicated files found in module xxx. This may cause unexpected errors at runtime."

If the .so files with the same name exist in different versions during build, an error may occur. For example, if the .so file from the **har** module's products is copied to the **libs** directory of the **entry** module, then there is a file named **libhar.so** in both the **har** module and **entry** module. If the **entry** module depends on the **har** module, an error occurs when the **entry** module is built.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/5HRMf4dATEuPB_TTT2rdiQ/en-us_image_0000002194318620.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FEECE67B845FD864BEE067D3138905FE75CAED5275E7B417BC2A32E3C8917F4)

**Solution**

Use configuration items such as **select**, **pickFirsts**, and **pickLasts** to choose the .so files to be used. **select** provides precise selection capabilities for native products, with a higher priority than **excludes**, **pickFirsts**, and other configuration items. **pickFirsts** and **pickLasts** pack the .so files based on the priority. The priority order refers to the order of dependency collection, and the later it is collected, the higher the priority.

For details, see [Module-level build-profile.json5 File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile).

Add a **select** configuration in the **entry** module's **build-profile.json5** file to choose the .so file from the **har** module, set **package** to **har**, and select **libhar.so** using **include**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/wSi55HA6QwWqt3qZXU6Y5g/en-us_image_0000002194159000.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B35540F0E1D39F822DF88077A3ABFD21A6A52CD9E76F37DBA4767BFE8190B7A)
