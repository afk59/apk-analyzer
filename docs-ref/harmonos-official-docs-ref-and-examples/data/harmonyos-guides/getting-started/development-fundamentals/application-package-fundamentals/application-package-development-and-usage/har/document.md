# HAR

A Harmony Archive (HAR) is a static shared package that can contain code, C++ libraries, resource files, and configuration files (also called profiles). It enables modules and projects to share code of ArkUI components, resources, and more.

#### When to Use

-   Supports intra-application sharing or, after being released, intra-application sharing.
-   As a second-party library for internal applications, by being released to the [OHPM private repository](../../../../../environment-setup/creating-a-project/managing-modules/ohpm-repo-private-repository-setup-tool/document.md).
-   As a third-party library for external applications, by being released to the [OHPM central repository](https://ohpm.openharmony.cn/#/en/home).

#### Constraints

-   A HAR can only be referenced as a dependency of an application module. It cannot be installed or run independently on a device.
-   Since API version 14, the declaration of the [UIAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-overview/document.md) component in the configuration file is supported. For details about how to configure a **UIAbility**, see [Adding a UIAbility to a Module](../../../../../environment-setup/creating-a-project/managing-modules/adding-an-ability-to-a-module/document.md#section18658758104318). Starting a **UIAbility** in a HAR is the same as starting one [in an application](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/starting-uiability-within-the-same-application/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/g9iJ4Vp-SjKgUELXkF7S7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34D21F4BD8150B977F2731591D7F2663C30BEB20BA5E3AF74AFE0D692CDD422A)

If the [startAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability) API is used to start the **UIAbility** in the HAR, the value of **moduleName** in the API parameter must be the module name of the [HAP](../hap/document.md) or [HSP](../hsp/document.md) that depends on the HAR.

-   Since API version 18, HAR supports the declaration of the [ExtensionAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md) component in the configuration file. However, **ExtensionAbility** with entry capabilities (that is, **entity.system.home** and **ohos.want.action.home** configured for the **skill** tag) is not supported. For details about how to configure an **ExtensionAbility** in a HAR, see [Adding an ExtensionAbility to a Module](../../../../../environment-setup/creating-a-project/managing-modules/adding-an-ability-to-a-module/document.md#section18891639459). For API version 17 and earlier versions, the [ExtensionAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md) component cannot be declared in the configuration file.
-   A HAR does not support the declaration of the [pages](../../../application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#pages) tag in the configuration file. Still, it can include pages, which can be redirected through [Page Navigation](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md#routing-operations).
-   A HAR does not support referencing resources in the **AppScope** folder. This is because the content in the **AppScope** folder is not packaged into the HAR during building.
-   As the HSP supports only intra-application sharing, a HAR that depends on any HSP can be shared only within the same application. Do not release such a HAR to a second-party or third-party repository for other applications to use; otherwise, build failures will occur.
-   When multiple HAPs or HSPs reference the same HAR, the application package may contain multiple copies of code and resource files for the HAPs or HSPs, resulting in an unwelcome large package size.
-   A HAR can depend on other HARs or HSPs, but does not support cyclic dependency or dependency transfer.
-   When a HAP references a HAR, the system automatically combines their permission configurations during compilation and build. Therefore, you do not need to repeatedly request the same permission in the HAP and HAR.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/GeF_yt0xRxGWqi-4eZgFLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EEC7BAD0038532B2F4B4A7E8F23565DAA9B111F916C1CAFBD93FC0E475E5E08)

Cyclic dependency: For example, there are three HARs. HAR-A depends on HAR-B, HAR-B depends on HAR-C, and HAR-C depends on HAR-A.

Dependency transfer: For example, there are three HARs. HAR-A depends on HAR-B, and HAR-B depends on HAR-C. If dependency transfer is not supported, HAR-A can use the methods and components of HAR-B, but cannot directly use that of HAR-C.

#### Creating a HAR

You can create a HAR module for calling C++ code in DevEco Studio. During the creation, turn on **Enable native** on the **Configure New Module** page. For details, see [Creating a HAR Module](../../../../../environment-setup/creating-a-project/managing-modules/developing-and-publishing-shared-packages/developing-a-static-shared-package/document.md#section643521083015).

#### Developing a HAR

You can export the ArkUI components, APIs, and other resources of a HAR for other applications or intra-application modules to reference.

The **Index.ets** file acts as the entry of the HAR export declaration file and is where the HAR exports APIs. This file is automatically generated by DevEco Studio by default. You can specify another file as the entry declaration file in the **main** field in the **oh-package.json5** file of the module. The code snippet is as follows:

{
  // ...
  "main": "Index.ets",
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/PCXb_fTDQvWd8CC1vsV4SA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96F58D838B7C5ED968216AC6079FDDB5D8000871FCB9EB9440BC8A05283881CB)

When compiling together with the host application, the HAR code is directly compiled into the host application. A HAR package serves as an intermediate build product rather than a final runtime entity. At runtime, the HAR operates under the identity of its host application, and the system differentiates behaviors based on the version of the host application. If it is necessary to implement version-specific behaviors for the host application within the HAR, you can call the [getBundleInfoForSelf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself) API to obtain the host application's **targetVersion**, and then execute different logic based on the obtained **targetVersion**.

## Exporting ArkUI Components

Export ArkUI components using **export**. The code snippet is as follows:

// library/src/main/ets/components/mainpage/MainPage.ets
@Component
export struct MainPage {
  @State message: string = 'HAR MainPage';

  build() {
    Column() {
      Row() {
        Text(this.message)
          .fontSize(32)
          .fontWeight(FontWeight.Bold)
      }
      .margin({ top: '32px' })
      .height(56)
      .width('624px')

      Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center, alignContent: FlexAlign.Center }) {
        Column() {
          Image($r('app.media.pic\_empty')).width('33%')
          Text($r('app.string.empty'))
            .fontSize(14)
            .fontColor($r('app.color.text\_color'))
        }
      }.width('100%')
      .height('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor($r('app.color.page\_background'))
  }
}

In the **Index.ets** file, declare the APIs that the HAR exposes to external systems. The code snippet is as follows:

// library/Index.ets
export { MainPage } from './src/main/ets/components/mainpage/MainPage';

## Exporting Classes and Methods

Use **export** to export classes and methods. Multiple classes and methods can be exported. The code snippet is as follows:

// library/src/main/ets/test.ets
export class Log {
  static info(msg: string) {
    console.info(msg);
  }
}

export function func() {
  return 'har func';
}

export function func2() {
  return 'har func2';
}

In the **Index.ets** file, declare the APIs that the HAR exposes to external systems. The code snippet is as follows:

// library/Index.ets
export { Log, func, func2 } from './src/main/ets/test';

## Exporting Native Methods

The HAR can contain .so files written in C++. Native methods in the .so file can be exported from the HAR in the following way. In the example, the **add** API in the **liblibrary.so** file is exported.

// library/src/main/ets/utils/nativeTest.ets
import native from 'liblibrary.so';

export function nativeAdd(a: number, b: number): number {
  let result: number = native.add(a, b);
  return result;
}

In the **Index.ets** file, declare the APIs that the HAR exposes to external systems. The code snippet is as follows:

// library/Index.ets
export { nativeAdd } from './src/main/ets/utils/nativeTest';

## Exporting Resources

Specifically, DevEco Studio collects resource files from the HAP module and its dependent modules, and overwrites the resource files with the same name (if any) based on the following priorities (in descending order):

-   AppScope (supported only by the stage model)
-   Modules in the HAP
-   Dependent HAR modules
    
    If resource conflicts occur between dependent HAR modules, they are overwritten based on the dependency sequence indicated under **dependencies** in the **oh-package.json5** file. The module that is higher in the dependency sequence list has a higher priority. For example, in the following example, if **dayjs** and **lottie** folders contain files with the same name, resources in **dayjs** are used preferentially.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/rZFSsWsQSlCG4b7J2snO-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F86C04672A9DDB0FB6A039AC71BFB8C42181401EA9C45B4A77159528F5F09972)
    
    With regard to resources in the internationalization folder of **AppScope**, HAP, and HAR directories, the preceding priority rules also apply to resources with the same internationalization qualifier. In addition, resources with internationalization qualifiers are prioritized over those in the **base** folder. For example, if resources with the same name are configured in both the **base** folder under **AppScope** and the **en\_US** folder of a HAR, the one in the **en\_US** folder is prioritized for internationalization purposes.
    

{
  // ...
  "dependencies": {
    // ...
    "dayjs": "file:../dayjs",
    "lottie": "file:../lottie",
  },
}

#### Using a HAR

You can reference the ArkUI components, APIs, and resources in a HAR.

Before referencing the HAR, you need to configure the dependency on it. For details, see [Referencing a Shared Package](../../../../../environment-setup/creating-a-project/managing-modules/referencing-and-managing-a-shared-package/document.md).

## Referencing ArkUI Components

After configuring the dependency on the HAR, you can use **import** to import the ArkUI component exported from HAR. The following is an example:

// entry/src/main/ets/pages/IndexSec.ets
import { MainPage } from 'library';

@Entry
@Component
struct IndexSec {
  build() {
    Row() {
      // Reference the ArkUI component in the HAR.
      MainPage()
    }
    .height('100%')
  }
}

## Referencing ETS Classes and Methods

Use **import** to reference the classes and methods exported from the HAR. The code snippet is as follows:

// entry/src/main/ets/pages/Index.ets
import { Log, func } from 'library';
// ...
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Text(this.message)
        .fontFamily('HarmonyHeiTi')
        .fontWeight(FontWeight.Bold)
        .fontSize(32)

      // Reference ETS classes and methods.
      Button($r('app.string.button'))
        .id('button')
        .height(48)
        .width('624px')
        .margin({ top: '4%' })
        .type(ButtonType.Capsule)
        .onClick(() => {
          // Reference ETS classes and methods in the HAR.
          Log.info('har msg');
          this.message = 'func return: ' + func();
        })
      // ...

      // ...
    }
    .width('100%')
    .backgroundColor($r('app.color.page\_background'))
    .height('100%')
  }
}

