# What should I do if exception occurs when I run the hdc file send command?

**Symptom**

Run the **hdc file send** command to send HAP and HSP files to the mobile phone, but these files turn into 3.4 KB folders on the phone. A parsing error is reported when the **install** command is run. Click the green triangle button in the upper right corner in DevEco Studio. After the application is built, run the **hdc file send "./entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/app/entry-default-signed.hap"** command in the root directory of the project. However, the file passed to the phone is still not a single HAP file. The directory structure is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/vhhtayMGSXGRXjvqubBu6w/en-us_image_0000002229758677.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E91174BC0709DF848DD43C2E5918673E20F8A08B9B48C05A1631B8A1E5C2E71 "Click to enlarge")

**Solution**

The path used in the command must be an absolute path (separated with back slashes) instead of a relative path (separated with forward slashes).

Copy the absolute path in DevEco Studio. Copy the path as follows:

Right-click the file to be sent and choose **Copy Path**/**Reference...** > **Absolute Path**, or press **Ctrl+Shift+C**.
