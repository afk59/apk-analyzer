# What should I do if an error message "EPERM: operation not permitted, symlink 'xxxxxxxx' -> 'xxxxxxx'......" is displayed on the console during the build process?

**Symptom**

When DevEco Studio is used to compile and build a project or module on Windows, the following error information is displayed on the console: **EPERM: operation not permitted, symlink 'xxxxxxxx' -> 'xxxxxxx'......**, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/P7j75tCzSr2YYZ3xguPong/en-us_image_0000002466832505.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=441C08E0FBF892076FDA54FA5D66AD8D7E4F183FD2DDAD13078C0A81EF976052)

**Possible Causes**

During compilation and build, some files need to be copied. Node based hvigor uses the **copySync** API of the **fse-extra** module to perform the copy operation. When the **copySync** API is used to copy a file directory, if there are file directory symbolic links in the source directory, the same symbolic links will be created in the target directory by default. However, by default, there is no permission to create file directory symbolic links in the Windows system, so that the execution fails and an error is reported.

**Solution**

1\. On the Windows system, choose **Settings** > **System** > **Developer Mode**. After the developer mode is enabled, the permission to create file directory symbolic links is available.

2\. Run the build command as an administrator. The administrator has the permission to create file directory symbolic links.

Note: In method 2, you can close DevEco Studio, right-click the DevEco Studio icon, and choose **Run as administrator** from the shortcut menu. Alternatively, run the terminal as an administrator, run the **hvigorw --stop-daemon-all** command in the terminal to avoid the impact of the running daemon process, and then run the build command.
