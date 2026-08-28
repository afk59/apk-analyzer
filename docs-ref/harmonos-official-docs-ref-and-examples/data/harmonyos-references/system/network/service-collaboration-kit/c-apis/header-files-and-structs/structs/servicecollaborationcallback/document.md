# ServiceCollaborationCallback

#### Overview

Callback passed to [HMS\_ServiceCollaboration\_StartCollaboration](../../../modules/servicecollaboration/document.md#section4531193410296).

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

int32\_t(\* [OnEvent](#aafe5f2728b365097fc4b13a249581b6c) )([ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563) code, uint32\_t extraCode)

 | 

Function pointer to a callback triggered when the Device Interconnectivity service status changes.

 |
| 

int32\_t(\* [OnDataCallback](#aee0a1469ca582efe5b81d1cc198f308d) )([ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563) code, [ServiceCollaborationDataType](../../../modules/servicecollaboration/document.md#section1467523718564) dataType, uint32\_t dataSize, char \*data)

 | 

Function pointer to a callback triggered when data is returned through the Device Interconnectivity service.

 |

#### Member Variable Description

#### \[h2\]OnDataCallback

int32\_t(\* ServiceCollaborationCallback::OnDataCallback) ([ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563) code, [ServiceCollaborationDataType](../../../modules/servicecollaboration/document.md#section1467523718564) dataType, uint32\_t dataSize, char \*data)

**Description**

Function pointer to a callback triggered when data is returned through the Device Interconnectivity service.

**Parameters**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563) code

 | 

Result code.

 |
| 

[ServiceCollaborationDataType](../../../modules/servicecollaboration/document.md#section1467523718564) dataType

 | 

Type of the data returned.

 |
| 

uint32\_t dataSize

 | 

Data size, in bytes.

 |
| 

char \*data

 | 

Data.

 |

#### \[h2\]OnEvent

int32\_t(\* ServiceCollaborationCallback::OnEvent) ([ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563) code, uint32\_t extraCode)

**Description**

Function pointer to a callback triggered when the Device Interconnectivity service status changes.

**Parameters**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ServiceCollaborationEventCode](../../../modules/servicecollaboration/document.md#section967514377563) code

 | 

Result code.

 |
| 

uint32\_t extraCode

 | 

Extended result code that conveys additional information beyond standard result codes.

 |
