# When and How Can I Use the ID Token?

An ID token is a user identity credential that extends OAuth 2.0 in the [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) protocol.

The ID token is in JWT format, which means:

1\. User identity information is directly encoded within the ID token, eliminating the need for additional requests to retrieve user information.

2\. The ID token carries a digital signature from Account Kit, which can be verified to ensure the token's authenticity and integrity. This confirms that the token has not been altered since it was issued.

#### Use Case

1.  When there is no server and only an app, the authorization code cannot be used to get user information by calling server-side APIs. Instead, extract user information directly from the ID token.
2.  The app has a server and needs to parse the corresponding fields in the ID token on the server side to obtain user information.

#### Parameters

The ID token is in JWT format. The payload contains the following parameters:

| 
Parameter

 | 

Type

 | 

Returned by Default

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

iss

 | 

string

 | 

Yes

 | 

The value is always **https://accounts.huawei.com**.

 |
| 

sub

 | 

string

 | 

Yes

 | 

UnionID of a user. The value of this parameter is the same for a user within all apps of the same developer. For details about the format requirements, please refer to [Formats of OpenID and UnionID](../formats-of-openid-and-unionid/document.md).

 |
| 

aud

 | 

string

 | 

Yes

 | 

Client ID of an app that receives the ID token.

 |
| 

exp

 | 

number

 | 

Yes

 | 

Time when an ID token expires (10 digits).

 |
| 

iat

 | 

number

 | 

Yes

 | 

Time when an ID token is generated (10 digits).

 |
| 

at\_hash

 | 

string

 | 

Yes

 | 

Access token hash value.

 |
| 

azp

 | 

string

 | 

Yes

 | 

Client ID of an app that generates the ID token.

 |
| 

openid

 | 

string

 | 

Yes

 | 

OpenID of a user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](../formats-of-openid-and-unionid/document.md).

 |
| 

nonce

 | 

string

 | 

No

 | 

Random value for replay attack prevention. For details, please refer to the description of the **nonce** field in [LoginWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section42261825935) and [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165).

 |
| 

picture

 | 

string

 | 

No

 | 

Avatar URL. This parameter is returned when the scopes passed to [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) contain **profile**.

 |
| 

display\_name

 | 

string

 | 

No

 | 

Nickname of a HUAWEI ID. If this parameter is not set, the anonymized email address or mobile number is displayed. This parameter is returned in the following scenario:

The scopes passed to [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) contain **profile**.

 |
| 

nickname

 | 

string

 | 

No

 | 

Nickname of a HUAWEI ID. This parameter is returned in the following scenario:

The scopes passed to [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) contain **profile**.

 |

#### Parsing and Verification

## **Parsing and Verification on the Server**

Applicable to: apps with servers deployed.

For an app with its own server, you are advised to parse and verify the ID token on the server. For details, please refer to the Maven project dependency configuration and Java sample code provided below.

Maven project dependencies:

<dependencies>
    <dependency>
        <groupId>com.alibaba.fastjson2</groupId>
        <artifactId>fastjson2</artifactId>
        <version>2.0.51</version> <!--Use the version required by your project.-->
    </dependency>
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk18on</artifactId>
        <version>1.74</version> <!--Use the version required by your project.-->
    </dependency>
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.6</version> <!--Use the version required by your project.-->
    </dependency>
    <dependency>
        <groupId>com.auth0</groupId>
        <artifactId>jwks-rsa</artifactId>
        <version>0.8.2</version> <!--Use the version required by your project.-->
    </dependency>
    <dependency>
        <groupId>com.auth0</groupId>
        <artifactId>java-jwt</artifactId>
        <version>3.8.1</version> <!--Use the version required by your project.-->
    </dependency>
</dependencies>

Java sample code:

