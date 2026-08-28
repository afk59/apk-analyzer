# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/MnTTu2voR2m7ujx8gxfwdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062520Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DF87769CFD0A2652C0D6CBDA6B95FD5EC21789A2BCAC7DFE286ECCE71124B3D)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1010200001 No Permission to Access HUAWEI Wallet

**Message**

No permission to access the Wallet APIs.

**Description**

Identity verification failed for a third-party app.

**Possible causes**

The app is not authorized to call Wallet Kit APIs.

**Solution**

1\. Sign up with AppGallery Connect and integrate Wallet Kit into your app.

2\. Contact the contact person of Wallet Kit and request the permission to call Wallet Kit APIs.

3\. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010200002 HUAWEI Wallet Not Installed

**Message**

Wallet app not found.

**Description**

HUAWEI Wallet has not been installed on the device.

**Possible causes**

HUAWEI Wallet has not been installed on the device.

**Solution**

Download and install HUAWEI Wallet from AppGallery.

#### 1010200003 Environment of HUAWEI Wallet Is Not Ready

**Message**

The environment of the wallet is not ready.

**Description**

The environment of HUAWEI Wallet has not been prepared.

**Possible causes**

1.  The user has not agreed to the user agreement.
2.  The user has not signed in with HUAWEI ID.

**Solution**

Open HUAWEI Wallet, agree to the user agreement, and sign in with HUAWEI ID.

#### 1010200004 Card Cannot Be Activated on the Current Device

**Message**

The device does not support this card.

**Description**

The current device does not support activating this card.

**Possible causes**

The device model is not supported, or the HUAWEI Wallet version is out of date.

**Solution**

Check the device model and software version.

#### 1010200005 Operation Canceled by User

**Message**

The operation was canceled by the user.

**Description**

The user has canceled the operation.

**Possible causes**

The user taps the cancel button.

**Solution**

Check the logs for user cancellation details.

#### 1010200006 Cannot Connect to the Paired Watch

**Message**

The device's remote paired watch cannot be connected.

**Description**

Failed to connect to the paired watch.

**Possible causes**

Failed to connect to the paired watch.

**Solution**

Check the connection status of the watch.

#### 1010200007 OS Version Out of Date

**Message**

The OS version is too old. Please upgrade the OS version.

**Description**

The OS version of the device is out of date.

**Possible causes**

The OS version of the device is out of date.

**Solution**

Upgrade the device OS.

#### 1010200008 HUAWEI Wallet Version Out of Date

**Message**

The wallet version is too old. Please upgrade the wallet version.

**Description**

The HUAWEI Wallet version is out of date.

**Possible causes**

The HUAWEI Wallet version is out of date.

**Solution**

Upgrade HUAWEI Wallet.

#### 1010200009 Insufficient Storage on the Chipset

**Message**

The chip space is full, and no more cards can be added.

**Description**

The chipset storage is insufficient.

**Possible causes**

The chipset storage is full.

**Solution**

1\. Delete unnecessary cards.

2\. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010200010 Unable to Connect to the Network

**Message**

Network connection error.

**Description**

Network connection failed.

**Possible causes**

Network unavailable.

**Solution**

Enable the network and connect again.

#### 1010200011 Failure to Initialize the Environment for HUAWEI Wallet

**Message**

Failed to initialize the environment.

**Description**

Failed to initialize the environment for HUAWEI Wallet.

**Possible causes**

1.  The user has not agreed to the user agreement.
2.  The user has not signed in to their HUAWEI ID.

**Solution**

1.  Open HUAWEI Wallet and agree to the user agreement.
2.  Sign in with HUAWEI ID.

#### 1010200012 Repeated Request

**Message**

Duplicate request.

**Description**

Repeated request.

**Possible causes**

A new request is initiated before the previous request is completed.

**Solution**

Send a new request after the previous request is completed.

#### 1010200013 HUAWEI Wallet Internal Error

**Message**

Operation failed because of an internal error.

**Description**

An internal error occurred in HUAWEI Wallet.

**Possible causes**

