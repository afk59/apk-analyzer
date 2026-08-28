# What should I do if ohpm registry access fails in the environment check?

Troubleshoot based on the symptom:

**Symptom 1**

The registry address fails to be verified, and the message "check whether the ohpm repository is correctly set" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/2dAyxrPEReScFaXtaAfkrA/en-us_image_0000002324320444.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9951BD91468A299D601ADDD76CB308289DA61FA8D5AADFACE52B265B22E482CC)

**Solution**

-   **Scenario 1**: The registry may be incorrectly configured. Click **Click here** to verify the registry configuration or configure a new registry address.
-   **Scenario 2**: The network may be disconnected, and you need to configure a proxy to access the Internet using either of the following methods:
    
    Method 1: Click **Click here** to go to the proxy configuration page and configure the HTTP proxy.
    
    Method 2: Open the .ohpmrc file in **C:\\users\\_username_\\.ohpm** and modify the **http\_proxy** or **https\_proxy** configuration item. If the .ohpmrc file does not exist, create one.
    
    If your proxy server requires the user name and password for authentication, set them as follows.
    
    1.  Go to the **C:\\Users\\_username_\\.ohpm** directory and open the .ohpmrc file. If no .ohpmrc file is in the directory, create one.
    2.  Modify the ohpm proxy information. Add the **user** and **password** fields to **http\_proxy** and **https\_proxy**. Note that the values may vary depending on the proxy. Perform the following steps:
        
        http\_proxy=http://**u****se****r:password@**proxy.server.com:80
        https\_proxy=http://**user:password@**proxy.server.com:80
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/x-e1TKKPTRmMLHLmxtDO_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2082103C7C8C00427BEAD1373F38AFC573408F4199EA1EA15A7F9C54CB07BC7)
        
        1.  If the password contains special characters, such as @, #, and \*, the configuration may not take effect. In this case, you are advised to replace the special characters with ASCII codes and add a percent sign (%) before the ASCII codes. Refer to the following for the mapping between common symbols and ASCII codes:
        
        -   !: %21
        -   @: %40
        -   #: %23
        -   $: %24
        -   &: %26
        -   \*: %2A
        
    3.  After the proxy is configured, open the CLI and run the following command to check whether the network connectivity is normal.
        
        ohpm info @ohos/lottie
        
        If the information similar to the following is displayed, it indicates that the proxy has been set up successfully.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/WgJ9w8dfQWai5f6GBWsdsg/en-us_image_0000002358358913.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2D2B918729EC5A9698D03D628C4A3FDAAAB8C7EC41711F9104F8F0FE3451DD5)
        

**Symptom 2**

The registry certificate address verification fails, with the message "UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE" displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/qZisitnPTkuYhrlhqyVKvw/en-us_image_0000002358279041.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECD9724C4D3CF0B85D6FF71F895624A3BD5FC40C0D6C1AF5B755DC07F83F0465)

**Solution**

Perform the following:

Go to the **C:\\Users\\_username_\\.ohpm** directory and open the .ohpmrc file. If no .ohpmrc file is in the directory, create one.

-   Configure the URL of the registry certificate in the **ca\_files** field. Use commas (,) to separate URLs.
    
    ca\_files=your\_ca\_files\_path
    
-   Alternatively, set **strict\_ssl** to **false** to temporarily disable certificate verification.
    
    strict\_ssl=false
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/0Uu9y-9pRuOkC5p2f-gfLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EA41FF157D1C4AA86300E87C0E327D81470CB44F58B55E1F91FB16652E2B09F)
    
    Disabling certificate verification may bring security risks. Confirm the risks associated with disabling certificate verification before modifying the configuration. You are advised to enable certificate verification back promptly after use, by changing **false** to **true**.
