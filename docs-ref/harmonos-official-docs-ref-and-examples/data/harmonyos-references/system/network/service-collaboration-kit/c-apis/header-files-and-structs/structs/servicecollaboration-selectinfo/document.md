# ServiceCollaboration\_SelectInfo

#### Overview

Information about the selected device when [HMS\_ServiceCollaboration\_StartCollaboration](../../../modules/servicecollaboration/document.md#section4531193410296) is used to trigger Device Interconnectivity.

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

[ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#section16675437105618) [serviceFilterType](#a9154e00b7840c2e739599ebfce7c5deb)

 | 

Expected device capability types.

 |
| 

char [deviceNetworkId](#a8829d22e5d51fc0814cc3e1f5d814679) \[[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](../../../modules/servicecollaboration/document.md#ga22d10f5d68c518533857b4a3e5947647)\]

 | 

Network ID of the selected device.

 |
| 

uint32\_t [maxSize](#a8aa0e58e2736c50b8c9957c7b14c7cd3)

 | 

Maximum number of images that can be selected.

 |

#### Member Variable Description

#### \[h2\]deviceNetworkId

char ServiceCollaboration\_SelectInfo::deviceNetworkId\[[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](../../../modules/servicecollaboration/document.md#ga22d10f5d68c518533857b4a3e5947647)\]

**Description**

Network ID of the selected device.

#### \[h2\]maxSize

uint32\_t ServiceCollaboration\_SelectInfo::maxSize

**Description**

Maximum number of images that can be selected.

#### \[h2\]serviceFilterType

[ServiceCollaborationFilterType](../../../modules/servicecollaboration/document.md#section16675437105618) ServiceCollaboration\_SelectInfo::serviceFilterType

**Description**

Expected device capability types.
