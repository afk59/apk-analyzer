# buffer\_common.h

#### Overview

This file declares the common types used in the **NativeBuffer** module.

**File to include**: <native\_buffer/buffer\_common.h>

**Library**: libnative\_buffer.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

**Related module**: [OH\_NativeBuffer](../../modules/oh-nativebuffer/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeBuffer\_ColorXY](../../structs/oh-nativebuffer-colorxy/document.md) | OH\_NativeBuffer\_ColorXY | Describes the X and Y coordinates of the primary color. |
| [OH\_NativeBuffer\_Smpte2086](../../structs/oh-nativebuffer-smpte2086/document.md) | OH\_NativeBuffer\_Smpte2086 | Describes the SMPTE ST 2086 static metadata. |
| [OH\_NativeBuffer\_Cta861](../../structs/oh-nativebuffer-cta861/document.md) | OH\_NativeBuffer\_Cta861 | Describes the CTA-861.3 static metadata. |
| [OH\_NativeBuffer\_StaticMetadata](../../structs/oh-nativebuffer-staticmetadata/document.md) | OH\_NativeBuffer\_StaticMetadata | Describes the HDR static metadata. |

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeBuffer\_ColorSpace](#oh_nativebuffer_colorspace) | OH\_NativeBuffer\_ColorSpace | Defines an enum for the color spaces of an **OH\_NativeBuffer** instance. |
| [OH\_NativeBuffer\_MetadataType](#oh_nativebuffer_metadatatype) | OH\_NativeBuffer\_MetadataType | Defines an enum for the **OH\_NativeBuffer** image standards. |
| [OH\_NativeBuffer\_MetadataKey](#oh_nativebuffer_metadatakey) | OH\_NativeBuffer\_MetadataKey | Defines an enum for the key values of **OH\_NativeBuffer** description information, such as HDR metadata and ROI metadata. |
| [OH\_NativeBuffer\_Format](#oh_nativebuffer_format) | OH\_NativeBuffer\_Format | Defines an enum for the **OH\_NativeBuffer** formats. |
| [OH\_NativeBuffer\_TransformType](#oh_nativebuffer_transformtype) | OH\_NativeBuffer\_TransformType | Defines an enum for the conversion types of **OH\_NativeBuffer**. |

#### Enum Description

#### \[h2\]OH\_NativeBuffer\_ColorSpace

enum OH\_NativeBuffer\_ColorSpace

**Description**

Defines an enum for the color spaces of an **OH\_NativeBuffer** instance.

This enum is moved from **native\_buffer.h** to this header file since API version 12.

Before API version 12, use this enum only if **native\_buffer.h** is referenced. From API version 12 onwards, this enum can be used properly whether **native\_buffer.h** or **buffer\_common.h** is referenced.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 11

| Value | Description |
| :-- | :-- |
| OH\_COLORSPACE\_NONE | No color space is available. |
| OH\_COLORSPACE\_BT601\_EBU\_FULL | The color gamut is BT601\_P, the transfer function is BT709, the conversion matrix is BT601\_P, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_BT601\_SMPTE\_C\_FULL | The color gamut is BT601\_N, the transfer function is BT709, the conversion matrix is BT601\_N, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_BT709\_FULL | The color gamut is BT709, the transfer function is BT709, the conversion matrix is BT709, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_BT2020\_HLG\_FULL | The color gamut is BT2020, the transfer function is HLG, the conversion matrix is BT2020, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_BT2020\_PQ\_FULL | The color gamut is BT2020, the transfer function is PQ, the conversion matrix is BT2020, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_BT601\_EBU\_LIMIT | The color gamut is BT601\_P, the transfer function is BT709, the conversion matrix is BT601\_P, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_BT601\_SMPTE\_C\_LIMIT | The color gamut is BT601\_N, the transfer function is BT709, the conversion matrix is BT601\_N, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_BT709\_LIMIT | The color gamut is BT709, the transfer function is BT709, the conversion matrix is BT709, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | The color gamut is BT2020, the transfer function is HLG, the conversion matrix is BT2020, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | The color gamut is BT2020, the transfer function is PQ, the conversion matrix is BT2020, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_SRGB\_FULL | The color gamut is SRGB, the transfer function is SRGB, the conversion matrix is BT601\_N, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_P3\_FULL | The color gamut is P3\_D65, the transfer function is SRGB, the conversion matrix is P3, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_P3\_HLG\_FULL | The color gamut is P3\_D65, the transfer function is HLG, the conversion matrix is P3, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_P3\_PQ\_FULL | The color gamut is P3\_D65, the transfer function is PQ, the conversion matrix is P3, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_ADOBERGB\_FULL | The color gamut is ADOBERGB, the transfer function is ADOBERGB, the conversion matrix is ADOBERGB, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_SRGB\_LIMIT | The color gamut is SRGB, the transfer function is SRGB, the conversion matrix is BT601\_N, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_P3\_LIMIT | The color gamut is P3\_D65, the transfer function is SRGB, the conversion matrix is P3, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_P3\_HLG\_LIMIT | The color gamut is P3\_D65, the transfer function is HLG, the conversion matrix is P3, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_P3\_PQ\_LIMIT | The color gamut is P3\_D65, the transfer function is PQ, the conversion matrix is P3, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_ADOBERGB\_LIMIT | The color gamut is ADOBERGB, the transfer function is ADOBERGB, the conversion matrix is ADOBERGB, and the data range is RANGE\_LIMITED. |
| OH\_COLORSPACE\_LINEAR\_SRGB | The color gamut is SRGB, and the transfer function is LINEAR. |
| OH\_COLORSPACE\_LINEAR\_BT709 | It is equivalent to **OH\_COLORSPACE\_LINEAR\_SRGB**. |
| OH\_COLORSPACE\_LINEAR\_P3 | The color gamut is P3\_D65, and the transfer function is LINEAR. |
| OH\_COLORSPACE\_LINEAR\_BT2020 | The color gamut is BT2020, and the transfer function is LINEAR. |
| OH\_COLORSPACE\_DISPLAY\_SRGB | It is equivalent to **OH\_COLORSPACE\_SRGB\_FULL**. |
| OH\_COLORSPACE\_DISPLAY\_P3\_SRGB | It is equivalent to **OH\_COLORSPACE\_P3\_FULL**. |
| OH\_COLORSPACE\_DISPLAY\_P3\_HLG | It is equivalent to **OH\_COLORSPACE\_P3\_HLG\_FULL**. |
| OH\_COLORSPACE\_DISPLAY\_P3\_PQ | It is equivalent to **OH\_COLORSPACE\_P3\_PQ\_FULL**. |
| OH\_COLORSPACE\_DISPLAY\_BT2020\_SRGB | The color gamut is BT2020, the transfer function is SRGB, the conversion matrix is BT2020, and the data range is RANGE\_FULL. |
| OH\_COLORSPACE\_DISPLAY\_BT2020\_HLG | It is equivalent to **OH\_COLORSPACE\_BT2020\_HLG\_FULL**. |
| OH\_COLORSPACE\_DISPLAY\_BT2020\_PQ | It is equivalent to **OH\_COLORSPACE\_BT2020\_PQ\_FULL**. |

#### \[h2\]OH\_NativeBuffer\_MetadataType

enum OH\_NativeBuffer\_MetadataType

**Description**

Defines an enum for the **OH\_NativeBuffer** image standards.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

| Value | Description |
| :-- | :-- |
| OH\_VIDEO\_HDR\_HLG | Video HLG. |
| OH\_VIDEO\_HDR\_HDR10 | Video HDR10. |
| OH\_VIDEO\_HDR\_VIVID | Video HDR Vivid. |
| OH\_IMAGE\_HDR\_VIVID\_DUAL | 
Image HDR Vivid Dual.

**Since**: 22

 |
| OH\_IMAGE\_HDR\_VIVID\_SINGLE | 

Image HDR Vivid Single.

**Since**: 22

 |
| OH\_VIDEO\_NONE = -1 | 

No metadata.

**Since**: 13

 |

#### \[h2\]OH\_NativeBuffer\_MetadataKey

enum OH\_NativeBuffer\_MetadataKey

**Description**

Defines an enum for the key values of **OH\_NativeBuffer** description information, such as HDR metadata and ROI metadata.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

| Value | Description |
| :-- | :-- |
| OH\_HDR\_METADATA\_TYPE | Metadata type. For details about the available options, see [OH\_NativeBuffer\_MetadataType](#oh_nativebuffer_metadatatype). **size** indicates the size of **OH\_NativeBuffer\_MetadataType**. |
| OH\_HDR\_STATIC\_METADATA | Static metadata. For details about the available options, see [OH\_NativeBuffer\_StaticMetadata](../../structs/oh-nativebuffer-staticmetadata/document.md). **size** indicates the size of **OH\_NativeBuffer\_StaticMetadata**. |
| OH\_HDR\_DYNAMIC\_METADATA | Dynamic metadata. For details about the available options, see the SEI byte stream in the video stream. The value range of **size** is 1-3000. |
| OH\_REGION\_OF\_INTEREST\_METADATA | 
ROI metadata of video encoding and decoding. The configuration format is as follows: Top1,Left1-Bottom1,Right1=QpOffset1;Top2,Left2-Bottom2,Right2=QpOffset2;

Each ROI box consists of the position information (**Top,Left-Bottom,Right**) and encoding quality offset information (**QpOffset**), and ends with a semicolon (;).

The encoding quality offset information of the ROI box can be defaulted. The default value is **\-3**. The configuration example when the default value is used is as follows: **Top1,Left1-Bottom1,Right1;Top2,Left2-Bottom2,Right2;**

A maximum of six ROIs can be configured for each group of ROI metadata, and the total area of the ROIs cannot exceed 1/5 of the image.

This enumerated value can be called only through the [OH\_NativeBuffer\_SetMetadataValue()](../native-buffer-h/document.md#oh_nativebuffer_setmetadatavalue) API.

**Since**: 22

 |

#### \[h2\]OH\_NativeBuffer\_Format

enum OH\_NativeBuffer\_Format

**Description**

Defines an enum for the **OH\_NativeBuffer** formats.

This enum is moved from **native\_buffer.h** to this header file since API version 22.

Before API version 22, use this enum only if **native\_buffer.h** is referenced. From API version 22 onwards, this enum can be used properly whether **native\_buffer.h** or **buffer\_common.h** is referenced.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 10

| Value | Description |
| :-- | :-- |
| NATIVEBUFFER\_PIXEL\_FMT\_CLUT8 = 0 | 
CLUT8.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_CLUT1 | 

CLUT1.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_CLUT4 | 

CLUT4.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_565 = 3 | RGB565. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_5658 | RGBA5658. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBX\_4444 | RGBX4444. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_4444 | RGBA4444. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_444 | RGB444. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBX\_5551 | RGBX5551. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_5551 | RGBA5551. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_555 | RGB555. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBX\_8888 | RGBX8888. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 | RGBA8888. |
| NATIVEBUFFER\_PIXEL\_FMT\_RGB\_888 | RGB888. |
| NATIVEBUFFER\_PIXEL\_FMT\_BGR\_565 | BGR565. |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRX\_4444 | BGRX4444. |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRA\_4444 | BGRA4444. |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRX\_5551 | BGRX5551. |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRA\_5551 | BGRA5551. |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRX\_8888 | BGRX8888. |
| NATIVEBUFFER\_PIXEL\_FMT\_BGRA\_8888 | BGRA8888. |
| NATIVEBUFFER\_PIXEL\_FMT\_YUV\_422\_I | 

YUV422 interleaved.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_422\_SP | 

YCbCr422 semi-planar format.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_422\_SP | 

YCrCb422 semi-planar.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP | 

YCbCr420 semi-planar.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP | 

YCrCb420 semi-planar.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_422\_P | 

YCbCr422 planar.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_422\_P | 

YCrCb422 planar.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_P | 

YCbCr420 planar.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_P | 

YCrCb420 planar.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YUYV\_422\_PKG | 

YUYV422 packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_UYVY\_422\_PKG | 

UYVY422 packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YVYU\_422\_PKG | 

YVYU422 packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_VYUY\_422\_PKG | 

VYUY422 packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | 

RGBA\_1010102 packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010 | 

YCBCR420 semi-planar 10-bit packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010 | 

YCRCB420 semi-planar 10-bit packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_RAW10 | 

Raw 10-bit packed.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_BLOB | 

BLOB.

**Since**: 15

 |
| NATIVEBUFFER\_PIXEL\_FMT\_RGBA16\_FLOAT | 

RGBA16 float.

**Since**: 15

 |
| NATIVEBUFFER\_PIXEL\_FMT\_Y8 = 40 | 

Y8.

**Since**: 20

 |
| NATIVEBUFFER\_PIXEL\_FMT\_Y16 = 41 | 

Y16.

**Since**: 20

 |
| NATIVEBUFFER\_PIXEL\_FMT\_VENDER\_MASK = 0X7FFF0000 | 

Vender mask.

**Since**: 12

 |
| NATIVEBUFFER\_PIXEL\_FMT\_BUTT = 0X7FFFFFFF | Invalid format. |

#### \[h2\]OH\_NativeBuffer\_TransformType

enum OH\_NativeBuffer\_TransformType

**Description**

Defines an enum for the conversion types of **OH\_NativeBuffer**.

This enum is moved from **native\_buffer.h** to this header file since API version 22.

Before API version 22, use this enum only if **native\_buffer.h** is referenced. From API version 22 onwards, this enum can be used properly whether **native\_buffer.h** or **buffer\_common.h** is referenced.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

| Value | Description |
| :-- | :-- |
| NATIVEBUFFER\_ROTATE\_NONE = 0 | No rotation. |
| NATIVEBUFFER\_ROTATE\_90 | Rotates by 90 degrees. |
| NATIVEBUFFER\_ROTATE\_180 | Rotates by 180 degrees. |
| NATIVEBUFFER\_ROTATE\_270 | Rotates by 270 degrees. |
| NATIVEBUFFER\_FLIP\_H | Flips horizontally. |
| NATIVEBUFFER\_FLIP\_V | Flips vertically. |
| NATIVEBUFFER\_FLIP\_H\_ROT90 | Flips horizontally and rotates by 90 degrees. |
| NATIVEBUFFER\_FLIP\_V\_ROT90 | Flips vertically and rotates by 90 degrees. |
| NATIVEBUFFER\_FLIP\_H\_ROT180 | Flips horizontally and rotates by 180 degrees. |
| NATIVEBUFFER\_FLIP\_V\_ROT180 | Flips vertically and rotates by 180 degrees. |
| NATIVEBUFFER\_FLIP\_H\_ROT270 | Flips horizontally and rotates by 270 degrees. |
| NATIVEBUFFER\_FLIP\_V\_ROT270 | Flips vertically and rotates by 270 degrees. |