An internal error occurred in HUAWEI Wallet.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1010200014 HUAWEI Wallet Used by a Non-Owner User

**Message**

The Wallet APIs can be called by the device owner only.

**Description**

HUAWEI Wallet is used by a user who is not the owner.

**Possible causes**

The user has switched to guest mode or private space.

**Solution**

Switch to the owner account.

#### 1010200015 Child Account Not Supported

**Message**

This card is not available for a child account.

**Description**

Child accounts do not support this card.

**Possible causes**

The user has switched to a child account.

**Solution**

Switch to a non-child account.

#### 1010200016 Country/Region Not Supported

**Message**

This card is not available for the current country or region.

**Description**

This card does not support the current country or region.

**Possible causes**

No transportation card is available in the current country or region.

**Solution**

Switch the service area to the Chinese mainland.

#### 1010200017 HUAWEI Wallet Closed by User

**Message**

The Wallet app was closed by the user.

**Description**

The user has closed HUAWEI Wallet.

**Possible causes**

The user has closed HUAWEI Wallet.

**Solution**

Tap and open HUAWEI Wallet.

#### 1010210102 Token Verification Failure

**Message**

Failed to verify the caller token.

**Description**

Failed to verify the caller token.

**Possible causes**

The token passed is incorrect.

**Solution**

Verify that the token is correct.

#### 1010220002 Card Already Exists

**Message**

The card already exists in the specified device.

**Description**

The card already exists.

**Possible causes**

The card has already been activated on the device.

**Solution**

Delete this card.

#### 1010220003 Service Temporarily Unavailable

**Message**

Pass service is temporarily unavailable.

**Description**

The service is temporarily unavailable.

**Possible causes**

The network or server is faulty.

**Solution**

Verify the network connection and try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010220004 Card Does Not Exist on the Current Device

**Message**

The card does not exist in the specified device.

**Description**

The card does not exist on the current device.

**Possible causes**

The card has been deleted or has not been activated.

**Solution**

Activate the card first.

#### 1010220005 Card Count Reached the Upper Limit

**Message**

The number of cards has reached the upper limit.

**Description**

The number of cards activated has reached the upper limit.

**Possible causes**

The number of activated cards has reached the upper limit.

**Solution**

Delete unnecessary cards.

#### 1010220006 Bluetooth Permission Not Granted

**Message**

Bluetooth permission is not granted.

**Description**

The user has not granted the Bluetooth permission to HUAWEI Wallet.

**Possible causes**

The Bluetooth permission has not been granted.

**Solution**

Grant the Bluetooth permission.

#### 1010220401 Signature Verification Failure upon Card Activation

**Message**

Failed to add the card because the signature verification failed.

**Description**

Failed to verify the signature during card activation.

**Possible causes**

The signature algorithms of the input parameters are inconsistent or the signature content is incorrect.

**Solution**

Verify the input parameters.

#### 1010220402 Data Parsing Failure During Card Activation

**Message**

Failed to add the card because the data decryption failed.

**Description**

Failed to parse data during card activation.

**Possible causes**

The input parameters are encrypted abnormally.

**Solution**

Verify the input parameters.

#### 1010220403 Instance Does Not Exist upon Card Activation

**Message**

Failed to add the card because the instance ID does not exist.

**Description**

The instance does not exist during card activation.

**Possible causes**

The input parameter instance does not exist.

**Solution**

Check the input parameter instance.

#### 1010220404 Instance Already Exists upon Card Activation

**Message**

Failed to add the card because the instance ID has been used.

**Description**

The instance already exists during card activation.

**Possible causes**

The input parameter instance already exists.

**Solution**

Check the input parameter instance.

#### 1010220501 No Card Found

**Message**

No card that meets the search criteria is found.

**Description**

No card was found.

**Possible causes**

No card was found.

**Solution**

Check the service ID in input parameters and the activation process in code.

#### 1010220701 No Card Update Information Found

**Message**

Failed to update the card because no update is detected.

**Description**

No update was found for the card.

**Possible causes**

No update was found for the card.

