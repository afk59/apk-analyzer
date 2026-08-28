# HSP

A Harmony Shared Package (HSP) is a dynamic shared package that can contain code, C++ libraries, resource files, and configuration files (also called profiles) and allows for code and resource sharing. An HSP is released with the Application Package (App Pack) of the host application, shares a process with the host application, and has the same bundle name and lifecycle as the host application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/2l323hzjRcODUMqjFSU1wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7367B7F588AFEF62F78517BA183CAD5A313F354DADA61D6BF00A27A8985689B0)

-   In-app HSP: a type of HSP that is closely coupled with an application bundle name (**bundleName**) during compilation and can be used only by the specified application.
    
-   [Integrated HSP](../../../typical-scenarios-development/integrated-hsp/document.md): a type of HSP that is not coupled with specific application bundle names during building and publishing. The toolchain can automatically replace the bundle name of the integrated HSP with that of the host application and generate a new HSP as the installation package of the host application. The new HSP also belongs to the in-app HSP of the host application's HAP.
    
-   Unless otherwise specified, all HSPs in the guide and API reference documents are in-app HSPs by default.
    

#### Use Scenarios

-   By storing code and resource files shared by multiple HAPs/HSPs in one place, the HSP significantly improves the reusability and maintainability of the code and resource files. Furthermore, because only one copy of the HSP code and resource files is retained during building and packaging, the size of the application package is effectively controlled.
    
