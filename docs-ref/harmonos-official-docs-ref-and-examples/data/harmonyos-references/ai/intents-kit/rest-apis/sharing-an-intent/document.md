# Sharing an Intent

#### Function

This API allows your app or atomic service to share the intent-related event data with Intents Kit to enable event-based notifications.

#### Scenario Description

**User events**: Your app or atomic service shares data of a user-triggered event relevant to a specific intent with Intents Kit via the intent sharing API.

**Public events**: Huawei's public cloud server shares public event data (for example, typhoon) related to a specific intent with Intents Kit via the intent sharing API.

#### API Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="16.74%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="16.74%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Your server -&gt; Intents Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="16.74%"><p>URL</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>https://hag.cloud.huawei.com/open-ability/v2/service-events/notify</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="16.74%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="83.26%"><p>Request: Content-Type: application/json</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

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

Set the value to the app-level access token prefixed with **Bearer**. You can obtain the access token by calling the OAuth 2.0 API at **https://oauth-login.cloud.huawei.com/oauth2/v3/token**. (For details, see the steps for obtaining **x-appid** and **Authorization**.)

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

No

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

For details, see the request body example.

 |
| 

userAgree

 | 

Yes

 | 

Boolean

 | 

The value is always **true**, indicating that the user agrees to the operation.

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

**Value Range**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestTime

 | 

Yes

 | 

String

 | 

UTC time when a request is sent, in _yyyyMMddhhmmssSSS_ format.

 | 

Regular expression pattern: \[0-9\]{17}

 |
| 

abilityId

 | 

No

 | 

String

 | 

Ability ID.

 | 

Maximum length: 128 characters

 |
| 

sid

 | 

No

 | 

String

 | 

ID allocated by Huawei for a third-party account that is associated with a HUAWEI ID. (You do not need to bind the accounts.) Note that **openId** and **sid** cannot be both empty.

 | 

Maximum length: 512 characters

 |
| 

openId

 | 

No

 | 

String

 | 

ID allocated by Huawei for a third-party account that is associated with a HUAWEI ID. This parameter is mandatory when the event is a user-level event. Note that **openId** and **sid** cannot be both empty.

 | 

Maximum length: 512 characters

 |
| 

overwriteByEventName

 | 

No

 | 

Boolean

 | 

Indicates whether to overwrite other widgets of the same ability for a user, according to the event name. The default value is **false**.

 | 

\-

 |
| 

overwriteByAbility

 | 

No

 | 

Boolean

 | 

Indicates whether to overwrite other widgets of the same ability for a user. The default value is **true**.

 | 

\-

 |
| 

content

 | 

No

 | 

EventContent

 | 

Event notification content, which is used to determine the event validity and display the event content.

 | 

\-

 |

**EventContent**

| 
**Parameter**

 | 

**Mandatory**

 | 

**Type**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

contentData

 | 

Yes

 | 

List<ContentDataItem>

 | 

Event content data.

 | 

\-

 |

**ContentDataItem**

| 
**Parameter**

 | 

**Mandatory**

 | 

**Type**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

header

 | 

Yes

 | 

EventContentHeader

 | 

Content definition.

 | 

\-

 |
| 

payload

 | 

Yes

 | 

EventContentPayload

 | 

Content.

 | 

\-

 |

**EventContentHeader**

| 
**Parameter**

 | 

**Mandatory**

 | 

**Type**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

namespace

 | 

Yes

 | 

String

 | 

Content definition namespace.

 | 

The value is always **Intent**.

 |
| 

name

 | 

Yes

 | 

String

 | 

Intent name.

 | 

\-

 |

**EventContentPayload**

| 
**Parameter**

 | 

**Mandatory**

 | 

**Type**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

identifier

 | 

Yes

 | 

String

 | 

Unique ID of an event.

 | 

Regular expression pattern: \[a-zA-Z0-9\\-\]{1,64}

 |
| 

intentEntityInfo

 | 

Yes

 | 

Object

 | 

Intent entity.

 | 

Other information about an intent entity, in the format of one or more key-value pairs. The key is of the string type, and the value is of the Object type. The specific keys and values depend on the intent name. For details, please click [here](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713).

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
x-appid: 100012345
Accept:application/json
x-event-type:USER

Take the **ViewRepayment** intent as an example. The complete request body is as follows:

{
  "events": \[{
    "requestTime": "20240229143501798",  // UTC time when a request is sent, in _yyyyMMddhhmmssSSS_ format.
    "abilityId": "389ccb86317f41c19c2aa8762345069c", // Ability ID.
    "sid": "0bda3b89e3f44a44940eaad6b863dcc6",   // ID allocated by Huawei for a third-party account that is associated with a HUAWEI ID. (You do not need to bind the accounts.)
    "overwriteByEventName": false,   // Indicates whether to overwrite other widgets of the same ability for a user, according to the event name. The default value is **false**.
    "overwriteByAbility": false,  // Indicates whether to overwrite other widgets of the same ability for a user. The default value is **true**.
    "content": {  // Event content data.
      "contentData": \[{  // Event content data.
        "header": {  // Header information.
          "namespace": "Intent",  // Namespace. Set this parameter to **Intent**.
          "name": "ViewRepayment"  // Intent name.
        },
        "payload": {  // Payload.
          "identifier": "uuid", // Unique identifier of an event.
          "intentEntityInfo": {   // Intent entity.
            "repaymentType":"CreditCard",
            "statementDate": "2023-10-01",
            "repaymentDate": "2023-10-08",
            "bankName": "xxx Bank",
            "bankNameAbbreviation": "xx",
            "availableBeginTime": "2023-10-08T00:00:00+08:00",
            "availableEndTime": "2023-10-08T23:59:59+08:00",
            "eventStatus": "Repayment",
            "eventImage": "https://www-file.abc.com/-/media/corporate/images/home/logo/abc\_logo.png",
            "cardTailNumber": "1234",
            "cardType": "CreditCard"
          }
        }
      }\]
    }
  }\],
  "userAgree": true
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
-   If the API fails to be called, **400** will be returned. The following is an example of the response body format when the effective or expiration time is invalid:
    
    {
      "errorEvents":  \[{
        "requestId": "02240416001",
        "resultInfo": {
          "code": "invalidParam",
          "desc": "expireTime can not before nowTime"
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
