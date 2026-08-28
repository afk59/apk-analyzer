# Service Updates Sending API

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/s-voGbP9Rv65sfwMOlMNJw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=782FE827FC4CB81F237B6D1A67CDA64BC4AA677598B8692ABC1AD53E984638F8)

To ensure network security, the service updates API supports only TLS1.2 and later versions. Apps cannot use protocols earlier than TLS1.2 or unspecified cipher suites to send messages.

#### Function

This API is used by atomic services to deliver service updates messages.

#### Restrictions

-   The service updates capability is supported on phones and tablets.
-   The message body cannot exceed 4096 bytes.

#### Request Body Structure

## Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.5.2.1.3.1.1" valign="top" width="15.18%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="84.82%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.2.1" valign="top" width="15.18%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="84.82%"><p>Your server -&gt; Push Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.3.1" valign="top" width="15.18%"><p>URL</p></th><td class="cellrowborder" valign="top" width="84.82%"><p>https://push-api.cloud.huawei.com/v1/<strong>[projectId]</strong>/service_timeline/send</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>In the URL, <strong>[projectId]</strong> indicates the project ID. To obtain the project ID, sign in to <a href="https://developer.huawei.com/consumer/en/service/josp/agc/index.html" target="_blank">AppGallery Connect</a>, click <span class="wintitle"><b>Development and services</b></span>, click the desired project, and go to the <span class="wintitle"><b>Project settings</b></span> page.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.5.2.1.3.4.1" valign="top" width="15.18%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="84.82%"><p>Content-Type: application/json</p></td></tr></tbody></table>

## Request Header

| 
Parameter

 | 

Description

 | 

Example

 |
| :-- | :-- | :-- |
| 

Authorization

 | 

Authentication mode:

**JWT**

For details, please refer to [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token).

NOTE:

-   The **PS256** algorithm must be used to call the service updates API.
-   You are advised to set the JWT validity period to 3600 seconds, within which a JWT can be reused.
    
    This parameter value is **Bearer** followed by a space character and then the obtained authentication information.
    

 | 

Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*

 |

## Request Body

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

toOpenId

 | 

Yes

 | 

String

 | 

