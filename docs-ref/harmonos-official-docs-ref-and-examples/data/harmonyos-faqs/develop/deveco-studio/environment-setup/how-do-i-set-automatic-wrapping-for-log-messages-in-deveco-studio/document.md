# How do I set automatic wrapping for log messages in DevEco Studio?

Simply enable the Soft-Wrap feature.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/plLJ8dvHSIaGQ4JTyJlNEA/en-us_image_0000002194158840.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=737008CD79138BDEABDAD7586F55847D6287B38457F8A174015DBC180AA1913F "Click to enlarge")

The maximum length of a single log entry is 4096 characters. It is recommended that the length of printed log entries be checked in the application log framework. If an entry exceeds a certain length, print it in segments to avoid log loss.
