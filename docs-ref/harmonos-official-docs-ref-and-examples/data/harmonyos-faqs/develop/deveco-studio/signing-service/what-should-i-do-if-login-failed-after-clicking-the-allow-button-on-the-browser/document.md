# What should I do if login failed after clicking the Allow button on the browser?

**Symptom**

After you log in with a HUAWEI ID that has passed real-name authentication and click **Allow** to grant required permissions, the error message shown below is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/h_l9ydA3THWAyu-3vOLxhA/en-us_image_0000002229604393.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0840DA2F1795FA7D5A047F449627071ECFFD5AC781F50B95160243BEFE97405A "Click to enlarge")

**Solution**

This issue may be caused by the HTTP proxy settings of DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/wCaN4o0nR1qdnfL2WTvn1g/en-us_image_0000002194318608.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=874595D8F56B0F9A72BD46FD0C3CEAFA8660BFEE852E7DE285390D82D25BDFE6 "Click to enlarge")

1.  Check the HTTP proxy settings.
    
    -   If the network can access the Internet without a proxy, setting a proxy will affect the login authorization of the Emulator. In this case, set **HTTP Proxy** to **No proxy**.
    -   If your network requires a proxy to access the Internet, set **HTTP Proxy** to **Manual proxy configuration**. For details, see [Setting Up the Proxy](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-environment-config#section10369436568).
    
2.  On the DevEco Studio page, click **Cancel** and perform login authorization again.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/ffiZpqvBS9CH5e5FuSh6DQ/en-us_image_0000002229758881.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39498ED06B443197405F285DEE6080511FA6F12290077B95A0A63B855FBF6CD8)
