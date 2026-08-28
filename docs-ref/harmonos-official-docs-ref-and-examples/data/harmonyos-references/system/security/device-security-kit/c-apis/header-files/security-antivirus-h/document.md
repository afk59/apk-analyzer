# security\_antivirus.h

#### Overview

This file defines functions related to the VirusProtectionServiceManager.

**Library**: libsecurityantivirus\_ndk.z.so

**System capability**: SystemCapability.Security.SecurityAntivirus

**Start version**: 6.0.0(20)

**Related module**: [SecurityAntivirus](../../modules/securityantivirus/document.md)

#### Summary

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

[SecurityAntivirus\_ErrCode](../../modules/securityantivirus/document.md#section7961454596){

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

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_RegisterAntivirus](../../modules/securityantivirus/document.md#section556519812196)(const char\* bundleName)

 | 

Called by a third-party EDR app to register with the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_UnregisterAntivirus](../../modules/securityantivirus/document.md#section3962618203519)(const char\* bundleName)

 | 

Called by a third-party EDR app to unregister from the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_UpdateAntivirus](../../modules/securityantivirus/document.md#section5548172953619)(const [SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\* antivirus)

 | 

Called by a third-party EDR app to update its information, including the package name, current version number, last update time, antivirus switch status, and user ID, to the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_QueryAntivirus](../../modules/securityantivirus/document.md#section499213812378)([SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\*\* list, uint32\_t\* length)

 | 

Called by a zero trust app to query the HarmonyOS VirusProtectionService for the registration information of all third-party EDR apps.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus](../../modules/securityantivirus/document.md#section109159243919)([SecurityAntivirus\_Antivirus](../../structs/securityantivirus-antivirus/document.md)\*\* list, uint32\_t\* length)

 | 

Called by an MDM app to query the HarmonyOS VirusProtectionService for the antivirus function status of all users.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus](../../modules/securityantivirus/document.md#section284719393418)(void)

 | 

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for all users.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus](../../modules/securityantivirus/document.md#section16629747456)(void)

 | 

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for all users.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount](../../modules/securityantivirus/document.md#section1272125114210)(int32\_t accountId)

 | 

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

 |
| 

SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount](../../modules/securityantivirus/document.md#section373142512429)(int32\_t accountId)

 | 

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

 |
