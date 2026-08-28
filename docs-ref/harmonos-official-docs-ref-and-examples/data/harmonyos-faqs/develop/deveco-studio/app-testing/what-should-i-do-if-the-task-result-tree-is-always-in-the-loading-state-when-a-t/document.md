# What should I do if the task result tree is always in the loading state when a test case is run?

**Symptom**

If multiple modules (for example, the entry and feature modules) depend on the HSP module, the task result tree remains stuck in the loading state after you run the entry and HSP modules on the device, followed by running the test cases of the feature module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ersHYUkFS96th604ZRPWkQ/en-us_image_0000002229758525.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAE9CE0907BC55B2598AE087E860D8960B45F396689F53F58883A58277173294)

**Solution**

1.  Open the **ohosTest/ets/testrunner/OpenHarmonyTestRunner.ts** file in a non-entry module.
2.  Add the **moduleName** field to **lMonitor** and **want** respectively. This field is used to specify the name of the current module, that is, the value of **name** for the **module** field in the **module.json5** file. The sample code snippet is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/xxPjFtE-RHChjWxMoVEk0w/en-us_image_0000002194158652.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A4F4A75D42548BBF746B29B41303E84B9039DA36E553E895B6736E9FAFCAA45)
