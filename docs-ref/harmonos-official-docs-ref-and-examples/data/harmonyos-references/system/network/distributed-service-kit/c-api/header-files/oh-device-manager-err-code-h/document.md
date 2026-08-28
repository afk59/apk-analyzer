# oh\_device\_manager\_err\_code.h

#### Overview

Declares the error codes of the distributed device management module.

**File to include**: <distributedhardware/device\_manager/oh\_device\_manager\_err\_code.h>

**Library**: libdevicemanager\_ndk.so

**System capability**: SystemCapability.DistributedHardware.DeviceManager

**Since**: 20

**Related module**: [DeviceManager](../../modules/devicemanager/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DeviceManager\_ErrorCode](#devicemanager_errorcode) | DeviceManager\_ErrorCode | Error code information of distributed device management module. |

#### Enum Description

#### \[h2\]DeviceManager\_ErrorCode

enum DeviceManager\_ErrorCode

**Description**

Error codes of the distributed device management module.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| ERR\_OK = 0 | Operation success. |
| ERR\_PERMISSION\_ERROR = 201 | Permission verification failed. |
| ERR\_INVALID\_PARAMETER = 401 | Invalid parameter. |
| DM\_ERR\_FAILED = 11600101 | Function execution failed. |
| DM\_ERR\_OBTAIN\_SERVICE = 11600102 | Failed to obtain the device management service. |
| DM\_ERR\_OBTAIN\_BUNDLE\_NAME = 11600109 | Failed to obtain the bundle name. |
