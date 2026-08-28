# Obtaining the Player ID

#### Function

-   Authenticates an access token.
-   Passes an access token to the Huawei server to obtain the player information such as **gamePlayerId** and **teamPlayerId**.

#### Scene Description

The game has obtained the access token and needs to parse and authenticate it. Then the game uses the access token to obtain information such as **gamePlayerId** and **teamPlayerId** of the player from the Huawei server.

#### API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="16.74%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="16.74%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Your server -&gt; Huawei game server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="16.74%"><p>API URL</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>Please use TLS 1.2 or a later version.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="16.74%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Request: Content-Type: application/x-www-form-urlencoded (form mode)</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

#### Request Parameters

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

This parameter must be set to **external.hms.gs.getPlayerInfo**.

 |
| 

accessToken

 | 

Yes

 | 

String

 | 

Access token obtained by the game through the API for [obtaining a user-level credential](../../../account-kit/rest-apis/api-call-credentials/obtaining-a-user-level-credential/document.md) of Account Kit.

 |

#### Request Example

POST /gameservice/api/gbClientApi HTTP/1.1
Content-Type: application/x-www-form-urlencoded
User-Agent: PostmanRuntime/7.24.0
Accept: \*/\*
Host: jos-open-api.cloud.huawei.com
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 717
// **The values of all request parameters** must be URL-encoded before being concatenated.
method=external.hms.gs.getPlayerInfo&accessToken=\*\*\*\*\*\*

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

Result from the server.

-   **0**: The information is obtained successfully.
-   **\-1**: Failed to obtain the information.
-   **2**: The access token is invalid.
-   **3001**: Invalid parameter.

 |
| 

acctInfo

 | 

No

 | 

