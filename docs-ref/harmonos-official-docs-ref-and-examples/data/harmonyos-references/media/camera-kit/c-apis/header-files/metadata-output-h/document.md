# metadata\_output.h

#### Overview

The file declares the metadata output concepts.

**File to include**: <ohcamera/metadata\_output.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [MetadataOutput\_Callbacks](../../structs/metadataoutput-callbacks/document.md) | MetadataOutput\_Callbacks | Describes the callbacks related to metadata output. |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md) | Camera\_MetadataOutput | 
Describes the metadata output object.

You can use [OH\_CameraManager\_CreateMetadataOutput](../camera-manager-h/document.md#oh_cameramanager_createmetadataoutput) to create such an object.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_MetadataOutput\_OnMetadataObjectAvailable)(Camera\_MetadataOutput\* metadataOutput,Camera\_MetadataObject\* metadataObject, uint32\_t size)](#oh_metadataoutput_onmetadataobjectavailable) | OH\_MetadataOutput\_OnMetadataObjectAvailable | Defines the callback defined in the [MetadataOutput\_Callbacks](../../structs/metadataoutput-callbacks/document.md) struct and used to report metadata output data. |
| [typedef void (\*OH\_MetadataOutput\_OnError)(Camera\_MetadataOutput\* metadataOutput, Camera\_ErrorCode errorCode)](#oh_metadataoutput_onerror) | OH\_MetadataOutput\_OnError | Defines the callback defined in the [MetadataOutput\_Callbacks](../../structs/metadataoutput-callbacks/document.md) struct and used to report metadata output errors. |
| [Camera\_ErrorCode OH\_MetadataOutput\_RegisterCallback(Camera\_MetadataOutput\* metadataOutput, MetadataOutput\_Callbacks\* callback)](#oh_metadataoutput_registercallback) | \- | Registers a callback to listen for metadata output events. |
| [Camera\_ErrorCode OH\_MetadataOutput\_UnregisterCallback(Camera\_MetadataOutput\* metadataOutput, MetadataOutput\_Callbacks\* callback)](#oh_metadataoutput_unregistercallback) | \- | Unregisters the callback used to listen for metadata output events. |
| [Camera\_ErrorCode OH\_MetadataOutput\_Start(Camera\_MetadataOutput\* metadataOutput)](#oh_metadataoutput_start) | \- | Starts metadata output. |
| [Camera\_ErrorCode OH\_MetadataOutput\_Stop(Camera\_MetadataOutput\* metadataOutput)](#oh_metadataoutput_stop) | \- | Stops metadata output. |
| [Camera\_ErrorCode OH\_MetadataOutput\_Release(Camera\_MetadataOutput\* metadataOutput)](#oh_metadataoutput_release) | \- | Releases a MetadataOutput instance. |

#### Function Description

#### \[h2\]OH\_MetadataOutput\_OnMetadataObjectAvailable()

typedef void (\*OH\_MetadataOutput\_OnMetadataObjectAvailable)(Camera\_MetadataOutput\* metadataOutput,Camera\_MetadataObject\* metadataObject, uint32\_t size)

**Description**

Defines the callback defined in the [MetadataOutput\_Callbacks](../../structs/metadataoutput-callbacks/document.md) struct and used to report metadata output data.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to the MetadataOutput instance that transfers the callback. |
| [Camera\_MetadataObject](../../structs/camera-metadataobject/document.md)\* metadataObject | Pointer to the metadata output data. |
| uint32\_t size | Size of the metadata object. |

#### \[h2\]OH\_MetadataOutput\_OnError()

typedef void (\*OH\_MetadataOutput\_OnError)(Camera\_MetadataOutput\* metadataOutput, Camera\_ErrorCode errorCode)

**Description**

Defines the callback defined in the [MetadataOutput\_Callbacks](../../structs/metadataoutput-callbacks/document.md) struct and used to report metadata output errors.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to the MetadataOutput instance that transfers the callback. |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) errorCode | Error code reported during metadata output. |

**See also**

[CAMERA\_SERVICE\_FATAL\_ERROR](../camera-h/document.md#camera_errorcode)

#### \[h2\]OH\_MetadataOutput\_RegisterCallback()

Camera\_ErrorCode OH\_MetadataOutput\_RegisterCallback(Camera\_MetadataOutput\* metadataOutput,MetadataOutput\_Callbacks\* callback)

**Description**

Registers a callback to listen for metadata output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to a MetadataOutput instance. |
| [MetadataOutput\_Callbacks](../../structs/metadataoutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_MetadataOutput\_UnregisterCallback()

Camera\_ErrorCode OH\_MetadataOutput\_UnregisterCallback(Camera\_MetadataOutput\* metadataOutput,MetadataOutput\_Callbacks\* callback)

**Description**

Unregisters the callback used to listen for metadata output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to a MetadataOutput instance. |
| [MetadataOutput\_Callbacks](../../structs/metadataoutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_MetadataOutput\_Start()

Camera\_ErrorCode OH\_MetadataOutput\_Start(Camera\_MetadataOutput\* metadataOutput)

**Description**

Starts metadata output.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to the MetadataOutput instance to start. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_MetadataOutput\_Stop()

Camera\_ErrorCode OH\_MetadataOutput\_Stop(Camera\_MetadataOutput\* metadataOutput)

**Description**

Stops metadata output.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to the MetadataOutput instance to stop. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_MetadataOutput\_Release()

Camera\_ErrorCode OH\_MetadataOutput\_Release(Camera\_MetadataOutput\* metadataOutput)

**Description**

Releases a MetadataOutput instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to the MetadataOutput instance to release. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |
