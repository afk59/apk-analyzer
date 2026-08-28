# Invoice Title Selection Button

#### Use Case

You can call the invoice title selection button component to show the page for users to select from saved invoice titles.

Run the sample code and tap **Select invoice title**. Saved invoice titles are displayed for you to select. You can also tap **Manage/Add invoice header** to access the page for adding an enterprise/individual invoice title. For details, please refer to [Obtaining the Invoice Title](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-invoice-title/document.md).

#### Prerequisites

For details, please refer to [Prerequisites](../../../account-kit/access-to-user-information-of-a-huawei-id/obtaining-the-invoice-title/document.md#section74611018114315).

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
                // **OpenType.CHOOSE\_INVOICE\_TITLE** indicates that the button is used to select an invoice title.
                openType: functionalButtonComponentManager.OpenType.CHOOSE\_INVOICE\_TITLE,
                label: 'Select invoice title',
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
              // When **OpenType** is set to **CHOOSE\_INVOICE\_TITLE**, the callback must be **onChooseInvoiceTitle**.
              controller: new functionalButtonComponentManager.FunctionalButtonController()
                .onChooseInvoiceTitle((err, data) => {
                  if (err) {
                    // Error processing.
                    hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                    return;
                  }
                  // Success processing.
                  hilog.info(0x0000, "testTag", "succeeded in obtaining invoice title");
                  // Obtain invoice information.
                  let type: string = data.type;
                  let title: string = data.title;
                  let taxNumber: string = data.taxNumber;
                  let companyAddress: string | undefined = data.companyAddress;
                  let telephone: string | undefined = data.telephone;
                  let bankName: string | undefined = data.bankName;
                  let bankAccount: string | undefined = data.bankAccount;
                })
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/J8fJqyrbRqKWSY8_Pn9-qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CB4F1AAE32457EE2CB653ADD46F40E56BC486EEE39DF72198576605F3AB3543)
    
    -   Set **openType** to **functionalButtonComponentManager.OpenType.CHOOSE\_INVOICE\_TITLE** to specify the purpose of the button as to select an invoice title.
    -   Set **controller** to **new functionalButtonComponentManager.FunctionalButtonController().onChooseInvoiceTitle**.
    -   You can use the custom **Modifier** to set the button style. For details, please refer to the [Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#section1251915241170).
    
    For details about other parameters, please refer to [FunctionalButton (Button Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-functionalbutton).
