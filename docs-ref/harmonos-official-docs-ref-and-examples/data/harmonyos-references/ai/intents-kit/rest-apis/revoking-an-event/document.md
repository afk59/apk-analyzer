# Revoking an Event

#### Function

This API deletes invalid data of intents shared by your app or atomic service, to prevent triggering invalid event notifications.

#### Scenario Description

**User events**: When user event data, triggered by user-initiated actions and shared by your app or atomic service, exceeds its validity period, Intents Kit will delete such data.

**Public events**: When public event data, triggered by public events, exceeds its validity period, Intents Kit will delete such data.

#### API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="16.74%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="16.74%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Your server -&gt; Intents Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="16.74%"><p>URL</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>https://hag.cloud.huawei.com/open-ability/v2/service-events/revoke</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="16.74%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Request: Content-Type: application/json</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

#### Request Parameters

**Request header**

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

x-appid

 | 

Yes

 | 

String

 | 

App ID registered in AppGallery Connect. To view the value, sign in to AppGallery Connect, click **My projects**, and select your app. The value of **x-appid** is the same as that of **Client ID**.

 |
| 

Authorization

 | 

Yes

 | 

String

 | 

Set the value to the app-level access token prefixed with **Bearer**. You can obtain the access token by calling the OAuth 2.0 API at **https://oauth-login.cloud.huawei.com/oauth2/v3/token**.

 |
| 

Content-Type

 | 

Yes

 | 

String

 | 

This parameter has a fixed value of **application/json**.

 |
| 

Accept

 | 

Yes

 | 

String

 | 

This parameter has a fixed value of **application/json**.

 |
| 

x-event-type

 | 

Yes

 | 

String

 | 

Event type. **USER** indicates a user event, and **COMMON** indicates a public event.

 |

**Request body**

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

events

 | 

Yes

 | 

List<Object>

 | 

For details, see the example.

 |

**Request body parameters**

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

requestTime

 | 

Yes

 | 

String

 | 

UTC timestamp when the API was requested, in format _yyyymmddhhmmssSSS_.

 |
| 

revokeBy

 | 

No

 | 

String

 | 

Revocation method. The default value is **REQUEST\_ID**.

 |
| 

identifier

 | 

Yes

 | 

String

 | 

ID that uniquely identifies a requested data record.

 |
| 

eventName

 | 

No

 | 

String

 | 

Event name. This parameter is optional when **revokeBy** uses the default value **REQUEST\_ID**.

 |
| 

openId

 | 

No

 | 

String

 | 

OpenID allocated by Huawei. This parameter must be set when events are pushed by OpenID. Note that **openId** and **sid** cannot be both empty.

 |
| 

sid

 | 

No

 | 

String

 | 

SID allocated by Huawei. This parameter must be set when events are pushed by SID. Note that **openId** and **sid** cannot be both empty.

 |
| 

abilityId

 | 

Yes

 | 

String

 | 

Ability ID.

 |

Steps of obtaining **x-appid** and **Authorization** are described as follows:

To view the value of **x-appid**, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/console/service/AppService), click **My projects**, and select your app. The value of **x-appid** is the same as that of **Client ID**.

The value of **Authorization** is obtained through the OAuth 2.0 API with the following URL:

https://oauth-login.cloud.huawei.com/oauth2/v3/token

**Request header**

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

Content-Type

 | 

Yes

 | 

String

 | 

This parameter has a fixed value of **application/x-www-form-urlencoded**.

 |

**Request body**

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

grant\_type

 | 

Yes

 | 

String

 | 

This parameter has a fixed value of **client\_credentials**.

 |
| 

client\_id

 | 

Yes

 | 

String

 | 

Obtained from AppGallery Connect.

 |
| 

client\_secret

 | 

Yes

 | 

String

 | 

Obtained from AppGallery Connect.

 |

The request body uses the form format, that is, **x-www-form-urlencoded**.

#### Request Example

An example of a complete request header is as follows:

Content-Type:application/json
Authorization:Bearer DQEBAGf5Mtm9rZl3W1W8sACVmWo0WhGUE3ANb/+KgRHjvmJqacjI3aF++jLEqbZsJ4H472MknoysUMaQrr8FgAHKPCU1YY4EKxUhsA==
x-appid:100012345 //
Accept:application/json
x-event-type:USER

An example of a complete request body is as follows:

{
  "events": \[
    {
      "requestTime": "Timestamp when the request was initiated",
      "revokeBy": "REQUEST\_ID",
      "identifier": "Identifier of the requested record", // **identifier** in the push API.
      "eventName": "Event name", // This parameter is optional when **revokeBy** is set to **REQUEST\_ID**.
      "openId": "openid", // Enter an OpenID for events pushed by **openid**.
      "sid": "0bda3b89e3f44a44940eaad6b863dcc6", // Enter an SID for events pushed by **sid**.
      "abilityId": "389ccb86317f41c19c2aa8762345069c" // Ability ID.
    }
  \]
}

#### Response Parameters

**Response header**

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

Content-Type

 | 

Yes

 | 

String

 | 

The value is **application/json;charset=UTF-8**.

 |

**Response body**

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

errorEvents

 | 

No

 | 

List<ErrorEvent>

 | 

See the following for the hierarchical structure. For details about the result, please refer to the sample code.

 |

**ErrorEvent**

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

requestId

 | 

Yes

 | 

String

 | 

Event identifier in the request body.

 |
| 

resultInfo

 | 

Yes

 | 

ResultInfo

 | 

Error details.

 |

**ResultInfo**

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

code

 | 

Yes

 | 

String

 | 

Error code.

 |
| 

desc

 | 

Yes

 | 

String

 | 

Error message.

 |

#### Response Example

-   If the API is successfully called, **200** will be returned, and the response body is empty.
-   If the API fails to be called, **400** will be returned. The following is an example of the response body format when mandatory parameters are not set:
    
    {
      "errorEvents": \[{
        "requestId": "02240416001",
        "resultInfo": {
          "code": "invalidParam",
          "desc": "openId and sid can not both be blank"
        }
      }\]
    }
    
    -   If an error occurs during the API call because the authentication information is invalid or has expired, **401** will be returned, and the response body is empty.
    -   If an error occurs during the API call because the gateway fails to verify your permission, **403** will be returned, and the response body is empty.
    -   If an error occurs during the API call because no UID corresponding to the SID you have passed has been obtained, **404** will be returned, and the response body is as follows:
        
        {
          "errorEvents": \[{
            "requestId": "02240416001",
            "resultInfo": {
              "code": "userNotFound",
              "desc": "User is not found"
            }
          }\]
        }
