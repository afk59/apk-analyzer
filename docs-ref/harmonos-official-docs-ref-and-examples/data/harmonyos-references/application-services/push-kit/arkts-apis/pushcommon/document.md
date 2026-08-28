# pushCommon

This module provides common information of Push Kit, including the bound account type, scenario-specific message data **PushPayload**, extended notification data, target content for an extended notification, data configured for the event to be triggered upon message tapping, and in-app call message data.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.0.0(10)

#### Module Import

import { pushCommon } from '@kit.PushKit';

#### AppProfileType

Enumerated values of the bound account type.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this enumeration is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this enumeration is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this enumeration is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PROFILE\_TYPE\_OS\_DISTRIBUTED\_ACCOUNT

 | 

1

 | 

HUAWEI ID.

 |
| 

PROFILE\_TYPE\_APPLICATION\_ACCOUNT

 | 

2

 | 

Account in the app's own account system.

 |

#### PushPayload

An app can use [receiveMessage](../pushservice/document.md#section125883044911)() to obtain the parameter definition of scenario-specific message data.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Type of the message sent to the ability. The options are as follows:

**IM**: text-to-speech message

**VoIP**: in-app call message

**BACKGROUND**: background message

**EMERGENCY**: emergency event message

**ALERT**: notification message

 |
| 

data

 | 

string

 | 

No

 | 

No

 | 

Data transferred to the Ability.

-   When **type** is set to **IM**, a value example of **data** (formatted) is as follows:
    
    {
        "data": "extraData", **// The value of data equals that of extraData contained in payload of the REST API.**
        "header": {
            "token": "MA\*\*"
        },
        "messageAction": 0,
        "notification": {
            "bigBody": "bigBodyXX",
            "bigTitle": "bigTitleXX",
            "body": "bodyXX",
            "data": "",
            "image": "https://\*\*/image\*\*.png",
            "notifyId": -1,
            "title": "titleXX"
        }
    }
    
-   When **type** is set to **VoIP**, **BACKGROUND**, or **EMERGENCY**, a value example of **data** (formatted) is as follows:
    
    {
        "data": "extraData", **// The value of data equals that of extraData contained in payload of the REST API.**
        "header": {
            "token": "MA\*\*"
        }
    }
    
-   When **type** is set to **ALERT**, you do not need to set the **data** parameter.
    
    For details about the notification fields, see the [Notification](../../rest-apis/scenario-specific-message/request-body-parameters/document.md#section17371529101117) struct in **AlertPayload** (notification message).
    
    {
        "data": "", // Pass an empty string.
        "header": {
            "token": "MA\*\*"
        },
        "messageAction": 0,
        "notification": {
            // For details about the notification fields, see the **Notification** struct in **AlertPayload** (notification message).
        }
    }
    

 |

#### RemoteNotificationInfo

Extended notification data, which is inherited from [PushPayload](#section16335431712).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

number

 | 

No

 | 

No

 | 

Notification ID.

 |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Message type transferred to [RemoteNotificationExtensionAbility](../remotenotificationextensionability/document.md). This parameter is inherited from [PushPayload](#section16335431712).

 |
| 

data

 | 

string

 | 

No

 | 

No

 | 

Data transferred to [RemoteNotificationExtensionAbility](../remotenotificationextensionability/document.md). This parameter is inherited from [PushPayload](#section16335431712).

 |

#### RemoteNotificationContent

Target content of an extended notification.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

No

 | 

Yes

 | 

Title of an extended notification.

NOTE:

The **title** parameter is optional since version 5.0.0(12).

 |
| 

text

 | 

string

 | 

No

 | 

Yes

 | 

Content of an extended notification.

NOTE:

The **text** parameter is optional since version 5.0.0(12).

 |
| 

overlayIcon

 | 

image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

Yes

 | 

Overlay icon of an extended notification.

NOTE:

It is recommended that the image width x height be less than 128 x 128 pixels. Images larger than 49,152 pixels will not be displayed.

 |
| 

badgeNumber

 | 

number

 | 

No

 | 

Yes

 | 

Badge number increment (but not the actual badge number displayed) during the display of an extended notification. The value range is (0, 100).

 |
| 

setBadgeNumber

 | 

number

 | 

No

 | 

Yes

 | 

Badge number displayed for an extended notification. The value range is \[0, 100). If both this parameter and **badgeNumber** are returned, this parameter takes precedence over **badgeNumber**.

NOTE:

Start version: 5.0.0(12).

 |
| 

wantAgent

 | 

[RemoteWantAgent](#section122049160211)

 | 

No

 | 

Yes

 | 

Data configured for the action to be triggered upon message tapping.

 |

#### RemoteWantAgent

Data configured for the action to be triggered upon message tapping.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

abilityName

 | 

string

 | 

No

 | 

No

 | 

Custom page name.

 |
| 

parameters

 | 

Record<string, Object>

 | 

No

 | 

Yes

 | 

Data transferred to an app.

 |

#### VoIPInfo

In-app call message data, which is inherited from [PushPayload](#section16335431712).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

callId

 | 

string

 | 

No

 | 

No

 | 

Unique ID of a call.

 |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Message type transferred to [VoIPExtensionAbility](../voipextensionability/document.md). This parameter is inherited from [PushPayload](#section16335431712).

 |
| 

data

 | 

string

 | 

No

 | 

No

 | 

Data transferred to [VoIPExtensionAbility](../voipextensionability/document.md). This parameter is inherited from [PushPayload](#section16335431712).

 |
