# How do I obtain the value in BuildProfile?

After the **BuildProfile** file is generated, you can import the file to the code through the relative path. For example, use this file in the **Index.ets** file of the HAR module as follows:

import BuildProfile from './BuildProfile';

Obtain the value in the **BuildProfile** class as follows:

const HAR\_VERSION: string = BuildProfile.HAR\_VERSION;
const BUILD\_MODE\_NAME: string = BuildProfile.BUILD\_MODE\_NAME;
const DEBUG: boolean = BuildProfile.DEBUG;

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/GPoJkgMrTx2k_vFDfDKFFw/en-us_image_0000002229604169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FD018435E76A1D9309CC5EC1B17B26C7242C7C600E8593C63FD2634B6E54F57 "Click to enlarge")

**Reference**

[Obtaining Build Parameters During HAR Running](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-guide#section68146594553)
