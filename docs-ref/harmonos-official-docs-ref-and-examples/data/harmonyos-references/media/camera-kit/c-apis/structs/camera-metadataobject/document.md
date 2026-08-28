# Camera\_MetadataObject

typedef struct Camera\_MetadataObject {...} Camera\_MetadataObject

#### Overview

The struct describes the camera metadata.

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Camera\_MetadataObjectType](../../header-files/camera-h/document.md#camera_metadataobjecttype) type | Type of the metadata object. |
| int64\_t timestamp | Timestamp of the metadata object, in nanoseconds (ns). |
| [Camera\_Rect](../camera-rect/document.md)\* boundingBox | Pointer to the axis aligned bounding box of the metadata object. |
