# Configuring Products

Before implementing the product purchase capability, you need to configure product information (including the product ID, type, name, and prices in different countries/regions) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). When your app calls the API for in-app purchases, only the product ID and type will be passed, and IAP Kit will automatically show the product information (such as the name and price) based on the country or region to which the user account belongs.

#### Configuring a Consumable, Non-consumable, or Non-renewable Subscription

-   Add a [consumable, non-consumable, or non-renewable subscription](https://developer.huawei.com/consumer/en/doc/app/non-subscription-0000001959074885).
-   Set a promotional price (targeted at specific user groups) for a consumable, non-consumable, or non-renewable subscription. For details, please refer to [Setting Promotional Prices > Non-subscriptions](https://developer.huawei.com/consumer/en/doc/app/promotion-non-subscription-0000001931836332).
-   [Modify the configurations (such as the product name and price)](https://developer.huawei.com/consumer/en/doc/app/revise-non-subscription-0000001931836328) of a consumable, non-consumable, or non-renewable subscription.

#### Configuring an Auto-renewable Subscription

-   [Add a subscription group](https://developer.huawei.com/consumer/en/doc/app/gain-0000001959074909) first, and then specify the subscription group when [creating an auto-renewable subscription](https://developer.huawei.com/consumer/en/doc/app/non-subscription-0000001958955109).
-   Set promotions for an auto-renewable subscription, including [introductory offers](../../product-purchase/auto-renewable-subscription-purchase/understanding-auto-renewable-subscriptions/document.md#li1088435316541) (for new users), [promotional offers](../../product-purchase/auto-renewable-subscription-purchase/understanding-auto-renewable-subscriptions/document.md#li1264912560544) (for specific user groups), and [win-back offers](../../product-purchase/auto-renewable-subscription-purchase/understanding-auto-renewable-subscriptions/document.md#li27291112195419) (for users considering cancellation **and will be available soon**). For details, please refer to [Setting Promotional Prices > Auto-renewable Subscriptions](https://developer.huawei.com/consumer/en/doc/app/promotion-renewal-0000001959074897).
-   [Modify the configurations (such as the product name and price) of an auto-renewable subscription](https://developer.huawei.com/consumer/en/doc/app/revise-renewal-0000001959074893).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/9ClFFEQ3Q7WJ_nlIrpzHfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062108Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8DF830D0B83F3A010D2329E7A6C0C6551B745AACBC79EDBD1E92C5C68CAD4C0)

[AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) does not automatically update your product prices based on the latest exchange rates. Regularly [update the prices](https://developer.huawei.com/consumer/en/doc/app/single-0000001931995708) yourself.
