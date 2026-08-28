# SecurityAudit

#### Overview

This module provides security audit APIs.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[security\_audit.h](../../header-files/security-audit-h/document.md)

 | 

Defines the security audit functions.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [SecurityAudit\_Event](../../structs/securityaudit-event/document.md)

 | 

Defines the audit event information.

 |
| 

struct [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md)

 | 

Provides filters.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef void(\* [SecurityAudit\_Handler](#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370)) (const [SecurityAudit\_Event](../../structs/securityaudit-event/document.md) \*events, uint64\_t count)

 | 

Defines an event processing function.

 |
| 

typedef struct SecurityAudit\_AuthClient\_Impl [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868)

 | 

Defines an authentication event management client.

 |
| 

typedef struct SecurityAudit\_Client\_Impl [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974)

 | 

Defines a notification event management client.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) {

SECURITY\_AUDIT\_NOTIFY\_EVENT\_PASTEBOARD = 0x27000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE = 0x1C000007, SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED = 0x2700003C, SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT = 0x10000100,

SECURITY\_AUDIT\_NOTIFY\_EVENT\_WINDOW = 0x07000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_VOLUME = 0x0F000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINTER = 0x2E000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS = 0x1C000008,

SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_TRAFFIC = 0x1C00000E, SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_CONN = 0x1C00000F, SECURITY\_AUDIT\_NOTIFY\_EVENT\_CAMERA = 0x2D000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP = 0x10000000,

SECURITY\_AUDIT\_NOTIFY\_EVENT\_EDM = 0x11000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_CERT = 0x12003000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_CREATE = 0x1C00000B, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ = 0x1C000012,

SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_VARIANT = 0x1C00000C, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_INTERCEPT = 0x1C00000A, SECURITY\_AUDIT\_NOTIFY\_EVENT\_PERMISSION = 0x0B000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_DNS = 0x03000001,

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_INSTALL\_INTERCEPTED = 0x18000100, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UNINSTALL\_INTERCEPTED = 0x18000101, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UPDATE\_INTERCEPTED = 0x18000102, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_RECOVER\_INTERCEPTED = 0x18000103,

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_START\_INTERCEPTED = 0x18000104, SECURITY\_AUDIT\_NOTIFY\_EVENT\_USB\_ACCESS\_INTERCEPTED = 0x30000000

}

 | 

Defines the notification event IDs.

 |
| 

[SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) {

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE = 0x1C801100, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_OPEN = 0x1C801101, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_RENAME = 0x1C801102, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETE = 0x1C801103,

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_SETEXTATTR = 0x1C801104, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETEEXTATTR = 0x1C801105

}

 | 

Defines the authentication event IDs.

 |
| 

[SecurityAudit\_FilterType](#en-us_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) {

EVENT\_TYPE\_EQUAL = 0x00000100, EVENT\_SUBTYPE\_EQUAL = 0x00000200, FILE\_PATH\_EQUAL = 0x00010000, FILE\_PATH\_PREFIX = 0x00010001,

FILE\_PATH\_SUFFIX = 0x00010002, PROCESS\_UID\_EQUAL = 0x00020000, PROCESS\_PID\_EQUAL = 0x00020100, PROCESS\_NAME\_EQUAL = 0x00020200,

PROCESS\_NAME\_PREFIX = 0x00020201, PROCESS\_NAME\_SUFFIX = 0x00020202

}

 | 

Defines the filter types.

 |
| 

[SecurityAudit\_AuthResult](#en-us_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) { SECURITY\_AUDIT\_AUTH\_RESULT\_ALLOW = 0, SECURITY\_AUDIT\_AUTH\_RESULT\_DENY = 1 }

 | 

Defines the authentication result types.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_SecurityAudit\_NewClient](#en-us_topic_0000002349017400_ga18d7c9fe5c578d6113c86dd0c09353b4) ([SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*\*client, [SecurityAudit\_Handler](#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

 | 

Creates a notification event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_DeleteClient](#en-us_topic_0000002349017400_ga26838e6288eea1421f03e6130aafd837) ([SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client)

 | 

Deletes a notification event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_Subscribe](#en-us_topic_0000002349017400_ga3530687f761edfb0141f6c17ff3ba4cd) (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, const [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) \*events, uint64\_t count)

 | 

Subscribes to notification events.

 |
| 

int32\_t [HMS\_SecurityAudit\_Unsubscribe](#en-us_topic_0000002349017400_ga208aff2c03535311e85428fbd375d09f) (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, const [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) \*events, uint64\_t count)

 | 

Unsubscribes from notification events.

 |
| 

int32\_t [HMS\_SecurityAudit\_AddFilter](#en-us_topic_0000002349017400_ga292bdf10008513a439d6bb08450328b0) (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Adds a filter for a notification event.

 |
| 

int32\_t [HMS\_SecurityAudit\_RemoveFilter](#en-us_topic_0000002349017400_ga3c7aa36f4cff9a0107bf144f7fbbdcd5) (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Deletes a filter of a notification event.

 |
| 

int32\_t [HMS\_SecurityAudit\_NewAuthClient](#en-us_topic_0000002349017400_gab59201b529a964c3cc7f9ed12ab0330e) ([SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*\*client, [SecurityAudit\_Handler](#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

 | 

Creates an authentication event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_DeleteAuthClient](#en-us_topic_0000002349017400_ga0a518a6380e80f47869a58f9cf14af87) ([SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client)

 | 

Deletes an authentication event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_SubscribeAuthEvent](#en-us_topic_0000002349017400_gab33847480e92d3107a91d76a10b8c82f) (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, const [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) \*events, uint64\_t count)

 | 

Subscribes to authentication events.

 |
| 

int32\_t [HMS\_SecurityAudit\_UnsubscribeAuthEvent](#en-us_topic_0000002349017400_gaebf52f27e5409c29dc3ad0c3eba47783) (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, const [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) \*events, uint64\_t count)

 | 

Unsubscribes from authentication events.

 |
| 

int32\_t [HMS\_SecurityAudit\_AddAuthEventFilter](#en-us_topic_0000002349017400_ga3d9df28411da9cc483c2e82d304cb38e) (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Adds a filter for an authentication event.

 |
| 

int32\_t [HMS\_SecurityAudit\_RemoveAuthEventFilter](#en-us_topic_0000002349017400_gaef069b340e428715c10531885326c079) (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Deletes a filter of an authentication event.

 |
| 

int32\_t [HMS\_SecurityAudit\_Auth](#en-us_topic_0000002349017400_gafbb9c2e5389b79d8def76c530e01e26c) (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, const [SecurityAudit\_Event](../../structs/securityaudit-event/document.md) \*event, [SecurityAudit\_AuthResult](#en-us_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) authResult)

 | 

Sets the authentication result for an audit event.

 |
| 

int32\_t [HMS\_SecurityAudit\_QueryAllProcesses](#en-us_topic_0000002349017400_section0945443114617)(char\*\* result)

 | 

Obtains the information about all app processes.

 |
| 

int32\_t [HMS\_SecurityAudit\_QueryProcesses](#en-us_topic_0000002349017400_section11373745488)(uint64\_t\* pids, uint64\_t count, char\*\* result)

 | 

Obtains the information about app processes with the specified PIDs.

 |

#### Type Definition Description

#### \[h2\]SecurityAudit\_AuthClient

typedef struct SecurityAudit\_AuthClient\_Impl [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868)

**Description**

Defines an authentication event management client.

**Start version**: 6.0.0(20)

#### \[h2\]SecurityAudit\_Client

typedef struct SecurityAudit\_Client\_Impl [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974)

**Description**

Defines a notification event management client.

**Start version**: 6.0.0(20)

#### \[h2\]SecurityAudit\_Handler

typedef void(\* SecurityAudit\_Handler) (const [SecurityAudit\_Event](../../structs/securityaudit-event/document.md) \*events, uint64\_t count)

**Description**

Defines an event processing function.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

events

 | 

Pointer to audit event information.

 |
| 

count

 | 

Number of events in the array.

 |

#### Enumeration Description

#### \[h2\]SecurityAudit\_Auth\_Event

enum [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f)

**Description**

Defines the authentication event IDs.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE

 | 

File creation authentication event.

 |
| 

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_OPEN

 | 

File opening authentication event.

 |
| 

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_RENAME

 | 

File renaming authentication event.

 |
| 

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETE

 | 

File deletion authentication event.

 |
| 

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_SETEXTATTR

 | 

Authentication event for extended file attribute setting.

 |
| 

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETEEXTATTR

 | 

Authentication event for extended file attribute deletion.

 |

#### \[h2\]SecurityAudit\_AuthResult

enum [SecurityAudit\_AuthResult](#en-us_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de)

**Description**

Defines the authentication result types.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

SECURITY\_AUDIT\_AUTH\_RESULT\_ALLOW

 | 

Allowed event.

 |
| 

SECURITY\_AUDIT\_AUTH\_RESULT\_DENY

 | 

Rejected event.

 |

#### \[h2\]SecurityAudit\_FilterType

enum [SecurityAudit\_FilterType](#en-us_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f)

**Description**

Defines the filter types.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

EVENT\_TYPE\_EQUAL

 | 

Event type filter.

 |
| 

EVENT\_SUBTYPE\_EQUAL

 | 

Event subtype filter.

 |
| 

FILE\_PATH\_EQUAL

 | 

File path filter.

 |
| 

FILE\_PATH\_PREFIX

 | 

File path prefix filter.

 |
| 

FILE\_PATH\_SUFFIX

 | 

File path suffix filter.

 |
| 

PROCESS\_UID\_EQUAL

 | 

Process UID filter.

 |
| 

PROCESS\_PID\_EQUAL

 | 

Process ID filter.

 |
| 

PROCESS\_NAME\_EQUAL

 | 

Process name filter.

 |
| 

PROCESS\_NAME\_PREFIX

 | 

Process name prefix filter.

 |
| 

PROCESS\_NAME\_SUFFIX

 | 

Process name suffix filter.

 |

#### \[h2\]SecurityAudit\_Notify\_Event

enum [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea)

**Description**

Defines the notification event IDs.

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_PASTEBOARD

 | 

Clipboard copy and paste events.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE

 | 

File event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED

 | 

File access rule violation event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT

 | 

Sign-in or sign-out event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_WINDOW

 | 

Screenshot, screen recording, or screen projection event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_VOLUME

 | 

Insertion or removal event of a removable storage device.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINTER

 | 

Printer event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS

 | 

Process creation or exit event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_TRAFFIC

 | 

Network traffic event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_CONN

 | 

Network connection event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_CAMERA

 | 

Camera event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP

 | 

App event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_EDM

 | 

Enterprise device management event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_CERT

 | 

Certificate operation event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_CREATE

 | 

KIA file creation event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ

 | 

KIA file read event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_VARIANT

 | 

KIA file variation event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_INTERCEPT

 | 

KIA file interception event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_PERMISSION

 | 

App permission change event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_DNS

 | 

DNS audit event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_INSTALL\_INTERCEPTED

 | 

App installation interception event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UNINSTALL\_INTERCEPTED

 | 

App uninstallation interception event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UPDATE\_INTERCEPTED

 | 

App update interception event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_RECOVER\_INTERCEPTED

 | 

App recovery interception event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_START\_INTERCEPTED

 | 

App startup interception event.

 |
| 

SECURITY\_AUDIT\_NOTIFY\_EVENT\_USB\_ACCESS\_INTERCEPTED

 | 

USB access interception event.

 |

#### Function Description

#### \[h2\]HMS\_SecurityAudit\_AddAuthEventFilter()

int32\_t HMS\_SecurityAudit\_AddAuthEventFilter (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \* client, [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \* filter )

**Description**

Adds a filter for an authentication event.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Authentication event management client that has been created.

 |
| 

event

 | 

Authentication event for which a filter is to be added.

 |
| 

filter

 | 

Authentication event filter description.

 |

**Required permission**:

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned. If the number of filters exceeds the upper limit, **1012000004** is returned. If the event does not support the filter, **1012000005** is returned.

#### \[h2\]HMS\_SecurityAudit\_AddFilter()

int32\_t HMS\_SecurityAudit\_AddFilter (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \* client, [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \* filter )

**Description**

Adds a filter for a notification event.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Notification event management client that has been created.

 |
| 

event

 | 

Event for which a filter is to be added.

 |
| 

filter

 | 

Notification event filter description.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned. If the number of filters exceeds the upper limit, **1012000004** is returned. If the event does not support the filter, **1012000005** is returned.

#### \[h2\]HMS\_SecurityAudit\_Auth()

int32\_t HMS\_SecurityAudit\_Auth (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \* client, const [SecurityAudit\_Event](../../structs/securityaudit-event/document.md) \* event, [SecurityAudit\_AuthResult](#en-us_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) authResult )

**Description**

Sets the authentication result for an audit event.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Authentication event management client that has been created.

 |
| 

event

 | 

Audit authentication event information.

 |
| 

authResult

 | 

Authentication result.

 |

**Required permission**:

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_DeleteAuthClient()

int32\_t HMS\_SecurityAudit\_DeleteAuthClient ([SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \* client)

**Description**

Deletes an authentication event management client.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Authentication event management client instance to be deleted.

 |

**Required permission**:

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_DeleteClient()

int32\_t HMS\_SecurityAudit\_DeleteClient ([SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \* client)

**Description**

Deletes a notification event management client.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Client instance to be deleted.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_NewAuthClient()

int32\_t HMS\_SecurityAudit\_NewAuthClient ([SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*\* client, [SecurityAudit\_Handler](#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler )

**Description**

Creates an authentication event management client.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Pointer to the new authentication event management client instance.

 |
| 

handler

 | 

Handler that processes all messages sent to the client.

 |

**Required permission**:

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned. If the number of clients exceeds the system-wide upper limit, **1012000002** is returned. If the number of clients exceeds the upper limit of the current process, **1012000003** is returned.

#### \[h2\]HMS\_SecurityAudit\_NewClient()

int32\_t HMS\_SecurityAudit\_NewClient ([SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*\* client, [SecurityAudit\_Handler](#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler )

**Description**

Creates a notification event management client.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Pointer to the new client instance.

 |
| 

handler

 | 

Handler that processes all messages sent to the client.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned. If the number of clients exceeds the system-wide upper limit, **1012000002** is returned. If the number of clients exceeds the upper limit of the current process, **1012000003** is returned.

#### \[h2\]HMS\_SecurityAudit\_RemoveAuthEventFilter()

int32\_t HMS\_SecurityAudit\_RemoveAuthEventFilter (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \* client, [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \* filter )

**Description**

Deletes a filter of an authentication event.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Authentication event management client that has been created.

 |
| 

event

 | 

Authentication event for which a filter is to be deleted.

 |
| 

filter

 | 

Authentication event filter description.

 |

**Required permission**:

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned. If the event does not support the filter, **1012000005** is returned.

#### \[h2\]HMS\_SecurityAudit\_RemoveFilter()

int32\_t HMS\_SecurityAudit\_RemoveFilter (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \* client, [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \* filter )

**Description**

Deletes a filter of a notification event.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Notification event management client that has been created.

 |
| 

event

 | 

Event for which a filter is to be deleted.

 |
| 

filter

 | 

Notification event filter description.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned. If the event does not support the filter, **1012000005** is returned.

#### \[h2\]HMS\_SecurityAudit\_Subscribe()

int32\_t HMS\_SecurityAudit\_Subscribe (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \* client, const [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) \* events, uint64\_t count )

**Description**

Subscribes to notification events.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Client that subscribes to notification events.

 |
| 

events

 | 

Array of notification events to be subscribed to.

 |
| 

count

 | 

Number of notification events in the array.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_SubscribeAuthEvent()

int32\_t HMS\_SecurityAudit\_SubscribeAuthEvent (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \* client, const [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) \* events, uint64\_t count )

**Description**

Subscribes to authentication events.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Authentication event management client that has been created.

 |
| 

events

 | 

Array of authentication events to be subscribed to.

 |
| 

count

 | 

Number of authentication events in the array.

 |

**Required permission**:

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_Unsubscribe()

int32\_t HMS\_SecurityAudit\_Unsubscribe (const [SecurityAudit\_Client](#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \* client, const [SecurityAudit\_Notify\_Event](#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) \* events, uint64\_t count )

**Description**

Unsubscribes from notification events.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Client that unsubscribes from notification events.

 |
| 

events

 | 

Array of notification events to be unsubscribed from.

 |
| 

count

 | 

Number of notification events in the array.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_UnsubscribeAuthEvent()

int32\_t HMS\_SecurityAudit\_UnsubscribeAuthEvent (const [SecurityAudit\_AuthClient](#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \* client, const [SecurityAudit\_Auth\_Event](#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) \* events, uint64\_t count )

**Description**

Unsubscribes from authentication events.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

client

 | 

Authentication event management client that has been created.

 |
| 

events

 | 

Array of authentication events to be unsubscribed from.

 |
| 

count

 | 

Number of authentication events in the array.

 |

**Required permission**:

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_QueryAllProcesses()

int32\_t HMS\_SecurityAudit\_QueryAllProcesses(char\*\* result)

**Description**

Queries the information about all app processes.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

result

 | 

Obtained app processes information.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned.

#### \[h2\]HMS\_SecurityAudit\_QueryProcesses()

int32\_t HMS\_SecurityAudit\_QueryProcesses(uint64\_t\* pids, uint64\_t count, char\*\* result)

**Description**

Queries the information about app processes with the specified PIDs.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pids

 | 

Array of PIDs to be queried.

 |
| 

count

 | 

Number of PIDs in the array to be queried.

 |
| 

result

 | 

Obtained app processes information.

 |

**Required permission**:

ohos.permission.QUERY\_AUDIT\_EVENT

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs, **1012000001** is returned. If the number of PIDs in the array to be queried exceeds the upper limit, **1012000006** is returned.
