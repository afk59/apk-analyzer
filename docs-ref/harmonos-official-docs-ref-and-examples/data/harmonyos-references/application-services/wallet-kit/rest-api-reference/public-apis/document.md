# Public APIs

#### Obtaining an Access Token

This API is used to obtain an access token. Each HTTPS request sent to the HUAWEI Wallet server needs to contain an access token, which will be verified by the HUAWEI Wallet server.

## API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.2.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.2.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Third-party management service -&gt; HUAWEI Wallet server</p></td></tr><tr><th class="firstcol" id="mcps1.3.2.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://oauth-login.cloud.huawei.com/oauth2/v3/token</p></td></tr><tr><th class="firstcol" id="mcps1.3.2.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/x-www-form-urlencoded</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

## Request Parameters

**Request Header**

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

 |

**Request Body**

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

Permission grant mode. Set this parameter to **client\_credentials**, which indicates the client credential mode.

 |
| 

client\_id

 | 

Yes

 | 

String

 | 

OAuth 2.0 client ID obtained during [app development preparations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview). For an app created in AppGallery Connect, set this parameter to the value of **Client ID**.

 |
| 

client\_secret

 | 

Yes

 | 

String

 | 

Client secret allocated to the client ID created in [app development preparations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview). For an app created in AppGallery Connect, set this parameter to the value of **Client Secret**.

 |

## Request Example

grant\_type=client\_credentials&client\_id=<_Client ID_\>&client\_secret=<_Client secret_\>

## Response Parameters

**Response Header**

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

Content type. The value is **application/json;charset=UTF-8**.

 |

**Response Body**

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

Token type. The value is always **Bearer**.

 |
| 

access\_token

 | 

Yes

 | 

String

 | 

Access token.

 |
| 

expires\_in

 | 

No

 | 

Long

 | 

Access token validity period, in seconds. The default value is 3600 seconds (that is, 60 minutes).

 |

## Response Example

{
  "access\_token": "<_Returned access token_\>",
  "expires\_in": 3600,
  "token\_type": "Bearer"
}

## Call Example

    public static String getToken(String clientId, String clientSecret) {
        HttpHeaders header = new HttpHeaders();
        header.setContentType(MediaType.APPLICATION\_FORM\_URLENCODED);

        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
        map.add("grant\_type", "client\_credentials");
        map.add("client\_id", clientId);
        map.add("client\_secret", clientSecret);

        String tokenUrl = ConfigUtil.instants().getValue("gw.tokenUrl");

        HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, header);
        ResponseEntity<JSONObject> exchange =
            REST\_TEMPLATE.exchange(tokenUrl, HttpMethod.POST, entity, JSONObject.class);

        JSONObject response = exchange.getBody();
        if (response == null) {
            throw new NullPointerException("Get null token response.");
        }
        String accessToken = response.getString("access\_token");
        if (Strings.isEmpty(accessToken)) {
            throw new NullPointerException("Get null access token.");
        }
        return accessToken;
    }

#### Device Authentication

This API is used to request the third-party management service to authenticate the authorization certificate after pre-personalization. The authentication request is forwarded by the HUAWEI Wallet server and the request body contains the applet's public key and its corresponding digital signature issued by the HUAWEI Wallet server.

## API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.9.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.9.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>HUAWEI Wallet server -&gt; Third-party management service</p></td></tr><tr><th class="firstcol" id="mcps1.3.9.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://{webServiceURL}/v1/passes/registrations</p></td></tr><tr><th class="firstcol" id="mcps1.3.9.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json;charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/9yZmkYSERG2A6PLpU4waqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062520Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4831B0A147FCFE2E205FFB222906F6A662A80FD6FD467F68CED607B9C5CF10EC)

**webServiceURL** indicates the domain name of the DK management service.

## Request Parameters

**Request Header**

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

Content type. The value is **application/json;charset=UTF-8**.

 |
| 

Authorization

 | 

Yes

 | 

String

 | 

Token value in the **linkDevicePass** parameter, used to [apply for a key card](../digital-car-key-apis/document.md#section129511211195). The token is used to check whether the request is valid.

 |

**Request Body**

| 
Parent Node Parameter

 | 

Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestBody

 | 

passTypeIdentifier

 | 

String

 | 

Mandatory

 | 

Service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212) in AppGallery Connect.

 |
| 

serialNumber

 | 

String

 | 

Mandatory

 | 

Number of the car key card on the HUAWEI Wallet server, which is used by the issuer to identify the card.

 |
| 

passVersion

 | 

String

 | 

Optional

 | 

