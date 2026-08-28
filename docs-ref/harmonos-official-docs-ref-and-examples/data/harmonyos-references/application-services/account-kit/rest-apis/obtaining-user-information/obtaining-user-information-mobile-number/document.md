# Obtaining User Information: Mobile Number

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/unTfJDG3SE2XB-aosnuTeg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5C3955A5358694ADB919B487856D383B92AAADF62E9FAA76207CEB584484214)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is called by your app server from the Account Kit server to obtain the UnionID, OpenID, mobile number authorized by the user, and other related information. For details, please refer to [Obtaining the Mobile Number](https://developer.huawei.com/consumer/en/doc/atomic-guides/account-guide-atomic-get-phone).

#### Scenario

Your app has obtained an access token using the authorization code, and needs to obtain the UnionID, OpenID, mobile number authorized by the user, and other related information. This function is usually used for atomic services and games.

#### Restrictions

-   Ensure that the network on the caller side is normal.
-   Before obtaining the mobile number, the app needs to request the **phone** scope (scope for obtaining the mobile number) and pass this scope when requesting an authorization code. For details, please refer to the [service process](https://developer.huawei.com/consumer/en/doc/atomic-guides/account-guide-atomic-get-phonenumber#section168761120115).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/6Y5kBp_OT1uM8xjF8kZYKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11056E6DAF9A47E5BA15C7C9B9DBDA684570B86525867C69F1795F9239010250)

If your app has not requested the **phone** scope (required for obtaining the mobile number) or does not pass the **phone** scope when requesting an authorization code, the response will not contain the mobile number after the relevant API is successfully called.

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

Access token obtained through the API for [Obtaining a User-Level Credential](../../api-call-credentials/obtaining-a-user-level-credential/document.md). Make sure your app passes the **profile** scope when requesting an authorization code.

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

mobileNumber

 | 

No

 | 

String

 | 

Mobile number authorized by a user to your app, either the mobile number bound to the HUAWEI ID or selected by the user. For details, please refer to [Obtaining the Mobile Number](https://developer.huawei.com/consumer/en/doc/atomic-guides/account-guide-atomic-get-phone).

**mobileNumber** is not returned in the following scenarios:

-   The user has not bound a mobile number.
-   The mobile number authorized by the user is unassociated from the HUAWEI ID.
-   The app does not have the **phone** scope.
-   The **phone** scope is not passed in the request to obtain an authorization code.

 |
| 

purePhoneNumber

 | 

No

 | 

String

 | 

Mobile number without an international call prefix and country/region code.

If **mobileNumber** is not returned, this parameter is not returned.

 |
| 

phoneCountryCode

 | 

No

 | 

String

 | 

International call prefix (**00**) and country/region code of **purePhoneNumber**.

If **mobileNumber** is not returned, this parameter is not returned.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/kevPx49HTWi5IxpDCQDOxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5087E5CF532769A7033C66EC84E4E1FE6EE19F16E1F6C6EF2CD69F22D4703F17)

Unless otherwise specified, the mobile number returned by the Account Kit server is in the following format:

-   If the HUAWEI ID is registered in the Chinese mainland and bound to a Chinese mainland mobile number, the mobile number is returned without the international call prefix and country/region code, for example, **11136000008**.
-   In other cases, the format shall follow: international call prefix (fixed as **00**) + country/region code + mobile number, for example, **0085261234567** (Hong Kong, China) and **0079871234560** (Russia).

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

-   For HUAWEI IDs registered in the Chinese mainland and bound to a Chinese mainland mobile number:

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "openID": "AQAxrBzThFv\*\*\*\*\*lv9tV\_4rMCc",
    "unionID": "AQAxrB1HNA\*\*\*\*\*n-IfWRSUVq2M7xU",
    // Mobile number authorized by the user, in plaintext format.
    "mobileNumber": "191\*\*\*\*\*\*08",
    // Mobile number excluding the international call prefix and country/region code, in plaintext format.
    "purePhoneNumber": "191\*\*\*\*\*\*08",
    "phoneCountryCode": "0086"
}

-   For other cases:

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "openID": "AQAxrBzThFv\*\*\*\*\*lv9tV\_4rMCc",
    "unionID": "AQAxrB1HNA\*\*\*\*\*n-IfWRSUVq2M7xU",
    // Mobile number authorized by the user, in plaintext format.
    "mobileNumber": "00790\*\*\*\*\*\*43",
    // Mobile number excluding the international call prefix and country/region code, in plaintext format.
    "purePhoneNumber": "90\*\*\*\*\*\*43",
    "phoneCountryCode": "007"
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

/\*\*
 \* Obtain user information, that is, the mobile number.
 \*/
@Slf4j
public class GetUserMobileDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining the mobile number bound to the HUAWEI ID.
        String url = "https://account.cloud.huawei.com/rest.php?nsp\_svc=GOpen.User.getInfo";
        // Replace it with the user-level access token you obtained.
        String accessToken = "_<Access Token>_";
        JSONObject result = getInfo(url, accessToken);
        // Parse the result to obtain openID.
        String openID = result.getString("openID");
        // Parse the result to obtain unionID.
        String unionID = result.getString("unionID");
        // Parse the result to obtain mobileNumber.
        String mobileNumber = result.getString("mobileNumber");
        // Parse the result to obtain purePhoneNumber.
        String purePhoneNumber = result.getString("purePhoneNumber");
        // Parse the result to obtain phoneCountryCode.
        String phoneCountryCode = result.getString("phoneCountryCode");
    }

    private static JSONObject getInfo(String url, String accessToken) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("access\_token", accessToken));
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/fTem4qhBRoqmHB-2wTJnDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8D670B8D3A588F8249A0FA94702952185173BCF12D8B6E2FA138368E908F8F2)

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

Change the parameter value according to the _API Reference_.

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
