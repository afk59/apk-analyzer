# What should I do if the editing feature fails and the message "ArkTS language service terminated due to memory constraints." is displayed?

**Symptom**

Scenario 1: When performing operations involving extensive code modifications multiple times, such as executing **git pull** or switching branches, the memory peak of the editor's Node.js process exceeds the limit (8 GB by default). It fails to reclaim memory in time, leading to an OOM (out-of-memory) error. Consequently, editing features become ineffective, and a dialog box appears with the message: "ArkTS language service terminated due to memory constraints."

Scenario 2: When the editor starts, it scans the project code. When a project is too large, the editor may encounter an issue where the Node.js process exceeds the memory limit (8 GB by default) during project code scanning, leading to a launch failure of the editor, and the message "Scan files to index fail" is displayed.

**Solution**

You can adjust the memory limit for the Node.js process in the editor to solve the preceding problem. Please set a proper memory limit for the Node.js process based on the project code amount and the memory size of the development environment. The memory limit needs to increase with the code amount and complexity of the project. Generally, it is recommended that the memory limit be greater than 12 GB for a project with 3 million lines of code and greater than 15 GB for a project with 4 million lines of code. The memory limit increases by 3 GB for every additional 1 million lines of code. You can adjust the memory limit as required.

For example, if you want to set the memory limit to 12 GB, open DevEco Studio and choose **Help** > **Edit Custom Properties** to open the **idea.properties** configuration file. Add **arkts.server.max.old.space.size=12288** to the file and restart DevEco Studio. Then the memory limit is set to 12288 MB (12 GB).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/mnhZvZP3QjGMjlKupKSkFQ/en-us_image_0000002412101125.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4DDB20629B605616918C84CEEAD5479709DA43375B83CB258CEB975B43AAC2D)