**Solution**

Check the card update process.

#### 1010220801 Failure to Delete the Card Due to a Certificate Verification Error

**Message**

Failed to delete the card because the signature verification failed.

**Description**

Failed to delete the card due to a certification verification error.

**Possible causes**

The certificate does not match the card to be deleted.

**Solution**

Check the card deletion process.

#### 1010221001 Failure to Obtain the Paring Code

**Message**

Connection failed because the pairing code is not obtained.

**Description**

Failed to obtain the pairing code during Bluetooth connection.

**Possible causes**

The Bluetooth link or protocol is abnormal.

**Solution**

Verify that the interface for obtaining the pairing code can respond normally.

#### 1010221101 Repeated Listener Registration

**Message**

Registration failed because of duplicate register name.

**Description**

The listener has already been registered.

**Possible causes**

A listener with the same name has already been registered.

**Solution**

Check the listener registration process.

#### 1010221201 Listener Already Unregistered

**Message**

The registration may have been unregistered before.

**Description**

The listener has already been unregistered.

**Possible causes**

The listener with the same name has already been unregistered.

**Solution**

Check the listener unregistration process.

#### 1010221301 Failure to Send a Car Control Message Due to Disconnection

**Message**

Failed to send the RKE message because of a connection failure.

**Description**

Failed to send a car control message due to Bluetooth disconnection.

**Possible causes**

Bluetooth is disconnected.

**Solution**

Check the Bluetooth connection process.

#### 1010221302 Failure to Send a Car Control Message Due to Authentication Failure

**Message**

Failed to send the RKE message because of an authentication failure.

**Description**

Failed to send a car control message due to Bluetooth authentication failure.

**Possible causes**

Bluetooth authentication failed.

**Solution**

1\. Obtain Bluetooth air interface information and check whether the authentication process is normal.

2\. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010210101 Invalid Card Status

**Message**

The card status is not correct.

**Description**

Failed to obtain card information due to invalid card status.

**Possible causes**

The card is not activated properly.

**Solution**

Call the **getCardMetadataInDevice** API to check whether the card exists and has been activated.

#### 1010210119 Failure to Read Card Data

**Message**

Failed to read the card data.

**Description**

Failed to read card data.

**Possible causes**

No card was found based on the input parameter.

**Solution**

Call the **getCardMetadataInDevice** API to check whether the card exists and has been activated.

#### 1010210201 Cannot Add Card Specified by issuerId for Specified Device

**Message**

The device does not support adding the card specified by issuerId.

**Description**

Failed to add the card specified by **issuerId** for the specified device.

**Possible causes**

Failed to add the card specified by **issuerId** for the specified device.

**Solution**

Verify that **issuerId** is set for the device on the management console.

#### 1010210202 Card Specified by IssuerId Already Exists on the Device

**Message**

A card conflicting with the specified card already exists in the device.

**Description**

The card specified by **IssuerId** has already been activated on the specified device.

**Possible causes**

The card specified by **IssuerId** has already been activated on the specified device.

**Solution**

Check whether the card has already been activated.

#### 1010210203 Card Specified by IssuerId Already Exists

**Message**

The specified card already exists.

**Description**

The card specified by **IssuerId** already exists.

**Possible causes**

The card specified by **IssuerId** already exists.

**Solution**

Check whether the card has already been activated.

#### 1010210204 Card Activation Service Temporarily Unavailable

**Message**

The card addition service is temporarily offline.

**Description**

The card activation service is temporarily unavailable.

**Possible causes**

The card activation service is temporarily unavailable.

**Solution**

Verify that the card activation service is enabled properly.

#### 1010210301 addCardToken Expired

**Message**

The card adding conditions are not met. The order can be refunded to end the card addition process.

**Description**

The **addCardToken** has expired.

**Possible causes**

The **addCardToken** has expired.

**Solution**

The token has expired. Call the API to apply for a new token.

#### 1010210302 Card Activation Order Confirmation Failure

**Message**

Failed to confirm the order. The order can be refunded to end the card addition process.

**Description**

