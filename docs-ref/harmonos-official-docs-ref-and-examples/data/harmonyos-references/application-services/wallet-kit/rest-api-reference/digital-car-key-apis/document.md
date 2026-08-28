# Digital Car Key APIs

#### Preset Templates

The first step of the integration is to create card templates. This entails sending HTTP/HTTPS requests to the HUAWEI Wallet server with card style details, including the card's main title, subtitle, logo, and background image for display in HUAWEI Wallet.

You can create multiple templates with different template IDs, under the same organization name and service ID. When you apply for a car key, each card must be associated with a unique template ID. That is, one template can be associated with multiple car keys, but one car key can be associated with only one template.

## API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.2.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.2.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Third-party management service -&gt; HUAWEI Wallet server</p></td></tr><tr><th class="firstcol" id="mcps1.3.2.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/key_stdcar/model</p></td></tr><tr><th class="firstcol" id="mcps1.3.2.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json;charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

Concatenate the value of **access\_token** obtained in [Obtaining an Access Token](../public-apis/document.md#section37263211548) to the end of **Bearer**, with a space in between, to generate the value of **Authorization**.

 |
| 

Accept

 | 

Yes

 | 

String

 | 

Content type. The value is **application/json;charset=UTF-8**.

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

passTypeIdentifier

 | 

Yes

 | 

String

 | 

The value is in hwpass.stdcarkey._xxx.xxx_ format, where _xxx_ can be a company name or product name containing up to 32 lowercase letters.

Service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212) in AppGallery Connect.

 |
| 

passStyleIdentifier

 | 

Yes

 | 

String

 | 

Custom template ID, which is the same as **modelId**. A unique ID is used under the same **appId**. The value contains a maximum of 64 characters, including only letters, digits, dots (.), hyphens (-), and underscores (\_).

 |
| 

organizationName

 | 

Yes

 | 

String

 | 

Organization name, containing a maximum of 64 bytes. The value can be customized and can contain both English and Chinese characters.

 |
| 

passVersion

 | 

Yes

 | 

String

 | 

Version number, which is always **10.0**.

You can determine the version of the HUAWEI Wallet object based on this parameter.

 |
| 

fields

 | 

Yes

 | 

fields

 | 

Custom fields.

The parameter defines card display information, including **appendFields** and **commonFields**.

 |

| 
appendFields Parameter

 | 

Value

 | 

Label

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isCreateWhiteCard

 | 

true

 | 

NFCCardFlag

 | 

Yes

 | 

Indicates whether the card is an NFC card.

 |

| 
commonFields Parameter

 | 

Value

 | 

Label

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

logo

 | 

Image link starting with **https://**, which is defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Logo on the card.

The logo must be a 128 x 128 px right-angle image of up to 20 KB.

 |
| 

backgroundImage

 | 

Image link starting with **https://**, which is defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Card background image.

The background image must be a 1312 x 820 px right-angle image.

 |
| 

picUrl

 | 

Image link starting with **https://**, which is defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Card background image with a logo.

The background image must be a 1312 x 820 px right-angle image.

 |
| 

merchantName

 | 

Value defined by the car manufacturer

 | 

Card main title

 | 

Yes

 | 

Main title on the card.

The title should contain less than 256 bytes.

 |
| 

name

 | 

Value defined by the car manufacturer

 | 

Card subtitle

 | 

Yes

 | 

Subtitle on the card.

The title should contain less than 256 bytes.

 |

## Request Example

{
  "passVersion": "10.0",
  "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
  "passStyleIdentifier": "DigitalCarKeyTestModel",
  "organizationName": "Replace with your organization name",
  "fields": {
    "appendFields": \[
      {
        "label": "NFCCardFlag",
        "value": "true",
        "key": "isCreateWhiteCard"
      }
    \],
    "commonFields": \[
      {
        "label": "Card main title",
        "value": "My car",
        "key": "merchantName"
      },
      {
        "label": "Card subtitle",
        "value": "XXX car key",
        "key": "name"
      },
      {
        "label": "",
        "value": "https://xxx/xxx.png",
        "key": "logo"
      },
      {
        "label": "",
        "value": "https://xxx/xxx.webp",
        "key": "backgroundImage"
      },
      {
        "label": "",
        "value": "https://xxx/xxx.png",
        "key": "picUrl"
      }
    \]
  }
}

