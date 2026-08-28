# About Digital Products

The digital product service provides apps that have integrated IAP Kit with functions such as [displaying digital products](../../distributing-digital-products-in-your-app/displaying-digital-products/document.md), [purchasing digital products](../../distributing-digital-products-in-your-app/purchasing-digital-products/document.md), and [delivering digital products](../../distributing-digital-products-in-your-app/delivering-digital-products/document.md).

#### Digital Product Types

<table><tbody><tr><td class="cellrowborder" valign="top" width="27.310000000000002%"><p><strong>Product Type</strong></p></td><td class="cellrowborder" valign="top" width="39.42%"><p><strong>Description</strong></p></td><td class="cellrowborder" valign="top" width="33.269999999999996%"><p><strong>Example</strong></p></td></tr><tr><td class="cellrowborder" valign="top" width="27.310000000000002%"><p>Consumables</p></td><td class="cellrowborder" valign="top" width="39.42%"><p>Product designed for one-time use, becoming unusable after its first use.</p></td><td class="cellrowborder" valign="top" width="33.269999999999996%"><p>In-game currency and items, and in-app coupons</p></td></tr><tr><td class="cellrowborder" valign="top" width="27.310000000000002%"><p>Non-consumables</p></td><td class="cellrowborder" valign="top" width="39.42%"><p>Product that is purchased once and can be used long-term without expiring or losing effectiveness over time.</p></td><td class="cellrowborder" valign="top" width="33.269999999999996%"><p>Extra game levels in a game or permanent membership of an app</p></td></tr><tr><td class="cellrowborder" valign="top" width="27.310000000000002%"><p>Auto-renewable subscriptions</p></td><td class="cellrowborder" valign="top" width="39.42%"><p>Users can purchase access to value-added functions or content in a specified period of time. The subscriptions are automatically renewed on a recurring basis until users decide to cancel.</p></td><td class="cellrowborder" valign="top" width="33.269999999999996%"><p>Non-permanent membership of an app, such as a monthly video membership</p></td></tr><tr><td class="cellrowborder" valign="top" width="27.310000000000002%"><p>Non-renewing subscriptions</p></td><td class="cellrowborder" valign="top" width="39.42%"><p>Value-added functions or content that are open to users in a limited period of time. Subscriptions to these functions or content are not automatically renewed.</p></td><td class="cellrowborder" valign="top" width="33.269999999999996%"><p>One-year access to live games after subscription</p></td></tr></tbody></table>

#### Digital Product Purchase Scenarios

People can use in-app purchase to buy either consumables or non-consumables by making a one-time payment. You can choose to offer either consumables, non-consumables, or both, depending on your requirements.

Users gain access to premium app features or content for a set duration upon purchasing an auto-renewable subscription. At the end of a billing cycle, the subscription automatically renews for the next cycle unless the user cancels it.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="52.16%"><div class="fignone"><span class="figcap"><b>Figure 1 </b>A user purchases a consumable or non-consumable</span></div><p></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="47.839999999999996%"><div class="fignone"><span class="figcap"><b>Figure 2 </b>A user purchases an auto-renewable subscription</span></div></td></tr><tr><td class="cellrowborder" style="border: none;" valign="top" width="52.16%"><p><span><img height="526.4257040000001" originheight="3264" originwidth="1540" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/ZX_2Ab6oQpqEbe5_v4mVcw/en-us_image_0000002371732785.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=CB4843C4BF2A3887AFF95EAF24AD71A0217EECA579187C36E6BC5990E13A680F" title="Click to enlarge" width="248.37750000000003"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="47.839999999999996%"><p><span><img height="530.8305310000001" originheight="3053" originwidth="1440" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/kYm-77G6SvaQ77pTxtoiZw/en-us_image_0000002337894596.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=7E5A0376F3AD9B59E1B9F65F668CC1DB4906D768DF7F560FDD514EB7A3A36563" title="Click to enlarge" width="250.3725"></span></p></td></tr></tbody></table>

#### Configuring Auto-renewable Subscriptions

Auto-renewable subscriptions are managed and maintained by subscription groups. Before creating an auto-renewable subscription, create a subscription group and specify the subscription group to which the subscription belongs. A subscription group comprises auto-renewable subscriptions of similar services, but only one subscription within the group can be active for each user at a time. For an active subscription, your app needs to grant relevant rights to the user. Such a mechanism provides you with a convenient way to easily manage products with slight differences in their functions.

The billing cycle of an auto-renewable subscription can be 1 week, 30 days, 31 days, 1 month, 2 months, 3 months, 6 months, or 12 months. To set the billing cycle, please refer to [Configuring Digital Products in AppGallery Connect](../configuring-digital-products-in-appgallery-connect/document.md).

#### Subscription Statuses and Changes

A subscription has the following statuses.

| 
Status

 | 

Description

 |
| :-- | :-- |
| 

Renewable

 | 

