# Payment in Mini Games

After integrating the mini game payment APIs of the basic game service, your mini game can offer paid products, enabling in-game purchases for players.

#### Prerequisites

-   You have made [all necessary preparations](../preparations/document.md).
-   You have enabled the [Merchant Service](https://developer.huawei.com/consumer/en/doc/start/merchant-service-0000001053025967).
-   You have [added digital products](https://developer.huawei.com/consumer/en/doc/app/create-digital-goods-0000001958955105) for your mini game in AppGallery Connect.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/yhEm6-6PS8K28xqLztepTA/en-us_image_0000002474151174.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99FCA5E354DF90E9EFB4C87C3B76879C56E35A9F58BF081E75DC8D8473DFC3D9)

1.  A player purchases a product in the mini game.
2.  The mini game calls [miniGamePay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section91831924175010) to send a payment request to Game Service Kit.
3.  Game Service Kit sends a request to IAP Kit to start the cashier, and IAP Kit processes the payment request. For details, please refer to [Product Purchase](../../../../iap-kit/product-purchase/document.md).
4.  After completing the processing, IAP Kit returns the purchase result to Game Service Kit.
5.  Game Service Kit returns the purchase result. You will receive a [CreatePurchaseResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section193852021105111) object, in which the **purchaseData** field contains the purchase result.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer).

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void

 | 

Initializes Game Service Kit using the default context. This API returns the result through a callback.

 |
| 

[miniGamePay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section91831924175010)(context: common.Context, parameter: PurchaseParameter): Promise<CreatePurchaseResult>

 | 

Mini game payment API. This API returns the result through a promise.

 |

#### Development Procedure

## Importing Modules

Import Game Service Kit and common modules.

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

## Performing Initialization

Call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719) API to initialize Game Service Kit.

onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent("pages/index", (err, data) => {
    try {
      gamePlayer.init(this.context,()=>{
        hilog.info(0x0000, 'testTag', \`Succeeded in initializing.\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to init. Code: ${err.code}, message: ${err.message}\`);
    }
  });
}

## Initializing a Payment Request

Call [miniGamePay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section91831924175010) to send a payment request to Game Service Kit. Game Service Kit requests IAP Kit to start the cashier and process the payment request. After processing the payment request, IAP Kit sends information including the purchase result to Game Service Kit, which then returns the information to you using the [CreatePurchaseResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section193852021105111) object.

let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.PurchaseParameter = {
  productId: 'xxx', // ID of the product to be paid for.
  productType: 0, // Product type to be queried.
  developerPayload: 'xxx', // Reserved for the merchant-side information. The length range of this parameter is \[0, 256\]. If this parameter is specified, its value will be returned to your app in a payment success callback.
  reservedInfo: 'xxx' // Additional information, which is a JSON string. Extra fields can be included as key-value pairs within this JSON string.
};
try {
  gamePlayer.miniGamePay(context, request).then((result: gamePlayer.CreatePurchaseResult) => {
    hilog.info(0x0000, 'testTag', \`Succeeded in paying\`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', \`Failed to pay. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to pay. Code: ${err.code}, message: ${err.message}\`);
}
