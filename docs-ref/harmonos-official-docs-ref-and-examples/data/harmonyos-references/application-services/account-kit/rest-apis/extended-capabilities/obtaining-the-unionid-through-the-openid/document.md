# Obtaining the UnionID Through the OpenID

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/SQa2M52dSC-Lib76pvfrZQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C4DBF458235103FDACE9D6969153B004269FE7AB88BB74B8412A0BABAB53B36)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is called by your app server from the Account Kit server to obtain the UnionID through the OpenID of a user.

#### Scenario

When developing HarmonyOS apps, you need to consider whether the data of the same user can be exchanged between non-HarmonyOS apps and HarmonyOS apps. If you used OpenID to associate user data within non-HarmonyOS apps before, it is recommended that you switch to UnionID to ensure that your users can inherit their data from earlier versions after using HarmonyOS apps.

#### Restrictions

-   Ensure that the network on the caller side is normal.
-   Using the OpenID of a user, an app can obtain only the UnionID within itself, rather than the UnionID of the user within any other app.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://oauth-login.cloud.huawei.com/rest.php?nsp_svc=huawei.oauth2.app.openIdToUnionId</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: text/plain;charset=utf-8</p></td></tr></tbody></table>

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

The request body parameters must comply with the request header format. Otherwise, the request may fail. For details about the parameters to pass, please refer to [Sample Code](#section15783195817216).

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

Access token obtained through the API for [Obtaining an App-Level Credential](../../api-call-credentials/obtaining-an-app-level-credential/document.md).

 |
| 

open\_id

 | 

Yes

 | 

String

 | 

OpenID of a user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |

#### Request Example

Send a POST request. Example:

POST /rest.php?nsp\_svc=huawei.oauth2.app.openIdToUnionId HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

open\_id=_<open\_id>_&access\_token=_<access\_token>_

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

Content type. The value is **text/plain;charset=utf-8**.

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

union\_id

 | 

Yes

 | 

String

 | 

UnionID of a user, which is generated after the user ID and app developer ID are concatenated and signed. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

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

Error code. For details, see [HTTP Response Codes](#section1737691991515).

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
Content-Type: text/plain;charset=utf-8

{"union\_id":"AQAxrB1HNA\*\*\*\*\*n-IfWRSUVq2M7xU"}

## Request Failure

HTTP/1.1 200 OK
Content-Type: text/plain;charset=utf-8
**NSP\_STATUS: 102**

{
    "error": "invalid session"
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
 \* Obtain the UnionID through the OpenID.
 \*/
@Slf4j
public class OpenIdToUnionIdDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining the UnionID through the OpenID.
        String url = "https://oauth-login.cloud.huawei.com/rest.php?nsp\_svc=huawei.oauth2.app.openIdToUnionId";
        // Replace it with the app-level access token you obtained.
        String accessToken = "_<Access Token>_";
        // Replace it with the OpenID you obtained.
        String openId = "_<OpenID>_";
        JSONObject result = openIdToUnionId(url, accessToken, openId);
        // Parse the result to obtain union\_id.
        String unionId = result.getString("union\_id");
    }

    private static JSONObject openIdToUnionId(String url, String accessToken, String openId) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("access\_token", accessToken));
        request.add(new BasicNameValuePair("open\_id", openId));
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/TnvHhzltR_yFJ9YyetJKyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B3FF35B3BB9A02621E87D717C42051234B607AF134E09916C311D3ABAA06539)

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

The **access\_token** parameter value is invalid. The possible cause is as follows: The value of **Content-Type** in the request header is **application/x-www-form-urlencoded**. However, the request body parameters are not converted through URL encoding during code running. For details, please refer to [Sample Code](#section15783195817216).

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
