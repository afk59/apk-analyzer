# REST API Result Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/mbs3-GofSiutHhkUIi7l2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C096575ABD803048844066D20194BC9C0A2C07B59E62ABC7876076371B2751AF)

If the error persists, go to [Submit ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/), select the relevant topic, and submit your ticket. Huawei will get back to you as soon as possible.

| 
Value

 | 

MSG

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- | :-- |
| 

0

 | 

IAP\_RESPONSE\_RESULT\_OK

 | 

Success.

 | 

N/A

 |
| 

1001880005

 | 

IAP\_APP\_IAP\_NOT\_ACTIVATED

 | 

The IAP service is not enabled.

 | 

Enable the IAP service for your app in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/).

 |
| 

1001880006

 | 

IAP\_RESPONSE\_RESULT\_ERROR

 | 

A critical error occurs during API operations.

 | 

Fix the error based on the error information in the response.

 |
| 

1001880008

 | 

IAP\_RESPONSE\_RESULT\_ITEM\_NOT\_OWNED

 | 

Acknowledging the delivery failed because the user does not own the product.

 | 

Make sure that acknowledging the delivery is performed after a successful purchase. Then, you also need to ensure that the input parameters in the API call request are correct.

 |
| 

1001880009

 | 

IAP\_RESPONSE\_RESULT\_ITEM\_CONSUMED\_OR\_ACKNED

 | 

Acknowledging the delivery is already complete for a consumable or non-renewable subscription, and no more delivery acknowledgement is allowed. A non-consumable can be purchased only once and delivered only once.

 | 

Check why repeated API calls occur and further optimize the project logic. If process check and suggestions are required, contact Huawei technical support.

 |
| 

1001880010

 | 

IAP\_RESPONSE\_RESULT\_HIGHTRISK

 | 

The operation is rejected because the user account has a high risk.

 | 

Use another account or register a new account if no other account is available.

 |
| 

1001880011

 | 

IAP\_USER\_ACCOUNT\_INVALID

 | 

The user account is abnormal, for example, the account has been deregistered.

 | 

Use another account or register a new account if no other account is available.

 |
| 

1001880012

 | 

IAP\_RECORD\_NOT\_EXIST

 | 

The order does not exist. Only the latest order of a product can be queried. The order in this query may be a historical order.

 | 

Token verification is unnecessary for a historical order under normal circumstances, and IAP Kit only allows for token verification for the latest order of a product. Check your integration process to make sure it complies with that described in the development guide.

 |
| 

1001880020

 | 

IAP\_RESPONSE\_RESULT\_REPEAT\_SHIP\_CONFIRM

 | 

Acknowledging the delivery is already complete for an auto-renewable subscription, and no more delivery acknowledgement is allowed.

 | 

Check why repeated API calls occur and further optimize the project logic. If process check and suggestions are required, contact Huawei technical support.

 |
