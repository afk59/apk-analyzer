# Obtaining the Invoice Title

#### Use Case

When an app needs to obtain a user's invoice title, it can use the invoice assistant capability provided by Account Kit to help the user access the invoice title selection screen to select or manage invoice titles. This section describes the function of obtaining an invoice title provided by Account Kit. Additionally, the [invoice title selection button](../../../scenario-fusion-kit/scenario-specific-buttons/invoice-title-selection-button/document.md) provided by Scenario Fusion Kit can be used to obtain an invoice title.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ZwQBjd1IQ0CA9bh_xlsp4Q/en-us_image_0000002528943235.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5393312861A6FC897EF431F63385004327177949565CF32D5F89850114F56E1B "Click to enlarge")

#### Restrictions

The capability of obtaining an invoice title is not supported on wearables and TVs.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/p9ovxRhAQx66J0a7golrag/en-us_image_0000002497223274.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59C1A41C13EDC4D304633F050305BA5FF2422F749E7EB8DC9E98D5EDB48223D5 "Click to enlarge")

The process is as follows:

1.  When the user needs to use an invoice title, the app calls the API for selecting an invoice title to show the screen where the user can select an invoice title.
2.  Then, the user can select an existing invoice title on this screen or redirect to the invoice title management screen to add a new one. The invoice title finally confirmed by the user will be returned to the app.

#### API Description

The table below lists the key API for obtaining the invoice title of a user. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-invoiceassistant).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[selectInvoiceTitle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-invoiceassistant#section162103412610)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-common#context)): Promise<[InvoiceTitle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-invoiceassistant#section9615740103819)\>

 | 

Shows the invoice title selection screen and returns the selected invoice title asynchronously through a promise.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/l6dskxFCS6OllUh2cdiPCQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB0E237434594B01A047E3E4286E542014C60E9A046E914BC58705DFA0B35FBC)

The above APIs must be called within the lifecycle of a page or custom component.

#### Prerequisites

Before coding, make sure that you have [configured the signing information and fingerprint](../../getting-started/configuring-signing-information-and-fingerprint/document.md) and also [set the client ID](../../getting-started/configuring-the-client-id/document.md). No additional scope or permission needs to be requested for the scenario described in this topic.

#### Development Procedure

1.  Import the [invoiceAssistant](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-invoiceassistant) module and related common modules.
    
    import { invoiceAssistant } from '@kit.AccountKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [selectInvoiceTitle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-invoiceassistant#section162103412610) method to show the invoice title selection screen.
    
    // Execute the request.
    if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
      try {
        // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
        invoiceAssistant.selectInvoiceTitle(this.getUIContext().getHostContext())
          .then((data: invoiceAssistant.InvoiceTitle) => {
            hilog.info(0x0000, 'testTag', 'Succeeded in selecting invoice title');
            const type: string = data.type;
            const title: string = data.title;
            const taxNumber: string = data.taxNumber;
            const companyAddress: string = data.companyAddress;
            const telephone: string = data.telephone;
            const bankName: string = data.bankName;
            const bankAccount: string = data.bankAccount;
    
          // Process **type**, **title**, **taxNumber**, **companyAddress**, **telephone**, **bankName**, and **bankAccount**.
            // ...
    
          })
          .catch((error: BusinessError<Object>) => {
            dealAllError(error);
          })
      } catch (error) {
        dealAllError(error);
      }
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device does not support the invoking of the selectInvoiceTitle interface.');
    }
    
    // Handle the error.
    function dealAllError(error: BusinessError<Object>): void {
      hilog.error(0x0000, 'testTag', \`Failed to selectInvoiceTitle. Code: ${error.code}, message: ${error.message}\`);
    }
