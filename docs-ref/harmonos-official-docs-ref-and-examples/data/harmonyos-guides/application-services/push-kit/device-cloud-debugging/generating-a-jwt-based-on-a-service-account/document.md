# Generating a JWT Based on a Service Account

#### Overview

A service account is used for API authentication between servers. You can create a service account on the [API Console](https://developer.huawei.com/consumer/en/console/api/myApi) of HUAWEI Developers, and then generate a JSON Web Token (JWT) in your app based on the public and private keys returned. With this JWT, your app can call Huawei public APIs that support service account-based authentication.

The JWT generated from a service account is a JWT string, which consists of the following parts:

-   Header
-   Payload
-   Signature

The three parts are concatenated through dots (.). You can obtain the signature by concatenating the header and payload and then signing the concatenated string using the SHA256withRSA/PSS algorithm.

**Example**

eyJra\*\*\*\*\*JjNjBjMXXX.
eyJhd\*\*\*\*\*JodHRXXX.
BRNss\*\*\*\*\*7az5oU7-Zp5g9X2WJVXXX

For more about JWT, please refer to [Introduction to JSON Web Tokens](https://jwt.io/introduction/).

#### Development Procedure

1.  Create the key file of a service account.
    
    You need to create and download the key file of a service account to call Push Kit APIs on [API Console](https://developer.huawei.com/consumer/en/console/api/myApi). The following figure shows the creation entry. You need to select your project and create a service account key. For details, please refer to [API Console Operation Guide - Creating a Service Account Key](https://developer.huawei.com/consumer/en/doc/start/api-0000001062522591#section2080424916353).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Db4clpJrRkyUwNosS0Ak_w/en-us_image_0000002492787672.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAE24EC9E2B4D0DFD6D61DF6149B67D683B8F9D594C62BB9F80BCD834F9DF204 "Click to enlarge")
    
    The following is an example of a key file (with key data masked):
    
    {
        "project\_id": "\*\*\*\*\*",
        "key\_id": "\*\*\*\*\*",
        "private\_key": "-----BEGIN PRIVATE KEY-----\\nMIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCKw6kJKtCh7qmMvp1u1dI27z2TKZrPOzHbQaXO/Eez0AWZ2EN+ouF496R3pfo7fQXC1XOT/YTbVC4DNZwWSMA54fu3/AOCY9Zzyi46OK\*\*\*\*\*==\\n-----END PRIVATE KEY-----\\n",
        "sub\_account": "\*\*\*\*\*",
        "auth\_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/authorize",
        "token\_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
        "auth\_provider\_cert\_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/certs",
        "client\_cert\_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/x509?client\_id="
    }
    
2.  Ensure that the value of **project\_id** in the key file is the same as the ID of the project to which your app belongs.
    
    To check the actual project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/HLaMHRtxSde8Bu4ilRH3-w/en-us_image_0000002525227785.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1EAF8409C3BC02BABCEB2879BC6FD0165371B875D82EEB30E668745FB173B3E "Click to enlarge")
    
3.  Generate the header in a JWT string.
    
    Generate a JSON body and encode it using Base64 to obtain the header. In the JSON body, the value of **kid** is the same as the value of **key\_id** in the service account key file.
    
    Example
    
    {
      "kid": "\*\*\*\*\*",
      "typ": "JWT",
      "alg": "PS256"
    }
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    kid
    
     | 
    
    The value is the same as that of the **key\_id** field in the key file.
    
     |
    | 
    
    typ
    
     | 
    
    Data type. The value is always **JWT**.
    
     |
    | 
    
    alg
    
     | 
    
    Algorithm type. The value is always **PS256**.
    
     |
    
4.  Generate the payload in a JWT string.
    
    Generate a JSON body and encode it using Base64 to obtain the payload. In the JSON body, the value of **iss** is the same as the value of **sub\_account** in the service account key file.
    
    **Example**
    
    {
      "aud": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
      "iss": "\*\*\*\*\*",
      "exp": 1581410664,
      "iat": 1581407064
    }
    
    | 
    Field
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    iss
    
     | 
    
    Data generator ID. The value is the same as that of the **sub\_account** field in the key file.
    
     |
    | 
    
    aud
    
     | 
    
    The value is always **https://oauth-login.cloud.huawei.com/oauth2/v3/token**.
    
     |
    | 
    
    iat
    
     | 
    
    UTC timestamp when a JWT string is signed. The value is the number of seconds counting from 1970-01-01 00:00:00 (UTC) to the time when the JWT string is signed.
    
     |
    | 
    
    exp
    
     | 
    
    UTC timestamp when a JWT string expires. The value is 3600 seconds later than that of **iat**.
    
     |
    
5.  Generate a JWT.
    
    Use a dot (.) to concatenate the header and payload generated after Base64 encoding, and use **private\_key** (kept by yourself not Huawei) in the key file and the SHA256withRSA/PSS algorithm to sign the concatenated string. Then, a signature is generated.
    
    By now, the required parts of the JWT string have been prepared.
    

#### Calling a Push Kit REST API

When your app calls a Push Kit REST API, you need to add the JWT to the **Authorization** header of the API call request. Call the Push Kit REST API using the URL of the V3 version.

**Example**

POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:0

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/-QwdFlTlT6OqpX3m_vv1Gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=610D87867AFE92E177AD2196CBE3FD5E420F0FFB531716D81ED81320BFC065A7)

The value of **Authorization** is **Bearer** followed by a space character and then the obtained authentication information.

API request URL version: Call the Push Kit REST API using the URL of the V3 version.

In the [request body](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) of a scenario-specific message, if the API request URL version is V3 (https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send), the message can be pushed to HarmonyOS Next/5.x and later versions. If the API request URL version is V2 (https://push-api.cloud.huawei.com/v2/\[projectId\]/messages:send), the message can be pushed only to HarmonyOS 3.x/4.x.

#### Sample Code

You can generate a JWT from a service account by referring to the Java sample code. Modify parameters based on comments in the sample code before running it.

If you do not use Java, select the corresponding [JWT open-source component](https://jwt.io/libraries) for development.

Perform the following steps to generate an authentication token:

1.  Create and download the service account key file (JSON file) that has been generated for Push Kit in step 1 in [Development Procedure](#section16173145352) from the [API Console](https://developer.huawei.com/consumer/en/console/api/myApi) of HUAWEI Developers. The file format is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Q73vDNZ4TL6VjuORFZdM3g/en-us_image_0000002402305789.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=180C957AF6B427E023B0C7001D540464CA5B1FF2EDCB2733F5A2CE6FA50D81F6)
    
2.  Copy the preceding JSON file to your project and parse the file by referring to the following code (**private.json** used as an example):

**Java**
/\* The recommended Java version is java8. The Maven dependency is as follows:
  <dependency>
   <groupId>com.fasterxml.jackson.core</groupId>
   <artifactId>jackson-databind</artifactId>
   <version>2.16.2</version>
  </dependency>
  <dependency>
   <groupId>io.jsonwebtoken</groupId>
   <artifactId>jjwt-api</artifactId>
   <version>0.11.5</version>
  </dependency>
  <dependency>
   <groupId>io.jsonwebtoken</groupId>
   <artifactId>jjwt-impl</artifactId>
   <version>0.11.5</version>
   <scope>runtime</scope>
  </dependency>
  <dependency>
   <groupId>io.jsonwebtoken</groupId>
   <artifactId>jjwt-jackson</artifactId>
   <version>0.11.5</version>
   <scope>runtime</scope>
  </dependency>
  <dependency>
   <groupId>org.bouncycastle</groupId>
   <artifactId>bcprov-jdk18on</artifactId>
   <version>1.78.1</version>
   <scope>runtime</scope>
  </dependency>
\*/

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import io.jsonwebtoken.\*;
import io.jsonwebtoken.lang.Maps;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.interfaces.RSAPrivateKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Base64;
import java.util.Map;

public class JsonWebTokenFactory {

    // Store the public address in the configuration file or database during development.
    private static final String AUD = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";

    public static String createJwt() throws NoSuchAlgorithmException, InvalidKeySpecException, IOException, NullPointerException {
        // Read the configuration file.
        ObjectMapper mapper = new ObjectMapper();
        // Save the **private.json** file in the **src/main/resources** directory of the project.
        URL url = JsonWebTokenFactory.class.getClassLoader().getResource("private.json");
        if (url == null) {
            throw new NullPointerException("File not exist");
        }
        JsonNode rootNode = mapper.readTree(new File(url.getPath()));

        RSAPrivateKey privateKey = (RSAPrivateKey) generatePrivateKey(rootNode.get("private\_key").asText()
                .replace("-----BEGIN PRIVATE KEY-----", "")
                .replace("-----END PRIVATE KEY-----", "")
                .replaceAll("\\\\s", ""));
        long iat = System.currentTimeMillis() / 1000;
        long exp = iat + 3600;

        Map<String, Object> header = Maps.<String, Object>of(JwsHeader.KEY\_ID, rootNode.get("key\_id").asText())
                .and(JwsHeader.TYPE, JwsHeader.JWT\_TYPE)
                .and(JwsHeader.ALGORITHM, SignatureAlgorithm.PS256.getValue())
                .build();

        Map<String, Object> payload = Maps.<String, Object>of(Claims.ISSUER, rootNode.get("sub\_account").asText())
                .and(Claims.ISSUED\_AT, iat)
                .and(Claims.EXPIRATION, exp)
                .and(Claims.AUDIENCE, AUD)
                .build();

        return Jwts.builder()
                .setHeader(header)
                .setPayload(new ObjectMapper().writeValueAsString(payload))
                .signWith(privateKey, SignatureAlgorithm.PS256)
                .compact();
    }

    private static PrivateKey generatePrivateKey(String base64Key) throws NoSuchAlgorithmException, InvalidKeySpecException {
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(Base64.getDecoder().decode(base64Key.getBytes(StandardCharsets.UTF\_8)));
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePrivate(keySpec);
    }

    public static void main(String\[\] args) {
        try {
            // Obtain the JWT.
            String jwt = createJwt();
        } catch (NoSuchAlgorithmException e) {
            // Exception handling process 1.
        } catch (InvalidKeySpecException e) {
            // Exception handling process 2.
        } catch (IOException e) {
            // Exception handling process 3.
        } catch (NullPointerException e) {
            // Exception handling process 4.
        }
    }
}

**Node.js**
// Configure the dependency: npm i jsonwebtoken
const jwt = require('jsonwebtoken');
const fs = require('fs');
let privateJson;
try {
  // Change the first parameter in **readFileSync** to the actual path of **private.json**.
  const data = fs.readFileSync('private.json', 'utf8');
  privateJson = JSON.parse(data);
// Custom header.
  const header = {
  alg: 'PS256', // The PS256 algorithm is recommended.
    kid: privateJson?.key\_id,
  typ: 'JWT'    // The type is JWT.
  };
// Create a JWT payload.
  const payload = {
    iss: privateJson?.sub\_account,
    aud: 'https://oauth-login.cloud.huawei.com/oauth2/v3/token', // Store the public address in the configuration file or database during development.
    iat: Math.floor(Date.now() / 1000),
    exp: Math.floor(Date.now() / 1000) + 3600
  };
  const private\_key = privateJson?.private\_key;
  // Replace **\\\\n** in the string with **\\n**, and split the string by lines and convert them into an array.
  const lines = private\_key.replace(/\\\\n/g, '\\n').split('\\n');
  // Extract the first three lines.
  const firstThreeLines = lines.slice(0, 3);
  // Combine the extracted lines into a three-line string.
  const PRIVATE\_KEY = firstThreeLines.join('\\n');
  // Obtain the JWT.
  const token = jwt.sign(payload, PRIVATE\_KEY, { algorithm: 'PS256', header: header });
} catch (error) {
  console.error("File processing error:", error);
}

**Go**
// Dependency: go get github.com/golang-jwt/jwt/v5

package main

import (
	"encoding/json"
	"encoding/pem"
	"errors"
	"fmt"
	"github.com/golang-jwt/jwt/v5"
	"log"
	"os"
	"strings"
	"time"
)

type ServiceAccountKey struct {
	KeyID      string \`json:"key\_id"\`
	SubAccount string \`json:"sub\_account"\`
	PrivateKey string \`json:"private\_key"\`
}

func main() {
	// Replace it with the actual JSON file path. In this example, the JSON file is at the same directory level as the sample code.
	signedToken, err := generateJWTToken("private.json")
	if err != nil {
		log.Fatalf("Failed to generate JWT token: %v", err)
	}

	// **signedToken** indicates the authentication token. It is passed in the **Authorization** header of a Push Kit REST API request for authentication.
	sendMessage(signedToken)
}

func sendMessage(token string) {
	// Implement the service process by yourself.
}

func generateJWTToken(keyFile string) (string, error) {
	saKey, err := loadServiceAccountKey(keyFile)
	if err != nil {
		return "", err
	}

	formattedPrivateKey, err := formatPrivateKey(saKey.PrivateKey)
	if err != nil {
		return "", err
	}

	privateKey, err := jwt.ParseRSAPrivateKeyFromPEM(\[\]byte(formattedPrivateKey))
	if err != nil {
		return "", fmt.Errorf("failed to parse private key: %w", err)
	}

	token, err := buildJWTToken(saKey.KeyID, saKey.SubAccount)
	if err != nil {
		return "", err
	}

	return token.SignedString(privateKey)
}

// Call **buildJWTToken** to build a JWT object.
func buildJWTToken(keyID, subAccount string) (\*jwt.Token, error) {
	now := time.Now().UTC()
	iat := now.Unix()
	exp := iat + 3600 // Token expiration time: one hour later

	claims := jwt.MapClaims{
		// Store the public address in the configuration file or database during development.
		"aud": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
		"iss": subAccount,
		"exp": exp,
		"iat": iat,
	}

	token := jwt.NewWithClaims(jwt.SigningMethodPS256, claims)

	// Set the header.
	token.Header\["kid"\] = keyID
	token.Header\["typ"\] = "JWT"
	token.Header\["alg"\] = "PS256"

	return token, nil
}

// **loadServiceAccountKey** loads a service account key from the JSON file.
func loadServiceAccountKey(filename string) (\*ServiceAccountKey, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil, fmt.Errorf("failed to read key file: %w", err)
	}

	var saKey ServiceAccountKey
	if err := json.Unmarshal(data, &saKey); err != nil {
		return nil, fmt.Errorf("failed to parse key file: %w", err)
	}

	if saKey.KeyID == "" || saKey.SubAccount == "" || saKey.PrivateKey == "" {
		return nil, errors.New("invalid service account key file: missing required fields")
	}

	return &saKey, nil
}

// The **formatPrivateKey** is in PEM format.
func formatPrivateKey(privateKeyStr string) (string, error) {
	trimmed := strings.TrimSpace(privateKeyStr)

	// If the private key is already in PEM format, it is returned directly.
	if strings.HasPrefix(trimmed, "-----BEGIN PRIVATE KEY-----") &&
		strings.HasSuffix(trimmed, "-----END PRIVATE KEY-----") {
		return trimmed, nil
	}

	block, \_ := pem.Decode(\[\]byte(trimmed))
	if block == nil {
		return "", errors.New("failed to decode PEM block")
	}

	pemBytes := pem.EncodeToMemory(block)
	if pemBytes == nil {
		return "", errors.New("failed to encode private key to PEM format")
	}

	return string(pemBytes), nil
}

**Python**
# Dependency: pip install PyJWT cryptography

import jwt
import json
import time
from cryptography.hazmat.primitives import serialization

def load\_private\_key\_from\_json(json\_file\_path):
    """
     Load private key information from a JSON file.
    :param json\_file\_path: JSON file path.
    :return: (key\_id, sub\_account, private\_key\_pem)
    """
    with open(json\_file\_path, 'r') as f:
        data = json.load(f)

    # Obtain the values of **kid** and **iss**.
    key\_id = data.get('key\_id')
    sub\_account = data.get('sub\_account')

    # Convert the private key to PEM format.
    private\_key\_str = data.get('private\_key')
    private\_key\_pem = serialization.load\_pem\_private\_key(
        private\_key\_str.encode(),
        password=None
    )

    return key\_id, sub\_account, private\_key\_pem

def generate\_jwt\_token(json\_file\_path):
    # Load information from a JSON file.
    kid, iss, private\_key = load\_private\_key\_from\_json(json\_file\_path)

    # Current time and expiration time. (Fixed values are used in the example. Calculate them based on the actual situation.)
    iat = int(time.time())
    exp = iat + 3600

    # Construct a header.
    header = {
        "kid": kid,
        "typ": "JWT",
        "alg": "PS256"
    }

    # Construct a payload.
    payload = {
        # Store the public address in the configuration file or database during development.
        "aud": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
        "iss": iss,
        "exp": exp,
        "iat": iat
    }

    # Generate a JWT.
    token = jwt.encode(
        payload=payload,
        key=private\_key,
        algorithm='PS256',
        headers=header
    )

    return token

def send\_message(jwt\_token):
    # Implement the service process by yourself.
    pass

if \_\_name\_\_ == "\_\_main\_\_":
    json\_file = "private.json"  # Replace it with your actual JSON file path. In this example, the JSON file is at the same directory level as the sample code.

    try:
        # **jwt\_token** indicates the authentication token. It is passed in the **Authorization** header of a Push Kit REST API request for authentication.
        jwt\_token = generate\_jwt\_token(json\_file)
        send\_message(jwt\_token)
    except Exception as e:
        print(f"Error generating JWT token: {str(e)}")

**PHP**
<?php
// Dependency: composer require lcobucci/jwt:^5.4.2
// Dependency: composer require lcobucci/jwt-rsassa-pss
// php: ~8.2.0 || ~8.3.0 || ~8.4.0
require 'vendor/autoload.php';

use Lcobucci\\JWT\\Configuration;
use Lcobucci\\JWT\\Signer\\RsaPss\\Sha256;
use Lcobucci\\JWT\\Signer\\Key\\InMemory;

class ServiceAccount
{
    public string $keyId;
    public string $subAccount;
    public string $privateKey;
    public string $tokenURI;

    public function \_\_construct(string $keyId, string $subAccount, string $privateKey, string $tokenURI)
    {
        $this->keyId = $keyId;
        $this->subAccount = $subAccount;
        $this->privateKey = $privateKey;
        $this->tokenURI = $tokenURI;
    }
}

function loadServiceAccount(string $filePath): ServiceAccount
{
    if (!file\_exists($filePath)) {
        throw new RuntimeException("The configuration file does not exist: $filePath");
    }

    $json = file\_get\_contents($filePath);
    $config = json\_decode($json, true);
    if (json\_last\_error() !== JSON\_ERROR\_NONE) {
        throw new RuntimeException("JSON parsing error: " . json\_last\_error\_msg());
    }

    // Verify required fields.
    $requiredKeys = \['key\_id', 'sub\_account', 'private\_key', 'token\_uri'\];
    foreach ($requiredKeys as $key) {
        if (!isset($config\[$key\])) {
            throw new RuntimeException("The required field does not exist: $key");
        }
    }

    // Process the newline characters in the private key.
    $privateKey = str\_replace('\\n', "\\n", $config\['private\_key'\]);

    return new ServiceAccount(
        $config\['key\_id'\],
        $config\['sub\_account'\],
        $privateKey,
        $config\['token\_uri'\]
    );
}

function sendMessage()
{
    // Implement the service process by yourself.
}

function generateJWTToken(ServiceAccount $serviceAccount)
{
    $now = new DateTimeImmutable();
    $expire = $now->modify("+3600 seconds");

    $configuration = Configuration::forSymmetricSigner(
        new Sha256(),
        InMemory::plainText($serviceAccount->privateKey)
    );

    return $configuration->builder()
        ->withHeader('alg', 'PS256') // Specify the PS256 algorithm.
        ->withHeader('typ', 'JWT')   // JWT type.
        ->withHeader('kid', $serviceAccount->keyId) // Key ID.
        ->issuedBy($serviceAccount->subAccount) // iss
        ->permittedFor($serviceAccount->tokenURI) // aud
        ->issuedAt($now) // iat
        ->expiresAt($expire) // exp
        ->getToken($configuration->signer(), $configuration->signingKey())
        ->toString();
}

function main()
{
    try {
        // Replace it with the actual JSON file path. In this example, the JSON file is at the same directory level as the sample code.
        $filePath = 'private.json';
        $serviceAccount = loadServiceAccount($filePath);
        $signedToken = generateJWTToken($serviceAccount);

        // **signedToken** indicates the authentication token. It is passed in the **Authorization** header of a Push Kit REST API request for authentication.
        sendMessage($signedToken);
    } catch (Exception $e) {
        error\_log("Error: " . $e->getMessage());
        exit(1);
    }
}

main();
?>
