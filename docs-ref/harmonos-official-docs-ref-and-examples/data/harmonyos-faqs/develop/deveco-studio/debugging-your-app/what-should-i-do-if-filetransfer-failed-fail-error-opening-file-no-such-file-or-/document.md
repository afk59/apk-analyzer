# What should I do if "FileTransfer Failed: \[Fail\]Error opening file: no such file or directory" is displayed during HAP installation on DevEco Studio?

**Symptom**

The error message "FileTransfer Failed: \[Fail\]Error opening file: no such file or directory" is displayed during HAP installation on DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/X75AsHJjSmaUmU7wtn_peQ/en-us_image_0000002356774736.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A55B9BBEBAB640649667EC1DC4950C19199371782CC16EB9A8590DC6F27FD971)

**Solution**

The issue arises because the installation package at the specified path does not exist. You can check whether the signed HAP file has been built successfully, modify the signature configuration, and then install it again.

**Reference**

[Signing the HAP or APP File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-command-line-building-app#section103321051433)
