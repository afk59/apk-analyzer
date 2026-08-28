# What should I do if "Failed connect to unix-abstract-connect" is displayed when C++ debugging is started?

**Symptom**

The error message "Failed to connect to unix-abstract-connect://\\\*\\\*\\\*\\\*\\\*\\\*\\\*\\\*\\\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet" is displayed when C++ debugging is started.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/MlQK9bVLRfm6WZXoP7fzPg/en-us_image_0000002194158920.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89651B151556BD4E676E519EB62CF6A5D0E05CB4FD92EE4DBA3B843FE53A4AB8)

**Solution**

1.  Make sure the device image version matches the DevEco Studio version.
2.  If a release certificate is used for signing, switch to a debug certificate and perform signing again.
3.  Go to **/data/local/tmp/debugserver/** and delete the folder with the same name as the application package.
