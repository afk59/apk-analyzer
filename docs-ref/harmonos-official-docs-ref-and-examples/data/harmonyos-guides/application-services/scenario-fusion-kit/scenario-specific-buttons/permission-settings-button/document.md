# Permission Settings Button

#### Use Case

You can call the permission settings button component to show the permission settings pop-up for users to grant permissions if they previously rejected the authorization when prompted the first time.

Run the sample code, and tap **Request user authorization** and then tap **Deny** in the displayed pop-up. Then you can tap **Permission settings** to display the authorization pop-up to ask for authorization again.

#### Restrictions

The permission settings button supports phones, tablets, 2-in-1 devices, and (since 5.1.0(18)) TVs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/xh8Yx1MOTmGVsyxmegm7aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD1F99A6820BC7670C8FBF243D8626A3D6F08122F3260FE14D571B1482826631)

This API supports only UIAbilities/UIExtensionAbilities.

Before calling this API, call [requestPermissionsFromUser](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9) first. If the user has granted the permissions required when the permission settings pop-up is displayed the first time, calling this API will not display the authorization pop-up.

#### Prerequisites

-   When the [requestPermissionsFromUser](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9) API is called, the user rejects authorization in the permission settings pop-up.
-   For details, please refer to [Preparations](../../preparations/document.md).

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Declare FunctionalButton in the container, set **openType** for the button, and configure the callback.
    
    @Entry
    @Component
    struct Index {
      build() {
        Row() {
          Column({ space: 3 }) {
            // Call the **Button** API of **requestPermissionsFromUser**.
            Button('Request user authorization')
              .fontSize(20)          
              .onClick(() => {
                let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
                let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                try {
                  // Add the **ohos.permission.READ\_CALENDAR** and **ohos.permission.WRITE\_CALENDAR** permissions to the **module.json5** file.
                  atManager.requestPermissionsFromUser(context,
                    \['ohos.permission.READ\_CALENDAR', 'ohos.permission.WRITE\_CALENDAR'\],
                    (err: BusinessError, data: PermissionRequestResult) => {
                      if (err) {
                        hilog.error(0x0000, "testTag", "failed in requesting Permissions from user : %{public}d %{public}s",
                          err.code, err.message);
                      } else {
                        hilog.info(0x0000, "testTag", 'data permissions: %{public}s', data.permissions?.join(','));
                        hilog.info(0x0000, "testTag", 'data authResults: %{public}s', data.authResults?.join(','));
                        hilog.info(0x0000, "testTag", 'data dialogShownResults: %{public}s', data.dialogShownResults?.join(','));
                      }
                    })
                } catch (err) {
                  hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                }
              })
    
            // Declare FunctionalButton.
            FunctionalButton({
              params: {
                // **OpenType.PERMISSION\_SETTING** indicates that the button is used to set permissions.
                openType: functionalButtonComponentManager.OpenType.PERMISSION\_SETTING,
                label: 'Permission settings',
                permissionListParam: \['ohos.permission.READ\_CALENDAR', 'ohos.permission.WRITE\_CALENDAR'\],
                // Adjust the button style.
                styleOption: {
                  styleConfig: new functionalButtonComponentManager.ButtonConfig()
                    .fontSize(20)                
                },
              },
              // When **OpenType** is set to **PERMISSION\_SETTING**, the callback must be **onPermissionSetting**.
              controller: new functionalButtonComponentManager.FunctionalButtonController().onPermissionSetting((err,
                data) => {
                if (err) {
                  // Error processing.
                  hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                  return;
                }
                // Success processing.
                hilog.info(0x0000, "testTag", "succeeded in setting permission ");
                let result = data.permissionResult;
                result.forEach(res => {
                  hilog.info(0x0000, "testTag", "data: %{public}s", String(res));
                })
              })
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/TdssIK6XRxG63O07rKkThQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=759A7F0EF3E97ED7B22BA8EB7D452E71E6F2EDB9A4979DF918C025ED1421E016)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.PERMISSION\_SETTING** to specify the purpose of the button as to set the permission.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onPermissionSetting**.
    -   You can use the custom **Modifier** to set the button style. For details, please refer to the [Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#section1251915241170).
        
        For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