Version number, which is always **10.0**.

 |
| 

userDeviceId

 | 

String

 | 

Mandatory

 | 

Unique ID of a user device.

 |
| 

transId

 | 

String

 | 

Mandatory

 | 

Random number.

 |
| 

signature

 | 

\-

 | 

String

 | 

Mandatory

 | 

Signature of the hash value in **requestBody**, created by using the applet identity private key.

 |
| 

certificate

 | 

signature

 | 

String

 | 

Mandatory

 | 

Signature value generated for the public key by the HUAWEI Wallet server using the private key. When receiving the request, the DK management service needs to use the public key provided by the HUAWEI Wallet server to authenticate the signature.

 |
| 

publicKey

 | 

String

 | 

Mandatory

 | 

Identity public key of the applet.

 |

## Request Example

{
  "requestBody": {
    "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
    "passVersion": "10.0",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "transId": "16198381994485116358",
    "userDeviceId": "xxx"
  },
  "certificate": {
    "publicKey": "xxx",
    "signature": "xxx"
  },
  "signature": "xxx"
}

## Response Parameters

**Response Header**

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

Content type. The value is **application/json;charset=UTF-8**.

 |

**Response Body**

| 
Parent Node Parameter

 | 

Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Httpstatus

 | 

\-

 | 

String

 | 

Mandatory

 | 

HTTP status code.

 |
| 

response

 | 

certificate

 | 

Certificate

 | 

Optional

 | 

Certificate returned, which is signed by the DK management service using the private key generated in step 4 of [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212).

 |

**Certificate Parameters**

| 
Certificate Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

signature

 | 

String

 | 

Mandatory

 | 

Signature value generated for the public key by the HUAWEI Wallet server using the private key. When receiving the request, the DK management service needs to use the public key provided by the HUAWEI Wallet server to authenticate the signature.

 |
| 

publicKey

 | 

String

 | 

Mandatory

 | 

Identity public key of the applet.

 |

## Response Example

{
  "httpStatus": "0",
  "response": {
    "certificate": {
      "signature": "xxx",
      "publicKey": "xxx"
    }
  }
}

## Call Example of the Third-Party Management Service

For details about the complete call example, please refer to the sample code in [Wallet Kit - Card Activation on the Server](https://gitee.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java).

    public RegistrationsResponse dealWithRegisterRequest(String token, RegistrationsRequest request) {
        RegistrationsResponse response = new RegistrationsResponse();
        if (token == null) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_PARAM\_ERROR));
            return response;
        }
        if (!ParamChecker.isValidRegistrationsRequest(request)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_PARAM\_ERROR));
            return response;
        }
        Certificate walletCertificate = request.getCertificate();
        if (!verifyWalletCert(walletCertificate)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_SIGN\_ERROR));
            return response;
        }

        if (!ParamChecker.hashSignatureCheck(request.toJsonString(), request.getSignature(),
                appletAuthPublicKey, DataConvertUtil.SIGN\_MODE\_SHA256\_RSA\_MGF1)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_SIGN\_ERROR));
            return response;
        }

        String userDeviceId = request.getRequestBody().getUserDeviceId();
        response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_OK));
        Response responseBody = new Response();
        Certificate serverCert = PassData.getServerCert(appletAuthPublicKey);
        responseBody.setCertificate(serverCert);
        response.setResponse(responseBody);
        deviceIdCertMap.put(userDeviceId, serverCert);
        return response;
    }

#### Obtaining a Personal Data Token

This API is used to obtain a personal data token from the third-party management service. The request is forwarded by the HUAWEI Wallet server. The token will be used to calculate the hash value in the personal data request.

## API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.16.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.16.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>HUAWEI Wallet server -&gt; Third-party management service</p></td></tr><tr><th class="firstcol" id="mcps1.3.16.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://{webServiceURL}/v1/passes/requestPersonalizeToken</p></td></tr><tr><th class="firstcol" id="mcps1.3.16.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json;charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

## Request Parameters

**Request Header**

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

Content type. The value is **application/json;charset=UTF-8**.

 |
| 

Authorization

 | 

Yes

 | 

String

 | 

Token value in the **linkDevicePass** parameter, used to [apply for a key card](../digital-car-key-apis/document.md#section129511211195). The token is used to check whether the request is valid.

 |

**Request Body**

| 
Parent Node Parameter

 | 

Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestBody

 | 

passTypeIdentifier

 | 

String

 | 

Mandatory

 | 

Service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212) in AppGallery Connect.

 |
| 

serialNumber

 | 

String

 | 

Mandatory

 | 

