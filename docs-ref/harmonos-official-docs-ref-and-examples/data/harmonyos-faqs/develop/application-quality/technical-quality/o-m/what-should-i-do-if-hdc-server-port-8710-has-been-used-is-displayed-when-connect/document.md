# What should I do if "hdc server port 8710 has been used" is displayed when connecting a phone to the computer?

-   Method 1: Stop the application that occupies the port.
    1.  Run the command line tool and enter **netstat -ano | findstr _Port number_** to query the process ID (PID) that occupies the port number.
    2.  Open **Task Manager**, click the **Details** tab, and locate the application based on the PID.
    3.  Stop the application and restart DevEco Studio.
-   Method 2: Set other environment variables for the hdc port number.
    1.  Set environment variables in Windows:
        
        Choose **This PC** > **Properties** > **Advanced system settings** > **Advances** > **Environment Variables**, add the variable _OHOS\_HDC\_SERVER\_PORT_, and set its value to any port number not in use.
        
    2.  Set environment variables in macOS:
        
        a. Start the terminal tool and run the **echo $SHELL** command. Based on the command output, run the following commands:
        
        If the output is **/bin/bash**, run the **vi ~/.bash\_profile** command to open the **.bash\_profile** file.
        
        If the output is **/bin/zsh**, run the **vi ~/.zshrc** command to open the **.zshrc** file.
        
        b. Press **i** to enter **Insert** mode.
        
        c. In the following content to add **OHOS\_HDC\_SERVER\_PORT** information to **PATH**.
        
        OHOS\_HDC\_SERVER\_PORT= port number
        launchctl setenv OHOS\_HDC\_SERVER\_PORT $OHOS\_HDC\_SERVER\_PORT
        export OHOS\_HDC\_SERVER\_PORT
        
        d. Press **Esc** to exit the edit mode, and then input **:wq** and press **Enter** to save the settings and exit.
        
        e. Run the following command for the environment variable to take effect.
        
        If the **.bash\_profile** file is opened in step 1, run the **source ~/.bash\_profile** command.
        
        If the **.zshrc** file is opened in step 1, run the **source ~/.zshrc** command.
        
        f. Restart DevEco Studio.
