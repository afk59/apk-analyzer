# How do I use Charles to capture packets?

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/COgLhWh0TleJjI6C2TfYLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C18C9A5BD0101E0CA955A4A43C44621D048F522E2872A6A867ECA5987DC56F36)

1.  When Charles displays a confirmation dialog box during environment setup, click **Allow** to connect to the mobile phone.
2.  Certificates in **.crt** format are not supported. You need to convert the certificates to the **.pem** format before installation.
3.  Charles cannot capture packets of the upload and download APIs in the @ohos.request module.

Charles is a proxy tool used for network debugging and analysis, which allows you to view and debug the network communication between devices and servers. With this tool, you can monitor the network traffic of applications, modify requests and responses, and even simulate different network conditions. It provides the following functions:

-   Intercepts HTTP and HTTPS network packets.
-   Resends network requests to facilitate backend debugging.
-   Modifies network request parameters.
-   Intercepts and dynamically modifies network requests.
-   Supports simulation of low-speed networks.

When using Charles to capture packets, you need to configure a Charles client proxy to forward application requests to the server. When you start Charles, it automatically sets the browser as a proxy. Once network requests are sent through the browser, Charles directly captures network packets of the network requests and their responses.

Charles can capture HTTP requests from both PCs and applications. To implement network capturing on a mobile device, you need to [configure the Charles proxy](#li9948mcpsimp). To capture HTTPS packets, you need to [download the Charles certificate](#li17228123363716) and [install the certificate](#li47368423374).

To use Charles, perform the following steps:

1.  Install Charles.
2.  Configure the Charles proxy.
    1.  Check the IP address of Charles. Generally, the IP address is the same as the IP address of the PC.
        -   To view the IP address of Charles, choose **Help** > **Local IP Address**.
        -   To view the IP address of the PC, open the **Run** dialog box (press **Win+R** or click **Search** on the taskbar), enter **cmd**, and run **ipconfig** in the command line window.
    2.  Set the debugging port number for Charles.
        -   Choose **Proxy** > **SSL Proxy Settings**. In the **Include** area, click **Add**, and then add **:** to set **Host** and **Port** as **\*** and add **\*:443** to set **Host** as **\*** and **Port** as **443**. Click **OK**.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/NhPnzw2tQlmgPQEKzl0KmQ/en-us_image_0000002229604213.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E779BA4954A21C451468D716235B796DA621B4C5087A66AEA3D604A5C6B824FE "Click to enlarge")
            
        -   Choose **Proxy** > **Proxy Settings**. In the **HTTP Proxy** area, set **Port** to the listening port of Charles, which is **8888** by default. Select **Enable transparent HTTP proxying**. Then click **OK**.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/R_r-IyELSlun74fEljiwTw/en-us_image_0000002194318440.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AE668B891EB668360E7BAE2BC9CA862083789A059F546A2C4606B783561C2F6 "Click to enlarge")
            
    3.  Connect the mobile phone and PC to the same LAN. Enable manual proxy setup for Wi-Fi on the mobile phone, and set the host name and port of the server to the IP address and listening port of Charles.
        
        Tap the target Wi-Fi network to launch the setup screen. Select **Manual** from **Proxy**, and set the host name and port number of the proxy server to the IP address and listening port of Charles (that is, 8888). Then, enter the correct password to connect to the Wi-Fi network.
        
3.  Download the Charles certificate.
    1.  Install the Charles root certificate in a directory trusted by the PC.
        
        On the top menu bar, choose **Help** > **SSL Proxying** > **Install Charles Root Certificate** > **Install Certificate**. Set the storage location (the current user or local computer) and click **Next**. Select **Place all certificates in the following store**, click **Browse**, and set the certificate storage path to **Trusted Root Certification Authorities**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/BwBnnEfKRmW5GBDSbafRNg/en-us_image_0000002194158828.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F466DCB3AB185C15EF875B963919E1C452A0E90593468839DA71C5287795161 "Click to enlarge")
        
    2.  Import the system root certificate to the mobile phone.
        
        Method 1: On the top menu bar, choose **Help** > **SSL Proxying** > **Install Charles Root Certificate on a Mobile Device or Remote Browser**. Access **http://chls.pro/ssl ->** via the browser of the mobile phone, and click **Download Now** to download the certificate to the mobile phone memory.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/tMh1lqGfT5Csd9tvxAssWA/en-us_image_0000002229758713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9EC1C89C8338CB62D5B85E1F024CD9F51B51330698D7C23A74AFCDF69A34211 "Click to enlarge")
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/4H9xwiPmRSivtW3r4Rn7qA/en-us_image_0000002194318444.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A034CC74A7BAAA76EC1DCC60446F774465391374C1B93213FF87D6A13596567)
        
        Method 2: On the PC, choose **Help** > **SSL Proxying** > **Save Charles Root Certificate...** to save the certificate in **.pem** format to the local PC. Connect the mobile phone to the PC, and upload the PEM file to the phone through DevEco Studio (specifically, right-click the folder where the PEM file is to be uploaded, click **Upload...**, and select the PEM file).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/KCq1bR1KQh-gTTvBiL5lvw/en-us_image_0000002213656456.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2644FBD5CC9BFC689310CED95054ACCE29D3B863BD31C4DF38745B1C3B30AE9 "Click to enlarge")
        
4.  Install the certificate.
    
    To install a certificate on a mobile phone, perform the following steps:
    
    On the mobile phone, go to **Settings** > **Security** > **More settings** > **Encryption and credentials**. Select **Install from storage**, and click **CA Certificate**. When you see a warning, click **Continue**, navigate to the downloaded certificate, click the certificate to install it. The certificate is successfully installed if a success message is displayed.
    
    | 
    Selecting **Install from storage**
    
     | 
    
    Clicking **CA Certificate**
    
     |
    | :-- | :-- |
    | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/BsJsHyW_QD6aSpE8Hhr3ww/en-us_image_0000002229758705.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D7439D7797D67E8E51668C80121CAACA8C8BE36BA82224140C5EC98892CA083)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/twXcYCOyTqelNJSrMJ7vgg/en-us_image_0000002229758709.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4CB2AD699C04D744C257046EB9626D1EFEB29E49A7D607F8D1E7896F1264680)
    
     |
    
5.  Filter network requests.
    
    Generally, the tool is expected to listen only for the requests sent by the specified directory server and filter out other network requests. To meet this requirement, you can use either of the following methods:
    
    1.  On the main screen, press **Ctrl+F** to open the search box and enter the keywords to be filtered. Assume that the target address is **www.charlesproxy.com**. You only need to set the filter criteria in the **Text to find** area, select other options as needed, and click **Find**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/5PuqfDSBSzGflx7xRGdghg/en-us_image_0000002229604209.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C050DECF64F0F123E535A63260353DCF2B22E7E661DC2957BF1633113B1A255 "Click to enlarge")
        
    2.  On the menu bar of Charles, choose **Proxy** > **Recording Settings**. On the **Include** tab, click **Add** to add a project. Set the protocol information as required and start listening again. In this way, the tool listens only for network requests from the target website.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/gFwr2q81TQS3HrZx80mSQQ/en-us_image_0000002194318436.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062609Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9144C61EBC31C83F80BB360B12D63E7B592976681DA88025F0553BD291452565 "Click to enlarge")
