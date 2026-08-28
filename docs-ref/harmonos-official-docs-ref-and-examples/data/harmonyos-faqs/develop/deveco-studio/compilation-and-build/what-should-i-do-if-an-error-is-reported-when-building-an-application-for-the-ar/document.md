# What should I do if an error is reported when building an application for the ARKUI-X project in DevEco Studio 6.0.0 Beta1 and later versions?

**Symptom**

The error message "Could not open settings generic class cache for settings file" is displayed during application building.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/DQcCH_ytTA2GfcKyL27nVg/en-us_image_0000002381980508.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F657D2767CAEFA53398FAC882F620DA35CBB67B7D9F2E1D2DB7A47C78DCC4983)

**Common Error Scenarios**

The current project is created using DevEco Studio earlier than 6.0.0 Beta1.

**Possible Causes**

The Java version built in DevEco Studio 6.0.0 Beta1 is 21, and the current Gradle version is earlier than the one matching Java 21.

**Solution**

-   Method 1: Upgrade the Gradle version
    
    Modify the **distributionUrl** in **gradle-wrapper.properties** to upgrade Gradle to 8.4.
    
    distributionUrl=https\\://repo.huaweicloud.com/gradle/gradle-8.4-bin.zip
    

-   Method 2: Specify to use Java 17.
    
    If JDK 17 is installed, you can use the **org.gradle.java.home** variable in the **gradle.properties** file to specify Java 17.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/CZytAlHCSyq0uMTq_hFdXA/en-us_image_0000002415859685.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34AF528E9DBAB8F38BD58D7C5EBE81173D945C10A74A0C982581C1A876D9B21F)
