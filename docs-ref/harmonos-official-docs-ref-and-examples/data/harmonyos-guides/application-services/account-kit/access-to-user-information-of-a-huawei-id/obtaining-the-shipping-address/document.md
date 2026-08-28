# Obtaining the Shipping Address

#### Use Case

Account Kit provides the ability to obtain a user's shipping address, which can be an existing one selected or a new one added by the user. This section describes the function of obtaining a shipping address provided by Account Kit. Additionally, the [shipping address selection button](../../../scenario-fusion-kit/scenario-specific-buttons/shipping-address-selection-button/document.md) provided by Scenario Fusion Kit can be used to obtain a shipping address.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Rr1nJ42ZQHee7l9Px-w1jw/en-us_image_0000002528943241.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F059EA0F3DC678D26B6C38C85CDDC7B7A1529F54C7637AF059314068A746B49 "Click to enlarge")

#### Restrictions

1.  Shipping addresses and associated mobile numbers must be from the Chinese mainland only.
2.  The capability of obtaining a shipping address is not supported on wearables and TVs.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/XiIJrnRySue3ZPfLF-FS8A/en-us_image_0000002497063290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE46A0729B37456403CBB9F0EC8156142618E75E87B94D47992A9863935A467F)

The process is as follows:

1.  When a user needs to specify a shipping address, the app calls the shipping address selection API to show the shipping address management screen of Account Kit.
2.  The user can add a shipping address or select an existing one on the shipping address management screen. After the user confirms the operation, the added or selected shipping address is returned to the app.

#### API Description

The table below lists the key API for obtaining the shipping address of a user. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-choose-address).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[chooseAddress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-choose-address#section0668846105912)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-common#context)): Promise<[AddressInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-choose-address#section9615740103819)\>

 | 

Shows the shipping address management screen and returns the shipping address specified by a user.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/c5n5IFi5RHWY7-YfildMyQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A24F362BF809E06046BF284A2565DB02BACFFCF7E8A62B298F9AF3666732A0E)

The above APIs must be called within the lifecycle of a page or custom component.

#### Prerequisites

Before coding, make sure that the following preparations are complete:

1\. [Apply for necessary scopes and permissions](../../getting-started/requesting-scopes/document.md). If the API for obtaining a user's shipping address is called when you have not obtained the relevant scope, error [1008100005](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-error-code#section515972151510) will be returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/M3oNeKX-TqOU-WY4FZDb3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EDB1E942E016BCC98BADAA9B35FA87876023BF208088AE0951D672DCB012DDB)

If you have configured signing information and added a fingerprint before applying for necessary scopes, you will need to [reapply for a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278) and [sign your app manually](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section112371245115818).

2\. [Configure the signing information and fingerprint](../../getting-started/configuring-signing-information-and-fingerprint/document.md) and [configure the client ID](../../getting-started/configuring-the-client-id/document.md). If the API for obtaining a user's shipping address is called when you have not completed the two configuration tasks, error [1008100004 App Certificate Fingerprint Verification Failure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-error-code#section1415952110158) will be returned.

#### Development Procedure

1.  Import the [shippingAddress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-choose-address) module and related common modules.
    
    import { shippingAddress } from '@kit.AccountKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [chooseAddress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-choose-address#section0668846105912) method to show the shipping address management screen, on which the user can select or add an address. Then, the address finally confirmed by the user will be sent to the app.
    
    // Execute the request.
    try {
      // The following provides only code snippets. Use it in the custom component instance to obtain the UIContext object as the input parameter of the function.
      shippingAddress.chooseAddress(this.getUIContext().getHostContext()).then((data: shippingAddress.AddressInfo) => {
        hilog.info(0x0000, 'testTag', 'Succeeded in choosing address.');
        const userName: string = data.userName;
        const mobileNumber: string = data.mobileNumber;
        const countryCode: string = data.countryCode;
        const provinceName: string = data.provinceName;
        const cityName: string = data.cityName;
        const districtName: string = data.districtName;
        const streetName: string = data.streetName;
        const detailedAddress: string = data.detailedAddress;
        // Process the obtained shipping address information.
      }).catch((error: BusinessError) => {
        dealAllError(error);
      })
    } catch (error) {
      dealAllError(error);
    }
    
    // Handle the error.
    function dealAllError(error: BusinessError): void {
      hilog.error(0x0000, 'testTag', \`Failed to chooseAddress. Code: ${error.code}, message: ${error.message}\`);
    }
