# What should I do if the error message "Node service error detected.Reinstall DevEco Studio to fix the error." is displayed during the Previewer startup?

**Symptom**

The attempt to launch the Previewer triggers the following error message in the PreviewerLog window: "Node service error detected.Reinstall DevEco Studio to fix the error."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/DbLefShTQHSof8jOpdXQ9g/en-us_image_0000002194318348.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3A83D4523145EE495E3E02353898B44ED0B33933D00267644EA7C5FF02BC240 "Click to enlarge")

**Solution**

-   Solution 1: The built-in files of DevEco Studio may be damaged. Reinstall DevEco Studio.
-   Solution 2: Make sure there is the **127.0.0.1 localhost** configuration in the **hosts** file, whose path varies by platform:
    
    -   Windows: **C:\\Windows\\System32\\drivers\\etc\\hosts**
    -   macOS: **/private/etc/hosts**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/F-4_ZSxvSnyawjBRnyNFUw/en-us_image_0000002229758609.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CE6D1CA1519579E7F64E74F3F8E10B3C7886E4E682E5DA864B14DE078F3C227 "Click to enlarge")
    
-   Solution 3: Restart the WinNAT service on Windows.
    
    Open the CLI or PowerShell as an administrator and run the following commands:
    
    1.  Stop WinNAT.
        
        net stop winnat
        
    2.  Start WinNAT.
        
        net start winnat
