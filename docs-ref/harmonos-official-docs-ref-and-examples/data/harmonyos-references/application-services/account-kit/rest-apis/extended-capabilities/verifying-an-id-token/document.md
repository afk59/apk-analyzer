# Verifying an ID Token

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/mN3NFKPbR2-Pu3-UCEYT5A/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF7003FCFE877AD16161148006E560EBE493DEA8874B5CF27458E3F5B6910DA3)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

#### Function

This API is used by the app server from the Account Kit server to verify an ID token and parse the ID token. It is used for debugging only.

#### Scenario

-   Your app uses an ID token to request authorization for HUAWEI ID sign-in. Before parsing the ID token, you need to verify its validity. If local verification fails, your app can call this API to send a verification request to the Account Kit server.
-   ID tokens obtained by calling the API for [obtaining a user-level credential](../../api-call-credentials/obtaining-a-user-level-credential/document.md) do not need to be verified.

#### Restrictions

-   Ensure that the network on the caller side is normal.
-   Given the long response time and sensitivity to network conditions, this API is intended for debugging purposes only. For commercial environments, local verification should be used. For details, please refer to [Parsing and Verification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-12#section6924154019588).

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="20.49%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="79.51%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="20.49%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="79.51%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="20.49%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="79.51%"><p>https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="20.49%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="79.51%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

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

The request body parameters must comply with the request header format. Otherwise, the request may fail. For details about the parameters to pass, please refer to [Sample Code](#section1635104211466).

 |

## Request Body

| 
**Parameter**

 | 

Mandatory

 | 

**Type**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

id\_token

 | 

Yes

 | 

String

 | 

ID token obtained by an app.

 |

#### Request Example

Send a POST request. Example:

POST /oauth2/v3/tokeninfo HTTP/1.1
Host:oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

id\_token=_<id\_token>_

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

typ

 | 

Yes

 | 

String

 | 

ID token format. The value is always **JWT**.

 |
| 

alg

 | 

Yes

 | 

String

 | 

ID token signing algorithm.

-   PS256
-   RS256

 |
| 

kid

 | 

Yes

 | 

String

 | 

ID of the public-private key pair used for signature verification. The value contains a maximum of 256 characters.

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

Error code. For details, please refer to [HTTP Response Codes](#section1186915200438).

 |
| 

sub\_error

 | 

int

 | 

Sub-error code. For details, please refer to [HTTP Response Codes](#section1186915200438).

 |
| 

error\_description

 | 

String

 | 

Error description.

 |

#### ID Token Parsing

Some parameters are returned only when certain scopes are passed for ID token generation. Check the tables below for the relationships between parameters and scopes.

If the **openid** scope is passed in the request, parameters in the following table are returned.

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

iss

 | 

Yes

 | 

String

 | 

The value is always **https://accounts.huawei.com**.

 |
| 

sub

 | 

Yes

 | 

String

 | 

UnionID of a user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

aud

 | 

Yes

 | 

String

 | 

Client ID of the app that receives an ID token.

 |
| 

exp

 | 

Yes

 | 

Long

 | 

Time when an ID token expires (10 digits).

 |
| 

iat

 | 

Yes

 | 

Long

 | 

Time when an ID token is generated (10 digits).

 |
| 

at\_hash

 | 

Yes

 | 

String

 | 

Access token hash value.

 |
| 

azp

 | 

Yes

 | 

String

 | 

Client ID of the app that generates an ID token.

 |
| 

openid

 | 

Yes

 | 

String

 | 

OpenID of a user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

nonce

 | 

No

 | 

String

 | 

Random value for replay attack prevention. For details, please refer to the description of the **nonce** field in [LoginWithHuaweiIDRequest](../../../arkts-api/authentication-unified-authentication-service/document.md#section42261825935) and [AuthorizationWithHuaweiIDRequest](../../../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165).

 |

If the **profile** scope is passed in the request, parameters in the following table are returned.

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

picture

 | 

No

 | 

String

 | 

User avatar URL.

 |
| 

display\_name

 | 

No

 | 

String

 | 

Nickname of a HUAWEI ID. If this parameter is not set, the anonymized email address or mobile number is displayed.

 |
| 

nickname

 | 

No

 | 

String

 | 

Nickname of a HUAWEI ID.

 |

If the **quickLoginAnonymousPhone** scope is passed in the request, the parameter in the following table is returned.

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

anonymized\_login\_mobile\_number

 | 

No

 | 

String

 | 

Anonymous mobile number bound to a HUAWEI ID. For details, please refer to [Signing In with HUAWEI ID Through Just One Tap (Obtaining the Mobile Number, UnionID, and OpenID)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-phone-unionid-login).

 |

If the **email** scope is passed in the request, parameters in the following table are returned.

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

email\_verified

 | 

No

 | 

Boolean

 | 

Indicates whether a user's email address has been verified.

-   **true**: yes
-   **false**: no

As an email address is not a required field for a HUAWEI ID, the response may not include this parameter.

 |
| 

email

 | 

No

 | 

String

 | 

Email address. As an email address is not a required field for a HUAWEI ID, the response may not include this parameter.

 |

#### Response Example

## Request Success

HTTP/1.1 200 OK
Content-Type: application/json

{
	"at\_hash": "Dx5WUwU\*\*\*\*\*L-SKuAvWUg",
	"sub": "AQAxrB1HNA\*\*\*\*\*n-IfWRSUVq2M7xU",
	"kid": "6a2880c5d6a88c\*\*\*\*\*88eb680e05197d5bebd\*\*\*\*\*7b71757fc1b9530809ca",
	"iss": "https://accounts.huawei.com",
	"typ": "JWT",
	"display\_name": "Jack",
	"nickname": "Jack",
	"aud": "30\*\*\*\*\*33",
	"azp": "30\*\*\*\*\*33",
	"exp": 1563823909,
	"iat": 1563820309,
	"alg": "PS256",
	"nonce": "default",
	"openid": "AQAxrBzThFv\*\*\*\*\*lv9tV\_4rMCc"
}

## Request Failure

HTTP/1.1 400 Bad Request
Content-Type: application/json

{
	"sub\_error": 14004,
	"error\_description": "jwk not found error",
	"error": 1400
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
 \* Verify an ID Token.
 \*/
@Slf4j
public class IDTokenAPIDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for verifying an ID token.
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo";
        // Replace it with the ID token you obtained.
        String idToken = "_<ID Token>_";
        JSONObject result = getDetailByIDToken(url, idToken);
        // Parse the result to obtain kid.
        String kid = result.getString("kid");
        // Parse the result to obtain typ.
        String typ = result.getString("typ");
        // Parse the result to obtain alg.
        String alg = result.getString("alg");
        // Parse the result to obtain iss.
        String iss = result.getString("iss");
        // Parse the result to obtain sub.
        String sub = result.getString("sub");
        // Parse the result to obtain aud.
        String aud = result.getString("aud");
        // Parse the result to obtain exp.
        Long exp = result.getLong("exp");
        // Parse the result to obtain iat.
        Long iat = result.getLong("iat");
        // Parse the result to obtain at\_hash.
        String atHash = result.getString("at\_hash");
        // Parse the result to obtain azp.
        String azp = result.getString("azp");
        // Parse the result to obtain openid.
        String openid = result.getString("openid");
        // Parse the result to obtain nonce.
        String nonce = result.getString("nonce");
    }

    private static JSONObject getDetailByIDToken(String url, String idToken) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("id\_token", idToken));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
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

1203

 | 

100305

 | 

Failed to parse the header in the ID token.

 | 

The value format of **id\_token** is incorrect or its value is forged.

-   Ensure that the value of **id\_token** is in JWT format.
-   Ensure that the value is the original one returned by HUAWEI ID.

 |
| 

100306

 | 

Failed to parse the payload in the ID token.

 | 

The value format of **id\_token** is incorrect or its value is forged.

-   Ensure that the value of **id\_token** is in JWT format.
-   Ensure that the value is the original one returned by HUAWEI ID.

 |
| 

150021

 | 

Failed to parse the ID token.

 | 

The value format of **id\_token** is incorrect or its value is forged.

-   Ensure that the value of **id\_token** is in JWT format.
-   Ensure that the value is the original one returned by HUAWEI ID.

 |
| 

150023

 | 

Failed to parse the signature of the ID token.

 | 

The value format of **id\_token** is incorrect or its value is forged.

-   Ensure that the value of **id\_token** is in JWT format.
-   Ensure that the value is the original one returned by HUAWEI ID.

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

The value format of **id\_token** is incorrect or its value is forged.

-   Ensure that the value of **id\_token** is in JWT format.
-   Ensure that the value is the original one returned by HUAWEI ID.

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
