# Account Disassociation Notification

#### Function

This API is used by the Huawei game server to send a key event notification to your server to remind you of account disassociation.

#### Scene Description

After you [set a callback address](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gameservice-address) in AppGallery Connect, the Huawei game server will remind you of account disassociation after a player deletes their HUAWEI ID. If your server returns a non-success response, the Huawei game server will periodically send a notification of this key event. It is recommended that your server returns a success response immediately after receiving the notification to avoid notification accumulation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/mqNplSr_T9evpeTuXjND6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE04C7B5D8CC1603F75F6BCC6301BAEBF2D83E615AD03E91F042FCA10D48EB7C)

To ensure the reliability of the resending mechanism, the number of notifications resent is likely to be more than what have been mentioned.

#### Restrictions

-   You are advised not to enable IP address restriction on your server. Otherwise, a change in Huawei game server's egress IP address may cause a service interruption.
-   You need to configure the callback address in AppGallery Connect in advance. The address must support HTTPS and be secured with a valid commercial certificate.

#### API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="16.74%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="16.74%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Huawei game server -&gt; Your server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="16.74%"><p><strong>Performance Indicator</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>TPS&gt;50</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="16.74%"><p><strong>Maximum Response Time</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>&lt;1s</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.5.1" valign="top" width="16.74%"><p>API URL</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Callback address configured in AppGallery Connect.</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.6.1" valign="top" width="16.74%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><ul><li>Request: Content-Type: application/json</li><li>Response: Content-Type: application/json</li></ul></td></tr></tbody></table>

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

appIds

 | 

No

 | 

List<String>

 | 

List of app IDs to be disassociated from games:

-   If the association is at the developer level, the value is the app that initiates the association.
-   If the association is at the game level, the value is the associated app.

 |
| 

teamPlayerId

 | 

Yes

 | 

String

 | 

teamPlayerId. The value contains a maximum of 256 characters.

 |
| 

sign

 | 

Yes

 | 

String

 | 

When sending a request, Huawei server signs all body parameters except **sign** using the SHA256WithRSA/PSS algorithm and returns the signed character string in the **sign** parameter.

You need to obtain the public key for signature verification and use the public key to perform signature verification on the signature string based on the encryption algorithm. For details about the signature verification method, see [Signature Verification Mechanism](#section1815419216397).

NOTE:

This parameter is sent after UTF-8 URL encoding. If the **getParameter()** method in a Java request is used, URL encoding is not required.

 |

#### Request Example

POST {API URL}
Host: xxx 
Content-Type: application/json 
{    
    "appIds": \["109\*\*\*688", "691\*\*\*237"\],    
    "teamPlayerId": "E5B\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*E9B",   
    "sign": "J0Eslg0p\*\*\*tKR37AB" 
}

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

result

 | 

Yes

 | 

int

 | 

Code returned by the server.

-   **0**: success
-   **1**: signature verification failure
-   **2**: timeout
-   **3**: service information error
-   **94**: system error
-   **95**: I/O error
-   **96**: incorrect URL
-   **97**: incorrect response
-   **98**: incorrect parameter
-   **99**: other errors

 |

#### Response Example

HTTP/1.1 200 OK 
Content-Type: application/json;charset=UTF-8
{
    "result": 0
}

#### Signature Verification Mechanism

1.  Obtain the signature string in the request, that is, the **sign** parameter.
2.  Sort the parameters except **sign** in the request body in ascending order according to the ASCII codes of the initial letters of their names. If the initial letters of two parameters are the same, their second letters will be used for sorting, and so on.
3.  After the sorting is complete, perform URL encoding on all numeric values involved in the signature and use **&** to concatenate the parameters to a string, for example, **a=xxxxxx&b=xxxxxxx&c=xxxxxx**. Signature verification is required for the string.
4.  Use the game public key to sign the string which requires signature verification based on the RSA algorithm (SHA256WithRSA/PSS) and verify the consistency between the signed string and the signature string in the **sign** parameter.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Ch_7bTEfTgufpl10IGJnwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDCD0D68F612C8AC10046F2B72A39D493A835170573B11D79CA84EA8622F3C30)
    
    For details about how to obtain the public key of a game, please refer to [Obtaining the Game Key](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/gameservice-key).
    
    Java sample code:
    
    // Packages of basic types such as List and Map are provided by the JDK. You can customize other types of packages and import them.
    // Assemble body parameters. The parameter values here are only examples.
    List<String> appIds =  Arrays.asList("appId1","appId2");
    Map<String, String> paramsMap = new HashMap<>();
    paramsMap.put("appIds", StringUtils.join(appIds, ","));
    paramsMap.put("teamPlayerId", "teamPlayerId");
    
    // Sort the parameters in alphabetical order.
    Map<String, String> tempMap = new TreeMap<>(paramsMap);
    // Concatenate parameters.
    StringBuffer base = new StringBuffer();
    for (Map.Entry<String, String> entry : tempMap.entrySet()) {
    	String key = entry.getKey();
    	String value = entry.getValue();
    	base.append(key).append('=').append(null == value ? "" : URLEncoder.encode(value, "UTF-8")).append('&');
    }
    String signStr = "";
    if (base.length() > 0) {
    	signStr = base.deleteCharAt(base.length() - 1).toString();
    }
    
    // Obtain the public key for signature verification. The implementation method is determined by yourself. The following is only an example.
    String publicKey = "xxx";
    String sign = "sign";
    
    // Signature verification
    byte\[\] keyBytes = Base64.decodeBase64(publicKey);
    X509EncodedKeySpec pkcs8KeySpec = new X509EncodedKeySpec(keyBytes);
    KeyFactory keyFactory = KeyFactory.getInstance("RSA");
    PublicKey publicK = keyFactory.generatePublic(pkcs8KeySpec);
    Signature signature = Signature.getInstance("SHA256WithRSA/PSS", new BouncyCastleProvider());
    signature.initVerify(publicK);
    signature.update(signStr.getBytes("UTF-8"));
    signature.verify(Base64.decodeBase64(sign));