## Response Parameters

When templates are preset successfully, that is, when the HTTP status code 200 is returned, the HUAWEI Wallet server returns the same data in the request body sent from the DK management service. For details about other error codes, please refer to [REST API Error Codes](../rest-api-result-codes/document.md).

## Call Example

    public void createStdCarKeyModel() {
        JSONObject model = JSONObject.parseObject(ConfigUtil.readFile("StdCarKeyModel.json"));
        HwWalletObjectUtil.validateModel(model);
        String urlSegment = "/v2/key\_stdcar/model";
        JSONObject responseModel = serverApiService.postToWalletServer(urlSegment, JSONObject.toJSONString(model));
    }

#### Applying for an ICCE Car Key

When the car owner app applies for an ICCE car key from the DK management service, the DK management service adds the car key card information to the HUAWEI Wallet server. In the process, the interaction between the car owner app and DK management service is implemented by the car manufacturer. This section focuses on the part that the DK management service applies for an ICCE car key from the HUAWEI Wallet server, including applying for a key card and generating JWE data.

## Applying for a Key Card

This API is used by the DK management service to request the HUAWEI Wallet server to create a car key card.

## API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.9.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.9.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Third-party management service -&gt; HUAWEI Wallet server</p></td></tr><tr><th class="firstcol" id="mcps1.3.9.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass/v2/key_stdcar/instance</p></td></tr><tr><th class="firstcol" id="mcps1.3.9.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json;charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

Concatenate the value of **access\_token** obtained in [Obtaining an Access Token](../public-apis/document.md#section37263211548) to the end of **Bearer**, with a space in between, to generate the value of **Authorization**.

 |
| 

Accept

 | 

Yes

 | 

String

 | 

Content-Type: application/json;charset=UTF-8

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

passTypeIdentifier

 | 

Yes

 | 

String

 | 

The value is in hwpass.stdcarkey._xxx.xxx_ format, where _xxx_ can be a company name or product name containing up to 32 lowercase letters.

Service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212) in AppGallery Connect.

 |
| 

passStyleIdentifier

 | 

Yes

 | 

String

 | 

Custom parameter. The default value in the sample code is for reference only.

Use the template ID created in the preset template, that is, **modelId**. A unique ID is used under the same **appId**. The value contains a maximum of 64 characters, including only letters, digits, dots (.), hyphens (-), and underscores (\_).

 |
| 

organizationName

 | 

Yes

 | 

String

 | 

Custom parameter. The default value in the sample code is for reference only.

Use the organization name created in the preset template. The value contains a maximum of 64 bytes.

 |
| 

organizationPassId

 | 

Yes

 | 

String(64)

 | 

Custom parameter. The default value in the sample code is for reference only.

ID of a car key card on your server. A unique ID is used under the same **appId**. The value contains 16 bytes, including digits and all uppercase letters. To ensure uniqueness, do not manually enter the value. You are advised to use code to generate a random number. The value is the same as that of **serialNumber**.

 |
| 

serialNumber

 | 

Yes

 | 

String(64)

 | 

Custom parameter. The default value in the sample code is for reference only.

Number of a car key card on the HUAWEI Wallet server, that is, **instanceId**. A unique ID is used under the same **appId**. The value contains 16 bytes, including digits and all uppercase letters. To ensure uniqueness, do not manually enter the value. You are advised to use code to generate a random number. The value is the same as that of **organizationPassId**.

 |
| 

fields

 | 

Yes

 | 

fields

 | 

Custom parameter.

