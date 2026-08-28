# What should I do if the build fails due to mismatch of the JDK version?

**Symptom**

HarmonyOS applications or atomic services fail to be built using command lines, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/qPL_nXdsRZWQ5uwl33-Rsg/en-us_image_0000002229604033.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=277A833B23F45D1DAD190F691D4D7AF835C15F57B4D59DA01FD298D913963C75)

**Solution**

JDK version 17 must be used during the build process. To fix it, install JDK 17 as follows:

1.  Download and install JDK 17.
2.  Change the value of **JAVA\_HOME** to **JDK 17**. For details about how to use commands to build a service or an application in Linux, see [Configuring the JDK](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-command-line-building-app#section195447475220).
