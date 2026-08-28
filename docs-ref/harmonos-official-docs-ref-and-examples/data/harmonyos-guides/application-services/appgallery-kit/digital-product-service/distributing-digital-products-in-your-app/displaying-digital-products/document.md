# Displaying Digital Products

The digital product service provides apps that support consumable, non-consumable, non-renewing subscription, and auto-renewable subscription purchases with the capability to display information about available products.

#### Prerequisites

The digital product service is supported in the service area to which the HUAWEI ID currently in use belongs.

#### Development Procedure

1.  Check whether IAP Kit is supported in the service area to which the HUAWEI ID currently in use belongs.
    
    To use IAP Kit, your app needs to send a [queryEnvironmentStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section192192415554) request to this kit to check whether the service area to which the HUAWEI ID currently in use belongs is supported by IAP Kit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/utz2PxMnRBygbddPkiE0Bw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68D50F3D446D6B0BC92BCC03660F4F669035233BCE910334B34AC6E167715F27)
    
    Currently, IAP Kit is available only in the Chinese mainland.
    
    import { iap } from '@kit.IAPKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { UIContext } from '@kit.ArkUI'
    
    class QueryEnvironmentStatus {
      queryEnvironmentStatus() {
        const context: common.UIAbilityContext = UIContext.prototype.getHostContext() as common.UIAbilityContext;
        iap.queryEnvironmentStatus(context).then(() => {
          // The request succeeded.
          console.info('Succeeded in querying environment status.');
        }).catch((err: BusinessError) => {
          // The request failed.
          console.error(\`Failed to query environment status. Code is ${err.code}, message is ${err.message}\`);
        });
      }
    }
    

2.  Query product information.
    
    Call the [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) API to obtain the product information configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). You need to include the product ID in [QueryProductsParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section1033653365917), and set **productType** according to your actual configuration. For a subscription-based product, set **productType** to [iap.ProductType.AUTORENEWABLE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section59035422210).
    
    Upon a successful API call, IAP Kit will return the list of product information ([Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313)), including the product price, name, and description. Based on the returned [Product](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section346874219313) information, the app shows the list of products available for purchase.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/1LHGl1ejQ-CwO1CqzLL4OQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17CEE048A9417E19AB762ECC6DE2A1BEDB9B33D0E83C398A47746E0EE41D8397)
    
    The [queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) API can only query one type of product at a time, and each query should not exceed 200 records.
    
    import { iap } from '@kit.IAPKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    import { UIContext } from '@kit.ArkUI'
    class Queryproducts {
      queryProducts() {
        const queryProductParam: iap.QueryProductsParameter = {
          // iap.ProductType.CONSUMABLE: consumable
          // iap.ProductType.NONCONSUMABLE: non-consumable
          // productType: iap.ProductType.AUTORENEWABLE: subscription
          productType: iap.ProductType.CONSUMABLE,
          // Only the products already configured in AppGallery Connect can be queried.
          productIds: \['ohos\_consume\_001'\]
        };
        const context: common.UIAbilityContext = UIContext.prototype.getHostContext() as common.UIAbilityContext;
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
    }