Number of the car key card on the HUAWEI Wallet server, which is used by the issuer to identify the card.

 |
| 

passVersion

 | 

String

 | 

Optional

 | 

Version number, which is always **10.0**.

 |
| 

userDeviceId

 | 

String

 | 

Mandatory

 | 

Unique ID of a user device.

 |
| 

transId

 | 

String

 | 

Mandatory

 | 

Random number.

 |
| 

signature

 | 

\-

 | 

String

 | 

Mandatory

 | 

Signature of the hash value in **requestBody**, created by using the applet identity private key.

 |
| 

certificate

 | 

signature

 | 

String

 | 

Mandatory

 | 

Signature of the certificate returned by the [Device Authentication](#section113578586311) API.

The DK management service signs the identity public key of the applet using the private key generated in step 4 of [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212).

 |
| 

publicKey

 | 

String

 | 

Mandatory

 | 

Identity public key of the applet in the certificate returned by the [Device Authentication](#section113578586311) API.

 |

## Request Example

{
  "requestBody": {
    "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
    "passVersion": "10.0",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "transId": "16198381994485116358",
    "userDeviceId": "xxx"
  },
  "certificate": {
    "publicKey": "xxx",
    "signature": "xxx"
  },
  "signature": "xxx"
}

## Response Parameters

**Response Header**

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

Content type. The value is **application/json;charset=UTF-8**.

 |

**Response Body**

| 
Parent Node Parameter

 | 

Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Httpstatus

 | 

\-

 | 

String

 | 

Mandatory

 | 

HTTP status code.

 |
| 

response

 | 

token

 | 

String

 | 

Mandatory

 | 

Personal data token.

 |

## Response Example

{
  "httpStatus": "0",
  "response": {
    "token": "sp.token.1619838979341"
  }
}

## Call Example of the Third-Party Management Service

For details about the complete call example, please refer to the sample code in [Wallet Kit - Card Activation on the Server](https://gitee.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java).

    public RequestTokenResponse dealWithTokenRequest(RequestTokenRequest request) {
        RequestTokenResponse response = new RequestTokenResponse();
        String userDeviceId = request.getRequestBody().getUserDeviceId();
        Certificate spCertFromRequest = request.getCertificate();
        if (CommonUtils.isStringEmpty(userDeviceId) || !ParamChecker.checkSpServerCertificate(spCertFromRequest)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_PARAM\_ERROR));
            return response;
        }
        Certificate cachedCert = deviceIdCertMap.get(userDeviceId);
        if (cachedCert == null) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_SIGN\_ERROR));
            return response;
        }
        if (!ParamChecker.hashSignatureCheck(request.toJsonString(), request.getSignature(),
                appletAuthPublicKey, DataConvertUtil.SIGN\_MODE\_SHA256\_RSA\_MGF1)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_SIGN\_ERROR));
            return response;
        }
        response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_OK));
        Response responseBody = new Response();
        String personalizeToken = PassData.getPersonalizeToken();
        responseBody.setToken(personalizeToken);
        deviceIdTokenMap.put(userDeviceId, personalizeToken);
        response.setResponse(responseBody);
        return response;
    }

#### Obtaining Personal Data

This API is used to obtain personal data from the third-party management service. The request is forwarded by the HUAWEI Wallet server.

## API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.23.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>HUAWEI Wallet server -&gt; Third-party management service</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://{webServiceURL}/v1/passes/requestPersonalize</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json;charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

## Request Parameters

**Request Header**

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

Content type. The value is **application/json;charset=UTF-8**.

 |
| 

Authorization

 | 

Yes

 | 

String

 | 

Token value returned in [Obtaining a Personal Data Token](#section257714144308), which is used to check whether the request is valid.

 |

**Request Body**

| 
Parent Node Parameter

 | 

Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestBody

 | 

cardSEId

 | 

String

 | 

Mandatory

 | 

Unique ID of an applet, which can be used to distribute the car key.

 |
| 

passTypeIdentifier

 | 

String

 | 

Mandatory

 | 

Service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212) in AppGallery Connect.

 |
| 

serialNumber

 | 

String

 | 

Mandatory

 | 

Number of the car key card on the HUAWEI Wallet server, which is used by the issuer to identify the card.

 |
| 

passVersion

 | 

String

 | 

Optional

 | 

Version number, which is always **10.0**.

 |
| 

userDeviceId

 | 

String

 | 

Mandatory

 | 

Unique ID of a user device.

 |
| 

personalizePublicKey

 | 

String

 | 

Mandatory

 | 

