# Typical Scenarios

The following shows two typical application scenarios of SmartFill.

#### Identity Verification for Ticket Purchase

Example 1: The function can intelligently recognize content on the clipboard to facilitate one-tap copy and one-tap filling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/PrNU43roQbC71MFjVtuoiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=848CD01DB73B3A20FD5CFFA1C05503CC9B77C10751F90022AC9A0CEE80F939B7)

Currently, only Chinese names and addresses are supported for suggestions based on clipboard content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/g5naCdSlRwGnQzPZRWF13w/en-us_image_0000002470332178.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51C9974E40B3C0C2FCED5E165F9BA72A68F9616FDAC2BCB418CE7047974AE420 "Click to enlarge")

Example 2: The function can intelligently match information in data sources such as recent forms and Account Kit based on current user input to implement one-tap information filling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/MqKCH71NQW6Yxgn3Fu9wsQ/en-us_image_0000002470492172.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2FE802DF6CB6E3E4B7305A945FFE39DA708158206167BAC375366E4DDE0C037 "Click to enlarge")

#### Shipping Address Filling

Example 1: The function can intelligently recognize content on the clipboard to facilitate one-tap copy and one-tap filling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/O-jw8P0ERmGWUkSgsDwO3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5848AAD3BE0CFA200ABA48CB8D0C59FB1C3FC70E512E4503BFEC18DE3CD86664)

Currently, only Chinese names and addresses are supported for suggestions based on clipboard content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/9Uah21ZPSsm1khMWejYOQQ/en-us_image_0000002470332182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6048CB89AA98E7E8EE4222E726F9CDA086567C04E1255C3BF4900410E02080BF "Click to enlarge")

Example 2: The function can intelligently match information in data sources such as recent forms and Account Kit based on current user input to implement one-tap information filling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/f5nmJkFtRQGjNBOHg0uwEw/en-us_image_0000002503572053.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABB178422D09749D47A91A377CB791755EDD79DB748D12089DCB4D3BE7B853FD "Click to enlarge")

#### Sample Code

import { autoFillManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SmartFill {
  @State isClicked: boolean = false;

  build() {
    Column({ space: 5 }) {
      Row() {
        Text('Nickname:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.NICKNAME).selectionMenuHidden(true)
      }

      Row() {
        Text('Name:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.PERSON\_FULL\_NAME).selectionMenuHidden(true)
      }

      Row() {
        Text('Phone:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.PHONE\_NUMBER).selectionMenuHidden(true)
      }

      Row() {
        Text('Email:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.EMAIL\_ADDRESS).selectionMenuHidden(true)
      }

      Row() {
        Text('ID No.:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.ID\_CARD\_NUMBER).selectionMenuHidden(true)
      }

      Row() {
        Text('Address:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.FORMAT\_ADDRESS).selectionMenuHidden(true)
      }

      Button('Save')
        .onClick(() => {
          if (!this.isClicked) {
            // Save historical form input actively.
            try {
              autoFillManager.requestAutoSave(this.getUIContext())
            } catch (err) {
              let e: BusinessError = err as BusinessError;
              hilog.error(0x0000, 'DemoTest', 'error: %{public}d %{public}s', e.code, e.message);
            }
            this.isClicked = true;
            // Set a timeout period to prevent saving historical form input repeatedly.
            setTimeout(() => {
              this.isClicked = false;
            }, 1000)
            // Or switch to another page through routing to trigger the saving of historical form input.
            this.getUIContext().getRouter().pushUrl({
              url: 'xxx'
            })
          }
        })
        .width("50%")
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/TEvI7bZNS8OsRWeqn5x6bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0F0619B5C9208C01E3F13C4A6C9857D0EB418EB5A14633FD195B3BB45A5B2D1)

-   SmartFill saves input when a user switches pages or manually triggers form saving.

-   The clipboard text recognition function has achieved an accuracy of over 90%. Nonetheless, recognition errors may still occur in some scenarios. To ensure the accuracy of form filling, it is recommended that enhanced checks be used at key points, including:
    1.  Format check: automatically checks and corrects the input format.
    2.  Input confirmation: asks users to confirm automatically filled information via a pop-up to prevent errors.
-   If you have provided your own filling suggestion function via pop-ups, you are advised to set the [enableAutoFill](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput#enableautofill11) attribute of involved input components to **false** so the SmartFill function does not conflict with yours.
