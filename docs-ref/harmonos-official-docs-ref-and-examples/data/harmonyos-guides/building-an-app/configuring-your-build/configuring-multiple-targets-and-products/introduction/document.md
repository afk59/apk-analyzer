# Introduction

In real-world cases, you may often need to build multiple editions of your app – standard edition, premium edition, locale edition, international edition, and the like – to cater for different audiences, deployment environments, runtime environments, and more. DevEco Studio offers a great way to achieve this: multi-product and multi-target. With a small amount of targeted configuration, you can effortlessly reuse your existing source code and resource files to build multiple editions of an app.

Before setting out to customize multi-product and multi-target builds, you may want to familiarize yourself with the concepts of **target** and **product**.

-   Each module in a project, be it of the entry or feature type, is built into a HAP, which can independently run on a device. To allow a module to come in different HAPs for different use cases, the concept of **target** is introduced. A target is mapped to a HAP. With multiple targets defined, a module can be built into multiple HAPs, varying in functionality and resources.
-   A HarmonyOS project is built into an App Pack, which can be used to release the app/atomic service to AppGallery. To allow a project to come in different App Packs for different release purposes, **product** is introduced. A product is mapped to an App Pack. With multiple products defined, a project can be built into multiple App Packs, each of which caters to specific settings and service needs.

For more information, see [Building Multi-target Products](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-target).

#### Customizing Multi-Target Builds

You can define targets for an entry or feature module in the module's **build-profile.json5** file, differentiating these targets by the following factors: HAP name, device type (**deviceType**), source code set (**source**), resource (**resource**), **buildOption** configuration (such as .so dependencies of C++, obfuscation configurations, ABI types, and **cppFlags**), and distribution rules (**distributionFilter**).

**Defining targets**

First things first: Plan names for your targets, each of which is mapped to a HAP. The following example is a module-level **build-profile.json5** file for an ArkTS project of the stage model. It defines targets for a free edition and a paid edition.

{ 
  "apiType": 'stageMode', 
  "buildOption": {   
  }, 
  "targets": \[  // Define different targets.
    { 
      "name": "default",  // Default target name.
    }, 
    { 
      "name": "free",  // Name of the target for a free edition.
    }, 
    { 
      "name": "pay",  // Name of the target for a paid edition.
    } 
  \] 
}

In the previous example of target configuration, three HAPs will be generated: **default**, **free**, and **pay**.

## Defining HAP Names for Products

You can specify a product name for each target.

{ 
  "apiType": "stageMode", 
  "buildOption": { 
  }, 
  "targets": \[ 
    { 
      "name": "default", 
      "output": { 
        "artifactName": "customizedTargetOutputName-1.0.0"  // The product name is customizedTargetOutputName-1.0.0.
      } 
    }, 
    { 
      "name": "free", 
      "output": { 
        "artifactName": "customizedTargetOutputName1-1.0.0"  // The product name is customizedTargetOutputName1-1.0.0.
      } 
    }, 
    { 
      "name": "pay", 
      "output": { 
        "artifactName": "customizedTargetOutputName2-1.0.0"  // The product name is customizedTargetOutputName2-1.0.0.
      } 
    } 
  \] 
}

If a signature has been configured, the HAP name of a target is the customized product name. Otherwise, it is the customized product name appended with "unsigned."

## Defining Device Types for Targets

You can define the **deviceType** field for a target to specify the supported device types. If this field is not defined, a target supports all the device types defined in **module.json5** or [config.json](../../../../getting-started/development-fundamentals/application-configuration-files-in-fa-model/application-configuration-files-fa-model/document.md).

The device types specified for a target can be some or all of those defined in **module.json5** or **config.json**. For example, in the preceding three defined targets, the **default** target supports all device types, and the **free** and **pay** targets support only phone devices.

{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": \[ 
    { 
      "name": "default",  // deviceType is not defined. In this case, the target supports all device types defined in config.json or module.json5.

    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": \[  // The free target supports only phone devices.
          "phone" 
        \] 
      } 
    }, 
    { 
      "name": "pay", 
      "config": { 
        "deviceType": \[  // The pay target supports only phone devices.
          "phone" 
        \] 
      } 
    } 
  \] 
}

## Defining Distribution Rules for Targets

