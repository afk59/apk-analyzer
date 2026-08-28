# How do I resolve the "resource busy or locked, open 'xxx\\outputs\\build-logs\\build.log'" error?

**Symptom**

After DevEco Studio is upgraded to version 5.0.3.403, opening a historical project sometime results in the following error message "resource busy or locked, open 'xxx\\outputs\\build-logs\\build.log'."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/O51drVUUSBS8sV-xTrbkMQ/en-us_image_0000002194158364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DC8EF82E59F916D7CD7C6B1B3DAB170559A313B3FFEB0EE9B936BA2550C66CE)

**Possible Causes**

The error is likely due to a conflict in log writing during initialization, where the **build-log** file in the **.hvigor** directory is being used by another process.

**Solution**

-   Method 1: Click **Sync Now** at the top of the editor window.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/zKCGc8HzRZ-83iN1CBceRw/en-us_image_0000002194317984.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18638A9AB953C2CC2F53B5358AFBD40A3F2A11BA4FBAA200E43E3D0FEF9BD408)
    
-   Method 2: Choose **File** > **Sync and Refresh Project** from the toolbar.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/9R5HKqn_T_2ZKpSUYRVFAw/en-us_image_0000002229758229.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D356F0758EBFF2444C7815BA967D2CC2EDEA7023703A7166FF5DBEAD300F15E7)
    
-   Method 3: If the issue persists, manually delete the **.hvigor** directory in the project directory and restart the sync.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/TFI4bzOQTly6gmfNtiTmPA/en-us_image_0000002229758233.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D67F0CEE9B1202C758938C76C9B8014FA3485F284D0CCFB25B0F915696D2C082)
