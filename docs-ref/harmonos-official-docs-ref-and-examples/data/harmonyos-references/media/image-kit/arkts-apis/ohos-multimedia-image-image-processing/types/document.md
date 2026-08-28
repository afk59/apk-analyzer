# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/rTMyUQFwRGC-i8RBVSl1Mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD21F95C4FE85F8520927E1C5617C708B3F68186C7AE4E1415B4EEF02C763056)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### HdrMetadataValue12+

type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata

Describes the HDR metadata values used by a PixelMap, which corresponds to the values available for [HdrMetadataKey](../enums/document.md#hdrmetadatakey12).

**System capability**: SystemCapability.Multimedia.Image.Core

| Type | Description |
| :-- | :-- |
| [HdrMetadataType](../enums/document.md#hdrmetadatatype12) | Metadata value corresponding to the **HDR\_METADATA\_TYPE** key in [HdrMetadataKey](../enums/document.md#hdrmetadatakey12). |
| [HdrStaticMetadata](../interfaces-others/document.md#hdrstaticmetadata12) | Metadata value corresponding to the **HDR\_STATIC\_METADATA** key in [HdrMetadataKey](../enums/document.md#hdrmetadatakey12). |
| ArrayBuffer | Metadata value corresponding to the **HDR\_DYNAMIC\_METADATA** key in [HdrMetadataKey](../enums/document.md#hdrmetadatakey12). |
| [HdrGainmapMetadata](../interfaces-others/document.md#hdrgainmapmetadata12) | Metadata value corresponding to the **HDR\_GAINMAP\_METADATA** key in [HdrMetadataKey](../enums/document.md#hdrmetadatakey12). |
