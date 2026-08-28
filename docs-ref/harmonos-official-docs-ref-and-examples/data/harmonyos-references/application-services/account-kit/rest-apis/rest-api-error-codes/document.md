# REST API Error Codes

#### Obtaining a User-Level Credential/Refreshing a User-Level Credential/Obtaining an App-Level Credential

API URL: https://oauth-login.cloud.huawei.com/oauth2/v3/token

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Successful.

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Further locate the fault based on the relevant **error code** and **sub-error code**.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

| 
Error Code

 | 

Sub-error Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- | :-- |
| 

1101

 | 

12304

 | 

The value of **client\_secret** is incorrect.

 | 

Verify **client\_secret** in AppGallery Connect.

 |
| 

20002

 | 

The value of **client\_id** is in an incorrect format.

 | 

Ensure that the value of **client\_id** meets the regular expression ^\[0-9\]{1,64}$.

 |
| 

20003

 | 

The value of **client\_id** is in an invalid format or it could not be found in the system.

 | 

-   Ensure that the value of **client\_id** meets the regular expression ^\[0-9\]{1,64}$.
-   Verify that the configured client ID (**client\_id**) exists in AppGallery Connect.

 |
| 

20041

 | 

The scope format is incorrect, or the number of scopes exceeds 150.

 | 

-   Ensure that the scope parameter meets the regular expression ^\[0-9a-zA-Z:/\\\\.\\u0020\]+$.
-   Ensure that the number of scopes does not exceed 150.

 |
| 

20042

 | 

Invalid scope.

 | 

-   The passed scope is not contained in the scopes passed to the API for obtaining a refresh token.
-   The passed scope is a forged value.

 |
| 

20085

 | 

The **client\_secret** parameter is left empty.

 | 

Pass a valid value for the **client\_secret** parameter according to the parameter specifications.

 |
| 

20152

 | 

The value of **code** is in an incorrect format.

 | 

Ensure that the value format of **code** meets the regular expression ^\[0-9a-zA-Z=/\\\\+\]+$.

This error code is returned in the following scenarios:

-   The **code** parameter is tampered with. As a result, the value format is incorrect.

