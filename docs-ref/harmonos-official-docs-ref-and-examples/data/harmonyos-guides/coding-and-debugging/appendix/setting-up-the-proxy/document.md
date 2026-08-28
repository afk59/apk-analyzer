# Setting Up the Proxy

The DevEco Studio development environment relies on an Internet connection to ensure the tools function properly.

Generally, if you are using a personal or home network, you do not need to configure proxy information. Proxy configuration is only necessary when you are on an enterprise network that has specific restrictions.

#### Diagnosing the Development Environment

To get the most out of DevEco Studio, run a diagnostic test on your development environment and fix the failed items based on the provided suggestions. To start a diagnostic test, click **Diagnose** on the welcome page or choose **Help** > **Diagnostic Tools** > **Diagnose Development Environment** from the menu bar on the project page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/2W9a-0gyShmDx6hM5qETxg/en-us_image_0000002501069920.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04D1224E29E278E77B42EA6E9EF100330311CA8254DEC98B9A705B518AA39DF2)

The diagnosis items include the computer configuration and network connectivity. Fix the failed items, if any, based on the provided suggestions.

#### Setting Up the Proxy

1.  On the welcome page, choose **Customize** > **All settings...** > **Appearance & Behavior** > **System Settings** > **HTTP Proxy**. If a project has been opened, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Appearance & Behavior** > **System Settings** > **HTTP Proxy** to access the HTTP Proxy settings page.
    
    -   **HTTP** parameters: **If you are not sure about the information, contact your network administrator.**
        -   **Host name**: Enter the host name or IP address of the proxy server.
        -   **Port number**: Enter the port number of the proxy server.
        -   **No proxy for**: Enter the URLs or IP addresses to which your computer can directly connect without a proxy server. Use commas (,) to separate URLs and IP addresses.
    -   **Proxy authentication** parameters: Set the parameters only when the proxy server requires authentication.
        -   **Login**: Enter the username used to access the proxy server.
        -   **Password**: Enter the password used to access the proxy server.
        -   **Remember**: Select this option to remember the password.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/L0K_4Wz7RxirIvuPnGb7gA/en-us_image_0000002532670005.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04ED352F06E6D25EF46D3FC40B4F49BA754EEF8C8C5E0B0E4985D7D060471FDB)
    
2.  When you have finished, click **Check connection** and enter a URL (for example, **https://developer.huawei.com**) to check the network connectivity. If the message "Connection successful" is displayed, it indicates that the proxy has been set up successfully.

#### Setting Up the npm Proxy

During initialization, hvigor and ohpm need to download dependencies from the npm repository. If a proxy is required to access the network, configure the npm proxy as follows.

1.  Go to the **C:\\Users\\_username_** directory and open the .npmrc file. If no .npmrc file is in the directory, create one.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/RDuHUSM7SyCQcYe7KhjvWg/en-us_image_0000002532670003.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07324B4F50DE02A1FD9561CCDC5EDE19C5E0464F7E1D9E129485203AF76C8F17)
    
2.  Modify the npm repository information. The following is an example:
    
    registry=https://repo.huaweicloud.com/repository/npm/
    @ohos:registry=https://repo.harmonyos.com/npm/
    
3.  Modify the proxy information. In **proxy** and **https-proxy**, change the values of **user**, **password**, **proxyserver**, and **port** based on the actual proxy server. **If you are not sure about the information, contact your network administrator.** The following is an example:
    
    proxy=http://_user_:_password_**@**proxy._proxyserver_.com:_port_
    https-proxy=http://_user_:_password_**@**proxy._proxyserver_.com:_port_
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/sZxY9BpUTyWwPGbUuqo3mA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE1131DB4B74F3AC9E0F8D414721AD144666B9203A318685AB17425495731FA1)
    
    If the password contains special characters, such as @, #, and \*, the configuration may not take effect. As such, you are advised to replace the special characters with ASCII codes and add a percent sign (%) before the ASCII codes. Refer to the following for the mapping between common symbols and ASCII codes:
    
    -   !: %21
    -   @: %40
    -   #: %23
    -   $: %24
    -   &: %26
    -   \*: %2A
    
4.  Add Node.js to environment variables.
    
    -   On Windows:
        
        Add the Node.js installation path, which is **$_DevEco Studio installation directory_\\tools\\node** by default, to **Path** under system or user variables.
        
    -   On macOS:
        
        Start the terminal tool and run the following command:
        
        export NODE\_HOME=/home/xx/Downloads/node-vxx.xx.x-linux-x64  # Replace the path here with the Node.js installation path, which is $DevEco Studio installation directory\\tools\\node by default.
        export PATH=$NODE\_HOME/bin:$PATH
        
    
