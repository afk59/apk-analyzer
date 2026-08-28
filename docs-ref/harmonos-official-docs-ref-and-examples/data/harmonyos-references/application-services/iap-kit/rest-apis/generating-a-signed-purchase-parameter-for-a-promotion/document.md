# Generating a Signed Purchase Parameter for a Promotion

For a promotion, you must provide a JWT-formatted **jwsRepresentation** parameter that includes details about the purchase, including the product and promotional activity. JWT is an open standard (RFC 7519) that defines a secure method for transmitting information. For details, please refer to [jwt.io](https://jwt.io/). You can use the private key downloaded from [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) to generate a token in JWT format. For details about how to generate and download a private key, please refer to [Configuring the Key](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section12796923310). To create a signed purchase parameter in JWT format, perform the following steps:

1.  Create a JWT header.
2.  Create JWT payload.
3.  Create a signature in JWT format.

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

Expected receiver of the JWT. Ensure that the JWT is for the app itself. The value is always **iap-v1**.

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

data

 | 

Yes

 | 

String

 | 

A JSON string structured as [PurchaseReservedInfo](../data-types/document.md#section13876141516408), providing extra promotion information.

 |

#### Creating a Signature in JWT Format

Use the algorithm (ES256) specified in the header and the private key associated with the key ID to generate a JWT. You can use various open-source libraries to create a token in JWT format. For details, please refer to [jwt.io](https://jwt.io/).

## Sample Code

**Java** 
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;

import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.interfaces.ECPrivateKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Base64;
import java.util.Map;

public class JwsRepresentationGenerator {
    public static String createJwsRepresentation(String signingKey, Map<String, Object> jwtHeader,
        Map<String, Object> jwtPayload) {
        try {
            // Configure a key and download the private key file in AppGallery Connect.
            byte\[\] derEncodedSigningKey = Base64.getDecoder().decode(signingKey);
            KeyFactory keyFactory = KeyFactory.getInstance("EC");
            PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(derEncodedSigningKey);
            ECPrivateKey ecPrivateKey = (ECPrivateKey) keyFactory.generatePrivate(keySpec);
            return JWT.create().withHeader(jwtHeader).withPayload(jwtPayload).sign(Algorithm.ECDSA256(ecPrivateKey));
        } catch (NoSuchAlgorithmException | InvalidKeySpecException e) {
            // TODO: Need to replace it with the actual business logic.
            throw new RuntimeException(e);
        }
    }
}
