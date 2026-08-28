# Map Location Selection Button

#### Use Case

You can call the map location selection button component to show the Map Kit page for users to select a location on the map and obtain the selected location information.

Run the sample code and tap **Select map location**. The page for location selection is displayed.

#### Restrictions

The map location selection button supports phones, tablets, and (since 5.0.1(13)) 2-in-1 devices.

#### Prerequisites

For details, please refer to [Preparations](../../../map-kit/preparations/document.md).

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
                // **OpenType.CHOOSE\_LOCATION** indicates that the button is used to select a location on the map.
                openType: functionalButtonComponentManager.OpenType.CHOOSE\_LOCATION,
                label: 'Select map location',
                // Adjust the button style.
                styleOption: {
                  bgColor: functionalButtonComponentManager.ColorType.DEFAULT,
                  size: functionalButtonComponentManager.SizeType.DEFAULT,
                  plain: false,
                  disabled: false,
                  loading: false,
                  hoverClass: functionalButtonComponentManager.HoverClassType.HOVER\_CLASS,
                  hoverStartTime: 0,
                  hoverStayTime: 0,
                  styleConfig: new functionalButtonComponentManager.ButtonConfig()
                    .fontSize(20)                
                },
              },
              // When **OpenType** is set to **CHOOSE\_LOCATION**, the callback must be **onChooseLocation**.
              controller: new functionalButtonComponentManager.FunctionalButtonController()
                .onChooseLocation((err, data) => {
                  if (err) {
                    // Error processing.
                    hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                    return;
                  }
                  // Success processing.
                  hilog.info(0x0000, "testTag", "succeeded in choosing location");
                  let name: string = data.name;
                  let address: string = data.address;
                  let longitude: number = data.longitude;
                  let latitude: number = data.latitude;
                })
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/bXW7eCkGTCGuoL8A5etfbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5FD8C0D2EE4C6246BB099FC9A4B054E7A25D90304785083DA07BE4E3D0AD0A1)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.CHOOSE\_LOCATION** to specify the purpose of the button as to select a location on the map.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onChooseLocation**.
    -   You can use the custom **Modifier** to set the button style. For details, please refer to the [Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#section1251915241170).
    
    For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
