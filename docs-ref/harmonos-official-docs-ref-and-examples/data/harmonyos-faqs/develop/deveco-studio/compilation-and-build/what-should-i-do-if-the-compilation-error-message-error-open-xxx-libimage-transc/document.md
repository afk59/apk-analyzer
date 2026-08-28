# What should I do if the compilation error message "Error: open 'xxx\\libimage\_transcoder\_shared.dll' failed" is displayed?

**Symptom**

During a project compilation on Windows, the error message "Error: open 'xxx\\deveco-studio\\sdk\\default\\hms\\toolchains\\lib\\libimage\_transcoder\_shared.dll' failed" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/UgAjz3xESEOXr8MCC-bf7g/en-us_image_0000002194158948.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AC1CB6738A4E367A1B571AAD45FB677091C8A9EA6D7C64AF69A7C14DCE89024)

**Possible Causes**

1\. The system cannot find the **libimage\_transcoder\_shared.dll** file and the path of the third-party library on which the file depends in the environment variables.

2\. Some paths in the user or system environment variables might contain directories with restricted permissions or damaged files. If these paths are listed before the **libimage\_transcoder\_shared.dll** file path in the environment variables, the system will attempt to access these problematic paths first, leading to a failure when trying to load the .dll file.

For example, the **%USERPROFILE%\\AppData\\Local\\Microsoft\\WindowsApps** path is in the user environment variables.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/hDwBzSAoQg6ay499H5JnzA/en-us_image_0000002229758829.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A77E1C3661698B0FD7AF86A8CA6704973156F000D7D3767E4A006C0C5E3412DE)

However, files in this path cannot be accessed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/lCDxrjSiSuS-58627tuY8A/en-us_image_0000002194158944.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB259B85310E8CF5A0D09C6DF790A4FBF78C1B479E5A54E85AF4201826163440)

**Solution**

1\. Add the **xxx\\deveco-studio\\sdk\\default\\hms\\toolchains\\lib** and **xxx\\deveco-studio\\sdk\\default\\openharmony\\previewer\\common\\bin** paths to the beginning of the system environment variables.

2\. Check both user and system environment variables for any paths that may be causing the issue. Verify that all paths in the environment variables are accessible. You can attempt actions such as modifying or compressing files in the directories to confirm there are no errors. If there are any inaccessible paths, remove them from the environment variables.
