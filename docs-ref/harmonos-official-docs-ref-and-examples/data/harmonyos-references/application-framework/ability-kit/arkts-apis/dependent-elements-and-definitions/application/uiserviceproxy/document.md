# UIServiceProxy

UIServiceProxy functions as a proxy to send data from the UIServiceExtensionAbility client to the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/XC-1kgM4Q8SDp70TNy5kag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0366F7D5081598EA4EA62C8E763E983FAE9F6689DA3B3BCA0075782519F8AA3F)

-   The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.
-   The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### UIServiceProxy.sendData

sendData(data: Record<string, Object>): void

Sends data to the UIServiceExtensionAbility server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/T0ur22W_SQi-YBZSGQniUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEF7E7C46E338C5B90A196AF6A491C00729DED6947C25770D194050AD5E946FF)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | Record<string, Object> | Yes | Data to be sent to the UIServiceExtensionAbility server. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**Example**

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '\[Extension\] ';

@Entry
@Component
struct UIServiceExtensionAbility {
  comProxy: common.UIServiceProxy | null = null;
  dataCallBack: common.UIServiceExtensionConnectCallback = {
    onData: (data: Record<string, Object>) => {
      console.info(\`${TAG} dataCallBack received data: ${JSON.stringify(data)}.\`);
    },
    onDisconnect: () => {
      console.info(\`${TAG} dataCallBack onDisconnect.\`);
      this.comProxy = null;
    }
  }

  build() {
    Scroll() {
      Column() {
        // Create a button for connecting to the UIServiceExtensionAbility.
        Button('connectUIServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
          .margin({
            top: 5,
            left: 10,
            right: 10,
            bottom: 5
          })
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.myConnectUIServiceExtensionAbility()
          });
      }
      .width('100%')
    }
    .height('100%')
  }

  // Customize a function for connecting to the UIServiceExtensionAbility.
  myConnectUIServiceExtensionAbility() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let startWant: Want = {
      deviceId: '',
      bundleName: 'com.acts.myapplication',
      abilityName: 'UiServiceExtensionAbility'
    };

    try {
      // Connect to the UIServiceExtensionAbility.
      context.connectUIServiceExtensionAbility(startWant, this.dataCallBack)
        .then((proxy: common.UIServiceProxy) => {
          console.info(TAG + \`try to connectUIServiceExtensionAbility ${proxy}}\`);
          this.comProxy = proxy;
          let formData: Record<string, string> = {
            'PATH': '/tmp/aaa.jpg'
          };
          try {
            console.info(\`${TAG} sendData.\`);
            // Send data to the UIServiceExtensionAbility.
            this.comProxy.sendData(formData);
          } catch (err) {
            let code = (err as BusinessError).code;
            let message = (err as BusinessError).message;
            console.error(\`${TAG} sendData failed, code is ${code}, message is ${message}.\`);
          }
        }).catch((err: Error) => {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(\`${TAG} connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.\`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`${TAG} connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.\`);
    }
  }
}