The parameter defines card display information, including **commonFields**, **timeList**, and **status**.

 |
| 

linkDevicePass

 | 

Yes

 | 

linkDevicePass

 | 

Custom parameter.

This parameter stores the URL of the car key management server, public key, and whether NFC cards are supported.

 |

| 
timeList Parameter

 | 

Value

 | 

Label

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

linkDevicePassExpireTime

 | 

Custom value

 | 

/

 | 

Yes

 | 

Time list.

 |

| 
status Parameter

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

String

 | 

Status. The options are as follows:

-   active
-   inactive
-   completed
-   expired

 |
| 

effectTime

 | 

Yes

 | 

String

 | 

UTC time when the car key takes effect.

 |
| 

expireTime

 | 

Yes

 | 

String

 | 

UTC time when the car key expires. The car key will automatically expire if the set expiration time is earlier than the current time.

 |

| 
commonFields Parameter

 | 

Value

 | 

Label

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bleServiceUuid

 | 

Value defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Service UDID of a car manufacturer's Bluetooth device, which is used by mobile phones to detect a car's digital car key service for which Bluetooth is enabled. You need to adhere to the Bluetooth standard, such as 0000xxxx-0000-1000-8000-00805f9b34fb. If you want to customize the value, consult ICCE.

 |
| 

ownerPassTypeIdentifier

 | 

Fixed value

 | 

Service ID of the primary car key

 | 

Yes

 | 

The value is always **hwpass.stdcarkey.std** (ICCE car key).

 |
| 

readerMatchValue

 | 

Value defined by the car manufacturer

 | 

readerId

 | 

Yes

 | 

Car key ID. It is recommended that the value contain no more than 20 bytes. The first byte indicates the car manufacturer, the second byte indicates the brand or series, and the subsequent bytes must be unique within the car manufacturer. The value can contain only digits (0-9) and uppercase letters (A-F).

 |
| 

bleTargetPackage

 | 

Value defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Package name of the car manufacturer app, which is used by HUAWEI Wallet to launch the car manufacturer app in specific scenarios. Set this parameter to the full package name after the app is installed, that is, **applicationId** of the app, for example, **com.huawei.wallet**.

 |
| 

bleTargetActivity

 | 

Value defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Activity of the car manufacturer app, which is used by HUAWEI Wallet to launch the car manufacturer app in specific scenarios. Set this parameter to the full path name without the file suffix, for example, **com.huawei.xxx.xxx.ShowCarDetailActivity**.

 |
| 

bleTargetService

 | 

Value defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Service of the car manufacturer app, which is used by HUAWEI Wallet to launch the car manufacturer app in specific scenarios. Set this parameter to the full path name without the file suffix, for example, **com.huawei.xxx.xxx.BleICCEService**.

 |
| 

bleMacAddress

 | 

Value defined by the car manufacturer

 | 

/

 | 

Yes

 | 

MAC address of the Bluetooth device on the car, which is used by Huawei phones to detect the Bluetooth module on the car and initiate a GATT connection to the Bluetooth module. Set this parameter to an MAC address in valid format, for example, **01:23:45:67:89:0A**. Note that all characters must be capitalized.

 |
| 

bleFeature

 | 

Fixed value

 | 

/

 | 

Yes

 | 

The value is always **hwpass.carkey.ble**, indicating that Bluetooth car keys are supported.

 |
| 

deviceType

 | 

Value that specifies a device type

 | 

/

 | 

Yes

 | 

Device type enabled for the current car key, for example, **Phone** or **Wear**.

 |
| 

keyHolderType

 | 

Value that specifies the key holder type

 | 

/

 | 

Yes

 | 

Key holder type, for example, **Owner** or **Share**.

 |
| 

vehicleId

 | 

Value defined by the car manufacturer

 | 

/

 | 

Yes

 | 

Car VIN, which contains up to 20 bytes.

 |
| 

personalizedData

 | 

Value defined by the car manufacturer

 | 

