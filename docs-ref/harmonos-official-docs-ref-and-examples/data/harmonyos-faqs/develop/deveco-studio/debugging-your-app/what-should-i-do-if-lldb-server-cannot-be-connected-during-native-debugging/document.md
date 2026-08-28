# What should I do if lldb-server cannot be connected during native debugging?

**Symptom**: Native debugging is not started for a long time, and the error message "Attach request timeout after 600000 milliseconds " is displayed after DevEco Studio times out, or the error message "Failed to connect port" is displayed after native debugging is started.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/A8nwc7YiRualizzjIb2jfQ/en-us_image_0000002229758601.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF922D03AE42952C700B52249A865F8619AF936653165E4C4D5F9C0B63982AF0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/lNDCpr6PS2e_d_Dw41HyaQ/en-us_image_0000002194318340.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07266FB8CC4BB01470A6D02BF167469270E6CA73F6AAFA8AE5C65178E4347390)

**Possible Causes**

The **/etc/hosts** file in Linux or macOS is modified.

**Solution**

1.  Add the following information to the **/etc/hosts** file:
    
    127.0.0.1 localhost
    255.255.255.255 broadcasthost
    ::1 localhost
    
2.  Restart the computer for the modification to take effect.
