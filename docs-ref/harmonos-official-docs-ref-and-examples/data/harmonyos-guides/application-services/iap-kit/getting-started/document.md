# Getting Started

#### Quick Tutorial

Before developing your app, you can follow instructions in the [codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_IAPKit-ArkTS) to experience how to quickly integrate this kit into an app.

#### Development Process

Follow the steps below to develop your app.

| 
No.

 | 

Step

 | 

Description

 |
| :-- | :-- | :-- |
| 

1

 | 

[Enabling Merchant Service](../preparations/basic-preparations/enabling-merchant-service/document.md)

 | 

Before starting your development, make [necessary preparations](../../../getting-prepared/application-development-preparations/document.md). When **configuring the signing information**, use the manual signing method.

To enable IAP Kit, you need to enable Merchant Service first. Under **Merchant Service**, you need to specify the bank account and currency for receiving your share of revenue from Huawei.

 |
| 

2

 | 

[Creating a Project and App](../preparations/basic-preparations/creating-a-project-and-app/document.md)

 | 

Before starting app development, create a project in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and under the project, create an app.

 |
| 

3

 | 

[Enabling and Activating IAP Kit](../preparations/basic-preparations/enabling-and-activating-iap-kit/document.md)

 | 

IAP Kit is available only after you enable and activate it.

 |
| 

4

 | 

[(Optional) Setting Necessary Parameters](../preparations/basic-preparations/optional-setting-necessary-parameters/document.md)

 | 

-   Configure the address for receiving order/subscription-related notifications.
-   Configure the key.

 |
| 

5

 | 

[Configuring Products](../preparations/configuring-products/document.md)

 | 

Configure necessary product information in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). When an app calls the purchase API, the product ID and type configured here must be passed.

 |
| 

6

 | 

[Configuring Signing Information](../preparations/configuring-signing-information/document.md)

 | 

Configure signing information in DevEco Studio to ensure successful project compilation and development.

 |
| 

7

 | 

[Configuring App Identity Information](../preparations/configuring-app-identity-information/document.md)

 | 

Configure the bundle name and client ID in the project.

 |
| 

8

 | 

[Product Purchase](../product-purchase/document.md)

 | 

-   [Consumable or Non-consumable Purchase](../product-purchase/consumable-or-non-consumable-purchase/document.md): Integrate the consumable/non-consumable purchase capabilities, including showing the product list, buying a product, and delivering a product. For details, please refer to [Implementing the Purchase Process](../product-purchase/consumable-or-non-consumable-purchase/implementing-the-purchase-process/document.md).
-   [Auto-renewable Subscription Purchase](../product-purchase/auto-renewable-subscription-purchase/document.md): Read [Understanding Auto-renewable Subscriptions](../product-purchase/auto-renewable-subscription-purchase/understanding-auto-renewable-subscriptions/document.md) to learn the concepts and functions related to auto-renewable subscription. For details about how to implement desired functions, please refer to [Implementing the Purchase Process](../product-purchase/auto-renewable-subscription-purchase/implementing-the-purchase-process/document.md).
-   [Non-renewable Subscription Purchase](../product-purchase/non-renewable-subscription-purchase/document.md): Integrate the non-renewable subscription purchase capabilities, including showing the subscription list, buying a subscription, and granting relevant benefits. For details, please refer to [Implementing the Purchase Process](../product-purchase/non-renewable-subscription-purchase/implementing-the-purchase-process/document.md).

NOTE:

During development, you can use [Sandbox Testing](../sandbox-testing/document.md) to test relevant functions. Sandbox testing allows you to complete payment testing without actual payments during the integration and debugging process of IAP Kit.

 |

#### Sample Code

Refer to the [sample code](https://gitee.com/harmonyos_samples/iapkit-sample-clientdemo-arkts) to check how to implement the capabilities of purchasing consumables, non-consumables, and auto-renewable subscriptions in your app.
