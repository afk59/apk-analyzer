# App Launch Button

#### Use Case

You can call the app launch button component to redirect a user to another app.

Run the sample code and tap **Open APP**. The confirm page is displayed. If you tap **Allow**, you will be redirected to that app.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/iuhck8yDQ8WXUqyIcHwONQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A8CCE587198CFBFF9410EF8F07B037755A5FAF39DC33CF5BAA464FF426BFFD2)

Whether and how to display a pop-up is subject to the implementation of the target app.

#### Restrictions

The app launch button supports phones, tablets, 2-in-1 devices, and (since 5.1.0(18)) TVs.

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Declare FunctionalButton in the container, set **openType** for the button, and configure the callback.
    
    @Entry
    @Component
    struct Index {
      build() {
        Row() {
          Column() {
            // Declare FunctionalButton.
            FunctionalButton({
              params: {
                // **OpenType.LAUNCH\_APP** indicates that the button is used to launch an app.
                openType: functionalButtonComponentManager.OpenType.LAUNCH\_APP,
                label: 'Open APP',
                // When **OpenType** is set to **LAUNCH\_APP**, **appParam** is mandatory.
                appParam: {
                  bundleName: "xxx",
                  abilityName: "xxx"
                },
                // Adjust the button style.
                styleOption: {
                  styleConfig: new functionalButtonComponentManager.ButtonConfig()
                    .fontSize(20)
                },
              },
              // When **OpenType** is set to **LAUNCH\_APP**, the callback must be **onLaunchApp**.
              controller: new functionalButtonComponentManager.FunctionalButtonController().onLaunchApp((err) => {
                if (err) {
                  // Error processing.
                  hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                  return;
                }
                // Success processing. In this case, no value is returned.
                hilog.info(0x0000, "testTag", "succeeded in launching app");
              })
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/xvT_7TknT1GbYkfU0rzgaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71901F4978B45CE56EFABA5DF96470FF12B96574E105BE09C4BAC04016293025)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.LAUNCH\_APP** to specify the purpose of the button as to open an app.
    -   When **openType** is set to **functionalButtonComponentManager.OpenType.LAUNCH\_APP**, **appParam** is mandatory.
    -   In the value, **bundleName** indicates the package name and **abilityName** indicates the ability name.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onLaunchApp**.
    -   You can use the custom **Modifier** to set the button style. For details, please refer to the [Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#section1251915241170).
    
    For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
