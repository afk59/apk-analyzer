# What should I do if the command execution is suspended on the daemon startup log or the compilation error "ReferenceError, TransformStream is not defined in hvigorfile: XXX" is reported?

**Symptom**

After the command is executed in the pipeline or command line, the following information is displayed in the daemon log:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/vuSJu5GeTWCG4T_zRP1G1w/en-us_image_0000002345811941.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F22A6A38AD59E13AC5BF693696933E432F30EB78BE0F9FD5F8534CF6284D6025)

Or, a compilation error is reported in the pipeline or command line:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/WG_n265QRsGvSxUHgz3pYQ/en-us_image_0000002312015854.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=248B921A2258BFE1F3CE717531B40A5DEDA17CF8AC35505B2583D9699283DA47)

**Possible Causes**

The build system requires Node.js v18.0.0 or later. For details, see [Setting the Node.js Environment Variables](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-command-line-building-app#section159168531288).

**Solution**

1\. Check the Node.js version.

On Windows, open Command Prompt or PowerShell and run the following command. On macOS or Linux, open Terminal and run the following command.

node -v

Check the version output.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/cnMIKjn8Smu_4FNCiB20EA/en-us_image_0000002284561689.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=663D4D104952BB03E618F6442902A8F15FE2F60EF6BCCC58F7875325A76CC0DF)

2\. If the Node.js version is earlier than v18.0.0, consider using the Node.js package provided by DevEco Studio or Command Line Tools to configure system variables.

On Windows, open the environment variable settings and add the path of Node.js to **Path** under system variables. If the Node.js path is configured using the **NODE\_HOME** variable, update the variable value accordingly. If Node.js of another version already exists in the system, add the Node.js path provided by the tool to the beginning of the Path variable to ensure that this version is used first. When using **NODE\_HOME** to configure, check whether Path contains **%NODE\_HOME %/bin** (Windows) or **$NODE\_HOME/bin** (Mac/Linux) to ensure that the configuration takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/nw84zyUdSzi797jx0Y_WeA/en-us_image_0000002284693797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8962F046CDE7769496634C66D87A12D72EEC174F377C823884F84089955D920)

On macOS or Linux, you can set the Node.js environment variables by referring to [Setting the Node.js Environment Variables](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-command-line-building-app#section159168531288).

Path of Node.js in DevEco Studio: **_DevEco Studio installation directory_/DevEco Studio/tools/node**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/5H9FXmBaQEWU9TV4us6E8A/en-us_image_0000002284546061.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3D47348DEECA4C63891225E09A98B1874BA5401E1322EE0CB927CCD1A193066)

Path of Node.js in the Command Line Tools package: **_Command Line Tools installation directory_/command-line-tools/tool/node**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/xAEmrxwoSs6k0vVZCONxhQ/en-us_image_0000002284672673.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13632474866EDC8FB955F8E9D56550A303E73313A7A81B326E01D15E707DBF79 "Click to enlarge")

3\. Upgrade the Node.js version in use to match the one provided by DevEco Studio or Command Line Tools. Run **node -v** in the specified path to check the version, and download the corresponding version from the Node.js official website: https://nodejs.org/dist/v18.20.1/.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ES7r5aiWS1i2c4MWXltxGQ/en-us_image_0000002277140989.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=571CB6E9AE680A93210304D85E0911E1FE6465C0DCE70B24D270D4E8AEA04C6B)