5.  After the proxy is configured, open the CLI and run the following command to check whether the network is normal.
    
    npm info express
    
    If the following information is displayed after running the command, it indicates that the proxy has been set up successfully.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/PxraqnVmRmOVDvFJVOR7Og/en-us_image_0000002532749953.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ECA0E934D4BD2B5BA38CEECB2F35DB43BBA2AC9AF742CD08B8355FADBC741F7)
    

#### Setting Up the ohpm Proxy

To access the ohpm proxy configuration:

-   On the welcome page, choose **Customize** > **All settings...** > **Build, Execution, Deployment** > **Ohpm** > **Optimize config**.
-   If a project has been opened, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Ohpm** > **Optimize config** to access the ohpm proxy configuration page.

Set the following fields:

-   **ohpm registry**: address of the ohpm repository.
    
    https://ohpm.openharmony.cn/ohpm/
    

-   **HTTP proxy**: proxy server information. By default, the value is the same as that of **HTTP proxy** of DevEco Studio. **If you are not sure about the information, contact your network administrator.** If your proxy server requires the username and password for authentication, set them as follows:
    
    http://_u__se__r_:_password_@proxy._proxyserver_.com
    
-   **Enable HTTPS proxy**: whether to enable the HTTPS proxy.

After you select and set the preceding fields, click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/rPTb7CDqTEWsq-s97buv7Q/en-us_image_0000002500910086.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD3E814B5DD8B9E1AE4D23C425554C6FBFF7C9FED76076E4561B76569F28F045)

Note: By default, ohpm verifies the registry address certificate. If a certificate verification error such as "SELF\_SIGNED\_CERT\_IN\_CHAIN" or "UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE" is displayed for ohpm registry access during environment diagnosis, see [FAQ – Symptom 2](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-development-environment-10) for troubleshooting.

The settings configured on this page are written into the **.ohpmrc** file in the **users/_username_/.ohpmrc** directory. This means that you can also configure the ohpm settings from this file. To do so:

1.  Go to the **C:/Users/_username_/.ohpmrc** directory and open the .ohpmrc file. If no .ohpmrc file is in the directory, create one.
2.  Modify the ohpmrc repository information. The following is an example:
    
    registry=https://ohpm.openharmony.cn/ohpm/
    
3.  Modify the proxy information. In **http\_proxy** and **https\_proxy**, change the values of **user**, **password**, **proxyserver**, and **port** based on the actual proxy server. The following is an example:
    
    http\_proxy=http://_user_:_password_@proxy._proxyserver_.com:_port_
    https\_proxy=http://_user_:_password_@proxy._proxyserver_.com:_port_
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ts3Q6FtlQWe8pQJyP5XUJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C81B5E40F7E82A15DECD977967BAA19F0B8A2B641EBBE8F7C9F1DB059B36BF12)
    
    If the password contains special characters, such as @, #, and \*, the configuration may not take effect. As such, you are advised to replace the special characters with ASCII codes and add "%" before the ASCII codes. Refer to the following for the mapping between common symbols and ASCII codes:
    
    -   !: %21
    -   @: %40
    -   #: %23
    -   $: %24
    -   &: %26
    -   \*: %2A
    
4.  Add ohpm to environment variables.
    
    -   For Windows:
        
        Choose **This PC** > **Properties** > **Advanced System Settings** > **Advanced** > **Environment Variables**, and add the **bin** folder path in the ohpm installation path to the **Path** environment variable under system or user variables. The default path is **_DevEco Studio installation directory_\\tools\\ohpm**.
        
    -   For macOS:
        
        Start the terminal tool and run the following command:
        
        export OHPM\_HOME=/home/xx/Downloads/ohpm  # Replace the path here with the ohpm installation path, which is /home/xx/Downloads/DevEco Studio installation directory\\tools\\ohpm by default.
        export PATH=$OHPM\_HOME/bin:$PATH
        
    
5.  After the proxy is configured, run the following command to check whether the network connectivity is normal.
    
    ohpm info @ohos/lottie
    
    If the following information is displayed after running the command, it indicates that the proxy has been set up successfully.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/zYfa4j80TKag-3rBj1cArQ/en-us_image_0000002532749957.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BDB6590DFBD23A0732777F2F34CFD1A2C0EA8F0008DE8C62FCA06455FA9A75A)
