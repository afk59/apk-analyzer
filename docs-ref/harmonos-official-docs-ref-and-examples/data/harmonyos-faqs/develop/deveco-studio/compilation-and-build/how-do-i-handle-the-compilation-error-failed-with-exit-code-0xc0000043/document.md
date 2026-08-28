# How do I handle the compilation error "failed with:Exit code 0xc0000043"?

**Symptom**

When compiling and building the Native C++ module, an error occurs: "failed with: Exit code 0xc0000043".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/DN291Rk2S5ijMo1QkXr7IQ/en-us_image_0000002547275017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFD0486D52D6AB3BAC9185A543072C7251549A4AC502759AD94094767F25A11D)

**Possible Causes**

This error is an NTSTATUS error code on the Windows system. The error may occur because a corrupted or incomplete executable file is used, or because antivirus software/firewall blocks the loading of the **ninja.exe** file.

**Solution**

1\. Open the command line tool in the directory where the problematic **ninja.exe** file is located, and execute the command **ninja.exe --version**. If the version information fails to be output normally, the file may be corrupted or missing; it is recommended to reinstall DevEco Studio.

2\. Disable the antivirus software temporarily, or manually add the **ninja.exe** file to the antivirus software's whitelist, and then perform the compilation and building again.
