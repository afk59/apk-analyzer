# How do I start a UIAbility using the hdc command?

Run the following command to start the specified UIAbility:

hdc shell aa start -a <UIAbility Name> -b <Bundle Name>

If the ability is started, "start ability successfully." is returned; otherwise, the error message "error: failed to start ability." and the corresponding error information are returned.

Refer to the sample code below.

hdc shell aa start -a EntryAbility -b com.example.myapplication

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/JCK6txq7TJeCKk1SO6ecbQ/en-us_image_0000002229758597.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062534Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11DE5098962399EF3EED417754F643120CBC0DACACFD08727CB60F25EFD8490A "Click to enlarge")

**Reference**

[Ability Assistant](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/aa-tool)