/

 | 

No

 | 

Personal data of the car manufacturer, which can be used to store data such as car calibration data.

 |
| 

logo

 | 

Image link starting with **https://**, which is defined by the car manufacturer

 | 

/

 | 

No

 | 

Logo on the card, which must be a 128 x 128 px right-angle image of up to 20 KB.

If this parameter is passed, the corresponding field in the template will be replaced with the parameter value.

 |
| 

backgroundImage

 | 

Image link starting with **https://**, which is defined by the car manufacturer

 | 

/

 | 

No

 | 

Card background image, which must be a 1312 x 820 px right-angle image.

If this parameter is passed, the corresponding field in the template will be replaced with the parameter value.

 |
| 

picUrl

 | 

Image link starting with **https://**, which is defined by the car manufacturer

 | 

/

 | 

No

 | 

Card background image with a logo, which must be a 1312 x 820 px right-angle image.

If this parameter is passed, the corresponding field in the template will be replaced with the parameter value.

 |
| 

merchantName

 | 

Value defined by the car manufacturer

 | 

Card main title

 | 

No

 | 

Main title on the card, which contains less than 256 bytes.

If this parameter is passed, the corresponding field in the template will be replaced with the parameter value.

 |
| 

name

 | 

Value defined by the car manufacturer

 | 

Card subtitle

 | 

No

 | 

Subtitle on the card, which contains less than 256 bytes.

If this parameter is passed, the corresponding field in the template will be replaced with the parameter value.

 |

| 
linkDevicePass Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

webServiceURL

 | 

Yes

 | 

String

 | 

URL of the DK management service, which is used to initiate requests to the DK management service, including requesting device authentication, obtaining a personal data token, and obtaining personal data.

 |
| 

token

 | 

Yes

 | 

String

 | 

Token generated by the DK management service, without a fixed format. It is used in **Authorization** carried in the header of [device authentication](../public-apis/document.md#section113578586311) and [personal data token obtaining](../public-apis/document.md#section257714144308) requests sent from the HUAWEI Wallet app to the DK management service.

 |
| 

serialNumber

 | 

Yes

 | 

String

 | 

Set this parameter to the value of **serialNumber**.

 |
| 

passVersion

 | 

No

 | 

String

 | 

**DevicePass** package version, which is always **10.0**.

 |
| 

spPublickey

 | 

Yes

 | 

String

 | 

Public key generated in step 4 of [Applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212), which is used to verify the signature of the personal data of the applet returned from the DK management service. NFC card data will not be sent to the HUAWEI Wallet server. Therefore, the device needs to verify the signature using this parameter.

 |
| 

nfcType

 | 

Yes

 | 

String

 | 

NFC card type, with a fixed value of **1**, indicating that NFC capabilities are enabled. If the value is not **1**, the NFC capabilities will be unavailable for a card instance.

 |

## Request Example

{
  "organizationName": "Replace with your organization name",
  "passTypeIdentifier": "Replace with the Service ID you applied on AGC",
  "passStyleIdentifier": "DigitalCarKeyTestModel",
  "organizationPassId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "fields": {
    "timeList": \[
      {
        "value": "timeListValue",
        "key": "linkDevicePassExpireTime"
      }
    \],
    "status": {
      "state": "active",
      "effectTime": "2020-04-06T00:00:00.111Z",
      "expireTime": "2030-04-06T00:00:00.111Z"
    },
    "commonFields": \[
      {
        "value": "xxx.CarActivity",
        "key": "bleTargetActivity"
      },
      {
        "value": "hwpass.carkey.ble",
        "key": "bleFeature"
      },
      {
        "value": "01:23:45:67:89:AB",
        "key": "bleMacAddress"
      },
      {
        "label": "readerId",
        "value": "CAD34B258391C097",
        "key": "readerMatchValue"
      },
      {
        "label": "Service ID of primary car key",
        "value": "hwpass.stdcarkey.std",
        "key": "ownerPassTypeIdentifier"
      },
      {
        "value": "0000xxxx-0000-1000-8000-00805f9b34fb",
        "key": "bleServiceUuid"
      },
      {
        "value": "xxx",
        "key": "bleTargetPackage"
      },
      {
        "value": "xxx",
        "key": "bleTargetService"
      },
      {
        "value": "Phone",
        "key": "deviceType"
      },
      {
        "value": "Owner",
        "key": "keyHolderType"
      },
      {
        "value": "xxx",
        "key": "vehicleId"
      }
    \]
  },
  "linkDevicePass": {
    "webServiceURL": "https://xxx",
    "nfcType": "1",
    "serialNumber": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "passVersion": "10.0",
    "spPublickey": "xxx",
    "token": "xxx"
  }
}

