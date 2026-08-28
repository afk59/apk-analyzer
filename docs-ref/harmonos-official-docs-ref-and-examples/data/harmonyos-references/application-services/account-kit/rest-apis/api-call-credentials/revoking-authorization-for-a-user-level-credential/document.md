# Revoking Authorization for a User-Level Credential

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/lD8GUJ7NR0aeyQaJiIqaFw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062501Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55211BC201A1A6DED81A67120EB42796331F402A3E53831681BB60E83B678392)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API allows the app to revoke the authorization for the obtained user-level access token or refresh token. The access token and refresh token are in a pair. If the authorization of one token is revoked, the authorization of the other token also becomes invalid.

#### Scenario

When your app no longer needs to use the obtained user-level access token or refresh token, it calls this API to revoke the authorization.

#### Restrictions

Ensure that the network on the caller side is normal.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="19.82%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="19.82%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="19.82%"><p>API URL</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>https://oauth-login.cloud.huawei.com/oauth2/v3/revoke</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="19.82%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80.17999999999999%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

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

token

 | 

Yes

 | 

String

 | 

Access token (user-level credential) or refresh token (credential used to obtain a new access token).

 |

#### Request Example

POST /oauth2/v3/revoke HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

token=_<token>_

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

Content type. The value is **application/json**.

 |

## Response Body

If the API is successfully called, an empty JSON object will be returned.

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
Content-Type: application/json

{}

## Request Failure

HTTP/1.1 400 Bad Request
Content-Type: application/json

{
	"sub\_error": 31204,
	"error\_description": "token revoked",
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
 \* Revoke authorization for a user-level credential.
 \*/
@Slf4j
public class RevokeTokenAPIDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for revoking the authorization of a user-level credential.
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/revoke";
        // Access token (user-level credential) or refresh token (credential used to obtain a new access token).
        String token = "_<Access Token or Refresh Token>_";
        JSONObject result = revokeToken(url, token);
    }

    private static JSONObject revokeToken(String url, String token) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("token", token));
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

20222

 | 

Invalid token.

 | 

The token format is incorrect. The possible cause is as follows:

The value of **Content-Type** in the request header is **application/x-www-form-urlencoded**. However, the request body parameters are not converted through URL encoding during code running. For details, please refer to [Sample Code](#section14184218174113).

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

Internal system error. Record the error code and [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>).

 |
