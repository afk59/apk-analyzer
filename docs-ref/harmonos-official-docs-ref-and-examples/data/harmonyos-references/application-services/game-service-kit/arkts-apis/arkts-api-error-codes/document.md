# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/VhPF0wUERy2N1sX83ysb7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C1CFD7FDCBAC5A0C52FA505DE9B344D49CFCB6B0149B22FC8681DB817011939)

This section describes only the error codes related to Game Service Kit. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1010300001 Internal System Error

**Message**

System internal error.

**Description**

Internal system error.

**Possible causes**

An internal error occurs in the Game Service Kit system.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004&amp;keyWord=Game Service Kit>). Huawei technical support will get back to you as soon as possible.

#### 1010300002 Authentication Failure

**Message**

Auth failed.

**Description**

Authentication failed.

**Possible causes**

The network connection is abnormal, or a parameter passed is invalid.

**Solution**

1.  For users' first sign-in on a device, the network must be properly connected.
2.  Ensure that the parameters passed to the [init](../gameperformance-game-scene-perception/document.md#section131971556806) API are valid.

#### 1010300003 Invalid Request

**Message**

Invalid request.

**Description**

Invalid request.

**Possible causes**

Other APIs are called when the initialization is not performed or fails.

**Solution**

Call the [init](../gameperformance-game-scene-perception/document.md#section131971556806) API first and ensure that the API is successfully called.

#### 1002000001 Common Internal Error

**Message**

System internal error.

**Description**

Common internal error.

**Possible causes**

Possible causes are:

-   The total size of input parameter **accountIcon** passed to the [unionLogin](../gameplayer-basic-game-service/document.md#section157848375136) API exceeds 35 KB.
-   Input parameter **context** passed to the API does not meet the requirements.

**Solution**

1.  Ensure the size of the official game account icon does not exceed 35 KB.
2.  Ensure that input parameter **context** passed to each API meets the requirements. You are advised to obtain **context** in the following way:
    
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    
3.  [Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004&amp;keyWord=Game Service Kit>). Huawei technical support will get back to you as soon as possible.

#### 1002000002 Network Error

**Message**

Network connection error.

**Description**

Network error.

**Possible causes**

Possible causes are:

-   The debug certificate signature is not configured.
-   The fingerprint for the debug certificate is not added.
-   The **client\_id** and **app\_id** in the **module.json5** file of the **entry** module are inconsistent with those in AppGallery Connect.
-   Network connection error.

**Solution**

1.  Ensure that configuration items are correctly set. For details, please refer to [Development Preparations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gameservice-gameplayer-huawei#en-us_topic_0000002385861065_section818512085410).
2.  Ensure that the network connection is working properly.

#### 1002000003 No HUAWEI ID Information Is Found

**Message**

The HUAWEI ID is not signed in or not authorized.

**Description**

No HUAWEI ID information is found.

**Possible causes**

No HUAWEI ID information is found.

**Solution**

Ensure that the user has signed in using a HUAWEI ID and granted authorization.

#### 1002000004 Identity Verification Is Required But the Player Cancels It or Identity Verification Has Not Been Performed

**Message**

User cancels real name authentication or not real name.

**Description**

Identity verification is required but the player cancels it or identity verification has not been performed.

**Possible causes**

Identity verification is required but the player cancels it or identity verification has not been performed.

**Solution**

Call the [unionLogin](../gameplayer-basic-game-service/document.md#section157848375136) API again to instruct the user to perform identity verification.

#### 1002000005 Only HUAWEI IDs with Both the Service Area and Registration Location Within the Chinese Mainland Are Supported

**Message**

The country or region of the signed-in Huawei ID does not support.

**Description**

Only HUAWEI IDs with both the service area and registration location within the Chinese mainland are supported.

**Possible causes**

The service area or registration location of the HUAWEI ID may not be within the Chinese mainland.

**Solution**

When a user attempts to sign in to the game, prompt them to use or register a HUAWEI ID whose service area and registration location are both within the Chinese mainland.

#### 1002000006 The Player Is a Minor and the Current Time Is Not Within the Permitted Game Duration

**Message**

User is underage and has no playable time.

**Description**

The player is a minor and the current time is not within the permitted game duration.

**Possible causes**

The player is a minor and the current time is not within the permitted game duration.

**Solution**

Check whether the current game time of the minor is between 20:00 to 21:00 on Friday, Saturday, Sunday, or legal holidays.

-   If not, the game exit logic has been configured in Game Service Kit. No extra processing is required.
-   Otherwise, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004). Huawei technical support will get back to you as soon as possible.

#### 1002000007 The App to Which the Product Belongs Is Not Released to Specified Countries or Regions

**Message**

The application to which the product belongs is not listed in the specified country.

**Description**

The app to which the product belongs is not released to specified countries or regions.

**Possible causes**

The app to which the product belongs is not released to specified countries or regions.

**Solution**

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). Click **My apps**, select an app, and go to **Distribute** > **Version information** > **Draft**. Then check the countries or regions to which the app will be released.

#### 1002000008 The HUAWEI ID Is in the Blocklist

**Message**

The HUAWEI ID is in the blocklist.

**Description**

The HUAWEI ID is in the blocklist.

**Possible causes**

-   Games are not allowed on the National Memorial Day.
-   The player with the current HUAWEI ID is prohibited from playing games due to risk control.

**Solution**

-   If there are pop-ups related to risk control or the National Memorial Day, no action is required.
-   In other cases, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004&amp;keyWord=Game Service Kit>). Huawei technical support will get back to you as soon as possible.

#### 1002000009 Third-Party Game Accounts Are Not Supported Currently

**Message**

The game account is unavailable for the game.

**Description**

Third-party game accounts are not supported currently.

**Possible causes**

The account used for sign-in is invalid.

**Solution**

Use another game account.

#### 1002000010 teamPlayerId Does Not Match the Current Player

**Message**

The playerId is not current player.

**Description**

**teamPlayerId** does not match the current player.

**Possible causes**

When the [bindPlayer](../gameplayer-basic-game-service/document.md#section2090261116551) or [unbindPlayer](../gameplayer-basic-game-service/document.md#section57861515615) API is called, an incorrect **teamPlayerId** is passed.

**Solution**

Check whether **teamPlayerId** is correct. If it is not correct, call the [bindPlayer](../gameplayer-basic-game-service/document.md#section2090261116551) or [unbindPlayer](../gameplayer-basic-game-service/document.md#section57861515615) API again to pass the correct **teamPlayerId**.

#### 1002000011 The Player Has Not Confirmed the Agreement or Privacy Statement

**Message**

Agreement not agreed.

**Description**

The player has not confirmed the agreement or privacy statement.

**Possible causes**

The player cancels the privacy agreement, or another API is called before the **init** API is successfully called.

**Solution**

Call the [init](../gameplayer-basic-game-service/document.md#section131971556806) API again.

#### 1002000012 The Official Game Account Has Been Associated with teamPlayerId

**Message**

The thirdOpenId or teamPlayerId has been bound.

**Description**

The official game account has been associated with **teamPlayerId**.

**Possible causes**

When the [bindPlayer](../gameplayer-basic-game-service/document.md#section2090261116551) API is called, the official game account has been associated with **teamPlayerId**.

**Solution**

No action is required.

#### 1002000013 The Official Game Account Is Not Associated with teamPlayerId

**Message**

The thirdOpenId and teamPlayerId are not bound.

**Description**

The official game account is not associated with **teamPlayerId**.

**Possible causes**

When the [unbindPlayer](../gameplayer-basic-game-service/document.md#section57861515615) API is called, the official game account has not been associated with **teamPlayerId**.

**Solution**

No action is required.

#### 1002000014 This API Is Not Available for This Game

**Message**

This interface is not available for this game.

**Description**

This API is not available for this game.

**Possible causes**

This API cannot be called by the current game.

**Solution**

1.  Check whether the error is reported when the [unionLogin](../gameplayer-basic-game-service/document.md#section157848375136) API is called in the current game.
2.  If yes, try an API other than **unionLogin**.
3.  If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004&amp;keyWord=Game Service Kit>). Huawei technical support will get back to you as soon as possible. If the error is not reported, the current game does not have permission to use the **unionLogin** API. In this case, use another API.
4.  If your game needs to use the **unionLogin** API but does not have permission to use it, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004). Huawei technical support will get back to you as soon as possible.

#### 1002000015 The Player Information Is Invalid

**Message**

The current player information is invalid.

**Description**

The player information is invalid.

**Possible causes**

The user switches to another HUAWEI ID after signing in to the game. As a result, the current player information in the game becomes invalid.

**Solution**

Call the [unionLogin](../gameplayer-basic-game-service/document.md#section157848375136) API again to obtain the player information.

#### 1002000016 The Player Cancels Multi-provider Sign-In

**Message**

Union login canceled by user.

**Description**

The player cancels multi-provider sign-in.

**Possible causes**

The player cancels multi-provider sign-in during the multi-provider sign-in process.

**Solution**

To continue the sign-in, call the [unionLogin](../gameplayer-basic-game-service/document.md#section157848375136) API again.

#### 1002000017 Invalid App

**Message**

Illegal application identity.

**Description**

Invalid app.

**Possible causes**

The configuration such as the client ID, app ID, and signature is incorrect or missing.

**Solution**

Ensure that information such as [app ID, client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gameservice-gameplayer-huawei#en-us_topic_0000002385861065_section7658201162412), and [signing certificate fingerprint](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gameservice-gameplayer-huawei#en-us_topic_0000002385861065_section205943551234) is correctly configured.

#### 1002000018 API Available Only for Mini Games

**Message**

This API is only provided for HarmonyOS mini games.

**Description**

This API is available only for mini games.

**Possible causes**

This API is used in a game that is not a mini game.

**Solution**

Use a supported API.

#### 1002000019 Parameter Error

**Message**

Parameter error.

**Description**

Parameter error.

**Possible causes**

-   A mandatory parameter is not passed.
-   Incorrect parameter type. (Type Error)
-   The number of parameters is incorrect. (Argument Count Error)
-   Null is passed to a parameter that requires a value. (Null Argument Error)
-   Invalid parameter format. (Format Error)
-   The parameter value is out of the valid range. (Value Range Error)

**Solution**

Ensure that all mandatory parameters are specified and that all parameters are of the valid types. Pass parameters according to the relevant requirements.

#### 1002000020 Current Operation Canceled by the User

**Message**

The operation was canceled by the user.

**Description**

The current operation is canceled by the user.

**Possible causes**

The user canceled the current operation.

**Solution**

Display a message to the user, indicating that the operation is canceled.

#### 1002000021 Excessive API Call Frequency

**Message**

Too frequent API calls.

**Description**

The API is called too frequently.

**Possible causes**

The API is called too frequently.

**Solution**

Avoid excessive API calls. The current default access interval for the API is 5 seconds.

#### 1002000050 Invalid Product Information

**Message**

Invalid product information.

**Description**

The product information is invalid.

**Possible causes**

1.  The passed product ID or type is incorrect.
2.  The product created in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) has not been submitted for review or has not been approved. For details about how to create and submit a product for review, please refer to [Adding a Single Product](https://developer.huawei.com/consumer/en/doc/app/new-0000001931836320).

**Solution**

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). Click **My apps**, select an app, and go to **Operate** > **Products** > **Product Management**. In the product list, check whether the product exists, and if so, check whether all its mandatory information is provided and has been approved. If the product fails to be approved, use a sandbox account for testing. For details, please refer to [Sandbox Testing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-sandbox).

#### 1002000051 Purchase Failure Because the User Already Owns the Product

**Message**

Failed to purchase a product because the user already owns the product.

**Description**

The purchase failed because the user already owns the product.

**Possible causes**

The product has already been purchased.

**Solution**

Use the [queryPurchases](../../../iap-kit/arkts-apis/iap/document.md#section1147122418532) API to check whether the user has purchased the product.

-   For a consumable or non-renewable subscription that has been purchased, check whether the product is delivered, and if so, call the [finishPurchase](../../../iap-kit/arkts-apis/iap/document.md#section124751324135814) API to complete the purchase. Then, the product can be purchased again.
-   If the product is a non-consumable or an auto-renewable subscription, it can only be purchased once.

#### 1002000052 Delivery Failure Because the User Does Not Own the Product

**Message**

The purchase cannot be finished because the user has not paid for it.

**Description**

The delivery failed because the user does not own the product.

**Possible causes**

The user has not purchased the product.

**Solution**

Use the [queryPurchases](../../../iap-kit/arkts-apis/iap/document.md#section1147122418532) API to check whether the user has purchased the product.

#### 1002000053 Repeated Delivery

**Message**

The purchase has been finished and cannot be finished again.

**Description**

The product has been delivered. No more delivery is needed.

**Possible causes**

The product has been delivered. No more delivery is needed.

**Solution**

Use the [queryPurchases](../../../iap-kit/arkts-apis/iap/document.md#section1147122418532) API to check whether the product has a delivery acknowledgement record.

#### 1002000054 Service Area Unsupported by IAP Kit

**Message**

The country or region of the signed-in HUAWEI ID does not support IAP.

**Description**

The country or region to which the signed-in HUAWEI ID belongs is not supported by IAP Kit.

**Possible causes**

The country or region to which the signed-in HUAWEI ID belongs is not supported by IAP Kit.

**Solution**

For signed-in HUAWEI IDs whose service area is not within the Chinese mainland, you are advised to hide the entry points for related payment functions in your app.

#### 1002000056 Transaction Rejected

**Message**

The user is not allowed to make purchase.

**Description**

The user transaction is rejected.

**Possible causes**

The transaction behavior triggers IAP Kit risk control.

**Solution**

Try again later or change the payment method.

#### 1018300001 Common Internal Error

**Message**

System internal error.

**Description**

Common internal error.

**Possible causes**

An internal error occurs in the Game Service Kit system.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004&amp;keyWord=Game Service Kit>). Huawei technical support will get back to you as soon as possible.

#### 1018300002 Authentication Failed

**Message**

Authentication failed.

**Description**

Authentication failed.

**Possible causes**

The network connection is abnormal, parameters passed to the API are invalid, or the app ID is not configured in the trustlist.

**Solution**

1.  For users' first sign-in on a device, the network must be properly connected.
2.  Ensure that the parameters passed to the [create](../gamenearbytransfer-nearby-transfer/document.md#section131971556806) API are valid.
3.  If your app ID is not configured in the trustlist, contact the operations personnel to add your app ID in the trustlist. For details, please refer to [Preparations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gameservice-nearbytransfer-config-agc).

#### 1018300003 Invalid Request

**Message**

Invalid request.

**Description**

Invalid request.

**Possible causes**

Other APIs are called when the nearby transfer service has not been created or fails to be created.

**Solution**

Call the [create](../gamenearbytransfer-nearby-transfer/document.md#section131971556806) API first to perform initialization. Make sure that the API is successfully called.

#### 1018300004 Service Unavailable

**Message**

No service available.

**Description**

Service unavailable.

**Possible causes**

No nearby devices can be bound to.

**Solution**

After confirming that the receiver has published the nearby transfer service, try discovering a device again and bind to the service.

#### 1018300005 WLAN and Bluetooth Must Be Enabled

**Message**

The wireless network and Bluetooth should be enabled at the same time.

**Description**

WLAN and Bluetooth must be enabled at the same time.

**Possible causes**

WLAN and Bluetooth are not enabled simultaneously on the device where the game is installed.

**Solution**

Enable WLAN and Bluetooth on the device simultaneously.

#### 1018300006 Publishing Failed

**Message**

Publish failed.

**Description**

Publishing failed.

**Possible causes**

Publishing failed.

**Solution**

Internal system error. Try publishing the nearby transfer service again.

#### 1018300007 Discovery Failed

**Message**

Discovery failed.

**Description**

Discovery failed.

**Possible causes**

No devices are found.

**Solution**

After confirming that the receiver has published the nearby transfer service, try discovering a device again.

#### 1018300008 Invalid Parameter

**Message**

Invalid parameter.

**Description**

Invalid parameter.

**Possible causes**

1.  A mandatory parameter is left empty.
2.  Invalid parameter type.
3.  Failed to verify the parameter.

**Solution**

Ensure that all mandatory parameters are specified and that all parameters are of the valid types. Pass parameters according to the relevant requirements.
