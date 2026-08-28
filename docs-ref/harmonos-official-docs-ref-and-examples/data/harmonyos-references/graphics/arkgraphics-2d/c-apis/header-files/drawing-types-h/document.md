# drawing\_types.h

#### Overview

This file declares the data types of the canvas, brush, pen, bitmap, and path used to draw 2D graphics.

**File to include**: <native\_drawing/drawing\_types.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md) | OH\_Drawing\_Point2D | Defines a two-dimensional coordinate point. |
| [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md) | OH\_Drawing\_Corner\_Radii | Defines a struct for the radii of a rounded corner. The radii consist of the x-axis radius and y-axis radius. |
| [OH\_Drawing\_Point3D](../../structs/oh-drawing-point3d/document.md) | OH\_Drawing\_Point3D | Defines a three-dimensional coordinate point. |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) | OH\_Drawing\_Image\_Info | Describes the image information. |
| [OH\_Drawing\_RectStyle\_Info](../../structs/oh-drawing-rectstyle-info/document.md) | OH\_Drawing\_RectStyle\_Info | Describes the style of a rectangle. |
| [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) | OH\_Drawing\_String | Describes a string of characters encoded in UTF-16. |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) | OH\_Drawing\_Canvas | Defines a struct for a rectangular canvas, on which various shapes, images, and texts can be drawn by using the brush and pen. |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) | OH\_Drawing\_Pen | Defines a struct for a pen, which is used to describe the style and color to outline a shape. |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) | OH\_Drawing\_Region | Defines a struct for a region, which represents a closed area on the canvas for more accurate graphic control. |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) | OH\_Drawing\_Brush | Defines a struct for a brush, which is used to describe the style and color to fill in a shape. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) | OH\_Drawing\_Path | Defines a struct for a path, which is used to customize various shapes. |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md) | OH\_Drawing\_Bitmap | Defines a struct for a bitmap, which is a memory area that contains the pixel data of a shape. |
| [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md) | OH\_Drawing\_Point | Defines a struct for a coordinate point. |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) | OH\_Drawing\_PixelMap | Defines a struct for a pixel map, which is used to wrap the real pixel map supported by the image framework. |
| [OH\_Drawing\_ColorSpace](../../structs/oh-drawing-colorspace/document.md) | OH\_Drawing\_ColorSpace | Defines a struct for a color space, which is used to describe the color information. |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) | OH\_Drawing\_PathEffect | Defines a struct for a path effect that affects the stroke. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) | OH\_Drawing\_Rect | Defines a struct for a rectangle. |
| [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md) | OH\_Drawing\_RoundRect | Defines a struct for a rounded rectangle. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) | OH\_Drawing\_Matrix | Defines a struct for a matrix, which is used to describe coordinate transformation. |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) | OH\_Drawing\_ShaderEffect | Defines a struct for a shader effect, which is used to describe the source color of the drawn content. |
| [OH\_Drawing\_ShadowLayer](../../structs/oh-drawing-shadowlayer/document.md) | OH\_Drawing\_ShadowLayer | Defines a struct for a shadow, which is used to describe the shadow layer of the drawn content. |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) | OH\_Drawing\_Filter | Defines a struct for a filter, which consists of a color filter, mask filter, and image filter. |
| [OH\_Drawing\_MaskFilter](../../structs/oh-drawing-maskfilter/document.md) | OH\_Drawing\_MaskFilter | Defines a struct for a mask filter. |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md) | OH\_Drawing\_ColorFilter | Defines a struct for a color filter, which is used to convert a color into a new one. |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) | OH\_Drawing\_Font | Defines a struct for a font. |
| [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md) | OH\_Drawing\_FontFeatures | Defines a struct for font features, which are typesetting rules within a font that determine how glyphs look, such as ligatures, alternates, and superscripts/subscripts. |
| [OH\_Drawing\_MemoryStream](../../structs/oh-drawing-memorystream/document.md) | OH\_Drawing\_MemoryStream | Defines a struct for a memory stream. |
| [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md) | OH\_Drawing\_FontArguments | Defines a struct for font arguments. |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) | OH\_Drawing\_Typeface | Defines a struct for a typeface. |
| [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md) | OH\_Drawing\_TextBlob | Defines a struct for a text blob, an immutable container that holds multiple texts. Each text blob consists of glyphs and position. |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) | OH\_Drawing\_Image | Defines a struct for an image that describes a two-dimensional pixel array. |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) | OH\_Drawing\_ImageFilter | Defines a struct for an image filter, which is used to operate all color bits that make up image pixels. |
| [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) | OH\_Drawing\_SamplingOptions | Defines a struct for sampling options, which describe the sampling methods for images and bitmaps. |
| [OH\_Drawing\_TextBlobBuilder](../../structs/oh-drawing-textblobbuilder/document.md) | OH\_Drawing\_TextBlobBuilder | Defines a struct for a text blob builder, which is used to build a text blob. |
| [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md) | OH\_Drawing\_GpuContext | Defines a struct for the GPU context, which is used to describe the GPU backend context. |
| [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md) | OH\_Drawing\_Surface | Defines a struct for a surface, which is used to manage the content drawn on the canvas. |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) | OH\_Drawing\_FontMgr | Defines a struct for the font manager, which is used for font management. |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) | OH\_Drawing\_FontStyleSet | Defines a struct for a font style set, which is used for font style family matching. |
| [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md) | OH\_Drawing\_RecordCmdUtils | Defines the recording command tool, which is used to generate recording commands. |
| [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md) | OH\_Drawing\_RecordCmd | Defines the recording command class, which is used to store the set of recording commands. |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) | OH\_Drawing\_Array | Defines a struct for an array object, which is used to store multiple objects of the same type. |

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_ColorFormat](#oh_drawing_colorformat) | OH\_Drawing\_ColorFormat | Defines an enum for the storage formats of bitmap pixels. |
| [OH\_Drawing\_AlphaFormat](#oh_drawing_alphaformat) | OH\_Drawing\_AlphaFormat | Defines an enum for the alpha formats of bitmap pixels. |
| [OH\_Drawing\_BlendMode](#oh_drawing_blendmode) | OH\_Drawing\_BlendMode | 
Defines an enum for blend modes. In blend mode, each operation generates a new color from two colors (source color and destination color).

These operations are the same for the red, green, and blue color channels (the alpha channel follows a different rule).

For simplicity, the following description uses the alpha channel as an example rather than naming each channel individually. For brevity, the following abbreviations are used:

**s**: source.

**d**: destination.

**sa**: source alpha.

**da**: destination alpha.

The following abbreviations are used in the calculation result:

**r**: The calculation methods of the four channels are the same.

**ra**: used when only the alpha channel is manipulated.

**rc**: used when the other three color channels are manipulated.

 |
| [OH\_Drawing\_TextEncoding](#oh_drawing_textencoding) | OH\_Drawing\_TextEncoding | Defines an enum for the text encoding types. |

#### Enum Description

#### \[h2\]OH\_Drawing\_ColorFormat

enum OH\_Drawing\_ColorFormat

**Description**

Defines an enum for the storage formats of bitmap pixels.

**Since**: 8

| Value | Description |
| :-- | :-- |
| COLOR\_FORMAT\_UNKNOWN | Unknown format. |
| COLOR\_FORMAT\_ALPHA\_8 | Each pixel is represented by 8 bits, which together indicate alpha. |
| COLOR\_FORMAT\_RGB\_565 | Each pixel is represented by 16 bits. From the most significant bit to the least significant bit, the first 5 bits indicate red, the subsequent 6 bits indicate green, and the last 5 bits indicate blue. |
| COLOR\_FORMAT\_ARGB\_4444 | Each pixel is represented by 16 bits. From the most significant bit to the least significant bit, every 4 bits indicate alpha, red, green, and blue, respectively. |
| COLOR\_FORMAT\_RGBA\_8888 | Each pixel is represented by 32 bits. From the most significant bit to the least significant bit, every 8 bits indicate alpha, red, green, and blue, respectively. |
| COLOR\_FORMAT\_BGRA\_8888 | Each pixel is represented by 32 bits. From the most significant bit to the least significant bit, every 8 bits indicate blue, green, red, and alpha, respectively. |

#### \[h2\]OH\_Drawing\_AlphaFormat

enum OH\_Drawing\_AlphaFormat

**Description**

Defines an enum for the alpha formats of bitmap pixels.

**Since**: 8

| Value | Description |
| :-- | :-- |
| ALPHA\_FORMAT\_UNKNOWN | Unknown format. |
| ALPHA\_FORMAT\_OPAQUE | The bitmap does not have the alpha component. |
| ALPHA\_FORMAT\_PREMUL | The color component of each pixel is premultiplied by the alpha component. |
| ALPHA\_FORMAT\_UNPREMUL | The color component of each pixel is not premultiplied by the alpha component. |

#### \[h2\]OH\_Drawing\_BlendMode

enum OH\_Drawing\_BlendMode

**Description**

Defines an enum for blend modes. In blend mode, each operation generates a new color from two colors (source color and destination color).

These operations are the same for the red, green, and blue color channels (the alpha channel follows a different rule).

For simplicity, the following description uses the alpha channel as an example rather than naming each channel individually. For brevity, the following abbreviations are used:

**s**: source.

**d**: destination.

**sa**: source alpha.

**da**: destination alpha.

The following abbreviations are used in the calculation result:

**r**: The calculation methods of the four channels are the same.

**ra**: used when only the alpha channel is manipulated.

**rc**: used when the other three color channels are manipulated.

**Since**: 11

| Value | Description |
| :-- | :-- |
| BLEND\_MODE\_CLEAR | Clear mode. r = 0. |
| BLEND\_MODE\_SRC | r = s (The four channels of **result** are equal to the four channels of **source**, that is, the result is equal to the source.) |
| BLEND\_MODE\_DST | r = d (The four channels of **result** are equal to the four channels of **destination**, that is, the result is equal to the destination.) |
| BLEND\_MODE\_SRC\_OVER | r = s + (1 - sa) \* d. |
| BLEND\_MODE\_DST\_OVER | r = d + (1 - da) \* s. |
| BLEND\_MODE\_SRC\_IN | r = s \* da. |
| BLEND\_MODE\_DST\_IN | r = d \* sa. |
| BLEND\_MODE\_SRC\_OUT | r = s \* (1 - da). |
| BLEND\_MODE\_DST\_OUT | r = d \* (1 - sa). |
| BLEND\_MODE\_SRC\_ATOP | r = s \* da + d \* (1 - sa). |
| BLEND\_MODE\_DST\_ATOP | r = d \* sa + s \* (1 - da). |
| BLEND\_MODE\_XOR | r = s \* (1 - da) + d \* (1 - sa). |
| BLEND\_MODE\_PLUS | r = min(s + d, 1). |
| BLEND\_MODE\_MODULATE | r = s \* d. |
| BLEND\_MODE\_SCREEN | Screen mode. r = s + d - s \* d. |
| BLEND\_MODE\_OVERLAY | Overlay mode. |
| BLEND\_MODE\_DARKEN | Darken mode. rc = s + d - max(s \* da, d \* sa), ra = s + (1 - sa) \* d. |
| BLEND\_MODE\_LIGHTEN | Lighten mode. rc = rc = s + d - min(s \* da, d \* sa), ra = s + (1 - sa) \* d. |
| BLEND\_MODE\_COLOR\_DODGE | Color dodge mode. |
| BLEND\_MODE\_COLOR\_BURN | Color burn mode. |
| BLEND\_MODE\_HARD\_LIGHT | Hard light mode. |
| BLEND\_MODE\_SOFT\_LIGHT | Soft light mode. |
| BLEND\_MODE\_DIFFERENCE | Difference mode. rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = s + (1 - sa) \* d. |
| BLEND\_MODE\_EXCLUSION | Exclusion mode. rc = s + d - two(s \* d), ra = s + (1 - sa) \* d. |
| BLEND\_MODE\_MULTIPLY | Multiply mode. r = s \* (1 - da) + d \* (1 - sa) + s \* d. |
| BLEND\_MODE\_HUE | Hue mode. |
| BLEND\_MODE\_SATURATION | Saturation mode. |
| BLEND\_MODE\_COLOR | Color mode. |
| BLEND\_MODE\_LUMINOSITY | Luminosity mode. |

#### \[h2\]OH\_Drawing\_TextEncoding

enum OH\_Drawing\_TextEncoding

**Description**

Defines an enum for the text encoding types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| TEXT\_ENCODING\_UTF8 | One byte used to indicate UTF-8 or ASCII characters. |
| TEXT\_ENCODING\_UTF16 | Two bytes used to indicate most Unicode characters. |
| TEXT\_ENCODING\_UTF32 | Four bytes used to indicate all Unicode characters. |
| TEXT\_ENCODING\_GLYPH\_ID | Two bytes used to indicate the glyph index. |
