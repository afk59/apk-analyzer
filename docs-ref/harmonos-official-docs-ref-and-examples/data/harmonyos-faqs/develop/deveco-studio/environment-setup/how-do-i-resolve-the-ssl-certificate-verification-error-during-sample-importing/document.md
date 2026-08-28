# How do I resolve the SSL certificate verification error during sample importing?

**Symptom**

During sample importing, the error message "SSL certificate problem: unable to get local issuer certificate" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/V7qDvjYxTROa3jL63fMmIg/en-us_image_0000002194318052.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5A0970C699532E6C39BC53EC89671125732C62185263BFAF430C0F1E400B89E)

**Solution**

This issue occurs when your network is being attacked or your network provider's policy blocks related operations. If you confirm that the network environment is secure, you can temporarily disable certificate verification.

1.  Go to the Git installation directory, which is **C:\\Program Files\\Git** by default, and double-click the **git-cmd.exe** file.
2.  In the displayed CLI, disable SSL certificate verification.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/EIL8Rdb-S-ui2jGBymQo0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BC108EE703E1F02AEAE901F1DC095E066B0C78E7A084488D5F190F3F51A2F1E)
    
    Disabling SSL certificate verification may bring security risks. Enable it back once the sample importing is complete. To enable certificate verification, change **false** to **true**.
    
    git config --global http.sslVerify false
    
3.  When you are done, try again to import the sample.
