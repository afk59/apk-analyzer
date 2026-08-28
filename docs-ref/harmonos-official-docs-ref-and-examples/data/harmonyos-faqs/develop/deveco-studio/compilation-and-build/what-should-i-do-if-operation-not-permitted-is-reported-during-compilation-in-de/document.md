# What should I do if "Operation not permitted" is reported during compilation in DevEco Studio?

**Symptom**

After the DevEco Studio is installed, "Operation not permitted" is reported multiple times. The error message is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/J1TJLpVMQFCtk9IsMrrPVQ/en-us_image_0000002194158416.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5A89845F2F4BA6DA6BFBD51253CE0431CBD5C1199C0DD31739C8A237CF7D834)

**Root Cause**

The macOS has restrictions on file access.

**Solution**

Run the following command to check whether the **com.example.myapplication** identifier exists:

**xattr -l /path/to/es2abc**

Run the following command to delete the identifier:

**xattr -d com.example.myapplication/path/to/es2abc**
