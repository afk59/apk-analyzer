# AntifraudPicker

This module provides APIs for apps to obtain fraudulent messages and call logs for anti-fraud purposes.

**Start version**: 5.0.3(15)

#### Module Import

import {antifraudPicker} from '@kit.DeviceSecurityKit';

#### AntifraudMessageOptions

Request parameters for obtaining fraudulent messages.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxSelectNumber

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of items that can be selected. If no value is passed, the default value **50** is used. The value ranges from 1 to 50.

 |

#### SingleAntifraudMessageInfo

Information about a fraudulent message.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

senderNumber

 | 

string

 | 

No

 | 

No

 | 

Mobile number of a message sender.

 |
| 

receivingTime

 | 

number

 | 

No

 | 

No

 | 

Timestamp when a message is received, in milliseconds.

 |
| 

messageContent

 | 

string

 | 

No

 | 

No

 | 

Message content, which contains a maximum of 17,152 characters.

 |
| 

senderName

 | 

string

 | 

No

 | 

No

 | 

Sender name.

 |
| 

senderPlace

 | 

string

 | 

No

 | 

No

 | 

Home area of the mobile number of a message sender.

 |
| 

messageType

 | 

string

 | 

No

 | 

No

 | 

Message type. The options are as follows: **0**: SMS message; **1**: MMS message.

 |
| 

mmsSubject

 | 

string

 | 

No

 | 

Yes

 | 

Subject of an MMS message. This parameter is valid only when the message type is MMS.

 |
| 

mmsAttachments

 | 

