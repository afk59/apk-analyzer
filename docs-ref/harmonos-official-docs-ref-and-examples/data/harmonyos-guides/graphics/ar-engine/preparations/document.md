# Preparations

#### Software Requirements

-   Recommended OS for installing DevEco Studio: Windows 10 or later, or MacOS 11 or later
-   Recommended DevEco Studio: DevEco Studio 6.0.0 Release or later
-   Recommended HarmonyOS SDK: HarmonyOS 6.0.0 Release SDK or later

#### Hardware Requirements

You can choose the appropriate API for your programming language to check if a device supports AR Engine. The following demonstrates API call examples:

ArkTS ([ARViewContext.init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section07524457283)):

import { arViewController, ARView } from '@kit.AREngine';
import { BusinessError } from '@kit.BasicServicesKit';
@Component
struct ARTest {
  @State arContext?: arViewController.ARViewContext = undefined;
  build() {
    NavDestination() {
      RelativeContainer() {
        if (this.arContext) {
          ARView({ context: this.arContext })
        }
      }
    }
    .onAppear(() => {
      this.initARView()
    })
    .onWillDisappear(() => {
      await this.arContext?.destroy();
    })
  }

  private initARView(): void {
    let context = new arViewController.ARViewContext()
    context.init().then(() => {
      this.arContext = context;
      console.info(\`Succeeded in initializing ARView.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to init context. Code is ${err.code}, message is ${err.message}\`);
    });
  }
}

C/C++ ([HMS\_AREngine\_ARSession\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga47713cb18234569e03b5216b6c8442d3)):

#include "ar/ar\_engine\_core.h" 

bool isSupportAREngine() {
    AREngine\_ARSession \*arSession = nullptr;
    if(HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession) == ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED){
        return false;
    }
    return true;
}

If the API returns error code 801 or "ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED", AR Engine does not support the current device.

#### Setting Up the Environment

Make preparations by referring to [Preparing for App Development](../../../getting-prepared/application-development-preparations/document.md).

#### Applying for Permissions

When developing AR apps, it is necessary to first request camera-related permissions to ensure the app has access to the camera hardware and other functionalities. The required permissions are outlined below. Before applying for any permissions, ensure that you have complied with the [basic principles for using permissions](../../../system/security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions).

-   Before using the camera for capturing, the **ohos.permission.CAMERA** permission must be obtained.
-   To utilize the accelerometer for detecting device motion status, the **ohos.permission.ACCELEROMETER** permission must be obtained.
-   To use the gyroscope for sensing device pose information, the **ohos.permission.GYROSCOPE** permission must be obtained.

#### Making Preparations

It is advised to use [Component Navigation (Navigation) (Recommended)](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md) as the page routing method and apply the [Page Lifecycle](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md#page-lifecycle) provided by [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation).

You need to first create a home page, from which users can select the AR Engine scene to enter.

1.  Import the required modules.
    
    import { abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create a basic page. For details, please refer to [Component Navigation (Navigation) (Recommended)](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md).
    
    @Entry
    @Component
    struct Selector {
      pageInfo: NavPathStack = new NavPathStack();
    
      build(): void {
        Navigation(this.pageInfo) {
    
        }
        .mode(NavigationMode.Stack)
        .hideTitleBar(true)
        .hideBackButton(true)
        .hideToolBar(true)
      }
    }
    
3.  Create **sampleButton**, encapsulating button functionality and permission verification, decorate it using **@Builder**, and configure **routerMap** for page redirection.
    
    @Entry
    @Component
    struct Selector {
      pageInfo: NavPathStack = new NavPathStack();
      private hasPermission: boolean = false;
      @State context: Context = this.getUIContext().getHostContext() as Context;
    
      build(): void {
        // ...
      }
    
      @Builder
      sampleButton(sampleName: string): void {
        Button(sampleName, { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(async () => {
            if (!this.hasPermission) {
              this.hasPermission = await requestPermissionOnSetting(this.context);
              if (!this.hasPermission) {
                return;
              }
            }
            this.pageInfo.clear();
            this.pageInfo.pushDestinationByName(sampleName, null).catch((error: BusinessError) => {
              console.error(\`\[pushDestinationByName\]failed. Code: ${error.code}.\`);
            });
          })
      }
    }
    
4.  Create the **requestPermissionOnSetting** method to verify whether the camera permission has been granted before entering the AR scene.
    
    struct Selector {
      // ...
    }
    
    async function requestPermissionOnSetting(context: Context): Promise<boolean> {
      let requestResult: boolean = false;
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      await atManager.requestPermissionOnSetting(context, \['ohos.permission.CAMERA'\])
        .then((data: abilityAccessCtrl.GrantStatus\[\]) => {
          console.info('data:' + JSON.stringify(data));
          if (data\[0\] === abilityAccessCtrl.GrantStatus.PERMISSION\_GRANTED) {
            requestResult = true;
          }
        })
        .catch((err: BusinessError) => {
          console.error('data:' + JSON.stringify(err));
        })
      return requestResult;
    }
    
5.  Add a button on the page for accessing the AR scene.
    
    build(): void {
      Navigation(this.pageInfo) {
        Column() {
          this.sampleButton('ARWorld'); // Enter the ARWorld scene.
        }
        .justifyContent(FlexAlign.SpaceEvenly)
        .width('100%')
        .height('100%')
      }
      .mode(NavigationMode.Stack)
      .hideTitleBar(true)
      .hideBackButton(true)
      .hideToolBar(true)
    }
    
6.  In the **onAppear** method, configure **requestPermissionOnFirstStartup** to handle permission verification when the app is launched for the first time.
    
    struct Selector {
      // ...
      build(): void {
        Navigation(this.pageInfo) {
          Column() {
            this.sampleButton('ARWorld');
          }
          .justifyContent(FlexAlign.SpaceEvenly)
          .width('100%')
          .height('100%')
        }
        .onAppear(() => {
          this.requestPermissionOnFirstStartup();
        })
        .mode(NavigationMode.Stack)
        .hideTitleBar(true)
        .hideBackButton(true)
        .hideToolBar(true)
      }
    
      @Builder
      sampleButton(sampleName: string): void { 
        // ...
      }
    
      private requestPermissionOnFirstStartup(): void {
        abilityAccessCtrl.createAtManager()
          .requestPermissionsFromUser(this.context, \['ohos.permission.CAMERA'\])
          .then((data: PermissionRequestResult) => {
            let grantStatus: number\[\] = data.authResults;
            if (grantStatus\[0\] === 0) {
              this.hasPermission = true;
              console.info('Succeeded in getting requestPermission.');
            } else {
              this.hasPermission = false;
              console.error('Failed to get requestPermission, user rejected.');
            }
          })
          .catch((err: BusinessError) => {
            console.error(\`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}.\`);
          })
      }
    }
