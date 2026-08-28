# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/_tzEtzmcQteoEzm0ctlZAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93DBD50688298014F6B913FB9D43F28A2B1B3AD97C9A3C00D9E4534EAC4CBF8B)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

If the error persists, go to [Submit ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/), select the relevant topic, and submit your ticket. Huawei will get back to you as soon as possible.

#### 1001860000 Operation Canceled by User

**Message**

The operation was canceled by the user.

**Description**

The user cancels the current operation.

**Possible causes**

The user cancels the current operation.

**Solution**

Display a message to the user that the operation is canceled.

#### 1001860001 Internal Error

**Message**

System internal error.

**Description**

Internal system error.

**Possible causes**

An error is reported during program running.

**Solution**

-   If this result code is returned upon a purchase request, you are advised to use the [queryPurchases](../iap/document.md#section1147122418532) API to check whether there are products purchased but not delivered, and if yes, deliver them in a timely manner.
-   In other cases, try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1001860002 App Not Authorized to Call the API

**Message**

The application is not authorized.

**Description**

The app is not authorized to call the API.

**Possible causes**

1.  The app signature or identity information is incorrectly configured.
2.  The app does not have the IAP service enabled.

**Solution**

1.  Refer to [Configuring App Identity Information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-app-identity-info) and [Adding a Public Key Fingerprint](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview#section1726913517284) to check whether relevant configurations are correct.
2.  Make sure the manual signing method is used. To check the signing method in use, please refer to [Configuring Signing Information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview#section42841246144813).
3.  Verify that you have [enabled and activated IAP Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-enable-in-app-purchases).

#### 1001860003 Invalid Product Information

**Message**

Invalid product information.

**Description**

Invalid product information.

**Possible causes**

1.  The passed product ID or type is incorrect.
2.  The product created in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) has not been submitted for review or has not been approved. For details about how to create and submit a product for review, please refer to [Adding a Single Product](https://developer.huawei.com/consumer/en/doc/app/new-0000001931836320).

**Solution**

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). Click **My apps**, select an app, and go to **Operate** > **Products** > **Product Management**. In the product list, check whether the product exists, and if so, check whether all its mandatory information is available and has been approved. If the product fails to be approved, use a sandbox account for testing. For details, please refer to [Sandbox Testing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-sandbox).

#### 1001860004 API Calls Too Frequent

**Message**

Too frequent API calls.

**Description**

API calls are too frequent.

**Possible causes**

The API call interval is too short.

**Solution**

Control the API call frequency. The current default interval for accessing this API is 5 seconds. In the future, IAP Kit may adjust the call frequency limit up or down as needed.

#### 1001860005 Network Connection Error

**Message**

Network connection error.

**Description**

Network connection error.

**Possible causes**

Check the network.

**Solution**

Display a message to users, asking them to check the network.

#### 1001860007 App Not Released in the Specified Location

**Message**

The app to which the product belongs is not released in a specified location.

**Description**

The app to which the product belongs is not released in a specified location.

**Possible causes**

The app to which the product belongs is not released in a specified location.

**Solution**

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). Click **My apps**, select an app, and go to **Distribute** > **Version information** > **Draft**. Under **Countries/Regions**, check the countries or regions to which the app will be released.

#### 1001860050 HUAWEI ID Not Signed In

**Message**

The HUAWEI ID is not signed in.

**Description**

The HUAWEI ID is not signed in.

**Possible causes**

The HUAWEI ID is not signed in.

**Solution**

Guide the user to sign in with HUAWEI ID.

#### 1001860051 Purchase Failure Because the User Already Owns the Product

**Message**

Failed to purchase a product because the user already owns the product.

**Description**

The purchase failed because the user already owns the product.

**Possible causes**

The product has already been purchased.

**Solution**

Use the [queryPurchases](../iap/document.md#section1147122418532) API to check whether the user has purchased the product.

-   For a consumable or non-renewable subscription that has been purchased, check whether the product is delivered, and if so, call the [finishPurchase](../iap/document.md#section124751324135814) API to complete the purchase. Then, the product can be purchased again.
-   If the product is a non-consumable or an auto-renewable subscription, it cannot be purchased again once it has been purchased.

#### 1001860052 Delivery Failure Because the User Does Not Own the Product

**Message**

The purchase cannot be finished because the user has not paid for it.

**Description**

The delivery failed because the user does not own the product.

**Possible causes**

The user has not purchased the product.

**Solution**

Use the [queryPurchases](../iap/document.md#section1147122418532) API to check whether the user has purchased the product.

#### 1001860053 Repeated Delivery

**Message**

The purchase has been finished and cannot be finished again.

**Description**

The product has been delivered. No more delivery is needed.

**Possible causes**

The product has been delivered. No more delivery is needed.

**Solution**

Use the [queryPurchases](../iap/document.md#section1147122418532) API to check whether the product has a delivery acknowledgement record.

#### 1001860054 Service Area Unsupported by IAP Kit

**Message**

The country or region of the signed-in HUAWEI ID does not support IAP.

**Description**

The country or region to which the signed-in HUAWEI ID belongs does not support IAP Kit.

**Possible causes**

The country or region to which the signed-in HUAWEI ID belongs does not support IAP Kit.

**Solution**

For HUAWEI IDs with service locations outside the Chinese mainland, you are advised to hide IAP Kit–related functions within your app.

#### 1001860056 Transaction Rejected

**Message**

The user is not allowed to make purchase.

**Description**

The transaction is rejected.

**Possible causes**

The transaction behavior triggers IAP Kit risk control.

**Solution**

Try again later or change the payment method.

#### 1001860057 App Without a Debug Signature

**Message**

The app provision type is not debug.

**Description**

The app does not have a debug signature.

**Possible causes**

The app does not have a debug signature.

**Solution**

[Build an app with a debug signature](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-sandbox#li151047103116).

#### 1001860058 HUAWEI ID Not a Test Account

**Message**

The HUAWEI ID is not test account.

**Description**

The signed-in HUAWEI ID is not a test account.

**Possible causes**

The HUAWEI ID is not configured as a test account under **Users and permissions** in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/).

**Solution**

Configure a test account under **Users and permissions** in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). For details, please refer to [Adding test accounts](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-sandbox#li145164719318).

#### 1001860059 Invalid Special Offer Information

**Message**

Invalid promotional offer id.

**Description**

Invalid special offer information.

**Possible causes**

Special offers for custom user groups are not configured for the product during the task of [Configuring Products](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-product).

**Solution**

You can use the [queryProducts](../iap/document.md#section43916499256) API to check whether there are promotional offers set for the product. For details, please refer to [Setting Promotional Prices](https://developer.huawei.com/consumer/en/doc/app/set-0000001931995712).

#### 1001860060 Invalid Signature Information

**Message**

Invalid purchase signature.

**Description**

Invalid signature information.

**Possible causes**

The signature key or signature parameter is invalid, or the signature fails.

**Solution**

Handle the signing process by referring to [Generating a Signed Purchase Parameter for a Promotion](../../rest-apis/generating-a-signed-purchase-parameter-for-a-promotion/document.md).

#### 1001860061 Product Already or Being Refunded

**Message**

The purchase has been refunded or in refund.

**Description**

The product has been refunded or is in the process of being refunded.

**Possible causes**

The product has been refunded or is in the process of being refunded.

**Solution**

Configure your app to guide users to the order details page to view the refund status.

#### 1001860062 Refunds Not Allowed

**Message**

Refund is not allowed.

**Description**

The order cannot be refunded.

**Possible causes**

Refunds are not available for this order. Currently, the refund API integrated in the app is applicable only to non-game scenarios.

**Solution**

Make sure that the refund entry is unavailable in game scenarios.
