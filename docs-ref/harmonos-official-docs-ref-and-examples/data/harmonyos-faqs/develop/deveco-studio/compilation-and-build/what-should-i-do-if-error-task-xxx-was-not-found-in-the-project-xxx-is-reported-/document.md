# What should I do if "ERROR: Task xxx was not found in the project xxx" is reported during build?

**Symptom**

If the build fails and the error "ERROR: Task xxx was not found in the project xxx" is reported when you run the build command in the CLI. To rectify the fault, perform the following operations:

\- Check whether the task name is correct.

\- Check whether the project contains the task.

\- Check whether the project path is correct.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/3BumvWxSTZiI833tO8fbKg/en-us_image_0000002194318376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=757D916197126B45DA578D9016F588B7337B06B30F8EF18DB0FA70A99603FF7F)**Cause Analysis**

1.  Run the **hvigorw tasks** command to check whether the corresponding command exists.
2.  Check whether the **type** field in **module.json5** file of the specific project matches the command execution module. As shown in the preceding figure, the **assembleHar** command is used to pack the HAR module in the project. If the **type** field in **module.json5** file is not **har**, the preceding error is reported.

**Solution**

1.  Run the correct command.
2.  Check the **type** field in **module.json5** file of the project and run the corresponding command.
