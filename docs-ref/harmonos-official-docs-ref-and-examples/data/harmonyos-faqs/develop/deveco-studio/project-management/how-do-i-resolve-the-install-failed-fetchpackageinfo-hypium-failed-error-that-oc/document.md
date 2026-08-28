# How do I resolve the "Install failed FetchPackageInfo: hypium failed" error that occurs when opening a historical project?

**Symptom**

When a historical project is opened in DevEco Studio, the dependency installation fails and the error message "Install failed FetchPackageInfo: hypium failed" is displayed.

**Solution**

The package name may be incorrect. In the project-level **oh-package.json5** file, change **hypium** in the **devDependencies** field to **@ohos/hypium**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/f-EB3smSTG6z6hdMiXCuQQ/en-us_image_0000002194158560.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1702F4A55168A7F7B5D66BCE3BC3FA02FE0776702D20AA58E26E07FC0B6AEB1)

You can run the **ohpm info @ohos/hypium** command in the DevEco Studio terminal to obtain the **@ohos/hypium** version number. The version number is under **dist-tags** in the command output.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/UNFchP_4Q3K2Ekb5ulnHiQ/en-us_image_0000002402257997.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6409450C9A576F8DFC3C7DF5BE86E2F120E7704B03D967A5F5F009F4442D9CA7)
