# (Optional) Setting Necessary Parameters

#### Configuring the Address for Receiving Order/Subscription Notifications

The IAP server can send [key event notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-key-event-notifications) to your app server. After a user makes a purchase, the IAP server will send a notification to the specified address in the case of a key order (consumable/non-consumable purchase) or subscription event. For details about how to set the address, please refer to [Activating the In-App Purchases Service and Configuring Event Notifications](https://developer.huawei.com/consumer/en/doc/app/parameters-0000001931995692).

#### Configuring the Key

The IAP server requires JSON Web Token (JWT) authorization for each server API request. You can use the API key downloaded from [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) to sign the token and generate a JWT to authorize the server-side API request.

Perform relevant operations by referring to [key creation](https://developer.huawei.com/consumer/en/doc/app/key-0000001959074877), [key download](https://developer.huawei.com/consumer/en/doc/app/download-0000001958955101), and [key revocation](https://developer.huawei.com/consumer/en/doc/app/cancel-0000001931995696).