## Response Parameters

The returned result also contains the information in the preset template.

## Call Example

For details about the complete call example, please refer to the sample code in [Wallet Kit - Card Enabling on the Server](https://gitee.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java).

    public void addStdCarKeyInstance() {
        JSONObject instance = JSONObject.parseObject(ConfigUtil.readFile("StdCarKeyInstance.json"));
        HwWalletObjectUtil.validateInstance(instance);
        String urlSegment = "/v2/key\_stdcar/instance";
        JSONObject responseInstance =
            serverApiService.postToWalletServer(urlSegment, JSONObject.toJSONString(instance));

        if (responseInstance.containsKey("serialNumber")) {
            String serialNumber = responseInstance.getString("serialNumber");
            JweTest test = new JweTest();
            test.generateThinJWEToBindUser(serialNumber);
        }
    }

## Generating JWE Data

Car key cards in HUAWEI Wallet are activated based on the JWE mode. Therefore, after the DK management service successfully applies to the HUAWEI Wallet server for creating a car key, the DK management service generates JWE data based on the **serialNumber** of the created car key and returns the JWE data to the car manufacturer app.

The JWE string contains the JWE encrypted key, initial vector (IV), ciphertext, and signature. The generation process is as follows:

1.  Generate a random content encryption key (CEK).
2.  Encrypt the CEK using the public key provided by the HUAWEI Wallet server with the RSA-OAEP algorithm to generate the JWE encrypted key.
3.  Generate the JWE IV.
4.  Encrypt the plaintext to generate the ciphertext along with a 128-bit authentication tag using the AES GCM algorithm. Encode the preceding generated parts using Base64.
5.  **Signature** is generated by signing the preceding parts using the private key generated in step 4 of [Applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations#li69221528123212).

## Call Example

For details about the complete call example, please refer to the sample code in [Wallet Kit - Card Enabling on the Server](https://gitee.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java).

     public static String generateJwe(String jwePrivateKey, String payload) {
        Map<String, String> jweHeader = getHeader(); 
        String jweHeaderEncode = getEncodeHeader(jweHeader);
        String sessionKey = generateSecureRandomFactor(16);
        String sessionKeyPublicKey = "MIIBojA\*\*\*\*"; // Enter the actual public key value.
        String encryptedKeyEncode = getEncryptedKey(sessionKey, sessionKeyPublicKey);
        byte\[\] iv = AesUtil.getIvByte(12);
        String ivHexStr = new String(Hex.encodeHex(iv, false));
        String ivEncode = Base64.encodeBase64URLSafeString(ivHexStr.getBytes(StandardCharsets.UTF\_8));
        String cipherTextEncode = getCipherText(payload, sessionKey, iv);
        String signature = getSignature(jwePrivateKey, sessionKey, payload, jweHeaderEncode, ivEncode);
        StringBuilder stringBuilder = new StringBuilder().append(jweHeaderEncode)
            .append(".")
            .append(encryptedKeyEncode)
            .append(".")
            .append(ivEncode)
            .append(".")
            .append(cipherTextEncode)
            .append(".")
            .append(signature);
        return stringBuilder.toString();
    }
