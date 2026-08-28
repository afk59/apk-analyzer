# Pre-release Check

Review your game against the following checklist before submitting it for release, so your game can have a better chance to get approved.

After the self-check, submit your game for release review in AppGallery Connect.

| 
Level-1 Category

 | 

Level-2 Category

 | 

Check Item

 | 

Impact

 |
| :-- | :-- | :-- | :-- |
| 

Compliance check

 | 

Privacy, game qualification, and more

 | 

Your game meets the requirements for content, security, user privacy, and others. For details, please refer to [AppGallery Review Guidelines](https://developer.huawei.com/consumer/en/doc/50104).

 | 

If your game does not meet the requirements, it will be rejected.

 |
| 

User identity verification information

 | 

Before submitting the game for release review, complete the National Press and Publication Administration identity verification application and obtain approval.

 | 

The release application may be rejected.

 |
| 

Configuration check

 | 

App category

 | 

Sign in to AppGallery Connect and check whether you have classified your game into the game category.

 | 

If not, the anti-addiction mechanism will not function properly and your game release request will be rejected.

 |
| 

Release package version

 | 

A package of the release version needs to be used when you release your game. Check the relevant parameter setting in the **oh-uni-package.json** file under the SDK directory, and replace the app package if it is not a release version. Alternatively, the check can also be completed as follows: After the package is generated, decompress the package and check the **releaseType** field in the **pack.info** file under the HAP resource directory.

 | 

If the package is not of the release version, the release request will be rejected.

 |
| 

Fingerprint information in the signing certificate

 | 

You need to add the corresponding fingerprint for the release certificate in the release phase.

 | 

If the corresponding fingerprint is not added, your game release will be affected.

 |
| 

App ID mapping

 | 

Sign in to AppGallery Connect and [configure the app ID mapping](../online-game-sign-in/mandatory-sign-in-with-a-huawei-id/document.md#en-us_topic_0000002385861065_section3907114313255).

 | 

If the app ID mapping is not configured, your game release will be affected.

 |
| 

**module.json5** file

 | 

In the **module.json5** file of the **entry** module in the project, check whether **client\_id** and **app\_id** in **metadata** are correctly configured.

 | 

If the configuration is incorrect, Game Service Kit APIs cannot be called.

 |
| 

Code check

 | 

Initialization

 | 

After the game is launched, the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section131971556806) API must be called first before other APIs.

 | 

If the game does not call the **init** API, your game release request will be rejected.

 |
| 

Sign-in

 | 

When using the HUAWEI ID sign-in icon, you must comply with the [Management Rules for Using the Sign-in Capability of Account Kit](../../../../account-kit/management-rules-for-using-the-sign-in-capability-of-account-kit/document.md).

 | 

If the condition fails to be met, your game release may be affected.

 |
| 

-   For users who sign in to your game using their HUAWEI IDs, their account assets must be synchronized between the HarmonyOS 4-and-earlier version and HarmonyOS 5.0-and-later version of your game.
-   For users who sign in to your game using their official game accounts, account asset interoperability must be implemented between the official version and HarmonyOS 5.0-and-later version of your game.

 | 

If account asset interoperability is not implemented, your game release will be affected.

 |
| 

The game must call the [unionLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section157848375136) API to display the multi-provider sign-in panel.

 | 

If your game does not call the **unionLogin** API, your game release request will be rejected.

 |
| 

If a user has not signed in to their device using a HUAWEI ID, the [unionLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section157848375136) API will display the HUAWEI ID sign-in pop-up of the device. After the user taps the back button on the pop-up, it should not be displayed again unless the user manually opens it.

 | 

If the HUAWEI ID sign-in pop-up of the device cannot be manually opened or is automatically displayed repeatedly, your game release request will be rejected.

 |
| 

If your game provides the official account sign-in mode, the last used sign-in account will be used by default for players. You are advised to provide the [in-game account switch](../online-game-sign-in/sign-in-with-an-official-game-account/document.md#en-us_topic_0000002385861113_section26517112362) function for players to select a different sign-in account. When displaying the multi-provider sign-in panel again, your game is required to call the [unionLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section157848375136) API to set **showLoginDialog** in **loginParam** to **true**. If the [unionLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section157848375136) API is called, the [getLocalPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section17453143012584) API does not need to be called in the game sign-in process.

 | 

It is recommended that your game allow players to reselect their sign-in account to avoid a negative impact on the sign-in experience.

 |
| 

After a player signs in to your game, the game is required to call the [verifyLocalPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section15119154416715) API to perform compliance verification, including identity verification and anti-addiction control status verification of the HUAWEI ID signed in on the current device. If the verification fails, the corresponding error code will be returned.

 | 

If your game does not call the **verifyLocalPlayer** API, your game release request will be rejected.

 |
| 

Payment

 | 

If your game provides in-app purchases, you must integrate [IAP Kit](../../../../iap-kit/document.md) into your app.

 | 

If your game does not call the **createPurchase** API, your game release request will be rejected.

 |
| 

The product ID and type passed to the **purchase** API should be consistent with those configured in AppGallery Connect.

 | 

If the product ID and type passed during payment do not match those in AppGallery Connect, the payment page cannot be displayed.

 |
| 

The order redelivery logic needs to be executed when the payment API returns a response and when the app is launched. The relevant error codes include [1001860001](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-error-code#section194868144472) and [1001860051](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-error-code#section5254205612317). For details, please refer to [Delivering a Consumable/Non-consumable Product](../../../../iap-kit/product-purchase/consumable-or-non-consumable-purchase/delivering-a-consumable-non-consumable-product/document.md).

 | 

If order redelivery is not implemented, the purchased product may fail to be delivered when an exception (such as process termination or crash) occurs.

 |
| 

Game exit

 | 

Games released in the Chinese mainland must provide the exit function for players.

 | 

If your name fails to provide the exit function, your game release request will be rejected.

 |
