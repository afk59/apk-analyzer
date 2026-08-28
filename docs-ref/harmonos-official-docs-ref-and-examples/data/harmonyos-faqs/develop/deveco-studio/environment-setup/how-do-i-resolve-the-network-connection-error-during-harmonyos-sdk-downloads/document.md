# How do I resolve the network connection error during HarmonyOS SDK downloads?

**Symptom**

During a HarmonyOS SDK download, an error is displayed while the network connection is normal.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/X6TlsguVQpiFgJ6hAqfYRA/en-us_image_0000002229758633.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72EA7174634595FCE04DE4BBAECC47F40D51BFCE8BAF9163DC1C4904AE1BE20F)

**Solution**

A possible cause is that the PC system language is English and the region code is US. Close DevEco Studio and perform the steps below to change the region code to CN:

In **C:\\Users\\\_username\_\\AppData\\Roaming\\Huawei\\DevEcoStudio4.1\\options** (**/Users/\_username\_/Library/Application Support/Huawei/DevEcoStudio4.1/options** on macOS), open the **country.region.xml** file and change the value of **countryregion name** to **CN**.

<application>
    <component name="CountryRegionSetting">
        <countryregion name="CN"/>
    </component>
</application>
