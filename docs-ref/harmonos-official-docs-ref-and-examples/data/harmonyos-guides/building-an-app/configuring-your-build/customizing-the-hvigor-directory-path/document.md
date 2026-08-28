# Customizing the .hvigor Directory Path

By default, the **.hvigor** directory is located in the user directory, with specific paths depending on the operating system:

-   Windows: C:\\Users\\username\\.hvigor
-   macOS: /Users/username/.hvigor
-   Linux:
    -   root user: /root/.hvigor
    -   Non-root user: /home/username/.hvigor

If the disk space in the default directory is insufficient, you can customize the **.hvigor** directory path by following these steps:

-   Setting environment variables in Windows:
    
    Add the absolute path to the .hvigor directory under system or user variables.
    
    Variable name: **HVIGOR\_USER\_HOME**
    
    Variable value: absolute path where you want to store the **.hvigor** directory, for example, **D:\\HvigorUserHome**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jj_33GmtRw2GYKD5G90dIQ/en-us_image_0000002500910090.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE809246B7D9A912B112847F48A7EF32A94C11571D2F97C7F56CD82F3A0D2F92)
    
-   Setting environment variables in macOS:
    
    To set environment variables for DevEco Studio on macOS, you can use **launchd**.
    
    -   Temporary setting method:
        
        Execute the **launchctl setenv** command in the terminal and restart DevEco Studio to apply the changes.
        
        launchctl setenv HVIGOR\_USER\_HOME /Users/xx #Replace with the absolute path for the .hvigor directory
        
        Note that this setting will be lost after restarting your computer.
        
    -   Permanent setting method:
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/y4PK_ilqTnybik4bRQiAgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A361CACC09796CCAE82DF7FA9B28C300DB2965BA2D221924C86C1FF3302DAAC4)
        
        The method to set system variables on macOS can vary depending on the system version. The following is just one example. Adjust according to your specific system version.
        
        Add the following line to **/etc/launchd.conf** (if the file does not exist, you can create it yourself).
        
        setenv HVIGOR\_USER\_HOME /Users/xx #Replace with the absolute path for the .hvigor directory
        
        After making this change, restart your computer for the setting to take effect.
        
    
-   Setting environment variables on Linux:
    
    Start the terminal tool and run the following command:
    
    vim ~/.bashrc
    
    Add the **HVIGOR\_USER\_HOME** environment variable:
    
    export HVIGOR\_USER\_HOME=/home/xx  #Replace with the absolute path for the .hvigor directory
    
    Save and close the file, then reload the .bashrc configuration file with the **source** command:
    
    source ~/.bashrc