When **distributionFilter** is not defined for a target, the distribution rules configured through [distributionFilter](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#distributionfilter) or [distroFilter](../../../../getting-started/development-fundamentals/application-configuration-files-in-fa-model/structure-of-the-module-tag/document.md#internal-structure-of-the-distrofilter-attribute) of the module apply.

If multiple targets support the same device types, you must define the **distributionFilter** field for these targets separately.

For a FA project, the field concerned is **distroFilter**.

{ 
  "apiType": "stageMode", 
  "buildOption": { 
  }, 
  "targets": \[ 
    { 
      "name": "default", 

    }, 
    { 
      "name": "free", 
      "config": { 
        "distributionFilter": {  // For details, see the distributionFilter field.
          "screenShape": { // Screen shape
            "policy": "include", 
            "value": \["circle"\] 
          } 
        } 
      } 
    }, 
    { 
      "name": "pay", 
      "config": { 
        "distributionFilter": { 
          "screenShape": { 
            "policy": "include", 
            "value": \["rect"\] 
          } 
        } 
      } 
    } 
  \] 
}

## Defining Subpackages for Targets

To speed up the initial load of your atomic service, you can define the **preloads** field. If this field is not defined, the configuration in the **module.json5** file is applied.

{ 
  "apiType": 'stageMode', 
  "showInServiceCenter": true, 
  "buildOption": { 
  }, 
  "targets": \[   
    { 
      "name": "default",   
    },
    { 
      "name": "free",   
    },
    { 
      "name": "pay",   
      "config": { 
        "atomicService": { 
          "preloads": \[  // Specify the module to preload.
            { 
              "moduleName": "preloadSharedLibrary"
            } 
          \] 
        } 
      } 
    } 
  \] 
}

## Defining Source Code Files for Targets: pages

Depending on the API model, you can set source code files for pages: pages in the **pages** directory for the stage model and pages in the ability directories for the FA model.

-   In this example, the **Index.ets**, **Page1.ets**, and **Page2.ets** files are defined in the module-level **pages** directory for a project in the stage model. The **default** target uses **Index.ets** file as the source code file, the **free** target uses **Index.ets** and **Page1.ets**, and the **pay** target uses **Index.ets** and **Page2.ets**. The sample code is as follows:
    
    { 
       "apiType": 'stageMode', 
       "buildOption": { 
       }, 
       "targets": \[ 
         { 
           "name": "default", 
           "source": {  // Specify the source code files for the pages of the default target in the stage model.
             "pages": \[ 
               "pages/Index" 
             \] 
           } 
         }, 
         { 
           "name": "free", 
           "config": { 
             "deviceType": \[ 
               "phone" 
             \] 
           }, 
           "source": {  // Specify the source code files for the pages of the free target in the stage model.
             "pages": \[ 
               "pages/Index", 
               "pages/Page1" 
             \] 
           } 
         }, 
         { 
           "name": "pay", 
           "config": { 
             "deviceType": \[ 
               "phone" 
             \] 
           }, 
           "source": {  // Specify the source code files for the pages of the pay target in the stage model.
             "pages": \[ 
               "pages/Index", 
               "pages/Page2" 
             \] 
           } 
         } 
       \] 
     }
    

-   In this example, the **Index.ets**, **Page1.ets**, and **Page2.ets** files are defined in the module-level **MainAbility** directory for a project in the FA model. The **default** target uses **Index.ets** file as the source code file, the **free** target uses **Index.ets** and **Page1.ets**, and the **pay** target uses **Index.ets** and **Page2.ets**. The sample code is as follows:
    
    { 
       "apiType": 'faMode', 
       "buildOption": { 
       }, 
       "targets": \[ 
         { 
           "name": "default", 
           "source": {  // Specify the source code files for the pages of the default target in the FA model.
             "abilities": \[ 
               { 
                 "name": ".MainAbility", 
                 "pages": \[ 
                   "pages/index" 
                 \] 
               } 
             \], 
           } 
         }, 
         { 
           "name": "free", 
           "config": { 
             "deviceType": \[ 
               "phone" 
             \] 
           }, 
           "source": {  // Specify the source code files for the pages of the free target in the FA model.
             "abilities": \[ 
               { 
                 "name": ".MainAbility", 
                 "pages": \[ 
                   "pages/index", 
                   "pages/page1" 
                 \] 
               } 
             \], 
           } 
         }, 
         { 
           "name": "pay", 
           "config": { 
             "deviceType": \[ 
               "phone" 
             \] 
           }, 
           "source": {  // Specify the source code files for the pages of the pay target in the FA model.
             "abilities": \[ 
               { 
                 "name": ".MainAbility", 
                 "pages": \[ 
                   "pages/index", 
                   "pages/page2" 
                 \] 
               } 
             \], 
           } 
         } 
       \] 
     }
    

## Defining Source Code Files for Targets: sourceRoots

Within the main code space (**src/main**) of a module, the public code you have written is hosted. If you need to implement differentiated logic between different targets, you can use differentiated code spaces (**sourceRoots**). With the capability of differentiated code spaces, it is possible to compile corresponding code for different targets into the final product without changing the code in the main code space.

**Concepts**

-   **packageName**: name in the current module's **oh-package.json5** file.
-   **sourceRoot**: <defaultSourceRoot> | <targetSourceRoot>, where **<defaultSourceRoot>** is **src/main**, and **<targetSourceRoot>** can be customized. The addressing priority is <targetSourceRoot> > <defaultSourceRoot&gt.
-   **sourcePath**: code directory in **sourceRoot**.
-   **sourceFileName**: name of the .ets file in the code directory.

For example, consider the following project directory structure:

entry
|--src
|----main
|------ets
|--------code
|----------test.ets
|----target
|------util
|--------util.ets

-   **packageName** is **entry**.
-   **sourceRoot** is **src/main** and **src/target**.
-   **sourcePath** is **ets/code** and **util**.
-   **sourceFileName** is **test.ets** and **util.ets**.

**Constraints**

1\. **import xxx from '<packageName>/sourcePath/sourceFileName'**: By using the **packageName** approach and omitting **sourceRoot**, differentiated builds for different targets can be achieved.

2\. HAPs, HSPs, and HARs are supported. (Note: For HAR modules with [file or folder name obfuscation](../../../../application-framework/arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/arkguard-principles-and-capabilities-for-source-code-obfuscation/document.md#section-enable-filename-obfuscation) enabled, you need to use **\-keep-file-name** to specify **sourceRoot**, **sourcePath**, and **sourceFileName** to prevent the corresponding file and folder names from being obfuscated.)

3\. Cross-module references are not supported.

4\. Dynamic imports are not supported.

**Priority for Selecting Module Targets During Compilation**

During the compilation of a module, the **sourceRoots** used by the module is determined by the target used. The priority for selecting a target during the module compilation is as follows: target explicitly specified using commands > target referenced by the direct dependency > default.

For example, consider the following dependency chain:

hap -> hsp -> har (the arrow "->" indicates dependency)

Both **hap** and **hsp** have three targets: **default**, **custom**, and **static**, while **har** has two targets: **default** and **static**.

-   With the **hvigorw -p module=hap@custom assembleHap** command, the target specified for **hap** is **custom**. Therefore, the targets for the three modules during compilation are as follows:
    
    **hap**: **custom**, which is explicitly specified using commands.
    
    **hsp**: **custom**, which is not explicitly specified using commands and is determined based on the direct dependency, **hap**. Since the target for **hap** is **custom** and **hsp** has this target, **custom** is used for **hsp**.
    
    **har**: **default**, which is not explicitly specified using commands and is determined based on the direct dependency, **hsp**. Since the target for **hap** but **har** does not have this target, **default** is used for **hsp**.
    

-   With the **hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp** command, the target specified for **hap** and **hsp** is **custom** and **static**, respectively. Therefore, the targets for the three modules during compilation are as follows:
    
    **hap**: **custom**, which is explicitly specified using commands.
    
    **hsp**: **static**, which is explicitly specified using commands.
    
    **har**: **static**, which is not explicitly specified using commands and is determined based on the direct dependency, **hsp**. Since the target for **hsp** is **static** and **har** has this target, **static** is used for **har**.
    
-   On the basis of the current dependency relationship, add the dependency: hap -> har. Execute the **hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp** command. Since **har** does not explicitly specify a target and has two direct dependents, **hap** and **hsp**, with different targets (**custom** and **static**, respectively), only one of the targets can be selected for **har** during compilation. In this scenario, it is recommended that you explicitly specify the target for the module to be compiled, for example, **hvigorw -p module=hap@custom,hsp@static,har@static assembleHap assembleHsp assembleHar**.

**Example**

1\. Add **sourceRoots** to the **build-profile.json5** of the **entry** module:

{
  "apiType": "stageMode",
  "buildOption": {},
  "targets": \[ 
    { 
      "name": "default", 
      "source": { 
The "sourceRoots": \["./src/default"\] // Configure the differentiated code space for the default target.
      } 
    }, 
    { 
      "name": "custom", 
      "source": { 
        "sourceRoots": \["./src/custom"\] // Configure the differentiated code space for the custom target.
      } 
    } 
  \]
}

2\. Add **default/Test.ets** and **custom/Test.ets** under the **src** directory. The new module directory structure is as follows:

entry
  |--src
    |--main
      |--ets
        |--pages
          |--Index.ets
    |--default
      |--Test.ets  // Added
    |--custom
      |--Test.ets  // Added

3\. Write code in **default/Test.ets**:

export const getName = () => "default"

4\. Write code in **custom/Test.ets**:

export const getName = () => "custom"

5\. Modify the code in **src/main/ets/pages/Index.ets**:

import { getName } from 'entry/Test'; // entry is the value of the name field in the module-level oh-package.json5 file
@Entry
@Component
struct Index { 
  @State message: string = getName(); 
  build() { 
    RelativeContainer() { 
      Text(this.message) 
    } 
    .height('100%') 
    .width('100%') 
  }
}

6\. Set **targets** in the project-level **build-profile.json5** file.

{
  "app": {
    "signingConfigs": \[\],
    "products": \[
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "runtimeOS": "HarmonyOS",
      }
    \],
    "buildModeSet": \[
      {
        "name": "debug",
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
        },
        {
          "name": "custom",
          "applyToProducts": \[
            "default"
          \]
        }
      \]
    }
  \]
}

7\. After the synchronization is complete, when the target for the **entry** module is set to **default** and you click **Run**, the UI will display **default**. When the target for the **entry** module is set to **custom** and you click **Run**, the UI will display **custom**.

## Defining Resources for Targets

As different targets may use different resources, you can customize target-specific resource directories. The customizable directories depend on the project type. For an ArkTS project, the customizable directory is **resource** under **main**. For a JS project, the customizable directories are **resource** under **main** and **res** under an ability directory. The following uses an ArkTS project as an example.

{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": \[ 
    { 
      "name": "default", 
      "source": { 
        "pages": \[ 
          "pages/Index" 
        \] 
      }, 
      "resource": {  // Customize the resource directories for the default target.
        "directories": \[ 
          "./src/main/resources\_default" 
        \] 
      } 
    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": \[ 
          "phone" 
        \] 
      }, 
      "source": {   
        "pages": \[ 
          "pages/Index", 
          "pages/Page1" 
        \] 
      }, 
      "resource": {  // Customize the resource directories for the free target.
        "directories": \[ 
          "./src/main/resources\_free",
          "./src/main/resources\_default"
        \] 
      } 
    }, 
    { 
      "name": "pay", 
      "config": { 
        "deviceType": \[ 
          "phone" 
        \] 
      }, 
      "source": {   
        "pages": \[ 
          "pages/Index", 
          "pages/Page2" 
        \] 
      }, 
      "resource": {  // Customize the resource directories for the pay target.
        "directories": \[ 
          "./src/main/resources\_pay",
          "./src/main/resources\_default"
        \] 
      } 
    } 
  \] 
}

