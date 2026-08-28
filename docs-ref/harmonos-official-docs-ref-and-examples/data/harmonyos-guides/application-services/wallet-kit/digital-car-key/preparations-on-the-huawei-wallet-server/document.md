# Preparations on the HUAWEI Wallet Server

#### Configuring Basic Integration Information on the HUAWEI Wallet Server

Set the parameters by following the instructions in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).

| 
Wallet Kit Service Parameter

 | 

Value

 |
| :-- | :-- |
| 

Service Type

 | 

Key

 |
| 

Service Project

 | 

ICCE car key

 |
| 

Service Name

 | 

Set it to **_xxx_ digital car key service**, where **_xxx_** can be a company name or product name. This field is used only for you to distinguish between multiple services.

 |
| 

Service ID

 | 

This parameter uniquely identifies an ICCE car key card issuer. The value is in hwpass.stdcarkey._xxx.xxx_ format, where _xxx_ can be a company name or product name containing up to 32 lowercase letters. HUAWEI Wallet can manage card issuers using this value. This value is carried in the request body for presetting a template, generating a key card, and enabling and activating a key.

 |
| 

Callback address

 | 

Address you provide for Wallet Kit to send a callback notification when a user successfully adds or deletes a pass. The value must start with **https**, for example: **https://_Your server address_/v1/passes/nfccallback**.

 |
| 

User public key

 | 

Generate a public key using the method provided in step 4 of [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md) and paste the generated public key here.

 |

| 
NFC Parameter

 | 

Value

 |
| :-- | :-- |
| 

Whether to support synchronization across mobile devices

 | 

YES

 |
| 

Whether to enable the NFC capability

 | 

YES

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/U4UCWGx9T5653IttzQdrOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19C2EF21BA5482B5B1833B67247829725BD0DE4D820EA378A69B1E7D420005DE)

Select **YES** for **Whether to enable the NFC capability** as long as Bluetooth is supported.

#### Configuring the Car Key Management Console Address on the HUAWEI Wallet Server

During the car key enabling, HUAWEI Wallet needs to request data from your server. The data transfer direction is as follows: HUAWEI Wallet app > HUAWEI Wallet server > DK management service.

The HUAWEI Wallet server needs to know the DK management service address before sending requests to the DK management service. Therefore, you need to configure the DK service management service address on the HUAWEI Wallet server.

"registrationsUrl": "Your server address/v1/passes/registrations",
"requestPersonalizeTokenUrl": "Your server address/v1/passes/requestPersonalizeToken",
"requestPersonalizeUrl": "Your server address/v1/passes/requestPersonalize",
"spNfcOperCallBackUrl": "Your server address/v1/passes/nfccallback"

#### UI Design

| 
Car Key List Element

 | 

Design Specifications

 |
| :-- | :-- |
| 

Logo

 | 

A square image of 64 x 64 dp.

 |
| 

Name

 | 

N/A

 |

| 
Car Key Details Element

 | 

Design Specifications

 |
| :-- | :-- |
| 

Logo

 | 

An image of 32 x 32 dp.

 |
| 

Name

 | 

N/A

 |
| 

Background image of the card

 | 

A square image of 328 x 205 dp.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/xpuXUMxuRuWxgxDFAwEuuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2364F27CC83DB77C8F4019FCBBD3DFE9E91791E921F1A737348A4D0A310711C1)

All images should have clean, sharp corners. Please avoid rounded corners and ensure there are no white borders in dark mode for a better user experience.
