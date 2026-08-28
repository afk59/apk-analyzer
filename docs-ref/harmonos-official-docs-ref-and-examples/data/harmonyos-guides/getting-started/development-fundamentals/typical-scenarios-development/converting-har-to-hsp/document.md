# Converting HAR to HSP

Currently, the HAR has a problem with duplicate packaging, leading an oversize application package. To fix this problem, you can convert the HAR to the HSP by changing the configuration items.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/OgvVuPUhSBeKNd-0wyMcDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F1E47B1DB5B65CD9ADA57142ABB45E48D0FA75C006E81D77423C20393D5BE9E)

There are differences when some components and modules are integrated and used in the HAP, HSP, and HAR. For example, separate constraints are provided on loading the Worker thread file in the HAR compared with that in the HSP. For details, see [Precautions for File URLs](../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md#precautions-for-file-urls). Therefore, after HAR is converted to HSP by performing the following steps, pay attention to the corresponding components and modules and perform adaptation.

#### How to Convert

1.  Set **type** to **shared** and add the **deliveryWithInstall** and **pages** fields in the **module.json5** file of the HAR module.
    
    {
      "module": {
        // ...
        "type": "shared",
        "deliveryWithInstall": true,
        "pages": "$profile:main\_pages",
        // ...
      }
    }
    
2.  Create a **profile** folder in the **resources\\base** directory. Then add the **main\_pages.json** file to the created folder and configure it as follows:
    
    {
      "src": \[
        "pages/PageIndex"
      \]
    }
    
3.  Create a **pages** folder in the **ets** directory. Then add the **PageIndex.ets** file to the created folder and configure it as follows:
    
    @Entry
    @Component
    struct PageIndex {
      @State message: string = 'hello world';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
4.  Delete the **consumerFiles** field from the **build-profile.json5** file of the HAR module.
    
5.  Replace the content in the **hvigorfile.ts** file of the HAR module with the following content:
    
    // library\\hvigorfile.ts
    import { hspTasks } from '@ohos/hvigor-ohos-plugin';
    
    export default {
      system: hspTasks,  // Change the value to the HSP task.
      plugins:\[\]
    }
    
6.  Add the **packageType** field in the **oh-package.json5** file.
    
    {
      // ...
      "packageType": "InterfaceHar"
    }
    
7.  Add the **targets** tag to **build-profile.json5** > **modules** > **library** in the root directory of the project.
    
    "modules": \[
      // ...
      {
        "name": "library",
        "srcPath": "./library",
        "targets": \[
          {
            "name": "default",
            "applyToProducts": \[
              "default"
            \]
          }
        \]
      }
    \],
