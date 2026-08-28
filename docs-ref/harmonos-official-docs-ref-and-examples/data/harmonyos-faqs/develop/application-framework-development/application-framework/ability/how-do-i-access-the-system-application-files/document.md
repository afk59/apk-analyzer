# How do I access the system application Files?

You can use [openLink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) to access the system application Files, with the URL of **Files** passed to the **link** field. The sample code is as follows:

import { common, OpenLinkOptions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '\[UIAbilityComponentsOpenLink\]';
const DOMAIN\_NUMBER: number = 0xFF00;

@Entry
@Component
struct Index {
  @State message: string = 'Start Files';
  context = this.getUIContext();

  build() {
    Row() {
      Column() {
        Button(this.message)
          .width('100%')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context: common.UIAbilityContext = this.context.getHostContext() as common.UIAbilityContext;
            let link: string = 'filemanager://openDirectory';
            let openLinkOptions: OpenLinkOptions = {
              parameters: {
                'fileUri': ''
              }
            };
            try {
              context.openLink(link, openLinkOptions)
                .then(() => {
                  hilog.info(DOMAIN\_NUMBER, TAG, 'open link success.');
                }).catch((err: BusinessError) => {
                hilog.error(DOMAIN\_NUMBER, TAG, \`open link failed. Code is ${err.code}, message is ${err.message}\`);
              });
            } catch (paramError) {
              hilog.error(DOMAIN\_NUMBER, TAG,
                \`Failed to start link. Code is ${paramError.code}, message is ${paramError.message}\`);
            }
          })
      }
      .padding({ left: 16, right: 16 })
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[UIAbilityContext.openLink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12)
