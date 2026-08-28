# Converting teamPlayerId in Batches

#### Function

This API is used to transfer a game on HUAWEI Developers from one account to another. The game assets belong to the receiving account.

The transferring account or the receiving account can call this API to submit information associated with the game before the transfer (for example, **teamPlayerId**) to the Huawei server in batches and obtain the corresponding information in batches after the transfer.

#### Restrictions

-   Before calling this API, ensure that the transferring account or the receiving account has completed game transfer. Otherwise, **teamPlayerId** cannot be converted.
-   A maximum of 1000 **teamPlayerId** records can be obtained in a single API call.
-   Call this API with an interval longer than 3 seconds.

#### API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="16.74%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="16.74%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Your server -&gt; Huawei server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="16.74%"><p>API URL</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>China site: https://connect-api.cloud.huawei.com/api/jas/open/players/player-accounts/team-player/convert</p><div class="caution"><span class="cautiontitle">CAUTION:</span><div class="cautionbody"><p>When you call the API for <a href="https://developer.huawei.com/consumer/en/doc/AppGallery-connect-References/agcapi-obtain_token-0000001158365043" target="_blank">obtaining a token</a>, the domain name must be the same as that in this API URL. For example, if the domain name in this API URL is <strong>connect-api.cloud.huawei.com</strong>, the URL <strong>https://connect-api.cloud.huawei.com/api/jas/open/players/player-accounts/team-player/convert</strong> must be used to call the API for <a href="https://developer.huawei.com/consumer/en/doc/AppGallery-connect-References/agcapi-obtain_token-0000001158365043" target="_blank">obtaining a token</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="16.74%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Request: Content-Type: application/json</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

#### Request Parameters

## Header

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

client\_id

 | 

Yes

 | 

String

 | 

