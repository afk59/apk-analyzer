# How do I install Python on macOS without modifying environment variables?

1\. Download the official Python installation package for macOS. Python [3.11.7](https://mirrors.huaweicloud.com/python/3.11.7/python-3.11.7-macos11.pkg) is recommended.

2\. You can customize the installation on macOS without modifying the environment variables. For details, see [Using Python on macOS](https://docs.python.org/3.14/using/mac.html), and deselecting **UNIX command-line tools** and **shell profile updater**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/2Apeq0p2SkWiSYi7lbMNhA/en-us_image_0000002498271829.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B13FE086BD22C3466B2CF65B82EE6A3234051BC258317B631348370DAC2601A)

3\. Close DevEco Studio and modify the **other.xml** file.

cd ~/Library/Application\\ Support/Huawei/DevEcoStudio6.0/options

vi other.xml

Enter **/python** to locate the **location.python.path** line and change the Python path to **/Library/Frameworks/Python.framework/Versions/3.11/bin**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/pdMKxY_rRTuM-ybL7xkRKA/en-us_image_0000002465312430.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40C58E65E371379C057D3E48F1CD34EA0DFF6C654759C779A5CF45DCEEE65926)
