# How do I resolve the "Scan files to index fail" error when starting DevEco Studio?

**Symptom**

When a project is opened in DevEco Studio, the startup is slow and the error message "Scan files to index fail" is displayed after a while.

**Solution**

When a project is opened in DevEco Studio, the Node.js process in the editor is started to scan the project code to create an index. The default memory limit of the Node.js process is 8 GB. When the memory limit is exceeded, the Node.js process fails to be started, and error "Scan files to index fail" is reported. To prevent the editor from failing to start due to an excessively large volume of project code, configure an appropriate memory upper limit for the Node.js process based on the project code volume and the memory size of the development environment. The memory limit needs to increase with the code amount and complexity of the project. Generally, it is recommended that the memory limit be greater than 12 GB for a project with 3 million lines of code and greater than 15 GB for a project with 4 million lines of code. The memory limit increases by 3 GB for every additional 1 million lines of code. You can adjust the memory limit as required.

For example, if you want to set the memory limit to 12 GB, open DevEco Studio and choose **Help** > **Edit Custom Properties** to open the **idea.properties** configuration file. Add **arkts.server.max.old.space.size=12288** to the file and restart DevEco Studio. Then the memory limit is set to 12288 MB (12 GB).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/HekP1kXORz2IunzxQbC84w/en-us_image_0000002378621596.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3342608D7D56E44DD65699A7EC22038866E7D7C6CAA1BE3A8443D122F02FA3D9)
