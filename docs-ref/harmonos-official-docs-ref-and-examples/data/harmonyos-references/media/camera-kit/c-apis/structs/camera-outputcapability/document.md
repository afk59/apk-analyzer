# Camera\_OutputCapability

typedef struct Camera\_OutputCapability {...} Camera\_OutputCapability

#### Overview

The struct describes the camera output capability.

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Camera\_Profile](../camera-profile/document.md)\*\* previewProfiles | Double pointer to the list of preview profiles. |
| uint32\_t previewProfilesSize | Size of the preview profiles. |
| [Camera\_Profile](../camera-profile/document.md)\*\* photoProfiles | 
Double pointer to the list of photo profiles.

In the configuration file, **size** is set to the width and height of the camera resolution, not the actual width and height of an output image.

 |
| uint32\_t photoProfilesSize | Size of the photo profiles. |
| [Camera\_VideoProfile](../camera-videoprofile/document.md)\*\* videoProfiles | Double pointer to the list of video profiles. |
| uint32\_t videoProfilesSize | Size of the video profiles. |
| [Camera\_MetadataObjectType](../../header-files/camera-h/document.md#camera_metadataobjecttype)\*\* supportedMetadataObjectTypes | Double pointer to the list of the metadata object types supported. |
| uint32\_t metadataProfilesSize | Size of the metadata profiles. |
