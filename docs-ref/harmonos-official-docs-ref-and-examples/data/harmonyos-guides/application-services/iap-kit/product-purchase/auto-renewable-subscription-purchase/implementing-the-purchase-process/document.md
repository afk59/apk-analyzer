# Implementing the Purchase Process

#### Constraints

The auto-renewable subscription capability supports phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.1(19), TVs are also supported.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/WR3FzxSlRaORl8tcDX83fA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3AA630F789A1EA5B8283B29F1825A79AF516B9F107DA36AA9E7522F4DC2DBE4)

The service process shown below also applies to standalone apps. For a standalone app, the communication between the app and the IAP server is implemented on the app side.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/7AQwr-wzQdGfliVtXdgiZQ/en-us_image_0000002413174328.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B51CF3E2D795D7246B0D009A871082CF214B4477B47459626E38A6A6E0DDCAB "Click to enlarge")

**Displaying product information:**

1.  The app sends a [queryEnvironmentStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#en-us_topic_0000001245084266_section192192415554) request to IAP Kit to check whether the service area to which the currently signed-in HUAWEI ID belongs is supported by IAP Kit.
    
    If the request fails, the app needs to hide IAP functions.
    
2.  The app sends a [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) request to IAP Kit to obtain the product information configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
3.  The app displays the list of products that can be purchased based on the returned product information, including the product name and price.

**Checking the service delivery status:**

1.  The app sends a [queryPurchases](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1147122418532) request to IAP Kit to obtain the list of active subscriptions. IAP Kit returns the [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) list. [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) is a JWS-format string that contains the relevant subscription information.
2.  The app displays the product subscription status. The purchase entry of products in auto-renewable state needs to be shielded. Additionally, the app handles the delivery of the services.
3.  If the delivery of a product is not acknowledged, after the product is delivered, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to IAP Kit to instruct the IAP server to update the delivery status of the product and complete the purchase process. After the app successfully executes [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814), the IAP server marks the purchased products as delivered.
    
    This step can also be performed on the app server. The app server can call the IAP server's API for [Acknowledging the Delivery for a Subscription](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-sub) to acknowledge the delivery and complete the purchase process.
    

For details, please refer to [Product Delivery for an Active Subscription](../delivering-an-auto-renewable-subscription-product/document.md#section1369619716116).

**Initiating and confirming a purchase:**

1.  When a user initiates a purchase, the app sends a [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) request to IAP Kit. The request includes the product ID, product type, and other information. IAP Kit creates an order and displays the checkout screen.
2.  Confirm the purchase result. If the purchase is successful, you can receive the purchase result through the app or app server (recommended).
    
    **Method 1: Receive the purchase result through the app.**
    
    1.  IAP Kit returns [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) containing subscription status information when the user successfully purchases a product.
    2.  The app reports [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) to the app server.
    3.  The app server decodes [PurchaseData.jwsSubscriptionStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) and performs signature verification by referring to [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature). Upon a successful verification, the [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318) JSON string will be returned.
    
    **Method 2 (Recommended): Receive the purchase result through the app server.**
    
    1.  To improve security, you can enable the [key event notification function](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) so that the IAP server sends a key event notification when the user successfully purchases a product.
    2.  The app server parses **purchaseToken** and **purchaseOrderId** from NotificationPayload.[NotificationMetaData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications#section526717832913) and queries the latest subscription status information from the IAP server through the API for [Querying the Subscription Status](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-query-subscription-status) to further guarantee the information accuracy.
    3.  The IAP server returns [jwsSubGroupStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-query-subscription-status#section96323317194).
    4.  The app server decodes [jwsSubGroupStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-query-subscription-status#section96323317194) and performs signature verification by referring to [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature). Upon a successful verification, the [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318) JSON string will be returned.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/u2UxtqkKRiyFRY3VnpGt_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EC652A4F18175630EA2B3E6F8DD9DB41763EFC072991FC56645FB269B4BA069)

If the purchase fails, ensure that the product can be delivered correctly. For details, please refer to [Subscription Delivery Guarantee](../delivering-an-auto-renewable-subscription-product/document.md#section1880231055910).

**Processing product delivery:**

1.  The app server processes product delivery once the purchase is confirmed. Check [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318).lastSubscriptionStatus.lastPurchaseOrder for whether the products are delivered. If not, deliver them and record the corresponding order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)) for subsequent delivery status check.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/gTIgKNAEStiqrSY0GJXFJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95FBFB43A7105CDDF95582A427F86556F33C5DE1C3764D460352A7659D1160B6)
    
    It is recommended that user services be associated with subscription status for standalone apps. The user will be entitled to access relevant services as long as the subscription is active.
    
2.  The app queries the order delivery status from the app server.
3.  The app server returns the delivery status and order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)).
4.  After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to IAP Kit, telling the IAP server to update the delivery status and complete the purchase process. After the app successfully executes [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814), the IAP server marks the purchased product as delivered. Then the products can be renewed properly.
    
    This step can also be performed on the app server. The app server can call the IAP server's API for [Acknowledging the Delivery for a Subscription](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-sub) to acknowledge the delivery and complete the purchase process.
    

#### Development Procedure

## Displaying Product Information

1.  Check whether IAP Kit is available for your app.
    
    To use IAP Kit, the app needs to send a [queryEnvironmentStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#en-us_topic_0000001245084266_section192192415554) request to this kit to check whether the service area to which the currently signed-in HUAWEI ID belongs is supported by IAP Kit. If the request fails, the app needs to hide IAP functions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/qFu2tbILSECGKjtyruEB9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65513B350DD4C9D82D8105AD912AE75E6C27F7FD0B5D36B45BEE37FEE6734986)
    
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
    
    The app calls the [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) API to obtain the product information configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). For a query request, the product IDs must be contained in [QueryProductsParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1033653365917) and **productType** must be set to [iap.ProductType.AUTORENEWABLE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section59035422210).
    
    Upon a successful API call, IAP Kit will return the list of product information ([Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313)), including the product price, name, and description. Based on the returned [Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313) information, the app shows the list of products available for purchase.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/CcGe-IWcTRCZucDOkIq50A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F3750454E61B01ABEA375ABA255E738ACFECE9007EFD8BD77F4AEE7181CBD41)
    
    Each request to [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) can query only one product type, with a limit of up to 200 products. Otherwise, an error will be reported.
    
    import { iap } from '@kit.IAPKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Index {
    
      queryProducts(context: common.UIAbilityContext) {
        const queryProductParam: iap.QueryProductsParameter = {
          productType: iap.ProductType.AUTORENEWABLE,
        // Use the IDs of products you configured in AppGallery Connect as the value of **productIds**.
          productIds: \['product1', 'product2', 'product3'\]
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
    

## Displaying the Subscription Status and Delivering Services

1.  The app obtains the list of active subscriptions.
2.  The app displays the product subscription status. The purchase entry of products in auto-renewable state needs to be shielded.
3.  The app processes the delivery of services for active subscriptions.

For details, please refer to [Product Delivery for an Active Subscription](../delivering-an-auto-renewable-subscription-product/document.md#section1369619716116).

## Initiating a Purchase

After a user initiates a purchase, the app sends a [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) request to IAP Kit, asking it to show the checkout screen. For a purchase request, the ID (that you configure for an auto-renewable subscription beforehand in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and must be still valid) must be contained in [PurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1340120344598) and **productType** must be set to [iap.ProductType.AUTORENEWABLE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section59035422210).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/qcdvYfWGQJO7CmAEKN5Xmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9134C14412BB658DC8AE43F95A9C3B9C8756723B2582AAA81D552193869865BF)

During development, you need to control the API call frequency. For details, please refer to [1001860004 API Calls Too Frequent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-error-code#section10919174355114).

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {

  subscribe(context: common.UIAbilityContext) {
    const createPurchaseParam: iap.PurchaseParameter = {
      productType: iap.ProductType.AUTORENEWABLE,
    // Use the ID of a product you configured in AppGallery Connect as the value of **productId**.
      productId: 'test001'
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/xjmFZVmCRImnCLw_on1rgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6DEFD0804D7F3FA1A7EB472C3D80CCFD0B464A8CB1A4A25859A3BE90618ADD0)

1.  For security purposes, it is recommended that your app server enable [key event notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) to receive the purchase success result, [decode and verify the signature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature), and complete the purchase.
2.  Make sure that the delivery is successful before the complete-the-purchase step. In this step, you can request the IAP server's API for [Acknowledging the Delivery for a Subscription](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-sub) to acknowledge the delivery and complete the purchase process.

The following describes how to **receive the purchase result through the app** and process the result.

1.  Upon a successful purchase, the app receives a [CreatePurchaseResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section193852021105111) object, in which [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) contains the purchase result.
2.  Decode [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482).jwsSubscriptionStatus and perform signature verification by referring to [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature). Upon a successful verification, the [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318) JSON string will be returned. It is recommended that the app send [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) to the app server so that this task can be executed on the app server.
3.  After the signature verification is successful, check whether the value of [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318).lastSubscriptionStatus.status is **1** (active). If so, the user will be entitled to access relevant services.
    
    You are advised to check the product delivery status of the order. If the product is not delivered, deliver it. After the delivery is successful, record relevant information such as [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318).lastSubscriptionStatus.lastPurchaseOrder for subsequent check.
    
4.  Complete the purchase.
    
    After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to acknowledge the delivery, telling the IAP server to update the delivery status and complete the purchase process. **productType**, **purchaseToken**, and **purchaseOrderId** in [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) must be passed to [FinishPurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section103714142118) in the [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request. Obtain [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) from [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318).lastSubscriptionStatus.lastPurchaseOrder. After the request is successful, the IAP server marks the product as delivered.
    

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
    const jwsSubscriptionStatus: string = JSON.parse(result.purchaseData).jwsSubscriptionStatus;
    if (!jwsSubscriptionStatus) {
      return;
    }
    const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
    if (!subscriptionStatus) {
      return;
    }
// Customize the **SubGroupStatusPayload** class. Check [SubGroupStatusPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section1311343185318) for the information included in this class.
    const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
    const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
    if (!lastSubscriptionStatus || lastSubscriptionStatus.status !== '1') {
      return;
    }
    const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
    if (purchaseOrderPayload === undefined) {
      return;
    }
    // Process product delivery.
    // ...
  // After the delivery is successful, send a **finishPurchase** request to IAP Kit to acknowledge the delivery and complete the purchase.
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

Upon a purchase failure, check whether the product needs to be delivered again for the scenario where the code is [iap.IAPErrorCode.PRODUCT\_OWNED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429) or [iap.IAPErrorCode.SYSTEM\_ERROR](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429). For details, please refer to [Subscription Delivery Guarantee](../delivering-an-auto-renewable-subscription-product/document.md#section1880231055910).

import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';

dealPurchaseError(err: BusinessError) {
  if (err.code === iap.IAPErrorCode.PRODUCT\_OWNED || err.code === iap.IAPErrorCode.SYSTEM\_ERROR) {
      // Follow the instructions in [Subscription Delivery Guarantee](../delivering-an-auto-renewable-subscription-product/document.md#section1880231055910) to check whether the product needs to be redelivered.
    // ...
  }
}