-   **Content-Type** in the request header is **application/x-www-form-urlencoded**. However, the request body is not converted through URL encoding during code running. For details, please refer to [Sample Code](../api-call-credentials/obtaining-a-user-level-credential/document.md#section14184218174113).

 |
| 

20154

 | 

The value of **client\_id** in **code** or **refresh\_token** is different from that of the input parameter **client\_id**.

 | 

Ensure that the value of **client\_id** is the same as the [configured value](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

 |
| 

20155

 | 

The code has expired. Its validity period is 5 minutes.

 | 

Obtain a new code.

 |
| 

20156

 | 

The code has been used.

 | 

The code can be used only once. Obtain a new code and try again.

 |
| 

20158

 | 

The authorization code has expired.

 | 

Obtain the code again and retry. (Possible cause: the user canceled the authorization.)

 |
| 

20171

 | 

The **client\_secret** parameter is left empty.

 | 

Pass a valid value for the **client\_secret** parameter according to the parameter specifications.

 |
| 

20172

 | 

The value of **client\_secret** is in an incorrect format.

 | 

Ensure that the value format of **client\_secret** meets the regular expression ^\[0-9a-zA-Z=/\\\\+\]+$.

 |
| 

20182

 | 

The **grant\_type** parameter has an incorrect value.

 | 

The options of **grant\_type** are as follows:

-   **authorization\_code**: It is used to [obtain a user-level credential](../api-call-credentials/obtaining-a-user-level-credential/document.md).
-   **refresh\_token**: It is used to [refresh a user-level credential](../api-call-credentials/refreshing-a-user-level-credential/document.md).
-   **client\_credentials**: It is used to [obtain an app-level credential](../api-call-credentials/obtaining-an-app-level-credential/document.md).

 |
| 

20192

 | 

The value of **refresh\_token** is in an incorrect format.

 | 

Ensure that the value format of **refresh\_token** meets the regular expression ^\[0-9a-zA-Z=/\\\\+\]+$.

 |
| 

1102

 | 

20001

 | 

The **client\_id** parameter is left empty.

 | 

Pass a valid value for the **client\_id** parameter according to the parameter specifications.

 |
| 

20151

 | 

The **code** parameter is left empty.

 | 

Pass a valid value for the **code** parameter according to the parameter specifications.

 |
| 

20181

 | 

The **grant\_type** parameter is left empty.

 | 

The options of **grant\_type** are as follows:

-   **authorization\_code**: It is used to [obtain a user-level credential](../api-call-credentials/obtaining-a-user-level-credential/document.md).
-   **refresh\_token**: It is used to [refresh a user-level credential](../api-call-credentials/refreshing-a-user-level-credential/document.md).
-   **client\_credentials**: It is used to [obtain an app-level credential](../api-call-credentials/obtaining-an-app-level-credential/document.md).

 |
| 

20191

 | 

The **refresh\_token** parameter is left empty.

 | 

Pass a valid **refresh\_token** according to the parameter specifications.

 |
| 

1103

 | 

20153

 | 

Invalid code.

 | 

Ensure that the code is correct.

 |
| 

1203

 | 

11205

 | 

The refresh token has expired.

 | 

Obtain a new refresh token.

 |
| 

12303

 | 

The value of **client\_id** does not exist.

 | 

Verify that the configured client ID (**client\_id**) exists in AppGallery Connect.

 |
| 

12304

 | 

Invalid client secret.

 | 

Make sure that **client\_id** and **client\_secret** match.

 |
| 

31202

 | 

Failed to parse the token.

 | 

Make sure that the **token** parameter is valid.

 |
| 

31204

 | 

The token has expired.

 | 

Obtain a new refresh token.

 |
| 

31218

 | 

Invalid token.

 | 

Ensure that the token format meets the regular expression ^\[0-9a-zA-Z=\\/\\+\]+$.

 |
| 

500

 | 

Internal system error.

 | 

Internal system error. Record the error code and [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

100300

 | 

The system processing is abnormal.

 | 

Try again. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Parsing a Credential

API URL: https://oauth-api.cloud.huawei.com/rest.php?nsp\_fmt=JSON&nsp\_svc=huawei.oauth2.user.getTokenInfo

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The API call is successful. The actual service processing result is indicated by **NSP\_STATUS** in **Response Header**.

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Check whether the request parameters comply with the specifications.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/m3nYuRDNRbqOqHRRA1Ldsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6004413C8FF0BA5539E482DE3E98C94BE16E34677CE75B78B9382DE37101EB8B)

The **NSP\_STATUS** parameter in **Response Header** will not be returned after being successfully processed.

| 
NSP\_STATUS

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

6

 | 

The access token has expired.

 | 

Obtain a new access token.

 |
| 

102

 | 

Invalid access token.

 | 

The **access\_token** parameter value is invalid. The possible cause is as follows: The value of **Content-Type** in the request header is **application/x-www-form-urlencoded**. However, the request body parameters are not converted through URL encoding during code running. For details, please refer to [Sample Code](../api-call-credentials/parsing-a-credential/document.md#section1571132717539).

 |
| 

500

 | 

Internal API error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

501

 | 

Service distribution exception.

 | 

-   Ensure that **nsp\_svc** in the request URL is correct.
-   If the request URL complies with the specifications, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

31204

 | 

Invalid access token.

 | 

Obtain a new access token.

 |

#### Revoking Authorization for a User-Level Credential

API URL: https://oauth-login.cloud.huawei.com/oauth2/v3/revoke

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Successful.

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Further locate the fault based on the relevant **error code** and **sub-error code**.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

| 
Error Code

 | 

Sub-error Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- | :-- |
| 

1101

 | 

20222

 | 

Invalid token.

 | 

The token format is incorrect. The possible cause is as follows:

The value of **Content-Type** in the request header is **application/x-www-form-urlencoded**. However, the request body parameters are not converted through URL encoding during code running. For details, please refer to [Sample Code](../api-call-credentials/revoking-authorization-for-a-user-level-credential/document.md#section14184218174113).

 |
| 

1102

 | 

20221

 | 

The **token** parameter is left empty.

 | 

Pass a valid value for the **token** parameter according to the parameter specifications.

 |
| 

1203

 | 

11205

 | 

The token has expired.

 | 

Obtain a new token and try again.

 |
| 

17009

 | 

Invalid token.

 | 

The passed token is invalid. Obtain a new token.

 |
| 

17010

 | 

Failed to verify the token.

 | 

Make sure that the **token** parameter is valid.

 |
| 

31202

 | 

Failed to parse the token.

 | 

Make sure that the **token** parameter is valid.

 |
| 

31204

 | 

The token has expired.

 | 

Obtain a new token and try again.

 |
| 

31218

 | 

The token is in an invalid format.

 | 

Ensure that the credential format meets the requirement.

 |
| 

500

 | 

Internal system error.

 | 

Internal system error. Record the error code and [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Obtaining User Information

API URL: https://account.cloud.huawei.com/rest.php?nsp\_svc=GOpen.User.getInfo

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The current API call is successful. (A successful API call does not mean successful service processing. For example, if the **NSP\_STATUS** field is returned in the response header, it indicates an error occurred during service processing, and you need to identify the root cause of the error.)

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Check whether the request parameters comply with the specifications.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/nlNf_pOvSOef7WHimsmGDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B04F40B40850739B8335530CE1B8AAE2EC9AA3546C876F5048D35A6180D6D5F9)

The **NSP\_STATUS** parameter in **Response Header** will not be returned after being successfully processed.

| 
NSP\_STATUS

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

6

 | 

Session invalidation (**session timeout**).

Possible causes:

-   The access token is invalid or has expired.
-   The access token format is incorrect.
-   Other internal causes.

 | 

-   Check whether the passed parameters are correct. If yes, try to obtain a new access token.
-   If the access token has not been URL-encoded, refer to the [sample code](../obtaining-user-information/obtaining-user-information-avatar-and-nickname/document.md#section1888515151299) for instructions on how to assemble the parameters.
-   Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

105

 | 

Incorrect parameter.

 | 

Modify the value according to the _API Reference_.

 |
| 

403

 | 

No access permission.

 | 

Go to AppGallery Connect to request scopes for your app. For details, please refer to [Requesting Scopes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-config-permissions).

 |
| 

500

 | 

Internal API error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Try again later.

 |
| 

70001201

 | 

Invalid parameter.

 | 

Modify the value according to the _API Reference_.

 |
| 

70001402

 | 

System authentication error.

 | 

The authentication system is abnormal. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

70020002

 | 

Internal network error.

 | 

The internal network is abnormal. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

70001401

 | 

Internal system error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Obtaining the UnionID/OpenID and Mobile Number Bound to a HUAWEI ID with One-Tap Sign-In

API URL: https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The API call is successful. The actual service processing result is indicated by **resultCode** in **Response Body**.

 | 

\-

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

| 
Error Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

60010002

 | 

Invalid parameter.

 | 

Check the input parameters according to the error description and the parameter description in [Request Body](../obtaining-user-information/obtaining-the-unionid-openid-and-mobile-number-bound-to-a-huawei-id-with-one-tap/document.md#section118656231362).

 |
| 

60010012

 | 

The value of the **code** parameter is incorrect.

 | 

The value of the **code** parameter is incorrect. The possible cause is that the value of **code** is invalid or is tampered with.

 |
| 

60010013

 | 

The value of the **clientSecret** parameter is incorrect.

 | 

The value of the **clientSecret** parameter is incorrect. For details about the value, please refer to the **OAuth 2.0 client ID > Client Secret** field in [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

 |
| 

60180003

 | 

The value of **client\_id** in **code** is different from that of the input parameter **client\_id**.

 | 

The value of **clientId** in **code** is different from that of the input parameter **clientId**. Ensure that the value of **client\_id** is the same as that specified in [Configuring the Client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

 |
| 

60180004

 | 

The code has expired. Its validity period is 5 minutes.

 | 

Obtain a new code.

 |
| 

60180005

 | 

The code has been used.

 | 

The code can be used only once. Obtain a new code and try again.

 |
| 

60180006

 | 

The authorization code has expired.

 | 

Obtain the code again and retry. (Possible cause: the user canceled the authorization.)

 |
| 

60180007

 | 

The authorization code does not have permission for HUAWEI ID one-tap sign-in.

 | 

Check the following causes:

-   Your app has not requested the one-tap HUAWEI ID sign-in scope before calling the corresponding capability. For details, please refer to [Requesting Scopes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-config-permissions).

-   The authorization code parameter is not obtained via **QuickLoginButtonComponent**. To address this, refer to the instructions on [showing the screen for one-tap sign-in with a HUAWEI ID and obtaining an authorization code](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-phone-unionid-login#li8130114016451).

 |
| 

60180008

 | 

No mobile number bound.

 | 

Check whether a mobile number is bound to the user's HUAWEI ID. If not, show the sign-in screen that contains other sign-in options.

 |
| 

60180009

 | 

The mobile number cannot be obtained.

 | 

-   The one-tap HUAWEI ID sign-in function is available only to users in the Chinese mainland.
-   When your app server requests the mobile number bound to a HUAWEI ID, make sure it is deployed in the Chinese mainland.

 |
| 

60010001

 | 

Internal system error.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Obtaining the Risk Level

API URL: https://account.cloud.huawei.com/user/getuserrisklevel

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The current API call is successful. (A successful API call does not mean successful service processing. The actual service processing result must be determined via **errCode** in **Response Body**.)

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Check whether the request parameters comply with the specifications.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

415

 | 

The media type is not supported.

 | 

Ensure that the content type (**contentType**) for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

| 
errCode

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

6

 | 

Session invalidation (**session timeout**).

Possible causes:

-   The access token is invalid or has expired.
-   The access token format is incorrect.
-   Other internal causes.

 | 

-   Check whether the passed parameters are correct. If yes, try to obtain a new access token.
-   The request data format of this API is **application/json;charset=utf-8**. When constructing a request body, ensure that the URL encoding is not performed on the **access\_token** parameter. For details on parameter assembly, please refer to [Sample Code](../obtaining-user-information/obtaining-the-risk-level/document.md#section1888515151299).
-   Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

403

 | 

No access permission.

 | 

Go to AppGallery Connect to request scopes for your app. For details, please refer to [Requesting Scopes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-config-permissions).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Try again later.

 |
| 

70001201

 | 

Invalid request parameter.

 | 

Modify the parameters in the request URL or request body.

 |
| 

70001402

 | 

System authentication error.

 | 

The authentication system is abnormal. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

70020002

 | 

Internal API request timeout.

 | 

Try again later.

 |
| 

70001401

 | 

Internal API error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Obtaining Real-Name Information

API URL: https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.getDetailInfo

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The API call is successful. The actual service processing result is indicated by **NSP\_STATUS** in **Response Header**.

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Check whether the request parameters comply with the specifications.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/N-FCzHF2SWiy-eFTOz0yJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00E7FEDD83DECDDA42156673DB1F87808DB12CE9D02E01F9B5016F5810C3E78A)

The **NSP\_STATUS** parameter in **Response Header** will not be returned after being successfully processed.

| 
NSP\_STATUS

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

6

 | 

Session invalidation (**session timeout**).

Possible causes:

-   The access token is invalid or has expired.
-   The access token format is incorrect.

 | 

-   For invalid or expired access tokens, check whether the passed parameters are correct. If yes, try to obtain a new access token.

-   For access tokens that have not been URL-encoded, refer to the [sample code](../completing-real-name-verification/obtaining-real-name-information/document.md#section1888515151299) for instructions on how to assemble the parameters.

 |
| 

105

 | 

Incorrect value of **nsp\_svc** in the request URL.

 | 

Ensure that the value of **nsp\_svc** in the request URL is correct.

 |
| 

403

 | 

No access permission.

 | 

Go to [Restrictions](../completing-real-name-verification/obtaining-real-name-information/document.md#section74906714178) to check related restrictions.

 |
| 

500

 | 

Internal API error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

API rate limiting triggered.

 | 

Too many API calling requests. Try again later.

 |
| 

70001201

 | 

Invalid request parameter.

 | 

Locate the error cause based on the error description, rectify the error, and try again.

 |
| 

70001401

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

70009019

 | 

The real-name information does not exist.

 | 

Guide users to complete real-name authentication or use a real-name verified account. If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Verifying Real-Name Information

API URL: https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.verifyRealName

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The API call is successful. The actual service processing result is indicated by **NSP\_STATUS** in **Response Header**.

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Check whether the request parameters comply with the specifications.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/yuRGSEMrTPC3Y6gSlWqPlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16ABC26D0EE9C72A638572DA99C4ABE2AA3266EC5785B6FEECA309BEEE3D4B86)

The **NSP\_STATUS** parameter in **Response Header** will not be returned after being successfully processed.

| 
NSP\_STATUS

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

6

 | 

Session invalidation (**session timeout**).

Possible causes:

-   The access token is invalid or has expired.
-   The access token format is incorrect.

 | 

-   For invalid or expired access tokens, check whether the passed parameters are correct. If yes, try to obtain a new access token.

-   For access tokens that have not been URL-encoded, refer to the [sample code](../completing-real-name-verification/verifying-real-name-information/document.md#section1888515151299) for instructions on how to assemble the parameters.

 |
| 

105

 | 

Incorrect value of **nsp\_svc** in the request URL.

 | 

Ensure that the value of **nsp\_svc** in the request URL is correct.

 |
| 

403

 | 

No access permission.

 | 

Go to [Restrictions](../completing-real-name-verification/verifying-real-name-information/document.md#section74906714178) to check related restrictions.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

500

 | 

Internal API error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

API rate limiting triggered.

 | 

Too many API calling requests. Try again later.

 |
| 

70001201

 | 

Invalid request parameter.

 | 

Locate the error cause based on the error description, rectify the error, and try again.

 |
| 

70001401

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

70009019

 | 

The real-name information does not exist.

 | 

Guide users to complete real-name authentication or use a real-name verified account. If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Obtaining the UnionID Through the OpenID

API URL: https://oauth-login.cloud.huawei.com/rest.php?nsp\_svc=huawei.oauth2.app.openIdToUnionId

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

The API call is successful. The actual service processing result is indicated by **NSP\_STATUS** in **Response Header**.

 |    |
| 

400

 | 

Incorrect parameter.

 | 

Check whether the request parameters comply with the specifications.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/q7sT5fMmS_G7QyzLRWUc9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35733AD67996E221A00EEA8471BEA50A65A7ECE2DAB59175E7869CACB071A187)

The **NSP\_STATUS** parameter in **Response Header** will not be returned after being successfully processed.

| 
NSP\_STATUS

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

6

 | 

The access token has expired.

 | 

Obtain a new access token.

 |
| 

102

 | 

Invalid access token.

 | 

The **access\_token** parameter value is invalid. The possible cause is as follows: The value of **Content-Type** in the request header is **application/x-www-form-urlencoded**. However, the request body parameters are not converted through URL encoding during code running. For details, please refer to [Sample Code](../extended-capabilities/obtaining-the-unionid-through-the-openid/document.md#section15783195817216).

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

500

 | 

Internal API error.

 | 

Rectify the error based on the returned error description. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

501

 | 

Service distribution exception.

 | 

-   Ensure that **nsp\_svc** in the request URL is correct.
-   If the request URL complies with the specifications, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

1302

 | 

API rate limiting triggered.

 | 

The call frequency is too high. Keep the concurrent calls per app below 100 TPS.

 |
| 

31204

 | 

Invalid access token.

 | 

Obtain a new access token.

 |
| 

150028

 | 

The value of **open\_id** is empty or too long.

 | 

Ensure that the value of **open\_id** is not empty and does not exceed 256 characters. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |

#### Obtaining OpenID Connect Public Configurations

API URL: https://oauth-login.cloud.huawei.com/.well-known/openid-configuration

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Successful.

 | 

\-

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

#### Obtaining the JWT Public Key for ID Token Verification

API URL: https://oauth-login.cloud.huawei.com/oauth2/v3/certs

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Successful.

 | 

\-

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

#### Verifying an ID Token

API URL: https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo

Message:

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Successful.

 | 

\-

 |
| 

400

 | 

Incorrect parameter.

 | 

Further locate the fault based on the relevant **error code** and **sub-error code**.

 |
| 

403

 | 

No access permission.

 | 

Check the network environment configuration to see if the access is blocked by the caller's network security policy. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

405

 | 

Unsupported HTTP request method.

 | 

Ensure that the method for the HTTP request complies with the API specifications.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

Connection error. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

System rate limiting triggered.

 | 

Rate limiting has been triggered by the system. Please retry later.

 |
| 

504

 | 

Connection timed out. This typically occurs when network connectivity is unstable.

 | 

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

590

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |

| 
Error Code

 | 

Sub-error Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- | :-- |
| 

1203

 | 

100305

 | 

Failed to parse the header in the ID token.

 | 

The ID token format is incorrect or its value is forged. Ensure that the ID token is in the JWT format and correct.

 |
| 

100306

 | 

Failed to parse the payload in the ID token.

 | 

The ID token format is incorrect or its value is forged. Ensure that the ID token is in the JWT format and correct.

 |
| 

150021

 | 

Failed to parse the ID token.

 | 

The ID token format is incorrect or its value is forged. Ensure that the ID token is in the JWT format and correct.

 |
| 

150023

 | 

Failed to parse the signature of the ID token.

 | 

The ID token format is incorrect or its value is forged. Ensure that the ID token is in the JWT format and correct.

 |
| 

500

 | 

Internal system error.

 | 

Internal system error. Record the error code and [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

1400

 | 

14004

 | 

The JWT public key is not found based on the value of **kid**.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

1500

 | 

15003

 | 

Invalid ID token.

 | 

The ID token format is incorrect or its value is forged. Ensure that the ID token is in the JWT format and correct.

 |
| 

15004

 | 

Failed to verify the ID token.

 | 

Ensure that the public key and algorithm used for verification are correct.

 |
| 

15005

 | 

Failed to verify the issuer of the ID token.

 | 

Ensure that the ID token is not tampered with.

 |
| 

15006

 | 

The ID token has expired.

 | 

Obtain a new ID token.

 |
| 

15007

 | 

The **id\_token** parameter is left empty.

 | 

Pass a valid value for the **id\_token** parameter according to the parameter specifications.

 |
| 

15008

 | 

The ID token format is incorrect.

 | 

Ensure that the value format of **id\_token** meets the regular expression ^\[0-9a-zA-Z\_\\-\\.\]+$.

 |
