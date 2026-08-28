# How do I install a digital certificate for initiating HTTPS requests?

**Symptom**

When using a network proxy to send HTTPS requests, you need to install the digital certificate of the website server.

**Solution**

1.  Drag and upload the certificate to the Emulator. You can view the uploaded file in the **Phone** > **Downloads** directory.
2.  The certificate can be installed in the following way:
    -   Choose **Settings** > **WLAN** > ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/GwZZxg3hTKm9RI3C5wUN0A/en-us_image_0000002395407910.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1B90D5135649DF3DF53715C25B0FEB818024EBB55E3B7E15E386A6A9A359AA2) > **Install certificates** > **CA certificates**, and select the PEM certificate to install it.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/QZcWrzW8SFK3Izj9MI79AQ/en-us_image_0000002229758177.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED3F7CAF77E64388D903FA5E0157CCAD450DC1DB82BD5F20F03B80A95B63ED7F)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/I8wjUP-MQQii0xiZnuCj5A/en-us_image_0000002194317924.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=149455A81F4DB2AFD70D4F1663C3903BE24E8C5FA3D7F9440CF1DE54EDC80F13)
        
    -   Run the following command on the CLI of the local host to open the certificate management window:
        
        hdc shell aa start -a MainAbility -b com.ohos.certmanager
        
        Select **Install from storage** and choose the PEM certificate for installation.