During the compilation and build process, resource files follow the priority order below:

-   Resource files in the **AppScope** directory are merged into the resource directory at the corresponding path in the module. If files with the same name exist in both directories, the resource files from the **AppScope** directory override those in the module after compilation and packaging.
-   If multiple resource directories referenced by a target contain files with the same name, the resources are used based on the sequence in which the directories are configured. For example, in the resource directories (**resources\_pay** and **resources\_default**) of the **pay** target, if resources with the same name exist, the one in the **resources\_pay** directory is used and packaged to the HAP.

## Defining the Icon, Label, and Launch Type for a Product

For each target's ability, you can customize the icon, label, and launch type. If they are not defined, the target will adopt the icon and label configured in the **module.json5** file under **module.abilities**, and the launch type will default to **singleton**. The following is an example:

{ 
   "apiType": 'stageMode', 
   "buildOption": { 
   }, 
   "targets": \[ 
     { 
       "name": "default", 
       "source": {
        "abilities": \[
          {
            "name": "EntryAbility",
            "icon":"$media:layered\_image",
            "label":"$string:EntryAbility\_label",
            "launchType": "singleton"
          }
        \]
      }
     }, 
     { 
       "name": "free", 
       "source": {
        "abilities": \[
          {
            "name": "EntryAbility",
            "icon":"$media:layered\_image",
            "label":"$string:EntryAbility\_label",
            "launchType": "multiton"
          }
        \]
      }
     }
   \] 
 }

