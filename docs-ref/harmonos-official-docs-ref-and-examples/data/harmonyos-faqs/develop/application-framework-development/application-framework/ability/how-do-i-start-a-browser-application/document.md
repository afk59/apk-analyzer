# How do I start a browser application?

To start a browser application, you can implicitly set **action** in the **want** parameter to **ohos.want.action.viewData** and set **uri** in the **want** parameter to the URL of the web page. In this case, the system starts the default browser on the device. If there are multiple browsers on the device, you can set **ohos.ability.params.showDefaultPicker** in **parameters** to **true** to allow users to select a browser. Refer to the code snippet below.

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function startBrowsableAbility(context: common.UIAbilityContext): void {
  let want: Want = {
    action: 'ohos.want.action.viewData',
    entities: \['entity.system.browsable'\],
    uri: 'https://www.huawei.com/',
    parameters: {
      'ohos.ability.params.showDefaultPicker': true
    }
  };
  context.startAbility(want)
    .then(() => {
      console.error('Start browsableAbility successfully.');
    })
    .catch((err: BusinessError) => {
      console.error(\`Failed to startAbility. Code: ${err.code}, message: ${err.message}\`);
    });
}

@Entry
@Component
struct BrowsableAbilityView {
  @State message: string = 'Pull up the browser and open the Huawei official website';

  build() {
    Row() {
      Column() {
        Button(this.message)
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            const context: common.UIAbilityContext = this.getUIContext().getHostContext()! as common.UIAbilityContext;
            startBrowsableAbility(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
