# What should I do if the connection to Gitee timed out during sample importing?

**Symptom**

During sample importing, the error message "Failed to connect to gitee.com port 443: Time out" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/jLtsCCQxQ2iz2bUKfisN4A/en-us_image_0000002229758801.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F540655A93CF36FD160D3578340E0340F282977F4A16B1CFDB88944D2F698306)

**Solution**

Check the network connection. If the network is restricted, you need to access the network through a proxy server. Perform the following steps to configure the Git proxy information:

1.  Go to the Git installation directory, which is **C:\\\\Program Files\\\\Git** by default, and double-click the **git-cmd.exe** file.
2.  In the displayed CLI, run the following command to configure the proxy, replacing **proxyUsername**, **proxyPassword**, **proxyServer**, and **port** with the actual proxy information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-P7qOIKzTZux9ujNJ0HYvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80FA0DEE2936C5006F0C0C7A0DD1165FF2A92AA303320D14204EB94EE4F00289)
    
    If the password contains special characters, such as at signs (@), number signs (#), and asterisks (\*), the settings may not take effect. As such, you are advised to replace the special characters with ASCII codes and add a percent sign (%) before the ASCII codes. Refer to the following for the mapping between common symbols and ASCII codes:
    
    -   !: %21
    -   @: %40
    -   #: %23
    -   $: %24
    -   &: %26
    -   \*: %2A
    
    git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
    
3.  When you are done, try again to import the sample.
