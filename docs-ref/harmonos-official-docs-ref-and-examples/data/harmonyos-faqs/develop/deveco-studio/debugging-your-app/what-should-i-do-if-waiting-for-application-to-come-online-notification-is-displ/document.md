# What should I do if "Waiting for application to come online notification" is displayed when debugging is started?

**Possible Causes**

-   The old process PID is used for debugging.
    
    Run the **hdc shell** command to access the device, and then run the **ps -ef|grep bundleName** command to check the number of processes corresponding to the bundle name. If there are two processes, the old process PID is used.
    
    \> hdc shell
    ps -ef|grep bundleName
    
    **Solution**
    
    Uninstall the application and restart the debugging process. If the issue persists, restart the device and start debugging again.
    
-   The application is not started.
    
    Run the **hdc track-jpid** command to check whether the application is running.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/8smkIQlpQ2-DtYtdbLC2Mw/en-us_image_0000002194158768.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D54AD1D8F1CDCAD7D1F4BDEE7EC0B4756F6B1232055E75EFA441DEDC489E423D)
    
    If the application is not listed, you can check whether the application is running as follows: Run the **hdc shell** command to access the device, and then run the **ps -ef|grep bundleName** command to check the number of processes corresponding to the bundle name.
    
    If the application is missing, it has not started. If the application exists but is not listed in the **hdc track-jpid** list, the application is not registered.
    
    Run the **hdc shell bm dump -n bundleName** command and open the **aa.txt** file to check whether the value of **debug** is true. If yes, the application is a release application. Clean the project and rebuild the debug version. If the issue persists, the application was not installed correctly. If the application is a pre-installed one, you are advised to perform an OTA update.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/933TfTjHQLeBGIgHosmUkQ/en-us_image_0000002229604145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58267C9347CDD0DD277BB54D33A8CDAF335C6C43EB6D5ADA483DFFD2D543E0DF "Click to enlarge")
    
    **build mode**: Select **<None>** or **debug** to build a debug package.
    
-   The Hvigor version is not compatible.
    
    Make sure you are using a compatible Hvigor version. Create a template project and check the version number in the **hvigor-config.json5** file located in the **hvigor** directory to ensure it matches the current version.
