# Introduction

During the build, hvigor generates the **BuildProfile** class for you to obtain build parameters. You can also add custom fields through **buildProfileFields** in **build-profile.json5** to access these custom parameters during runtime.

#### Usage

**buildProfileFields** has a hierarchy of precedence that determines which configuration takes priority when there are overlapping settings. The order of precedence, from highest to lowest, is as follows: module-level **target** > module-level **buildOptionSet** > module-level **buildOption** > project-level **product** > project-level **buildModeSet**

#### Obtaining Build Parameters During HAP/HSP Running

## Generating the BuildProfile Class File

Currently, the **BuildProfile** class file can be generated in the following ways:

-   Select the module for build and choose **Build** > **Generate Build Profile ${moduleName}** on the menu bar.
-   Choose **Build** > **Build Hap(s)/APP(s)** > **Build Hap(s)** or **Build** > **Build Hap(s)/APP(s)** > **Build APP(s)** on the menu bar.
-   Run the following command on the **Terminal** page:
    
    hvigorw GenerateBuildProfile
    

The **BuildProfile.ets** file is generated in **${moduleName} / build / ${productName} / generated / profile / ${targetName}**. The following is an example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/8KuwBOBHSVistdMJusOAEA/en-us_image_0000002532670311.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44B5E0784F8639BA58E690CD5E13CC6FFB079F5AE8C312DB1EA2F07AABE0A808)

## Obtaining Build Parameters from Code

After the **BuildProfile** class file is generated, you can import it to the code with the following statement, where _packageName_ indicates the value of the **name** field in the module-level **oh-package.json5** file:

import BuildProfile from '${packageName}/BuildProfile';

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/N0Y8RqT6TWCYgKnAyB1AhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9CFD8FED660330B759D2A35F40E9D6F5082CACAB401B9628046A0DF5F76E054)

With usage of an HSP, you might encounter compilation errors when using **import BuildProfile from 'BuildProfile'** in a cross-package integration scenario. To avoid such issues, you are advised to use **import BuildProfile from '${packageName}/BuildProfile'**.

Run the following command to obtain build parameters:

@State message: string = BuildProfile.BUNDLE\_NAME;

## Default Parameters

When generating the **BuildProfile** class file, hvigor also generates some default parameters based on the configuration information of the current project. You can directly use the default parameters in the code.

**Table 1** Description of default parameters
| 
Name

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

BUNDLE\_NAME

 | 

string

 | 

Bundle name.

 |
| 

BUNDLE\_TYPE

 | 

string

 | 

Bundle type.

 |
| 

VERSION\_CODE

 | 

number

 | 

Version code of the application, which is the internal version number.

 |
| 

VERSION\_NAME

 | 

string

 | 

Version number of the app, which is shown to users.

 |
| 

TARGET\_NAME

 | 

string

 | 

Target name.

 |
| 

PRODUCT\_NAME

 | 

string

 | 

Product name.

 |
| 

BUILD\_MODE\_NAME

 | 

string

 | 

Build mode.

 |
| 

DEBUG

 | 

boolean

 | 

Whether the app can be debugged.

 |

## Customizing Parameters

You can add customized parameters to the module-level **build-profile.json5** file and use them in the code after the **BuildProfile** class file is generated.

Parameter customization can be implemented by adding **buildProfileFields** to the **arkOptions** subnode under **buildOption**, **buildOptionSet**, or **targets** nodes. Customized parameters are configured in a key-value pair format. The value type can only be **number**, **string**, or **boolean**.

The following is a configuration example.

{
  "apiType": "stageMode",
  "buildOption": {
    "arkOptions": {
      "buildProfileFields": {
        "data": "Data",
      }
    }
  },
  "buildOptionSet": \[
    {
      "name": "release",
      "arkOptions": {
        "buildProfileFields": {
          "buildOptionSetData": "BuildOptionSetDataRelease",
          "data": "DataRelease"
        }
      }
    },
    {
      "name": "debug",
      "arkOptions": {
        "buildProfileFields": {
          "buildOptionSetData": "BuildOptionSetDataDebug",
          "data": "DataDebug"
        }
      }
    }
  \],
  "targets": \[
    {
      "name": "default",
      "config": {
        "buildOption": {
          "arkOptions": {
            "buildProfileFields": {
              "targetData": "TargetData",
              "data": "DataTargetDefault"
            }
          }
        }
      }
    },
    {
      "name": "default1",
      "config": {
        "buildOption": {
          "arkOptions": {
            "buildProfileFields": {
              "targetData": "TargetData1",
              "data": "DataTargetDefault1"
            }
          }
        }
      }
    },
    {
      "name": "ohosTest",
    }
  \]
}

