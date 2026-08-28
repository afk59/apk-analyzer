# OH\_Pixelmap\_HdrMetadataValue

typedef struct OH\_Pixelmap\_HdrMetadataValue {...} OH\_Pixelmap\_HdrMetadataValue

#### Overview

The struct describes the HDR metadata values used by the PixelMap and available for the key [OH\_Pixelmap\_HdrMetadataKey](../../header-files/pixelmap-native-h/document.md#oh_pixelmap_hdrmetadatakey). It is used in [OH\_PixelmapNative\_SetMetadata](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_setmetadata) and [OH\_PixelmapNative\_GetMetadata](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_getmetadata).

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [pixelmap\_native.h](../../header-files/pixelmap-native-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_HdrMetadataType](../../header-files/pixelmap-native-h/document.md#oh_pixelmap_hdrmetadatatype) type | Values available for the key **HDR\_METADATA\_TYPE**. |
| [OH\_Pixelmap\_HdrStaticMetadata](../oh-pixelmap-hdrstaticmetadata/document.md) staticMetadata | Values available for the key **HDR\_STATIC\_METADATA**. |
| [OH\_Pixelmap\_HdrDynamicMetadata](../oh-pixelmap-hdrdynamicmetadata/document.md) dynamicMetadata | Values available for the key **HDR\_DYNAMIC\_METADATA**. |
| [OH\_Pixelmap\_HdrGainmapMetadata](../oh-pixelmap-hdrgainmapmetadata/document.md) gainmapMetadata | Values available for the key **HDR\_GAINMAP\_METADATA**. |