[MmsAttachmentInfo](#section14579643718)\[\]

 | 

No

 | 

Yes

 | 

MMS attachment information list. This parameter is valid only when the message type is MMS.

 |

#### MmsAttachmentInfo

MMS attachment information.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

attachmentType

 | 

number

 | 

No

 | 

No

 | 

MMS attachment type. The options are as follows:

-   **\-1**: MMS message not downloaded
-   **0**: SMIL file
-   **1**: image
-   **2**: video
-   **3**: audio
-   **4**: contact card
-   **5**: theme
-   **6**: slide
-   **7**: text
-   **8**: location

 |
| 

uri

 | 

string

 | 

No

 | 

No

 | 

Attachment URI.

 |

#### AntifraudMessageResult

Fraudulent messages.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

messageInfo

 | 

[SingleAntifraudMessageInfo](#section143653475548)\[\]

 | 

No

 | 

No

 | 

Fraudulent message list.

 |

#### SingleAntifraudCallLogInfo

Information about a fraudulent call log.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

callerNumber

 | 

string

 | 

No

 | 

No

 | 

Calling number.

 |
| 

receivingTime

 | 

number

 | 

No

 | 

No

 | 

Timestamp when a call is answered, in milliseconds.

 |
| 

callLogType

 | 

number

 | 

No

 | 

No

 | 

Call log type. The options are as follows: **0**: incoming call; **1**: outgoing call.

 |
| 

callerName

 | 

string

 | 

No

 | 

No

 | 

Calling party name.

 |
| 

callDuration

 | 

number

 | 

No

 | 

No

 | 

Call duration, in milliseconds.

 |

#### AntifraudCallLogResult

Fraudulent call logs.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

callLogInfo

 | 

[SingleAntifraudCallLogInfo](#section123791738142115)\[\]

 | 

No

 | 

No

 | 

Fraudulent call log list.

 |

#### AntifraudCallLogOptions

Request parameters for obtaining fraudulent call logs.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxSelectNumber

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of items that can be selected. If no value is passed, the default value **50** is used. The value ranges from 1 to 50.

 |

#### selectFraudMessage

selectFraudMessage(context: common.Context, options?: [AntifraudMessageOptions](#section11617213173419)): Promise<[AntifraudMessageResult](#section1874123611170)\>

Starts the fraudulent message picker and obtains the information about fraudulent messages selected by a user. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

App context.

 |
| 

options

 | 

[AntifraudMessageOptions](#section11617213173419)

 | 

No

 | 

Request parameters. If no value is passed, the maximum number of items that can be selected is **50** by default.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AntifraudMessageResult](#section1874123611170)\>

 | 

Promise used to return fraudulent messages.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied. Interface caller does not have permission "ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER".

 |
| 

401

 | 

Input parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1017100001

 | 

Unknown error.

 |
| 

1017100002

 | 

The device type is not supported.

 |

**Example:**

import { antifraudPicker} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

const TAG = "AntifraudPickerJsTest";

// Request to obtain the fraudulent message information and process the service.
let options: antifraudPicker.AntifraudMessageOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudMessage begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudMessageResult = await antifraudPicker.selectFraudMessage(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudMessage failed: %{public}d %{public}s', e.code, e.message);
}

#### selectFraudCallLog

selectFraudCallLog(context: common.Context, options?: [AntifraudCallLogOptions](#section27151161387)): Promise<[AntifraudCallLogResult](#section1746504983517)\>

Starts the fraudulent call log picker and obtains the information about fraudulent call logs selected by a user. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.0.3(15)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

App context.

 |
| 

options

 | 

[AntifraudCallLogOptions](#section27151161387)

 | 

No

 | 

Request parameters. If no value is passed, the maximum number of items that can be selected is **50** by default.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AntifraudCallLogResult](#section1746504983517)\>

 | 

Promise used to return fraudulent call logs.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied. Interface caller does not have permission "ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER".

 |
| 

401

 | 

Input parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1017100001

 | 

Unknown error.

 |
| 

1017100002

 | 

The device type is not supported.

 |

**Example:**

import { antifraudPicker} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

const TAG = "AntifraudPickerJsTest";

// Request to obtain the fraudulent call log information and process the service.
let options: antifraudPicker.AntifraudCallLogOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudCallLog begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudCallLogResult = await antifraudPicker.selectFraudCallLog(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudCallLog failed: %{public}d %{public}s', e.code, e.message);
}

#### AntifraudAppOptions

Request parameters for obtaining fraudulent apps.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.1.1(19)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxSelectNumber

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of items that can be selected. If no value is passed, the default value **50** is used. The value ranges from 1 to 50.

 |

#### AntifraudAppResult

Obtained fraudulent app result.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.1.1(19)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

appInfo

 | 

[SingleAntifraudAppInfo](#section244421110162)\[\]

 | 

No

 | 

No

 | 

Fraudulent app list.

 |

#### SingleAntifraudAppInfo

Information about a fraudulent app.

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.1.1(19)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

applicationName

 | 

string

 | 

No

 | 

No

 | 

Application program name.

 |
| 

bundleName

 | 

string

 | 

No

 | 

No

 | 

App package name.

 |
| 

versionCode

 | 

number

 | 

No

 | 

No

 | 

App version code.

 |
| 

versionName

 | 

string

 | 

No

 | 

No

 | 

App version name.

 |
| 

installTime

 | 

number

 | 

No

 | 

No

 | 

Timestamp when an app is installed, in milliseconds.

 |
| 

appId

 | 

string

 | 

No

 | 

No

 | 

App ID.

 |
| 

label

 | 

string

 | 

No

 | 

No

 | 

App name displayed to users, for example, **Clock**.

 |
| 

installSource

 | 

string

 | 

No

 | 

No

 | 

Installation source of the app. The options are as follows:

\- **pre-installed**: The app is a preset app installed at initial device startup.

\- **ota**: The app is a preset app added during system upgrade.

\- **recovery**: The preset app is uninstalled and then restored.

\- _App package name_: The app is installed from the specified package.

\- **unknown**: The installation source is unknown.

 |

#### selectFraudApp

selectFraudApp(context: common.Context, options?: [AntifraudAppOptions](#section1550072910133)): Promise<[AntifraudAppResult](#section13366182610149)\>

Starts the fraudulent app picker and obtains the information about fraudulent apps selected by a user. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.USE\_FRAUD\_APP\_PICKER

**System capability**: SystemCapability.Security.Antifraud

**Start version**: 5.1.1(19)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

App context.

 |
| 

options

 | 

[AntifraudAppOptions](#section1550072910133)

 | 

No

 | 

Request parameters. If no value is passed, the maximum number of items that can be selected is **50** by default.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AntifraudAppResult](#section13366182610149)\>

 | 

Promise used to return fraudulent apps.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied. Interface caller does not have permission "ohos.permission.USE\_FRAUD\_APP\_PICKER".

 |
| 

1017600001

 | 

Unknown error.

 |
| 

1017600002

 | 

The device type is not supported.

 |
| 

1017600003

 | 

Parameter verification failed.

 |

**Example:**

import { antifraudPicker} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

const TAG = "AntifraudPickerJsTest";

// Request to obtain the fraudulent app information and process the service.
let options: antifraudPicker.AntifraudAppOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudApp begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudAppResult = await antifraudPicker.selectFraudApp(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudApp failed: %{public}d %{public}s', e.code, e.message);
}
