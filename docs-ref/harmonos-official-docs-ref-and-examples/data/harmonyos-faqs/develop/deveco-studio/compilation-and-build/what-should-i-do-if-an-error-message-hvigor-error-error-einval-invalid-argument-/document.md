# What should I do if an error message "hvigor ERROR: Error: EINVAL: invalid argument, mkdir 'D:xxx\\yyy\\zzz\\D:'/ 'C:xxx\\yyy\\zzz\\C:at Object.mkdirSync (node:fs:1391:3)" is displayed?

**Symptom**

A build error message " hvigor ERROR: Error: EINVAL: invalid argument, mkdir 'D:xxx\\yyy\\zzz\\D:'" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/P_tA21szRlmqmYJrUBNI6w/en-us_image_0000002433194024.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA808C9D5F8962EEB72DBC166B61BB897B432F611A7D515F56A6CB63CC0C31E1)

**Common Error Scenarios**

Project A uses the HAR module of project B. After executing **ohpm** in project B, project A directly compiles (or debugs) without executing **ohpm install** again, causing a compilation error.

**Possible Causes**

After the installation of ohpm, a remote third-party package, the path pointed to by symbolic links is not within the current project (due to tampering by other projects), and unexpected errors occur during compilation. Note: Dependencies that can exist outside the project path are only local modules. For details, see the usage of modules outside the project on the official website.

**Solution**

1\. Re-execute **ohpm install** or **sync** in the project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/ofqrPbigSVOwEhBlhVHxaA/en-us_image_0000002433353864.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2815F6F4A6191F19EEAF0B6D8AC74A55D8EEA26CC7C3E172ED74252FE469A617 "Click to enlarge")

2\. Use the **Build** menu to build the project first, and then debug and run the project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/Shbsoa40TEW_4zagND1nnQ/en-us_image_0000002466912421.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8922215F34444DA46F9C4FAC8F2321BFD1FBB6294CB5BBAEE751F70952EA92B5 "Click to enlarge")
