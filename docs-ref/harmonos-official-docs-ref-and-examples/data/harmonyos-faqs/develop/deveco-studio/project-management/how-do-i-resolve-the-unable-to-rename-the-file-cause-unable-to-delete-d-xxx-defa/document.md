# How do I resolve the "Unable to rename the file. Cause: Unable to delete D:\\xxx\\default" error when uninstalling the SDK on Windows using DevEco Studio?

**Symptom**

The SDK fails to be uninstalled using DevEco Studio on Windows, with the following message displayed:

Unable to rename the file. Cause: Unable to delete D:\\\\xxx\\\\default.

**Solution**

1\. Open Task Manager.

2\. Switch to the **Performance** tab page.

3\. Click **Open Resource Monitor**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/a3h8yI9oRHCZHXGhQXgpfw/en-us_image_0000002194158616.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC015EA958A7474E3D63641D193D415B1FA88C6A0F64BBD15ED27DC2BC183BE7)

4\. Paste the path in the error message (**D:\\_xxx_\\default**) to the search box on the right of the associated handle window, press **Enter** to search for the process that is occupying the SDK, and end that process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/vh522JMmSkKGgSygg-3B5Q/en-us_image_0000002229758493.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BC7206D3FDD807DACA25E614769E0A9C8EB3C80F0E6D57624A21DDF08A005B9)