## Referencing Native Methods

Use **import** to reference the native methods exported from the HAR. The code snippet is as follows:

// entry/src/main/ets/pages/Index.ets
import { nativeAdd } from 'library';
// ...
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Text(this.message)
        .fontFamily('HarmonyHeiTi')
        .fontWeight(FontWeight.Bold)
        .fontSize(32)

      // ...
      // Reference the native method in the HAR.
      Button($r('app.string.native\_add'))
        .id('nativeAdd')
        .height(48)
        .width('624px')
        .margin({ top: '4%', bottom: '6%' })
        .type(ButtonType.Capsule)
        .onClick(() => {
          this.message = 'result: ' + nativeAdd(1, 2);
        })

      // ...
    }
    .width('100%')
    .backgroundColor($r('app.color.page\_background'))
    .height('100%')
  }
}

## Referencing Resources

Use **$r** to reference resources in the HAR. For example, add the **name: hello\_har** string (defined in the **string.json** file) and **icon\_har.png** image to the **src/main/resources** directory of the HAR module, and then reference the string and image in the entry module. The code snippet is as follows:

// entry/src/main/ets/pages/Index.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Text(this.message)
        .fontFamily('HarmonyHeiTi')
        .fontWeight(FontWeight.Bold)
        .fontSize(32)

      // ...

      // Reference the string in the HAR.
      Text($r('app.string.hello\_har'))
        .id('stringHar')
        .fontFamily('HarmonyHeiTi')
        .fontColor($r('app.color.text\_color'))
        .fontSize(24)
        .fontWeight(500)
        .margin({ top: '40%' })

      List() {
        ListItem() {
          // Reference the image in the HAR.
          Image($r('app.media.icon\_har'))
            .id('iconHar')
            .borderRadius('48px')
        }
        .margin({ top: '5%' })
        .width('312px')
      }
      .alignListItem(ListItemAlign.Center)
    }
    .width('100%')
    .backgroundColor($r('app.color.page\_background'))
    .height('100%')
  }
}

