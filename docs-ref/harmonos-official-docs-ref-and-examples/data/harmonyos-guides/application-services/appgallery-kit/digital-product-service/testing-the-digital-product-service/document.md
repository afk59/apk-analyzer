# Testing the Digital Product Service

You can use the sandbox testing service to test processes like digital product purchase without real payment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/E58c0P-4Q3KQepuBCaQdgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08FEE3BA194A6F8FB4DCDE61F32B00AB8ADCB9667D29EFBE7A6736762CBDFA79)

Sandbox orders are not real transactions and cannot be found in **Developer center** > **My reports** > **HUAWEI IAP**.

#### Preparing for Sandbox Testing

-   Configuring a test account
    
    Add test accounts, which are real HUAWEI IDs, under **Users and permissions** in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). Before performing tests in the IAP sandbox environment on a HarmonyOS device, sign in to the device with the test account already configured. To add a test account, do as follows:
    
    1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Users and permissions**.
    2.  Go to **Sandbox** > **Test accounts** and click **Add**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/8gzibYXnT1OgMU0hiMHVPA/en-us_image_0000002337894564.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E29E6CBAF26B32B458B7E0127EE934416EE711D98ACD69F64EAEF732DBF4642A "Click to enlarge")
        
    3.  Specify test account information and click **OK**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/HfvI1dIPREWXBAvV8X5WMQ/en-us_image_0000002371652933.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E41FA3B7168CFB4DA30007CCA8741490C14BD1010D537959E661CB4AC3B7588A)
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/qrlMODZ-TN-1SlYQQtBYwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36A6FFC8D3DF0651B688FDE7C85E461BB5601DAB8477BFCFCF40B890ABF66E1C)
    
    A test account must be a registered HUAWEI ID. It takes 5 to 10 minutes for the configuration to take effect. Before starting sandbox testing, make sure that you have configured the HUAWEI ID you will use for sandbox testing as a test account.
    

-   Building an app with a debug signature
    
    Sandbox testing is available only for the app with a debug signature. To build a debug-signature app, perform the following steps:
    

