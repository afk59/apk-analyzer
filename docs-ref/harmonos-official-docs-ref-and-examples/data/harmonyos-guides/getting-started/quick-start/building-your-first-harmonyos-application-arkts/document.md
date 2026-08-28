# Building Your First HarmonyOS Application (ArkTS)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/89FCrJ1DTUSHDvCUdOr0iw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3863FD88AE641D3E90C1D088A1A7148621103853AFE9222F18A9DF04B9E76E3C)

To ensure optimal results, this guide uses **[the latest version of DevEco Studio](https://developer.huawei.com/consumer/en/download/)** as an example.

#### Creating an ArkTS Project

1.  If you are opening DevEco Studio for the first time, click **Create Project**. If a project is already open, choose **File** > **New** > **Create Project** from the menu bar.
2.  On the **Choose Your Ability Template** page, select **Application** (or [Atomic Service](../../harmonyos-terms/document.md#section10825114113817), depending on your project), select **Empty Ability** as the template, and click **Next**.
    
    To develop a native project, select the **Native C++** template. For details about how to use other templates, see [Introduction to Project Templates](../../../environment-setup/creating-a-project/introduction-to-project-templates/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/GXxUC13wR9ai9U8xxYRiWQ/en-us_image_0000002497900180.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A14867BEEE2EEE0AFBAC6CBA338DE5664FFC82335A1822E47CCD90C1F2BF4ACB "Click to enlarge")
    
3.  On the **Create Project** page, choose **6.0.1(21)** as an example of **Compatible SDK**, which specifies the earliest compatible API version. Retain the default values for other parameters.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/oirDEQhLQmu-BXluc0f6Yg/en-us_image_0000002529700141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91C89834E9526950EE12D693E7D07F858FF9ACA073BAB6B387FE3BE32F348B91 "Click to enlarge")
    
4.  Click **Finish**. DevEco Studio will automatically generate the sample code and resources that match your project type. Wait until the project is created.

#### ArkTS Project Directory Structure (Stage Model)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/cRUFxo7sRNWyQyIrjjyC5g/en-us_image_0000002529700143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8E1D92D76C2560E595BC2C30D67555AEDD5DE60102AEAF16DDFCC0E2F3FEDC3 "Click to enlarge")

-   **AppScope > app.json5**: global configuration of your application. For details, see [app.json5 Configuration File](../../development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md).
-   **entry**: HarmonyOS project module, which can be built into a Harmony Ability Package ([HAP](../../development-fundamentals/application-package-glossary/document.md#hap)).
    
    -   **src > main > ets**: a collection of ArkTS source code.
    -   **src > main > ets > entryability**: entry to your application/service.
    -   **src > main > ets > entrybackupability**: the capability to back up and restore data.
    -   **src > main > ets > pages**: a collection of pages contained in your application/service.
    -   **src > main > resources**: a collection of resource files used by your application/service, such as graphics, media, strings, and layout files. For details about resource files, see [Resource Categories and Access](../../resource-categories-and-access/document.md).
    -   **src > main > module.json5**: [module](../../development-fundamentals/application-package-glossary/document.md#module) configuration file. This file describes the global configuration information of the application/service, the device-specific configuration information, and the configuration information of the HAP file. For details about the configuration file, see [module.json5 Configuration File](../../development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    -   **build-profile.json5**: current module information and build configuration options, including **buildOption** and **targets**.
    -   **hvigorfile.ts**: module-level build script.
    -   **obfuscation-rules.txt**: obfuscation rule file. When obfuscation is enabled, the code will be compiled, obfuscated, and compressed during builds in release mode. For details, see [Using Obfuscation for Code Hardening](../../../building-an-app/using-obfuscation-for-code-hardening/document.md).
    -   **oh-package.json5**: describes the bundle name, version, entry file (type declaration file), and dependencies.
    
-   **oh\_modules**: third-party library dependency information.
-   **build-profile.json5**: project-level configuration information, including **signingConfigs** and **products**. Under **products**, you can configure the current operating environment, with HarmonyOS as the default.
    
-   **hvigorfile.ts**: project-level build script.
    
-   **oh-package.json5**: global configuration, including **overrides**, **overrideDependencyMap**, and **parameterFile**.

#### Building the First Page

1.  Use the **Text** component.
    
    After the project synchronization is complete, in the **Project** window, choose **entry** > **src** > **main** > **ets** > **pages** to open the **Index.ets** file, and change the page layout from relative layout (**RelativeContainer**) to linear layout (**Row**/**Column**).
    
    In this application, texts and buttons are used to implement page redirection and return. You can use the [Row](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-row) and [Column](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-column) components to set up the page layout. For scenarios with more complex element alignment, you can use the [RelativeContainer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-relativecontainer) component to set up the layout. For details about UI layout selection and usage, see [Layout Selection](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/component-layouts/layout-overview/document.md#layout-selection).
    
    The sample code in the **Index.ets** file is shown below:
    
    // Index.ets
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
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
    
2.  Add a **Button** component.
    
    On the default page, add a **Button** component to respond to the **onClick** events and implement redirection to another page. The sample code in the **Index.ets** file is shown below:
    
    // Index.ets
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
            // Add a button to respond to the onClick events.
            Button() {
              Text('Next')
                .fontSize(30)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({
              top: 20
            })
            .backgroundColor('#0D9FFB')
            .width('40%')
            .height('5%')
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
3.  On the toolbar in the upper right corner of the editing window, click **Previewer**. Below is how the first page looks in the Previewer.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/t0vORPzBQtWXhcYcPX8X8g/en-us_image_0000002497900182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53118641BB9C027E81D40A8F37A2DED3445B72180022DCF00602D241BF4EB1B1)
    

#### Building the Second Page

1.  Create the second page.
    
    -   Creating the second page file: In the **Project** window, choose **entry > src > main > ets**, right-click the **pages** folder, choose **New > ArkTS File** from the shortcut menu, name the page **Second**, and press **Enter**. Below shows the created page in the **pages** folder.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/dLzqFL7UTQ-q9ukJyZE9yA/en-us_image_0000002497900176.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3C9B0FAC7516D2E3023175323ADE67865161D9501EA5F3432A8B212EC7BEF0E)
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/LJmNlQUpRyKwqn67q9Agqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA266BF43A0CACF01DE59AE4ADE322C3822BA5A937E0F60F2A5924D7DD2D867C)
        
        You can also right-click the **pages** folder, choose **New** > **Page** > **Empty Page**, name the page **Second**, and click **Finish**. In this way, there is no need to manually configure the route for the second page (described below).
        
    -   Configuring the route for the second page: In the **Project** window, choose **entry** > **src** > **main** > **resources** > **base** > **profile**. In the **main\_pages.json** file, set **pages/Second** under **src**. The sample code is as follows:
        
        {
          "src": \[
            "pages/Index",
            "pages/Second"
          \]
        }
        
    
2.  Add **Text** and **Button** components.
    
    Add **Text** and **Button** components and set their styles, as you do for the first page. The sample code in the **Second.ets** file is shown below:
    
    // Second.ets
    @Entry
    @Component
    struct Second {
      @State message: string = 'Hi there';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
            Button() {
              Text('Back')
                .fontSize(30)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({
              top: 20
            })
            .backgroundColor('#0D9FFB')
            .width('40%')
            .height('5%')
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

#### Implementing Page Redirection

You can implement page redirection through the [page router](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/page-routing-ohos-router-not-recommended/document.md), which finds the target page based on the page URL.

[Navigation](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md) is recommended if you want to achieve better transition effects.

1.  Implement redirection from the first page to the second page.
    
    In the **Index.ets** file of the first page, bind the **onClick** event to the **Next** button so that clicking this button redirects the user to the second page. The sample code in the **Index.ets** file is shown below:
    
    // Index.ets
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
            // Add a button to respond to the onClick events.
            Button() {
              Text('Next')
                .fontSize(30)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({
              top: 20
            })
            .backgroundColor('#0D9FFB')
            .width('40%')
            .height('5%')
            // Bind the onClick event to the Next button so that clicking the button redirects the user to the second page.
            .onClick(() => {
              console.info(\`Succeeded in clicking the 'Next' button.\`)
              // Obtain UIContext.
              let uiContext: UIContext = this.getUIContext();
              let router = uiContext.getRouter();
              // Redirect to the second page.
              router.pushUrl({ url: 'pages/Second' }).then(() => {
                console.info('Succeeded in jumping to the second page.')
    
              }).catch((err: BusinessError) => {
                console.error(\`Failed to jump to the second page. Code is ${err.code}, message is ${err.message}\`)
              })
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
2.  Implement redirection from the second page to the first page.
    
    In the **Second.ets** file of the second page, bind the **onClick** event to the **Back** button so that clicking this button redirects the user back to the first page. The sample code in the **Second.ets** file is shown below:
    
    // Second.ets
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Second {
      @State message: string = 'Hi there';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
            Button() {
              Text('Back')
                .fontSize(30)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({
              top: 20
            })
            .backgroundColor('#0D9FFB')
            .width('40%')
            .height('5%')
            // Bind the onClick event to the Back button so that clicking the button redirects the user back to the first page.
            .onClick(() => {
              console.info(\`Succeeded in clicking the 'Back' button.\`)
              // Obtain UIContext.
              let uiContext: UIContext = this.getUIContext();
              let router = uiContext.getRouter();
              try {
                // Return to the first page.
                router.back()
                console.info('Succeeded in returning to the first page.')
              } catch (err) {
                let code = (err as BusinessError).code; 
                let message = (err as BusinessError).message; 
                console.error(\`Failed to return to the first page. Code is ${code}, message is ${message}\`)
              }
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
3.  Open the **Index.ets** file and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/B67Ld6cAQNqtsOlEEKoZXA/en-us_image_0000002497740214.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A082ACF195796154D50CE783DCCC1408AF78230B7CADF0263268E64C8D0385F0) in the Previewer to refresh the UI. The figure below shows the effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/e9Mz5KX9QIy4H_Ni_gMDKA/en-us_image_0000002529580177.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E2EAC8FA4AA407F287883F0FCB05DE10C7939EC6DC702D26C5888D733E4970E)
    

#### Running the Application on a Real Device

1.  Connect a real device running HarmonyOS to your computer. For details, see [Running Your App on a Local Real Device](../../../coding-and-debugging/running-your-app-on-a-local-real-device/document.md).
2.  Choose **File** > **Project Structure...** > **Project** > **Signing Configs** and select **Automatically generate signature**. When prompted, click **Sign In**. Then the system will automatically sign your application/service. For details, see [Signing an App Not Associated with a Registered App](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section151231211105010). The figure shown below is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/CBq1rS5BQwW2Wbs8GD5qJw/en-us_image_0000002529700147.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=010FE640248E7D271415B5944E754215B115D684E29098211652163C9AE2AD82 "Click to enlarge")
    
3.  On the toolbar in the upper right corner of the editing window, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/jHlmz8VxTZmNCzMxFM8M9g/en-us_image_0000002497740216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9978A355AAA60D400101F4B303F9D0385B0518CF3E29EC17923FAFCD4BA7BDA1) to run the project. The figure below shows the effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/W_RrgXZ5RiKHVgORS22bCQ/en-us_image_0000002529580173.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26EEA063511A3E5BEF515FEE404FD146EB1233DAF785C630B8F091C53278B1DF "Click to enlarge")
    

Congratulations! You have successfully built your first HarmonyOS application based on ArkTS. Feel free to explore more HarmonyOS features!