import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.JSONObject;
import com.auth0.jwk.InvalidPublicKeyException;
import com.auth0.jwk.Jwk;
import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTDecodeException;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.auth0.jwt.exceptions.TokenExpiredException;
import com.auth0.jwt.interfaces.DecodedJWT;
import org.apache.commons.codec.binary.Base64;
import org.apache.http.HttpEntity;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
import java.security.Security;
import java.security.Signature;
import java.security.interfaces.RSAPublicKey;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class IDTokenParser {
    // Replace it with the client ID of your app.
    private final static String CLIENT\_ID = "123456";
    private final static int MAX\_PUBLIC\_KEY\_SIZE = 4;
    // Cache the JWT public key.
    private final Map<String, RSAPublicKey> keyId2PublicKey = new HashMap<>();
    /\*\*
     \* JSON Web Key (JWK) endpoint, from which you can fetch the JWKs generated within the past two days.
     \* Make sure that the ID token is generated within 24 hours. (The public key will be updated within 24 hours.)
     \*/
    private static final String CERT\_URL = "https://oauth-login.cloud.huawei.com/oauth2/v3/certs";
    // Issuer of the ID token.
    public static final String ID\_TOKEN\_ISSUE = "https://accounts.huawei.com";
    public static final String ALG\_RS256 = "RS256";
    public final static String ALG\_PS256 = "PS256";
    public static void main(String\[\] args) throws Exception {
        // ID token generated based on the value of CLIENT\_ID.
        String idToken = "_<ID Token>_";
        IDTokenParser idTokenParser = new IDTokenParser();
        JSONObject idTokenInfo = idTokenParser.verifyAndParse(idToken);
        // Parse the ID token to obtain necessary data, such as iss.
        String iss = idTokenInfo.getString("iss");
    }
    /\*\*
     \* Verify and parse the ID token.
     \* @param idToken idToken
     \* @return Information contained in the ID token.
     \* @throws Exception
     \*/
    public JSONObject verifyAndParse(String idToken) throws Exception {
        try {
            DecodedJWT decoder = JWT.decode(idToken);
            if (!decoder.getIssuer().equals(ID\_TOKEN\_ISSUE)) {
                // If the issuer verification fails, an exception is thrown. (The exception type can be customized.)
                throw new RuntimeException("issuer no match");
            }
            if (decoder.getAudience().size() > 0) {
                if (!decoder.getAudience().get(0).equals(CLIENT\_ID)) {
                    // If the audience verification fails, an exception is thrown. (The exception type can be customized.)
                    throw new RuntimeException("audience no match");
                }
            }
            // Obtain the algorithm used for signing the ID token.
            String alg = decoder.getAlgorithm();
            if (ALG\_RS256.equals(alg)) {
                Algorithm algorithm = Algorithm.RSA256(getRSAPublicKeyByKid(decoder.getKeyId()), null);
                JWTVerifier verifier = JWT.require(algorithm).build();
                JSONObject jsonObject = JSONObject.parseObject(new String(Base64.decodeBase64(decoder.getPayload())));
                // Verify the signature.
                verifier.verify(decoder);
                jsonObject.put("alg", decoder.getAlgorithm());
                jsonObject.put("typ", decoder.getType());
                jsonObject.put("kid", decoder.getKeyId());
                return jsonObject;
            } else if (ALG\_PS256.equals(alg)) {
                PS256Algorithm algorithm = new PS256Algorithm(getRSAPublicKeyByKid(decoder.getKeyId()));
                boolean verifyResult = algorithm.verify(decoder.getHeader(), decoder.getPayload(),
                    decoder.getSignature());
                if (verifyResult) {
                    JSONObject jsonObject = JSONObject.parseObject(
                        new String(Base64.decodeBase64(decoder.getPayload())));
                    jsonObject.put("alg", decoder.getAlgorithm());
                    jsonObject.put("typ", decoder.getType());
                    jsonObject.put("kid", decoder.getKeyId());
                    return jsonObject;
                }
            }
            return null;
        } catch (JWTDecodeException e) {
            // Failed to parse the ID token. The common cause is that the ID token format is incorrect.
            throw new RuntimeException("ID Token decode failed");
        } catch (TokenExpiredException e) {
            // The ID token has expired.
            throw new RuntimeException("ID Token expired");
        }
    }
    /\*\*
     \* Obtain the public key through kid. Cache the public key. In this example, the map method is used for caching. You can use other suitable methods.
     \* @param keyId  keyId
     \* @return Public key.
     \* @throws InvalidPublicKeyException Exception.
     \*/
    private RSAPublicKey getRSAPublicKeyByKid(String keyId) throws InvalidPublicKeyException {
        if (keyId2PublicKey.get(keyId) != null) {
            return keyId2PublicKey.get(keyId);
        }
        JSONArray keys = getJwks();
        if (keys == null) {
            return null;
        }
        if (keyId2PublicKey.size() > MAX\_PUBLIC\_KEY\_SIZE) {
            keyId2PublicKey.clear();
        }
        for (int i = 0; i < keys.size(); i++) {
            String kid = keys.getJSONObject(i).getString("kid");
            String alg = keys.getJSONObject(i).getString("alg");
            if (ALG\_RS256.equals(alg) || ALG\_PS256.equals(alg)) {
                keyId2PublicKey.put(kid, getRsaPublicKeyByJwk(keys.getJSONObject(i)));
            }
        }
        return keyId2PublicKey.get(keyId);
    }
    /\*\*
     \* Obtain the JWK from https://oauth-login.cloud.huawei.com/oauth2/v3/certs.
     \* The JWK is updated every day. Therefore, it needs to be cached.
     \* @return JSONObject Array of public keys.
     \*/
    private static JSONArray getJwks() {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(CERT\_URL);
        RequestConfig requestConfig = RequestConfig.custom()
            .setConnectTimeout(5000)
            .setConnectionRequestTimeout(5000)
            .setSocketTimeout(5000)
            .build();
        httpGet.setConfig(requestConfig);
        try {
            CloseableHttpResponse response = httpClient.execute(httpGet);
            HttpEntity entity = response.getEntity();
            String result = EntityUtils.toString(entity);
            return JSONObject.parseObject(result).getJSONArray("keys");
        } catch (Exception e) {
            return null;
        } finally {
            if (null != httpClient) {
                try {
                    httpClient.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
    /\*\*
     \* Obtain the public key using JWK.
     \* @return RSAPublicKey Public key.
     \*/
    private static RSAPublicKey getRsaPublicKeyByJwk(JSONObject jwkObject) throws InvalidPublicKeyException {
        Map<String, Object> additionalAttributes = new HashMap<>();
        additionalAttributes.put("n", jwkObject.getString("n"));
        additionalAttributes.put("e", jwkObject.getString("e"));
        List<String> operations = new ArrayList<>();
        Jwk jwk = new Jwk(jwkObject.getString("kid"), jwkObject.getString("kty"), jwkObject.getString("alg"),
            jwkObject.getString("use"), operations, null, null, null, additionalAttributes);
        return (RSAPublicKey) jwk.getPublicKey();
    }
    static class PS256Algorithm {
        private final RSAPublicKey publicKey;
        public PS256Algorithm(RSAPublicKey publicKey) {
            this.publicKey = publicKey;
        }
        public boolean verify(String header, String payload, String signature) throws JWTVerificationException {
            byte\[\] contentBytes = (header + '.' + payload).getBytes(StandardCharsets.UTF\_8);
            byte\[\] signatureBytes = Base64.decodeBase64(signature);
            try {
                Security.addProvider(new BouncyCastleProvider());
                Signature sign = Signature.getInstance("SHA256WithRSA/PSS");
                sign.initVerify(publicKey);
                sign.update(contentBytes);
                return sign.verify(signatureBytes);
            } catch (GeneralSecurityException e) {
                throw new JWTVerificationException("JWT verify failed");
            }
        }
    }
}

## **Parsing and Verification in the App**

Applicable to: apps without servers deployed.

For an app without a server, it obtains the ID token by calling the relevant API of Account Kit and performs local parsing and verification. After the parsing, you can obtain the user information and verify the signature. For details, see the ArkTS sample code below. Pass the ID token obtained by the app to the method for parsing and verifying the ID token, and set **CLIENT\_ID** to the app's actual client ID.

import { buffer } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { http } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

decodeBase64(data: string): string {
  return buffer.from(data, 'base64').toString('utf8');
}
// Parse the ID token and verify it.
decodeIdToken(idToken: string): void {
  const parts = idToken.split('.');
  if (parts.length !== 3) {
    return;
  }
  const idTokenObj: Record<string, Object> = {};
  // ID token header.
  idTokenObj\['header'\] = JSON.parse(this.decodeBase64(parts\[0\]));
  // ID token payload.
  idTokenObj\['payload'\] = JSON.parse(this.decodeBase64(parts\[1\]));
  // ID token signature.
  idTokenObj\['signature'\] = parts\[2\];
  const header: Record<string, string> = idTokenObj\['header'\] as Record<string, string>;
  // Parse data such as nonce from the payload.
  const payLoad: Record<string, string> = idTokenObj\['payload'\] as Record<string, string>;
  const nonce: string = payLoad\['nonce'\];
  // Client ID of the app. Set it to the actual one.
  const CLIENT\_ID: string = '<_App's client ID_\>';
  const ID\_TOKEN\_ISSUE: string = 'https://accounts.huawei.com';
  const iss: string = payLoad\['iss'\];
  const aud: string = payLoad\['aud'\];
  if(iss !== ID\_TOKEN\_ISSUE){
    // If the verification fails, handle the error.
    hilog.error(0x0000, 'testTag', 'Failed to check iss');
    return;
  }
  if(aud !== CLIENT\_ID){
    // If the verification fails, handle the error.
    hilog.error(0x0000, 'testTag', 'Failed to check aud');
    return;
  }
  // Verify the signature.
  this.checkSignature(idToken, header\['kid'\], header\['alg'\]);
}

private stringToUint8Array(str: string): Uint8Array {
  const arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  const tmpUint8Array: Uint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}
// Signature verification method.
private checkSignature(idToken: string, kid: string, alg: string) {
  if (!idToken) {
    return;
  }
  const parts = idToken.split('.');
  if (parts.length !== 3) {
    return;
  }
  const url = 'https://oauth-login.cloud.huawei.com/oauth2/v3/certs';
  // Create an HTTP request. To send this request, the app needs to first request the ohos.permission.INTERNET network permission in the module.json5 file.
  const httpRequest = http.createHttp();
  httpRequest.request(url, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', \`Failed to httpRequest. Code: ${err.code}, message: ${err.message}\`);
      httpRequest.destroy();
      return;
    }
    let nStr = '';
    let eStr = '';
    const keys: object\[\] = JSON.parse(data.result as string)\["keys"\];
    for (let item of keys) {
      if (kid === item\['kid'\]) {
        nStr = item\['n'\];
        eStr = item\['e'\];
        break;
      }
    }
    const nBigInt = '0x' + buffer.from(nStr, "base64url").toString('hex');
    const eBigInt = '0x' + buffer.from(eStr, "base64url").toString('hex');
    const dsaCommonSpec: cryptoFramework.RSACommonParamsSpec = {
      algName: "RSA",
      specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
      n: BigInt(nBigInt),
    }
    const rsaKeyPairSpec: cryptoFramework.RSAPubKeySpec = {
      algName: "RSA",
      specType: cryptoFramework.AsyKeySpecType.PUBLIC\_KEY\_SPEC,
      params: dsaCommonSpec,
      pk: BigInt(eBigInt),
    }
    const asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(rsaKeyPairSpec);
    asyKeyGeneratorBySpec.generatePubKey(async (error, publicKey) => {
      if (error) {
        return;
      }
      if (publicKey === null) {
        return;
      }
      const idTokenSign = parts\[2\];
      const idTokenSignArr: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(idTokenSign, "base64url").buffer) };
      const idToken = parts\[0\] + '.' + parts\[1\];
      const idTokenArr: cryptoFramework.DataBlob = { data: this.stringToUint8Array(idToken) };
      const verifier = alg === 'PS256' ? cryptoFramework.createVerify("RSA2048|PSS|SHA256|MGF1\_SHA256")
        : cryptoFramework.createVerify("RSA2048|PKCS1|SHA256");
      verifier.init(publicKey, (initErr, result) => {
        verifier.verify(idTokenArr, idTokenSignArr, (verifyErr, data) => {
          // Return the signature verification result. If the result is **true**, the signature verification is successful.
          hilog.info(0x0000, 'testTag', 'verify result is: %{public}s', data);
        });
      });
    })
    httpRequest.destroy();
  });
}
