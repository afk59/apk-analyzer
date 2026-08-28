# How Can I Replace the Certificate of My Message Receipt Server?

-   Scenario 1: Both the new and old certificates are issued by commercial CAs, or both are self-signed certificates issued by the same CA.
    
    You only need to replace the old certificate with the new one on your message receipt server, without making any modification in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
    
-   Scenario 2: The new certificate is issued by a commercial CA, but the old certificate is a self-signed certificate.
    
    You need to replace the old certificate with the new one on your message receipt server, and sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) to modify the message receipt settings accordingly. During the replacement, the message receipt service will not be interrupted.
    
    To modify the message receipt settings, perform the following steps:
    
    1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, and find and click the desired project in the project list. Then, go to **Grow** > **Push Kit** > **Settings**.
    2.  Select the app whose message receipt settings need to be modified, and click **Modify** next to **App receipt**.
    3.  On the **Select receipt** page displayed, select a message receipt whose certificate needs to be replaced and click **Modify** in the **Operation** column.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/OfUG2d42QQaAezOZbKZ0KQ/en-us_image_0000002475120837.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=822B595E985D0FA9EE1BBEA2758CDE504AE0704120A80BB4A85CACE80FAF44D7)
        
    4.  On the **Configure receipt page**, check the latest certificate information detected by the message receipt service. You do not need to modify the information.
    5.  Click **Submit** to save the information.
    6.  Click **OK** to go back to the **Settings** page.
-   Scenario 3: Both the new and old certificates are self-signed certificates but are issued by different CAs.
    
    To prevent the message receipt service from being interrupted during certificate replacement, you need to sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and set the new certificate as a backup certificate before replacing the old certificate on your message receipt server.
    
    The message receipt service will trust both the old and backup certificates within 30 days, after which the old certificate will be replaced with the backup certificate if the certificate on your message receipt server has been replaced.
    
    To set a backup certificate, perform the following steps:
    
    1.  Repeat steps [a](#li107723205182) to [c](#li0773122016181) in [scenario 2](#li616213236713) to open the **Configure receipt** page.
    2.  On the **Configure receipt** page, click **Set backup certificate** and enter information about the new certificate.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/pfmtt6RjQzyuJgdKdtaZGw/en-us_image_0000002475041041.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=044E8B54924CA37071010C2011E24F09F7EFFA0746D0E459FB4C44B76518DA98 "Click to enlarge")
        
    3.  Click **Submit** to save the information.
    4.  Click **OK** to go back to the **Settings** page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ZKdmvvkmTH-ZS7PCnqeSFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AF9BC24C9E117B1C0868B9D653C11364AB49CC2A2A8EA127082C0C165061AA2)

How to obtain the CA information of the certificate on your message receipt server?

-   If the certificate has been installed on the message receipt server and the server is accessible, you can create a new receipt configuration and enter the callback address. Then, the CA information of the current certificate will be displayed.
-   If the certificate is not installed on the message receipt server, you can obtain the certificate CA information from the certificate.

The message receipt service will store the certificate CA information, and verify the certificate CA information to ensure that message receipts are correctly sent to the configured message receipt address.
