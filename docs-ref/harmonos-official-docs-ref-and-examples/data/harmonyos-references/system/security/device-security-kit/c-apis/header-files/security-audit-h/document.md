# security\_audit.h

#### Overview

This file defines the security audit functions.

**Library**: libsecurityaudit\_ndk.z.so

**System capability**: SystemCapability.Security.SecurityAudit

**Start version**: 6.0.0(20)

**Related module**: [SecurityAudit](../../modules/securityaudit/document.md)

#### Summary

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

typedef void(\* [SecurityAudit\_Handler](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370)) (const [SecurityAudit\_Event](../../structs/securityaudit-event/document.md) \*events, uint64\_t count)

 | 

Defines an event processing function.

 |
| 

typedef struct SecurityAudit\_AuthClient\_Impl [SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868)

 | 

Defines an authentication event management client.

 |
| 

typedef struct SecurityAudit\_Client\_Impl [SecurityAudit\_Client](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974)

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

[SecurityAudit\_Notify\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea){

SECURITY\_AUDIT\_NOTIFY\_EVENT\_PASTEBOARD = 0x27000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE = 0x1C000007, SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED = 0x1C001100, SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT = 0x10000100,

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

[SecurityAudit\_Auth\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f){

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE = 0x1C801100, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_OPEN = 0x1C801101, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_RENAME = 0x1C801102, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETE = 0x1C801103,

SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_SETEXTATTR = 0x1C801104, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETEEXTATTR = 0x1C801105

}

 | 

Defines the authentication event IDs.

 |
| 

[SecurityAudit\_FilterType](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) {

EVENT\_TYPE\_EQUAL = 0x00000100, EVENT\_SUBTYPE\_EQUAL = 0x00000200, FILE\_PATH\_EQUAL = 0x00010000, FILE\_PATH\_PREFIX = 0x00010001,

FILE\_PATH\_SUFFIX = 0x00010002, PROCESS\_UID\_EQUAL = 0x00020000, PROCESS\_PID\_EQUAL = 0x00020100, PROCESS\_NAME\_EQUAL = 0x00020200,

PROCESS\_NAME\_PREFIX = 0x00020201, PROCESS\_NAME\_SUFFIX = 0x00020202

}

 | 

Defines the filter types.

 |
| 

[SecurityAudit\_AuthResult](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) { SECURITY\_AUDIT\_AUTH\_RESULT\_ALLOW = 0, SECURITY\_AUDIT\_AUTH\_RESULT\_DENY = 1 }

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

int32\_t [HMS\_SecurityAudit\_NewClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga18d7c9fe5c578d6113c86dd0c09353b4) ([SecurityAudit\_Client](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*\*client, [SecurityAudit\_Handler](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

 | 

Creates a notification event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_DeleteClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga26838e6288eea1421f03e6130aafd837) ([SecurityAudit\_Client](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client)

 | 

Deletes a notification event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_Subscribe](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga3530687f761edfb0141f6c17ff3ba4cd) (const [SecurityAudit\_Client](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, const [SecurityAudit\_Notify\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) \*events, uint64\_t count)

 | 

Subscribes to notification events.

 |
| 

int32\_t [HMS\_SecurityAudit\_Unsubscribe](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga208aff2c03535311e85428fbd375d09f) (const [SecurityAudit\_Client](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, const [SecurityAudit\_Notify\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) \*events, uint64\_t count)

 | 

Unsubscribes from notification events.

 |
| 

int32\_t [HMS\_SecurityAudit\_AddFilter](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga292bdf10008513a439d6bb08450328b0) (const [SecurityAudit\_Client](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, [SecurityAudit\_Notify\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Adds a filter for a notification event.

 |
| 

int32\_t [HMS\_SecurityAudit\_RemoveFilter](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga3c7aa36f4cff9a0107bf144f7fbbdcd5) (const [SecurityAudit\_Client](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) \*client, [SecurityAudit\_Notify\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Deletes a filter of a notification event.

 |
| 

int32\_t [HMS\_SecurityAudit\_NewAuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gab59201b529a964c3cc7f9ed12ab0330e) ([SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*\*client, [SecurityAudit\_Handler](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

 | 

Creates an authentication event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_DeleteAuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga0a518a6380e80f47869a58f9cf14af87) ([SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client)

 | 

Deletes an authentication event management client.

 |
| 

int32\_t [HMS\_SecurityAudit\_SubscribeAuthEvent](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gab33847480e92d3107a91d76a10b8c82f) (const [SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, const [SecurityAudit\_Auth\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) \*events, uint64\_t count)

 | 

Subscribes to authentication events.

 |
| 

int32\_t [HMS\_SecurityAudit\_UnsubscribeAuthEvent](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaebf52f27e5409c29dc3ad0c3eba47783) (const [SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, const [SecurityAudit\_Auth\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) \*events, uint64\_t count)

 | 

Unsubscribes from authentication events.

 |
| 

int32\_t [HMS\_SecurityAudit\_AddAuthEventFilter](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga3d9df28411da9cc483c2e82d304cb38e) (const [SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, [SecurityAudit\_Auth\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Adds a filter for an authentication event.

 |
| 

int32\_t [HMS\_SecurityAudit\_RemoveAuthEventFilter](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaef069b340e428715c10531885326c079) (const [SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, [SecurityAudit\_Auth\_Event](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit\_Filter](../../structs/securityaudit-filter/document.md) \*filter)

 | 

Deletes a filter of an authentication event.

 |
| 

int32\_t [HMS\_SecurityAudit\_Auth](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gafbb9c2e5389b79d8def76c530e01e26c) (const [SecurityAudit\_AuthClient](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) \*client, const [SecurityAudit\_Event](../../structs/securityaudit-event/document.md) \*event, [SecurityAudit\_AuthResult](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) authResult)

 | 

Sets the authentication result for an audit event.

 |
| 

int32\_t [HMS\_SecurityAudit\_QueryAllProcesses](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_section0945443114617) (char\*\* result)

 | 

Obtains the information about all app processes.

 |
| 

int32\_t [HMS\_SecurityAudit\_QueryProcesses](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_section11373745488) (uint64\_t\* pids, uint64\_t count, char\*\* result)

 | 

Obtains the information about app processes with the specified PIDs.

 |
