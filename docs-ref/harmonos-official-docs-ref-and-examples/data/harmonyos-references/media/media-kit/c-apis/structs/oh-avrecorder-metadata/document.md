# OH\_AVRecorder\_Metadata

typedef struct OH\_AVRecorder\_Metadata {...} OH\_AVRecorder\_Metadata

#### Overview

The struct describes the metadata.

**Since**: 18

**Related module**: [AVRecorder](../../modules/avrecorder/document.md)

**Header file**: [avrecorder\_base.h](../../header-files/avrecorder-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* genre | Pointer to the type or genre of the media asset. |
| char\* videoOrientation | Pointer to the video rotation direction, in degrees. |
| [OH\_AVRecorder\_Location](../oh-avrecorder-location/document.md) location | Geographical location of the media asset. |
| [OH\_AVRecorder\_MetadataTemplate](../oh-avrecorder-metadatatemplate/document.md) customInfo | Custom key-value mappings read from **moov.meta.list**. |