## Defining .so File Dependencies for Targets in a C++ Project

In a C++ project, you can define the .so files on which a target depends. In the following example, a module depends on the **function1.so**, **function2.so**, and **function3.so** files, the **default** target depends on the **function1.so** and **function2.so** files, and the **vip** target depends on **function1.so** and **function3.so** files.

{
  "apiType": 'stageMode',
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": \[\],
      "abiFilters": \[
        "arm64-v8a",
        "x86\_64"
      \],
      "cppFlags": "",
    }
  },
  "targets": \[  // Define different targets.
    {
      "name": "default",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              // Pack the function1.so file with the highest priority.
              "pickFirsts": \[
                "\*\*/function1.so"
              \],
              // Exclude the function3.so file so it is not packed.
              "excludes": \[
                "\*\*/function3.so"
              \],
            // Allow the resource in the .so file with a higher priority to overwrite the .so file with a lower priority when the resources have the same name.
              "enableOverride": true
            }
          }
        }
      }
    },
    {
      "name": "vip",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              // Pack the function1.so file with the highest priority.
              "pickFirsts": \[
                "\*\*/function1.so"
              \],
            // Exclude the function2.so file so it is not packed.
              "excludes": \[
                "\*\*/function2.so"
              \],
            // Allow the resource in the .so file with a higher priority to overwrite the .so file with a lower priority when the resources have the same name.
              "enableOverride": true
            }
          }
        }
      }
    }
  \]
}

