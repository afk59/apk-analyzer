# How Do I Fix the Error of an Incomplete Certificate Chain?

If your certificate does not match anyone in the built-in trust store of IAP Kit, it will not be trusted by IAP Kit. In this case, you need to create a complete certificate chain.

The following procedure will use Google Chrome, which generally auto-validates certificate chains, to create a complete certificate chain.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/_e6n8wKtQteEWZBlVjn1Ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E53B560C24FAFAC9D14FBE4AF47075AA90EE95CFFC33254C5D1D944634DED07)

You can also use other tools to do this as you prefer.

1.  View the server certificate.
    
    Visit the [HUAWEI Developers](https://developer.huawei.com/consumer/en/) website, click the icon for viewing website information in the address box, click **Connection is secure**, and click the icon for showing certificate information. In the window that is displayed, click the **Details** tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/9gnr7U7yQo6Qlxe1EKLsUw/en-us_image_0000002446733489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29FEC1883C62E3BF1561837A9AE6D75370B67AFAD808FBFEF861EEA2FF6D20AA "Click to enlarge")
    
2.  Export the server certificate chain as a file.
    
    Click the server certificate and click **Export**. In the **Save As** window, set **Save as type** to **Base64-encoded ASCII, certificate chain (\*.pem;\*.crt)** and click **Save**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/AbMHajzhR-Ob_POCJAye7g/en-us_image_0000002446613573.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D5292FB743031761102E9C7939D05E85BF34C189BE469D2A7DAC998792F17FB "Click to enlarge")
    
3.  Use a text editor to open the exported certificate chain file in .crt format. You will see the certificate content (server certificate, intermediate certificate, and root certificate from top to bottom) in PEM format, which is similar to that shown in the following figure. Then, send the certificate chain file to the IAP server.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/u13ODVjHSpOq0xzH6hzvRg/en-us_image_0000002446613569.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7226871113A8607991FDA5FDDE73035A4560CED2A0FF8DF898024EB57FC13BF "Click to enlarge")