The subscription has taken effect and its services are available. Billing will happen as expected for the next renewal.

 |
| 

Expiring

 | 

A user has canceled a subscription, but they still have access to the subscription until the end of the current billing cycle. When the billing cycle ends, no more renewals will be incurred and the user will lose access to the subscription.

 |
| 

Expired

 | 

The subscription has expired and relevant services are unavailable. The possible causes may be as follows: The fee deduction fails in the last renewal, the user cancels the subscription, the user does not agree to the price increase, or the fee deduction account is abnormal.

Expired subscriptions remain accessible for up to 180 days. During this period, users cannot access the services associated with the auto-renewable subscription. However, they can regain access to these services by reactivating their subscriptions.

 |
| 

To take effect

 | 

The subscription has not taken effect. Users are not entitled to access the services of the auto-renewable subscription.

If a user switches between subscriptions within a subscription group and selects a subscription that will take effect at the next renewal, the new subscription enters the to-take-effect state and will become active only after the original subscription expires. After the subscription change operation is done, the original subscription will enter the expiring state, and the new subscription will enter the to-take-effect state. The start time of the new subscription is displayed on the editing screen of the original auto-renewable subscription.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/e9koEL7mTMmS_R5UGNLOkA/en-us_image_0000002337894604.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA50AFC12247610B9EA8B4E026302D5AE677707D07809F3A1E0AE841A620303A "Click to enlarge")

After a user successfully purchases an auto-renewable subscription, the subscription will enter the renewable state. The subscription status will change when the following operations are performed:

-   Unsubscribing: Cancel an auto-renewable subscription. After a subscription is canceled, the user retains access to it until the end of the current billing cycle.
-   Resuming a subscription: A user can resume an expiring or expired subscription to regain access to it.
-   Switching between subscriptions: Switch between different auto-renewable subscriptions in the same subscription group. The new subscription can:
    -   Take effect immediately (no retention period for the original subscription): The original subscription balance will be converted into days for the new subscription, extending the validity period of the new subscription. This happens in the following scenarios:
        -   Subscription upgrade: The new subscription has a higher level than the original subscription.
        -   The new subscription has the same level and also the same billing cycle as the original subscription.
    -   Take effect later: The original subscription is set to the expiring state and the new subscription is set to the to-take-effect state. The new subscription will be charged and take effect upon the date when the original subscription becomes expired. This happens in the following scenarios:
        -   Subscription downgrade: The new subscription has a lower level than the original subscription.
        -   The new subscription has the same level as the original subscription, but they have different billing cycles.

#### Subscription Management by Users

The digital product service provides apps that support in-app subscriptions with the capability of [redirecting users to a subscription page or the subscription details page](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section39973360502). This allows users to manage their subscriptions, for example, viewing, canceling, switching, and resuming subscriptions.

<table style="border-style: none;"><tbody><tr><td class="row-nocellborder" style="border: none;" valign="top" width="33.239999999999995%"><p><span><img height="515.836244" originheight="3264" originwidth="1540" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/4UY_gso8Tl6Jkt2HYfm2Jg/en-us_image_0000002337894600.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=C1A7E3280212D3454016DB1766233D3979D63CB953E65BD0DAC81303CAF7872D" title="Click to enlarge" width="243.39000000000001"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="66.75999999999999%"><p><span><img height="516.276075" originheight="3264" originwidth="1540" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/PM2zosD2TtSE3wEE9WvNcg/en-us_image_0000002371732797.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=2E8FF52587D24DAE02BC865524F67BEABA41D1F7B7B1C60E4F227C31D3A3D5FC" title="Click to enlarge" width="243.58950000000002"></span></p></td></tr></tbody></table>

#### Renewal Processing

The renewal price for a subscription (including the original price or any price changes) will be determined 10 days before the renewal date. For an auto-renewable subscription with a billing cycle of one week, the price for the next renewal needs to be confirmed immediately after the current renewal is successful. If the price is adjusted after it is confirmed, the next renewal will still be billed at the original price, and the renewal after that will be billed at the new price.

24 hours before the end of a billing cycle, the digital product server will attempt to charge the user to renew their auto-renewable subscription. If the charge fails, the digital product server will retry the charge within a certain period to restore the subscription.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/-HkMTFaKSE-gJcOZp0LUyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF840A1D6BF78080FB79CD89C5D9FAC9295ED85BD7BD7D330DE237BC276FB2D6)

If a subscription becomes inactive due to failed billing, the system will automatically retry the billing for up to 60 days.

#### Special Offers

To make auto-renewable subscriptions more attractive, the following two methods of promotion are available:

**Introductory offers for new users**

-   Discount price: Users who have purchased a subscription can enjoy a lower price for a period of time. After this period ends, the user will be charged the full subscription price.
-   Free trial: Users can try out a subscription free of charge for a period of time before making a payment. Once the free trial period ends, they will be charged the standard price.

