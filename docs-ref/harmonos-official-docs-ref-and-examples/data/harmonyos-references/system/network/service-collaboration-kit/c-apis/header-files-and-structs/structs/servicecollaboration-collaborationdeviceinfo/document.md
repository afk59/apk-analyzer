# ServiceCollaboration\_CollaborationDeviceInfo

#### Overview

Device information object obtained by Device Interconnectivity, including basic device information and capability types.

**Start version**: 5.0.0(12)

**Related module**: [ServiceCollaboration](../../../modules/servicecollaboration/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

uint32\_t [deviceType](#a17cfb1e778b48e1ab1086c3db5730247)

 | 

Type of the remote device. The value can only be **0x14** (phone) or **0x17** (tablet).

 |
| 

char [deviceNetworkId](#ac029c525120d06c49e2870b2558a4713) \[[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](../../../modules/servicecollaboration/document.md#ga22d10f5d68c518533857b4a3e5947647)\]

 | 

Network ID of the remote device.

 |
| 

char [deviceName](#a0e045f8cff3ce1255996f3fce3e39809) \[[COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](../../../modules/servicecollaboration/document.md#section115253318501)\]

 | 

Name of the remote device.

 |
| 

uint32\_t [filterNum](#a52bb822ea7f7a30c9396b0db636ed182)

 | 

Size of the list of capabilities supported by the remote device.

 |
| 

[ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#section16675437105618) \* [serviceFilterTypes](#a02e04d9d0416ecd2c34fde480f4b5a69)

 | 

List of capabilities supported by the remote device.

 |

#### Member Variable Description

#### \[h2\]deviceName

char ServiceCollaboration\_CollaborationDeviceInfo::deviceName\[[COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](../../../modules/servicecollaboration/document.md#section115253318501)\]

**Description**

Name of the remote device.

#### \[h2\]deviceNetworkId

char ServiceCollaboration\_CollaborationDeviceInfo::deviceNetworkId\[[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](../../../modules/servicecollaboration/document.md#ga22d10f5d68c518533857b4a3e5947647)\]

**Description**

Network ID of the remote device.

#### \[h2\]deviceType

uint32\_t ServiceCollaboration\_CollaborationDeviceInfo::deviceType

**Description**

Type of the remote device. The value can only be **0x14** (phone) or **0x17** (tablet).

#### \[h2\]filterNum

uint32\_t ServiceCollaboration\_CollaborationDeviceInfo::filterNum

**Description**

Size of the list of capabilities supported by the remote device.

#### \[h2\]serviceFilterTypes

[ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#section16675437105618)\* ServiceCollaboration\_CollaborationDeviceInfo::serviceFilterTypes

**Description**

List of capabilities supported by the remote device.
