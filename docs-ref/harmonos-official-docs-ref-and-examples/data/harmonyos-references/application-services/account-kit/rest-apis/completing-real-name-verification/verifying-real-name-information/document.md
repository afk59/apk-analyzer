# Verifying Real-Name Information

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/vMv2aX7pQG6BlWhUp6WB1A/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B56CF0456CA0D1B39D00089180DDECDFDD87DB914E48E927B3552215BD42F3E7)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ud8ySqn3RDCalzgTxVXvKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE686EF760054C59EC49202750AE9E4873EB6B9A084E544DE222DD3892A390DE)

This API is temporarily unavailable.

#### Function

This API is called by your app server to the Account Kit server to verify whether the real-name information provided by the user is consistent with that associated with the HUAWEI ID.

#### Scenario

After obtaining an access token using the authorization code and requested the required scope, the app verifies the real-name information provided by the user against the real-name information associated with their HUAWEI ID, and retrieves the verification result.

#### Restrictions

This API is temporarily unavailable.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.6.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://openrealname.cloud.huawei.com/rest.php?nsp_svc=OpenRealName.User.verifyRealName</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

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

Access token obtained through the API for [Obtaining a User-Level Credential](../../api-call-credentials/obtaining-a-user-level-credential/document.md).

NOTE:

In this scenario, the access token can be used only once. If the access token is used for a second time, the error message "access forbidden" is returned.

 |
| 

sceneID

 | 

Yes

 | 

Integer

 | 

Scenario.

-   **0**: Use the real-name information about a HUAWEI ID to verify a user's name, ID type, and ID card number.
-   **1**: Use the real-name information about a HUAWEI ID to verify a user's name, ID type, ID card number, and face.
-   **2**: Use the real-name information about a HUAWEI ID to verify the face.

 |
| 

idType

 | 

Yes

 | 

Integer

 | 

Enumeration object of ID types.

-   **1**: UserID
-   **2**: OpenID
-   **3**: UnionID

 |
| 

idValue

 | 

Yes

 | 

String

 | 

ID value, for example, UnionID and OpenID of a user. The value type is defined by **idType**.

 |
| 

ctfType

 | 

No

 | 

Integer

 | 

ID type.

-   1: ID card (This parameter needs to be passed when **sceneID** is set to **0** or **1**.)

 |
| 

realName

 | 

No

 | 

String

 | 

Real name to be verified. The name must be hashed using the SHA-512 algorithm, and is mandatory when **sceneID** is set to **0** or **1**.

 |
| 

ctfCode

 | 

No

 | 

String

 | 

ID card number to be verified. If the number ends with x, convert it to uppercase X for verification. The number must be hashed using the SHA-512 algorithm, and is mandatory when **sceneID** is set to **0** or **1**.

 |
| 

supportAlg

 | 

Yes

 | 

String

 | 

Signing algorithm type of the returned **verifyToken**.

-   RS256
-   PS256
-   ES256

 |

#### Request Example

Send a POST request. Example:

POST /rest.php?nsp\_svc=OpenRealName.User.verifyRealName HTTP/1.1
Host: openrealname.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

access\_token=_<access\_token>_&sceneID=1&ctfType=1&realName=_<realName>_&ctfCode=_<ctfCode>_&idType=2&idValue=_<idValue>_&supportAlg=RS256

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

state

 | 

Yes

 | 

Integer

 | 

Real-name verification status. The options are as follows:

-   **0**: not verified
-   **1**: verified
-   **2**: being verified

 |
| 

realNameLevel

 | 

No

 | 

Integer

 | 

Level of real-name verification.

-   **0**: Identity not verified.
-   **10**: Information submitted but not yet verified by an authoritative source.

-   **20**: Identity verified via the submitted name and ID number.
-   **30**: Identity verified via the submitted ID photo.
-   **35**: Identity verified via the linked bank card.
-   **40**: Identity verified via facial recognition.

 |
| 

verifyResult

 | 

No

 | 

Integer

 | 

Consistency check result.

-   **0**: Information is consistent.
-   **1**: Names are inconsistent.
-   **2**: The name does not match the ID card number.

 |
| 

verifyToken

 | 

No

 | 

String

 | 

Token returned after the verification is successful. The value is in JWT format.

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
    "state": 1,
    "verifyResult": 0,
    "realNameLevel": 20,
    "verifyToken": "eyJraWQ\*\*\*\*Aad-dw"
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
import javax.xml.bind.annotation.adapters.HexBinaryAdapter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/\*\*
 \* Verify real-name information.
 \*/
@Slf4j
public class VerifyRealNameDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for verifying real-name information.
        String url = "https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.verifyRealName";
        // Replace it with the access token you obtained.
        String accessToken = "_<Access Token>_";
        // Replace it with the real name to be verified.
        String realName = "_<realName>_";
        // Replace it with the ID card number to be verified.
        String ctfCode = "_<ctfCode>_";
        JSONObject result = verifyRealName(url, accessToken, realName, ctfCode);
        // Parse the result to obtain state.
        Integer state = result.getInteger("state");
        // Parse the result to obtain realNameLevel.
        Integer realNameLevel = result.getInteger("realNameLevel");
        // Parse the result to obtain verifyResult.
        Integer verifyResult = result.getInteger("verifyResult");
        // Parse the result to obtain verifyToken.
        String verifyToken = result.getString("verifyToken");
    }

    private static JSONObject verifyRealName (String url, String accessToken, String realName, String ctfCode) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("access\_token", accessToken));
        // Adjust the value of sceneID based on the actual situation.
        request.add(new BasicNameValuePair("sceneID", "_<sceneID>_"));
        // Adjust the value of idType based on the actual situation.
        request.add(new BasicNameValuePair("idType", "_<idType>_"));
        // Adjust the value of idValue based on the actual situation.
        request.add(new BasicNameValuePair("idValue", "_<idValue>_"));
        // Adjust the value of ctfType based on the actual situation.
        request.add(new BasicNameValuePair("ctfType", "_<ctfType>_"));
        request.add(new BasicNameValuePair("realName", encryptBySHA512(<realName>)));
        request.add(new BasicNameValuePair("ctfCode", encryptBySHA512(ctfCode.toLowerCase(Locale.US))));
        // Adjust the value of supportAlg based on the actual situation.
        request.add(new BasicNameValuePair("supportAlg", "_PS256_"));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // Use the default exception handling logic. For custom exception handling, use the CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>) API.
        return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
    }
    private static String encryptBySHA512(String str) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-512");
            return new HexBinaryAdapter().marshal(md.digest(str.getBytes(StandardCharsets.UTF\_8)))
                .toLowerCase(Locale.US);
        } catch (NoSuchAlgorithmException e) {
            log.error("no such alg", e);
        }
        return null;
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/6VSVC0FGT1Camsj4UbDvQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC69AE4663890EB54FE639C1AFF752FAF1660707A7AC90A4282BBD16B3D32418)

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

-   For access tokens that have not been URL-encoded, refer to the [sample code](#section1888515151299) for instructions on how to assemble the parameters.

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

Go to [Restrictions](#section74906714178) to check related restrictions.

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
