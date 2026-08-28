# service\_collaboration\_api.h

#### Overview

APIs defined by the **export** function.

**Library**: libservice\_collaboration\_ndk.z.so

**System capability**: SystemCapability.Collaboration.Service

**Start version**: 5.0.0(12)

**Related module**: [ServiceCollaboration](../../../modules/servicecollaboration/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [ServiceCollaboration\_CollaborationDeviceInfo](../../structs/servicecollaboration-collaborationdeviceinfo/document.md)

 | 

Device information object obtained by Device Interconnectivity, including basic device information and capability types.

 |
| 

struct [ServiceCollaboration\_CollaborationDeviceInfoSets](../../structs/servicecollaboration-collaborationdeviceinfosets/document.md)

 | 

Remote device information object set obtained through [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../../../modules/servicecollaboration/document.md#gaeffea1546cbe64aeba533e5b72bca7ba).

 |
| 

struct [ServiceCollaboration\_SelectInfo](../../structs/servicecollaboration-selectinfo/document.md)

 | 

Information about the selected device when [HMS\_ServiceCollaboration\_StartCollaboration](../../../modules/servicecollaboration/document.md#section4531193410296) is used to trigger Device Interconnectivity.

 |
| 

struct [ServiceCollaborationCallback](../../structs/servicecollaborationcallback/document.md)

 | 

Callback passed to [HMS\_ServiceCollaboration\_StartCollaboration](../../../modules/servicecollaboration/document.md#section4531193410296).

 |

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](../../../modules/servicecollaboration/document.md#ga22d10f5d68c518533857b4a3e5947647) 65

 | 

Maximum length of a device network ID.

 |
| 

[COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](../../../modules/servicecollaboration/document.md#section115253318501) 128

 | 

Maximum length of a device name.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#section16675437105618) [ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#ga1d033f8a2e87fab0e1e01cb1e9859243)

 | 

Device Interconnectivity capability types.

 |
| 

typedef enum [ServiceCollaborationDataType](../../../modules/servicecollaboration/document.md#section1467523718564) [ServiceCollaborationDataType](../../../modules/servicecollaboration/document.md#ga3547eca8cf19ab049ffc992e5b712142)

 | 

Types of the data returned.

 |
| 

typedef enum [ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563) [ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#ga7ff0af9a33e5e5a3acfada94d422a60b)

 | 

Result codes.

 |
| 

typedef struct [ServiceCollaboration\_CollaborationDeviceInfo](../../structs/servicecollaboration-collaborationdeviceinfo/document.md) [ServiceCollaboration\_CollaborationDeviceInfo](../../../modules/servicecollaboration/document.md#ga36cefd0afb1105cdbc28b9460d5f336f)

 | 

Device information object.

 |
| 

typedef struct [ServiceCollaboration\_CollaborationDeviceInfoSets](../../structs/servicecollaboration-collaborationdeviceinfosets/document.md) [ServiceCollaboration\_CollaborationDeviceInfoSets](../../../modules/servicecollaboration/document.md#section121718545319)

 | 

Set of device information objects.

 |
| 

typedef struct [ServiceCollaboration\_SelectInfo](../../structs/servicecollaboration-selectinfo/document.md) [ServiceCollaboration\_SelectInfo](../../../modules/servicecollaboration/document.md#section1871418518535)

 | 

Information about the selected device.

 |
| 

typedef struct [ServiceCollaborationCallback](../../structs/servicecollaborationcallback/document.md) [ServiceCollaborationCallback](../../../modules/servicecollaboration/document.md#section1958717716536)

 | 

Callback that returns Device Interconnectivity service status information.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#section16675437105618) {

TAKE\_PHOTO = 1,

SCAN\_DOCUMENT = 2,

IMAGE\_PICKER = 3

}

 | 

Device Interconnectivity capability types.

 |
| 

[ServiceCollaborationDataType](../../../modules/servicecollaboration/document.md#section1467523718564){

IMAGE = 1

}

 | 

Types of the data returned.

 |
| 

[ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563){

LAST\_DATA\_BACK = 1001202000,

PEER\_CANCEL = 1001202001,

NETWORK\_ERROR = 1001202002,

PEER\_WIFI\_NOT\_OPEN = 1001202004,

LOCAL\_WIFI\_NOT\_OPEN = 1001202005,

DATA\_BACK\_START = 1001202006,

MIDDLE\_DATA\_BACK = 1001202007,

TIMEOUT\_AUTO\_CANCEL = 1001202008,

DATA\_READ\_FAILED = 1001202009,

LINK\_SHUTDOWN = 1001202011,

REMOTE\_HOTSPOT\_CONFLICT = 1001202013,

REMOTE\_DISTRIBUTED\_SERVICES\_CONFLICT = 1001202014

}

 | 

Result codes.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ServiceCollaboration\_CollaborationDeviceInfoSets](../../structs/servicecollaboration-collaborationdeviceinfosets/document.md)\* [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../../../modules/servicecollaboration/document.md#gaeffea1546cbe64aeba533e5b72bca7ba)(

uint32\_t fileterNum, [ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#section16675437105618) serviceFileterTypes\[\]);

 | 

Obtains the list of devices that support related capabilities.

 |
| 

uint32\_t [HMS\_ServiceCollaboration\_StartCollaboration](../../../modules/servicecollaboration/document.md#section4531193410296)(

const [ServiceCollaboration\_SelectInfo](../../structs/servicecollaboration-selectinfo/document.md)\* selectService, [ServiceCollaborationCallback](../../structs/servicecollaborationcallback/document.md)\* callback)

 | 

Starts the Device Interconnectivity capability.

 |
| 

int32\_t [HMS\_ServiceCollaboration\_StopCollaboration](../../../modules/servicecollaboration/document.md#section67211235132913)(uint32\_t collaborationId);

 | 

Stops the Device Interconnectivity capability.

 |
