# Understanding Auto-renewable Subscriptions

Users gain access to premium app features or content for a set duration upon purchasing an auto-renewable subscription. At the end of a billing cycle, the subscription automatically renews for the next cycle unless the user cancels it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/FOWzagenTGmoHbG62PFwZw/en-us_image_0000002446613497.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1016AD82B13984CE4F7CABE5B148544BD4F749B6DEF80CAB16D5819D2E7ED29 "Click to enlarge")

#### Configuring Auto-renewable Subscriptions

## Subscription Group

Subscriptions are managed and maintained by **subscription groups**. Before creating a subscription, ensure the corresponding subscription group has been created so you can specify the subscription group to which the subscription belongs.

-   A subscription group comprises subscriptions of similar services.
-   Only one subscription within the same subscription group can be active for each user at a time. For an active subscription, your app needs to grant relevant rights to the user.

Such a mechanism provides you with a convenient way to easily manage products with slight differences in their functions.

## Billing Cycle

The billing cycle of an auto-renewable subscription can be 1 week, 30 days, 31 days, 1 month, 2 months, 3 months, 6 months, or 12 months. To set the billing cycle, refer to [Configuring an Auto-renewable Subscription](../../../preparations/configuring-products/document.md#section49178516208).

## Account Hold Period

If a subscription expires due to cancellation, renewal failure, or other causes, the subscription enters the account hold period of up to 180 days. During this period, the user has no access to this subscription. However, if the user resumes a subscription during the account hold period, all services of this subscription are immediately accessible.

#### Subscription Statuses and Changes

## Subscription Statuses

| 
Status

 | 

Service Accessible

 | 

Description

 |
| :-- | :-- | :-- |
| 

To be active

 | 

No

 | 

The subscription has not taken effect and the user has no access to services of this subscription. (The subscription in this state cannot be queried.)

If a user changes their subscription to another subscription within the same group and the new subscription doesn't start immediately, their current subscription will be marked as expiring soon, and the new one will be set to start at the end of the current billing cycle. The user can view the start time of the new subscription on the details screen of the original subscription.

 |
| 

Active

 | 

Yes

 | 

**Renewable**: The subscription will be automatically renewed after the current billing cycle ends.

**Expire soon**: The subscription **will not** be automatically renewed after the current billing cycle ends.

 |
| 

Expired

 | 

No

 | 

The possible causes may be as follows: the fee deduction fails in the last renewal, the user cancels the subscription, the user does not agree to the price increase, or the fee deduction account is abnormal. Then, the subscription enters the [Account Hold Period](#section1656191811315).

 |
| 

Renewal attempt

 | 

No

 | 

The system will automatically attempt to renew your subscription at regular intervals, either shortly before or after your current subscription expires.

 |
| 

Canceled

 | 

No

 | 

The subscription has been successfully canceled. Relevant benefits will be revoked immediately, and neither the user nor you can undo the cancellation.

 |

## Subscription Status Changes

After a user successfully purchases an auto-renewable subscription, the subscription enters the renewable state. The subscription status changes when the operations listed in the table below are performed.

| 
Operation

 | 

Description

 |
| :-- | :-- |
| 

**Canceling a subscription**

 | 

Cancel an auto-renewable subscription. After a subscription is canceled, the user retains access to it until the end of the current billing cycle.

NOTE:

In this scenario, your app server will receive a [notification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) about the key event [AUTO\_RENEW\_DISABLED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications#section16254133782813) from the IAP Kit server.

 |
| 

**Resuming a subscription**

 | 

A user can resume an expiring or expired subscription to regain access to it.

NOTE:

In this scenario, your app server will receive a [notification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) about the key event [AUTO\_RENEW\_ENABLED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications#section16254133782813) or [RESTORE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications#section16254133782813) from the IAP Kit server.

 |
| 

**Switching from one subscription to another**

 | 

When a user has an active subscription and wants to switch to a different subscription within the same subscription group, two things can happen.

-   The new subscription takes effect immediately (no [Account Hold Period](#section1656191811315) for the original subscription): The original subscription balance will be converted into days for the new subscription, extending the validity period of the new subscription. This happens in the following scenarios:
    
    1.  Subscription upgrade: The new subscription has a higher level than the original subscription.
    2.  The new subscription has the same level and also the same billing cycle as the original subscription.
    
    NOTE:
    
    In this scenario, your app server will receive a [notification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) about the key event [UPGRADE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications#section16254133782813) from the IAP Kit server.
    
-   The new subscription will take effect at the end of the current billing cycle: The original subscription is set to the expiring state and the new subscription is marked as to-be-active. The new subscription will be charged and take effect upon the date when the original subscription becomes expired. This happens in the following scenarios:
    
    1.  Subscription downgrade: The new subscription has a lower level than the original subscription.
    2.  The new subscription has the same level as the original subscription, but they have different billing cycles.
    
    NOTE:
    
    In this scenario, your app server will receive a [notification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) about the key event [DOWNGRADE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications#section16254133782813) from the IAP Kit server.
    

 |

The subscription status changes as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/C53VOBJiRr-oJVo4juwAlA/en-us_image_0000002413014424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3036AB9119D3522C615D2CE300DD04FDCA7F615E6889AA1FE6513719C46089EB "Click to enlarge")

#### Subscription Management by Users

Your app can call the [iap.showManagedSubscriptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section39973360502) API to redirect users to the subscription status screen or subscription details screen for subscription management. Users can also go to **Settings** > **HUAWEI ID** > **Payment and purchases** > **Subscriptions** to manage subscriptions. They can perform operations such as viewing, canceling, changing, and resuming subscriptions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/6CCSsIwbTs6ydRZNElWg-A/en-us_image_0000002446613489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=692CDB3E5FE250D86806C52D08AAC695AB2509BE058FEFFD1ABBA588F12F785D "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/NbgdW2YeROG_efWatnIa4w/en-us_image_0000002413174284.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=887D33481046942BBD62E7661376207176697B896C3E5113EA81235F94C534DC "Click to enlarge")

#### Renewal Processing

The renewal price for a subscription (including the original price or any price changes) will be determined 10 days before the renewal date. For a subscription with a billing cycle of one week, the price for the next renewal needs to be confirmed immediately after the current renewal is successful. If the price is adjusted after it is confirmed, the next renewal will still be at the original price, and the renewal after that will be at the new price.

24 hours before the end of a billing cycle, the IAP server will attempt to charge the user to renew their subscription. If the charge fails, the IAP server will retry the charge within a certain period to restore the subscription.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Ec13A8FZS9uymLZQ01uHSw/en-us_image_0000002454362129.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3740A0D3D0BFE146C4AD4377918C35FCB58E021D3DCA9C1AAF5B40D240D555B "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/szDB0lBeSkqIf_RB4dcRGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80577F0BAF2A9D21428A7973EFE882875922A75B0BF6352A5E5A11D4B63743A2)

If a subscription becomes inactive due to failed billing, the system will automatically retry the billing for up to 60 days.

#### Promotional Offers

To make subscriptions more attractive and retain existing users, the following three types of offers are available:

-   **Introductory offers for new users**
    
    Promotional pricing can be set for a subscription to attract new users. You can specify the duration and type of the offer (free trial or recurring billing).
    
    Promotion rules:
    
    1.  A user is entitled to only one promotion in each subscription group. If a user has already enjoyed the promotion of one subscription in a group, the user will not be entitled to any other promotions, even after switching to another subscription in the group.
    2.  A user is entitled to the promotion of a subscription no matter whether the user subscribes to it for the first time, resumes it, or switches to it from another subscription. The only restriction is that a user can enjoy only one promotion in a subscription group.

-   **Promotional offers for specific user groups**
    
    You can tailor promotional activities to specific user groups in certain regions. Before a purchase is made, your app can retrieve promotional information for a particular product. This information is then passed to IAP Kit and displayed to the user during checkout.
    
    Promotion rules:
    
    1.  When a user meets the conditions of both the promotion for specific user groups and the promotion for new users, the former promotion takes priority over the latter
    2.  If a user has enjoyed a user group–based promotion in the past, the user is still qualified to enjoy a new-user promotion.
    3.  There is no limit on the number of times that a user enjoys user group–based promotions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/sGfBh3mpRB6_i2yT8NLKcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4067E0EE8305C42784AE4E18B6F027E6F42E3C4F44B4393432EE6E7A963EF696)
    
    User group–based promotions require the operation of [Generating a Signed Purchase Parameter for a Promotion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-server-subscribe-offer-sign) and are applicable only to apps with servers deployed.
    

-   **Win-back offers for users considering cancellation (coming soon)**
    
    Win-back offers are targeted for users who are about to cancel their auto-renewable subscriptions, providing specific promotional prices to prevent user churn. You can specify the offer duration, type (free trial or recurring billing), and interval for applying the offer again (starting from the end of the previous offer). When a user who meets the criteria for a win-back offer attempts to cancel their subscription on the subscription management screen, a pop-up will appear to provide the offer. The user can then choose to accept the offer and continue their subscription, or proceed with cancellation. If the user chooses to accept the win-back offer, it will take effect for the next renewal cycle, and they will be charged the promotional price.
    
    Rules of win-back offers:
    
    1.  If a user cancels their subscription before renewal after accepting a win-back offer, the win-back offer is voided. If the user subsequently resumes their subscription, the win-back offer cannot be used again within the current subscription period and will only be available after the next renewal.
    2.  A win-back offer can only be used again after the interval set by you has passed since the end of the user's last win-back offer.
    3.  Win-back offers can be used an unlimited number of times, but cannot be used in the following scenarios:
        1.  Win-back offers are unavailable for users who are currently benefiting from an introductory offer for new users or a promotional offer for specific user groups or will benefit from such an offer in the upcoming cycle.
        2.  Win-back offers are unavailable for users who are currently benefiting from or will benefit from a win-back offer in the upcoming cycle.
        3.  Win-back offers are unavailable for users who have not agreed to price increases configured by you.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/s_iAJXwkRpytoxbNLNqIhQ/en-us_image_0000002446613513.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C65C7BE96BD2644C8B8C77D0C2343F77B7D8478A346A5BB50892C7B8591AFED6 "Click to enlarge")
    

When setting a special offer, besides specifying the offer type, you also need to select a payment method for each offer:

-   **Free trial**: Users can access a subscription free of charge for a specific duration. They won't be billed until the free offer duration ends.
-   **Pay as you go**: Users pay a discounted price each billing cycle for a specific duration. Once the duration is over, they will be billed at the standard renewal price.
-   **Pay up front**: Users pay a one-time discounted price up front for a specific duration. Once the duration is over, they will be billed at the standard renewal price.

To set special offers, please refer to relevant sections in [Configuring Products](../../../preparations/configuring-products/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ZWt7LMatROeNz0Gwre_toQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F26C585F148D248D1B39C4BB9791A50C810A3B392B3D3C26EB51DB50BED12AD)

-   Whether a user can enjoy an offer depends on the offer ID passed by your app. For more information about this parameter, please refer to [Generating a Signed Purchase Parameter for a Promotion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-server-subscribe-offer-sign).
-   The IAP server determines whether a user can enjoy an introductory offer and automatically applies the offer to the user. You can check the **hasEligibilityForIntroOffer** field of **SubscriptionInfo** in the return value of [iap.queryProducts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section55531442102518) to determine whether a user has enjoyed an introductory offer.

#### Modifying Subscriptions

## Adjusting the Price of a Subscription

You can raise or lower the price of a subscription if you need. Check [Modifying a Single Product > Auto-Renewable Subscription](https://developer.huawei.com/consumer/en/doc/app/agc-help-modify-product-0000001146814541#section0980104712159) for the detailed operations.

-   Lowering a price: This adjustment is effective for all users, including existing subscribers and new subscribers. If the price is adjusted within 10 days before the next renewal date, the current price will be used for the next renewal, and the new price will be used for the renewal after the next renewal.
-   Raising a price: You can raise the price of a subscription in either of the following ways:
    -   Retain the original price for existing subscribers and apply the new price to new subscribers.
    -   Apply the new price to all subscribers. The IAP server will notify existing subscribers of the new price and the date when they will be billed at the new price. The notification will be sent 10 days before the next billing date. If the price adjustment occurs within 10 days before the next billing date, the IAP server will renew the subscription for one more cycle based on the original price and then notifies existing subscribers of the price adjustment 10 days before the "one more cycle" ends. However, there are still some other limitations:
        -   The new price of a subscription applies to existing subscribers only after they agree to it. If a subscriber does not agree to the new price, the subscription cannot be automatically renewed anymore for this subscriber.
        -   After a price increase takes effect, you cannot cancel it. You can, however, make another adjustment to lower the price. For users who have canceled their subscriptions due to a price increase, their subscriptions cannot be resumed automatically. They must repurchase the subscription if they still want to use it.
        -   If a user is in a discount-price period of a subscription when its price is adjusted, the user will be charged for the next renewal at the original price before the price adjustment when the discount-price period ends. Then, the new price will apply to the user for the renewal after the next one.

## Removing a Subscription

It is necessary to consider the impact on users when you plan to remove certain subscriptions.

-   Allowing existing users to renew the subscriptions and preventing new users from subscribing to them: You can [remove the subscriptions](https://developer.huawei.com/consumer/en/doc/app/lnvalid-0000001958955125) on the **Product Management** page to prevent new users from subscribing to them. However, you still need to make sure that existing users can access and renew them.
-   Making subscriptions unavailable to both new and existing users: You can [delete digital products](https://developer.huawei.com/consumer/en/doc/app/delete-0000001959074905) on the **Product Management** page to prevent new users from purchase and existing users from renewal. It is recommended to delete a digital product and then officially stop offering services after a certain period of time. This period should be consistent with its renewal cycle to ensure that existing users can experience the services for a full cycle. For example, for a subscription with a billing cycle of one month, the subscription should be deleted one month in advance to ensure that no new purchase can be made during this period, and that existing users can experience the services for a full cycle before the subscription reaches its end of service.

#### Receiving Notifications About Key Subscription Events

If you have [specified the address for receiving key subscription events](../../../preparations/basic-preparations/optional-setting-necessary-parameters/document.md#section22711950153313), the IAP server will call the relevant API to send key event notifications to the specified address. For details, please refer to [Key Event Notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications). Here are some key events:

-   A user successfully makes a subscription for the first time.
-   An expired subscription is resumed after a successful auto-renewal.
-   A user proactively renews an expired subscription.
-   A user switches from one subscription to another at the same level. If the two subscriptions have the same billing cycle, the new subscription will take effect immediately.
-   A user switches from one subscription to another at the same level. If the two subscriptions have different billing cycles, the new subscription will take effect on the next billing date.
-   A user proactively cancels a subscription or your app cancels a subscription. In this scenario, the user can still access the services, but no more renewal will happen after this cycle ends.
-   A subscription is successfully renewed.
-   An expired subscription enters the [account hold period](#section1656191811315).

If your app server returns a failure response (the HTTP status code in the response is not **200**), the notification about the key event will be periodically resent to your app server. It is recommended that your app server return a success response immediately after receiving the notification, to avoid constantly receiving messages from the IAP server.

#### Notes on Integrating the Subscription Functions for an App with Multiple Roles for an Account

A user uses their HUAWEI ID to purchase a subscription. For one subscription, only one purchase is allowed for each HUAWEI ID at the same time. In this case, if your app allows an account to have multiple roles, there is a possibility that services are delivered incorrectly. The recommended solutions for this issue are as follows:

1.  Allow a user to purchase only common duration-based products for their roles other than role A, for which they have purchased a subscription. (This can be implemented via consumables.)
2.  Design a mechanism for transferring retained benefits. For example, when a user purchases a subscription for role B after they have purchased a subscription for role A, this mechanism can be used to transfer retained benefits from role A to role B.
3.  Configure multiple subscriptions. For example, for a game in which different game servers have different roles, create independent subscriptions for each server.
