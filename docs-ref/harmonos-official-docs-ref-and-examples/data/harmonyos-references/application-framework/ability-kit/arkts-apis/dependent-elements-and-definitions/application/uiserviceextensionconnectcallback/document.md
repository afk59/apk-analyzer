# UIServiceExtensionConnectCallback

UIServiceExtensionConnectCallback provides callbacks for the connection to a UIServiceExtensionAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/o1urxCBAT6Cy6-eUgxhuwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6723F596CBD9DF16A9058602561C12A324C8C701700FDCC993FC0AC83D51DA34)

-   The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.
-   The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### UIServiceExtensionConnectCallback.onData

onData(data: Record<string, Object>): void

Called to receive data when a connection to the UIServiceExtensionAbility is established.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/q_16i6ykS227j0VFS1ifRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68D359772D9A8380F999398443733DB12CE502559031F5904F708DA954D59EEF)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | Record<string, Object> | Yes | Data about the UIServiceExtensionAbility connection. |

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

  myConnectUIServiceExtensionAbility() {
    // Obtain the context.
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
          console.info(TAG + \`try to connectUIServiceExtensionAbility ${proxy}\`);
          this.comProxy = proxy;
          let formData: Record<string, string> = {
            'PATH': '/tmp/aaa.jpg'
          };
          try {
            console.info(\`${TAG} sendData.\`);
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

#### UIServiceExtensionConnectCallback.onDisconnect

onDisconnect(): void

Called when the connection to the UIServiceExtensionAbility is interrupted.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/NnJA8Eo8RZatxfro_IigzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06162D15E96D7B0143F3E1384F055D4166472C0B1BAD1D45D7C24DB8E00B5B1B)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Example**

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '\[Extension\] ';

@Entry
@Component
struct UIServiceExtensionAbility {
  comProxy: common.UIServiceProxy | null = null;
  // Callback for the connection.
  dataCallBack: common.UIServiceExtensionConnectCallback = {
    onData: (data: Record<string, Object>) => {
      console.info(\`${TAG} dataCallBack received data: ${JSON.stringify(data)}.\`);
    },
    onDisconnect: () => {
      // Callback for the disconnection.
      console.info(\`${TAG} dataCallBack onDisconnect.\`);
      this.comProxy = null;
    }
  }

  build() {
    Scroll() {
      Column() {
        // Create a button for disconnecting from the UIServiceExtensionAbility.
        Button('disConnectUIServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
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

  myConnectUIServiceExtensionAbility() {
    // Obtain the context.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // Disconnect from the UIServiceExtensionAbility.
    try {
      // this.comProxy is saved when the connection is established.
      context.disconnectUIServiceExtensionAbility(this.comProxy).then(() => {
        console.info(\`${TAG} disconnectUIServiceExtensionAbility success.\`);
      }).catch((err: Error) => {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(\`${TAG} disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.\`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`${TAG} disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}.\`);
    }
  }
}
