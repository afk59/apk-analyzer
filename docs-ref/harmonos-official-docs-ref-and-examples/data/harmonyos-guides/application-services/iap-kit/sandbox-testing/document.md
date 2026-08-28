# Sandbox Testing

Sandbox testing allows you to simulate virtual payments for orders during the testing phase of IAP Kit integration.

You are advised to use sandbox testing to debug your virtual products while they are still in draft or pre-submission state, before you submit them for official review. By setting up sandbox test accounts, you can simulate real-world virtual product transactions. This allows you to identify and fix any issues during testing, ensuring a stable and smooth purchase experience for users once your products go live.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PpLspdnpTN-p7HnpCLWnvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A276C4C362D51EF0FD6026514DD49787884492DC2D6243381939F74DC1CF70F3)

Sandbox orders are not real transactions and cannot be found in **Developer center** > **My reports** > **HUAWEI IAP**.

#### Preparing for Sandbox Testing

-   Adding test accounts
    
    Add test accounts, which must be real HUAWEI IDs, under **Users and permissions** in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). Before performing tests in the IAP Kit sandbox environment on a device, sign in to the device with the test account already added. To add a test account, do as follows:
    
    1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Users and permissions**.
    2.  Go to **Sandbox** > **Test accounts** and click **Add**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/8K3eW1_MSn6EjhkklVGEcQ/en-us_image_0000002413014464.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87E3D00B2D96EE4F944E288E5D09A39C06F2C83EC5A9D8545CB243AFC659C8D9 "Click to enlarge")
        
    3.  Specify test account information and click **OK**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/EoYnOftnQty3kM0Xmqp17g/en-us_image_0000002446613549.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C55C84EA063839C7A4CBC2AB7B40240C2EF8259FFFA81617F339F6B31E212D85 "Click to enlarge")
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/UetQJyfRRxGh1LauKutGWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D9DFAF3FF89F8B1E719EC50177D2E09DC573EE7A52079DA275934AB2ACFE57D)
    
    It takes 5 to 10 minutes for the configuration to take effect.
    

-   Building an app with a debug signature
    
    Sandbox testing is available only for the app with a debug signature. To build a debug-signature app, perform the following steps:
    
    1\. [Request a debug certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-cert-0000002283256797), [register a debugging device](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-device-0000002283189937), and [request a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278) in AppGallery Connect. Then, [manually configure signing information](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section112371245115818).
    
    2\. [Configure the public key fingerprint](https://developer.huawei.com/consumer/en/doc/app/agc-help-cert-fingerprint-0000002278002933) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
    

#### Troubleshooting Sandbox Access Issues

If you fail to access the sandbox, please refer to [Preparing for Sandbox Testing](#section1055471316) to check the following items:

-   Check whether a test account has been added in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/).
-   Check whether the app has a debug signature.

Besides, you can also use the [isSandboxActivated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section634215616315) API within your app to figure out why the sandbox environment does not work.

#### Testing Consumable or Non-consumable Purchases

During sandbox testing, the [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) API is called to bring up the checkout screen. Users go through the standard purchase process, but no actual charges will be incurred.

-   The purchase process in the sandbox environment mirrors that of the production environment, requiring users to bind a payment method. However, no actual charges will be incurred during this process.
-   In the receipt information [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) of a successful payment, an **environment** field with the value **SANDBOX** will be included to indicate that this payment happens in the sandbox environment.
-   In the sandbox environment, after a non-consumable is purchased, your app needs to acknowledge the delivery. Then, the non-consumable can be purchased again for testing purposes.
-   A sandbox testing reminder will be displayed on the checkout screen and also the result screen, as shown in the figures below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/XMgTRzmiRECSwcgIGXETzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27A6A767DB26CC687A10ABFB24C5EB25BAB0CB91847CAC8D950E1CA031C09C17)

