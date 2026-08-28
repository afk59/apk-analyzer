# Refreshing a User-Level Credential

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/tY73uL2cThOT6MPcnNgn2w/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062501Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1156B36A2C75ECF7643E01C3F69894A1607A2BB31D0ABE758C92E83114EFAC37)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API allows the app server to obtain a new access token using a refresh token.

#### Scenario

The access token is about to expire or has expired, and you want to use the refresh token to obtain a new access token.

#### Restrictions

-   Ensure that the network on the caller side is normal.
-   The validity period of a refresh token is 180 days.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.6.2.1.3.1.1" valign="top" width="19.82%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.2.1" valign="top" width="19.82%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.3.1" valign="top" width="19.82%"><p>API URL</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>https://oauth-login.cloud.huawei.com/oauth2/v3/token</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.4.1" valign="top" width="19.82%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

#### Request Parameters

## Request Header

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

Content-Type

 | 

Yes

 | 

String

 | 

Content type. The value is **application/x-www-form-urlencoded**.

NOTE:

The request body parameters must comply with the request header format. Otherwise, the request may fail. For details about the parameters to pass, please refer to [Sample Code](#section14184218174113).

 |

## Request Body

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

grant\_type

 | 

Yes

 | 

String

 | 

Authorization mode. The value is always **refresh\_token**.

 |
| 

client\_id

 | 

Yes

 | 

String

 | 

Unique ID allocated by AppGallery Connect to a newly-created app. For details about the value, please refer to the **OAuth 2.0 client ID > Client ID** field in [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

NOTE:

The client ID used for obtaining a refresh token must be the same as the value of **client\_id**. Otherwise, an error (**sub\_error=20154**) will be triggered. If such an error occurs, find the appropriate client ID by referring to [Configuring the Client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

 |
| 

client\_secret

 | 

Yes

 | 

String

 | 

Client secret allocated by AppGallery Connect to a newly-created app. For details about the value, please refer to the **OAuth 2.0 client ID > Client Secret** field in [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

 |
| 

refresh\_token

 | 

Yes

 | 

String

 | 

Refresh token obtained by following the instructions in [Obtaining a User-Level Credential](../obtaining-a-user-level-credential/document.md), which is used to get a new access token.

 |
| 

scope

 | 

No

 | 

String

 | 

Used to obtain scopes in an access token. The value must be a subset of the **scope** value contained in the refresh token. Separate multiple scopes by spaces. A maximum of 150 scopes can be passed at a time.

-   If the **scope** parameter is not passed, the scope contained in the generated access token is the same as that in the refresh token.
-   If the **scope** parameter is passed, the scope contained in the generated access token is the intersection of the scope in the refresh token and the passed value of this parameter.

 |
| 

supportAlg

 | 

No

 | 

String

 | 

Algorithm for generating an ID token. Supported algorithms include the following:

-   PS256 (recommended)
-   RS256

If no algorithm is specified or the specified algorithm is not supported, RS256 is used by default.

 |

#### Request Example

POST /oauth2/v3/token HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

grant\_type=refresh\_token&client\_id=_<client\_id>_&client\_secret=_<client\_secret>_&refresh\_token=_<refresh\_token>_

#### Response Parameters

## Response Header

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

Content-Type

 | 

Yes

 | 

String

 | 

Content type. The value is **application/json;charset=utf-8**.

 |

## Response Body

If the API is successfully called, the response body is as follows.

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

token\_type

 | 

Yes

 | 

String

 | 

The value is always **Bearer**.

 |
| 

access\_token

 | 

Yes

 | 

String

 | 

Access token, which is a credential for accessing resources under permission control. For details about its length, please refer to [What are the length limits of access token and refresh token?](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-11).

 |
| 

scope

 | 

No

 | 

String

 | 

Scope contained in an access token. If no scope is contained, this parameter will not be returned. For details, see the description of the **scope** parameter in the **Request Body** table above.

 |
| 

expires\_in

 | 

Yes

 | 

Integer

 | 

Access token validity period, in seconds. It is valid for 3600 seconds.

 |
| 

id\_token

 | 

No

 | 

String

 | 

This parameter is returned in JWT format if the **scope** parameter in the response body contains **openid**. For details about the ID token, please refer to its description in [Verifying an ID Token](../../extended-capabilities/verifying-an-id-token/document.md).

 |

If the API fails to be called, the response body is as follows.

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

error

 | 

int

 | 

Error code. For details, please refer to [HTTP Response Codes](#section1394417423453).

 |
| 

sub\_error

 | 

int

 | 

Sub-error code. For details, please refer to [HTTP Response Codes](#section1394417423453).

 |
| 

error\_description

 | 

String

 | 

Error description.

 |

#### Response Example

## Request Success

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
	"access\_token": "DgEAAN7qd\*\*\*\*\*U0TvQ/eXpE4x+gvhoYh5/UuzL",
	"id\_token": "eyJraW\*\*\*\*\*ifQ.eyJhdF9oYX\*\*\*\*\*Q2fQ.TT05lFYe\*\*\*\*\*vDwb\_Gj1ccR59yyB2Ig",
	"expires\_in": 3600,
	"scope": "openid profile email",
	"token\_type": "Bearer"
}

## Request Failure

HTTP/1.1 400 Bad Request
Content-Type: application/json

{
	"sub\_error": 12304,
	"error\_description": "invalid client\_secret",
	"error": 1203
}

#### Sample Code

The Java sample code is as follows. Before running it, [configure the sample code environment](../../common-description/document.md#section444143185314). (Place this sample code and the **CallUtils** utility class in the same directory. If not, manually add the corresponding **import** statement to the sample code.)

import com.alibaba.fastjson2.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.message.BasicNameValuePair;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/\*\*
 \* Example of refreshing a user-level credential.
 \*/
@Slf4j
public class RefreshTokenAPIDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for refreshing a user-level credential
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
        // Authorization mode. The value is always refresh\_token.
        String grantType = "refresh\_token";
        // Replace it with the client ID of your app.
        String clientId = "_<Client ID>_";
        // Replace it with the client secret corresponding to the client ID of your app.
        String clientSecret = "_<Client Secret>_";
        // Replace it with the refresh token obtained based on the client ID of your app.
        String refreshToken = "_<Refresh Token>_";
        JSONObject result = refreshToken(url, refreshToken, clientSecret, clientId, grantType);
        // Parse the result to obtain scope.
        String scope = result.getString("scope");
        // Parse the result to obtain token\_type.
        String tokenType = result.getString("token\_type");
        // Parse the result to obtain access\_token.
        String accessToken = result.getString("access\_token");
        // Parse the result to obtain expires\_in.
        Integer expiresIn = result.getInteger("expires\_in");
        // Parse the result to obtain id\_token.
        String idToken = result.getString("id\_token");
    }

    private static JSONObject refreshToken(String url, String refreshToken, String clientSecret,
                                           String clientId, String grantType) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("client\_secret", clientSecret));
        request.add(new BasicNameValuePair("refresh\_token", refreshToken));
        request.add(new BasicNameValuePair("client\_id", clientId));
        request.add(new BasicNameValuePair("grant\_type", grantType));
        request.add(new BasicNameValuePair("supportAlg", "PS256"));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // For custom exception handling, use api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>).
        return CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpPost));
    }
}

#### HTTP Response Codes

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

The **scope** parameter contains a forged value. Pass a valid parameter according to the parameter specifications.

 |
| 

20154

 | 

The value of **client\_id** in **refresh\_token** is different from that of the input parameter **client\_id**.

 | 

Ensure that the value of **client\_id** is the same as the [configured value](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

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

-   **authorization\_code**: It is used to [obtain a user-level credential](../obtaining-a-user-level-credential/document.md).
-   **refresh\_token**: It is used to [refresh a user-level credential](#).
-   **client\_credentials**: It is used to [obtain an app-level credential](../obtaining-an-app-level-credential/document.md).

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

20181

 | 

The **grant\_type** parameter is left empty.

 | 

The options of **grant\_type** are as follows:

-   **authorization\_code**: It is used to [obtain a user-level credential](../obtaining-a-user-level-credential/document.md).
-   **refresh\_token**: It is used to [refresh a user-level credential](#).
-   **client\_credentials**: It is used to [obtain an app-level credential](../obtaining-an-app-level-credential/document.md).

 |
| 

20191

 | 

The **refresh\_token** parameter is left empty.

 | 

Pass a valid **refresh\_token** according to the parameter specifications.

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

Internal system error. Record the error code and [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>).

 |
