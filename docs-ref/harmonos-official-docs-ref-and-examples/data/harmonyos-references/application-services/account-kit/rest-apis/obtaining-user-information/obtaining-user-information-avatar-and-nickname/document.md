# Obtaining User information: Avatar and Nickname

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/qdg5R5I7Seigop1HSqY3vg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3C179F0CDE1AB07A7E9458629ADBD3203B4044237500B59EB17893C6DC87126)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is called by your app server from the Account Kit server to obtain the avatar and nickname information and the UnionID/OpenID. For details, please refer to [Obtaining the Avatar and Nickname](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-avatar-nickname).

#### Scenario

After obtaining the access token through the authorization code, the app obtains the avatar and nickname information and the UnionID/OpenID.

#### Restrictions

-   Ensure that the network on the caller side is normal.
-   Before obtaining the nickname and avatar, your app must include the **profile** (nickname and avatar) scope in the request for the authorization code. For details, please refer to [Service Process](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-avatar-nickname#section11804191416341).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/dxYceCgeRmea0pWdbrjnHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E210AE10381B79EE03555DD23B512BB0C99BFB3572752AAC8E4D98788DC66C42)

If the app does not include the **profile** (nickname and avatar) scope when requesting the authorization code, the response will not contain the nickname and avatar after a successful call.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://account.cloud.huawei.com/rest.php?nsp_svc=GOpen.User.getInfo</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

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

The request body parameters must comply with the request header format. Otherwise, the request may fail. For details about the parameters to pass, please refer to [Sample Code](#section1888515151299).

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

access\_token

 | 

Yes

 | 

String

 | 

Access token obtained through the API for [Obtaining a User-Level Credential](../../api-call-credentials/obtaining-a-user-level-credential/document.md). Make sure the app carries the **profile** scope when requesting the authorization code.

 |
| 

getNickName

 | 

No

 | 

int

 | 

Type of the returned nickname. The default value is **0**.

-   **0**: The anonymized nickname is returned.
-   **1**: The nickname of the HUAWEI ID is returned. If no nickname exists, an anonymized nickname is returned.

 |

#### Request Example

Send a POST request. Example:

POST /rest.php?nsp\_svc=GOpen.User.getInfo HTTP/1.1
Host: account.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

access\_token=_<Access Token>_

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
**Parameter**

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

openID

 | 

Yes

 | 

String

 | 

OpenID of a user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

unionID

 | 

Yes

 | 

String

 | 

UnionID of a user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

displayName

 | 

No

 | 

String

 | 

Nickname of a user. For details about the return value, please refer to [Obtaining the Avatar and Nickname](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-avatar-nickname).

-   If **getNickName** is set to **0** or not passed, an anonymized nickname is returned.
-   If **getNickName** is set to **1**, the nickname is returned. If no nickname exists, an anonymized nickname is returned.
    
    NOTE:
    
    If the response does not contain the nickname field **displayName** after a successful call, check whether the obtained authorization code includes the **profile** (nickname and avatar) scope. For details, please refer to [App-Side Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-avatar-nickname#section154801110677).
    

 |
| 

displayNameFlag

 | 

No

 | 

int

 | 

Returned nickname type.

-   **0**: nickname
-   **1**: anonymized account
    
    NOTE:
    
    If the response does not contain the nickname type field **displayNameFlag** after a successful call, check whether the obtained authorization code includes the **profile** (nickname and avatar) scope. For details, please refer to [App-Side Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-avatar-nickname#section154801110677).
    

 |
| 

headPictureURL

 | 

No

 | 

String

 | 

Avatar of a user. For details about the return value, please refer to [Obtaining the Avatar and Nickname](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-avatar-nickname). If the user has not set an avatar, this parameter is not returned.

 |

If the API fails to be called, the response body is as follows.

| 
Parameter

 | 

Location

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

NSP\_STATUS

 | 

header

 | 

String

 | 

Error code. For details, see [HTTP Response Codes](#section15782984912).

 |
| 

error

 | 

body

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
    "displayName": "182\*\*\*\*\*\*74",
    "displayNameFlag": 1,
    "openID": "AQAxrBzThFv\*\*\*\*\*lv9tV\_4rMCc",
    "unionID": "AQAxrB1HNA\*\*\*\*\*n-IfWRSUVq2M7xU",
    "headPictureURL": "https://upfile-\*\*\*\*\*.jpg"
}

## Request Failure

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8
**NSP\_STATUS: 6**

{
    "error": "session timeout"
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
import java.util.Objects;

/\*\*
 \* Obtain user information, including the avatar and nickname.
 \*/
@Slf4j
public class GetUserAvatarAndNickNameDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining the avatar and nickname of a HUAWEI ID.
        String url = "https://account.cloud.huawei.com/rest.php?nsp\_svc=GOpen.User.getInfo";
        // Replace it with the user-level access token you obtained.
        String accessToken = "_<Access Token>_";
        JSONObject result = getUserAvatarAndNickName(url, accessToken, 1);
        // Parse the result to obtain openID.
        String openID = result.getString("openID");
        // Parse the result to obtain unionID.
        String unionID = result.getString("unionID");
        // Parse the result to obtain displayName.
        String displayName = result.getString("displayName");
        // Parse the result to obtain displayNameFlag.
        Integer displayNameFlag = result.getInteger("displayNameFlag");
        // Parse the result to obtain headPictureURL.
        String headPictureURL = result.getString("headPictureURL");
    }

    private static JSONObject getUserAvatarAndNickName(String url, String access\_token, Integer getNickName) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("access\_token", access\_token));
        request.add(new BasicNameValuePair("getNickName", Objects.isNull(getNickName) ? null : String.valueOf(getNickName)));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // Use the default exception handling logic. For custom exception handling, use the CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>) API.
        return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LZpaN2KOScKhV6EENJojNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32378BC7B18839841BAACEF343C048712BFA9304F30967A88630F136095B007E)

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
-   If the access token has not been URL-encoded, refer to the [sample code](#section1888515151299) for instructions on how to assemble the parameters.
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