#### Customizing Multi-Target Builds

You can define targets for a HAR in its **build-profile.json5** file, differentiating these targets by the following factors: device type (**deviceType**), resource (**resource**), **buildOption** configuration (such as .so dependencies of C++, obfuscation configurations, ABI types, and **cppFlags**), and source set (**source**).

In versions earlier than DevEco Studio 6.0.2 Beta1, only the default target is supported when you build a HAR module in DevEco Studio. To specify a different target, use the CLI.

For example, to build a HAR with a custom target named **free**, you can run the following command:

hvigorw --mode module -p product=default -p module=library@free -p buildMode=debug assembleHar

Since DevEco Studio 6.0.2 Beta1, you can now select the target for a HAR module directly in DevEco Studio. The selected target only takes effect when the HAR package is built independently. If a HAP or an HSP is built, the target of the dependent HAR will be dynamically calculated. For details, see [Understanding Multi-Product Build Targets](#section7121513141619).

## Defining Device Types for Targets

You can define the **deviceType** field for a target to specify the supported device types. If this field is not defined, a target supports all the device types defined in **module.json5** or [config.json](../../../../getting-started/development-fundamentals/application-configuration-files-in-fa-model/application-configuration-files-fa-model/document.md).

The device types specified for a target can be some or all of those defined in **module.json5** or **config.json**. For example, in the preceding defined targets, the **default** target supports all device types, and the **free** target supports only 2-in-1 devices.

{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": \[ 
    { 
      "name": "default"  // deviceType is not defined. In this case, the target supports all device types defined in config.json or module.json5.
    }, 
    { 
      "name": "free",
      "config": { 
        "deviceType": \[  // The free target supports only 2-in-1 devices.
          "2in1" 
        \] 
      } 
    }
  \] 
}

## Defining .so File Dependencies for Targets in a C++ Project

In a C++ project, you can define the .so files on which a target depends. In the following example, a module depends on the **function1.so**, **function2.so**, and **function3.so** files, the **default** target depends on the **function1.so** and **function2.so** files, and the **vip** target depends on **function1.so** and **function3.so** files.

{
  "apiType": 'stageMode',
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": \[\],
      "abiFilters": \[
        "arm64-v8a",
        "x86\_64"
      \],
      "cppFlags": "",
    }
  },
  "targets": \[  // Define different targets.
    {
      "name": "default",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              // Pack the function1.so file with the highest priority.
              "pickFirsts": \[
                "\*\*/function1.so"
              \],
              // Exclude the function3.so file so it is not packed.
              "excludes": \[
                "\*\*/function3.so"
              \],
            // Allow the resource in the .so file with a higher priority to overwrite the .so file with a lower priority when the resources have the same name.
              "enableOverride": true
            }
          }
        }
      }
    },
    {
      "name": "vip",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              // Pack the function1.so file with the highest priority.
              "pickFirsts": \[
                "\*\*/function1.so"
              \],
            // Exclude the function2.so file so it is not packed.
              "excludes": \[
                "\*\*/function2.so"
              \],
            // Allow the resource in the .so file with a higher priority to overwrite the .so file with a lower priority when the resources have the same name.
              "enableOverride": true
            }
          }
        }
      }
    }
  \]
}

## Defining Resources for Targets

As different targets may use different resources, you can customize target-specific resource directories. The customizable directories depend on the project type. For an ArkTS project, the customizable directory is **resource** under **main**. For a JS project, the customizable directories are **resource** under **main** and **res** under an ability directory. The following uses an ArkTS project as an example.

{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": \[ 
    { 
      "name": "default",
      "resource": {  // Customize the resource directories for the default target.
        "directories": \[ 
          "./src/main/resources\_default" 
        \] 
      } 
    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": \[ 
          "2in1" 
        \] 
      }, 
      "resource": {  // Customize the resource directories for the free target.
        "directories": \[ 
          "./src/main/resources\_free",
          "./src/main/resources\_default"
        \] 
      } 
    },
  \] 
}

## Defining Source Code Files for Targets: sourceRoots

