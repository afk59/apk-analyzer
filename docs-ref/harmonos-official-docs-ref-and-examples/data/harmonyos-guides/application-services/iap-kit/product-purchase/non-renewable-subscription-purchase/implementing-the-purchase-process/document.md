# Implementing the Purchase Process

#### Use Case

After purchasing a non-renewable subscription, users can access the app's premium features or content for a specific period. Once this period ends, access will be restricted unless they purchase another auto-renewable or non-renewable subscription.

Before implementing the non-renewable subscription purchase process, you first need to [configure products](../../../preparations/configuring-products/document.md). When a user initiates an in-app purchase, the app brings up the checkout screen of IAP Kit, which shows information such as the product name and price, for the user to complete the purchase.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/TBVjhfxDR321F0w4KbMDwA/en-us_image_0000002413174344.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21E51864392562AD034E99B9D1456BFFADBCED76EA69710BC143FF9BA1065D0A "Click to enlarge")

#### Promotional Offers

To make non-renewable subscriptions more appealing, IAP Kit allows you to configure promotional offers, that is, promotions for specific user groups.

You can tailor promotional activities to specific user groups in certain regions. Before a purchase is made, your app can retrieve promotional information for a particular product. This information is then passed to IAP Kit and displayed to the user during checkout.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/OpvlKXr5T5OvkmU7yAPZCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79ECB32F47F8EFB349492E72716C3C821609FDE6D2D92FFDD2ABA0DE0163495C)

-   User group–based promotions require the operation of [Generating a Signed Purchase Parameter for a Promotion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-server-subscribe-offer-sign) and are applicable only to apps with servers deployed.
-   There is no limit on the number of times that a user enjoys user group–based promotions.

#### Constraints

The non-renewable subscription purchase capability supports phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.1(19), TVs are also supported.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/HqF3sIUFTNS9Gl_WmzyaiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE977BDB6DFE64BA446EFE407E3CFDCC06E914D515D42F03A3897D8CDC11B9C4)

The service process shown below also applies to standalone apps. For a standalone app, the communication between the app and the IAP server is implemented on the app side.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/l1CRmZuaRbeglu1q5nvHwA/en-us_image_0000002446613561.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=417B94503B29EBAFB03E91C54B5DDAC35D6AE5859061C835645BF98FEE7FDA60 "Click to enlarge")

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
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/jkERsMz6RbCeAGgyH61cxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC05423C3BCD8BC8759B1A7A8D47870BA8DE41F5A3FCED04651CE9922F75BEE8)

If the purchase fails, ensure that the product can be delivered correctly. For details, please refer to [Delivering a Non-renewable Subscription Product](../delivering-a-non-renewable-subscription-product/document.md).

**Processing product delivery:**

1.  The app server processes product delivery. Check [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) for whether relevant products are delivered. If not, deliver them and record the corresponding order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)) for subsequent delivery status check.
2.  The app queries the order delivery status from the app server.
3.  The app server returns the delivery status and order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)).
4.  After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to IAP Kit, telling the IAP server to update the delivery status and complete the purchase process.
    
    After the app successfully executes this step, the IAP server marks the purchased product as delivered. For a non-renewable subscription, the IAP server will reset the product status to available for purchase. Then, the user can purchase the product again. (Stacking subscription durations can be adopted as needed. If stacking is allowed, after purchasing a non-renewable subscription, and before the current period ends, a user can purchase another non-renewable subscription. This new subscription would seamlessly connect to the end of the previous one. If stacking is not allowed, then a user must wait until the current subscription period is over before purchasing another. You have the final say on whether "stacking subscription durations" is supported.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/QvXDxX-RTXmGMYB2WCMBuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C54589DD4578D02C991E535B9F378EDC62BD8FFF96A97D9BF2619310158522CD)
    
    -   This step can also be performed on the app server. The app server can call the [order status query](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-order) API of the IAP server to acknowledge the delivery and complete the purchase process.
    -   Ensure that this step is executed only after successful product delivery. Otherwise, the following problem may occur: the IAP server believed the order has been delivered successfully, but the app server has not actually delivered it.
    

#### Development Procedure

## Displaying Product Information