Personalized public key of the applet, which is used to encrypt personal data field values.

 |
| 

personalizeCert

 | 

String

 | 

Mandatory

 | 

Signature of **personalizePublicKey**, created by using the applet identity private key.

 |
| 

personalizeCertType

 | 

String

 | 

Mandatory

 | 

Fixed value. The private-key signature is used by default.

 |
| 

transPublicKey

 | 

String

 | 

Mandatory

 | 

Transaction public key, which is used to encrypt the returned symmetric key and make a digital envelope for the returned data.

 |
| 

transId

 | 

String

 | 

Mandatory

 | 

Transaction ID, which is used to combine the returned symmetric key.

 |
| 

signature

 | 

\-

 | 

String

 | 

Mandatory

 | 

Signature of the hash value in **requestBody**, created by using the applet identity private key. The obtained personal data token in [Obtaining a Personal Data Token](#section257714144308) is used as a key value in **requestBody** for hash value calculation.

 |
| 

certificate

 | 

signature

 | 

String

 | 

Mandatory

 | 

Signature of the certificate returned by the [Device Authentication](#section113578586311) API.

The DK management service signs the identity public key of the applet using the private key generated in step 4 of [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212).

 |
| 

publicKey

 | 

String

 | 

Mandatory

 | 

Identity public key of the applet in the certificate returned by the [Device Authentication](#section113578586311) API.

 |

## Request Example

{
  "requestBody": {
    "cardSEId": "xxxxxxxxxxxxxxxx",
    "personalizeCert": "xxx",
    "personalizeCertType": "",
    "personalizePublicKey": "xxx",
    "transPublicKey": "xxx",
    "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
    "passVersion": "10.0",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "transId": "858947076d58a5e66ee22b9ed1c43c4d",
    "userDeviceId": "xxx"
  },
  "certificate": {
    "publicKey": "xxx",
    "signature": "xxx"
  },
  "signature": "xxx"
}

## Response Parameters

**Response Header**

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

Content type. The value is **application/json;charset=UTF-8**.

 |

**Response Body**

| 
Parent Node Parameter

 | 

Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Httpstatus

 | 

\-

 | 

String

 | 

Mandatory

 | 

HTTP status code.

 |
| 

response

 | 

encryptSessionKey

 | 

String

 | 

Mandatory

 | 

Session key encrypted by the DK management service using **transPublicKey** in the request. The fields involved in encryption using Base64 encoding are described as follows: The AES128 values of **aesKey** and **aesIv** are generated by the third-party management service and are used to generate **encryptAppletPersonalizeFields** and **encryptDevicePass** after encryption. The values of **transId**, **aesKey**, and **aesIv** are encrypted using **transPublicKey** in the request and then encoded by Base64 to obtain **encryptSessionKey**. Encryption algorithm: RSA/ECB/OAEPWithSHA-256AndMGF1Padding.

 |
| 

encryptDevicePass

 | 

String

 | 

Optional

 | 

Empty string.

 |
| 

encryptAppletPersonalizeFields

 | 

String

 | 

Mandatory

 | 

Personal data parameter of the applet, used for authentication and data encryption and decryption during Bluetooth/NFC card swiping. The parameter is encrypted by the DK management service using the generated session key. The value is then encoded by Base64.

 |
| 

signature

 | 

\-

 | 

String

 | 

Mandatory

 | 

The DK management service signs the hash value of the response using the private key generated in step 4 of [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212).

 |

| 
encryptAppletPersonalizeFields Subnode Parameter

 | 

Type

 | 

Mandatory/Optional

 | 

Storage Format

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

temp\_key

 | 

String

 | 

Mandatory

 | 

\-

 | 

Plaintext of AES128 key, left padded with a fixed hexadecimal string 34810233 and then encrypted using **appletPublicKey**. The AES128 key contains 16 bytes and is used to encrypt **CardId** and **cardPrivateInfo**. The encryption algorithm is RSA/NONE/OAEPWithSHA1AndMGF1Padding.

 |
| 

temp\_iv

 | 

String

 | 

Mandatory

 | 

\-

 | 

AES-128 IV encrypted using **appletPublicKey** (applet personal public key), which contains 16 bytes and is used by the applet to decrypt the card data. The encryption algorithm is RSA/NONE/OAEPWithSHA1AndMGF1Padding.

 |
| 

card\_id

 | 

String

 | 

Mandatory

 | 

9F3B + Lc + CardId

 | 

Unique ID of a card issued by the issuer, which is the same as the value of **serialNumber** defined when the key card is generated. The ID contains 16 bytes. The card ID is encoded in TLV format, where **T=9F3B** indicates the data type, **Lc=10** specifies the length as 10 bytes, and **V** represents the card ID. The entire TLV is encrypted using **aesKey** and **aesIv** and then converted into a hexadecimal string. The CBC encryption mode is used and the encryption algorithm is AES/CBC/NoPadding.

 |
| 

card\_key

 | 

String

 | 

Mandatory

 | 

\-

 | 

Key of a card, which contains 16 bytes and is used to calculate **SessionKey**. Each card supports one key. The key is left padded with **34010133**, and then the entire string is converted into a hexadecimal string and encrypted using **appletPublicKey**. The encryption algorithm is RSA/NONE/OAEPWithSHA1AndMGF1Padding.

 |
| 

card\_info

 | 

String

 | 

Mandatory

 | 

9F05 + Lc + CardInfo1 + 9F31 + Lc + CardAuthParameter

 | 

Private information about a card, which can be read before authentication (**GetProcessData** step) and stored in TLV format (with multiple TLV records combined). The plaintext TLV data is padded with 800...00 to a multiple of 16 bytes. The result is encrypted using **aesKey** and **aesIv**, and then converted into a hexadecimal string. The CBC encryption mode is used and the encryption algorithm is AES/CBC/NoPadding.

 |
| 

card\_privateInfo

 | 

String

 | 

Mandatory

 | 

\-

 | 

Private information about a card, such as the validity period and permissions. The information is read after authentication (**ReadBinary** step) and parsed by the third-party management service. The plaintext data is padded with 800...00 to a multiple of 16 bytes. The result is encrypted using **aesKey** and **aesIv**, and then converted into a hexadecimal string. The CBC encryption mode is used and the encryption algorithm is AES/CBC/NoPadding.

 |
| 

card\_key\_iv

 | 

String

 | 

Mandatory

 | 

Lc + CardKeyIV

 | 

Session key negotiated in the transaction process (which needs to be delivered to the car synchronously). The value contains 16 bytes. If you do not need to use this value, pass zeros for all bytes.

 |

## Response Example

{
  "httpStatus": "0",
  "response": {
    "encryptDevicePass": "xxx",
    "encryptAppletPersonalizeFields": "xxx",
    "encryptSessionKey": "xxx"
  },
  "signature": "xxx"
}

## Call Example of the Third-Party Management Service

For details about the complete call example, please refer to the sample code in [Wallet Kit - Card Activation on the Server](https://gitee.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java).

    public PersonalizeResponse dealWithPersonalizeDataRequest(String token, PersonalizeRequest request) {
        PersonalizeResponse response = new PersonalizeResponse();
        RequestBody requestBody = request.getRequestBody();
        String userDeviceId = requestBody.getUserDeviceId();
        Certificate spCertFromRequest = request.getCertificate();
        String cachedToken = deviceIdTokenMap.remove(userDeviceId);
        if (cachedToken == null || !cachedToken.equals(token)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_PARAM\_ERROR));
            return response;
        }
        if (CommonUtils.isStringEmpty(userDeviceId) || !ParamChecker.checkSpServerCertificate(spCertFromRequest)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_PARAM\_ERROR));
            return response;
        }

        Certificate cachedCert = deviceIdCertMap.get(userDeviceId);
        if (cachedCert == null) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_PARAM\_ERROR));
            return response;
        }
        if (!ParamChecker.hashSignatureCheck(request.toJsonString(token), request.getSignature(),
                appletAuthPublicKey, DataConvertUtil.SIGN\_MODE\_SHA256\_RSA\_MGF1)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_SIGN\_ERROR));
            return response;
        }
        String personalizePKSign = requestBody.getPersonalizeCert();
        byte\[\] srcBytes = DataConvertUtil.base64Decode(requestBody.getPersonalizePublicKey());
        if (!DataConvertUtil.checkSign(srcBytes, personalizePKSign,
                appletAuthPublicKey, DataConvertUtil.SIGN\_MODE\_SHA256\_RSA\_MGF1)) {
            response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_SIGN\_ERROR));
            return response;
        }
        response.setHttpStatus(String.valueOf(Constants.RESULT\_CODE\_OK));
        PassDataResponse passData = getDevicePassData(requestBody);
        response.setResponse(passData);
        String passDataStr = passData.toJsonString();
        String passHashValue = DataConvertUtil.encodeSHA256(passDataStr);
        String signature = DataConvertUtil.signData(passHashValue, Constants.SERVER\_SECRET\_KEY);
        response.setSignature(signature);
        return response;
    }
