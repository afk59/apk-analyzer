# Mobile Number and Risk Level Retrieval Button

#### Use Case

Since version 6.0.2(22), Scenario Fusion Kit provides the button that can obtain the mobile number and risk level of a user.

You can integrate this button into your app as needed. It will first obtain an authorization code, which is then used to obtain a user's mobile number and risk level. With this information, your app can detect and implement risk control over malicious accounts, thereby safeguarding your app. For details about obtaining risk level information, please refer to [Obtaining a User's Risk Level Through Other Ways for HUAWEI ID Sign-in](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/obtaining-a-user-s-risk-level-through-other-ways-for-huawei-id-sign-in/document.md).

#### Prerequisites

You have successfully requested the scope for obtaining users' mobile numbers and the permission for obtaining the risk level. For details, please refer to [Requesting Scopes](../../../account-kit/getting-started/requesting-scopes/document.md) and [Prerequisites](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/obtaining-a-user-s-risk-level-through-other-ways-for-huawei-id-sign-in/document.md#section13750142919492).

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
                // **OpenType.GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL** indicates that the button is used to obtain a user's mobile number and the corresponding risk level.
                openType: functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL,
                label: 'Obtain mobile number and risk level',
                // Adjust the button style.
                styleOption: {
                  styleConfig: new functionalButtonComponentManager.ButtonConfig()
                    .fontSize(20)
                },
              },
              // When **OpenType** is set to **GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL**, the callback must be **onGetPhoneNumberAndRiskLevel**.
              controller: new functionalButtonComponentManager.FunctionalButtonController()
                .onGetPhoneNumberAndRiskLevel((data) => {
                  if (data?.errCode) {
                    // Error processing.
                    hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", data?.errCode, data?.errMsg);
                    return;
                  }
                  // Success processing.
                  hilog.info(0x0000, "testTag", "succeeded in authentication");
                  // Authorization code processing.
                  let authorizationCode = data?.code;
                })
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/TSKvF8YbQcGVXXbO940mpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85F36638F351B068BFF4D7A40B9591AF9E9A4D39EA580A59C747677062E0E6A7)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL** to specify the purpose of the button as to obtain a user's mobile number and the corresponding risk level.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onGetPhoneNumberAndRiskLevel**.
    -   If the button is triggered successfully, an authorization code is returned in the callback and you can use this code to obtain the user's mobile number and risk level. For details about obtaining risk level information, please refer to [Obtaining a User's Risk Level Through Other Ways for HUAWEI ID Sign-in](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/obtaining-a-user-s-risk-level-through-other-ways-for-huawei-id-sign-in/document.md).
    
    For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
