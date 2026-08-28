# Shipping Address Selection Button

#### Use Case

You can call the shipping address selection button component to show the page for users to select a shipping address and obtain the selected address.

Run the sample code and tap **Select shipping address**. Saved shipping addresses are displayed for you to select. You can also tap **Manage addresses** to access the address adding page. For details, please refer to [Obtaining the Shipping Address](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-shipping-address/document.md).

#### Prerequisites

For details, please refer to [Prerequisites](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-shipping-address/document.md#section1061219267293).

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
                // **OpenType.CHOOSE\_ADDRESS** indicates that the button is used to select a shipping address.
                openType: functionalButtonComponentManager.OpenType.CHOOSE\_ADDRESS,
                label: 'Select shipping address',
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
              // When **OpenType** is set to **CHOOSE\_ADDRESS**, the callback must be **onChooseAddress**.
              controller: new functionalButtonComponentManager.FunctionalButtonController()
                .onChooseAddress((err, data) => {
                  if (err) {
                    // Error processing.
                    hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                    return;
                  }
                  // Success processing.
                  hilog.info(0x0000, "testTag", "succeeded in choosing address");
                  // Obtain address information.
                  let userName: string = data.userName;
                  let mobileNumber: string = data.mobileNumber as string;
                  let countryCode: string = data.countryCode as string;
                  let provinceName: string = data.provinceName as string;
                  let cityName: string = data.cityName as string;
                  let districtName: string = data.districtName as string;
                  let streetName: string = data.streetName as string;
                  let detailedAddress: string = data.detailedAddress;
                })
            })
          }.width('100%')
        }.height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/GqpAfA4CQKaci3J2JimDFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2821B7922DA91698A0D8458F7B8908B46902CBE30B8F6A3461AA5189E4D136D7)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.CHOOSE\_ADDRESS** to specify the purpose of the button as to select a shipping address.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onChooseAddress**.
    -   You can use the custom **Modifier** to set the button style. For details, please refer to the [Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#section1251915241170).
    
    For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
