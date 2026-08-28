# About This Kit

IAP Kit can be easily integrated into your app to deliver a streamlined in-app payment experience, making it easier for you to focus on your app's core business and drive revenue. With the help of IAP Kit's system-level payment APIs, your app can quickly show the IAP checkout screen for users to pay for various **virtual goods** sold within it.

These goods fall into the following categories: consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions.

| 
Product Type

 | 

Definition

 | 

Duration of User Entitlement

 | 

Processing on Your Side

 | 

Example

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Consumables

 | 

Such products are depleted as they are used and can be purchased again.

 | 

No time limit

 | 

Grant entitlements without providing further management.

 | 

In-game currencies and items.

 |
| 

Non-consumables

 | 

They are purchased once and can be used indefinitely. They are not depleted with use.

 | 

Permanent

 | 

Permanently maintain user benefits.

 | 

Extra game levels in games or unlimited premium memberships in an app.

 |
| 

Auto-renewable subscriptions

 | 

A purchase that grants users access to enhanced features or content for a limited time. The subscription automatically renews at the end of each cycle.

 | 

Recurring cycles

 | 

Periodically maintain user benefits.

 | 

Auto-renewable premium memberships within an app, such as a month-to-month video membership.

 |
| 

Non-renewable subscriptions

 | 

A non-renewable subscription provides users with temporary access to enhanced features or content. After the specified duration, these privileges are terminated. To continue enjoying these benefits, users must make another purchase (auto-renewable subscription or non-renewable subscription) to extend their access.

 | 

Only one cycle

 | 

Maintain user benefits within only one cycle.

 | 

Time-limited premium memberships, such as a one-month video membership.

 |

#### Constraints

## Supported Devices

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/vuGoFjPITw6aels_GBH7Xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062108Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B37367988655F5E16E8338399333828A1F3A1875D6B62DF0FB1DCF9D67D8EC9F)

Only wearable devices are supported in countries/regions [supported by HUAWEI IAP](../appendix/global-coverage-of-iap-kit/document.md) (excluding the Chinese mainland).

Available products and supported devices in Chinese mainland:

| 
Product Type

 | 

Supported Device

 |
| :-- | :-- |
| 

Consumables

 | 

Phone | PC/2-in-1 device | Tablet | Wearable | TV

 |
| 

Non-consumables

 | 

Phone | PC/2-in-1 device | Tablet | Wearable | TV

 |
| 

Auto-renewable subscriptions

 | 

Phone | PC/2in1 | Tablet | Wearable | TV

 |
| 

Non-renewable subscriptions

 | 

Phone | PC/2in1 | Tablet | Wearable | TV

 |

When triggered on a TV, the checkout UI displays a QR code for payment. Refer to the example below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/UzTP5xMhS2SAZywTxBzyTg/en-us_image_0000002446733449.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062108Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FC2986BDB5059310688CA9FF572FFB5F80157DFC8CE8691C31ED00DC1501FEE "Click to enlarge")

## Supported Countries/Regions

The countries/regions supported by IAP Kit depend on device types. For details, please refer to [Supported Devices](#section131061227914).
