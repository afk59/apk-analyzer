# What should I do if "In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty" is reported during compilation?

**Symptom**

If the value of **updateEnabled** is **true** in the **form\_config.json** file, the **updateDuration** and **scheduleUpdateTime** fields cannot be empty at the same time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/0doLE4OjR7WaKHkhawt5bg/en-us_image_0000002229758573.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AF6AE41BC8B47A2CAF072122604E4D890B2BEDBBD2913667BC22E69417E0E09 "Click to enlarge")

**Possible Causes**

In DevEco Studio NEXT Developer Preview2 and later versions, the following rule applies: The widget configuration file must contain **updateEnabled**. If **updateEnabled** is set to **true**, you can choose to update the widget at a specified interval (**updateDuration**) or at the scheduled time (**scheduledUpdateTime**). If both of them are set, **updateDuration** takes precedence.

**Solution**

Go to the **module.json5** file and set **updateEnabled** to **false**, or set **updateDuration** and **scheduledUpdateTime** as required.