For details, see [Defining Source Code Files for Targets: sourceRoots](#section18668905913).

#### Customizing Multi-Product Builds

You can customize different products to create App Packs that meet different release purposes. These products can be differentiated by the bundle name, bundle type, signature information, icon, label, and target.

**Defining products**

First things first: Plan names for your products, for example, **productA** and **productB**. The following is an example of the project-level **build-profile.json5** file.

When customizing products, make sure the **default** product exists. Otherwise, an error will occur at compile time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/z_DCpBT6QOqre4t_6-7aiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42769EFF2264377BC340728A2E2E43C400233667CB15CBE1C5FCA9D3BDAA8634)

In the compilation and build process, both the **default** product and **default** target serve as fallback mechanisms. The **default** target is optional. When a module omits its **default** target, Hvigor automatically adds a **default** target and attaches it to the **default** product. Therefore, building the **default** product will inherently build the **default** target. If you need to avoid building the **default** target, define a custom **product** with explicitly specified targets instead. For details, see [Defining Targets for Products](#section7613106105114).

"app": { 
  "signingConfigs": \[\], 
  "products": \[ 
    { 
      "name": "default", 
      "signingConfig": "default", 
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
    }, 
    { 
      "name": "productA", 
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
    }, 
    { 
      "name": "productB", 
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
    } 
  \], 
  "buildModeSet": \[ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  \] 
}

## Defining a Product's Package Name and Vendor Name

You can specify the package name and vendor name for each product.

{ 
  "app": { 
    "signingConfigs": \[\], 
    "products": \[ 
      { 
        "name": "default", 
        "signingConfig": "default", 
        "compatibleSdkVersion": "6.0.2(22)", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputName-1.0.0"  // The product name is customizedProductOutputName-1.0.0.
        }, 
        "vendor": "customizedProductVendorName"   // The vendor name is set to customizedProductVendorName.
      }, 
      { 
        "name": "productA", 
        "compatibleSdkVersion": "6.0.2(22)", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputNameA-1.0.0"  // The product name is customizedProductOutputNameA-1.0.0.
        }, 
        "vendor": "customizedProductVendorNameA"   // The vendor name is set to customizedProductVendorNameA.
      }, 
      { 
        "name": "productB", 
        "compatibleSdkVersion": "6.0.2(22)", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputNameB-1.0.0" // The product name is customizedProductOutputNameB-1.0.0.
        }, 
        "vendor": "customizedProductVendorNameB"   // The vendor name is set to customizedProductVendorNameB.
      } 
    \], 
    "buildModeSet": \[ 
      { 
        "name": "debug", 
      }, 
      { 
        "name": "release" 
      } 
    \] 
  }, 
}

If a signature has been configured, the App Pack name of a product is the customized product name. Otherwise, it is the customized product name appended with "unsigned."

## Defining Bundle Names for Products

You can define a bundle name for each product. If no custom bundle name is defined, a product uses the default bundle name of the project. The following is an example:

"app": { 
  "signingConfigs": \[\], 
  "products": \[ 
    { 
      "name": "default", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com"  // Define the bundle name for product default.
    }, 
    { 
      "name": "productA", 
      "signingConfig": "default", 
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com"  // Define the bundle name for productA.
    }, 
    { 
      "name": "productB", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com"  // Define the bundle name for productB.
    } 
  \], 
  "buildModeSet": \[ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  \] 
}

## Defining Bundle Types for Products

You can define the **bundleType** field for each product to specify its type, which can be either of the following:

-   **app**: The product is an app.
-   **atomicService**: The product is an atomic service.

If **bundleType** is not defined, a product is of the type specified for the project when it was created. The following is an example:

"app": { 
  "signingConfigs": \[\], 
  "products": \[ 
    { 
      "name": "default", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com",   
      "bundleType": "app" // Define the bundle type for product default.
    },
    { 
      "name": "productA", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com",    
      "bundleType": "atomicService"  // Define the bundle type for product productA.
    },
    { 
      "name": "productB", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com",    
      "bundleType": "atomicService"  // Define the bundle type for product productB.
    } 
  \], 
  "buildModeSet": \[ 
    { 
      "name": "debug", 
    },
    { 
      "name": "release"
    } 
  \] 
}

## Defining Signature Information for Products

A signature file can be defined for each product. If no signature file is defined, the App Pack to generate for the product will be unsigned.

In general cases, you need to configure the signature information on the signature configuration page or in the **build-profile.json5** file of the project. For example, from the **File** > **Project Structure** > **Project** > **Signing Configs** page, configure signature information for products **default**, **productA**, and **productB**, as shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/3uyblqYkTBabUBaSdFoDKg/en-us_image_0000002532670331.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0956F2829F0510A35E9C818C829381DA3C8F6CD7AD9701CA2F65567DF910FCA)