OpenID of a sign-in user. Use the OpenID reported by the device, or request the Account Kit server to [obtain user information](../../../../account-kit/rest-apis/obtaining-user-information/document.md). For details about how to design and integrate the HUAWEI ID sign-in function, please refer to the [account usage specifications](https://developer.huawei.com/consumer/en/doc/design-guides/accounts-0000001967444380) of atomic services.

 |
| 

appId

 | 

Yes

 | 

String

 | 

App ID of an atomic service. The value contains 1 to 64 characters.

NOTE:

**\[appId\]**: To obtain the app ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Apps/Atomic services**, select an atomic service, and query the app ID of the atomic service under **Basic information** on the **App information** page.

 |
| 

sceneId

 | 

Yes

 | 

String

 | 

Scenario ID. For details, please refer to [Service Updates Sending Scenarios](../service-updates-parameters/document.md#section159496312255). The value contains 1 to 32 characters.

 |
| 

subSceneId

 | 

Yes

 | 

String

 | 

Subscenario ID. For details, please refer to [Service Updates Sending Scenarios](../service-updates-parameters/document.md#section159496312255). The value contains 1 to 32 characters.

 |
| 

code

 | 

Yes

 | 

String

 | 

-   When a user uses Huawei Pay for payment in an atomic service, you can obtain the Huawei Pay order number (**sysTransOrderNo**) as the code.
-   When a code is generated after a user taps a scenario-specific button, you can obtain the code through the [Service Updates Authorization Code Button](https://developer.huawei.com/consumer/en/doc/atomic-guides/scenario-fusion-button-atomic-getservicecode).

 |
| 

content

 | 

Yes

 | 

[TimelineStatusContent](../service-updates-parameters/document.md#section1126513338180) Object

 | 

Status parameter in service updates.

For the takeout self-pickup scenario, please refer to [Takeout Self-Pickup Structure](../service-updates-parameters/document.md#section9109111521810).

For the takeout delivery scenario, please refer to [Takeout Delivery Structure](../service-updates-parameters/document.md#section910252410213).

 |

#### Request Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/1DjEeR-eQi-S1RmWFeqqYw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C8866A071C33C7333726492218E79C8001E0A463A63197725B79238812FC1F9)

Send requests based on the mandatory parameter and optional parameter requirements in different states. The following uses the takeout self-pickup scenario as an example.

**Example request: In preparation**

// Request URL
POST "https://push-api.cloud.huawei.com/v1/\[projectId\]/service\_timeline/send"
 
// Request Header
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*

// Request Body
{
    "appId": "5\*\*\*\*\*\*\*\*\*\*7",
    "toOpenId": "A\*\*\*\*\*\*\*\*\*\*O",
    "sceneId": "10001",
    "subSceneId": "100010001",
    "code": "3\*\*\*\*\*\*\*\*\*\*7",
    "content": {
        "status": 3,
        "orderTime": 1716191520,
        "amount": "¥ 18.00",
        "productCount": 1,
        "productName": "Mango",
        "productImg": "image\_test\_1",
        "merchantName": "Store A",
        "pickupNumber": "1668",
        "pickupTime": "16:08",
        "remainOrders": "5 orders/5 cups",
        "waitTime": "10-20 minutes",
        "button": {
            "type": 0,
            "text": "Pickup code",
            "data": {
                "testKey": "testValue"
            }
        },
        "clickAction": {
            "type": 0,
            "data": {
                "testKey": "testValue"
            }
            
        },
        "appendButtons": \[
            {
                "type": 0,
            "text": "Pickup code",
                "data": {
                    "testKey": "testValue"
                }
            }
        \]
    }
}

**Request example: Pending payment**

// Request URL
POST "https://push-api.cloud.huawei.com/v1/\[projectId\]/service\_timeline/send"
 
// Request Header
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*

// Request Body
{
    "appId": "6\*\*\*\*\*\*\*\*\*\*3",
    "toOpenId": "A\*\*\*\*\*\*\*\*\*\*F",
    "sceneId": "10001",
    "subSceneId": "100010001",
    "code": "1\*\*\*\*\*\*\*\*\*\*6",
    "content": {
        "status": 1,
        "orderTime": 1715236319,
        "amount": "¥ 5.00",
        "productCount": 1,
        "productName": "Mango",
        "productImg": "image\_test\_1",
        "paymentEndTime": "Pay in 5 minutes",
        "merchantName": "Store B",
        "button": {
            "type": 0,
            "text": "Pay now",
            "action": "https://\*\*\*"
        },
        "clickAction": {
            "type": 0,
            "action": "https://\*\*\*"
        },
        "appendButtons": \[
            {
                "type": 0,
            "text": "Pay now",
                "action": "https://\*\*\*"
            }
        \]
    }
}

#### Response Parameters

## Response Body

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

String

 | 

Response code.

 |
| 

msg

 | 

Yes

 | 

String

 | 

Response message.

 |
| 

requestId

 | 

Yes

 | 

String

 | 

Request ID.

 |

#### Response Examples

**Success response example**:

{
  "code": "80000000",
  "msg": "Success",
  "requestId": "157\*\*\*\*\*\*\*006"
}

**Failure response example**:

{  
  "code": "82600010",  
  "msg": "status content missing required field", 
  "requestId": "157\*\*\*\*\*\*\*006"
}

#### HTTP Response Codes

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Success.

 | 

\-

 |
| 

400

 | 

Invalid parameter.

 | 

Check the service response code and locate the fault accordingly.

 |
| 

401

 | 

Authentication failed.

 | 

Check the **Authorization** parameter in the HTTP header.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

The connection request is abnormal, generally because the network is unstable.

 | 

Try again later or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

503

 | 

Traffic control.

 | 

-   Distribute the sending speed evenly.
-   Spread out push notification delivery to avoid peak sending times.

 |
| 

504

 | 

The gateway timed out.

 | 

Try again later or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Service Response Codes

## 80000000 Success

**Message**

Success.

**Description**

Sent successfully.

**Possible causes**

Sent successfully.

**Solution**

None.

## 82600001 System Internal Error

**Message**

system error.

**Description**

System internal error.

**Possible causes**

An unknown error occurred.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

## 82600002 Invalid Parameter

**Message**

invalid parameter {errorTips}.

**Description**

Invalid parameter.

**Possible causes**

Invalid parameter.

**Solution**

Verify the request parameters as prompted by the response.

## 82600003 Service Denied

**Message**

access deny.

**Description**

Service denied.

**Possible causes**

The service updates sending permission is not enabled.

**Solution**

Enable the [service updates sending permission](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section20387153745216).

## 82600004 Risk Control Error

**Message**

status content blocked.

**Description**

Risk control error.

**Possible causes**

Some scenario parameters are prohibited.

**Solution**

Verify that the scenario parameters do not contain prohibited parameters as prompted by the response.

## 82600005 Service Updates Message Sending Failure

**Message**

send message failed{errorTips}.

**Description**

Failed to send the service updates message.

**Possible causes**

1.  There are no online recipients.
2.  The request body size exceeds the default value (4096 bytes).

**Solution**

Rectify the fault as follows:

1.  Verify that there are online recipients.
2.  Verify that the request body size does not exceed the default value (4096 bytes) and send the message again.

## 82600006 OpenID Verification Failure

**Message**

invalid openId.

**Description**

OpenID failed the verification.

**Possible causes**

The OpenID of the recipient is incorrect.

**Solution**

Use the OpenID reported by the device, or request the Account Kit server to [obtain the OpenID in user information](../../../../account-kit/rest-apis/obtaining-user-information/document.md).

## 82600007 Incorrect Scenario and Subscenario IDs

**Message**

invalid sceneId or subSceneId.

**Description**

The scenario and subscenario IDs are incorrect.

**Possible causes**

There is no permission on the scenario and subscenario.

**Solution**

Send the message based on enabled scenario and subscenario IDs.

## 82600008 Incorrect Authorization Code

**Message**

invalid code.

**Description**

The authorization code is incorrect.

**Possible causes**

1.  The transaction order ID is invalid.
2.  The transaction order ID is not activated within the validity period (1 hour).

**Solution**

Verify the following:

1.  The transaction order ID is valid.
2.  Regenerate the authorization code and push the message again.

Use the Huawei Pay order number (**sysTransOrderNo**) as the authorization code to push the message again.

## 82600009 Incorrect Scenario-specific Status

**Message**

invalid scene status.

**Description**

The scenario-specific status is incorrect.

**Possible causes**

Invalid request body parameter.

**Solution**

Verify the request body parameters according to [Service Updates Sending Scenarios](../service-updates-parameters/document.md#section159496312255).

## 82600010 Mandatory Status Parameters Are Missing

**Message**

status content missing required field {errorTips}.

**Description**

Mandatory status parameters are missing.

**Possible causes**

Mandatory status parameters are missing.

**Solution**

Verify the request body parameters according to [Service Updates Sending Scenarios](../service-updates-parameters/document.md#section159496312255).

## 82600011 Invalid Status Parameter Format

**Message**

status content has invalid field {errorTips}.

**Description**

The status parameter format is invalid.

**Possible causes**

The status parameter format is invalid.

**Solution**

Verify the [request body parameters](#section16714723163811) as prompted by the response.

## 82600012 Invalid Status Transition

**Message**

invalid status transition.

**Description**

Invalid status transition.

**Possible causes**

Invalid status transition.

**Solution**

-   For the takeout self-pickup scenario, verify the request body parameters by referring to the [requirements](../service-updates-parameters/document.md#section323244401911).
-   For the takeout delivery scenario, verify the request body parameters by referring to the [requirements](../service-updates-parameters/document.md#section14839531235).

## 82600013 Service Updates Push Disabled by User

**Message**

user close service.

**Description**

The user disabled the service updates push.

**Possible causes**

The user disabled the service updates push in this scenario.

**Solution**

Enable the service updates push permission in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). For details, please refer to [Applying for Required Permissions](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section20387153745216).

## 82600014 Invalid Image Resource ID

**Message**

invalid image id.

**Description**

Invalid image resource ID.

**Possible causes**

The image resource specified by the resource ID does not exist.

**Solution**

Check whether the image resource specified by the resource ID exists. If not, provide the image to [apply for image resource hosting](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section19921168203013) and obtain the resource ID again.

## 82600015 Status Updates Quantity Exceeds Upper Limit

**Message**

status refresh frequency reached upper limit.

**Description**

The number of status updates exceeds the upper limit.

**Possible causes**

The number of status updates exceeds the upper limit.

**Solution**

Reduce unnecessary status updates.

## 82600016 Service Updates Expired

**Message**

event expired.

**Description**

Service updates expired.

**Possible causes**

After the time specified by **expireTime** elapses, service updates messages are not allowed.

**Solution**

Set **expireTime** properly and push the message again.

## 82600017 No Authorized Device

**Message**

no authorization device.

**Description**

The user does not have any authorized devices.

**Possible causes**

The user does not have any authorized devices in this scenario.

**Solution**

Add an authorized device for this scenario and push the message again.

## 82600018 Service Updates Event Ended

**Message**

event already closed.

**Description**

The service updates event has ended.

**Possible causes**

The event has ended. No more messages can be sent.

**Solution**

Create a new service updates event to push messages.

## 82600019 Active Authorization Code Quantity Exceeds Upper Limit

**Message**

code reached upper limit.

**Description**

The number of active authorization codes exceeds the upper limit.

**Possible causes**

The number of authorization codes pushed to the same user exceeds the upper limit (20).

**Solution**

Reduce the number of authorization codes pushed to the same user to be within 20.
