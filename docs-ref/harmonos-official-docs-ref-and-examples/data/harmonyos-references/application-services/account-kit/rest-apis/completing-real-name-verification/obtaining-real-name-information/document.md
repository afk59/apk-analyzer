# Obtaining Real-Name Information

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/niE6YmM4Rp69rvfFw9rhmg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67F4FD558A2085966DE345A5B19D0C7D1FD5A98C967008228A49E650DCA37FE9)

To ensure secure network access, use the TLS 1.2 protocol and the specified cipher suites. If your app server accesses Account Kit using TLS 1.0, TLS 1.1, or unsupported cipher suites, the connection may fail.

For details about TLS 1.2 and the specified cipher suites, see [TLS Protocol and Cipher Suites](../../common-description/document.md#section1329115361128).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/egd0kq0yQm-D05SQshUr6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6F928B628BA66281F9B5234883AEB09F6D423517A96E5C113CFF887FF39766F)

This API is temporarily unavailable.

#### Function

This API is called by your app server from the Account Kit server to obtain the real-name information (name and ID card number) of a HUAWEI ID.

#### Scenario

After your app has obtained an access token using the authorization code and has requested the relevant scopes for obtaining user information, it can access user information such as the name and ID card number.

#### Restrictions

This API is temporarily unavailable.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.6.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Developer server -&gt; Account Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>API URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://openrealname.cloud.huawei.com/rest.php?nsp_svc=OpenRealName.User.getDetailInfo</p></td></tr><tr><th class="firstcol" id="mcps1.3.6.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

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

 |
| 

queryRangeFlag

 | 

Yes

 | 

String

 | 

Real-name information query scope.

The value is always **0001**.

 |
| 

serviceAccountClientID

 | 

Yes

 | 

String

 | 

Service account.

The value of this parameter is the same as that of **sub\_account** in the service account key file that you generate under **Credentials** on the [HUAWEI Developers console](https://developer.huawei.com/consumer/en/console/api/credentials/dev388421841221457823/0).

 |
| 

serviceAccountKeyID

 | 

Yes

 | 

String

 | 

Service account key ID.

The value of this parameter is the same as that of **key\_id** in the key file generated when the service account key is created.

 |

#### Request Example

Send a POST request. Example:

POST /rest.php?nsp\_svc=OpenRealName.User.getDetailInfo HTTP/1.1
Host: openrealname.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

access\_token=_<access\_token>_&queryRangeFlag=0001&serviceAccountClientID=_<serviceAccountClientID>_&serviceAccountKeyID=_<serviceAccountKeyID>_

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

encryptedInfo

 | 

No

 | 

String

 | 

Encrypted name and ID card number.

Use the Base64.decodeBase64 method to decode the string and use the private key corresponding to the **serviceAccountKeyID** passed in the request to decrypt the string. The decryption algorithm is RSA/ECB/OAEPWithSHA-256AndMGF1Padding. After decryption, you can obtain the plaintext name and ID card number in JSON format, for example, {realName:_xxx_, ctfCode:_xxx\*\*xxx_}.

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
    "encryptedInfo": "Uqk1s2m2Go-wN0bZIvgDawGUXjQb5i73pyhwQp\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ytyISICH0zSKP87zrw"
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
import org.apache.commons.codec.binary.Base64;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.message.BasicNameValuePair;
import javax.crypto.Cipher;
import javax.crypto.spec.OAEPParameterSpec;
import javax.crypto.spec.PSource;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.spec.MGF1ParameterSpec;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.ArrayList;
import java.util.List;

/\*\*
 \* Obtain real-name information.
 \*/
@Slf4j
public class GetDetailInfoDemo {
    public static void main(String\[\] args) throws IOException {
        // URL of the API for obtaining real-name information.
        String url = "https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.getDetailInfo";
        // Replace it with the access token you obtained.
        String accessToken = "_<Access Token>_";
        // Replace it with the private key allocated when you create a service account. (Strip away the -----BEGIN PRIVATE KEY-----\\n header and \\n-----END PRIVATE KEY-----\\n footer, leaving only the key material in between.)
        String privateKey = "_<Private Key>_";
        JSONObject result = getDetailInfo(url, accessToken);
        // Parse the result to obtain encryptedInfo.
        String encryptedInfo = result.getString("encryptedInfo");
        // Decrypt encryptedInfo.
        String plainData = null;
        try {
            plainData = decryptByPrivateKey(Base64.decodeBase64(encryptedInfo), privateKey);
        } catch (GeneralSecurityException e) {
            // Exception handling for decryption failure, for example, print logs.
            log.error("decrypt encryptedInfo failed");
        }
    }

    private static JSONObject getDetailInfo(String url, String accessToken) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("access\_token", accessToken));
        // Adjust the value of serviceAccountClientID based on the actual situation.
        request.add(new BasicNameValuePair("serviceAccountClientID", "_<serviceAccountClientID>_"));
        // Adjust the value of serviceAccountKeyID based on the actual situation.
        request.add(new BasicNameValuePair("serviceAccountKeyID", "_<serviceAccountKeyID>_"));
        // Adjust the value of queryRangeFlag based on the actual situation.
        request.add(new BasicNameValuePair("queryRangeFlag", "0001"));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // Use the default exception handling logic. For custom exception handling, use the CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>) API.
        return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
    }

    public static String decryptByPrivateKey(byte\[\] data, String privateKey) throws GeneralSecurityException {
        String KEY\_RSA = "RSA";
        String KEY\_RSA\_OAEP = "RSA/ECB/OAEPWithSHA-256AndMGF1Padding";
        byte\[\] bytes = Base64.decodeBase64(privateKey);
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(bytes);
        PrivateKey pk = KeyFactory.getInstance(KEY\_RSA).generatePrivate(keySpec);
        Cipher cipher = Cipher.getInstance(KEY\_RSA\_OAEP);
        OAEPParameterSpec spec = new OAEPParameterSpec("SHA-256", "MGF1", MGF1ParameterSpec.SHA256,
                PSource.PSpecified.DEFAULT);
        cipher.init(Cipher.DECRYPT\_MODE, pk, spec);
        return new String(cipher.doFinal(data), StandardCharsets.UTF\_8);
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/IoLKtRLhSyC7jhW5G9W89w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062502Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=552CF2E145CDD781CC46218B508E8952C2E946556EAC408EF9C2E80CEBD41B0C)

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

Try again later. If the problem persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

70009019

 | 

The real-name information does not exist.

 | 

Guide users to complete real-name authentication or use a real-name verified account. If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
