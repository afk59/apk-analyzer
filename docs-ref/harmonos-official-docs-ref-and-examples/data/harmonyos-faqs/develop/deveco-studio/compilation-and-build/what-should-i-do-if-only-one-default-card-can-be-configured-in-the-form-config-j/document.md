# What should I do if "Only one default card can be configured in the form\_config.json file" is reported during compilation?

**Symptom**

DevEco Studio compilation fails. The error "Only one default card can be configured in the form\_config.json file" is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/s_08yBj-RJGKLSFxZ5mXdQ/en-us_image_0000002229758657.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FA7ABC2544FC681F2FA37BE787CCC5F1D6398C785E5B564E36CDD2BE5D75E17 "Click to enlarge")

**Possible Causes**

In DevEco Studio NEXT Developer Preview2 and later versions, the following rule is added: In the widget configuration file, **isDefault** cannot be left empty. Each UIAbility has only one default widget.

**Solution**

Go to the **module.json5** file and select the only default widget. Set **isDefault** of other widgets to **false**.