If the screens in the following figures are not displayed, it means this transaction is not in the sandbox environment, and further testing will incur real charges. Refer to [Troubleshooting Sandbox Access Issues](#section549681919384) for a self-check.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/SwMx9j-yQ-C2AqbBdM6EfA/en-us_image_0000002413174268.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EDCE152FA523AC378FE91957E267B18D13EB2377A90BB2B5A4A08BD3BF6811A "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/4rGt0JPsQbCGYj8Z7_nRoQ/en-us_image_0000002413174248.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E53D55328CF3CCDCA63FB5BBDD597BA0B2C84164A1A346D2C8101DD5D008CCF0 "Click to enlarge")

#### Testing Auto-renewable Subscriptions

The purchase process of auto-renewable subscriptions is similar to that of consumables and non-consumables. However, auto-renewable subscriptions introduce complexities like renewal result (successful or failed) and billing cycle. To help you test your app's subscription features faster, we have added a "time machine" in the sandbox environment. This makes subscription renewals happen much quicker. In the sandbox, 10 seconds is like a whole day in real life. For example, for a weekly subscription, the renewal will occur 70 seconds after the initial purchase is successful.

-   The subscription process in the sandbox environment mirrors that of the production environment, requiring users to bind a payment method. However, no actual charges will be incurred during this process.
-   In the receipt information [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) of a successful payment, an **environment** field with the value **SANDBOX** will be included to indicate that this payment happens in the sandbox environment.
-   Auto-renewal processing does not require actual payment, and the IAP will return a success result directly.
-   In the sandbox testing environment, once the user initiates the first subscription cycle, the system will automatically renew it five more times (six cycles in total). After that, the user must manually resume the subscription. If a [promotional offer](../product-purchase/auto-renewable-subscription-purchase/understanding-auto-renewable-subscriptions/document.md#section15231185754812) is involved, the system will first complete auto-renewals for the promotional period, then proceed with the standard six-cycle renewal. In this case, the total number of renewals equals the number of promotional cycles plus six.
-   A sandbox testing reminder will be displayed on the checkout screen and also the result screen, as shown in the figures below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/EKNUF0XqRP2jbrCC0f6QaQ/en-us_image_0000002446613509.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20FDDD639FD8291C44BCE8E30C63BC1577B6C9F0BAB4B29C366682E7EA6C3F20 "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/GGzQ77sfQPK3-lXmir3LYg/en-us_image_0000002413014392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4C7180DD75C05A06CCA649B2929C16C6ABC30F59AE8666806CAC2059AAAF39A "Click to enlarge")

#### Testing Non-renewable Subscriptions

During sandbox testing, the [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) API is called to bring up the checkout screen. Users go through the standard purchase process, but no actual charges will be incurred.

-   The purchase process in the sandbox environment mirrors that of the production environment, requiring users to bind a payment method. However, no actual charges will be incurred during this process.
-   In the receipt information [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) of a successful payment, an **environment** field with the value **SANDBOX** will be included to indicate that this payment happens in the sandbox environment.
-   A sandbox testing reminder will be displayed on the checkout screen and also the result screen, as shown in the figures below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/FrDos5LgRQunUZV8wepVyA/en-us_image_0000002446613477.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CE0EB251BEDF44B534B33253D4D5D05DC43F8DABFE7958335891B3A0FCB438D "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/mEtrkGwgQsaf4EcqodRccQ/en-us_image_0000002413014408.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34E9FDC49B3EDC4E6F897009184F3EC49416EF3A623BB6D4C26A563BC6AE69AC "Click to enlarge")

#### Testing Refund Requests

You can use a sandbox account to submit a refund request for an order generated in the sandbox environment. For this refund request, the IAP server will automatically skip the refund review and also the payment refunding to the original payment method (as no actual charges are made in the sandbox environment). The IAP server will automatically approve the refund request by default in the sandbox environment and simultaneously send a refund success event notification to your server. Upon receiving this notification, you can test scenarios like in-app entitlement revocation.

To test a refund request, proceed as follows:

1.  Purchase a product with a sandbox account in the app's sandbox environment. A sandbox order is automatically created under **Settings** > **HUAWEI ID** > **Payment & purchases** > **Purchase history** on the test device.
2.  Tap the sandbox order whose refund request is to be tested. Then, on the **Details** screen, tap **Report issue**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/TUc8GF73Rc-3hv-T7CtLig/en-us_image_0000002446733361.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE6FC32464009DFD69368324B5BA80BC56B38300BEEBDE3FC9AEAE587AA44C62 "Click to enlarge")
    
3.  On the **Report issue** screen, tap **Request refund**, select a reason, fill in necessary information, and tap **Submit**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/1aVxYhuIQn-yV2wK6nMTuw/en-us_image_0000002478360074.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18D6274E5CF6E73495517CA103860BD6E192A90B12448F8DE26D351960960034 "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/xwnUaYVGT5eccvLXVUB-ww/en-us_image_0000002510320007.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0BDA63802DFB6EFBE66852F174FD7D0A233769BFAC16ED332FDA6054EE6C21F "Click to enlarge")
    
4.  After the refund request is submitted, the IAP server skips both the refund review and the payment refunding to the original payment method. The IAP server then automatically approves the refund request and simultaneously sends a refund success event notification (**NotificationSubtype**: **REFUND\_TRANSACTION**) to your server. If you have configured the address of the sandbox environment server, the notification will be sent to this server. For details, please refer to [Activating the In-App Purchases Service and Configuring Event Notifications](https://developer.huawei.com/consumer/en/doc/app/parameters-0000001931995692).
5.  After receiving the refund success event notification, you can simulate in-app operations like revoking entitlements for the involved sandbox account in the sandbox environment for testing purposes.

#### Clearing the Purchase History of a Sandbox Account

You can clear the purchase history of a sandbox account for a fresh start of more testing. Clearing the purchase history indicates that all purchase records (including auto-renewable subscriptions, consumables, and non-consumables) generated by the test account in the sandbox environment will be deleted. Then, the account can purchase auto-renewable subscriptions, consumables, and non-consumables in the sandbox environment again. The operation of clearing the purchase history cannot be undone. This operation does not affect data in the production environment.

Here are the steps to clear the purchase history of a sandbox account:

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Users and permissions**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/zR4Z3aIjTMegDzPVyT_hPQ/en-us_image_0000002413174244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5E7E78D124EF8BCD823CCCFB949C97E157B8C0BAB5C1758C4EB0E9D5C700470 "Click to enlarge")
    
2.  In the navigation pane on the left, choose **Sandbox** > **Test accounts**, select a test account, and click **Clear purchase history** in the upper right corner.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/nLjSD18hTbaGIiWvUF49HA/en-us_image_0000002446733433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=894ECBF9ACA8265870EBF31B561D612A0A86AA16E8B23D70EA490A74025B1246 "Click to enlarge")
    
