# Mobile Number Quick Verification Button

#### Use Case

Your app can leverage the mobile number quick verification button to request users' mobile numbers after their consent so that you can provide specific services in scenarios where it is necessary to obtain user mobile numbers, as defined in the "[Provisions on the Scope of Necessary Personal Information for Common Types of Mobile Internet Apps](https://appinchina.co/government-documents/notice-on-issuing-the-regulations-on-the-scope-of-necessary-personal-information-for-common-types-of-mobile-internet-applications/)" (third-party website content, for which Huawei does not provide any guarantee and bears no responsibility). For details, please check the relevant [use case](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-mobile-number/quick-verification/document.md#section175151155165314) of quick verification.

Run the sample code, and tap the **Verify mobile number quickly** button. The verification page is displayed. For details, please refer to [Quick Verification](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-mobile-number/quick-verification/document.md).

#### Restrictions

The mobile number quick verification button supports phones, tablets, 2-in-1 devices, and (since 5.1.0(18)) TVs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/NwpLN2bCQy2Oz-hUnJ2CSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8517410D2D894B1AF17C36A10155BF88F4D583EA44A3B42DB1D940ED3F8F6F1)

User authorization is required only when your app or atomic service is used for the first time. When it is accessed again, only the mobile number is verified and the number cannot be changed.

#### Prerequisites

For details, please refer to [Prerequisites](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-mobile-number/quick-verification/document.md#section2011736191112).

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
                // **OpenType.GET\_PHONE\_NUMBER** indicates that the button is used to verify a mobile number quickly.
                openType: functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER,
                label: 'Verify mobile number quickly',
                // Adjust the button style.
                styleOption: {
                  styleConfig: new functionalButtonComponentManager.ButtonConfig()
                    .fontSize(20)
                },
              },
              // When **OpenType** is set to **GET\_PHONE\_NUMBER**, the callback must be **onGetPhoneNumber**.
              controller: new functionalButtonComponentManager.FunctionalButtonController()
                .onGetPhoneNumber((err, data) => {
                  if (err) {
                    // Error processing.
                    hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                    return;
                  }
                  // Success processing.
                  hilog.info(0x0000, "testTag", "succeeded in authenticating");
                  // Authorization code processing.
                  let authorizationCode = data.code;
                })
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/u18cuqFGQ9WrD688fP1xxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E82C0273BF6F87E402714634741204E3E9B51ECBC5D68C772DA3A32F6974724)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER** to specify the purpose of the button as to quickly verify mobile numbers.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onGetPhoneNumber**.
    -   If the call is successful, you can obtain the real mobile number based on the authorization code (valid for five minutes) in the callback. For details, please refer to [Server-Side Development](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-mobile-number/quick-verification/document.md#section380015370555).
    -   You can use the custom **Modifier** to set the button style. For details, please refer to the [Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#section1251915241170).
    
    For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
