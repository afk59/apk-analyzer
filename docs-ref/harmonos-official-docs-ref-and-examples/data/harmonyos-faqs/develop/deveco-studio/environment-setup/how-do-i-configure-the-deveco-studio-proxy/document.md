# How do I configure the DevEco Studio proxy?

Setting up the development environment requires that your network can directly access the Internet.

If you are using a personal or home network, no proxy configuration is needed. However, if you are in a corporate network with restrictions, you will need to configure the proxy settings for DevEco Studio.

1.  Choose **File** > **Settings** > **Appearance & Behavior** > **System Settings** > **HTTP Proxy**.
2.  Select **Manual proxy configuration** and set the HTTP proxy of DevEco Studio.
    
    -   **HTTP** parameters: If you are not sure about the settings, contact your network administrator.
        -   **Host name**: Enter the host name or IP address of the proxy server.
        -   **Port number**: Enter the port number of the proxy server.
        -   **No proxy for**: Enter the URLs or IP addresses which the PC can directly connect to without a proxy server. Use commas (,) to separate URLs and IP addresses.
    -   **Proxy authentication** parameters: Set these parameters only when the proxy server requires authentication.
        -   **Login**: Enter the username used to access the proxy server.
        -   **Password**: Enter the password used to access the proxy server.
        -   **Remember**: Select this option to remember the password.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/4Amu0GpYQLe0rs7woFk5zQ/en-us_image_0000002229603741.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22E88EAE7D41B9BF5C7745466C122B25BE16CE7868C2C7FC4FDA83E989AC3E8B)
    
3.  When you are done, click **Check connection** and enter a URL to check the network connectivity. If the message "Connection successful" is displayed, it indicates that the proxy has been set up successfully. Click **OK** to finish.
