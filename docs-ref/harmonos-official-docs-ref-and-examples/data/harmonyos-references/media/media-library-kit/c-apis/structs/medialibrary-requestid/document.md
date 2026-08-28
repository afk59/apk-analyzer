# MediaLibrary\_RequestId

typedef struct MediaLibrary\_RequestId {...} MediaLibrary\_RequestId

#### Overview

Defines a struct for the request ID.

A value of this type is returned when a media asset is requested.

The request ID can be used to cancel a request.

If a request fails, an all-zero value, for example, **00000000-0000-0000-0000-000000000000** is returned.

**Since**: 12

**Related module**: [MediaAssetManager](../../modules/mediaassetmanager/document.md)

**Header file**: [media\_asset\_base\_capi.h](../../header-files/media-asset-base-capi-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char requestId\[UUID\_STR\_MAX\_LENGTH\] | Request ID. |
