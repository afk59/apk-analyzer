# How do I resolve the "Invalid form name 'xxx'." error?

**Symptom**

The widget name is invalid.

**Possible Causes**

When the intent framework is configured in the **insight\_intent.json** file, **formName** must be one of the **forms** section configured in the **form\_config.json** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/boDpX8BATDGhjgBPdc9TpA/en-us_image_0000002194158436.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C9E3CCB9D763616CC343FDB1986171F47C9481C075CDA04B6ABD66AC7F715F1 "Click to enlarge")

**Solution**

Make sure the value of **formName** in the **insight\_intent.json** file is listed under the **forms** section in the **form\_config.json** file.
