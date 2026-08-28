# SecurityAntivirus

#### Overview

The SecurityAntivirus module manages third-party antivirus apps.

**System capability**: SystemCapability.Security.SecurityAntivirus

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

[security\_antivirus.h](../../header-files/security-antivirus-h/document.md)

 | 

Defines the APIs called by antivirus apps.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)

 | 

Defines the antivirus app information, including the package name, current version number, last update time, antivirus switch status, and user ID.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[SecurityAntivirus\_ErrCode](#section7961454596){

SECURITY\_ANTIVIRUS\_SUCCESS = 0,

SECURITY\_ANTIVIRUS\_PERMISSION\_NOT\_GRANTED = 201,

SECURITY\_ANTIVIRUS\_PARAM\_INVALID = 1019900001,

SECURITY\_ANTIVIRUS\_NO\_REGISTER = 1019900002,

SECURITY\_ANTIVIRUS\_INNER\_ERROR = 1019900003

}

 | 

Defines the VirusProtectionServiceManager result codes.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_RegisterAntivirus](#section556519812196)(const char\* bundleName)

 | 

Called by a third-party Endpoint Detection and Response (EDR) app to register with the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_UnregisterAntivirus](#section3962618203519)(const char\* bundleName)

 | 

Called by a third-party EDR app to unregister from the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_UpdateAntivirus](#section5548172953619)(const [SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\* antivirus)

 | 

Called by a third-party EDR app to update its information, including the package name, current version number, last update time, antivirus switch status, and user ID, to the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_QueryAntivirus](#section499213812378)([SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\*\* list, uint32\_t\* length)

 | 

Called by a zero trust app to query the HarmonyOS VirusProtectionService for the registration information of all third-party EDR apps.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus](#section109159243919)([SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\*\* list, uint32\_t\* length)

 | 

Called by a Mobile Device Management (MDM) app to query the HarmonyOS VirusProtectionService for the antivirus function status of all users.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus](#section284719393418)(void)

 | 

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for all users.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus](#section16629747456)(void)

 | 

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for all users.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount](#section1272125114210)(int32\_t accountId)

 | 

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount](#section373142512429)(int32\_t accountId)

 | 

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

 |

#### Enumeration Description

#### \[h2\]SecurityAntivirus\_ErrCode

enum [SecurityAntivirus\_ErrCode](#section7961454596)

**Description**

Defines the VirusProtectionServiceManager result codes.

**System capability**: SystemCapability.Security.SecurityAntivirus

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

SECURITY\_ANTIVIRUS\_SUCCESS

 | 

The API is called successfully.

 |
| 

SECURITY\_ANTIVIRUS\_PERMISSION\_NOT\_GRANTED

 | 

API call permission verification fails.

 |
| 

SECURITY\_ANTIVIRUS\_PARAM\_INVALID

 | 

Input parameter verification fails.

 |
| 

SECURITY\_ANTIVIRUS\_NO\_REGISTER

 | 

The antivirus app is not registered.

 |
| 

SECURITY\_ANTIVIRUS\_INNER\_ERROR

 | 

An internal error occurs in the HarmonyOS VirusProtectionService.

 |

#### Function Description

#### \[h2\]HMS\_SecurityAntivirus\_RegisterAntivirus()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_RegisterAntivirus(const char\* bundleName)

**Description**

Called by a third-party EDR app to register with the HarmonyOS VirusProtectionService.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

bundleName

 | 

Third-party EDR package name.

 |

**Required permission**:

ohos.permission.REGISTER\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If the input parameters do not comply with the specifications, **1019900001** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_UnregisterAntivirus()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_UnregisterAntivirus(const char\* bundleName)

**Description**

Called by a third-party EDR app to unregister from the HarmonyOS VirusProtectionService.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

bundleName

 | 

Third-party EDR package name.

 |

**Required permission**:

ohos.permission.REGISTER\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If the input parameters do not comply with the specifications, **1019900001** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_UpdateAntivirus()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_UpdateAntivirus(const [SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\* antivirus)

**Description**

Called by a third-party EDR app to update its information, including the package name, current version number, last update time, antivirus switch status, and user ID, to the HarmonyOS VirusProtectionService.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

antivirus

 | 

Updated information about a third-party EDR app, including the package name, current version number, last update time, antivirus switch status, and user ID.

 |

**Required permission**:

ohos.permission.REGISTER\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If the input parameters do not comply with the specifications, **1019900001** is returned. If the current app is not registered with the antivirus system, **1019900002** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_QueryAntivirus()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_QueryAntivirus([SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\*\* list, uint32\_t\* length)

**Description**

Called by a zero trust app to query the HarmonyOS VirusProtectionService for the registration information of all third-party EDR apps.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

list

 | 

Registration information list of third-party EDR apps.

 |
| 

length

 | 

Number of registered third-party EDR apps.

 |

**Required permission**:

ohos.permission.MANAGE\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If the input parameters do not comply with the specifications, **1019900001** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus([SecurityAntivirus\_Antivirus](#)\*\* list, uint32\_t\* length)

**Description**

Called by an MDM app to query the HarmonyOS VirusProtectionService for the antivirus function status of all users.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

list

 | 

Antivirus function status information list of all users of the HarmonyOS VirusProtectionService.

 |
| 

length

 | 

Number of antivirus function status records of all users of the HarmonyOS VirusProtectionService.

 |

**Required permission**:

ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If the input parameters do not comply with the specifications, **1019900001** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus(void)

**Description**

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for all users.

**Start version**: 6.0.0(20)

**Required permission**:

ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus(void)

**Description**

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for all users.

**Start version**: 6.0.0(20)

**Required permission**:

ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount(int32\_t accountId)

**Description**

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

accountId

 | 

User ID.

 |

**Required permission**:

ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If the input parameters do not comply with the specifications, **1019900001** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.

#### \[h2\]HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount()

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount(int32\_t accountId)

**Description**

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

accountId

 | 

User ID.

 |

**Required permission**:

ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS

**Returns**:

Execution result of the function. If the operations are successful, **0** is returned. If the permission verification fails, **201** is returned. If the input parameters do not comply with the specifications, **1019900001** is returned. If an internal error occurs in the HarmonyOS VirusProtectionService, **1019900003** is returned.
