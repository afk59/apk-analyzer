# Avatar Selection Button

#### Use Case

You can call the avatar selection component to promptly show the avatar selection page for a user, so the user can select an avatar such as the one associated with their HUAWEI ID.

Run the sample code and tap the avatar selection button. The selection page is displayed for you. For details, please refer to [Obtaining the Avatar and Nickname](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-avatar-and-nickname/document.md).

#### Prerequisites

For details, please refer to [Prerequisites](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-avatar-and-nickname/document.md#section41863510349).

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Declare FunctionalButton in the container, set **openType** for the button, and configure the callback.
    
    @Entry
    @Component
    struct Index {
      // Add the **account.png** file to the **/resources/base/media/** directory. Otherwise, an error message will be displayed, indicating that the file cannot be found.
      @State url: ResourceStr = $r('app.media.account');
    
      build() {
        Column() {
          // Declare FunctionalButton.
          FunctionalButton({
            params: {
              // **OpenType.CHOOSE\_AVATAR** indicates that the button is used to select an avatar.
              openType: functionalButtonComponentManager.OpenType.CHOOSE\_AVATAR,
              label: '',
              // Adjust the button style.
              styleOption: {
                styleConfig: new functionalButtonComponentManager.ButtonConfig()
                  .type(ButtonType.Normal)
                  .backgroundImage(this.url)
                  .backgroundImageSize(ImageSize.Cover)
                  .width(80)
                  .height(80)
                  .backgroundColor('#E5E5E5')
              },
            },
            // If **OpenType** is set to **CHOOSE\_AVATAR**, the callback must be **onChooseAvatar**.
            controller: new functionalButtonComponentManager.FunctionalButtonController().onChooseAvatar((err, data) => {
              if (err) {
                // Error processing.
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // Success processing.
              hilog.info(0x0000, "testTag", "succeeded in choosing avatar");
              this.url = data.avatarUri!;
            })
          })
        }
        .padding({ top: 200 })
        .height('100%')
        .width('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/iyj8gql5T_eqT2k8SAWtkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E9FD8775503CD5FFF9B15D046CFE6509205C88C2FEDCDE82B959165A863D106)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.CHOOSE\_AVATAR** to specify the purpose of the button as to select an avatar.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onChooseAvatar**.
    -   If the call is successful, you can obtain the address of the selected avatar from **avatarUri** in the callback.
    -   You can use the custom **Modifier** to set the button style. For details, please refer to the [Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#section1251915241170).
    
    For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
