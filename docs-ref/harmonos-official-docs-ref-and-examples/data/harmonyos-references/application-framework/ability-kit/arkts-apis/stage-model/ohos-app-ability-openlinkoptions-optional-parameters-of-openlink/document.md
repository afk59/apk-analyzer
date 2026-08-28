# @ohos.app.ability.OpenLinkOptions (Optional Parameters of openLink)

**OpenLinkOptions** can be used as an input parameter of [openLink()](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#openlink12) to indicate whether to enable only App Linking and pass in optional parameters in the form of key-value pairs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/xM9vmtL_SqahLfh2jiISsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25F772017439F7C700422E1F9ABF1423530B1D63DC9749DFEE827E975A375897)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { OpenLinkOptions } from '@kit.AbilityKit';

#### OpenLinkOptions

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| appLinkingOnly | boolean | No | Yes | 
Whether the UIAbility must be started using [AppLinking](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup).

\- If this parameter is set to **true** and no UIAbility matches the URL in App Linking, the result is returned directly.

\- If this parameter is set to **false** and no UIAbility matches the URL in App Linking, App Linking falls back to [Deep Linking](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/deep-linking-startup). The default value is **false**.

When the aa command is used to implicitly start an ability, you can set **\--pb appLinkingOnly true** or **\--pb appLinkingOnly false** to start the ability in App Linking mode.

 |
| parameters | Record<string, Object> | No | Yes | 

List of parameters in Want.

Note: For details about the usage rules, see **parameters** in [want](../../both-models-recommended/ohos-app-ability-want-want/document.md).

 |
| hideFailureTipDialog21+ | boolean | No | Yes | 

Whether to display a "No app available" dialog box when a suitable application is not found using [Deep Linking](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/deep-linking-startup).

\- **true**: The "No app available" dialog box is not displayed.

\- **false**: The "No app available" dialog box is displayed. The default value is **false**.

Note: If **appLinkingOnly** is set to **true**, the Deep Linking process is not triggered, and this field does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| completionHandler21+ | [CompletionHandler](../ohos-app-ability-completionhandler-application-launch-result-handler/document.md#completionhandler) | No | Yes | 

Operation class used to handle the result of an application launch request.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

**Example**

import { common, OpenLinkOptions, wantConstant, CompletionHandler, bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0xeeee;
const TAG: string = '\[openLinkDemo\]';

@Entry
@Component
struct Index {
  @State message: string = 'I am caller';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Button('start browser', { type: ButtonType.Capsule, stateEffect: true })
          .width('87%')
          .height('5%')
          .margin({ bottom: '12vp' })
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let link: string = 'https://www.example.com';
            let completionHandler: CompletionHandler = {
              onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
                console.info(\`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}\`);
              },
              onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
                console.error(\`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}\`);
              }
            };
            let openLinkOptions: OpenLinkOptions = {
              appLinkingOnly: true,
              // hideFailureTipDialog takes effect only when appLinkingOnly is set to false.
              // hideFailureTipDialog: true,
              parameters: {
                \[wantConstant.Params.CONTENT\_TITLE\_KEY\]: 'contentTitle',
                keyString: 'str',
                keyNumber: 200,
                keyBool: false,
                keyObj: {
                  keyObjKey: 'objValue',
                }
              },
              completionHandler: completionHandler
            };
            try {
              context.openLink(
                link,
                openLinkOptions,
                (err, result) => {
                  hilog.error(DOMAIN, TAG, \`openLink callback error.code: ${JSON.stringify(err)}\`);
                  hilog.info(DOMAIN, TAG, \`openLink callback result: ${JSON.stringify(result.resultCode)}\`);
                  hilog.info(DOMAIN, TAG, \`openLink callback result data: ${JSON.stringify(result.want)}\`);
                }
              ).then(() => {
                hilog.info(DOMAIN, TAG, \`open link success.\`);
              }).catch((err: BusinessError) => {
                hilog.error(DOMAIN, TAG, \`open link failed, errCode: ${JSON.stringify(err.code)}\`);
              });
            } catch (e) {
              hilog.error(DOMAIN, TAG, \`open link failed, errCode: ${JSON.stringify(e.code)}\`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
