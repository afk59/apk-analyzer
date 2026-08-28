# Posting Back the Attribution Result

#### Function

The app attribution result meeting privacy requirements will be posted back to the developer, the winning distribution platform, and the attribution monitoring platform working with the distribution platform.

#### Scenario Description

The attribution result can be posted back only when the following conditions are met:

1.  If the statistical results of the same developer, distribution platform, and marketing task exceed the rough threshold set in the system, the system will return the attribution result.
2.  If the statistical results of the same developer, distribution platform, and marketing task exceed the rough threshold but do not exceed the detailed threshold, the system will return the developer ID and distribution platform ID.
3.  If the statistical results of the same developer, distribution platform, and marketing task exceed the detailed threshold, the system will return the developer ID, marketing task ID, distribution platform ID, and conversion event ID.
4.  When condition 2 or 3 is fulfilled, and the statistical results of the developer, distribution platform, marketing task, and media app reach the threshold for posting back the media app ID, the media app ID will be included in the postback result.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="18.98%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="81.02000000000001%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="18.98%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="81.02000000000001%"><p>Device-side Huawei app attribution service - &gt; distribution platform/developer/attribution monitoring platform</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="18.98%"><p>URL</p></th><td class="cellrowborder" valign="top" width="81.02000000000001%"><p>URL entered by the app ecosystem partner when registering an attribution role on the cloud platform of the app attribution service.</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="18.98%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="81.02000000000001%"><p>Request: Content-Type: application/json</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

#### Request Parameters

**Request Body**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Involved in Signing

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

ad\_tech\_id

 | 

String

 | 

No

 | 

Yes

 | 

ID of the distribution platform that has been successfully attributed. When the distribution platform registers a role with the cloud platform of the app attribution service, this ID is assigned by the app attribution service and is always eight characters long. If the result recipient is the distribution platform, then this ID is the ID of the distribution platform itself.

If the result recipient is an attribution monitoring platform or developer, this ID corresponds to the distribution platform that has been successfully attributed. The list of distribution platforms is specified when the attribution monitoring platform or developer registers conversion events.

 |
| 

campaign\_id

 | 

String

 | 

No

 | 

Yes

 | 

ID of the marketing task that the conversion is attributed to. It is only contained when postback conditions are met.

 |
| 

source\_id

 | 

String

 | 

No

 | 

Yes

 | 

Media app ID, which contains a maximum of 64 characters. It is only contained when postback conditions are met.

 |
| 

destination\_id

 | 

String

 | 

No

 | 

Yes

 | 

Developer's app ID. The value contains a maximum of 64 characters.

NOTE:

