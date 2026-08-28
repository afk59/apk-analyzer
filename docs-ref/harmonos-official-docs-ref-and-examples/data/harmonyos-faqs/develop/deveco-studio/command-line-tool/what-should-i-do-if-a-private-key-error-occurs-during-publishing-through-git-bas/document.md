# What should I do if a private key error occurs during publishing through Git Bash?

**Symptom**

Publishing works correctly through the CLI or terminal, but during publishing through Git Bash, an error message is displayed to indicate that the private key content in the private key path is incorrect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/BsvHlmMTQVu_3K7gM00UcQ/en-us_image_0000002194158912.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=119A8BE84A7AB9B96CC9A70B6CF13FF7F533C6110F6979569C855627E14166C1 "Click to enlarge")

**Solution**

Method 1: Download and install the latest version of Git from the official website and use the Git Bash terminal that comes with the installed version for operations.

Method 2: Add a **git-bash.config** file under the **etc** directory in the current Git installation path. Add the following line to the file: **MSYS=enable\_pcon**. Open the Git Bash terminal again and run the **ohpm publish** command.