[Client ID used for authentication](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agcapi-getstarted-0000001111845114#section103mcpsimp).

 |
| 

Authorization

 | 

Yes

 | 

String

 | 

Authentication information in **Authorization: Bearer ${****_access\_token_****}** format. In the format, _access\_token_ is obtained through the API for [obtaining a token](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-References/agcapi-obtain_token-0000001158365043).

 |
| 

appId

 | 

Yes

 | 

String

 | 

[App ID of a game](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569).

 |

## Body

The request body carries related information in JSON format. The following table lists the parameters involved.

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

srcCpId

 | 

Yes

 | 

Long

 | 

[ID of the developer who transfers the game](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569).

 |
| 

dstCpId

 | 

Yes

 | 

Long

 | 

[ID of the developer who receives the game](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569).

 |
| 

teamPlayerIds

 | 

Yes

 | 

List<String>

 | 

List of **teamPlayerId** before the transfer, which contains 1 to 1000 IDs.

NOTE:

Make sure that these IDs are deduplicated in the list.

 |

#### Request Example

POST  HTTP/1.1
Host: connect-api.cloud.huawei.com
Content-Type: application/json
client\_id: 41\*\*\*\*\*\*7168
appId: "\*\*\*\*\*"
Authorization: Bearer \*\*\*\*\*\*
{
    "srcCpId": 4130\*\*\*\*71055,
    "dstCpId": 4008\*\*\*\*74585,
    "teamPlayerIds":\[
        "\*\*\*\*\*\*\*\*\*\*",
        "\*\*\*\*\*\*\*\*\*\*",
        "\*\*\*\*\*\*\*\*\*\*"
    \]
}

#### Response Parameters

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

ret

 | 

Yes

 | 

[JosRet](#en-us_topic_0000002273612857_en-us_topic_0000002195007290_li266952144619)

 | 

JSON string containing the result code and description in {"code":_retcode_, "msg": "_description_"} format, in which _retcode_ indicates the result code and _description_ indicates the result code description.

 |
| 

data

 | 

Yes

 | 

List<[ConvertTeamPlayerIdItem](#en-us_topic_0000002273612857_en-us_topic_0000002195007290_li14201142814463)\>

 | 

Query result returned by the API for a single request.

 |

-   JosRet
    
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
    
    code
    
     | 
    
    Yes
    
     | 
    
    int
    
     | 
    
    Result code returned by a single API call.
    
    -   **0**: Request successful.
    -   **\-1**: Request failed.
    -   **3002**: Authentication error.
    
     |
    | 
    
    msg
    
     | 
    
    No
    
     | 
    
    String
    
     | 
    
    Error message.
    
     |
    
-   ConvertTeamPlayerIdItem
    
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
    
    srcCpId
    
     | 
    
    Yes
    
     | 
    
    Long
    
     | 
    
    ID of the developer who transfers the game.
    
     |
    | 
    
    srcTeamPlayerId
    
     | 
    
    Yes
    
     | 
    
    String
    
     | 
    
    **teamPlayerId** before the transfer.
    
     |
    | 
    
    dstCpId
    
     | 
    
    Yes
    
     | 
    
    Long
    
     | 
    
    ID of the developer who receives the game.
    
     |
    | 
    
    dstTeamPlayerId
    
     | 
    
    Yes
    
     | 
    
    String
    
     | 
    
    **teamPlayerId** after the transfer.
    
     |
    | 
    
    errCode
    
     | 
    
    Yes
    
     | 
    
    int
    
     | 
    
    Result code returned by a request for querying a single **teamPlayerId**:
    
    -   **0**: Request successful.
    -   **\-1**: Request failed.
    
     |
    

#### Response Example

{
    "ret": {
         "code": 0,     
         "msg": "string"
    },
    "data": \[
        {
            "srcCpId": 4330\*\*\*\*71055,       
            "srcTeamPlayerId": "\*\*\*\*\*\*",       
            "dstCpId": 4130\*\*\*\*71055,       
            "dstTeamPlayerId": "\*\*\*\*\*",       
            "errCode": 0
        }
    \]
}

#### Call Example

**Java**
/\*\*
 \* Convert **teamPlayerId** in batches.
 \*
 \* @param domain Select the URL of the nearest site based on the server deployment location. The domain name in the URL must be the same as that used for obtaining a token.
 \* @param client\_id Client ID used for authentication.
 \* @param token Token used for a POST authentication request.
 \* @param teamPlayerIds **teamPlayerId** list to be queried.
 \* @param appId App ID of the game.
 \*/
private static void batchGetOpenIds(String domain, String client\_id, String token, List<String> teamPlayerIds, String appId) {
        try {
            // API URL. Select the URL of the nearest site based on the server deployment location and ensure that the domain name in the URL is the same as that used for obtaining a token.
            HttpPost post = new HttpPost(domain + "/api/jas/open/players/player-accounts/team-player/convert");
            // Construct a message header.
            post.setHeader("Authorization", "Bearer " + token);
            post.setHeader("client\_id", client\_id);
            post.setHeader("appId", appId);
            // Construct a message body.
            JSONObject keyString = new JSONObject();
            keyString.put("srcCpId", srcCpId);
            keyString.put("dstCpId", dstCpId);
            keyString.put("teamPlayerId", teamPlayerIds); // **teamPlayerId** under the original account.
            StringEntity entity = new StringEntity(keyString.toString(), Charset.forName("UTF-8"));
            entity.setContentEncoding("UTF-8");
            // Send a data request in JSON format.
            entity.setContentType("application/json");
            post.setEntity(entity);
            CloseableHttpClient httpClient = HttpClients.createDefault();
            HttpResponse response = httpClient.execute(post);
            int statusCode = response.getStatusLine().getStatusCode();
            if (statusCode == HttpStatus.SC\_OK) {
                BufferedReader br =
                    new BufferedReader(new InputStreamReader(response.getEntity().getContent(), Consts.UTF\_8));
                String result = br.readLine();
                System.out.println(result);
                JSONObject object = JSON.parseObject(result);
            }
            post.releaseConnection();
            httpClient.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
}

**C#**
/\*\*
 \* Convert **teamPlayerId** in batches.
 \*
 \* @param domain Select the URL of the nearest site based on the server deployment location. The domain name in the URL must be the same as that used for obtaining a token.
 \* @param clientId Client ID used for authentication.
 \* @param token Token used for a POST authentication request.
\* @param teamPlayerIds List of **teamPlayerId** before the transfer.
 \* @param appId App ID of the game.
 \* @Param srcCpId ID of the developer who transfers the game.
 \* @Param dstCpId ID of the developer who receives the game.
 \*/
static void convertTeamPlayerId(string domain, string clientId, string token, List<string> teamPlayerIds, string appId, long srcCpId, long dstCpId)
{
    try
    {
        // API URL. Select the URL of the nearest site based on the server deployment location and ensure that the domain name in the URL is the same as that used for obtaining a token.
        var requestUrl = domain + "/api/jas/open/players/player-accounts/team-player/convert";
        HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;
        request.Method = "post";
        request.ContentType = "application/json";
        request.Headers.Add("client\_id", clientId);
        request.Headers.Add("Authorization", "Bearer " + token);
        request.Headers.Add("appId", appId);
        Dictionary<string, object> dic = new Dictionary<string, object>
        {
            {"srcCpId", srcCpId},
            {"dstCpId", dstCpId},
            {"teamPlayerIds", teamPlayerIds}
        };
        string sendData = JsonConvert.SerializeObject(dic, Formatting.Indented);
        Console.WriteLine(sendData);
        byte\[\] byteData = Encoding.GetEncoding("utf-8").GetBytes(sendData);
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
    catch (Exception e)
    {
        Console.WriteLine(e.ToString());
    }
}

**PHP**
/\*\*
 \* Convert **teamPlayerId** in batches.
 \*
 \* @param string $domain Select the URL of the nearest site based on the server deployment location. The domain name in the URL must be the same as that used for obtaining a token.
 \* @param string $client\_id Client ID used for authentication.
 \* @param string $token Token used for a POST authentication request.
 \* @param array $teamPlayerIds **teamPlayerId** list before the transfer.
\* @param string $appId App ID of the game.
\* @Param long $srcCpId ID of the developer who transfers the game.
 \* @Param long $dstCpId ID of the developer who receives the game.
 \* @throws Exception
 \*/
public function batch\_convert\_teamPlayerIds(string $domain, string $client\_id, string $token, array $teamPlayerIds, string $appId, long $srcCpId, long $dstCpId)
{
    $curl = curl\_init();
    $data = array("teamPlayerIds" => $teamPlayerIds, "srcCpId" => $srcCpId, "dstCpId" => $dstCpId);
    curl\_setopt\_array($curl, array(
        CURLOPT\_URL => $domain . '/api/jas/open/players/player-accounts/team-player/convert',
        CURLOPT\_RETURNTRANSFER => true,
        CURLOPT\_ENCODING => '',
        CURLOPT\_MAXREDIRS => 10,
        CURLOPT\_TIMEOUT => 0,
        CURLOPT\_FOLLOWLOCATION => true,
        CURLOPT\_SSL\_VERIFYHOST => false,
        CURLOPT\_SSL\_VERIFYPEER => false,
        CURLOPT\_HTTP\_VERSION => CURL\_HTTP\_VERSION\_1\_1,
        CURLOPT\_CUSTOMREQUEST => 'POST',
        CURLOPT\_POSTFIELDS => json\_encode($data),
        CURLOPT\_HTTPHEADER => array(
            'client\_id: ' . $client\_id,
            'Authorization: Bearer ' . $token,
            'Content-Type: application/json',
            'appId: ' . $appId
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

**Python**
from getToken import \*
class BatchConvertTeamPlayerIdsSolution:
    @staticmethod
    def batch\_convert\_team\_player\_ids(domain, client\_id, access\_token, team\_player\_id, app\_id, src\_cp\_id, dst\_cp\_id):
        url = domain + '/api/jas/open/players/player-accounts/team-player/convert'
        data = {"teamPlayerIds": team\_player\_id, "srcCpId": src\_cp\_id, "dstCpId": dst\_cp\_id}
        payload = json.dumps(data)
        headers = {
            'client\_id': client\_id,
            'Authorization': 'Bearer ' + access\_token,
            'Content-Type': 'application/json',
            'appId': app\_id
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
if \_\_name\_\_ == "\_\_main\_\_":
    # Select the URL of the nearest site based on your server deployment location. The domain name of the China site URL is used as an example here.
    input\_domain = 'https://connect-api.cloud.huawei.com'
    # Client ID.
    input\_client\_id = 'xxxxxxx'
    # Client secret.
    input\_client\_secret = 'xxxxxxxx'
    # Obtain a token.
    token\_function = GetToken()
    input\_access\_token = token\_function.get\_token(input\_domain, input\_client\_id, input\_client\_secret)
    # App ID of the game.
    input\_app\_id = 'xxxxx'
    # List of **teamPlayerIds** to be converted. A maximum of 1000 player IDs can be converted at a time. The following example lists two player IDs.
    input\_player\_Ids = \['xxxxxxx', 'xxxxxx'\]
    # ID of the developer who transfers the game.
    input\_src\_cp\_id = 111111
    # ID of the developer who receives the game.
    input\_dst\_cp\_id = 222222
    batch\_function = BatchGetOpenIdsSolution()
    batch\_function.batch\_convert\_team\_player\_ids(input\_domain, input\_client\_id, input\_access\_token, input\_player\_Ids, input\_app\_id, input\_src\_cp\_id, input\_dst\_cp\_id)
