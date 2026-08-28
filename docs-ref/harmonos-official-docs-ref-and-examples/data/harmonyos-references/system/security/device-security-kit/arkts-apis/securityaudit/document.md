# SecurityAudit

Unified security audit data subscription and unsubscription APIs are provided for apps to obtain security audit data on a device.

**Start version**: 5.0.0(12)

#### Module Import

import { securityAudit } from '@kit.DeviceSecurityKit';

#### AuditEventInfo

Request parameter of the subscription or unsubscription API.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 5.0.0(12)

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

eventId

 | 

number

 | 

No

 | 

No

 | 

Audit event ID, which specifies the security audit data to be obtained. Example: 0x810800800.

The value range of the audit event ID is \[0, 0xFFFFFFFFF\].

 |

#### AuditEvent

Security audit data.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 5.0.0(12)

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

eventId

 | 

number

 | 

No

 | 

No

 | 

Audit event ID, which is the same as that in the request.

 |
| 

version

 | 

string

 | 

No

 | 

Yes

 | 

Audit event version number.

 |
| 

timestamp

 | 

string

 | 

No

 | 

Yes

 | 

Time when an audit event occurs. The value is in _YYYYMMDDHHMMSS_ format.

 |
| 

content

 | 

string

 | 

No

 | 

Yes

 | 

Audit event content. Different audit events have different contents. The value is a JSON string, for example, **{"type": 1}**.

 |
| 

userId

 | 

number

 | 

No

 | 

Yes

 | 

Sign-in user ID when an audit event occurs.

 |
| 

deviceId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the device where an audit event occurs.

 |
| 

metadata

 | 

string

 | 

No

 | 

Yes

 | 

Audit event metadata, including the event version number, time when an event is received, device ID, and user ID.

**Start version**: 6.0.0(20)

 |

#### NotifyEvent

Enumerates notification events.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PASTEBOARD

 | 

0x27000000

 | 

Clipboard copy and paste events.

 |
| 

FILE

 | 

0x1C000007

 | 

File event.

 |
| 

FILE\_INTERCEPTED

 | 

0x1C001100

 | 

File access rule violation event.

 |
| 

ACCOUNT

 | 

0x10000100

 | 

Sign-in or sign-out event.

 |
| 

WINDOW

 | 

0x07000000

 | 

Screenshot, screen recording, or screen projection event.

 |
| 

VOLUME

 | 

0x0F000000

 | 

Insertion or removal event of a removable storage device.

 |
| 

PRINTER

 | 

0x2E000000

 | 

Printer event.

 |
| 

PROCESS

 | 

0x1C000008

 | 

Process creation or exit event.

 |
| 

NETWORK\_TRAFFIC

 | 

0x1C00000E

 | 

Network traffic event.

 |
| 

NETWORK\_CONN

 | 

0x1C00000F

 | 

Network connection event.

 |
| 

CAMERA

 | 

0x2D000000

 | 

Camera event.

 |
| 

APP

 | 

0x10000000

 | 

App event.

 |
| 

EDM

 | 

0x11000000

 | 

Enterprise device management event.

 |
| 

CERT

 | 

0x12003000

 | 

Certificate operation event.

 |
| 

KIA\_CREATE

 | 

0x1C00000B

 | 

KIA file creation event.

 |
| 

KIA\_READ

 | 

0x1C000012

 | 

KIA file read event.

 |
| 

KIA\_VARIANT

 | 

0x1C00000C

 | 

KIA file variation event.

 |
| 

KIA\_INTERCEPT

 | 

0x1C00000A

 | 

KIA file interception event.

 |
| 

PERMISSION

 | 

0x0B000000

 | 

App permission change event.

 |
| 

DNS

 | 

0x03000001

 | 

DNS audit event.

 |
| 

APP\_INSTALL\_INTERCEPTED

 | 

0x18000100

 | 

App installation interception event.

 |
| 

APP\_UNINSTALL\_INTERCEPTED

 | 

0x18000101

 | 

