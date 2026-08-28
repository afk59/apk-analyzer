# Disassociating an Account

#### Function

This API is used to report the result of disassociating an official game account from **teamPlayerId** to the Huawei game server.

#### Scene Description

When a player signs in to your game with a HUAWEI ID, your game needs to associate the official game account with **teamPlayerId** and report the association result to the Huawei game server. If the official game account needs to be disassociated from **teamPlayerId**, the disassociation result needs to be reported to Huawei. In this case, the game can call the [unbindPlayer](../../arkts-apis/gameplayer-basic-game-service/document.md#section57861515615) API of Game Service Kit to report the result, and the game server can call the API for disassociating an account to achieve this.

#### API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="16.74%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="16.74%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Your server -&gt; Huawei game server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="16.74%"><p>API URL</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="16.74%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Request: Content-Type: application/x-www-form-urlencoded (form mode)</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

#### Request Parameters

**Body parameters**

| 
**Parameter**

 | 

**Mandatory**

 | 

**Type**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

method

 | 

Yes

 | 

String

 | 

This parameter must be set to **external.hms.gs.player.unbindPlayer**. The value contains a maximum of 64 characters.

 |
| 

appId

 | 

No

 | 

String

 | 

[App ID of a game in AppGallery Connect](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569). The value contains a maximum of 32 characters. This parameter is mandatory if the association type of the game level is disassociated.

 |
| 

cpId

 | 

Yes

 | 

String

 | 

[Developer ID in AppGallery Connect](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569). The value contains a maximum of 32 characters.

 |
| 

teamPlayerId

 | 

Yes

 | 

String

 | 

Player ID in the game for HarmonyOS 5.0 and later, which can be obtained through the [unionLogin](../../arkts-apis/gameplayer-basic-game-service/document.md#section157848375136) API. The value can contain a maximum of 256 characters.

 |
| 

ts

 | 

Yes

 | 

Long

 | 

Timestamp of the current time, which is the number of milliseconds between the current time and 00:00:00 on January 1, 1970 (GMT).

 |
| 

sign

 | 

Yes

 | 

String

 | 

Signature string used by the Huawei game server to verify request parameters. The value contains a maximum of 1024 characters.

To prevent its requests from being tampered with, the game needs to generate a signature string based on [Signature Mechanism](#section455238132914). After receiving a request, the Huawei server verifies the signature string and performs subsequent processing only after the signature verification succeeds. Otherwise, the server returns an error code. All body parameters except **sign** and **method** in the request are used for signing.

 |

#### Request Example

POST /gameservice/api/gbClientApi
Host: jos-open-api.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded
// **The values of all request parameters** must be URL-encoded before being concatenated.
method=external.hms.gs.player.unbindPlayer&appId=135\*\*\*568&cpId=123\*\*\*21f&teamPlayerId=\*\*\*\*\*\*&ts=1670841860308&sign=\*\*\*\*\*\*\*\*\*\*\*\*\*\*

#### Response Parameters

| 
**Parameter**

 | 

**Mandatory**

 | 

**Type**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

rtnCode

 | 

Yes

 | 

int

 | 

Code returned by the server.

-   **\-1**: Response failed.

-   **0**: Disassociation succeeded.
-   **1**: Signature verification failed.
-   **3001**: Invalid parameter.
-   **2031002**: The player account information is incorrect.
-   **2031006**: The game information is incorrect.
-   **2031007**: The Huawei player account has been associated with another game player account.

 |
| 

errMsg

 | 

No

 | 

String

 | 

Error message.

 |

#### Response Example

HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
    "rtnCode":0
}

#### Signing Mechanism

To ensure HTTPS transmission security and prevent request parameters from being tampered with, an app must include a signature string of the request parameters for calling the API. The signature string is used by the Huawei server to verify the request parameters. The rules for generating a signature string are as follows:

1.  Sort the parameters except **sign** and **method** in the request body in ascending order according to the ASCII codes of the initial letters of their names. If the initial letters of two parameters are the same, their second letters will be used for sorting, and so on.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/VffB4ykvR82MZdOQ_BfFpQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D61F1A56E4DBFE0A3A0CAE3653256A9237C73A6FF04D5F310C51AE1C0871F298)
    
    The parameters **sign** and **method** are not used for signing.
    
2.  Add dependencies.
    
    <dependencies>
           <dependency>
                <groupId>commons-codec</groupId>
                <artifactId>commons-codec</artifactId>
                <version>1.15</version> <!-- Use the latest stable version. -->
            </dependency>
            <dependency>
                <groupId>org.bouncycastle</groupId>
                <artifactId>bcprov-jdk18on</artifactId>
                <version>1.74</version> <!-- Use the latest stable version. -->
            </dependency>
    </dependencies>
    
3.  Use **&** to concatenate the parameters included in signing and their URL encoded values to a string using the key-value pair format, for example, **a=xxxxxx&b=xxxxxxx&c=xxxxxxxxxxx...**. The parameter values need to be URL-encoded.
    
    Java sample code:
    
    // Assemble parameters except **sign** and **method** in the body. The parameter values here are only examples.
    Map<String, String> paramsMap = new HashMap<>();
    paramsMap.put("appId", "appId");
    paramsMap.put("cpId", "cpId");
    paramsMap.put("teamPlayerId", "teamPlayerId");
    paramsMap.put("ts", "111111111");
    
    // Sort the parameters in alphabetical order.
    Map<String, String> tempMap = new TreeMap<>(paramsMap);
    StringBuffer base = new StringBuffer();
    
    // Concatenate parameters.
    for (Map.Entry<String, String> entry : tempMap.entrySet()) {
        String key = entry.getKey();
        String value = entry.getValue();
        base.append(key).append('=').append(null == value ? '' : URLEncoder.encode(value, "UTF-8")).append('&');
    }
    
    if (base.length() > 0) {
        base.deleteCharAt(base.length() - 1);
    }
    
4.  Use the game private key to sign the generated string, applying the RSA algorithm (SHA256WithRSA/PSS). Use Base64 to encode the signed string. The obtained string is the signature string.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/hkOb9HXOQxSbsH6q3SgPRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2723DEA642125C44A4788DAF9E9F684157F79D9F9780DB25451A13FB9C847BCF)
    
    -   For details about how to obtain the private key of a game, please refer to [Obtaining the Game Key](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gameservice-key).
    -   The signature string needs to be URL-encoded before being added to the request.
    
    Java sample code:
    
    // Obtain the private key for signing. The implementation method is determined by yourself. The following is only an example.
    String privateKey = "xxxxxx";
    
    // Add a signature.
    byte\[\] keyBytes = Base64.decodeBase64(privateKey);
    PKCS8EncodedKeySpec pkcs8KeySpec = new PKCS8EncodedKeySpec(keyBytes);
    KeyFactory keyFactory = KeyFactory.getInstance("RSA");
    PrivateKey privateK =  keyFactory.generatePrivate(pkcs8KeySpec);
    Signature signature = Signature.getInstance("SHA256withRSA/PSS", new BouncyCastleProvider());
    signature.initSign(privateK);
    signature.update(base.getBytes(StandardCharsets.UTF\_8));
    String sign =  Base64.encodeBase64String(signature.sign());
