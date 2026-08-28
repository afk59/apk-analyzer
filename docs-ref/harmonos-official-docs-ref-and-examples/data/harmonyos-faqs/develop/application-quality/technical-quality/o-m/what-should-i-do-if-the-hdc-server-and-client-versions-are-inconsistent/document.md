# What should I do if the hdc server and client versions are inconsistent?

**Symptom**

The error message "Daemon Session Handshake failed" is displayed in the **hdc.log** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/1ZDC-ZbkQdCW4Y6KBXyxzQ/en-us_image_0000002194318252.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062534Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BEC0C46C1319932195CF289B4B98E62D55B34EED9D666125DD464F431D85F0A "Click to enlarge")

**Solution**

1.  Run the following command to check whether the server version matches the client version:
    
    hdc checkserver
    
2.  Run the following command to stop servers of other versions:
    
    hdc kill
