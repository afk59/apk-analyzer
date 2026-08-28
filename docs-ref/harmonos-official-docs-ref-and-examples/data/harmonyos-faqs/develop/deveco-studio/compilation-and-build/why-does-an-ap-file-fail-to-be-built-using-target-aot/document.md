# Why does an .ap file fail to be built using Target AOT?

**Symptom**

An .ap file fails to be built using Target AOT and "errno: 13" is reported, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/FAdtschBSASXeG9ChSqxCA/en-us_image_0000002229758617.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4359C6B02C5A9DBE22C015E32B8ED7F76A96874FAFDB777D0EFB4D12826A3C36)

**Solution**

"errno: 13" indicates that the permission is insufficient. Resolve this issue as follows:

Open the command line tool and run the following command to disable SELinux permission control.

hdc shell
setenforce 0

The preceding settings will be invalid after a restart. If the device is restarted, perform the above settings again.
