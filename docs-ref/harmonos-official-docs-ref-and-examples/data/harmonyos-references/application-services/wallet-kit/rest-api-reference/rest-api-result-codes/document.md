# REST API Result Codes

| 
Result Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Success.

 | 

\-

 |
| 

400

 | 

Invalid parameter.

 | 

Check whether the input parameters are correct based on the returned information and ensure that the JDK version of the organization server is later than 1.8.211. If no error is found, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

401

 | 

Authentication failed.

 | 

Obtain the **Authorization** parameter again and add it to the request header.

 |
| 

404

 | 

Incorrect URL.

 | 

Check whether the URL is correct.

 |
| 

405

 | 

Incorrect permissions.

 | 

Ensure that Wallet Kit is enabled in AppGallery Connect. For details. please refer to [Applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations). In addition,verify that the requested service ID, which is specified by **passTypeIdentifier**, matches the called API. If no error is found, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

429

 | 

Service unavailable.

 | 

The number of API calls has reached the upper limit. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
