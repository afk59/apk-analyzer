# Overview

The transportation card service in Wallet Kit provides the open capabilities for activating, topping up, updating, and deleting transportation cards. To implement these functions, your app needs to complete the following since transportation cards are issued by transportation card companies:

1.  Connect to payment service providers (such as Huawei Pay, WeChat Pay, Alipay, and UnionPay) to complete order payment for card activation and top up.
2.  Obtain the approval from transportation card companies and connect your server to their systems to apply for services corresponding to the preceding functions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/-yOazm_uSLWClRcACu9bLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BDB0AE3D1ACEFC4AF8A79E0716B1AD4AF8B80EBB0671271013A56A1D71C9A51)

The open capabilities of the transportation card service are available only to **invited apps**.

#### Overall Architecture

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/RAr_5rybRc-ydS2wdBTceQ/en-us_image_0000002378575673.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=704F0480F41B44EB03DA06A8C4E85DEB8000B9BB99759B4D4C4BA1109441A26E "Click to enlarge")

-   **Roles**:

**Your app**: your client app, which implements UX experience such as card activation, card information display, and card top-up, update, and deletion.

**Your server**: your service server, which processes card activation, top-up, and management requests from your client app, and delivers the corresponding tasks to the SP TSM system of the transportation card company. In addition, your server needs to connect to payment service providers to complete order payment for card activation and top-up.

**Payment service provider**: completes order payment.

**SP TSM**: TSM system of a transportation card company, which generates commands for adding, topping up, and managing cards.

**Wallet app**: implements Wallet Kit APIs. It delivers the SP TSM commands for adding, topping up, and managing cards to the data security chipset.

**Wallet server**: connects to the SP TSM system to obtain the commands for adding, topping up, and managing cards.

-   **API description**

| 
API

 | 

Call Direction

 | 

Description

 |
| :-- | :-- | :-- |
| 

IF1

 | 

Your app ->

Wallet app

 | 

Wallet Kit APIs, including the card status and information query API, card activation condition check API, card activation API, top-up API, card update API, and card deletion API.

 |
| 

IF2

 | 

Your app -> Your server

 | 

Initiates card activation, top-up, update, and deletion requests to your service server.

 |
| 

IF3

 | 

Your server -> Payment service provider

 | 

Completes order payment for card activation and top-up.

 |
| 

IF4

 | 

Your server -> SP TSM

 | 

Submits card activation, top-up, update, and deletion requests to the SP TSM system of a transportation card company.

 |
| 

IF5

 | 

Wallet server -> SP TSM

 | 

Obtains service requests for card activation, top-up, update, and deletion and the commands for implementing these service functions from the SP TSM system of a transportation card company.

 |
