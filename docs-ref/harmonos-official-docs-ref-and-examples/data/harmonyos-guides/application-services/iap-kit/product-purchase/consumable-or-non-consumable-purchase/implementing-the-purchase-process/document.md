# Implementing the Purchase Process

#### Use Case

People can use in-app purchase to buy either consumables or non-consumables by making a one-time payment. You can choose to offer either consumables, non-consumables, or both, depending on your specific requirements.

Before implementing the consumable or non-consumable purchase process, you first need to [configure products](../../../preparations/configuring-products/document.md). When a user initiates an in-app purchase, the app brings up the checkout screen of IAP Kit, which shows information such as the product name and price, for the user to complete the purchase.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/vINrIgrrQuG7huxXZR0Vig/en-us_image_0000002446733473.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7F58596AFB0925BA58535DFA7C289277874EE3AF0D67287CB614B1E4BC6F01E "Click to enlarge")

#### Promotional Offers

To make consumables and non-consumables more appealing, IAP Kit allows you to configure promotional offers, that is, promotions for specific user groups.

You can tailor promotional activities to specific user groups in certain regions. Before a purchase is made, your app can retrieve promotional information for a particular product. This information is then passed to IAP Kit and displayed to the user during checkout.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xW8QrPwLT-SKY4ttt2cqsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91DAD596927F6B63059EE76326009AEE8AEA0D383FB160B0D8BAF9DE6270792F)

-   User group–based promotions require the operation of [Generating a Signed Purchase Parameter for a Promotion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-server-subscribe-offer-sign) and are applicable only to apps with servers deployed.
-   There is no limit on the number of times that a user enjoys user group–based promotions.

#### Constraints

The consumable/non-consumable purchase capability supports phones, tablets, and PCs/2-in-1 devices. From version 5.1.0(18), wearables are supported. From version 5.1.1(19), TVs are supported.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/bhf67VbAQAOnE-s-j-Y5MQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF75C6D8A6899DEBF256DC6BB879FAAD885BB7A68CEEACF63FC2CACA2152B19A)

The service process shown below also applies to standalone apps. For a standalone app, the communication between the app and the IAP server is implemented on the app side.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/2Cy_C8yQQsuKz_qjavtyvA/en-us_image_0000002413174332.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACE328E44A139CD39FE616E14B1D60B947D48E94ACF6710C35D3E8EA5A7EBDB8 "Click to enlarge")

**Displaying product information:**

1.  The app sends a [queryEnvironmentStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#en-us_topic_0000001245084266_section192192415554) request to IAP Kit to check whether the service area to which the currently signed-in HUAWEI ID belongs is supported by IAP Kit.
    
    If the request fails, the app needs to hide IAP functions.
    
2.  The app sends a [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) request to IAP Kit to obtain the product information configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
3.  The app displays the list of products that can be purchased based on the returned product information, including the product name and price.

**Initiating and confirming a purchase:**

1.  When a user initiates a purchase, the app sends a [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) request to IAP Kit. The request includes the product ID, product type, and other information. IAP Kit creates an order and displays the checkout screen.
2.  Confirm the purchase result. If the purchase is successful, you can receive the purchase result through the app or app server (recommended).
    
    **Method 1: Receive the purchase result through the app.**
    
    1.  IAP Kit returns [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) containing order information when the user successfully purchases a product.
    2.  The app reports [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) to the app server.
    3.  The app server decodes [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482).jwsPurchaseOrder and performs signature verification. (See [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature) for details of signature verification.) After the verification is successful, the app server obtains the JSON character string [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380).
    
    **Method 2 (Recommended): Receive the purchase result through the app server.**
    
    1.  To improve security, you can enable the [key event notification function](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) so that the IAP server sends a key event notification when the user successfully purchases a product.
    2.  The app server parses **purchaseToken** and **purchaseOrderId** from NotificationPayload.[NotificationMetaData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications#section526717832913) and queries the latest order information from the IAP server through the [order status query](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-query-order-status) API to further guarantee the order information accuracy.
    3.  The IAP server returns the order information [jwsPurchaseOrder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-query-order-status#section860319341390).
    4.  The app server decodes [jwsPurchaseOrder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-query-order-status#section860319341390) and performs signature verification. (See [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature) for details of signature verification.) After the verification is successful, the app server obtains the JSON character string [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380).
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jkDKuISTQAGEZnOAjqxF8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88A6036EAD4D69D0B4BEB791B2ADFC010CE5E82490A7293D06E075E03733A175)

If the purchase fails, ensure that the product can be delivered correctly. For details, please refer to [Delivering a Consumable/Non-consumable Product](../delivering-a-consumable-non-consumable-product/document.md).

**Processing product delivery:**

1.  The app server processes product delivery once the purchase is confirmed. Check [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) for whether relevant products are delivered. If not, deliver them and record the corresponding order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)) for subsequent delivery status check.
2.  The app queries the order delivery status from the app server.
3.  The app server returns the delivery status and order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)).
4.  After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to IAP Kit, telling the IAP server to update the delivery status and complete the purchase process.
    
    After the app successfully executes this step, the IAP server marks the purchased product as delivered. If the product is a consumable, the IAP server will reset it to available for purchase. Then, the user can buy it again. If the product is a non-consumable, the user only needs to purchase the product once and then is entitled to it permanently.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/poMTItVLS8aEuzIjAvhqtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AD3D30DD95989595F1D5655952477164F7A8C53F83B1A8F924FB07FFB9CC060)
    
    This step can also be performed on the app server. The app server can call the [order status query](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-order) API of the IAP server to acknowledge the delivery and complete the purchase process.
    
    Ensure that this step is executed only after successful product delivery. Otherwise, the following problem may occur: the IAP server believed the order has been delivered successfully, but the app server has not actually delivered it.
    