-   The HSP is [loaded on demand](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-modular-design#section28312051291) during application running, which helps improve application performance.
    
-   The integrated HSP allows for code and resource sharing across applications in the same organization.
    

#### Constraints

-   An HSP can be installed and run with the HAP that depends on it. During installation or update, a consistency verification is performed between modules. For details, see [Consistency Verification for Application Installation and Update](../../application-management/consistency-verification-for-application-installation-and-update/document.md). During application packaging, validity verification is performed. For details, see [Packing Tool](../../../../../system/debugging-tools/debugging-commands/packing-and-unpacking-tools/packing-tool/document.md).
-   Since API version 14, HSP supports the declaration of the [UIAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-overview/document.md#declaration-configuration) component in the configuration file. However, a **UIAbility** with entry capabilities (that is, **entity.system.home** and **ohos.want.action.home** are configured for the **skill** tag) is not supported. For details about how to configure a **UIAbility**, see [Adding a UIAbility to a Module](../../../../../environment-setup/creating-a-project/managing-modules/adding-an-ability-to-a-module/document.md#section18658758104318). The method of starting a **UIAbility** in an HSP is the same as that described in [Starting UIAbility in the Same Application](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/starting-uiability-within-the-same-application/document.md). For API version 13 and earlier versions, the [UIAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-overview/document.md#declaration-configuration) component cannot be declared in the configuration file.
-   Since API version 18, HSP supports the declaration of the [ExtensionAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md) component in the configuration file. However, an **ExtensionAbility** with entry capabilities (that is, **entity.system.home** and **ohos.want.action.home** are configured for the **skill** tag) is not supported. For details about how to configure an **ExtensionAbility** in an HSP, see [Adding an ExtensionAbility to a Module](../../../../../environment-setup/creating-a-project/managing-modules/adding-an-ability-to-a-module/document.md#section18891639459). For API version 17 and earlier versions, the [ExtensionAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md) component cannot be declared in the configuration file.
-   An HSP can depend on other HARs or HSPs, and can be depended on or integrated by HAPs or HSPs. However, cyclic dependency and dependency transfer are not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/N9Xp-jFxTHCI4fJAepKJPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ACDBE40B562E83B65DD55300A7B212C88A249801636CF0FCA4633BA1F065F77)

Cyclic dependency: For example, there are three HSPs. HSP-A depends on HSP-B, HSP-B depends on HSP-C, and HSP-C depends on HSP-A.

Dependency transfer: For example, there are three HSPs. HSP-A depends on HSP-B, and HSP-B depends on HSP-C. Dependency transfer is not supported indicating that HSP-A can use the methods and components of HSP-B, but cannot directly use that of HSP-C.

#### Creating an HSP

Create an HSP module for calling C++ code on DevEco Studio and turn on **Enable native** on the **Configure New Module** page. For details, see [Creating an HSP Module](../../../../../environment-setup/creating-a-project/managing-modules/developing-and-publishing-shared-packages/developing-a-dynamic-shared-package/document.md#section7717162312546). The following uses the **library** module as an example. The basic project directory structure is as follows:

MyApplication
├── library
│   ├── src
│   │   └── main
|   |       ├── cpp
|   |       |   ├── CMakeLists.txt    // Configuration file for compiling C++ code
|   |       |   └── napi\_init.cpp     // C++ file for initializing the NAPI module
│   │       ├── ets
│   │       │   └── pages
│   │       │       └── index.ets     // Page file of the library module
│   │       ├── resources             // Resources of the library module
│   │       └── module.json5          // Configuration file of the library module
│   ├── oh-package.json5              // Module-level configuration file
│   ├── index.ets                     // Entry file
│   └── build-profile.json5           // Module-level configuration file
└── build-profile.json5               // Project-level configuration file

#### Developing an HSP

You can export the ArkUI components, APIs, and other resources of an HSP for other HAPs or HSPs in the same application to reference.

## Exporting ArkUI Components

Use **export** to export ArkUI components. The sample code is as follows:

// library/src/main/ets/components/MyTitleBar.ets
@Component
export struct MyTitleBar {
  build() {
    Row() {
      Text($r('app.string.library\_title'))
        .id('library')
        .fontFamily('HarmonyHeiTi')
        .fontWeight(FontWeight.Bold)
        .fontSize(32)
        .fontColor($r('app.color.text\_color'))
    }
    .width('100%')
  }
}

Declare the APIs exposed to external systems in the entry file **index.ets**.

// library/index.ets
export { MyTitleBar } from './src/main/ets/components/MyTitleBar';

## Exporting Classes and Methods

Use **export** to export classes and methods. The sample code is as follows:

// library/src/main/ets/utils/test.ets
export class Log {
  static info(msg: string): void {
    console.info(msg);
  }
}

export function add(a: number, b: number): number {
  return a + b;
}

export function minus(a: number, b: number): number {
  return a - b;
}

Declare the APIs exposed to external systems in the entry file **index.ets**.

// library/index.ets
export { Log, add, minus } from './src/main/ets/utils/test';

## Exporting Native Methods

The HSP can contain .so files compiled in C++. The HSP indirectly exports the native method in the .so file. In this example, the **multi** API in the **liblibrary.so** file is exported.

// library/src/main/ets/utils/nativeTest.ets
import native from 'liblibrary.so';

export function nativeMulti(a: number, b: number): number {
  let result: number = native.multi(a, b);
  return result;
}

Declare the APIs exposed to external systems in the entry file **index.ets**.

// library/index.ets
export { nativeMulti } from './src/main/ets/utils/nativeTest';

## Accessing Resources in an HSP Through $r

More often than not, you may need to use resources, such as strings and images, in components. For components in an HSP, such resources are typically placed in the HSP package, rather than in the package where the HSP is invoked, for the purpose of complying with the principle of high cohesion and low coupling.

In a project, application resources are referenced in the $r or $rawfile format. You can use $r or $rawfile to access resources in the **resources** directory of the current module. For example, you can use $r("app.media.example") to access the src/main/resources/base/media/example.png image stored in the **resources** directory. For details about how to use $r and $rawfile, see [Resource Categories and Access](../../../../resource-categories-and-access/document.md).

To avoid reference errors, do not use relative paths. Example:

If you use **Image("../../resources/base/media/example.png")**, the image actually used will be the one in the directory of the module that invokes the HSP. Specifically, if the module that invokes the HSP is **entry**, the system loads the image from **entry/src/main/resources/base/media/example.png**.

// library/src/main/ets/pages/Index.ets
// Correct case
Image($r('app.media.example'))
  .id('example')
  .borderRadius('48px')
// // Incorrect case
Image("../../resources/base/media/example.png")
  .id('example')
  .borderRadius('48px')

## Exporting Resources from HSP

When resources in an HSP need to be exported for cross-package access, it is recommended that a resource manager class be implemented to encapsulate the exported resources. In this way:

-   You can keep resources well under your control, eliminating the need for exporting resources that do not need to be exposed.
-   The invoking module does not need to be aware of the internal resource names of the HSP, or make adaptation to changes in these internal resource names.

The implementation is as follows:

Encapsulate the resources that need to be published into a resource management class.

// library/src/main/ets/ResManager.ets
export class ResManager{
  static getPic(): Resource{
    return $r('app.media.pic');
  }
  static getDesc(): Resource{
    return $r('app.string.shared\_desc');
  }
}

Declare the APIs exposed to external systems in the entry file **index.ets**.

// library/index.ets
export { ResManager } from './src/main/ets/ResManager';

#### Using an HSP

You can reference APIs in an HSP and implement page redirection in the HSP through page routing.

## Referencing APIs

To use APIs in the HSP, first configure the dependency on the HSP in the **oh-package.json5** file of the module that needs to call the APIs (called the invoking module). For details, see [Referencing a Shared Package](../../../../../environment-setup/creating-a-project/managing-modules/referencing-and-managing-a-shared-package/document.md).

You can then call the external APIs of the HSP in the same way as calling the APIs in the HAR. In this example, the external APIs are the following ones exported from **library**:

// library/index.ets
// ...
export { Log, add, minus } from './src/main/ets/utils/test';
// ...
export { MyTitleBar } from './src/main/ets/components/MyTitleBar';
// ...
export { ResManager } from './src/main/ets/ResManager';
// ...
export { nativeMulti } from './src/main/ets/utils/nativeTest';

The APIs can be used as follows in the code of the invoking module:

// entry/src/main/ets/pages/index.ets
import { Log, add, MyTitleBar, ResManager, nativeMulti } from 'library';
import { BusinessError } from "@kit.BasicServicesKit";
import { application} from '@kit.AbilityKit';

const TAG = 'Index';

@Entry
@Component
struct Index {
  @State message: string = '';

  build() {
    Column() {
      List() {
        ListItem() {
          MyTitleBar()
        }
        .margin({ left: '35px', top: '32px' })

        ListItem() {
          Text(this.message)
            .fontFamily('HarmonyHeiTi')
            .fontSize(18)
            .textAlign(TextAlign.Start)
            .width('100%')
            .fontWeight(FontWeight.Bold)
        }
        .width('685px')
        .margin({ top: 30, bottom: 10 })

        ListItem() {
          // Resource object returned by ResManager, which can be passed to a component for direct use or be extracted.
          Image(ResManager.getPic())
            .id('image')
            .borderRadius('48px')
        }
        .width('685px')
        .margin({ top: 10, bottom: 10 })
        .padding({ left: 12, right: 12, top: 4, bottom: 4 })

        ListItem() {
          Text($r('app.string.add'))
            .fontSize(18)
            .textAlign(TextAlign.Start)
            .width('100%')
            .fontWeight(500)
            .height('100%')
        }
        .id('add')
        .borderRadius(24)
        .width('685px')
        .height('84px')
        .backgroundColor($r('sys.color.ohos\_id\_color\_foreground\_contrary'))
        .margin({ top: 10, bottom: 10 })
        .padding({ left: 12, right: 12, top: 4, bottom: 4 })
        .onClick(() => {
          Log.info('add button click!');
          this.message = 'result: ' + add(1, 2);
        })

        ListItem() {
          Text(ResManager.getDesc())
            .fontSize(18)
            .textAlign(TextAlign.Start)
            .width('100%')
            .fontWeight(500)
            .height('100%')
        }
        .id('getStringValue')
        .borderRadius(24)
        .width('685px')
        .height('84px')
        .backgroundColor($r('sys.color.ohos\_id\_color\_foreground\_contrary'))
        .margin({ top: 10, bottom: 10 })
        .padding({ left: 12, right: 12, top: 4, bottom: 4 })
        .onClick(() => {
          // Obtain the context of the HSP module through application.createModuleContext and the resourceManager object of the HSP module, and call the API of resourceManager to obtain resources.
          application.createModuleContext(this.getUIContext()?.getHostContext(), "library").then((context:Context)=>{
            context.resourceManager.getStringValue(ResManager.getDesc().id)
              .then(value => {
                console.info('getStringValue is ' + value);
                this.message = 'getStringValue is ' + value;
              })
              .catch((err: BusinessError) => {
                console.error('getStringValue promise error is ' + err);
              });
          }).catch((err: BusinessError) => {
            console.error('createModuleContext promise error is ' + err);
          });
        })

        ListItem() {
          Text($r('app.string.native\_multi'))
            .fontSize(18)
            .textAlign(TextAlign.Start)
            .width('100%')
            .fontWeight(500)
            .height('100%')
        }
        .id('nativeMulti')
        .borderRadius(24)
        .width('685px')
        .height('84px')
        .backgroundColor($r('sys.color.ohos\_id\_color\_foreground\_contrary'))
        .margin({ top: 10, bottom: 10 })
        .padding({ left: 12, right: 12, top: 4, bottom: 4 })
        .onClick(() => {
          Log.info('nativeMulti button click!');
          this.message = 'result: ' + nativeMulti(3, 4);
        })
      }
      .alignListItem(ListItemAlign.Center)
    }
    .width('100%')
    .backgroundColor($r('app.color.page\_background'))
    .height('100%')
  }
}

## Page Redirection and Return

To add a button in the **entry** module to jump to the menu page (**library/src/main/ets/pages/library\_menu.ets**) in the **library** module, write the following code in the **entry/src/main/ets/pages/Index.ets** file of the **entry** module:

@Entry
@Component
struct Index {
  @State message: string = '';
  pathStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pathStack) {
      Column() {
        List() {
          ListItem() {
            Text($r('app.string.click\_to\_menu'))
              .fontSize(18)
              .textAlign(TextAlign.Start)
              .width('100%')
              .fontWeight(500)
              .height('100%')
          }
          .id('clickToMenu')
          .borderRadius(24)
          .width('685px')
          .height('84px')
          .backgroundColor($r('sys.color.ohos\_id\_color\_foreground\_contrary'))
          .margin({ top: 10, bottom: 10 })
          .padding({
            left: 12,
            right: 12,
            top: 4,
            bottom: 4
          })
          .onClick(() => {
            this.pathStack.pushPathByName('library\_menu', null)
          })
        }
        .alignListItem(ListItemAlign.Center)
      }
      .width('100%')
      .backgroundColor($r('app.color.page\_background'))
      .height('100%')
    }.title("Navigation\_Index")
    .mode(NavigationMode.Stack)
  }
}

Add a page file (**library/src/main/ets/pages/library\_menu.ets**) to the **library** module. The **back\_to\_index** button on the page can be used to return to the previous page.

@Builder
export function PageOneBuilder() {
  Library\_Menu()
}

@Entry
@Component
export struct Library\_Menu {
  @State message: string = 'Hello World';
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize($r('app.float.page\_text\_font\_size'))
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              this.message = 'Welcome';
            })
          Button('back\_to\_index').fontSize(50).onClick(() => {
            this.pathStack.pop();
          })
        }
        .width('100%')
      }
      .height('100%')
    }.title('Library\_Menu')
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    })
  }
}

Add the **route\_map.json** file (**library/src/main/resources/base/profile/route\_map.json**) to the **library** module.

{
  "routerMap": \[
    {
      "name": "library\_menu",
      "pageSourceFile": "src/main/ets/pages/library\_menu.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is library\_menu"
      }
    }
  \]
}

Configure the **route\_map.json** file in the **library/src/main/module.json5** file of the **library** module.

{
  "module": {
    "name": "library",
    "type": "shared",
    "description": "$string:shared\_desc",
    "deviceTypes": \[
      "tablet",
      "2in1"
    \],
    "deliveryWithInstall": true,
    "pages": "$profile:main\_pages",
    "routerMap": "$profile:route\_map" // Added configuration, which points to the route\_map.json file.
  }
}

The navigation feature is used for page redirection and return. For details, see [Page Navigation](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md#routing-operations).
