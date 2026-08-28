# What should I do if "Schema validate failed" is reported?

**Symptom**

During project synchronization or compilation and build, the error "Schema validate failed" is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Nw63YU0KSIilxeUxG0bzMA/en-us_image_0000002229604277.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=441E521C629B0B7CEFA160A98A326E29A68CCF899DBDBAE19DE1C2A06B936747)

**Solution**

During development, after a project is created, the startup window is automatically set by default. If a field is deleted by mistake, an error will be reported. To improve the cold start performance of an application or service during development, you can set the icon and background color of the startup window as follows:

1.  Right-click **resources** > **base** > **element** and choose **New** > **Element Resource File** from the shortcut menu to create a resource file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/QiRPt7rYTNu1Tz0cK_-zTA/en-us_image_0000002194318512.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58F396F06119F46139AB1A61D9A1B793D11C6C22BA3F76E8171AD60F86DE2686)
    
2.  In the dialog box that is displayed, you can set **File name**, for example, **color**, and set **Root element** to **color**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/PIFJcu2mRO2tLxrNQrhtGw/en-us_image_0000002194158900.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B939F3E6722B9F9169C708D1586B6F22AED20613C81AB83DDBDAF4CC75157E4)
    
    After creating, the **color.json** file is shown as below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/3b792ML9Rg-iyAxZgGpsIw/en-us_image_0000002194318508.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F6912A7526426E7C64B282187B142177F694A954ADFA72333A44B11CE18C4BF)
    
3.  Copy the **color.json** file created in [2](#en-us_topic_0000001233028585_li124901748185712) to the **ohosTest** \> **resources** \> **base** \> **element** directory of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/KJohsSh6QKyomYrjIZRsCg/en-us_image_0000002229604281.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24EAFF98B0D7D284B5D24E5DD763E7A2995DB1A2F930915DFED31DDE2214DD62)
    
4.  Add the **startWindowIcon** and **startWindowBackground** fields to the **abilities** array in the **src** > **main** > **module.json5** file of the module. If any field is missing, the error "ERROR: Schema validate failed" is reported. The **startWindowIcon** field is used to index the icon resource in **resources** > **base** > **media** of the module, and the **startWindowBackground** field is used to index the color in **resources** > **base** > **element** > **color.json**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/nyGQg1WWQl-cHrT79KHzFA/en-us_image_0000002194318504.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B722F973816B6814C0FA0958CFFB001C9B0A7B250E8096F21920092A26146C5)
    
5.  Add the **startWindowIcon** and **startWindowBackground** fields to the **abilities** array in the **src** > **ohosTest** > **module.json5** file. The **startWindowIcon** field is used to index the icon resource in **resources** \> **base** \> **media** of module **ohosTest**, and the **startWindowBackground** field is used to index the color in **resources** \> **base** \> **element** > **color.json** file.