[LoginAcctInfo](#li1628913126415)

 | 

Player ID, which will be returned upon successful retrieval.

 |
| 

bindInfo

 | 

Yes

 | 

[BindPlayerInfo](#li0462806435)

 | 

Official game account information associated with **PlayerId**.

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

-   LoginAcctInfo
    
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
    
    gamePlayerAcct
    
     | 
    
    No
    
     | 
    
    [PlayerAcct](#li137107744415)
    
     | 
    
    **gamePlayerId** information. In the transfer scene, **gamePlayerId** is returned by default.
    
     |
    | 
    
    teamPlayerAcct
    
     | 
    
    No
    
     | 
    
    [PlayerAcct](#li137107744415)
    
     | 
    
    **teamPlayerId** information. In the association scene, **teamPlayerId** is returned by default.
    
     |
    
    -   PlayerAcct
        
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
        
        id
        
         | 
        
        Yes
        
         | 
        
        String
        
         | 
        
        Player ID.
        
         |
        | 
        
        compatibleType
        
         | 
        
        Yes
        
         | 
        
        int
        
         | 
        
        Compatibility type.
        
        -   **0**: **gamePlayerId** is incompatible with **openId** and **playerId**. After the [getLocalPlayer](../../arkts-apis/gameplayer-basic-game-service/document.md#section17453143012584) API is called, the player ID is generated when a player signs in to your game for the first time. **teamPlayerId** is incompatible with **unionId**. When the [unionLogin](../../arkts-apis/gameplayer-basic-game-service/document.md#section157848375136) API is called, the player ID is generated when the player signs into your game for the first time and does not choose to transfer APK game data.
        -   **1**: **gamePlayerId** is compatible with **playerId**. That is, if a player chooses to transfer APK game data when signing in to your game for the first time and the APK game uses **playerId** as the player ID, Game Service Kit uses **playerId** as the new **gamePlayerId**.
        -   **2**: **gamePlayerId** is compatible with **openId**. That is, if a player chooses to transfer APK game data when signing in to your game for the first time and the APK game uses **openId** as the player ID, Game Service Kit uses **openId** as the new **gamePlayerId**.
        
         |
        | 
        
        idType
        
         | 
        
        Yes
        
         | 
        
        int
        
         | 
        
        Player ID type.
        
        -   **1**: gamePlayerId
        -   **2**: teamPlayerId
        
         |
        | 
        
        bindType
        
         | 
        
        Yes
        
         | 
        
        int
        
         | 
        
        Indicates whether an official game account can be associated.
        
        -   **0**: No
        -   **1**: Yes
        
         |
        

-   BindPlayerInfo
    
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
    
    bindMode
    
     | 
    
    No
    
     | 
    
    int
    
     | 
    
    Association mode:
    
    -   **0**: developer level.
    -   **1**: game level.
    
     |
    | 
    
    thirdOpenId
    
     | 
    
    No
    
     | 
    
    String
    
     | 
    
    Official game account ID.
    
     |
    

#### Response Example

HTTP/1.1 200 OK
Date: Tue, 19 May 2023 06:28:02 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Content-Encoding: gzip
Server: elb
{
    "acctInfo": {
        "gamePlayerAcct": {
            "id": "B7\*\*\*\*\*\*5E",
            "compatibleType": 0,
            "idType": 1,
            "bindType": 0
        }
    },
    "bindInfo":{
        "bindMode": 0,
        "thirdOpenId": "u\_123\*\*\*9ab"
   },
    "rtnCode": 0
}

#### Call Example

**Java**
package okhttp.com.post;
import com.alibaba.fastjson.JSONObject;
import okhttp3.\*;
import java.io.IOException;
public class GetTokenInfoTest {
    private static Integer RETURN\_CODE\_SUCCEED = 0;
    /\*\*
     \* Used for local debugging.
     \*/
    public static void main(String\[\] args) {
        String method = "external.hms.gs.getPlayerInfo"; // Fixed value.
        String accessToken= "xxxx"; // Use the access token obtained by the game client.
        getPlayerInfoService(method, accessToken);
    }
    /\*\*
     \* Obtain player ID information based on the access token.
     \*
     \* @param method Pass **external.hms.gs.getPlayerInfo**.
     \* @param accessToken Access token obtained when the game client calls the API of the Account Kit server.
     \*/
    private static void getPlayerInfoService(String method, String accessToken) {
        OkHttpClient client = new OkHttpClient().newBuilder().build();
        RequestBody mFormBody = new FormBody.Builder().add("method", method)
            .add("accessToken", accessToken)
            .build();
        Request request = new Request.Builder().url("https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi")
            .post(mFormBody)
            .build();
        try {
            Response response = client.newCall(request).execute();
            if (response.isSuccessful()) {
                JSONObject object = JSONObject.parseObject(response.body().string());
                if (RETURN\_CODE\_SUCCEED.equals(object.get("rtnCode")) && object.get("acctInfo") != null) {
                    JSONObject acctInfo = JSONObject.parseObject(object.get("acctInfo").toString());
                    if (acctInfo != null){
                        if (acctInfo.get("gamePlayerAcct") != null) {
                            JSONObject gamePlayerAcct = JSONObject.parseObject(acctInfo.get("gamePlayerAcct").toString());
                            System.out.println("gamePlayerId: " + gamePlayerAcct.get("id"));
                            System.out.println("gamePlayer compatibleType: " + gamePlayerAcct.get("compatibleType"));
                        }
                        if (acctInfo.get("teamPlayerAcct") != null) {
                            JSONObject teamPlayerAcct = JSONObject.parseObject(acctInfo.get("teamPlayerAcct").toString());
                            System.out.println("teamPlayerId: " + teamPlayerAcct.get("id"));
                            System.out.println("teamPlayer compatibleType: " + teamPlayerAcct.get("compatibleType"));
                        }
                    }
                    JSONObject bindInfo = JSONObject.parseObject(object.get("bindInfo").toString());
                    if (bindInfo != null) {
                        System.out.println("bindMode: " + bindInfo.get("bindMode"));
                        System.out.println("thirdOpenId: " + bindInfo.get("thirdOpenId"));
                    }
                } else {
                    System.out.println("rtnCode: " + object.get("rtnCode"));
                    System.out.println("rtnMsg: " + object.get("errMsg"));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

**C#**
using System;
using System.IO;
using System.Net;
using System.Text;
using System.Web;
namespace cXdemo
{
    class Program
    {
        static void Main(string\[\] args)
        {
            // This parameter must be set to **external.hms.gs.getPlayerInfo**.
            string method = "external.hms.gs.getPlayerInfo";
            // Access token obtained from the **Player** object of the current player.
            string accessToken = "xxxxx";
            // Request API.
            requestgameInfo(method, accessToken);
        }
        static void requestgameInfo(string method, string accessToken) 
        {
            var requestUrl = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi";
            HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;
            request.Method = "post";
            request.ContentType = "application/x-www-form-urlencoded";
            StringBuilder data = new StringBuilder();
            data.Append("method=" + HttpUtility.UrlEncode(method));
            data.Append("&accessToken=" + HttpUtility.UrlEncode(accessToken));
            byte\[\] byteData = Encoding.UTF8.GetBytes(data.ToString());
            request.ContentLength = byteData.Length;
            Stream postStream = request.GetRequestStream();
            postStream.Write(byteData, 0, byteData.Length);
            postStream.Close();
            WebResponse response = request.GetResponse();
            StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
            string strJson = reader.ReadToEnd();
            Console.WriteLine(strJson);
            reader.Close();
            response.Close();
        }
    }
}

**PHP**
class get\_token\_info
{
    /\*\*
     \* Obtain player information based on the access token.
     \*
     \* @param string $method Pass **external.hms.gs.getPlayerInfo**.
     \* @param string $accessToken Use the access token in the **Player** object of the client.
     \*/
    public function call\_https(string $method, string $accessToken): void
    {
        $data = array("method" => $method, "accessToken" => $accessToken);
        $curl = curl\_init();
        curl\_setopt\_array($curl, array(
            CURLOPT\_URL => 'https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi',
            CURLOPT\_RETURNTRANSFER => true,
            CURLOPT\_ENCODING => '',
            CURLOPT\_MAXREDIRS => 10,
            CURLOPT\_TIMEOUT => 0,
            CURLOPT\_FOLLOWLOCATION => true,
            CURLOPT\_CUSTOMREQUEST => 'POST',
            CURLOPT\_SSL\_VERIFYHOST => false,
            CURLOPT\_SSL\_VERIFYPEER => false,
            CURLOPT\_HTTP\_VERSION => CURL\_HTTP\_VERSION\_1\_1,
            CURLOPT\_POSTFIELDS => http\_build\_query($data),
            CURLOPT\_HTTPHEADER => array(
                'Content-Type: application/x-www-form-urlencoded'
            ),
        ));
        $response = curl\_exec($curl);
        if (curl\_error($curl)) {
            throw new Exception(curl\_error($curl));
        }
        curl\_close($curl);
        $result = json\_decode($response, true);
        var\_dump($result);
    }
}
$get\_token\_info = new get\_token\_info();
$method = "external.hms.gs.getPlayerInfo"; // Fixed value.
$accessToken = "xxxxx"; // Use the access token in the **Player** object of the client.
$get\_token\_info->call\_https($method, $accessToken);

**Python**
from typing import Any
import requests
import urllib.parse
class GetTokenInfoSolution:
    def get\_token\_info(self, method, accessToken):
        url = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi"
        params: dict\[str, Any\] = {
            'method': method,
            'accessToken': accessToken
        }
        encodedParams = urllib.parse.urlencode(params)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, headers=headers, data=encodedParams)
        print(response.text)
if \_\_name\_\_ == "\_\_main\_\_":
    # This parameter must be set to **external.hms.gs.getPlayerInfo**.
    input\_method = 'external.hms.gs.getPlayerInfo'
    # Use the access token in the **Player** object of the client.
    input\_accessToken = 'xxx'
    function = GetTokenInfoSolution()
    function.get\_token\_info(input\_method, input\_accessToken)
