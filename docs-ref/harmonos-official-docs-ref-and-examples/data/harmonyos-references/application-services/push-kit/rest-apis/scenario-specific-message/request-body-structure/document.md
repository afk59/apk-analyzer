# Request Body Structure

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.1.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.1.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; Push Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.1.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://push-api.cloud.huawei.com/v3/<strong>[projectId]</strong>/messages:send</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>In the URL, <strong>[projectId]</strong> indicates the project ID. To obtain the project ID, sign in to <a href="https://developer.huawei.com/consumer/en/service/josp/agc/index.html" target="_blank">AppGallery Connect</a>, click <span class="wintitle"><b>Development and services</b></span>, click the desired project, and go to the <span class="wintitle"><b>Project settings</b></span> page.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.1.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Content-Type: application/json</p></td></tr></tbody></table>

#### Request Header

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

Authentication mode: **JWT**

CAUTION:

HarmonyOS 5 and later versions no longer support OAuth 2.0-based authentication.

For details, please refer to [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token).

NOTE:

You are advised to set the JWT validity period to 3600 seconds, within which a JWT can be reused.

This parameter value is **Bearer** followed by a space character and then the obtained authentication information.

 | 

Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*

 |
| 

push-type

 | 

Message type. The options are as follows:

**0**: alert message (notification message)

**1**: widget update message

**2**: text-to-speech message

**6**: background message

**7**: live view message

**10**: in-app call message

 | 

0

 |

#### Request Body

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

payload

 | 

Yes

 | 

Object

 | 

Message structure. The **payload** definition varies depending on the **push-type** value:

-   **0**: [AlertPayload](../request-body-parameters/document.md#section1152516418157) (notification message)
-   **1**: [FormUpdatePayload](../request-body-parameters/document.md#section6471174713249) (widget update message)
-   **2**: [ExtensionPayload](../request-body-parameters/document.md#section161192514234) (text-to-speech message)
-   **6**: [BackgroundPayload](../request-body-parameters/document.md#section056120245274) (background message)
-   **7**: [LiveViewPayload](../request-body-parameters/document.md#section66881469306) (live view message)
-   **10**: [VoIPCallPayload](../request-body-parameters/document.md#section146341550144011) (in-app call message)

 |
| 

pushOptions

 | 

No

 | 

Object

 | 

Sending control parameter. For details, please refer to [pushOptions](../request-body-parameters/document.md#section418321011212).

 |
| 

target

 | 

Yes

 | 

Object

 | 

Sending target. For details, please refer to [target](../request-body-parameters/document.md#section1344624991218).

 |