#### Obtaining Build Parameters During HAR Running

## Generating the BuildProfile Class File

Currently, the **BuildProfile** class file can be generated in the following ways:

-   Select the module for build and choose **Build** > **Generate Build Profile ${moduleName}** on the menu bar.
-   Select the module for build and choose **Build** > **Make Module ${moduleName}** on the menu bar.
-   Run the following command on the **Terminal** page:
    
    hvigorw GenerateBuildProfile
    

The **BuildProfile.ets** file is generated in the root directory of the module. You can ignore this file by adding it to the **.gitignore** file. The following is an example of the **BuildProfile.ets** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/lUn44JJVSg6JkZBMpzR7UA/en-us_image_0000002532670309.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC2D10345C22D7DC4AA33C968595F1FD917255ACBF49F97DEEDDDE16027904DD)

## Obtaining Build Parameters from Code

After the **BuildProfile** class file is generated, you can import the file through a relative path in the code. For example, run the following command to import the class file to the **Index.ets** file of the HAR module:

import BuildProfile from './BuildProfile';

Then, run the following command to obtain build parameters:

const HAR\_VERSION: string = BuildProfile.HAR\_VERSION;

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/9p8EIOSRQySmsihIpsKk6Q/en-us_image_0000002501070236.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71EDC0C3FE7383CE97A6485EE7B1B093E2337F949984FE44B389587BCAF706C7)

## Default Parameters

When generating the **BuildProfile** class file, hvigor also generates some default parameters based on the configuration information of the current project. You can directly use the default parameters in the code.

**Table 2** Description of default parameters
| 
Name

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

HAR\_VERSION

 | 

string

 | 

HAR version number.

 |
| 

BUILD\_MODE\_NAME

 | 

string

 | 

Build mode.

 |
| 

DEBUG

 | 

boolean

 | 

Whether the app can be debugged.

 |
| 

TARGET\_NAME

 | 

string

 | 

Target name.

 |

## Customizing Parameters

You can add customized parameters to the module-level **build-profile.json5** file and use them in the code after the **BuildProfile** class file is generated.

Parameter customization can be implemented by adding **buildProfileFields** to **arkOptions** under the **buildOption** or **buildOptionSet** node. Customized parameters are configured in a key-value pair format. The value type can only be **number**, **string**, or **boolean**.

The following is a configuration example.

{
  "apiType": "stageMode",
  "buildOption": {
    "arkOptions": {
      "buildProfileFields": {
        "data": "Data",
      }
    }
  },
  "buildOptionSet": \[
    {
      "name": "release",
      "arkOptions": {
        "buildProfileFields": {
          "buildOptionSetData": "BuildOptionSetDataRelease",
          "data": "DataRelease"
        }
      }
    },
    {
      "name": "debug",
      "arkOptions": {
        "buildProfileFields": {
          "buildOptionSetData": "BuildOptionSetDataDebug",
          "data": "DataDebug"
        }
      }
    }
  \],
  "targets": \[
    {
      "name": "default",
    }
  \]
}

#### Configuring Customized Build Parameters at the Project Level

After you add customized parameters to the project-level **build-profile.json5** file, they will be automatically generated in the **BuildProfile** class files of all modules for use in code.

Parameter customization can be implemented by adding **buildProfileFields** to **arkOptions** under **buildOption** in **buildModeSet** of project-level products. Customized parameters are configured in a key-value pair format. The value type can only be **number**, **string**, or **boolean**.

The following is a configuration example.

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
          "arkOptions": {
            "buildProfileFields": {
              "productValue": "defaultValue"
            }
          }
        }
      }
    \],
    "buildModeSet": \[
      {
        "name": "debug",
        "buildOption": {
          "arkOptions": {
            "buildProfileFields": {
              "productBuildModeValue": "debugValue"
            }
          }
        }
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