1.  Follow the instructions [here](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-app-0000001914423098) to request an app debug certificate, register a debugging device, and request a debug profile.
2.  [Configure the signing information](../../../../app-release/release/document.md#section280162182818) in DevEco Studio.
3.  [Configure the signing certificate fingerprint](https://developer.huawei.com/consumer/en/doc/app/agc-help-signature-info-0000001628566748#section5181019153511) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

#### Troubleshooting Sandbox Access Issues

If you fail to access the sandbox, please refer to [Preparing for Sandbox Testing](#section1055471316) to check the following items:

-   Whether a test account has been added in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
-   Whether the app has a debug signature.

Besides, you can also use the [isSandboxActivated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section634215616315) API within your app to figure out why the sandbox environment does not work.

#### Testing Consumable or Non-consumable Purchases

During sandbox testing, your app can bypass the actual payment process by calling the [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) API to simulate a successful purchase.

-   The purchase process in the sandbox environment mirrors that of the production environment, requiring users to bind a payment method. However, no actual charges will be incurred during this process.
-   In the receipt information [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) of a successful payment, the **environment** field with the value **SANDBOX** will be included to indicate that this payment happens in the sandbox environment.
-   In the sandbox environment, after a non-consumable is purchased, your app needs to acknowledge the delivery to complete the purchase. Then, the non-consumable can be purchased again for testing purposes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/JVhZqiKDTaCao-MDuelhIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=912FF71151CF431AD447738C81845357E79FF2C4124758247AD9996B6201EAA8)
    
    In the production environment, a user can purchase the same non-consumable only once.
    
-   A sandbox testing reminder will be displayed on the checkout screen and also the result screen, as shown in the figures below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/B9JS836CStOgzJsO24IsJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1482CBDB128C3B0324901EEC12EAF89DE34858891260F8BCAABA471543BD123)

If you have not seen any sandbox testing reminder, it is because this purchase did not happen in the sandbox environment. If you continue with testing in this case, actual charges will be incurred. Check whether your app has met the two requirements listed in **Troubleshooting Sandbox Access Issues**. Besides, you can also use the [isSandboxActivated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section634215616315) API within your app to figure out why the sandbox environment does not work.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p><span><img height="477.821519" originheight="3264" originwidth="1540" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ULXyXoyiQXq1qKR8zgiuKA/en-us_image_0000002371652937.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=248596A4F3E284EDD56E9364669D942ACBCDA36B920087133F6D5104069C2242" title="Click to enlarge" width="225.435"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p><span><img height="465.133186" originheight="3264" originwidth="1540" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/HurKY1nXRtKgFbRh2O1EFA/en-us_image_0000002337734816.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=896A7AFA45E0A75E124AFBBAA4BF9EEE986AEDE9741FF43F62E2F521FABC9CD1" title="Click to enlarge" width="219.45000000000002"></span></p></td></tr></tbody></table>

#### Testing Auto-renewable Subscriptions

The purchase process of auto-renewable subscriptions is similar to that of consumables and non-consumables. However, subscriptions introduce complexities like renewal result (successful or failed) and billing cycle. To help you test your app's subscription features faster, we have added a "time machine" in the sandbox environment. This makes subscription renewals happen much quicker. In the sandbox, 10 seconds is like a whole day in real life. For example, for a weekly subscription, the renewal will occur 70 seconds after the initial purchase is successful.

-   The subscription process in the sandbox environment mirrors that of the production environment, requiring users to bind a payment method. However, no actual charges will be incurred during this process.
-   In the receipt information [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) of a successful payment, the **environment** field with the value **SANDBOX** will be included to indicate that this payment happens in the sandbox environment.
-   Auto-renewal processing does not require actual payment, and IAP Kit will return a success result directly.
-   A subscription in the sandbox environment will auto-renew 5 times (that is, a total of 6 periods), after which users must manually resume the subscription.
-   In the sandbox testing environment, once the user initiates the first subscription cycle, the system will automatically renew it five more times (six cycles in total). After that, the user must manually resume the subscription. If a [promotional offer](../../../iap-kit/product-purchase/auto-renewable-subscription-purchase/understanding-auto-renewable-subscriptions/document.md#section15231185754812) is involved, the system will first complete auto-renewals for the promotional period, then proceed with the standard six-cycle renewal. In this case, the total number of renewals equals the number of promotional cycles plus six.
-   A sandbox testing reminder will be displayed on the payment screen and also the result screen, as shown in the figures below.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="35.97%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="64.03%">&nbsp;&nbsp;</td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="35.97%"><p><span><img height="431.41675499999997" originheight="3053" originwidth="1440" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/kmAeUsU_Rl-xP95v7Dp2GQ/en-us_image_0000002337734840.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=29DFA3F76228296C81528F1E5E2D8FC867695D9CC72137B79679306F83C09E22" title="Click to enlarge" width="203.49"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="64.03%"><p><span><img height="429.306976" originheight="3053" originwidth="1440" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/WXqjNM4qQ3-u53PBEKMnNQ/en-us_image_0000002337894572.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=174CCA4DACB4D9D99E4B0A597F0450BEBE74054B796CB744D72899B2DA94FA24" title="Click to enlarge" width="202.4925"></span></p></td></tr></tbody></table>

#### Testing Non-renewable Subscriptions

During sandbox testing, the [createPurchase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section18798154545516) API is called to bring up the checkout screen. Users go through the standard purchase process, but no actual charges will be incurred.

-   The purchase process in the sandbox environment mirrors that of the production environment, requiring users to bind a payment method. However, no actual charges will be incurred during this process.
-   In the receipt information [PurchaseOrderPayload](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-data-model#section260562820380) of a successful payment, an **environment** field with the value **SANDBOX** will be included to indicate that this payment happens in the sandbox environment.
-   A sandbox testing reminder will be displayed on the checkout screen and also the result screen, as shown in the figures below.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="38.73%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="61.27%">&nbsp;&nbsp;</td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="38.73%"><p><span><img height="412.2468" originheight="3264" originwidth="1540" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/l9q03JtyS2i4LKGzPgpVow/en-us_image_0000002337734836.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=7A7ADC3FE46A724C0374539F086E480B60AC103765DB25E74A61DA2781E52180" title="Click to enlarge" width="194.51250000000002"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="61.27%"><p><span><img height="413.94853500000005" originheight="3264" originwidth="1540" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/7eC7BIFyS8C1wwQ6Mhp00Q/en-us_image_0000002371732757.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=E4FFDD67C6E408B62F74971C318C36DCFAE62CABEED6BFDBFA1E078F8AC09D3F" title="Click to enlarge" width="195.3105"></span></p></td></tr></tbody></table>

#### Clearing the Purchase History of a Sandbox Account

You can clear the purchase history of a sandbox account for a fresh start of more testing. Clearing the purchase history indicates that all purchase records (including auto-renewable subscriptions, consumables, and non-consumables) generated by the test account in the sandbox environment will be deleted. Then, the account can purchase auto-renewable subscriptions, consumables, and non-consumables in the sandbox environment again. The operation of clearing the purchase history cannot be undone. This operation does not affect data in the production environment.

Here are the steps to clear the purchase history of a sandbox account:

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Users and permissions**.![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/gUpUQdKQQmKK78CrLGkiHw/en-us_image_0000002337734844.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B95329DCD3E88CA0E75996FB62677491229BFFAE29A1D99D69B65FFBA400EE95 "Click to enlarge")
2.  In the navigation pane on the left, choose **Sandbox** > **Test accounts**, select a test account, and click **Clear purchase history** in the upper right corner.![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/v1p78yAXSnyInv2p6eNYzw/en-us_image_0000002337734828.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58CA690A39D54374ED4AFD005D208C12C84A576A51B4F8E8F507A6A553C830C1 "Click to enlarge")
3.  In the dialog box that is displayed, click **OK**. The purchase history of this account in the sandbox environment will be cleared, and this operation cannot be undone. If this account has a significant purchase history, the process of clearing its purchase history could be time-consuming.
    
    <table style="border-style: none;"><tbody><tr><td class="cell-norowborder" style="border: none;" valign="top" width="100%">&nbsp;&nbsp;</td></tr><tr><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p><span><img originheight="348" originwidth="412" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/MMIpWNJ1R06a1mSQHQNJPA/en-us_image_0000002371652909.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=445B55BB5F5CAF8E0B5E1769A186863CFF09A744915250F567AA2FAE130E2EF7"></span></p></td></tr></tbody></table>
