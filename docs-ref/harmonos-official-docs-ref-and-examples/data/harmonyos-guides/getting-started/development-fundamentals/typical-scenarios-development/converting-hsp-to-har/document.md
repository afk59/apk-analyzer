# Converting HSP to HAR

The HSP has requirements on the consistency of bundle names and signatures. Installing an HSP file in the debugging phase may cause many integration issues during multi-module development. In this case, you are advised to use the HAR file instead. This topic describes how to convert an HSP project to an HAR project by changing the configuration items.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/GPRegM4wS0y2rHHg31DPyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B70AF8E9D1F3520A2CB336DA65133E64252AB2D0361CBA0BAC58E07F8E4EE0A9)

Before reading this topic, you should learn the following concepts first: [HSP](../../application-package-fundamentals/application-package-development-and-usage/hsp/document.md), [HAR](../../application-package-fundamentals/application-package-development-and-usage/har/document.md), [module.json5](../../application-configuration-files-in-stage-model/module-json5-configuration-file/document.md), [hvigorfile.ts](../../../../building-an-app/customizing-your-build/dynamically-modifying-the-build-configuration/introduction/document.md), [oh-package.json5](../../../../command-line-tools/using-ohpm/oh-package-json5/document.md), and [build-profile.json5](../../../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md).

There are differences when some components and modules are integrated and used in the HAP, HSP, and HAR. For example, separate constraints are provided on loading the Worker thread file in the HAR compared with that in the HSP. For details, see [Precautions for File URLs](../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md#precautions-for-file-urls). Therefore, after HSP is converted to HAR by performing the following steps, pay attention to the corresponding components and modules and perform adaptation.

#### How to Convert

1.  In the **module.json5** file of the HSP module, change the value of the **type** field to **har** and delete the **deliveryWithInstall** and **pages** fields.
    
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
    
2.  Delete the **main\_pages.json** file from the **resource\\base\\profile** folder.
    
3.  Replace the content in the **hvigorfile.ts** file of the HSP module with the following:
    
    // MyApplication\\library\\hvigorfile.ts
    import { harTasks } from '@ohos/hvigor-ohos-plugin';
    
    export default {
      system: harTasks,  // Change this field to harTasks.
      plugins:\[\]
    }
    
4.  Delete the **packageType** configuration from the **oh-package.json5** file.
    
5.  Delete **targets** from the HSP configuration of the **modules** module in the project-level **build-profile.json5** configuration file.
