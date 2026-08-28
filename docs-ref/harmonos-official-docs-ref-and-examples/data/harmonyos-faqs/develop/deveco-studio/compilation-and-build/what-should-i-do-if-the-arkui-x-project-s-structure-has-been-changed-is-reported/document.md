# What should I do if "The ArkUI-X project's structure has been changed" is reported?

**Symptom**

When DevEco Studio 4.0.0.700 or later version is used to synchronize or build a historical ArkUI-X project, "ERROR: The ArkUI-X project's structure has been changed. Migrate and adapt the project as instructed in FAQs." is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/5oq_KYgVT_aPK_Zi8naSLw/en-us_image_0000002194158592.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B19C496F5996F13BB2FBC21ED025BFD76D6B8060752FD0ACEA9F156048A021BC)

**Solution**

In the ArkUI-X project template of an earlier version, the ArkUI-X project identifier (**"crossplatform": true**) is configured in the **build-profile.json5** file in the project directory, while in DevEco Studio 4.0.0.700 or later version, you need to configure the ArkUI-X project module and project ID in the **.arkui-x/arkui-x-config.json5** file in the project directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/BeViS72aQ62G8M2Kl5Xy2Q/en-us_image_0000002229758465.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE1C7B808834ACDE0CBE54A97853C6D40034F7E5B347D577E466C8F450F51629)

Due to the change of configuration location, if you use DevEco Studio 4.0.0.700 or a later version, you need to manually migrate and adapt the historical project template to the new project structure. The migration procedure is as follows:

1.  Delete the ArkUI-X project identifier (**"crossplatform": true**) from **build-profile.json5** file in the project directory.
2.  Create the **arkui-x-config.json5** file in the **.arkui-x** directory of the project and configure **"crossplatform": true** in this file. You can also configure the module names of all ArkUI-X modules in **"modules"**.
    
    The project structure after migration is as follows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nvg8Xdf_Q6Kt7v4WS3KI8g/en-us_image_0000002229758461.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B78F0CB81B039D73A2A3403DA02E5D682D816BA84E790DB96F2F924AF9509904)
    
3.  After migration, choose **File** > **Sync and Refresh Project** on the menu bar to synchronize, recompile, and build the project.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/blVOI2BcTL60zx0pWXw_-g/en-us_image_0000002229603993.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F6BEA5AF60DDE161DC0F50FE3294A9DDB4220B3BC6C0D47577ADC893A867E14)