After the signature information is configured, add the signature file for each product.

You can also define a signature file for a product in advance and then sign the product on the signature configuration page. In taking this approach, make sure the signature file used for signing is the same as the one predefined.

"app": { 
  "signingConfigs": \[\], // After the signature information is configured from the GUI, the corresponding signature configuration is automatically generated here. It is omitted in this example for simplicity.
  "products": \[ 
    { 
      "name": "default", 
      "signingConfig": "default", // Define the signature file for product default.
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com"  
    }, 
    { 
      "name": "productA", 
      "signingConfig": "productA", // Define the signature file for product productA.
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com"  
    }, 
    { 
      "name": "productB", 
      "signingConfig": "productB", // Define the signature file for product productB.
      "compatibleSdkVersion": "6.0.2(22)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com" 
    } 
  \], 
  "buildModeSet": \[ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  \] 
}

## Defining Icons and Labels for Products

You can define an icon and label for each product. If no custom icon or label is defined, a product uses the default ones of the project. The following is an example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/py6VBhR9SF2inQpBudoleQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=224852BB38869C359EC2EE0B2ABC5A6861147CA942BB70C0B2A8FF84A563BCE0)

During builds, the **icon** and **label** settings in **products** replace the corresponding settings in the [app.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md) file. These fields can be configured in both **app.json5** and **module.json5** files. For details about the priorities, see [Configuration Priority and Build Policy](../../../../getting-started/development-fundamentals/typical-scenarios-development/configuring-an-application-icon-and-label/document.md#configuration-priority-and-build-policy) .

{
  "app": {
    "signingConfigs": \[\],
    "products": \[
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:default\_icon", // Define the icon for product default.
        "label":"$string:default\_name", // Define the label for product default.
      },
      {
        "name": "productA",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "icon":"$media:productA\_icon", // Define the icon for product productA.
        "label":"$string:productA\_name", // Define the label for product productA.
      },
      {
        "name": "productB",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:productB\_icon", // Define the icon for product productB.
        "label":"$string:productB\_name",  // Define the label for product productB.
      }
    \],
    "buildModeSet": \[
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    \]
  },
  ...
}

## Defining Targets for Products

You can specify one or more targets for each product so that these targets are packed into the product.

Each target can be packed into one or more products. Yet, be mindful that different targets of the same module cannot be packed into the same product, unless these targets are configured with different device types or distribution rules.

In the following example, the previously defined targets are set for products as follows: The **default** target is packed into product **default**, the **free** target is packed into product **productA**, and the **pay** target is packed into product **productB**.

{ 
  "app": { 
  "signingConfigs": \[\], // After the signature information is configured from the GUI, the corresponding signature configuration is automatically generated here. It is omitted in this example for simplicity.
    "products": \[ 
      { 
        "name": "default", 
        "signingConfig": "default",
        "compatibleSdkVersion": "6.0.2(22)", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example00.com"  
      }, 
      { 
        "name": "productA", 
        "signingConfig": "productA",
        "compatibleSdkVersion": "6.0.2(22)", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example01.com"  
      }, 
      { 
        "name": "productB", 
        "signingConfig": "productB",  
        "compatibleSdkVersion": "6.0.2(22)", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example02.com" 
      } 
    \], 
  "modules": \[ 
    { 
      "name": "entry", 
      "srcPath": "./entry", 
      "targets": \[ 
        { 
          "name": "default",  // Pack the default target into product default.
          "applyToProducts": \[ 
            "default" 
          \] 
        }, 
        { 
          "name": "free",  // Pack the free target into product productA.
          "applyToProducts": \[ 
            "productA" 
          \] 
        }, 
        { 
          "name": "pay",  // Pack the pay target into product productB.
          "applyToProducts": \[ 
            "productB" 
          \] 
        } 
      \] 
    } 
  \] 
}

#### Building a HAP and App Pack

A target is mapped to a HAP, and a product is mapped to an App Pack. If there are multiple products or targets, you can specify which product and target are to be built.

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/MoCvFPItQvGZYRRflfEVnQ/en-us_image_0000002501070252.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAE423C5C832EE6E0DEE9CEF7A25B4F2F0509B293FEC067CB064CA1779F2561B) in the upper right corner, specify the product and target to be packaged, and click **Apply**. For example, select the **free** target of the entry module in product **ProductA**.

