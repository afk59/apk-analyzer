# How do I resolve the automatic signing error "The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again"?

**Symptom**

Automatic signing failed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ZotE4LlbQye4ISmvXjNHJQ/en-us_image_0000002229604309.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0519CCF4B58DEB9420AE6C2304BEC1EFD899548AD4626F62254B984F562CFDB)

**Solution**

Make sure the local PC time is synchronized with the server time (Beijing time), accurate to the second.

You can go to **Settings** > **Time and Language** > **Date and Time** and enable **Set time automatically** to synchronize your local time with the Internet time. Make sure your system time is accurate to within 1–2 seconds of the correct time. Alternatively, run the following command as the administrator:

net time /Domain:china.huawei.com /set /y