1.  Check whether IAP Kit is available for your app.
    
    To use IAP Kit, the app needs to send a [queryEnvironmentStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#en-us_topic_0000001245084266_section192192415554) request to this kit to check whether the service area to which the currently signed-in HUAWEI ID belongs is supported by IAP Kit. If the request fails, the app needs to hide IAP functions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/lDTEA2SYS2CK6F56ZuMGyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF381E911470BBA5B033607F2AE9D5888F28C11881DB73ED47371D77109BBD58)
    
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
    
    The app calls the [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) API to obtain the product information configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). For a query request, the product IDs must be contained in [QueryProductsParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1033653365917) and **productType** must be set to **NONRENEWABLE**.
    
    Upon a successful API call, IAP Kit will return the list of product information ([Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313)), including the product price, name, and description. Based on the returned [Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313) information, the app shows the list of products available for purchase.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/SwAkiYwfQo2w0ubxgbbcOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0C100203DA79D6F934BA2EB6F5EF71FA751DD35DE2A6451D36F3FE14AAB180F)
    
    Each request to [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) can query only one product type, with a limit of up to 200 products. Otherwise, an error will be reported.
    
    import { iap } from '@kit.IAPKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Index {
    
      queryProducts(context: common.UIAbilityContext) {
        const queryProductParam: iap.QueryProductsParameter = {
        // iap.ProductType.NONRENEWABLE: Non-renewable subscription.
          productType: iap.ProductType.NONRENEWABLE,
        // Use the IDs of products you configured in AppGallery Connect as the value of **productIds**.
          productIds: \['ohos\_nonrenewable\_001'\]
        };
        iap.queryProducts(context, queryProductParam).then((result) => {
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

After a user initiates a purchase, the app sends a [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) request to IAP Kit, asking it to show the checkout screen. The request parameter [PurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1340120344598) must contain the product ID (valid) configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and **productType** with the value **NONRENEWABLE**.

To support the function of purchasing multiple products at a time, add the **quantity** parameter to [PurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1340120344598). The value of **quantity** ranges from **1** to **10**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/8JeAG6MeR5GCcQRd0G3y9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F3A0493EDE953355539E7B1A5F63D4BB8672FCA382F0201C19237C11621399F)

During development, you need to control the API call frequency. For details, please refer to [1001860004 API Calls Too Frequent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-error-code#section10919174355114).

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {

  createPurchase(context: common.UIAbilityContext) {
    const createPurchaseParam: iap.PurchaseParameter = {
    // iap.ProductType.NONRENEWABLE: Non-renewable subscription.
      productType: iap.ProductType.NONRENEWABLE,
    // Use the ID of a product you configured in AppGallery Connect as the value of **productId**.
      productId: 'ohos\_nonrenewable\_001'
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/qH38u04LSUmmQBxnncJvwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=209ED8D49F8933F5C27E8AC2EBE40E6B6C9FDB94237EBC1A33008BE19620EEF7)

1.  For security purposes, it is recommended that your app server enable [key event notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) to receive the purchase success result, [decode and verify the signature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature), and complete the purchase.
2.  Make sure that the delivery is successful before the complete-the-purchase step. In this step, you can request the [delivery acknowledgement](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-order) API of the IAP server to acknowledge the delivery and complete the purchase process.

The following describes how to **receive the purchase result through the app** and process the result.

1.  Upon a successful purchase, the app receives a [CreatePurchaseResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section193852021105111) object, in which [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) contains the purchase result.
2.  Decode [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482).jwsPurchaseOrder and perform signature verification by referring to [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature). If the verification is successful, the JSON character string [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) will be returned. It is recommended that the app send [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) to the app server so that this task can be executed on the app server.
3.  After successful signature verification, if [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380).purchaseOrderRevocationReasonCode is empty, the purchase is successful, and the product can be delivered.
    
    You are advised to check the product delivery status of the order. If the product is not delivered, deliver it. After the delivery is successful, record relevant information such as [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) for subsequent check.
    
4.  Complete the purchase.
    
    After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to acknowledge the delivery, telling the IAP server to update the delivery status and complete the purchase process. **productType**, **purchaseToken**, and **purchaseOrderId** in [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) must be passed to [FinishPurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section103714142118) in the [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request.
    
    After the app successfully executes this step, the IAP server marks the purchased product as delivered. If the product is a non-renewable subscription, the IAP server will reset it to available for purchase. Then, the user can buy it again.
    
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

Upon a purchase failure, check whether the product needs to be delivered again for the scenario where the code is [iap.IAPErrorCode.PRODUCT\_OWNED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429) or [iap.IAPErrorCode.SYSTEM\_ERROR](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429). For details, please refer to [Delivering a Non-renewable Subscription Product](../delivering-a-non-renewable-subscription-product/document.md).

dealPurchaseError(err: BusinessError) {
  if (err.code === iap.IAPErrorCode.PRODUCT\_OWNED || err.code === iap.IAPErrorCode.SYSTEM\_ERROR) {
    // Follow the instructions in the relevant product delivery section to check whether the product needs to be redelivered.
    // ...
  }
}
