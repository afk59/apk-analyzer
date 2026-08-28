# Obtaining the JWT Public Key for ID Token Verification

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/BdMjpEGHRVin-3WCACaLhg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA20AC748AE0209D076B75BF2E45892DCB5EB159328F6ABB4D2DA75F0D77BDFA)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is used to obtain the JWT public key required for parsing and verifying the ID token. This API returns the JWT public keys of the current day and the previous day. The app server can compare the value of **kid** in the ID token with the **kid** returned by this API to obtain the corresponding public keys.

#### Scenario

After obtaining the ID token, your app needs to parse it to obtain user data and verify the signature.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/eDew37HZQ9Ow5GcBZfs6yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=775CBE142FF48BDA120B81389E2D10EBB67D9FE6C9B350CEB7A23B36AA81DA28)

-   The JWT public key is updated at 00:00 every day.
-   The JWT public keys of PS256 and RS256 are the same. For details about how to use the JWT public key to parse and verify the ID token, please refer to [Parsing and Verification on the Server](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-12#section1684141911591).

#### Restrictions

Ensure that the network on the caller side is normal.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST/GET</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://oauth-login.cloud.huawei.com/oauth2/v3/certs</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

#### Request Parameters

None

#### Request Example

Send a POST request. Example:

POST /oauth2/v3/certs HTTP/1.1
Host: oauth-login.cloud.huawei.com

Send a GET request. Example:

GET /oauth2/v3/certs HTTP/1.1
Host: oauth-login.cloud.huawei.com

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

keys

 | 

Yes

 | 

JSONArray

 | 

Array of JWT public keys.

 |

Below lists the parameters contained in each element in the **keys** array.

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

kty

 | 

Yes

 | 

String

 | 

JWK type. The value is always **RSA**.

 |
| 

e

 | 

Yes

 | 

String

 | 

Value of **e** in the RSA algorithm.

 |
| 

use

 | 

Yes

 | 

String

 | 

Intended use of the key.

**sig**: signature.

 |
| 

kid

 | 

Yes

 | 

String

 | 

Unique JWK ID.

 |
| 

alg

 | 

Yes

 | 

String

 | 

Algorithm type. The value is fixed at **RS256**.

 |
| 

n

 | 

Yes

 | 

String

 | 

Value of **n** in the RSA algorithm.

 |

#### Response Example

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
  "keys": \[
    {
      "kty": "RSA",
      "e": "AQAB",
      "use": "sig",
      "kid": "046fad4b211a9cbfbdc75debb4044901e029ba857c9d84f26f2839ba8aad22e8",
      "alg": "RS256",
      "n": "h\_6JivtuClNwkUxMg\*\*\*\*\*\*ZJKo239SANnkAfIgU6ECY5fxEZdIMBf7RJigO\*\*\*\*\*\*uMuK064QfT0Dw"
    },
    {
      "kty": "RSA",
      "e": "AQAB",
      "use": "sig",
      "kid": "65f642e667650cc0db5bad81c6781c1f20b00c0ec977e89aaca964e9beafd5d2",
      "alg": "RS256",
      "n": "m8-SeDRLSd-Y02u\*\*\*\*\*\*BbxzizQfSkEDLRjvksb74S2Bw2qQ82Er58\*\*\*\*\*\*yoc0j2yujCRZTpiF9-w"
    }
  \]
}

#### Sample Code

The Java sample code is as follows. Before running it, [configure the sample code environment](../../common-description/document.md#section444143185314). (Place this sample code and the **CallUtils** utility class in the same directory. If not, manually add the corresponding **import** statement to the sample code.)

import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.apache.http.client.methods.HttpGet;
import java.io.IOException;

/\*\*
 \* Obtain the JWT public key for ID token verification.
 \*/
@Slf4j
public class GetIdTokenCerts {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining the JWT public key used to verify the ID token.
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/certs";
        JSONObject result = CallUtils.toJsonObject(CallUtils.remoteCallOAuth(new HttpGet(url)));
        // Parse relevant fields to obtain keys in the response.
        JSONArray keys = result.getJSONArray("keys");
        for (Object keyInfo : keys) {
            // Obtain the field information in each element in keys.
            JSONObject jsonObj = (JSONObject) keyInfo;
            // Parse the JSON object to obtain kty.
            String kty = jsonObj.getString("kty");
            // Parse the JSON object to obtain e.
            String e = jsonObj.getString("e");
            // Parse the JSON object to obtain use.
            String use = jsonObj.getString("use");
            // Parse the JSON object to obtain kid.
            String kid = jsonObj.getString("kid");
            // Parse the JSON object to obtain alg.
            String alg = jsonObj.getString("alg");
            // Parse the JSON object to obtain n.
            String n = jsonObj.getString("n");
        }
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