Failed to confirm the order. The order can be refunded.

**Possible causes**

The **serverOrderId** passed is incorrect or in incorrect state, or the service provider server does not return correct data to the HUAWEI Wallet server.

**Solution**

Verify that the **serverOrderId** and its status are correct, and the service provider server has returned data as expected.

#### 1010210319 Card Activation Failure

**Message**

Failed to add the card.

**Description**

Failed to activate the card.

**Possible causes**

The chipset storage is insufficient, or card writing failed.

**Solution**

Verify that the card activation conditions are met.

#### 1010210401 Specified Card Does Not Exist

**Message**

The specified card does not exist.

**Description**

The specified card does not exist.

**Possible causes**

The specified card does not exist.

**Solution**

Check whether the card to be topped up has been deleted.

#### 1010210402 Card Specified by cardNumber Is in Abnormal State

**Message**

The status of the specified card is incorrect.

**Description**

The status of the card specified by **cardNumber** is abnormal.

**Possible causes**

The status of the card specified by **cardNumber** is abnormal.

**Solution**

Verify that the status of the card is normal.

#### 1010210403 Top-up Order Confirmation Failure

**Message**

Failed to confirm the order. The order can be refunded to end the recharging process.

**Description**

Failed to confirm the order. The order can be refunded.

**Possible causes**

The **serverOrderId** passed is incorrect or in incorrect state, or the service provider server does not return correct data to the HUAWEI Wallet server.

**Solution**

Verify that the **serverOrderId** and its status are correct, and the service provider server has returned data as expected.

#### 1010210419 Top-up Failure

**Message**

Failed to recharge the card.

**Description**

Top-up failed.

**Possible causes**

Top-up failed.

**Solution**

Check parameter settings.

#### 1010210501 Specified Card Does Not Exist

**Message**

The specified card does not exist.

**Description**

The specified card does not exist.

**Possible causes**

The card specified by **cardNumber** does not exist.

**Solution**

Verify that **cardNumber** is correct.

#### 1010210502 Card Specified by cardNumber Is in Abnormal State

**Message**

The status of the specified card is incorrect.

**Description**

The status of the card specified by **cardNumber** is abnormal.

**Possible causes**

The status of the card specified by **cardNumber** is abnormal.

**Solution**

Call the **updateTransitCard** API again.

#### 1010210503 Order Confirmation Failure

**Message**

Failed to confirm the order.

**Description**

Failed to confirm the order.

**Possible causes**

The **serverOrderId** passed is incorrect or in incorrect state, or the service provider server does not return correct data to the HUAWEI Wallet server.

**Solution**

Verify that the **serverOrderId** and its status are correct, and the service provider server has returned data as expected.

#### 1010210519 Card Update Failure

**Message**

Failed to update the card data.

**Description**

Failed to update the card.

**Possible causes**

Failed to update the card.

**Solution**

Call the **updateTransitCard** API again.

#### 1010210601 Order Confirmation Failure

**Message**

Failed to confirm the order.

**Description**

Failed to confirm the order.

**Possible causes**

The **serverOrderId** passed is incorrect or in incorrect state, or the service provider server does not return correct data to the HUAWEI Wallet server.

**Solution**

Verify that the **serverOrderId** and its status are correct, and the service provider server has returned data as expected.

#### 1010210619 Card Deletion Failure

**Message**

The card deleting failed.

**Description**

Failed to delete the card.

**Possible causes**

Failed to delete the card.

**Solution**

Call the **getCardMetadataInDevice** API to check whether the card exists and has been activated.

#### 1010210701 Token Verification Failure

**Message**

Failed to verify the caller token.

**Description**

Failed to verify the caller token.

**Possible causes**

The token passed is incorrect.

**Solution**

Verify that the token is correct.

#### 1010210702 Failure to Obtain Card Metadata

**Message**

Failed to get the metadata of the cards.

**Description**

Failed to obtain card metadata.

**Possible causes**

An internal error occurred in HUAWEI Wallet or the server is abnormal.

**Solution**

Call the API again.
