# Generating a Token for a Server-Side API Call

The **Authorization** header of a request to a server-side API must contain a token in JWT format for authentication. JWT is an open standard (RFC 7519) that defines a secure method for transmitting information. For details, please refer to [jwt.io](https://jwt.io/). You can use the private key downloaded from [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) to generate a token in JWT format. For details about how to generate and download a private key, please refer to [Configuring the Key](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section12796923310). To get a token in JWT format, create the following items step by step:

1.  JWT header
2.  JWT payload
3.  Token in JWT format

#### Creating a JWT Header

Below lists the parameters of a JWT header.

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

alg

 | 

Yes

 | 

String

 | 

Algorithm type. The value is always **ES256**.

 |
| 

typ

 | 

Yes

 | 

String

 | 

Token type. The value is always **JWT**.

 |
| 

kid

 | 

Yes

 | 

String

 | 

Key ID. For details about how to obtain the key ID, please refer to [Configuring the Key](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section12796923310). If there are multiple keys, use the key ID of the same private key that signs the JWT.

 |

#### Creating JWT Payload

The JWT payload contains some key information for accessing the server-side APIs, such as the key issuer ID, JWT issuance time, and JWT expiration time. Below lists the parameters of JWT payload.

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

Key issuer ID. For details about how to obtain the ID, please refer to [Configuring the Key](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section12796923310).

 |
| 

aud

 | 

Yes

 | 

String

 | 

Expected receiver of the JWT. The value is fixed at **iap-v1**.

 |
| 

iat

 | 

Yes

 | 

Long

 | 

Time when the JWT is issued. The value is a UTC timestamp, in seconds.

 |
| 

exp

 | 

Yes

 | 

Long

 | 

Time when the JWT expires. The value is a UTC timestamp, in seconds.

**exp-iat** indicates the validity period of the JWT, which cannot exceed one hour.

 |
| 

aid

 | 

Yes

 | 

String

 | 

App ID. For details about how to obtain the app ID, please refer to [Configuring App Identity Information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-app-identity-info).

 |
| 

digest

 | 

Yes

 | 

String

 | 

Hash value of the request body (JSON character string), which is used to verify the integrity of the body. The algorithm is SHA-256.

NOTE:

If the request body is empty, pass the hash value of an empty string ("").

 |

#### Creating a Token in JWT Format

Use the algorithm (ES256) specified in the header and the private key associated with the key ID to generate a JWT. You can use various open-source libraries to create a token in JWT format. For details, please refer to [jwt.io](https://jwt.io/).

## Sample Code

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/fOvNChBRQMelIyP84iEB7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=014AB808EC9C8980655692331F2CDB7F104285A9779406B30CF9DDD9F234CABC)

The following sample code uses Java as an example. You can view the sample code of Python, PHP, JavaScript, and Golang by switching the code branch in **[IAP Kit-Sample-ServerDemo](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-serverdemo/blob/Java/README_en.md)**.

**Java** 
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyFactory;
import java.security.interfaces.ECPrivateKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.time.Duration;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.codec.digest.DigestUtils;

public class JWTGenerator {
    /\*\*
     \* Private key file path.
     \* For key generation and download, please refer to [Configuring Keys](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section12796923310).
     \*/
    private static final String JWT\_PRI\_KEY\_PATH = "/path/to/key/priKey.p8"; // TODO: Need to replace it with the actual value.

    /\*\*
     \* JWT validity period, which is a UTC timestamp in seconds. The validity period cannot exceed 1 hour.
     \*/
    private static final long ACTIVE\_TIME\_SECOND = 3600;  // TODO: Need to replace it with the actual value.

    private static final Map<String, Object> JWT\_HEADER = new HashMap<>();

    private static final Map<String, Object> JWT\_PAYLOAD = new HashMap<>();

    static {
        // Algorithm type. The value is always ES256.
        JWT\_HEADER.put("alg", "ES256");
        // Token type. The value is always JWT.
        JWT\_HEADER.put("typ", "JWT");
        // Key ID.
        JWT\_HEADER.put("kid", "Key ID");  // TODO: Need to replace it with the actual value.

        // Key issuer ID.
        JWT\_PAYLOAD.put("iss", "Issuer ID");  // TODO: Need to replace it with the actual value.
        // Expected receiver of the JWT. The value is fixed at iap-v1.
        JWT\_PAYLOAD.put("aud", "iap-v1");
        // Time when the JWT is issued. The value is a UTC timestamp, in seconds.
        // Re-put the value in the genJwt method.
        JWT\_PAYLOAD.put("iat", 0);
        // Time when the JWT expires. The value is a UTC timestamp, in seconds. exp-iat indicates the validity period of the JWT, which cannot exceed one hour.
        // Re-put the value in the genJwt method.
        JWT\_PAYLOAD.put("exp", 0);
        // App ID.
        JWT\_PAYLOAD.put("aid", "App ID");  // TODO: Need to replace it with the actual value.
        // Hash value of the request body (JSON character string), which is used to verify the integrity of the body. The algorithm is SHA-256.
        JWT\_PAYLOAD.put("digest", "");
    }

    public static String genJwt(String bodyStr) throws Exception {
        try {
            // Fetch the Private Key Content in PEM format.
            Path filePath = Paths.get(JWT\_PRI\_KEY\_PATH);
            String fileString = new String(Files.readAllBytes(filePath), StandardCharsets.UTF\_8);
            String privateKey = fileString.replace("-----BEGIN PRIVATE KEY-----", "")
                .replaceAll("\\\\R+", "")
                .replace("-----END PRIVATE KEY-----", "");
            KeyFactory keyFactory = KeyFactory.getInstance("EC");
            byte\[\] privateKeyBytes = Base64.getDecoder().decode(privateKey);
            PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(privateKeyBytes);
            ECPrivateKey ecPrivateKey = (ECPrivateKey) keyFactory.generatePrivate(keySpec);
            Map<String, Object> jwtPayload = new HashMap<>(JWT\_PAYLOAD);
            long signTime = System.currentTimeMillis() / Duration.ofSeconds(1).toMillis();
            String digest = DigestUtils.sha256Hex(bodyStr);
            jwtPayload.put("iat", signTime);
            jwtPayload.put("exp", signTime + ACTIVE\_TIME\_SECOND);
            jwtPayload.put("digest", digest);
            return JWT.create().withHeader(JWT\_HEADER).withPayload(jwtPayload).sign(Algorithm.ECDSA256(ecPrivateKey));
        } catch (Exception e) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception(e);
        }
    }
}

POM file:

<dependency>
    <groupId>com.auth0</groupId>
    <artifactId>java-jwt</artifactId>
    <version>4.4.0</version>
</dependency>

#### Authorization Description

When a server API is called, the request header uses **Authorization: Bearer <JWT token>** to pass authentication information. Here is an example:

Authorization: Bearer eyJhbGciOi---xxx.eyJpc3MiOm---xxx.WFquGEx5gf---xxx