#### Building a HAR

For details, see [Building a HAR](../../../../../building-an-app/configuring-your-build/building-a-har/document.md).

## Configuring Obfuscation

HAR can be used as a second-party or third-party library for other applications. To protect code assets, you are advised to [enable code obfuscation](../../../../../application-framework/arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/using-arkguard-for-source-code-obfuscation/document.md#enabling-source-code-obfuscation).

After [code obfuscation](../../../../../application-framework/arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/arkguard-principles-and-capabilities-for-source-code-obfuscation/document.md) is enabled, DevEco Studio compiles, obfuscates, and compresses code when building HARs to protect code assets.

The obfuscation capability is enabled by default for the HAR module. When the compilation module is release, simple code obfuscation is automatically performed for the HAR module of API version 10 or later. **Since DevEco Studio 5.0.3.600, the code obfuscation is disabled by default when a project is created.** You can enable this feature by setting **enable** in the **ruleOptions** field in the **build-profile.json5** file of the HAR module. For details, see [Using Obfuscation for Code Hardening](../../../../../building-an-app/using-obfuscation-for-code-hardening/document.md). The configuration is as follows:

{
  "apiType": "stageMode",
  "buildOption": {
    // ...
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
          },
          "consumerFiles": \[
            "./consumer-rules.txt"
          \]
        }
      },
      // ...
    },
  \],
  "targets": \[
    {
      "name": "default"
    },
    // ...
  \]
}

#### Publishing a HAR

For details, see [Publishing a Shared Package](../../../../../environment-setup/creating-a-project/managing-modules/developing-and-publishing-shared-packages/publishing-a-shared-package/document.md).
