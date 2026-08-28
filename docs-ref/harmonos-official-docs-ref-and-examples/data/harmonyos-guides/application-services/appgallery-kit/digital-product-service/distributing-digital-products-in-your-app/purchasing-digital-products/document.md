# Purchasing Digital Products

#### Use Cases

Users can buy either consumables or non-consumables by making a one-time payment.

Users gain access to premium app features or content for a set duration upon purchasing an auto-renewable subscription. At the end of a billing cycle, the subscription will automatically renew for the next cycle unless the user cancels it.

Before integrating the digital product purchase capability, you first need to [configure digital products](../../configuring-digital-products/document.md) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), for example, setting product IDs and prices. When a user initiates a purchase, the app that supports the digital product service will call the [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) API of IAP Kit to bring up the checkout screen, which shows product information such as the name and price, for the user to complete the purchase.

#### Service Process and Development Procedure

## Consumables or Non-consumables

Please refer to [Consumable or Non-consumable Purchase](../../../../iap-kit/product-purchase/consumable-or-non-consumable-purchase/document.md).

## Auto-renewable Subscriptions

Please refer to [Auto-renewable Subscription Purchase](../../../../iap-kit/product-purchase/auto-renewable-subscription-purchase/document.md).

## Non-renewing Subscriptions

Please refer to [Non-renewable Subscription Purchase](../../../../iap-kit/product-purchase/non-renewable-subscription-purchase/document.md).