**Introductory offer rules:**

1.  A user is entitled to only one promotion in each subscription group. If a user has already enjoyed the promotion of one subscription in a group, the user will not be entitled to any other promotions, even after switching to another subscription in the group.
2.  A user is entitled to the promotion of a subscription no matter whether the user subscribes to it for the first time, resumes it, or switches to it from another subscription. The only restriction is that a user can enjoy only one promotion in a subscription group.

**Special offers for custom user groups**

You can tailor promotional activities to specific user groups and regions. Before a purchase is made, your app can retrieve promotional information for a particular product. This information is then passed to IAP Kit and displayed to the user during checkout.

**Promotion rules:**

-   When a user meets the conditions of both the promotion for specific user groups and the promotion for new users, the former promotion takes priority over the latter.
-   If a user has enjoyed a promotion for specific user groups in the past, the user is still qualified to enjoy a promotion for new users.
-   There is no limit on the number of times that a user enjoys promotions for specific user groups.

To set special offers, please refer to relevant sections in [Configuring Digital Products in AppGallery Connect](../configuring-digital-products-in-appgallery-connect/document.md).

#### Modifying Auto-renewable Subscriptions

## Adjusting the Price of an Auto-renewable Subscription

You can raise or lower the price of an auto-renewable subscription. Check [Modifying a Single Product > Auto-renewable Subscriptions](https://developer.huawei.com/consumer/en/doc/app/revise-renewal-0000001959074893) for the detailed operations.

-   Lowering a price: This adjustment takes effect upon the next renewal of a subscription and is effective for all subscribers, including both existing and new ones.
-   Raising a price: You can raise the price of an auto-renewable subscription in either of the following ways:
    -   Retain the original price for existing subscribers and apply the new price to new subscribers.
    -   Apply the new price to all subscribers. The digital product server will notify existing subscribers of the new price and the date when they will be billed at the new price. The notification will be sent 10 days before the next billing date. If the price adjustment occurs within 10 days before the next billing date, the IAP server will renew the subscription for one more cycle based on the original price and then notify existing subscribers of the price adjustment 10 days before the next billing date ends. However, there are still some other limitations:
        -   The new price of an auto-renewable subscription applies to existing subscribers only after they agree to it. If a subscriber does not agree to the new price, the subscription cannot be automatically renewed anymore for this subscriber.
        -   After a price increase takes effect, you cannot cancel it. You can, however, make another adjustment to lower the price. For users who have canceled their subscriptions due to a price increase, their subscriptions cannot be resumed automatically. They must repurchase the subscription if they still want to use it.
        -   If a user is in a discount-price period of an auto-renewable subscription when its price is adjusted, the user will be charged for the next renewal at the original price before the price adjustment when the discount-price period ends. The new price will then take effect starting from the second renewal following the discount period.

## Removing an Auto-renewable Subscription

It is necessary to consider the impact on users when you plan to remove certain auto-renewable subscriptions.

Before finally stopping providing services for a subscription, you first need to remove the subscription to make it unavailable for new purchases. It is recommended that the time to remove an auto-renewable subscription be aligned with its billing cycle. For example, if an auto-renewable subscription is renewed on a monthly basis, remove the subscription one month before you stop providing services so that users can experience the services of a complete subscription period before the subscription finally ends its services and will not be charged on the next billing date. Similarly, for a subscription that renews on a weekly basis, remove the subscription seven days in advance, and for a subscription that renews every six months, remove the subscription six months in advance. The same rule applies to all other subscriptions. When you remove an auto-renewable subscription, your users will receive a subscription termination notification.

#### Receiving Notifications About Key Subscription Events

If you have specified the address for receiving key subscription events when applying for the digital product service in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), the digital product server will call the relevant API to send notifications about users purchasing auto-renewable subscriptions to the specified address. For details, please refer to [Key Event Notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications). Here are some key events:

-   A user successfully makes a subscription for the first time.
-   An expired subscription is resumed after a successful auto-renewal.
-   A user proactively renews an expired auto-renewable subscription.
-   A user chooses to switch to an auto-renewable new subscription at the same level or at a lower level, which will take effect on the next renewal date.
-   A user chooses to switch to an auto-renewable subscription at the same level or at a higher level, which will take effect immediately.
-   A user proactively cancels or your app cancels an auto-renewable subscription. In this scenario, the user can still access the services, but no more renewal will happen after this cycle ends.
-   An auto-renewable subscription is successfully renewed.
-   An expired auto-renewable subscription enters the account retention period.
-   The renewal time for a subscription has been moved to a later time.
-   The renewal time for a subscription has been moved to an earlier time.

If your app server returns a failure response (that is, the HTTP status code in the response is not **200**), the IAP server will periodically resend the notification about the key event to your app server. It is recommended that your app server return a success response immediately after receiving the notification, to avoid constantly receiving messages from the IAP server.