App uninstallation interception event.

 |
| 

APP\_UPDATE\_INTERCEPTED

 | 

0x18000102

 | 

App update interception event.

 |
| 

APP\_RECOVER\_INTERCEPTED

 | 

0x18000103

 | 

App recovery interception event.

 |
| 

APP\_START\_INTERCEPTED

 | 

0x18000104

 | 

App startup interception event.

 |
| 

USB\_ACCESS\_INTERCEPTED

 | 

0x30000000

 | 

USB access interception event.

 |

#### FilterType

Enumerates event filter types.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

EVENT\_TYPE\_EQUAL

 | 

0x00000100

 | 

Event type filter.

 |
| 

EVENT\_SUBTYPE\_EQUAL

 | 

0x00000200

 | 

Event subtype filter.

 |
| 

FILE\_PATH\_EQUAL

 | 

0x00010000

 | 

File path filter.

 |
| 

FILE\_PATH\_PREFIX

 | 

0x00010001

 | 

File path prefix filter.

 |
| 

FILE\_PATH\_SUFFIX

 | 

0x00010002

 | 

File path suffix filter.

 |
| 

PROCESS\_UID\_EQUAL

 | 

0x00020000

 | 

Process UID filter.

 |
| 

PROCESS\_PID\_EQUAL

 | 

0x00020100

 | 

Process ID filter.

 |
| 

PROCESS\_NAME\_EQUAL

 | 

0x00020200

 | 

Process name filter.

 |
| 

PROCESS\_NAME\_PREFIX

 | 

0x00020201

 | 

Process name prefix filter.

 |
| 

PROCESS\_NAME\_SUFFIX

 | 

0x00020202

 | 

Process name suffix filter.

 |

#### AuthEvent

Enumerates authentication events.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

FILE\_CREATE

 | 

0x1C801100

 | 

File creation authentication event.

 |
| 

FILE\_OPEN

 | 

0x1C801101

 | 

File opening authentication event.

 |
| 

FILE\_RENAME

 | 

0x1C801102

 | 

File renaming authentication event.

 |
| 

FILE\_DELETE

 | 

0x1C801103

 | 

File deletion authentication event.

 |
| 

FILE\_SETEXTATTR

 | 

0x1C801104

 | 

Authentication event for extended file attribute setting.

 |
| 

FILE\_DELETEEXTATTR

 | 

0x1C801105

 | 

Authentication event for extended file attribute deletion.

 |

#### AuthResult

Enumerates authentication results.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ALLOW

 | 

0

 | 

Allows an authentication event.

 |
| 

DENY

 | 

1

 | 

Denies an authentication event.

 |

#### on('auditEventOccur')

