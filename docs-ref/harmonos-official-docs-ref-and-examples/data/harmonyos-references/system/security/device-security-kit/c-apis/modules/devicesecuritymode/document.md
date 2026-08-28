# DeviceSecurityMode

#### Overview

The DeviceSecurityMode module is used to manage the device security mode.

**System capability**: SystemCapability.Security.SafetyDetect

**Start version**: 5.0.1(13)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[device\_security\_mode.h](../../header-files/device-security-mode-h/document.md)

 | 

Defines the function related to the device security mode.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [DSM\_DeviceSecurityMode](#section1753134381213) [DSM\_DeviceSecurityMode](#section17561511173514)

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

[DSM\_DeviceSecurityMode](#section1753134381213) {

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

[DSM\_DeviceSecurityMode](#section1753134381213) [HMS\_DSM\_GetDeviceSecurityMode()](#section556519812196)

 | 

Queries the security mode of the current device.

 |

#### Type Definition Description

#### \[h2\]DSM\_DeviceSecurityMode

typedef enum DSM\_DeviceSecurityMode DSM\_DeviceSecurityMode

**Description**

Device security mode enumeration type definition.

**Start version**: 5.0.1(13)

#### Enumeration Description

#### \[h2\]DSM\_DeviceSecurityMode

enum DSM\_DeviceSecurityMode

**Description**

Enumerated values of the device security mode.

**Start version**: 5.0.1(13)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

DSM\_NORMAL\_MODE

 | 

Common mode, which is the default device security mode.

 |
| 

DSM\_SECURE\_SHIELD\_MODE

 | 

Secure Shield mode, which is used to protect devices from sophisticated cyberattacks. Certain web browsing features are restricted in this mode.

 |

#### Function Description

#### \[h2\]HMS\_DSM\_GetDeviceSecurityMode()

DSM\_DeviceSecurityMode HMS\_DSM\_GetDeviceSecurityMode(void)

**Description**

Queries the security mode of the current device.

**Start version**: 5.0.1(13)

**Returns**:

For details, please refer to [DSM\_DeviceSecurityMode](#section1753134381213).
