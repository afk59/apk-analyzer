# Delivering a Non-renewable Subscription Product

#### Use Case

Your app needs to deliver the product purchased by a user in time. In real-world applications, unexpected events such as network errors or process terminations can prevent the app from knowing whether a user's payment was successful. This can lead to failures in delivering products to users, a phenomenon known as "order loss." To ensure that products are delivered successfully, it is necessary to check for any undelivered items in a user's order in the following situations:

1.  The app is launching.
2.  [iap.IAPErrorCode.PRODUCT\_OWNED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429) or [iap.IAPErrorCode.SYSTEM\_ERROR](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1834394718429) is returned upon a purchase request ([createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516)).

If there are any undelivered items, deliver them. Then, acknowledge the delivery with IAP Kit to complete the purchase.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/7DJaBuOLSAqT2O2CmteRvA/en-us_image_0000002413014356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F9CEC88C2B426EC5B0221AD6C77171C21997C8FC504FE4E9FF51688BF022599 "Click to enlarge")

1.  The app sends a [queryPurchases](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1147122418532) request to IAP Kit to obtain the information about purchased products for which the delivery is not acknowledged.
2.  IAP Kit returns the [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) list. Purchase data is a JWS-format string that contains the relevant order information. For details, please refer to [Data Types](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model).
3.  The app reports the [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) list to the app server.
4.  The app server decodes [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482).jwsPurchaseOrder and performs signature verification. (See [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature) for details of signature verification.) After the verification is successful, the app server obtains the JSON character string [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380).
5.  Process product delivery. Check [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) for whether relevant products are delivered. If not, deliver them and record the corresponding order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)).
6.  The app queries the order delivery status from the app server.
7.  The app server returns the delivery status and order information ([PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380)).
8.  After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to IAP Kit, telling the IAP server to update the delivery status and complete the purchase process. After the app successfully executes [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814), the IAP server marks the purchased products as delivered.
    
    This step can also be performed on the app server. The app server can call the [order status query](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-confirm-purchase-for-order) API of the IAP server to acknowledge the delivery and complete the purchase process.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/qinmnuGjRy6UbsDAOt4Mng/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD4B303FF20E68B98404781D13FCE8202095D99F846CDF1D43AF0CF2C97E4C65)
    
    Ensure that this step is executed only after successful product delivery. Otherwise, the following problem may occur: the IAP server believed the order has been delivered successfully, but the app server has not actually delivered it.
    

#### Development Procedure

1.  The app sends a [queryPurchases](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1147122418532) request to IAP Kit to obtain the data of the non-renewable subscriptions that are purchased but not delivered.
    
    Set **productType** to **NONRENEWABLE** and **queryType** to [iap.PurchaseQueryType.UNFINISHED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1389262216514) in the request parameter [QueryPurchasesParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section555872993213). When the API request is successful, IAP Kit returns a [QueryPurchaseResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section820381425513) object. It contains a list of [PurchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) that contains order information.
    
2.  Decode [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482).jwsPurchaseOrder and perform signature verification by referring to [Verifying the Signature in the Returned Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-verifying-signature). It is recommended that the app send [purchaseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section650794012482) to the app server so that this task can be executed on the app server.
3.  After the verification is successful, the app server obtains the JSON character string [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380). If [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380).purchaseOrderRevocationReasonCode is empty, the purchase is successful and the app needs to redeliver the product.
    
    You are advised to check the product delivery status of the order. If the product is not delivered, deliver it. After the delivery is successful, record relevant information such as [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) for subsequent check.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/9ANEQSaOTRuqP79_FWsmDw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B85CDED0F5354C6F5F83055F323E6D418E3F170243A4EDEB553ADF1382D79F8)
    
    If your app supports the function of [purchasing](../implementing-the-purchase-process/document.md#section7929044255) non-renewable subscriptions in batches, it is necessary to check whether the number of subscriptions purchased is the same as the value of [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380).quantity.
    
4.  After a successful delivery, the app sends a [finishPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section124751324135814) request to acknowledge the delivery, telling the IAP server to update the delivery status and complete the purchase process.
    
    **productType**, **purchaseToken**, and **purchaseOrderId** in [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) must be passed in the request parameter [FinishPurchaseParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section103714142118).
    
    After the request is successful, the IAP server marks the product as delivered.
    
    import { iap } from '@kit.IAPKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // **JWSUtil** is a custom class. For details, please refer to the [sample code](../../../getting-started/document.md#section698882222912).
    import { JWSUtil } from '../common/JWSUtil';
    
    @Entry
    @Component
    struct Index {
    
      queryPurchases(context: common.UIAbilityContext) {
        const param: iap.QueryPurchasesParameter = {
          productType: iap.ProductType.NONRENEWABLE,
          queryType: iap.PurchaseQueryType.UNFINISHED
        };
        iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
          console.info('Succeeded in querying purchases.');
          const purchaseDataList: string\[\] = res.purchaseDataList;
          if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
            return;
          }
          for (let i = 0; i < purchaseDataList.length; i++) {
            const jwsPurchaseOrder: string = JSON.parse(purchaseDataList\[i\]).jwsPurchaseOrder;
            if (!jwsPurchaseOrder) {
              continue;
            }
            const purchaseStr = JWSUtil.decodeJwsObj(jwsPurchaseOrder);
          // Customize the **PurchaseOrderPayload** class. Check [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) for the information included in this class.
            const purchaseOrderPayload = JSON.parse(purchaseStr) as PurchaseOrderPayload;
          // Process product delivery.
            // ...
          // After the delivery is successful, send a **finishPurchase** request to IAP Kit to acknowledge the delivery and complete the purchase.
            this.finishPurchase(context, purchaseOrderPayload);
          }
        }).catch((err: BusinessError) => {
        // The request failed.
          console.error(\`Failed to query purchases. Code is ${err.code}, message is ${err.message}\`);
        });
      }
    
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