For details about how to obtain your app ID, please refer to [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

 |
| 

service\_tag

 | 

String

 | 

No

 | 

No

 | 

Business information that the distribution platform focuses on, such as creatives and assets. The value should not exceed 32 characters.

NOTE:

The app attribution service will add this parameter to a trustlist (for details, please contact Huawei operations staff) and open it to the distribution platform.

 |
| 

business\_scene

 | 

number

 | 

No

 | 

No

 | 

Business scene value, which is contained only when the developer meets the postback conditions.

The value ranges from 0 to 99.

NOTE:

The app attribution service will add this parameter to a trustlist (for details, please contact Huawei operations staff) and open it to developers.

 |
| 

trigger\_data

 | 

number

 | 

No

 | 

Yes

 | 

Conversion event ID.

For [standard conversion events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-trigger-standard), the value ranges from 1 to 200.

For [custom conversion events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-trigger-custom), the value ranges from 501 to 600.

 |
| 

installation\_status

 | 

number

 | 

No

 | 

No

 | 

App installation status.

NOTE:

The app attribution service will add this parameter to a trustlist (for details, please contact Huawei operations staff) and open it to developers.

 |
| 

nonce

 | 

String

 | 

Yes

 | 

Yes

 | 

Random number without hyphens (-), used for signature calculations. Generated by the app attribution service, the value of **nonce** is unique each time the attribution result is posted back.

 |
| 

timestamp

 | 

number

 | 

Yes

 | 

Yes

 | 

Unix timestamp in milliseconds, which is the timestamp when the postback occurs. It is recommended that the difference between the timestamp and the current time be less than or equal to 5 minutes.

 |
| 

signature

 | 

String

 | 

Yes

 | 

No

 | 

Signature. The result recipient must use the [public key](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-receive) provided by the app attribution service to verify the signature. For details, please refer to [Calculation Rule of Signature Verification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-receive#section15571357102111) and [Postback Result Signature Verification Method](#section114341820105218).

 |
| 

transaction\_id

 | 

String

 | 

Yes

 | 

No

 | 

Unique transaction ID for this postback. The result recipient can use this ID to handle the request in an idempotent manner, ensuring that the operation is performed only once, even if the request is received multiple times.

 |

#### Request Example

POST https://xxxxxxxx/attribution/report-attribution
Content-Type: application/json
{
    "ad\_tech\_id":"12345678",
    "campaign\_id":"50",
    "source\_id":"108\*\*\*\*321",
    "destination\_id":"101\*\*\*\*678",
    "trigger\_data":12,
    "nonce":"17aa292c\*\*\*\*4516\*\*\*\*25150\*\*\*\*195",
    "timestamp":167\*\*\*\*380,
    "signature":"MEQCIEQlmZ\*\*\*\*zKBSE8QnhLTIHZZZ\*\*\*\*ZpRqRxHss65Ko\*\*\*\*JgJKjdrWdkL\*\*\*\*juEx2RmFS7da\*\*\*\*ZRVZ8RyMyUXg==",
    "transaction\_id":"aa\*\*\*\*aaaa"
}

#### Response Parameters

**Response Header**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

Content-Type

 | 

String

 | 

Yes

 | 

The fixed value is **application/json; charset=UTF-8**.

 |

**Response Body**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

resultCode

 | 

String

 | 

Yes

 | 

Result returned after the app attribution service parses a response of the **application/json** type. **0** indicates success, while other values indicate failure.

 |
| 

resultDesc

 | 

String

 | 

Yes

 | 

Result description.

 |

#### Response Example

HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "resultCode": "0",
  "resultDesc": "Success."
}

#### Postback Result Signature Verification Method

1.  Import the open-source cryptographic algorithm package [Bouncy Castle](https://www.bouncycastle.org/latest_releases.html) of the latest version to the **pom.xml** file.
    
    <dependency>
      <groupId>org.bouncycastle</groupId>
      <artifactId>bcprov-jdk18on</artifactId>
      <version>${last\_version}</version>
    </dependency>
    <dependency>
      <groupId>commons-codec</groupId>
      <artifactId>commons-codec</artifactId>
      <version>${last\_version}</version>
    </dependency>
    
2.  Use the following code to verify the signature in the postback request:
    
    import org.apache.commons.codec.binary.Base64;
    import org.bouncycastle.jce.provider.BouncyCastleProvider;
    import java.nio.charset.StandardCharsets;
    import java.security.InvalidKeyException;
    import java.security.KeyFactory;
    import java.security.NoSuchAlgorithmException;
    import java.security.PublicKey;
    import java.security.Security;
    import java.security.Signature;
    import java.security.SignatureException;
    import java.security.spec.InvalidKeySpecException;
    import java.security.spec.X509EncodedKeySpec;
    
    /\*\*
     \* Postback result signature verification utility class.
     \* 
     \* @author \*\*\*\*\*\*
     \* @since \*\*\*\*-\*\*-\*\*
     \*/
    public class PostbackResultVerifyUtil {
        private static String publicKey = "MIIBoj\*\*\*\*\*AAE=";
        private static final String RSA\_ALGORITHM = "RSA";
        private static final String SHA256WithRSA\_PSS\_ALGORITHM = "SHA256WithRSA/PSS";
    
        /\*\*
         \* Method of verifying the postback result signature.
         \*
         \* @param content Concatenated fields of the signature.
         \* @param signature Signature in the postback request.
         \* @return Verification result.
         \* @throws NoSuchAlgorithmException NoSuchAlgorithmException
         \* @throws InvalidKeySpecException InvalidKeySpecException
         \* @throws InvalidKeyException InvalidKeyException
         \* @throws SignatureException SignatureException
         \*/
        public boolean verify(String content,String signature)
            throws NoSuchAlgorithmException, InvalidKeySpecException, InvalidKeyException, SignatureException {
            byte\[\] plainContent = content.getBytes(StandardCharsets.UTF\_8);
            byte\[\] signContent = decodeBase64(signature);
            Security.addProvider(new BouncyCastleProvider());
            PublicKey pubKey = getPublicKey(publicKey);
            Signature rsaSignature = Signature.getInstance(SHA256WithRSA\_PSS\_ALGORITHM);
            rsaSignature.initVerify(pubKey);
            rsaSignature.update(plainContent);
            return rsaSignature.verify(signContent);
        }
    
        private PublicKey getPublicKey(String key) throws NoSuchAlgorithmException, InvalidKeySpecException {
            X509EncodedKeySpec keySpec = new X509EncodedKeySpec(decodeBase64(key));
            KeyFactory keyFactory = KeyFactory.getInstance(RSA\_ALGORITHM);
            return keyFactory.generatePublic(keySpec);
        }
    
        private byte\[\] decodeBase64(String base64Str) {
            return Base64.decodeBase64(base64Str.getBytes(StandardCharsets.UTF\_8));
        }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/WjDHV27oRleb6Lg3-ynbxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062504Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEB2CFF57F32426C2B3D405E4F0C3529546678AC002B8E62B631CDF73C38E58E)
    
    In the **verify(String content,String signature)** method that verifies the postback result signature:
    
    **content**: concatenated fields of the signature. For details about the concatenation mode, please refer to [Calculation Rule of Signature Verification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-receive#section15571357102111).
    
    **signature**: signature in the postback request.
