# How do I set an application to automatically restart?

You can call **ApplicationContext.restartApp** to implement automatic restart. Refer to the sample code below.

import { Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })

      Button('RESTART').onClick(() => {
        let applicationContext = this.context.getApplicationContext();
        let want: Want = {
          bundleName: 'com.example.myapp',
          abilityName: 'EntryAbility'
        };
        try {
          applicationContext.restartApp(want);
          hilog.info(0x0000, 'testTag', '%{public}s', 'applicationContext.restartApp');
        } catch (error) {
          console.error(\`restartApp fail, error: ${JSON.stringify(error)}\`);
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}

**Reference**

[ApplicationContext.restartApp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextrestartapp12)
