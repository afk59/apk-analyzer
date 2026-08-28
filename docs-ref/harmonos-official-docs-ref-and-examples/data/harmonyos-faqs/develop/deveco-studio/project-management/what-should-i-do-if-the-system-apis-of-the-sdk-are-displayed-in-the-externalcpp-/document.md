# What should I do if the system APIs of the SDK are displayed in the ExternalCpp view?

**Symptom**

The ExternalCpp view displays the system APIs of the SDK.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Hv2I4Mk0RL-wQu10LtvDdQ/en-us_image_0000002194158908.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72F3D5EB7C06927BAA4334E13AC307CF0407BB3607F8CED1BD0B715A1375BEA6)

**Possible Causes**

The same project is opened in multiple DevEco Studio (including Command Line Tools) processes on the local PC and is built in daemon mode.

**Solution**

Close unnecessary DevEco Studio (including Command Line Tools) processes or use the **\--no-daemon** mode to build the project.

**Reference**

[Using the Daemon Process](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-daemon)
