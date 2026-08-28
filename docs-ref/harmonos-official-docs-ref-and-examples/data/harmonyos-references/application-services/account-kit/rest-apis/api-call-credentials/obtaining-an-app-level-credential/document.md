# Obtaining an App-Level Credential

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/WaxogxUITiOcGMUl7Worig/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062501Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55BB5278AFA0D5A4AC924E3453CFD714195D5F657266BDD541F668AE06EA4F72)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is used by an app server to obtain an app-level access token.

#### Scenario

This API is used to obtain an app-level credential and access resources controlled by app-level permissions with the credential. For example, [obtain a UnionID through an OpenID](../../extended-capabilities/obtaining-the-unionid-through-the-openid/document.md).

#### Restrictions

-   Ensure that the network on the caller side is normal.
-   The validity period of an app-level access token is 3600 seconds. To avoid unnecessary network overhead, your app server should reuse the access token within the validity period. The frequency limit for a single client ID to obtain app-level access tokens is 1000 times per 5 minutes. Exceeding this limit may trigger rate limiting and cause request failure.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="19.82%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="19.82%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="19.82%"><p>API URL</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>https://oauth-login.cloud.huawei.com/oauth2/v3/token</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="19.82%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

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

Authorization mode. The value is always **client\_credentials**.

 |
| 

client\_id

 | 

Yes

 | 

String

 | 

Unique ID allocated by AppGallery Connect to a newly-created app. For details about the value, please refer to the **OAuth 2.0 client ID > Client ID** field in [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

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

#### Request Example

POST /oauth2/v3/token HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

grant\_type=client\_credentials&client\_id=_<client\_id>_&client\_secret=_<client\_secret>_

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

expires\_in

 | 

Yes

 | 

Integer

 | 

Access token validity period, in seconds. It is valid for 3600 seconds.

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
	"expires\_in": 3600,
	"token\_type": "Bearer"
}

## Request Failure

HTTP/1.1 400 Bad Request
Content-Type: application/json

{
	"sub\_error": 12304,
	"error\_description": "invalid client\_secret",
	"error": 1101
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
 \* Obtain an app-level credential.
 \*/
@Slf4j
public class AppTokenAPIDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining an app-level credential.
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
        // Authorization mode. The value is always **client\_credentials**.
        String grantType = "client\_credentials";
        // Replace it with the client ID of your app.
        String clientId = "_<Client ID>_";
        // Replace it with the client secret corresponding to the client ID of your app.
        String clientSecret = "_<Client Secret>_";
        JSONObject result = getAppToken(url, clientSecret, clientId, grantType);
        // Parse the result to obtain access\_token.
        String accessToken = result.getString("access\_token");
        // Parse the result to obtain token\_type.
        String tokenType = result.getString("token\_type");
        // Parse the result to obtain expires\_in.
        Integer expiresIn = result.getInteger("expires\_in");
    }

    private static JSONObject getAppToken(String url, String clientSecret,
                                          String clientId, String grantType) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("client\_secret", clientSecret));
        request.add(new BasicNameValuePair("client\_id", clientId));
        request.add(new BasicNameValuePair("grant\_type", grantType));
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
-   **refresh\_token**: It is used to [refresh a user-level credential](../refreshing-a-user-level-credential/document.md).
-   **client\_credentials**: It is used to [obtain an app-level credential](#).

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
-   **refresh\_token**: It is used to [refresh a user-level credential](../refreshing-a-user-level-credential/document.md).
-   **client\_credentials**: It is used to [obtain an app-level credential](#).

 |
| 

1203

 | 

12303

 | 

The value of **client\_id** does not exist.

 | 

Verify that the configured client ID (**client\_id**) exists in AppGallery Connect.

 |
| 

500

 | 

Internal system error.

 | 

Internal system error. Record the error code and [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>).

 |
