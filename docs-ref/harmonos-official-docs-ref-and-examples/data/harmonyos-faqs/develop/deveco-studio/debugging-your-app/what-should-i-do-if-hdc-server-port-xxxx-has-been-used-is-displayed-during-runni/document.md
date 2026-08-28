# What should I do if "Hdc server port XXXX has been used" is displayed during running the HAP?

**Symptom**

When the HAP is running in the device, the error message "Hdc server port XXXX has been used. Configure environment variable 'OHOS\_HDC\_SERVER\_PORT' and restart DevEco Studio." is displayed.

**Solution**

This issue occurs because the default HDC port (8710) is being used by another process, preventing the service from starting. To resolve this issue:

Method 1: Stop the application that occupies the port.

1.  Run the command line tool and enter **netstat -ano | findstr _Port number_** to query the process ID (PID) that occupies the port number.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/AFZuA2BoSn-red9ngYwmcQ/en-us_image_0000002229604025.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CE6CE46841FFF7245E1296909B952DBA1A41018E48A332B75BBB2497DDF2CD6 "Click to enlarge")
    
2.  Open **Task Manager**, click the **Details** tab, and locate the application based on the PID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/mvRjihX_Rb-bbSJpxTVBbA/en-us_image_0000002229758501.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34F26BA700EAF565F04EA23B1A9FBE5B3C7F87C49EAE484663B5247D86136C3A "Click to enlarge")
    
3.  Stop the application and restart DevEco Studio.

Method 2: Set other environment variables for the hdc port number.

-   Setting environment variables in Windows:
    
    Choose **This PC** > **Properties** > **Advanced system settings** > **Advances** > **Environment Variables**, add the variable **OHOS\_HDC\_SERVER\_PORT**, and set its value to any port number not in use, such as **7035**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/L2moFNvDTbeAwcGEkGU4Pw/en-us_image_0000002229604017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4337107BC072FA072FA2FB58CC7F2F42F49968AD3F8621CBF8B547334ED070AA "Click to enlarge")
    
    Then restart DevEco Studio.
    
-   Setting environment variables in macOS:
    1.  Start the terminal and run the following command:
        
        echo $SHELL 
        
        -   If the command output is **/bin/bash**, open the **.bash\_profile** file.
            
            vi ~/.bash\_profile
            
        -   If the command output is **/bin/zsh**, open the **.zshrc** file.
            
            vi ~/.zshrc
            
    2.  Press **i** to enter Insert mode.
    3.  Enter the following content to add **OHOS\_HDC\_SERVER\_PORT** information to **PATH**.
        
        OHOS\_HDC\_SERVER\_PORT=7035
        launchctl setenv OHOS\_HDC\_SERVER\_PORT $OHOS\_HDC\_SERVER\_PORT
        export OHOS\_HDC\_SERVER\_PORT
        
    4.  Press **Esc** to exit the edit mode, enter **:wq**, and press **Enter** to save the settings.
    5.  Run the command for the environment variable to take effect.
        -   If the **.bash\_profile** file is opened in [1](#en-us_topic_0000001166752005_li1264071053012), run the following command:
            
            source ~/.bash\_profile
            
        -   If the **.zshrc** file is opened in [1](#en-us_topic_0000001166752005_li1264071053012), run the following command:
            
            source ~/.zshrc
            
    6.  Then restart DevEco Studio.

Method 3: If the port is not occupied, check whether the port is blocked by the firewall. If it is, unblock the port and then restart DevEco Studio to try again.
