# ServiceCollaboration

#### Overview

Provide NDK APIs for Device Interconnectivity of Service Collaboration Kit.

**System capability**: SystemCapability.Collaboration.Service

**Start version**: 5.0.0(12)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[service\_collaboration\_api.h](../../header-files-and-structs/header-files/service-collaboration-api-h/document.md)

 | 

Defines the Device Interconnectivity APIs and relevant types.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [ServiceCollaboration\_CollaborationDeviceInfo](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfo/document.md)

 | 

Device information object obtained by Device Interconnectivity, including basic device information and capability types.

 |
| 

struct [ServiceCollaboration\_CollaborationDeviceInfoSets](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfosets/document.md)

 | 

Remote device information object set obtained through [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](#gaeffea1546cbe64aeba533e5b72bca7ba).

 |
| 

struct [ServiceCollaboration\_SelectInfo](../../header-files-and-structs/structs/servicecollaboration-selectinfo/document.md)

 | 

Information about the selected device when [HMS\_ServiceCollaboration\_StartCollaboration](#section4531193410296) is used to trigger Device Interconnectivity.

 |
| 

struct [ServiceCollaborationCallback](../../header-files-and-structs/structs/servicecollaborationcallback/document.md)

 | 

Callback passed to [HMS\_ServiceCollaboration\_StartCollaboration](#section4531193410296).

 |

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](#ga22d10f5d68c518533857b4a3e5947647) 65

 | 

Maximum length of a device network ID.

 |
| 

[COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](#section115253318501) 128

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

typedef enum [ServiceCollaborationFilterType](#section16675437105618) [ServiceCollaborationFilterType](#ga1d033f8a2e87fab0e1e01cb1e9859243)

 | 

Device Interconnectivity capability types.

 |
| 

typedef enum [ServiceCollaborationDataType](#section1467523718564) [ServiceCollaborationDataType](#ga3547eca8cf19ab049ffc992e5b712142)

 | 

Types of the data returned.

 |
| 

typedef enum [ServiceCollaborationEventCode](#section967514377563) [ServiceCollaborationEventCode](#ga7ff0af9a33e5e5a3acfada94d422a60b)

 | 

Result codes.

 |
| 

typedef struct [ServiceCollaboration\_CollaborationDeviceInfo](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfo/document.md) [ServiceCollaboration\_CollaborationDeviceInfo](#ga36cefd0afb1105cdbc28b9460d5f336f)

 | 

Device information object.

 |
| 

typedef struct [ServiceCollaboration\_CollaborationDeviceInfoSets](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfosets/document.md) [ServiceCollaboration\_CollaborationDeviceInfoSets](#section121718545319)

 | 

Set of device information objects.

 |
| 

typedef struct [ServiceCollaboration\_SelectInfo](../../header-files-and-structs/structs/servicecollaboration-selectinfo/document.md) [ServiceCollaboration\_SelectInfo](#section1871418518535)

 | 

Information about the selected device.

 |
| 

typedef struct [ServiceCollaborationCallback](../../header-files-and-structs/structs/servicecollaborationcallback/document.md) [ServiceCollaborationCallback](#section1958717716536)

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

[ServiceCollaborationFilterType](#section16675437105618) {

TAKE\_PHOTO = 1,

SCAN\_DOCUMENT = 2,

IMAGE\_PICKER = 3

}

 | 

Device Interconnectivity capability types.

 |
| 

[ServiceCollaborationDataType](#section1467523718564){

IMAGE = 1

}

 | 

Types of the data returned.

 |
| 

[ServiceCollaborationEventCode](#section967514377563){

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

[ServiceCollaboration\_CollaborationDeviceInfoSets](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfosets/document.md)\* [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](#gaeffea1546cbe64aeba533e5b72bca7ba)(

uint32\_t fileterNum, [ServiceCollaborationFilterType](#section16675437105618) serviceFileterTypes\[\])

 | 

Obtains the list of devices that support related capabilities.

 |
| 

uint32\_t [HMS\_ServiceCollaboration\_StartCollaboration](#section4531193410296)(

const [ServiceCollaboration\_SelectInfo](../../header-files-and-structs/structs/servicecollaboration-selectinfo/document.md)\* selectService, [ServiceCollaborationCallback](../../header-files-and-structs/structs/servicecollaborationcallback/document.md)\* callback)

 | 

Starts the Device Interconnectivity capability.

 |
| 

int32\_t [HMS\_ServiceCollaboration\_StopCollaboration](#section67211235132913)(uint32\_t collaborationId)

 | 

Stops the Device Interconnectivity capability.

 |

#### Macro Description

#### \[h2\]COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH

#define COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH   65

**Description**

Maximum length of a device network ID.

**Start version**: 5.0.0(12)

#### \[h2\]COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH

#define COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH   128

**Description**

Maximum length of a device name.

**Start version**: 5.0.0(12)

#### Type Description

#### \[h2\]ServiceCollaboration\_CollaborationDeviceInfo

typedef struct [ServiceCollaboration\_CollaborationDeviceInfo](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfo/document.md) [ServiceCollaboration\_CollaborationDeviceInfo](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfo/document.md)

**Description**

Device information object.

**Start version**: 5.0.0(12)

#### \[h2\]ServiceCollaboration\_CollaborationDeviceInfoSets

typedef struct [ServiceCollaboration\_CollaborationDeviceInfoSets](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfosets/document.md) [ServiceCollaboration\_CollaborationDeviceInfoSets](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfosets/document.md)

**Description**

Set of device information objects.

**Start version**: 5.0.0(12)

#### \[h2\]ServiceCollaboration\_SelectInfo

typedef struct [ServiceCollaboration\_SelectInfo](../../header-files-and-structs/structs/servicecollaboration-selectinfo/document.md) [ServiceCollaboration\_SelectInfo](../../header-files-and-structs/structs/servicecollaboration-selectinfo/document.md)

**Description**

Information about the selected device.

**Start version**: 5.0.0(12)

#### \[h2\]ServiceCollaborationCallback

typedef struct [ServiceCollaborationCallback](../../header-files-and-structs/structs/servicecollaborationcallback/document.md) [ServiceCollaborationCallback](../../header-files-and-structs/structs/servicecollaborationcallback/document.md)

**Description**

Callback that returns Device Interconnectivity service status information.

**Start version**: 5.0.0(12)

#### \[h2\]ServiceCollaborationFilterType

typedef enum [ServiceCollaborationFilterType](#section16675437105618) [ServiceCollaborationFilterType](#section16675437105618)

**Description**

Device Interconnectivity capability types.

**Start version**: 5.0.0(12)

#### \[h2\]ServiceCollaborationDataType

typedef enum [ServiceCollaborationDataType](#section1467523718564) [ServiceCollaborationDataType](#section1467523718564)

**Description**

Types of the data returned.

**Start version**: 5.0.0(12)

#### \[h2\]ServiceCollaborationEventCode

typedef enum [ServiceCollaborationEventCode](#section967514377563) [ServiceCollaborationEventCode](#section967514377563)

**Description**

Result codes.

**Start version**: 5.0.0(12)

#### Enumeration Description

#### \[h2\]ServiceCollaborationFilterType

enum [ServiceCollaborationFilterType](#section16675437105618)

**Description**

Device Interconnectivity capability types.

**Start version**: 5.0.0(12)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

TAKE\_PHOTO = 1

 | 

Photographing.

 |
| 

SCAN\_DOCUMENT = 2

 | 

Scanning.

 |
| 

IMAGE\_PICKER = 3

 | 

Image selection from the gallery.

 |

#### \[h2\]ServiceCollaborationDataType

enum [ServiceCollaborationDataType](#section1467523718564)

**Description**

Types of the data returned.

**Start version**: 5.0.0(12)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

IMAGE = 1

 | 

Image.

 |

#### \[h2\]ServiceCollaborationEventCode

enum [ServiceCollaborationEventCode](#section967514377563)

**Description**

Result codes.

**Start version**: 5.0.0(12)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

LAST\_DATA\_BACK = 1001202000

 | 

Last data package received.

 |
| 

PEER\_CANCEL = 1001202001

 | 

Canceled on the remote device.

 |
| 

NETWORK\_ERROR = 1001202002

 | 

Network error.

 |
| 

PEER\_WIFI\_NOT\_OPEN = 1001202004

 | 

Wi-Fi not enabled on the remote device.

 |
| 

LOCAL\_WIFI\_NOT\_OPEN = 1001202005

 | 

Wi-Fi not enabled on the local device.

 |
| 

DATA\_BACK\_START = 1001202006

 | 

Data returning started.

 |
| 

MIDDLE\_DATA\_BACK = 1001202007

 | 

Intermediate data received.

 |
| 

TIMEOUT\_AUTO\_CANCEL = 1001202008

 | 

Data receiving canceled due to timeout.

 |
| 

DATA\_READ\_FAILED = 1001202009

 | 

Failed to read data.

 |
| 

LINK\_SHUTDOWN = 1001202011

 | 

Link disconnected.

 |
| 

REMOTE\_HOTSPOT\_CONFLICT = 1001202013

 | 

A link conflict occurred because the hotspot is enabled on the remote device.

**Start version**: 5.1.0(18)

 |
| 

REMOTE\_DISTRIBUTED\_SERVICES\_CONFLICT = 1001202014

 | 

A link conflict occurred because the remote device was interconnecting with another device.

**Start version**: 5.1.0(18)

 |

#### Function Description

#### \[h2\]HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos

[ServiceCollaboration\_CollaborationDeviceInfoSets](../../header-files-and-structs/structs/servicecollaboration-collaborationdeviceinfosets/document.md)\* HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos(
    uint32\_t fileterNum, [ServiceCollaborationFilterType](#section16675437105618) serviceFileterTypes\[\]);

**Description**

Obtains the list of devices that support related capabilities.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

uint32\_t fileterNum

 | 

Total number of service capability types.

 |
| 

[ServiceCollaborationFilterType](#section16675437105618) serviceFileterTypes\[\]

 | 

Array of required service capability types.

 |

**Returns**:

[ServiceCollaboration\_CollaborationDeviceInfoSets](#section121718545319), which is a set of device information objects.

#### \[h2\]HMS\_ServiceCollaboration\_StartCollaboration

uint32\_t HMS\_ServiceCollaboration\_StartCollaboration(
    const [ServiceCollaboration\_SelectInfo](../../header-files-and-structs/structs/servicecollaboration-selectinfo/document.md)\* selectService, [ServiceCollaborationCallback](../../header-files-and-structs/structs/servicecollaborationcallback/document.md)\* callback);

**Description**

Starts the Device Interconnectivity capability.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

const [ServiceCollaboration\_SelectInfo](#section1871418518535)\* selectService

 | 

Type of the service capability to be started.

 |
| 

[ServiceCollaborationCallback](#section1958717716536)\* callback

 | 

Callback.

 |

**Returns**:

**collaborationId** of the **uint32\_t** type, which is the unique ID of a Device Interconnectivity session.

#### \[h2\]HMS\_ServiceCollaboration\_StopCollaboration

int32\_t HMS\_ServiceCollaboration\_StopCollaboration(uint32\_t collaborationId);

**Description**

Stops the Device Interconnectivity capability.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

uint32\_t collaborationId

 | 

Unique ID of a Device Interconnectivity session.

 |

**Returns**:

The service termination result is returned. **0** indicates successful termination.