-   **Product**: product to be built.
-   **Build Mode**: [build mode](../../../customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916).
-   **Product Info**: bundle name and signature information.
-   **Target Select**: target of each module. A target can be selected only when it is included in the defined product. If no target is available, "No Target to apply" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/dkRZm9shQfeG5M63wj-IrA/en-us_image_0000002532670325.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74AB1897AACC3EB971B1BD5A6E4768A89E41D6AD44D0AD44CABDD32852D86F7C)

Execute the build task:

-   To build an App Pack, choose **Build** > **Build Hap(s)/APP(s)** > **Build APP(s)** on the menu bar. In this example, based on the [configuration file](#section7613106105114) and preceding settings, DevEco Studio builds and generates an APP Pack for ProductA, but not for products **default** and **ProductB**.
-   To build HAPs for all targets of a product, choose **Build** > **Build Hap(s)/APP(s)** > **Build Hap(s)** on the menu bar.

To build a HAP for a specific target of a module, click the module name in the project directory, and then choose **Build** > **Make Module'_Module name_'**. In this example, based on the preceding settings, DevEco Studio builds and generates a HAP for the **free** target of the entry module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/1PTvXVTAQ4aIkYof1kXoQg/en-us_image_0000002532670323.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CCA6787CED5635D5538FE35C1DEFA7F94BFC83C0EC7A8DB7D12A01D1596E9B2)

#### Debugging and Running a Target

To debug and run a target, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/4B8k487vQo-T2pZGYd8tgw/en-us_image_0000002532670327.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=090FA51E8C47931444602FEBD6149CEC1F7AED12E346EC6C10E7D1750A559FB0) in the upper right corner, select an option for **Module Target** of the selected product, and click **Apply**. Note that only one target can be run and debugged per module at any given time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EbkHrJF7S2K38NVyQttwow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B2FB8226599DAD45A3BF06962D4C4271F35DEC9F2A91351CB713BD5FA50EBE6)

For the selected targets to be debugged and run successfully, be sure to select only those that belong to the selected product.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/eDYrmh3ITP6pSmEsJR5Cgg/en-us_image_0000002501070254.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8594427433C057820C112F747CC772DE947D8B87909B0E3D828C53FAC1C38091)

#### Understanding Multi-Product Build Targets

-   align target
    
    The align target is the highest priority target in the build process. Once set for a project, it is automatically selected for building if it exists in the target module. The align target applies to the entire project; only one can be configured, through the CLI or the configuration file.
    
    -   Example of configuring an align target through the CLI:
        
        hvigorw -c properties.ohos.align.target=target1 assembleHap
        
    
    -   Example of configuring an align target through the **hvigor-config.json5** configuration file:
        
        "properties": {
          'ohos.align.target': 'target1'
        },
        

-   fallback target
    
    The fallback target is used for building when a specified target is not found for a module. If it is not set, the default target is used by default. One or more fallback targets can be configured, and they apply to the entire project. If an array of fallback targets are configured, the one that matches first in the array takes effect.
    
    -   Example of configuring a fallback target through the CLI:
        
        hvigorw -c properties.ohos.fallback.target=target1,target2 assembleHap
        
    
    -   Example of configuring a fallback target through the **hvigor-config.json5** configuration file:
        
        "properties": {
          'ohos.fallback.target': \['target1', 'target2'\]
        }
        

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/fVidjiwpRvKK53kvIoaffQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94DEDCA804852D2D850D852DAA216CB42EBA85AD7C47732B0AA22CAD50D95906)

-   For both the align target and fallback target, CLI configuration takes precedence over the configuration file.

-   The align target and fallback target configured through the configuration file work with the DevEco Studio **Build** menu, but not the **Run** menu. To debug them, use the [hdc command line tool](../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md) instead.

The priority order of targets is as follows: align target > CLI-specified module target > dependent parent module target > fallback target > default target.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/P-BzElEcQHyUxM_o7n3TRQ/en-us_image_0000002532750281.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=859B13BE7FA3EA56E0D2A17AE848D22C90B0DDF52B12EBDF00115F14534D880D)

Example:

Suppose a project dependency chain is entry -> lib1 -> lib2, and you need to build multiple products A, B, C, with the target configurations in the project as follows:

entry: A, B, default

lib1: B, C, default

lib2: A, C, default

If you specify the align target as A and the fallback target as C, then, the build command for the HAP is:

hvigorw --mode module -p module=entry -c properties.ohos.align.target=A -c properties.ohos.fallback.target=C assembleHap

The target selection for the build is as follows: entry@A, lib1@C, lib2@A.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/sJnUp10KRyKz2cwoTHth4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A051766A7A46151DE2828283B4F4F589C426AB3DEDD0A842B169F0F9EF08A72)

The preceding descriptions apply only to the non-ohosTest mode. In ohosTest mode, the target for dependencies is fixed at **default**, and other targets are not effective.
