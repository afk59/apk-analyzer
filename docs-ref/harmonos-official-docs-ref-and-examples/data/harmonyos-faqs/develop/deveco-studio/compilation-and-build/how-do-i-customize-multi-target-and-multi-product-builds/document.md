# How do I customize multi-target and multi-product builds?

**Symptom**

In order to cater for different deployment environments, audiences, operating environments, and more, multi-target and multi-product builds are required to customize multiple editions of an application.

**Solution**

Refer to the code snippet below.

1\. The configuration example of **build-profile.json5** is as follows:

{
  "app": {
    "products": \[
      {
        "name": "default",
        "signingConfig": "default",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      },
      {
        "name": "release",
        "signingConfig": "release",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      },
      {
        "name": "beta1",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      },
      {
        "name": "zhaohangzhuanyong",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      }
    \],
    "buildModeSet": \[
      {
        "name": "debug",
      },
      {
        "name": "beta1"
      }
    \],
    "signingConfigs": \[
      {
        "name": "release",
        "material": {
          "storePassword": "",
          "certpath": "",
          "keyAlias": "",
          "keyPassword": "",
          "profile": "",
          "signAlg": "SHA256withECDSA",
          "storeFile": ""
        },
        "type": "HarmonyOS"
      },
      {
        "name": "default",
        "material": {
          "storePassword": "",
          "certpath": "",
          "keyAlias": "",
          "keyPassword": "",
          "profile": "",
          "signAlg": "SHA256withECDSA",
          "storeFile": ""
        },
        "type": "HarmonyOS"
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
            "release"
          \]
        }
      \]
    },
    {
      "name": "library1",
      "srcPath": "./library1"
    },
    {
      "name": "library2",
      "srcPath": "./library2"
    },
    {
      "name": "library",
      "srcPath": "./library",
      "targets": \[
        {
          "name": "default",
          "applyToProducts": \[
            "release"
          \]
        }
      \]
    },
  \]
}

2\. The configuration example of **targets** in **modules** > **build-profile.json5** is as follows:

{
  "apiType": "stageMode",
  "buildOption": {
    "arkOptions": {
      // "apPath": "./modules.ap" /\* Profile used for profile-guided optimization (PGO), a compiler optimization technique to improve app runtime performance. \*/
    }
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
  \],
  "targets": \[
    {
      "name": "default",
      "runtimeOS": "HarmonyOS"
    },
    {
      "name": "ohosTest",
    }
  \]
}
