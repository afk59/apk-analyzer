# Obtaining OpenID Connect Public Configurations

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Skn0Vj1yT3Kz8BsWUS85KA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2077046085E8B4C276B71682088B619AB66E968CA36EA124A148BEC8E40658A)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is used to obtain OpenID Connect public configurations.

#### Scenario

Your app calls this API to obtain public configuration information about the OAuth2 service, such as authorization, token obtaining, authorization revoking, JWT public key, and other access address information.

#### Restrictions

Ensure that the network on the caller side is normal.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST/GET</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://oauth-login.cloud.huawei.com/.well-known/openid-configuration</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

#### Request Parameters

None

#### Request Example

Send a POST request. Example:

POST /.well-known/openid-configuration HTTP/1.1
Host: oauth-login.cloud.huawei.com

Send a GET request. Example:

GET /.well-known/openid-configuration HTTP/1.1
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

Content type. The value is **application/json**.

 |

## Response Body

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

issuer

 | 

Yes

 | 

String

 | 

Issuer.

 |
| 

authorization\_endpoint

 | 

Yes

 | 

String

 | 

Authorization access address.

 |
| 

token\_endpoint

 | 

Yes

 | 

String

 | 

Access address for obtaining tokens.

 |
| 

revocation\_endpoint

 | 

Yes

 | 

String

 | 

Access address for authorization revoking.

 |
| 

jwks\_uri

 | 

Yes

 | 

String

 | 

Access address for obtaining the JWT public key information.

 |
| 

response\_modes\_supported

 | 

Yes

 | 

String\[\]

 | 

Supported response modes for identity verification.

The value is always **\["form\_post"\]**, indicating that the authorization code is returned via HTTP GET/POST form submission.

 |
| 

response\_types\_supported

 | 

Yes

 | 

String\[\]

 | 

Supported authorization type. The value is always **\["code"\]**, indicating that the authorization code mode is supported.

 |
| 

subject\_types\_supported

 | 

Yes

 | 

String\[\]

 | 

Supported subject type.

The value is always **\["pairwise"\]**, indicating that the OpenID provider (OP) will assign a distinct **sub** value to each relying party (RP), thereby protecting user uniqueness across different RPs.

 |
| 

id\_token\_signing\_alg\_values\_supported

 | 

Yes

 | 

String\[\]

 | 

Algorithm supported by the ID token signature.

-   RS256
-   PS256

 |
| 

scopes\_supported

 | 

Yes

 | 

String\[\]

 | 

Supported scopes. The following scopes are supported:

-   openid
-   email
-   profile

 |
| 

token\_endpoint\_auth\_methods\_supported

 | 

Yes

 | 

String\[\]

 | 

List of client identity authentication methods when calling the token access address.

The value is always **\["client\_secret\_post"\]**, indicating that the client ID and client secret are passed to the authorization server as form fields using the HTTP POST method.

 |
| 

claims\_supported

 | 

Yes

 | 

String\[\]

 | 

Supported claims.

-   **aud**: client ID
-   **email**: user email
-   **email\_verified**: indicates whether the email address has been verified
-   **exp**: time when the ID token expires
-   **family\_name**: family name of the user
-   **given\_name**: given name of the user (excluding the family name)
-   **iat**: time when the ID token is issued
-   **iss**: issuer of the ID token
-   **locale**: preferred language and region of the user
-   **name**: full name of the user
-   **picture**: URL of the user's avatar
-   **sub**: unique user ID (UnionID)
-   **display\_name**: user nickname

 |
| 

code\_challenge\_methods\_supported

 | 

Yes

 | 

String\[\]

 | 

Method of encoding **code\_verifier** in PKCE authorization. The value is always **\["S256"\]**, indicating that the SHA-256 algorithm is used for encoding.

 |

#### Response Example

HTTP/1.1 200 OK
Content-Type: application/json

{ 
   "issuer": "https://accounts.huawei.com", 
   "authorization\_endpoint": "https://oauth-login.cloud.huawei.com/oauth2/v3/authorize", 
   "token\_endpoint": "https://oauth-login.cloud.huawei.com/oauth2/v3/token", 
   "revocation\_endpoint": "https://oauth-login.cloud.huawei.com/oauth2/v3/revoke", 
   "jwks\_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/certs", 
   "response\_modes\_supported": \[ 
      "form\_post" 
   \], 
   "response\_types\_supported": \[ 
      "code" 
   \], 
   "subject\_types\_supported": \[ 
      "pairwise" 
   \], 
   "id\_token\_signing\_alg\_values\_supported": \[ 
      "RS256", 
      "PS256" 
   \], 
   "scopes\_supported": \[ 
      "openid", 
      "email", 
      "profile" 
   \], 
   "token\_endpoint\_auth\_methods\_supported": \[
      "client\_secret\_post" 
   \], 
   "claims\_supported": \[ 
       "aud", 
       "email", 
       "email\_verified", 
       "exp", 
       "family\_name", 
       "given\_name", 
       "iat", 
       "iss", 
       "locale", 
       "name", 
       "picture", 
       "sub", 
       "display\_name"
    \], 
    "code\_challenge\_methods\_supported": \[ 
        "S256" 
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
 \* Obtain OpenID Connect public configurations.
 \*/
@Slf4j
public class GetOpenIdConnect {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining public configuration information about OpenID Connect.
        String url = "https://oauth-login.cloud.huawei.com/.well-known/openid-configuration";
        HttpGet httpGet = new HttpGet(url);
        JSONObject result = CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpGet));
        // Parse the result to obtain issuer.
        String issuer = result.getString("issuer");
        // Parse the result to obtain authorization\_endpoint.
        String authorizationEndpoint = result.getString("authorization\_endpoint");
        // Parse the result to obtain token\_endpoint.
        String tokenEndpoint = result.getString("token\_endpoint");
        // Parse the result to obtain revocation\_endpoint.
        String revocationEndpoint = result.getString("revocation\_endpoint");
        // Parse the result to obtain jwks\_uri.
        String jwksUri = result.getString("jwks\_uri");
        // Parse the result to obtain response\_modes\_supported.
        JSONArray responseModesSupported = result.getJSONArray("response\_modes\_supported");
        // Parse the result to obtain response\_types\_supported.
        JSONArray responseTypesSupported = result.getJSONArray("response\_types\_supported");
        // Parse the result to obtain subject\_types\_supported.
        JSONArray subjectTypesSupported = result.getJSONArray("subject\_types\_supported");
        // Parse the result to obtain id\_token\_signing\_alg\_values\_supported.
        JSONArray idTokenSigningAlgValuesSupported = result.getJSONArray("id\_token\_signing\_alg\_values\_supported");
        // Parse the result to obtain scopes\_supported.
        JSONArray scopesSupported = result.getJSONArray("scopes\_supported");
        // Parse the result to obtain token\_endpoint\_auth\_methods\_supported.
        JSONArray tokenEndpointAuthMethodsSupported = result.getJSONArray("token\_endpoint\_auth\_methods\_supported");
        // Parse the result to obtain claims\_supported.
        JSONArray claimsSupported = result.getJSONArray("claims\_supported");
        // Parse the result to obtain code\_challenge\_methods\_supported.
        JSONArray codeChallengeMethodsSupported = result.getJSONArray("code\_challenge\_methods\_supported");
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