on(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](#section1962713117486), callback: Callback<[AuditEvent](#section5557545175113)\>): void

Subscribes to security audit data.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

Subscribed event type. This parameter has a fixed value of **auditEventOccur**, indicating audit events.

 |
| 

auditEventInfo

 | 

[AuditEventInfo](#section1962713117486)

 | 

Yes

 | 

Subscribed audit data.

 |
| 

callback

 | 

Callback<[AuditEvent](#section5557545175113)\>

 | 

Yes

 | 

Callback function for receiving audit events.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

401

 | 

invalid parameters.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId);
};
let auditEventInfo: securityAudit.AuditEventInfo = {
   eventId: 0x810800800
};

try {
  hilog.info(0x0000, TAG, 'on begin.');
  securityAudit.on('auditEventOccur', auditEventInfo, callback);
  hilog.info(0x0000, TAG, 'Succeeded in on.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'on failed: %{public}d %{public}s', e.code, e.message);
}

#### off('auditEventOccur')

off(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](#section1962713117486), callback?: Callback<[AuditEvent](#section5557545175113)\>): void

Unsubscribes from security audit data.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

Unsubscribed event type. This parameter has a fixed value of **auditEventOccur**, indicating audit events.

 |
| 

auditEventInfo

 | 

[AuditEventInfo](#section1962713117486)

 | 

Yes

 | 

Unsubscribed audit data.

 |
| 

callback

 | 

Callback<[AuditEvent](#section5557545175113)\>

 | 

No

 | 

Callback function for receiving audit data. If a callback is passed, the subscription to this callback is canceled. If no callback is passed, subscriptions to all callbacks are canceled.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

401

 | 

invalid parameters.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuditJsTest";
let auditEventInfo: securityAudit.AuditEventInfo = {
   eventId: 0x810800800
};

try {
  hilog.info(0x0000, TAG, 'off begin.');
  securityAudit.off('auditEventOccur', auditEventInfo);
  hilog.info(0x0000, TAG, 'Succeeded in off.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message);
}

#### Filter

Filter information provided by you.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

isInclude

 | 

boolean

 | 

No

 | 

No

 | 

Filter flag, which determines whether events that meet the filter are returned to the subscriber.

**true**: The filter is a negative filter. Events that meet the negative filter are returned to the subscriber.

**false**: The filter is a positive filter. Events that meet the positive filter are not returned to the subscriber.

 |
| 

type

 | 

[FilterType](#section141981957164611)

 | 

No

 | 

No

 | 

Filter type.

 |
| 

values

 | 

string\[\]

 | 

No

 | 

No

 | 

Array of filter values.

 |

#### Client

Provides conditions for a notification client.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/LeNNgK1eTYif8eYL5RcPxQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9577C477FAC27D84CDCBD31ED8C0A3365AFFE51344FC48DEFA644AC04A63593)

You need to use [newClient](#section1137616421363) to construct an instance.

#### \[h2\]subscribe

subscribe(events: NotifyEvent\[\]): void

Subscribes to notification events.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

events

 | 

[NotifyEvent](#section116663494309)\[\]

 | 

Yes

 | 

Notification events to be subscribed to.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest"; 
const callback = (event: securityAudit.AuditEvent) => { 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
}; 
try { 
  client = securityAudit.newClient(callback);
  client?.subscribe(\[0x02D000000\]);
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message); 
}

#### \[h2\]unsubscribe

unsubscribe(events: NotifyEvent\[\]): void

Unsubscribes from notification events.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

events

 | 

[NotifyEvent](#section116663494309)\[\]

 | 

Yes

 | 

Subscribed notification events.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest"; 
const callback = (event: securityAudit.AuditEvent) => { 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
}; 
try { 
  client = securityAudit.newClient(callback);
  client?.unsubscribe(\[0x02D000000\]);
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message); 
}

#### \[h2\]addFilter

addFilter(event: NotifyEvent, filter: Filter): void

Adds a filter for a notification event. Whether events meeting the filter are returned to the subscriber is determined by the filter flag.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

event

 | 

[NotifyEvent](#section116663494309)

 | 

Yes

 | 

Notification event ID.

 |
| 

filter

 | 

[Filter](#section17889177696)

 | 

Yes

 | 

Notification event filter.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000004

 | 

The number of filters exceeds the upper limit.

 |
| 

1012000005

 | 

The event does not support the filter condition.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest"; 
const callback = (event: securityAudit.AuditEvent) => { 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
}; 
let filter : securityAudit.Filter = {
  type: 0x00000200,
  isInclude: true,
  values : \["2"\]
};
try { 
  client = securityAudit.newClient(callback);
  client?.addFilter(0x02D000000, filter);
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message); 
}

#### \[h2\]removeFilter

removeFilter(event: NotifyEvent, filter: Filter): void

Deletes a filter of a notification event. After the deletion, events meeting the filter will no longer be processed based on the filter flag.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

event

 | 

[NotifyEvent](#section116663494309)

 | 

Yes

 | 

Notification event ID.

 |
| 

filter

 | 

[Filter](#section17889177696)

 | 

Yes

 | 

Notification event filter.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000005

 | 

The event does not support the filter condition.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest"; 
const callback = (event: securityAudit.AuditEvent) => { 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
}; 
let filter : securityAudit.Filter = {
  type: 0x00000200,
  isInclude: true,
  values : \["2"\]
};
try { 
  client = securityAudit.newClient(callback);
  client?.removeFilter(0x02D000000, filter);
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message); 
}

#### newClient

newClient(callback: Callback<[AuditEvent](#section5557545175113)\>): Client

Creates a notification client. The methods provided by the client can be used to subscribe to and filter notification events.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

callback

 | 

Callback<[AuditEvent](#section5557545175113)\>

 | 

Yes

 | 

Callback function for receiving audit data.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Client](#section119445151153)

 | 

Notification client instance.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000002

 | 

The number of clients exceeds the global upper limit.

 |
| 

1012000003

 | 

The number of clients exceeds the current process upper limit.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest"; 
const callback = (event: securityAudit.AuditEvent) => { 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
}; 
try { 
  client = securityAudit.newClient(callback);
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'newClient failed: %{public}d %{public}s', e.code, e.message); 
}

#### deleteClient

deleteClient(client: Client): void

Deletes a notification client. After the deletion, the methods provided by the client can no longer be used, and the subscription and filtering information recorded by the client will be cleared.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

client

 | 

[Client](#section119445151153)

 | 

Yes

 | 

Notification client information.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest"; 
const callback = (event: securityAudit.AuditEvent) => { 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
}; 
try { 
  client = securityAudit.newClient(callback);
  securityAudit.deleteClient(client);
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'deleteClient failed: %{public}d %{public}s', e.code, e.message); 
}

#### AuthClient

Provides conditions for an authentication client.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/SgkZbCFyQoG4upFewMEKHw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F6D3E1EBC548482C40E069F50309386AFE5E188519E4A434868C0CF13B8C425)

You need to use [newAuthClient](#section1768135711112) to construct an instance.

#### \[h2\]subscribe

subscribe(events: AuthEvent\[\]): void

Subscribes to authentication events.

**Required permission**: ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

events

 | 

[AuthEvent](#section131951026124112)\[\]

 | 

Yes

 | 

Authentication events to be subscribed to.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.subscribe(\[securityAudit.AuthEvent.FILE\_CREATE\]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}

#### \[h2\]unsubscribe

unsubscribe(events: AuthEvent\[\]): void

Unsubscribes from authentication events.

**Required permission**: ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

events

 | 

[AuthEvent](#section131951026124112)\[\]

 | 

Yes

 | 

Subscribed authentication events.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.subscribe(\[securityAudit.AuthEvent.FILE\_CREATE\]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.unsubscribe(\[securityAudit.AuthEvent.FILE\_CREATE\]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
}

#### \[h2\]addFilter

addFilter(event: AuthEvent, filter: Filter): void

Adds a filter for an authentication event. Whether events meeting the filter are returned to the subscriber is determined by the filter flag.

**Required permission**: ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

event

 | 

[AuthEvent](#section131951026124112)

 | 

Yes

 | 

Authentication event ID.

 |
| 

filter

 | 

[Filter](#section17889177696)

 | 

Yes

 | 

Authentication event filter.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000004

 | 

The number of filters exceeds the upper limit.

 |
| 

1012000005

 | 

The event does not support the filter condition.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
let filter : securityAudit.Filter = {
  type: securityAudit.FilterType.PROCESS\_PID\_EQUAL,
  isInclude: true,
  values : \["2"\]
};
try {
  authClient?.addFilter(securityAudit.AuthEvent.FILE\_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}

#### \[h2\]removeFilter

removeFilter(event: AuthEvent, filter: Filter): void

Deletes a filter of an authentication event. After the deletion, events meeting the filter will no longer be processed based on the filter flag.

**Required permission**: ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

event

 | 

[AuthEvent](#section131951026124112)

 | 

Yes

 | 

Authentication event ID.

 |
| 

filter

 | 

[Filter](#section17889177696)

 | 

Yes

 | 

Authentication event filter.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000005

 | 

The event does not support the filter condition.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
let filter : securityAudit.Filter = {
  type: securityAudit.FilterType.PROCESS\_PID\_EQUAL,
  isInclude: true,
  values : \["2"\]
};
try {
  authClient?.addFilter(securityAudit.AuthEvent.FILE\_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.removeFilter(securityAudit.AuthEvent.FILE\_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
}

#### \[h2\]auth

auth(auditEvent: AuditEvent, authResult: AuthResult): void

Sets the authentication result of an authentication event. The audit module will allow or deny an event based on the authentication result.

**Required permission**: ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

auditEvent

 | 

[AuditEvent](#section5557545175113)

 | 

Yes

 | 

Authentication event information.

 |
| 

authResult

 | 

[AuthResult](#section10801114725511)

 | 

Yes

 | 

Authentication result.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000007

 | 

The auth event cannot be found.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const allowEventCallback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
  try {
    authClient?.auth(event, securityAudit.AuthResult.ALLOW);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'allowEventCallback', 'auth error:' + e.code);
  }
};
try {
  authClient = securityAudit.newAuthClient(allowEventCallback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}

#### newAuthClient

newAuthClient(callback: Callback<[AuditEvent](#section5557545175113)\>): AuthClient

Creates an authentication client. The methods provided by the client can be used to subscribe to, filter, and authenticate authentication events.

**Required permission**: ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

callback

 | 

Callback<[AuditEvent](#section5557545175113)\>

 | 

Yes

 | 

Callback function for receiving audit data.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AuthClient](#section85535761112)

 | 

Authentication client instance.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000002

 | 

The number of clients exceeds the global upper limit.

 |
| 

1012000003

 | 

The number of clients exceeds the current process upper limit.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}

#### deleteAuthClient

deleteAuthClient(client: AuthClient): void

Deletes an authentication client. After the deletion, the methods provided by the client can no longer be used, and the subscription and filtering information recorded by the client will be cleared.

**Required permission**: ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

client

 | 

[AuthClient](#section85535761112)

 | 

Yes

 | 

Authentication client information.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  securityAudit.deleteAuthClient(authClient);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'deleteAuthClient failed: %{public}d %{public}s', e.code, e.message);
}

#### queryAllProcesses

queryAllProcesses(): string;

Queries the information about all app processes.

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

App process information, which is a JSON string. Example: **{"1": {}}**.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit'; 
import { BusinessError } from '@kit.BasicServicesKit'; 
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditJsTest"; 
try { 
  hilog.info(0x0000, TAG, 'queryAllProcesses begin.'); 
  const result = securityAudit.queryAllProcesses();
  hilog.info(0x0000, TAG, 'Succeeded in queryAllProcesses.'); 
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'queryAllProcesses failed: %{public}d %{public}s', e.code, e.message); 
}

#### queryProcesses

queryProcesses(pids: number\[\]): string;

Queries the information about app processes with the specified process IDs (PIDs).

**Required permission**: ohos.permission.QUERY\_AUDIT\_EVENT

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

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

pids

 | 

number\[\]

 | 

Yes

 | 

IDs of the processes to be queried.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

App process information, which is a JSON string. Example: **{"1": {}}**.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/securityaudit/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

check permission fail.

 |
| 

1012000001

 | 

Internal error.

 |
| 

1012000006

 | 

The number of queried processes exceeds the threshold.

 |

**Example:**

import { securityAudit } from '@kit.DeviceSecurityKit'; 
import { BusinessError } from '@kit.BasicServicesKit'; 
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditJsTest"; 
let pids: number\[\] = \[1, 2\];
try { 
  hilog.info(0x0000, TAG, 'queryProcesses begin.'); 
  const result = securityAudit.queryProcesses(pids);
  hilog.info(0x0000, TAG, 'Succeeded in queryProcesses.'); 
} catch (err) { 
  let e: BusinessError = err as BusinessError; 
  hilog.error(0x0000, TAG, 'queryProcesses failed: %{public}d %{public}s', e.code, e.message); 
}