#### Development Procedure

## Displaying Product Information

1.  Check whether IAP Kit is available for your app.
    
    To use IAP Kit, the app needs to send a [queryEnvironmentStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#en-us_topic_0000001245084266_section192192415554) request to this kit to check whether the service area to which the currently signed-in HUAWEI ID belongs is supported by IAP Kit. If the request fails, the app needs to hide IAP functions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/KocnG3F7SzCkobr1bLrkCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C55F4ED605A6C390D267EBFE2C1A5B1C04EE6B2EB105F425822E1C05006A8BAF)
    
    IAP Kit is temporarily available only in the Chinese mainland.
    
    import { iap } from '@kit.IAPKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Index {
      queryEnvironmentStatus(context: common.UIAbilityContext) {
        iap.queryEnvironmentStatus(context).then(() => {
        // The request succeeded.
          console.info('Succeeded in querying environment status.');
        }).catch((err: BusinessError) => {
        // The request failed.
          console.error(\`Failed to query environment status. Code is ${err.code}, message is ${err.message}\`);
        });
      }
    
      build() {}
    }
    

2.  Display the product list.
    
    The app calls the [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) API to obtain the product information configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). The request parameter [QueryProductsParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1033653365917) must contain the IDs and types of products to be queried.
    
    Upon a successful API call, IAP Kit will return the list of product information ([Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313)), including the product price, name, and description. Based on the returned [Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313) information, the app shows the list of products available for purchase.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/qMw9BVfBQGii9EyzpgAbxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99CD2039AABD718F067D35B3BC2004F989C53782C77E3700700EF0D552C4F8D0)
    
    Each request to [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) can query only one product type, with a limit of up to 200 products. Otherwise, an error will be reported.
    
    import { iap } from '@kit.IAPKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Index {
      queryProducts(context: common.UIAbilityContext) {
        const queryProductParam: iap.QueryProductsParameter = {
        // iap.ProductType.CONSUMABLE: consumable
        // iap.ProductType.NONCONSUMABLE: non-consumable
          productType: iap.ProductType.CONSUMABLE,
        // Use the IDs of products you configured in AppGallery Connect as the value of **productIds**.
          productIds: \['ohos\_consume\_001'\]
        };
        iap.queryProducts(context, queryProductParam).then(() => {
        // The request succeeded.
          console.info('Succeeded in querying products.');
        // Show the product information.
          // ...
        }).catch((err: BusinessError) => {
        // The request failed.
          console.error(\`Failed to query products. Code is ${err.code}, message is ${err.message}\`);
        });
      }
    
      build() {}
    }
    

## Initiating a Purchase

After a user initiates a purchase, the app sends a [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) request to IAP Kit, asking it to show the checkout screen. The request parameter [PurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1340120344598) must contain the product ID (valid) and product type configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

To support the function of purchasing multiple products (consumables only) at a time, add the **quantity** parameter to **PurchaseParameter**. The value of **quantity** ranges from 1 to 10.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/r3646IdvSpO-d0xJFOxqLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA548B144F91ABD221026FAAAEBE674B1B5C747009B6261097AB76F44E55D08F)

During development, you need to control the API call frequency. For details, please refer to [1001860004 API Calls Too Frequent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-error-code#section10919174355114).

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  createPurchase(context: common.UIAbilityContext) {
    const createPurchaseParam: iap.PurchaseParameter = {
    // iap.ProductType.CONSUMABLE: consumable
    // iap.ProductType.NONCONSUMABLE: non-consumable
      productType: iap.ProductType.CONSUMABLE,
    // Use the ID of a product you configured in AppGallery Connect as the value of **productId**.
      productId: 'ohos\_consume\_001'
    };
    iap.createPurchase(context, createPurchaseParam).then((result) => {
      console.info('Succeeded in creating purchase.');
    // The purchase succeeded. Process the purchase result.
    // For details about the implementation of **dealPurchaseResult**, see the next section.
      this.dealPurchaseResult(result);
    }).catch((err: BusinessError) => {
    // The purchase failed.
      console.error(\`Failed to create purchase. Code is ${err.code}, message is ${err.message}\`);
    // For details about the implementation of **dealPurchaseError**, see the next section.
      this.dealPurchaseError(err);
    })
  }

  build() {}
}

## Processing the Purchase Result

**\[Result 1: The purchase is successful.\]**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/jcW_J8ZyS5exmYxxjnwjRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C65918EEA1D59ACC52B6CB3256D178224407C2D18941B046CA9F563A10762E6)

1.  For security purposes, it is recommended that your app server enable [key event notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) to receive the purchase success result, [decode and verify the signature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature), and complete the purchase.
2.  Make sure that the delivery is successful before the complete-the-purchase step. In this step, you can request the [delivery acknowledgement](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-order) API of the IAP server to acknowledge the delivery and complete the purchase process.

The following describes how to **receive the purchase result through the app** and process the result.

1.  Upon a successful purchase, the app receives a [CreatePurchaseResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section193852021105111) object, in which [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) contains the purchase result.
2.  Decode [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482).jwsPurchaseOrder and perform signature verification by referring to [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature). If the verification is successful, the JSON character string [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) will be returned. It is recommended that the app send [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) to the app server so that this task can be executed on the app server.
3.  After successful signature verification, if [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380).purchaseOrderRevocationReasonCode is empty, the purchase is successful, and the product can be delivered.
    
    You are advised to check the product delivery status of the order. If the product is not delivered, deliver it. After the delivery is successful, record relevant information such as [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) for subsequent check.
    
4.  Complete the purchase.
    
    After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to acknowledge the delivery, telling the IAP server to update the delivery status and complete the purchase process. **productType**, **purchaseToken**, and **purchaseOrderId** in [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) must be passed to [FinishPurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section103714142118) in the [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request.
    
    After the app successfully executes this step, the IAP server marks the purchased product as delivered. If the product is a consumable, the IAP server will reset it to available for purchase. Then, the user can buy it again. If the product is a non-consumable, the user only needs to purchase the product once and then is entitled to it permanently.
    
    import { iap } from '@kit.IAPKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // **JWSUtil** is a custom class. For details, please refer to the [sample code](../../../getting-started/document.md#section698882222912).
    import { JWSUtil } from '../common/JWSUtil';
    
    @Entry
    @Component
    struct Index {
      /\*\*
       \* Process the purchase result.
       \*
       \* @param result Purchase result.
       \*/
      dealPurchaseResult(context: common.UIAbilityContext, result: iap.CreatePurchaseResult) {
        const jwsPurchaseOrder: string = JSON.parse(result.purchaseData).jwsPurchaseOrder;
        if (!jwsPurchaseOrder) {
          return;
        }
      // Decode **jwsPurchaseOrder** and perform signature verification.
        const purchaseStr = JWSUtil.decodeJwsObj(jwsPurchaseOrder);
      // Customize the **PurchaseOrderPayload** class. Check **PurchaseOrderPayload** for the information included in this class.
        const purchaseOrderPayload = JSON.parse(purchaseStr) as PurchaseOrderPayload;
      // Process product delivery.
        // ...
      // After the delivery is successful, send a **finishPurchase** request to IAP Kit to acknowledge the delivery and complete the purchase.
      // The parameter settings of the **finishPurchase** request are obtained from **purchaseOrderPayload**.
        this.finishPurchase(context, purchaseOrderPayload);
      }
    
      /\*\*
    \* Acknowledge the delivery and complete the purchase.
       \*
     \* @param purchaseOrder Order information, which comes from the purchase request.
       \*/
      finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
        const finishPurchaseParam: iap.FinishPurchaseParameter = {
          productType: Number(purchaseOrder.productType),
          purchaseToken: purchaseOrder.purchaseToken,
          purchaseOrderId: purchaseOrder.purchaseOrderId
        };
        iap.finishPurchase(context, finishPurchaseParam).then(() => {
        // The request succeeded.
          console.info('Succeeded in finishing purchase.');
        }).catch((err: BusinessError) => {
        // The request failed.
          console.error(\`Failed to finish purchase. Code is ${err.code}, message is ${err.message}\`);
        });
      }
    
      build() {}
    }
    

**\[Result 2: The purchase fails.\]**

Upon a purchase failure, check whether the product needs to be delivered again for the scenario where the code is [iap.IAPErrorCode.PRODUCT\_OWNED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429) or [iap.IAPErrorCode.SYSTEM\_ERROR](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429). For details, please refer to [Delivering a Consumable/Non-consumable Product](../delivering-a-consumable-non-consumable-product/document.md).

import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';

dealPurchaseError(err: BusinessError) {
  if (err.code === iap.IAPErrorCode.PRODUCT\_OWNED || err.code === iap.IAPErrorCode.SYSTEM\_ERROR) {
    // Follow the instructions in [Delivering a Consumable/Non-consumable Product](../delivering-a-consumable-non-consumable-product/document.md) to check whether the product needs to be redelivered.
    // ...
  }
}
