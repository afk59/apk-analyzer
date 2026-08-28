# How do I implement another dialog box in a custom dialog box?

Use [openCustomDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialog12) to open dialog box A and click the button in dialog box A to open dialog box B. Use [getDialogController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-api#getdialogcontroller18) to obtain the **PromptActionDialogController** instance object and call the **close()** method to close the current dialog box. The code snippet is as follows:

import { ComponentContent } from '@kit.ArkUI';

@Component
struct DialogAComponent {
  build() {
    Column() {
      Column() {
        Text('dialog A')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
      }
      .justifyContent(FlexAlign.Center)
      .height(120)

      Row() {
        Text('close')
          .fontColor('#0A59F7')
          .onClick(() => {
            // close self.
            this.getDialogController()?.close();
          })
          .width('50%')
          .height('100%')
          .textAlign(TextAlign.Center)

        Text('open dialog B')
          .fontColor('#0A59F7')
          .onClick(() => {
            // Open dialog B.
            let uiContext = this.getUIContext();
            let promptAction = uiContext.getPromptAction();
            promptAction.openCustomDialog(new ComponentContent(uiContext, wrapBuilder(dialogBBuilder)));
          })
          .width('50%')
          .height('100%')
          .textAlign(TextAlign.Center)
      }
      .height(50)
    }
    .width(360)
    .borderRadius(32)
    .backgroundColor(Color.White)
  }
}

@Builder
function dialogABuilder() {
  DialogAComponent()
}

@Component
struct DialogBComponent {
  build() {
    Column() {
      Column() {
        Text('dialog B')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
      }
      .justifyContent(FlexAlign.Center)
      .height(120)

      Row() {
        Text('close')
          .fontColor('#0A59F7')
          .onClick(() => {
            // close self.
            this.getDialogController()?.close();
          })
          .width('50%')
          .height('100%')
          .textAlign(TextAlign.Center)
      }
      .height(50)
    }
    .width(320)
    .borderRadius(32)
    .backgroundColor(Color.White)
  }
}

@Builder
function dialogBBuilder() {
  DialogBComponent()
}

@Entry
@Component
struct PopUpDialogAgainInCustomDialog {
  build() {
    Column() {
      Button('open Dialog A')
        .onClick(() => {
          // Open dialog A.
          let uiContext = this.getUIContext();
          let promptAction = uiContext.getPromptAction();
          promptAction.openCustomDialog(new ComponentContent(uiContext, wrapBuilder(dialogABuilder)));
        })
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/brfR2WZhTzGQJmyztE2bYw/en-us_image_0000002399678053.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062552Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC73CC09CE8DC201F1B605A85495A2930B73460ACAB1FC2E0CB2F7F65BEE56EF "Click to enlarge")
