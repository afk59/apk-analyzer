# What should I do if the network is abnormal when obtaining the template data in device manager and download the Emulator image?

**Symptom**

-   Scenario 1: Failed to obtain the template data. The error message "Network request failed. Verify your network connection and Emulator is available in your country/region." is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/02AUL7rvRiKKe8vtd19Kzw/en-us_image_0000002194318324.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFFAE62652A73DFB417C358F9435A3C0120B6918B67355F80EF081AB780A8A45)
    
-   Scenario 2: Failed to download the Emulator image. The error message "The network or server is abnormal." is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/hkAEZlZYQKmtOR1rCNhMkA/en-us_image_0000002229758585.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10E0C34D5371BA7918BC56F02621BB0E8B5C356960AF7BB191238CE4EB9E2CDB)
    
-   Scenario 3: The Device Management page is empty. The error message "Network request failed. Verify your network connection and Emulator is available in your country/region." is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/g6q59ObVSHybuHJGIGRVoA/en-us_image_0000002313594524.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7275A0ED3DD3D2CDC6DE1D0DCD5392C2DAF7723E3620B1EBBC044192705902A6)
    

**Solution**

1.  Clear the cache files of DevEco Studio on the local PC and restart DevEco Studio. The cache directory is as follows:
    
    Windows:C:\\Users\\xxx\\AppData\\Local\\Huawei\\DevEcoStudioX.X\\caches
    
    Mac: ~/Library/Caches/Huawei/DevEcoStudioX.X/caches
    
2.  Modify the network environment and try again. For example, [setting up the proxy](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-environment-config#section10369436568), connecting to a mobile hotspot, or disabling the VPN.
