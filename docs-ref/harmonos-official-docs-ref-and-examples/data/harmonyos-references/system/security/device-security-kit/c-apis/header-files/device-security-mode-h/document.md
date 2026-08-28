# device\_security\_mode.h

#### Overview

The file defines the function related to the device security mode.

**Library**: libdevice\_security\_mode.z.so

**System capability**: SystemCapability.Security.SafetyDetect

**Start version**: 5.0.1(13)

**Related module**: [DeviceSecurityMode](../../modules/devicesecuritymode/document.md)

#### Summary

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [DSM\_DeviceSecurityMode](../../modules/devicesecuritymode/document.md#section1753134381213) [DSM\_DeviceSecurityMode](../../modules/devicesecuritymode/document.md#section17561511173514)

 | 

Device security mode enumeration type definition.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[DSM\_DeviceSecurityMode](../../modules/devicesecuritymode/document.md#section1753134381213) {

DSM\_NORMAL\_MODE = 0,

DSM\_SECURE\_SHIELD\_MODE = 1

}

 | 

Enumerated values of the device security mode.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[DSM\_DeviceSecurityMode](../../modules/devicesecuritymode/document.md#section1753134381213) [HMS\_DSM\_GetDeviceSecurityMode()](../../modules/devicesecuritymode/document.md#section556519812196)

 | 

Queries the security mode of the current device.

 |
