# Examples

Before officially releasing an app, you need to thoroughly debug its code. The build behaviors of the debugging version and official release may be different. You can use **buildMode** to customize build differences between the two versions.

Assume that the build product is **default**, the build behaviors vary according to build modes. Obfuscation is enabled in **release** mode, and **debugging** is enabled in debug mode.

The example project contains the entry module that is delivered to the default build product. The module customizes two build modes, **debug** and **release**, and binds them to the default build product. The following figure shows a project example (module).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/mM8S_0bvRimqGaTq5JPWaA/en-us_image_0000002501069730.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED4676D489BAD024348B32B5A766292452B7A6AAF69915842006D5B1167A0B08)

#### Example of Project-Level build-profile.json5

{
  "app": {
    "signingConfigs": \[\],
    "products": \[
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "strictMode": {
            "caseSensitiveCheck": true,
            "useNormalizedOHMUrl": true
          }
        }
      }
    \],
    "buildModeSet": \[
      {
        "name": "debug"
      },
      {
        "name": "release"
      }
    \]
  },
  "modules": \[
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": \[
        {
          "name": "default",
          "applyToProducts": \[
            "default"
          \]
        }
      \]
    }
  \]
}

#### Example of Module-Level build-profile.json5

## Entry Module

{
  "apiType": "stageMode",
  "buildOption": {
  },
  "buildOptionSet": \[
    {
      "name": "release",
      "arkOptions": {
        "obfuscation": {
          "ruleOptions": {
            "enable": true,
            "files": \[
              "./obfuscation-rules.txt"
            \]
          }
        }
      }
    },
    {
      "name": "debug",
      "debuggable": true,
      "arkOptions": {
        "obfuscation": {
          "ruleOptions": {
            "enable": false
          }
        }
      }
    }
  \],
  "buildModeBinder": \[
    {
      "buildModeName": "release",
      "mappings": \[
        {
          "buildOptionName": "release",
          "targetName": "default"
        }
      \]
    },
    {
      "buildModeName": "debug",
      "mappings": \[
        {
          "buildOptionName": "debug",
          "targetName": "default"
        }
      \]
    }
  \],
  "targets": \[
    {
      "name": "default",
    },
    {
      "name": "ohosTest",
    }
  \]
}

#### Specifying a Build Mode

## Command Line Tool

Example 1: When building an app, if the build product is **default** and the build mode is **debug**, run the following command:

hvigorw --mode project -p product=default -p buildMode=debug assembleApp

The figure below shows an example of the build product.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/44VqL5vtRza1P-A6vly9wQ/en-us_image_0000002501069728.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACEE12722CDE140BA81C8B385E17E587128F4A11425DCA6846727B4E04A20A96)

Example 2: When building an app, if the build product is **default** and the build mode is **release**, run the following command:

hvigorw --mode project -p product=default -p buildMode=release assembleApp

The figure below shows an example of the build product.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/4qGbnyy9SwyMs2Nkp5ZsSw/en-us_image_0000002532669795.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8595BA2961448962F85284B69EB3EC8952433A2558172EC5830E5B5D15FBE740)

## DevEco Studio GUI

On the DevEco Studio GUI, select **debug** from the **Build Mode** drop-down list box, and choose **Build** > **Build Hap(s)/APP(s)** > **Build APP(s)** to build an App Pack with build mode of **debug** and build product of **default**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/gF9yfW7XQ3yBkkEYJi14ug/en-us_image_0000002532669793.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49F5AEF035333877895CDDEE7048E9E0F5DDE47FAAAA2E7C5C9D8CAE37281658)