3.  In the dialog box that is displayed, click **OK**. The purchase history of this account in the sandbox environment will be cleared, and this operation cannot be undone. If this account has a significant purchase history, the process of clearing its purchase history could be time-consuming.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/bBuhCcwFQe2Jx2xKkLHcqg/en-us_image_0000002446733425.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0DB080BCCAC6B99B2CEBE2323709026AA634A3E7F244D3E8AE34567DB147AE9 "Click to enlarge")
    

#### Testing the Scenario Where a Product Purchase Fails

When the sandbox testing conditions are met, call the [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) API to bring up the checkout screen. If the configuration for interrupting your test account's purchase flow is enabled, you will be blocked right after confirming an order. This is useful for you to test how your app's error handling for failed purchases. To simulate a purchase failure, follow these steps:

1.  In [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), [enable the configuration for interrupting your test account's purchase flow](https://developer.huawei.com/consumer/en/doc/app/agc-help-testaccount-0000001146438651#section9546175114555).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/9MSxlFlZROCegDW7_3gOmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CE2F85CDBA23E2C2BC2B05D9C034B452F690DE7EBEC3E2F876A8F45FB6CFA9F)
    
    If you have changed the configuration for interrupting your test account's purchase flow, wait 3 to 5 minutes before placing an order to make sure that the configuration actually takes effect.
    
2.  Try purchasing a consumable, non-consumable, non-renewable subscription, or auto-renewable subscription. The checkout screen is displayed as expected.
3.  After confirming the purchase, you will see a message indicating that the service is unavailable and try again later, and your app will receive error [1001860056](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-error-code#section446955461117) indicating that the transaction is rejected.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/iAXcoVfxRH2Zl8JogXybSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54482F57F650AE2ADFD81EA7A2457641E9E92D9A66FB35FCA4A165D96DB908E3)
    
    If the purchase result is different from what is expected, wait 1 minute and try again.
    

#### Testing the Scenario Where a Subscription Auto-Renewal Fails

When the sandbox testing conditions are met and your test account has already purchased an auto-renewable subscription, you can simulate a failed renewal. To do this, first enable the configuration for interrupting your test account's purchase flow in AppGallery Connect. This will let you simulate scenarios where a subscription auto-renewal fails. When the test account's subscription repeatedly fails to renew, the subscription will eventually expire. At this point, the IAP server will send a notification to your app server indicating the subscription has expired. Upon receiving this expiry event notification, you can test scenarios like revoking in-app entitlements.

To simulate a subscription auto-renewable failure, follow these steps:

1.  Try purchasing an auto-renewable subscription.
2.  In [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), [enable the configuration for interrupting your test account's purchase flow](https://developer.huawei.com/consumer/en/doc/app/agc-help-testaccount-0000001146438651#section9546175114555).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/iSDEOGhITRqT-MfHIR5itg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC192B63D46ADA8F71E99F3671D4CB6157C1B9123FEE4D1E3EC2A7B2B18C309E)
    
    If you have changed the configuration for interrupting your test account's purchase flow, wait 3 to 5 minutes before placing an order to make sure that the configuration actually takes effect.
    
3.  On the test device, go to **Settings** > **HUAWEI ID** > **Payment and purchases** > **Subscriptions** and check the details of the subscription mentioned in the preceding step. You will see a subscription auto-renewable exception message.
