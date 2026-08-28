# Converting HAP to HAR

HAR allows you to export APIs or ArkUI components from a module and share the module as a second-party or third-party library with other modules or applications, while HAP does not. This topic will walk you through how to convert a HAP project to a HAR project by modifying configuration items.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/kbqXFAGpRxa28Ztp1nLC9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62F8EF627C1125C91A33000459E7067C4EEBD89A39D04A280D6F6813F564421B)

There are differences when some components and modules are integrated and used in the HAP, HSP, and HAR. For example, separate constraints are provided on loading the Worker thread file in the HAR compared with that in the HSP. For details, see [Precautions for File URLs](../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md#precautions-for-file-urls). Therefore, after HAP is converted to HAR by performing the following steps, pay attention to the corresponding components and modules and perform adaptation.

#### How to Convert

1.  Modify the [module.json5](../../application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file in the HAP module as follows:
    
    -   Change the value of **type** to **har**, and delete the **mainElement**, **deliveryWithInstall**, **installationFree**, and **pages** tags.
    -   Prior to API version 17, HARs do not support the creation of any ExtensionAbility. Starting from API version 18, HARs support only [two specific types of ExtensionAbility](../../../../environment-setup/creating-a-project/managing-modules/adding-an-ability-to-a-module/document.md#section18891639459). Therefore, for HARs used in either API version 17 or earlier, or API version 18 or later without the two supported ExtensionAbilities configured, you should delete the **extensionAbilities** tag and either delete the associated ExtensionAbility components or migrate them to another HAP module.
    -   UIAbility is not supported by the HAR module in API version 13 or earlier. Therefore, you need to delete the **abilities** tag and delete the associated UIAbility component or migrate it to the HAP module.
    
    {
      "module": {
        "name": "har",
        "type": "har",
        "deviceTypes": \[
          "tablet",
          "2in1"
        \]
      }
    }
    
2.  Delete the **main\_pages.json** file from the **src\\main\\resource\\base\\profile** folder of the HAP module.
    
3.  Replace the content in the **hvigorfile.ts** file of the HAP module with the following:
    
    import { harTasks } from '@ohos/hvigor-ohos-plugin';
    
    export default {
      system: harTasks,  // Change the value to the HAR task.
      plugins:\[\]
    }
    
4.  Create an **Index.ets** file in the root directory of the HAP module, and set the file in the **main** tag of the **oh-package.json5** file. The **Index.ets** file is used to export ArkUI components or APIs. For details, see [Developing a HAR](../../application-package-fundamentals/application-package-development-and-usage/har/document.md#developing-a-har).
    
    {
      // ...
      "main": "Index.ets",
      // ...
    }
    
5.  In the project-level configuration file [build-profile.json5](../../../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md), delete **targets** of the HAP under the **modules** tag.
