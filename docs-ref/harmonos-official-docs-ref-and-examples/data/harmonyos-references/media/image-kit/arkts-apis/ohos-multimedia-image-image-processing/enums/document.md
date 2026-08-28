# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/thSC4DsxS3K3gXO_cGxXRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B466C85B70374F11D5CAC6771850CF67D17821AA9AE014EE57E3AF2BAD896FA9)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### PixelMapFormat7+

Enumerates the pixel formats of images.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | 
Unknown format.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| ARGB\_888818+ | 1 | The color information consists of four components: alpha, R (Red), G (Green), and B (Blue). Each component occupies 8 bits, and the total length is 32 bits. Currently, this format supports only PixelMap APIs. |
| RGB\_565 | 2 | 

The color information consists of three components: R (Red), G (Green), and B (Blue), which occupies five bits, six bits, and five bits, respectively. The total length is 16 bits.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| RGBA\_8888 | 3 | 

The color information consists of four components: R (Red), G (Green), B (Blue), and alpha. Each component occupies 8 bits, and the total length is 32 bits. It corresponds to [CAMERA\_FORMAT\_RGBA\_8888 in CameraFormat](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/enums/document.md#cameraformat).

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| BGRA\_88889+ | 4 | 

The color information consists of four components: B (Blue), G (Green), R (Red), and alpha. Each component occupies 8 bits, and the total length is 32 bits.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| RGB\_8889+ | 5 | 

The color information consists of three components: R (Red), G (Green), and B (Blue). Each component occupies 8 bits, and the total length is 24 bits.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| ALPHA\_89+ | 6 | 

The color information consists of only the alpha component, which occupies eight bits. Each row of pixels is composed of one or more pixels, and the data for each row is aligned to 4 bytes. If the byte count of a row is not a multiple of 4, blank bytes are padded at the end to ensure proper alignment.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| RGBA\_F169+ | 7 | 

The color information consists of four components: R (Red), G (Green), B (Blue), and alpha. Each component occupies 16 bits, and the total length is 64 bits.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| NV219+ | 8 | 

YVU pixel arrangement, where the V component precedes the U component. The color information consists of the luminance component Y and the interleaved chrominance components V and U. The Y component occupies 8 bits, and the UV components occupy 4 bits on average due to 4:2:0 sampling. The total length is 12 bits on average. It corresponds to [CAMERA\_FORMAT\_YUV\_420\_SP in CameraFormat](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/enums/document.md#cameraformat).

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| NV129+ | 9 | 

YUV pixel arrangement, where the U component precedes the V component. The color information consists of the luminance component Y and the interleaved chrominance components U and V. The Y component occupies 8 bits, and the UV components occupy 4 bits on average due to 4:2:0 sampling. The total length is 12 bits on average.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| RGBA\_101010212+ | 10 | The color information consists of four components: R (Red), G (Green), B (Blue), and alpha. R, G, and B each occupy 10 bits, and alpha occupies 2 bits. The total length is 32 bits. |
| YCBCR\_P01012+ | 11 | The color information consists of the luminance component Y and the chrominance components Cb and Cr. Each component has effective 10 bits. In storage, the Y plane uses 16 bits per pixel (10 of which are effective). The UV plane is interleaved, with every four pixels taking up 32 bits of data (each chrominance component having 10 effective bits), resulting in an average of 15 effective bits overall. It corresponds to [CAMERA\_FORMAT\_YCBCR\_P010 in CameraFormat](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/enums/document.md#cameraformat). |
| YCRCB\_P01012+ | 12 | The color information consists of the luminance component Y and the chrominance components Cr and Cb. Each component has effective 10 bits. In storage, the Y plane uses 16 bits per pixel (10 of which are effective). The UV plane is interleaved, with every four pixels taking up 32 bits of data (each chrominance component having 10 effective bits), resulting in an average of 15 effective bits overall. It corresponds to [CAMERA\_FORMAT\_YCRCB\_P010 in CameraFormat](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/enums/document.md#cameraformat). |
| ASTC\_4x418+ | 102 | The storage format is ASTC\_4x4, and the memory usage is only 1/4 of that of RGBA\_8888. This format is intended for direct display scenarios. It does not support pixel access or editing in post-processing, and does not support cascaded affine transformations. |

#### AlphaType9+

Enumerates the alpha types of images.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | Unknown alpha type. |
| OPAQUE | 1 | There is no alpha or the image is opaque. |
| PREMUL | 2 | Premultiplied alpha. |
| UNPREMUL | 3 | RGB non-premultiplied alpha. |

#### AuxiliaryPictureType13+

Enumerates the auxiliary pictures types.

Auxiliary pictures do not directly participate in image display, and not all images contain auxiliary pictures.

Before obtaining and using a specific auxiliary picture, call [getAuxiliaryPicture](../interface-picture/document.md#getauxiliarypicture13) in Picture to obtain the auxiliary picture.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| GAINMAP | 1 | 
Gain map.

It is used to generate HDR images more accurately.

HDR synthesis usually involves using the SDR main image, gain map, and [HDR metadata](../interface-pixelmap/document.md#getmetadata12) to calculate the luminance mapping.

 |
| DEPTH\_MAP | 2 | 

Depth map.

It is used to store the distance between each pixel and the camera, and provides the 3D structure of the scene.

It is useful for tasks like 3D reconstruction, background separation, and scene understanding.

 |
| UNREFOCUS\_MAP | 3 | 

Unrefocus map.

It is used to store the pixel content that is not refocused during capture.

It is useful for post-processing effects such as portrait blurring, allowing users to select focus areas freely.

 |
| LINEAR\_MAP | 4 | 

Linear map.

It records lighting, color, or other visual elements linearly, providing additional data for image processing.

It is useful for visual effect enhancement and color post-processing.

 |
| FRAGMENT\_MAP | 5 | 

Fragment map.

It records areas of the original image obscured by watermarks. These areas might be cropped from the original image or filled with placeholder pixel data.

It is useful for watermark removal and original image restoration.

 |

#### MetadataType13+

Enumerates image metadata types.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| EXIF\_METADATA | 1 | Exif data. |
| FRAGMENT\_METADATA | 2 | Fragment map metadata. |
| GIF\_METADATA20+ | 5 | GIF image metadata. |

#### ScaleMode9+

Enumerates the scale modes of images.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CENTER\_CROP | 1 | Scales the image so that it fills the requested bounds of the target and crops the extra. |
| FIT\_TARGET\_SIZE | 0 | Reduces the image size to the dimensions of the target. |

#### PropertyKey7+

Enumerates the types of Exchangeable Image File Format (Exif) data of an image.

-   The key in the format example is **image.PropertyKey.XXX** (where XXX is the name of an enumeration name, for example, **image.PropertyKey.NEW\_SUBFILE\_TYPE**).
-   The format example is used only to show how to modify values and read results. For details about how to use them, see [modifyImageProperty](../interface-imagesource/document.md#modifyimageproperty11) (to modify a single Exif field), [modifyImageProperties](../interface-imagesource/document.md#modifyimageproperties12) (to modify multiple Exif fields), [getImageProperty](../interface-imagesource/document.md#getimageproperty11) (to read a single Exif field), and [getImageProperties](../interface-imagesource/document.md#getimageproperties12) (to read multiple Exif fields).

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description | Format Example |
| :-- | :-- | :-- | :-- |
| NEW\_SUBFILE\_TYPE12+ | "NewSubfileType" | 
Data type of a subfile, such as a full-resolution image, a thumbnail, or a part of a multi-frame image. The value is a bit mask. The value 0 indicates a full-resolution image, **1** indicates a thumbnail, and **2** indicates a part of a multi-frame image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Primary image');

**Example of read result**: "0"

 |
| SUBFILE\_TYPE12+ | "SubfileType" | 

Type of data contained in this subfile. This tag has been deprecated. Use **NewSubfileType** instead.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Full-resolution image data');

**Example of read result**: "1"

 |
| IMAGE\_WIDTH | "ImageWidth" | 

Image width.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'4096');

**Example of read result**: "4096"

 |
| IMAGE\_LENGTH | "ImageLength" | 

Image length.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3072');

**Example of read result**: "3072"

 |
| BITS\_PER\_SAMPLE | "BitsPerSample" | 

Number of bits per sample. For example, for RGB, which has three components, the format is 8,8,8.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use three non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'8 8 8');

or imageSource.modifyImageProperty(key,'8,8,8');

**Example of read result**: "8,8,8"

 |
| COMPRESSION12+ | "Compression" | 

Compression scheme used on the image data.

1: "Uncompressed".

2: "CCITT RLE".

3: "T4/Group 3 Fax".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Uncompressed');

**Example of read result**: "Uncompressed"

 |
| PHOTOMETRIC\_INTERPRETATION12+ | "PhotometricInterpretation" | 

Color space of the image data, for example, RGB or YCbCr.

0: "Reversed mono".

1: "Normal mono".

2: "RGB".

3: "Palette".

5: "CMYK".

6: "YCbCr".

8: "CieLAB".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Normal mono');

**Example of read result**: "Normal mono"

 |
| IMAGE\_DESCRIPTION10+ | "ImageDescription" | 

Image description.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Image description info');

**Example of read result**: "Image description info"

 |
| MAKE10+ | "Make" | 

Manufacturer.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Make');

**Example of read result**: "Make"

 |
| MODEL10+ | "Model" | 

Device model.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Model');

**Example of read result**: "Model"

 |
| STRIP\_OFFSETS12+ | "StripOffsets" | 

Byte offset of each strip.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'100');

**Example of read result**: "100"

 |
| ORIENTATION | "Orientation" | 

Image orientation.

1: **Top-left**: The image is not rotated.

2: **Top-right**: The image is flipped horizontally.

3: **Bottom-right**: The image is rotated by 180°.

4: **Bottom-left**: The image is flipped vertically.

5: **Left-top**: The image is flipped horizontally and then rotated clockwise by 270°.

6: **Right-top**: The image is rotated clockwise by 90°.

7: **Right-bottom**: The image is vertically flipped and then rotated clockwise by 90°.

8: **Left-bottom**: The image is rotated clockwise by 270°.

If an undefined value x is read, **Unknown Value x** is returned. The value of the property obtained is returned as a string. When modifying the property, you can specify the property either in the form of a number or a string.

For details about the image rotation angle, see [Obtaining the Rotation Angle of an Image](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-rotate-faq).

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Top-left');

**Example of read result**: "Top-left"

 |
| SAMPLES\_PER\_PIXEL12+ | "SamplesPerPixel" | 

Number of components per pixel. The value is **3** for RGB and YCbCr images. The **JPEG** key is used in JPEG compressed data.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3');

**Example of read result**: "3"

 |
| ROWS\_PER\_STRIP12+ | "RowsPerStrip" | 

Number of rows per strip.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'10');

**Example of read result**: "10"

 |
| STRIP\_BYTE\_COUNTS12+ | "StripByteCounts" | 

Number of bytes in each strip after compression.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'1024');

**Example of read result**: "1024"

 |
| X\_RESOLUTION12+ | "XResolution" | 

Number of pixels per ResolutionUnit in the image width (X) direction.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'72');

**Example of read result**: "72"

 |
| Y\_RESOLUTION12+ | "YResolution" | 

Number of pixels per ResolutionUnit in the image height (Y) direction.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'72');

**Example of read result**: "72"

 |
| PLANAR\_CONFIGURATION12+ | "PlanarConfiguration" | 

Storage format of components of each pixel, which can be chunky or planar.

1: "Chunky format": chunky format.

2: "Planar format": planar format.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Chunky format');

**Example of read result**: "Chunky format"

 |
| RESOLUTION\_UNIT12+ | "ResolutionUnit" | 

Unit of measurement for XResolution and YResolution, in inches or centimeters.

2: "Inch": measured in inches.

3: "Centimeter": measured in centimeters.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'2');

or imageSource.modifyImageProperty(key,'Inch');

**Example of read result**: "Inch"

 |
| TRANSFER\_FUNCTION12+ | "TransferFunction" | 

Transfer function for the image, which is usually used for color correction.

**Read/Write capability**: readable and writable.

 | This field is in a special format. Although it can be read and written, it is not parsed in the current version. |
| SOFTWARE12+ | "Software" | 

Name and version number of the software used to create the image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Software name and version');

**Example of read result**: "Software name and version"

 |
| DATE\_TIME10+ | "DateTime" | 

Date and time of image creation.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use either YYYY:MM:DD or YYYY:MM:DD HH:MM:SS.

**Example of modification**: imageSource.modifyImageProperty(key,'2024:07:07 13:45:59');

or imageSource.modifyImageProperty(key,'2024:07:07');

**Example of read result**: "2024:07:07 13:45:59" or "2024:07:07"

 |
| ARTIST12+ | "Artist" | 

Person who created the image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'User name');

**Example of read result**: "User name"

 |
| WHITE\_POINT12+ | "WhitePoint" | 

Chromaticity coordinates of the white point, the reference for "white", in the color space of the image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use two non-negative rational numbers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1,2');

or imageSource.modifyImageProperty(key,'1 2');

**Example of read result**: "1,2"

 |
| PRIMARY\_CHROMATICITIES12+ | "PrimaryChromaticities" | 

Chromaticities of the primaries of the image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'2/1');

**Example of read result**: "0.5"

 |
| PHOTO\_MODE10+ | "PhotoMode" | 

Photographing mode.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

**Example of read result**: "1"

 |
| JPEG\_INTERCHANGE\_FORMAT12+ | "JPEGInterchangeFormat" | 

Offset of the SOI marker of a JPEG interchange format bitstream.

**Read/Write capability**: read-only

 | **Example of read result**: "1024" |
| JPEG\_INTERCHANGE\_FORMAT\_LENGTH12+ | "JPEGInterchangeFormatLength" | 

Number of bytes of the JPEG stream.

**Read/Write capability**: read-only

 | **Example of read result**: "1024" |
| YCBCR\_COEFFICIENTS12+ | "YCbCrCoefficients" | 

Coefficients for the conversion matrix that transforms image data from RGB to YCbCr.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use three non-negative rational numbers, with a total sum of 1, as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'0.299, 0.587, 0.114');

**Example of read result**: "0.299, 0.587, 0.114"

 |
| YCBCR\_SUB\_SAMPLING12+ | "YCbCrSubSampling" | 

Subsampling factors used for the chrominance components of a YCbCr image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use two non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'2,2');

or imageSource.modifyImageProperty(key,'2 2');

**Example of read result**: "2,2"

 |
| YCBCR\_POSITIONING12+ | "YCbCrPositioning" | 

Positioning of subsampled chrominance components relative to luminance samples.

1: "Centered": Cb/Cr chrominance components are centered relative to the luminance pixels (common practice).

2: "Co-sited": Cb/Cr and Y sampling points align at the top-left corner.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Centered');

**Example of read result**: "Centered"

 |
| REFERENCE\_BLACK\_WHITE12+ | "ReferenceBlackWhite" | 

Reference values for black and white points.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

**Example of read result**: "1,255, 0,255, 0,255"

 |
| COPYRIGHT12+ | "Copyright" | 

Copyright notice of the image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'desc');

**Example of read result**: "desc (Photographer) - \[None\] (Editor)"

 |
| EXPOSURE\_TIME9+ | "ExposureTime" | 

Exposure time, for example, 1/33 seconds.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'1/2');

**Example of read result**: "1/33 sec."

 |
| F\_NUMBER9+ | "FNumber" | 

F number, for example, f/1.8.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'1/2');

**Example of read result**: "f/1.0"

 |
| EXPOSURE\_PROGRAM12+ | "ExposureProgram" | 

Class of the program used by the camera to set exposure when the image was captured.

0: "Not defined".

1: "Manual".

2: "Normal program".

3: "Aperture priority".

4: "Shutter priority".

5: "Creative program (biased toward depth of field)".

6: "Creative program (biased toward fast shutter speed)".

7: "Portrait mode (for closeup photos with the background out of focus)".

8: "Landscape mode (for landscape photos with the background in focus)".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Not defined');

**Example of read result**: "Not defined"

 |
| SPECTRAL\_SENSITIVITY12+ | "SpectralSensitivity" | 

Spectral sensitivity of each channel of the camera.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'SpectralSensitivity');

**Example of read result**: "SpectralSensitivity"

 |
| GPS\_VERSION\_ID12+ | "GPSVersionID" | 

GPS information version.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use four non-negative integers, separated by decimal points (.), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'2.3.0.0');

**Example of read result**: "2.3.0.0"

 |
| GPS\_LATITUDE\_REF | "GPSLatitudeRef" | 

Latitude reference (Northern or Southern Hemisphere) of the image capture location.

78: "North".

83: "South".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'78');

or imageSource.modifyImageProperty(key,'North');

**Example of read result**: "N" or "78"

 |
| GPS\_LATITUDE | "GPSLatitude" | 

Image latitude. The value must be in the format of degree,minute,second, for example, 39,54,7.542.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use three non-negative rational number strings, separated by commas (,).

**Example of modification**: imageSource.modifyImageProperty(key,'39,54,7.542');

**Example of read result**: "39,54,7.542"

 |
| GPS\_LONGITUDE\_REF | "GPSLongitudeRef" | 

Longitude reference (Eastern or Western Hemisphere) of the image capture location.

69: "East".

87: "West".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'69');

or imageSource.modifyImageProperty(key,'East');

**Example of read result**: "69" or "E"

 |
| GPS\_LONGITUDE | "GPSLongitude" | 

Image longitude. The value must be in the format of degree,minute,second, for example, 116,19,42.16.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use three non-negative rational number strings, separated by commas (,).

**Example of modification**: imageSource.modifyImageProperty(key,'116,19,42.16');

**Example of read result**: "116,19,42.16"

 |
| GPS\_ALTITUDE\_REF12+ | "GPSAltitudeRef" | 

Whether the latitude is north or south latitude.

0: Sea level, which is above sea level.

1: "Sea level reference," which is below the sea level.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Sea level');

**Example of read result**: "Sea level"

 |
| GPS\_ALTITUDE12+ | "GPSAltitude" | 

Altitude based on the reference in GPSAltitudeRef.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'123.45');

**Example of read result**: "123.45"

 |
| GPS\_TIME\_STAMP10+ | "GPSTimeStamp" | 

GPS timestamp.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use the format "HH:mm:ss.ddd".

**Example of modification**: imageSource.modifyImageProperty(key,'12:30:30.123');

**Example of read result**: "12:30:30.123"

 |
| GPS\_SATELLITES12+ | "GPSSatellites" | 

GPS satellites used for measurement.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'GPS Satellites');

**Example of read result**: "GPSSatellites"

 |
| GPS\_STATUS12+ | "GPSStatus" | 

Status of the GPS receiver when the image was recorded.

'A': "Measurement in progress", GPS is working, satellite signals are locked, and location data is trustworthy.

'V': "Measurement interrupted", GPS is not working, current positioning is unavailable, and location data may be missing or incorrect.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use letters or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'A');

or imageSource.modifyImageProperty(key,'Measurement in progress');

**Example of read result**: "A"

 |
| GPS\_MEASURE\_MODE12+ | "GPSMeasureMode" | 

GPS measurement pmode. Whether the 2D (planar) or 3D (with height) measurement mode is used for GPS positioning.

2: "2-dimensional measurement", (latitude+longitude).

3: "3-dimensional measurement", (latitude + longitude + height).

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'2');

or imageSource.modifyImageProperty(key,'2-dimensional measurement');

**Example of read result**: "2"

 |
| GPS\_DOP12+ | "GPSDOP" | 

GPS Dilution of Precision (DOP), which reflects the precision of GPS measurements taken when the photo was captured.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1.5');

**Example of read result**: "1.5"

 |
| GPS\_SPEED\_REF12+ | "GPSSpeedRef" | 

Unit used to express the movement speed of the GPS receiver.

'K': "km/h".

'M': "mph".

'N': "knots".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use letters or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'K');

or imageSource.modifyImageProperty(key,'km/h');

**Example of read result**: "K"

 |
| GPS\_SPEED12+ | "GPSSpeed" | 

Movement speed of the GPS receiver.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'123');

or imageSource.modifyImageProperty(key,'123.45');

**Example of read result**: "123.45"

 |
| GPS\_TRACK\_REF12+ | "GPSTrackRef" | 

Which type of "North" is used as the reference for the direction angle.

'T': "True direction", which is the geographic North Pole direction. This is the standard used for maps and navigation systems.

'M': "Magnetic direction", which is the direction pointed to by the Earth's magnetic field. Note that magnetic declination varies by location and changes over time.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use letters or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'T');

or imageSource.modifyImageProperty(key,'True direction');

**Example of read result**: "T"

 |
| GPS\_TRACK12+ | "GPSTrack" | 

Movement direction of the GPS receiver. Direction of movement (heading) of the camera at the moment the photo was taken, measured in degrees.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'180');

**Example of read result**: "180"

 |
| GPS\_IMG\_DIRECTION\_REF12+ | "GPSImgDirectionRef" | 

Reference of the direction of the image when it was captured.

'T': "True direction", which is the geographic North Pole direction. This is the standard used for maps and navigation systems.

'M': "Magnetic direction", which is the direction pointed to by the Earth's magnetic field. Note that magnetic declination varies by location and changes over time.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use letters or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'T');

or imageSource.modifyImageProperty(key,'True direction');

**Example of read result**: "T"

 |
| GPS\_IMG\_DIRECTION12+ | "GPSImgDirection" | 

Direction of the image when it was captured.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'120');

**Example of read result**: "120"

 |
| GPS\_MAP\_DATUM12+ | "GPSMapDatum" | 

Geodetic survey data used by the GPS receiver.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'GPS Map Datum');

**Example of read result**: "GPS Map Datum"

 |
| GPS\_DEST\_LATITUDE\_REF12+ | "GPSDestLatitudeRef" | 

Whether the latitude of the destination point is north or south latitude.

78: "North".

83: "South".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'78');

or imageSource.modifyImageProperty(key,'North');

**Example of read result**: "78"

 |
| GPS\_DEST\_LATITUDE12+ | "GPSDestLatitude" | 

Latitude of the destination point.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use three non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'39,54,7');

or imageSource.modifyImageProperty(key,'39 54 7');

**Example of read result**: "39,54,7"

 |
| GPS\_DEST\_LONGITUDE\_REF12+ | "GPSDestLongitudeRef" | 

Whether the longitude of the destination point is east or west longitude.

69: "East".

87: "West".

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'69');

or imageSource.modifyImageProperty(key,'East');

**Example of read result**: "69"

 |
| GPS\_DEST\_LONGITUDE12+ | "GPSDestLongitude" | 

Longitude of the destination point.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use three non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'116,19,42');

or imageSource.modifyImageProperty(key,'116 19 42');

**Example of read result**: "116,19,42"

 |
| GPS\_DEST\_BEARING\_REF12+ | "GPSDestBearingRef" | 

Reference of the bearing to the destination point.

'T': "True direction", which is the geographic North Pole direction. This is the standard used for maps and navigation systems.

'M': "Magnetic direction", which is the direction pointed to by the Earth's magnetic field. Note that magnetic declination varies by location and changes over time.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use letters or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'T');

or imageSource.modifyImageProperty(key,'True direction');

**Example of read result**: "T"

 |
| GPS\_DEST\_BEARING12+ | "GPSDestBearing" | 

Bearing to the destination point.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'120');

**Example of read result**: "120"

 |
| GPS\_DEST\_DISTANCE\_REF12+ | "GPSDestDistanceRef" | 

Unit used to express the distance to the destination point.

'K': "km."

'M': "miles."

'N': "nautical miles."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use letters or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'K');

or imageSource.modifyImageProperty(key,'km');

**Example of read result**: "K"

 |
| GPS\_DEST\_DISTANCE12+ | "GPSDestDistance" | 

Distance to the destination point.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'100');

**Example of read result**: "100"

 |
| GPS\_PROCESSING\_METHOD12+ | "GPSProcessingMethod" | 

String that records the name of the method used for positioning.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'GPS Processing Method');

**Example of read result**: "GPS Processing Method"

 |
| GPS\_AREA\_INFORMATION12+ | "GPSAreaInformation" | 

String that records the name of the GPS area.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'GPS Area Information');

**Example of read result**: "GPS Area Information"

 |
| GPS\_DATE\_STAMP10+ | "GPSDateStamp" | 

GPS date stamp.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use the format "YY:MM:DD".

**Example of modification**: imageSource.modifyImageProperty(key,'2020:07:07');

**Example of read result**: "2020:07:07"

 |
| GPS\_DIFFERENTIAL12+ | "GPSDifferential" | 

Whether differential correction is applied to the GPS receiver. It is critical to accurate location accuracy.

0: "Without correction", which indicates that no differential correction is used.

1:"Correction applied", which indicates that differential correction is used.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Without correction');

**Example of read result**: "0"

 |
| GPS\_H\_POSITIONING\_ERROR12+ | "GPSHPositioningError" | 

Horizontal positioning error, in meters.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'100');

**Example of read result**: "100"

 |
| ISO\_SPEED\_RATINGS9+ | "ISOSpeedRatings" | 

ISO sensitivity or ISO speed, for example, 400.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3200');

**Example of read result**: "3200"

 |
| PHOTOGRAPHIC\_SENSITIVITY12+ | "PhotographicSensitivity" | 

ISO sensitivity (ISO speed) used when the image was captured. It is the recommended field in Exif 2.3 and later. The earlier field, ISOSpeedRatings (Tag 0x8827), has the same data type and meaning. However, if both fields are present, the **PhotographicSensitivity** value should be used.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3200');

**Example of read result**: "3200"

 |
| OECF12+ | "OECF" | 

Opto-Electric Conversion Function (OECF) specified in ISO 14524.

**Read/Write capability**: readable and writable.

 | This field is in a special format. Although it can be read and written, it is not parsed in the current version. |
| SENSITIVITY\_TYPE10+ | "SensitivityType" | 

Sensitivity type.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Standard output sensitivity (SOS)');

**Example of read result**: "Standard output sensitivity (SOS)"

 |
| STANDARD\_OUTPUT\_SENSITIVITY10+ | "StandardOutputSensitivity" | 

Standard output sensitivity.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'400');

**Example of read result**: "400"

 |
| RECOMMENDED\_EXPOSURE\_INDEX10+ | "RecommendedExposureIndex" | 

Recommended exposure index.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3200');

**Example of read result**: "3200"

 |
| ISO\_SPEED10+ | "ISOSpeedRatings" | 

ISO speed.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3200');

**Example of read result**: "3200"

 |
| ISO\_SPEED\_LATITUDE\_YYY12+ | "ISOSpeedLatitudeyyy" | 

ISO speed latitude yyy value of the camera or input device, which is defined in ISO 12232.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3200');

**Example of read result**: "3200"

 |
| ISO\_SPEED\_LATITUDE\_ZZZ12+ | "ISOSpeedLatitudezzz" | 

ISO speed latitude zzz value of the camera or input device, which is defined in ISO 12232.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3200');

**Example of read result**: "3200"

 |
| EXIF\_VERSION12+ | "ExifVersion" | 

Version of the supported Exif standard.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string, separated by decimal points (.).

**Example of modification**: imageSource.modifyImageProperty(key,'2.3');

**Example of read result**: "Exif Version 2.3"

 |
| DATE\_TIME\_ORIGINAL9+ | "DateTimeOriginal" | 

Time when the original image data was generated, for example, 2022:09:06 15:48:00.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use the format "YY:MM:DD HH:mm:ss" or "YY:MM:DD".

**Example of modification**: imageSource.modifyImageProperty(key,'2024:07:07 13:45:59');

or imageSource.modifyImageProperty(key,'2024:07:07');

**Example of read result**: "2024:07:07" or "2024:07:07 13:45:59"

 |
| DATE\_TIME\_DIGITIZED12+ | "DateTimeDigitized" | 

Date and time when the image was stored as digital data, in the format of YYYY:MM:DD HH:mm:ss.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use the format "YY:MM:DD HH:mm:ss" or "YY:MM:DD".

**Example of modification**: imageSource.modifyImageProperty(key,'2024:07:07 13:45:59');

or imageSource.modifyImageProperty(key,'2024:07:07');

**Example of read result**: "2024:07:07" or "2024:07:07 13:45:59"

 |
| OFFSET\_TIME12+ | "OffsetTime" | 

Time with an offset from UTC when the image was captured.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use the format "YY:MM:DD HH:mm:ss" or "YY:MM:DD".

**Example of modification**: imageSource.modifyImageProperty(key,'2024:07:07 13:45:59');

or imageSource.modifyImageProperty(key,'2024:07:07');

**Example of read result**: "2024:07:07" or "2024:07:07 13:45:59"

 |
| OFFSET\_TIME\_ORIGINAL12+ | "OffsetTimeOriginal" | 

Time with an offset from UTC when the original image was created. It is critical for time-sensitive applications.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Offset Time Original');

**Example of read result**: "Offset Time Original"

 |
| OFFSET\_TIME\_DIGITIZED12+ | "OffsetTimeDigitized" | 

Time with an offset from UTC when the image was digitized. It helps to accurately adjust the timestamp.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Offset Time Digitized');

**Example of read result**: "Offset Time Digitized"

 |
| COMPONENTS\_CONFIGURATION12+ | "ComponentsConfiguration" | 

Specific information about compressed data.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: "Y Cb Cr -"

**Example of modification**: imageSource.modifyImageProperty(key,'Y Cb Cr -');

**Example of read result**: "Y Cb Cr -"

 |
| COMPRESSED\_BITS\_PER\_PIXEL12+ | "CompressedBitsPerPixel" | 

Number of bits per pixel. It is specific to compressed data.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'0.95');

**Example of read result**: "0.95"

 |
| SHUTTER\_SPEED12+ | "ShutterSpeedValue" | 

Shutter speed, expressed in Additive System of Photographic Exposure (APEX) values.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

**Example of read result**: "1.00 EV (1/2 sec.)"

 |
| APERTURE\_VALUE10+ | "ApertureValue" | 

Lens aperture. An example in the correct format is 4/1.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'5.6');

**Example of read result**: "5.60 EV (f/7.0)"

 |
| BRIGHTNESS\_VALUE12+ | "BrightnessValue" | 

Value of brightness, expressed in APEX values.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'2');

**Example of read result**: "2.00 EV (13.71 cd/m^2)"

 |
| EXPOSURE\_BIAS\_VALUE10+ | "ExposureBiasValue" | 

Exposure bias.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

**Example of read result**: 1.00 EV

 |
| MAX\_APERTURE\_VALUE12+ | "MaxApertureValue" | 

Smallest F number of the lens.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

**Example of read result**: "1.00 EV (f/1.4)"

 |
| SUBJECT\_DISTANCE12+ | "SubjectDistance" | 

Distance to the subject, in meters.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'100');

**Example of read result**: "100.0 m"

 |
| METERING\_MODE10+ | "MeteringMode" | 

Metering mode.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Average');

**Example of read result**: "Average"

 |
| LIGHT\_SOURCE10+ | "LightSource" | 

Light source. An example value is **Fluorescent**.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Daylight');

**Example of read result**: "Daylight"

 |
| FLASH10+ | "Flash" | 

Flash status.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0x00');

or imageSource.modifyImageProperty(key,'Flash did not fire');

**Example of read result**: "Flash did not fire"

 |
| FOCAL\_LENGTH10+ | "FocalLength" | 

Focal length of the lens.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'50');

or imageSource.modifyImageProperty(key,'50/1');

**Example of read result**: "50.0 mm"

 |
| SUBJECT\_AREA12+ | "SubjectArea" | 

Location and area of the main subject in the entire scene.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use two non-negative rational numbers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'50 50');

or imageSource.modifyImageProperty(key,'50,50');

**Example of read result**: "(x,y) = (50,50)"

 |
| MAKER\_NOTE12+ | "MakerNote" | 

Marker used by Exif/DCF manufacturers to record any required information.

This field is read-only in API versions 12 to 19 and is readable and writable in API version 20 and later.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Maker Note');

**Example of read result**: "Maker Note"

 |
| USER\_COMMENT10+ | "UserComment" | 

User comments.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'User Comment');

**Example of read result**: "User Comment"

 |
| SUBSEC\_TIME12+ | "SubsecTime" | 

Tag used to record fractions of seconds for the **DateTime** tag.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'629000');

**Example of read result**: "629000"

 |
| SUBSEC\_TIME\_ORIGINAL12+ | "SubsecTimeOriginal" | 

Tag used to record fractions of seconds for the **DateTimeOriginal** tag.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'629000');

**Example of read result**: "629000"

 |
| SUBSEC\_TIME\_DIGITIZED12+ | "SubsecTimeDigitized" | 

Tag used to record fractions of seconds for the **DateTimeDigitized** tag.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'62900');

**Example of read result**: "62900"

 |
| FLASHPIX\_VERSION12+ | "FlashpixVersion" | 

FlashPix format version supported by an FPXR file. It is used to enhance device compatibility.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use the version number format "1.0".

**Example of modification**: imageSource.modifyImageProperty(key,'1.0');

**Example of read result**: "FlashPix Version 1.0"

 |
| COLOR\_SPACE12+ | "ColorSpace" | 

Color space information, which is usually recorded as a color space specifier.

1: "sRGB", indicating the standard sRGB color space. It is the typical default value.

2: "Adobe RGB", indicating the Adobe RGB color space. It is not formally defined in Exif, but commonly used in practice.

0xffff: "Uncalibrated", indicating that the color space is uncalibrated and unknown.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'sRGB');

**Example of read result**: "sRGB"

 |
| PIXEL\_X\_DIMENSION10+ | "PixelXDimension" | 

Pixel X dimension.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'4096');

**Example of read result**: "4096"

 |
| PIXEL\_Y\_DIMENSION10+ | "PixelYDimension" | 

Pixel Y dimension.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'3072');

**Example of read result**: "3072"

 |
| RELATED\_SOUND\_FILE12+ | "RelatedSoundFile" | 

Name of an audio file related to the image data.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Related Sound File');

**Example of read result**: "Related Sound File"

 |
| FLASH\_ENERGY12+ | "FlashEnergy" | 

Strobe energy at the time the image was captured, in Beam Candle Power Seconds (BCPS).

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'5.0');

or imageSource.modifyImageProperty(key,'5/1');

**Example of read result**: "5"

 |
| SPATIAL\_FREQUENCY\_RESPONSE12+ | "SpatialFrequencyResponse" | 

Spatial frequency table of the camera or input device.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Spatial Frequency Response');

**Example of read result**: "Spatial Frequency Response"

 |
| FOCAL\_PLANE\_X\_RESOLUTION12+ | "FocalPlaneXResolution" | 

Number of pixels in the image width (X) direction per FocalPlaneResolutionUnit.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'500');

or imageSource.modifyImageProperty(key,'500.0');

**Example of read result**: "500"

 |
| FOCAL\_PLANE\_Y\_RESOLUTION12+ | "FocalPlaneYResolution" | 

Number of pixels in the image height (Y) direction per FocalPlaneResolutionUnit.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'500');

or imageSource.modifyImageProperty(key,'500.0');

**Example of read result**: "500"

 |
| FOCAL\_PLANE\_RESOLUTION\_UNIT12+ | "FocalPlaneResolutionUnit" | 

Unit for measuring FocalPlaneXResolution and FocalPlaneYResolution.

2: "Inch": measured in inches.

3: "Centimeter": measured in centimeters.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'2');

or imageSource.modifyImageProperty(key,'Inch');

**Example of read result**: "Inch"

 |
| SUBJECT\_LOCATION12+ | "SubjectLocation" | 

Location of the main subject relative to the left edge.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use two non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'123 456');

or imageSource.modifyImageProperty(key,'123,456');

**Example of read result**: "123,456"

 |
| EXPOSURE\_INDEX12+ | "ExposureIndex" | 

Exposure index selected at the time the image is captured.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

**Example of read result**: "1"

 |
| SENSING\_METHOD12+ | "SensingMethod" | 

Type of the image sensor on the camera.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'2');

or imageSource.modifyImageProperty(key,'One-chip color area sensor');

**Example of read result**: "One-chip color area sensor"

 |
| FILE\_SOURCE12+ | "FileSource" | 

Image source.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'DSC');

**Example of read result**: "DSC"

 |
| SCENE\_TYPE9+ | "SceneType" | 

Type of the scene, for example, portrait, scenery, motion, and night.

1: "Directly photographed", indicating that the image is directly captured by the image sensor.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Directly photographed');

**Example of read result**: "Directly photographed"

 |
| CFA\_PATTERN12+ | "CFAPattern" | 

Color Filter Array (CFA) geometric pattern of the image sensor.

**Read/Write capability**: readable and writable.

 | This field is in a special format. Although it can be read and written, it is not parsed in the current version. |
| CUSTOM\_RENDERED12+ | "CustomRendered" | 

Special processing on image data.

0: "Normal process", indicating normal processing (no custom rendering).

1: "Custom process", indicating custom processing (such as artistic effect, beauty, and HDR).

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Custom process');

**Example of read result**: "Custom process"

 |
| EXPOSURE\_MODE12+ | "ExposureMode" | 

Exposure mode set when the image was captured.

0: "Auto exposure."

1: "Manual exposure."

2: "Auto bracket."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Auto exposure');

**Example of read result**: "Auto exposure"

 |
| WHITE\_BALANCE10+ | "WhiteBalance" | 

White balance.

0: "Auto white balance."

1: "Manual white balance."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Auto white balance');

**Example of read result**: "Auto white balance"

 |
| DIGITAL\_ZOOM\_RATIO12+ | "DigitalZoomRatio" | 

Digital zoom ratio when the image was captured.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1/2');

**Example of read result**: "0.5"

 |
| FOCAL\_LENGTH\_IN\_35\_MM\_FILM10+ | "FocalLengthIn35mmFilm" | 

Focal length in 35mm film.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative integer string.

**Example of modification**: imageSource.modifyImageProperty(key,'50');

**Example of read result**: "50"

 |
| SCENE\_CAPTURE\_TYPE12+ | "SceneCaptureType" | 

Type of the scene that was captured.

0: "Standard."

1: "Landscape."

2: "Portrait."

3: "Night scene."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Standard');

**Example of read result**: "Standard"

 |
| GAIN\_CONTROL12+ | "GainControl" | 

Degree of overall image gain adjustment.

0: "Normal", no gain control.

1: "Low gain up."

2: "High gain up."

3: "Low gain down."

4: "High gain down."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Normal');

**Example of read result**: "Normal"

 |
| CONTRAST12+ | "Contrast" | 

Direction of contrast processing used by the camera.

0: "Normal", normal contrast.

1: "Soft", soft contrast.

2: "Hard", hard contrast.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Normal');

**Example of read result**: "Normal"

 |
| SATURATION12+ | "Saturation" | 

Direction of saturation processing used by the camera.

0:"Normal": normal saturation.

1: "Low saturation."

2: "High saturation."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Normal');

**Example of read result**: "Normal"

 |
| SHARPNESS12+ | "Sharpness" | 

Direction of sharpness processing used by the camera.

0:"Normal": normal sharpness.

1: "Soft."

2: "Hard."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'0');

or imageSource.modifyImageProperty(key,'Normal');

**Example of read result**: "Normal"

 |
| DEVICE\_SETTING\_DESCRIPTION12+ | "DeviceSettingDescription" | 

Information about the photographing conditions of a specific camera model.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of Modification**: imageSource.modifyImageProperty(key,'Device Setting Description');

**Example of read result**: "Device Setting Description"

 |
| SUBJECT\_DISTANCE\_RANGE12+ | "SubjectDistanceRange" | 

Distance to the subject.

0: "Unknown."

1: "Macro."

2: "Close view."

3: "Distant view."

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use numbers or strings.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'Macro');

**Example of read result**: "Macro"

 |
| IMAGE\_UNIQUE\_ID12+ | "ImageUniqueID" | 

Unique identifier assigned to each image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Image Unique ID');

**Example of read result**: "Image Unique ID"

 |
| CAMERA\_OWNER\_NAME12+ | "CameraOwnerName" | 

Name of the camera owner.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Camera Owner Name');

**Example of read result**: "Camera Owner Name"

 |
| BODY\_SERIAL\_NUMBER12+ | "BodySerialNumber" | 

Serial number of the camera body.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Body Serial Number');

**Example of read result**: "Body Serial Number"

 |
| LENS\_SPECIFICATION12+ | "LensSpecification" | 

Specifications of the lens.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use four non-negative rational number strings, separated by spaces or commas (,).

**Example of modification**: imageSource.modifyImageProperty(key,'12 12 12 12'); or imageSource.modifyImageProperty(key,'12,12,12,12');

**Example of read result**: "12,12,12,12"

 |
| LENS\_MAKE12+ | "LensMake" | 

Manufacturer of the lens.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Lens Make');

**Example of read result**: "Lens Make"

 |
| LENS\_MODEL12+ | "LensModel" | 

Model of the lens.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Lens Model');

**Example of read result**: "Lens Model"

 |
| LENS\_SERIAL\_NUMBER12+ | "LensSerialNumber" | 

Serial number of the lens.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Lens Serial Number');

**Example of read result**: "Lens Serial Number"

 |
| COMPOSITE\_IMAGE12+ | "CompositeImage" | 

Whether the image is a composite image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1');

or imageSource.modifyImageProperty(key,'NonComposite');

**Example of read result**: "1"

 |
| SOURCE\_IMAGE\_NUMBER\_OF\_COMPOSITE\_IMAGE12+ | "SourceImageNumberOfCompositeImage" | 

Number of source images of the composite image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use two non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'1 5');

or imageSource.modifyImageProperty(key,'1,5');

**Example of read result**: "1,5"

 |
| SOURCE\_EXPOSURE\_TIMES\_OF\_COMPOSITE\_IMAGE12+ | "SourceExposureTimesOfCompositeImage" | 

Exposure time of source images of the composite image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a string.

**Example of modification**: imageSource.modifyImageProperty(key,'Source Exposure Times Of CompositeImage');

**Example of read result**: "Source Exposure Times Of CompositeImage"

 |
| GAMMA12+ | "Gamma" | 

Gamma value.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use a non-negative rational number as a string.

**Example of modification**

imageSource.modifyImageProperty(key,'1');

**Example of read result**: "1"

 |
| DNG\_VERSION12+ | "DNGVersion" | 

DNG version. It encodes the DNG 4-tier version number.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use four non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**

imageSource.modifyImageProperty(key,'1 1 1 1');

or imageSource.modifyImageProperty(key,'1,1,1,1');

**Example of read result**: "1,1,1,1"

 |
| DEFAULT\_CROP\_SIZE12+ | "DefaultCropSize" | 

Size of the final image area, in raw image coordinates, taking into account extra pixels around the edges of the final image.

**Read/Write capability**: readable and writable.

 | 

**How to modify the parameter**: Use two non-negative integers, separated by spaces or commas (,), as a string.

**Example of modification**: imageSource.modifyImageProperty(key,'400 400');

or imageSource.modifyImageProperty(key,'400,400');

**Example of read result**: "400,400"

 |
| GIF\_LOOP\_COUNT12+ | "GIFLoopCount" | 

Number of GIF loops. The value **0** means an infinite loop, and other values means the number of loops.

**Read/Write capability**: read-only

 | \_ |
| IS\_XMAGE\_SUPPORTED12+ | "HwMnoteIsXmageSupported" | 

Whether XMAGE is supported.

**Read/Write capability**: readable and writable.

 | \_ |
| XMAGE\_MODE12+ | "HwMnoteXmageMode" | 

XMAGE watermark mode.

**Read/Write capability**: readable and writable.

 | \_ |
| XMAGE\_LEFT12+ | "HwMnoteXmageLeft" | 

X1 coordinate of the watermark region.

**Read/Write capability**: readable and writable.

 | \_ |
| XMAGE\_TOP12+ | "HwMnoteXmageTop" | 

Y1 coordinate of the watermark region.

**Read/Write capability**: readable and writable.

 | \_ |
| XMAGE\_RIGHT12+ | "HwMnoteXmageRight" | 

X2 coordinate of the watermark region.

**Read/Write capability**: readable and writable.

 | \_ |
| XMAGE\_BOTTOM12+ | "HwMnoteXmageBottom" | 

Y2 coordinate of the watermark region.

**Read/Write capability**: readable and writable.

 | \_ |
| CLOUD\_ENHANCEMENT\_MODE12+ | "HwMnoteCloudEnhancementMode" | 

Cloud enhancement mode.

**Read/Write capability**: readable and writable.

 | \_ |
| WIND\_SNAPSHOT\_MODE12+ | "HwMnoteWindSnapshotMode" | 

Motion snapshot mode.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_POINTER12+ | "HwMnoteScenePointer" | 

Pointer to the scene.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_VERSION12+ | "HwMnoteSceneVersion" | 

Scene algorithm version.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_FOOD\_CONF11+ | "HwMnoteSceneFoodConf" | 

Photographing scene: food.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_STAGE\_CONF11+ | "HwMnoteSceneStageConf" | 

Photographing scene: stage.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_BLUE\_SKY\_CONF11+ | "HwMnoteSceneBlueSkyConf" | 

Photographing scene: blue sky.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_GREEN\_PLANT\_CONF11+ | "HwMnoteSceneGreenPlantConf" | 

Photographing scene: green plant.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_BEACH\_CONF11+ | "HwMnoteSceneBeachConf" | 

Photographing scene: beach.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_SNOW\_CONF11+ | "HwMnoteSceneSnowConf" | 

Photographing scene: snow.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_SUNSET\_CONF11+ | "HwMnoteSceneSunsetConf" | 

Photographing scene: sunset.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_FLOWERS\_CONF11+ | "HwMnoteSceneFlowersConf" | 

Photographing scene: flowers.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_NIGHT\_CONF11+ | "HwMnoteSceneNightConf" | 

Photographing scene: night.

**Read/Write capability**: read-only

 | \_ |
| SCENE\_TEXT\_CONF11+ | "HwMnoteSceneTextConf" | 

Photographing scene: text.

**Read/Write capability**: read-only

 | \_ |
| FACE\_POINTER12+ | "HwMnoteFacePointer" | 

Face pointer.

**Read/Write capability**: read-only

 | \_ |
| FACE\_VERSION12+ | "HwMnoteFaceVersion" | 

Facial recognition algorithm version.

**Read/Write capability**: read-only

 | \_ |
| FACE\_COUNT11+ | "HwMnoteFaceCount" | 

Number of faces.

**Read/Write capability**: read-only

 | \_ |
| FACE\_CONF12+ | "HwMnoteFaceConf" | 

Face confidence.

**Read/Write capability**: read-only

 | \_ |
| FACE\_SMILE\_SCORE12+ | "HwMnoteFaceSmileScore" | 

Smile score of for faces.

**Read/Write capability**: read-only

 | \_ |
| FACE\_RECT12+ | "HwMnoteFaceRect" | 

Face rectangle.

**Read/Write capability**: read-only

 | \_ |
| FACE\_LEYE\_CENTER12+ | "HwMnoteFaceLeyeCenter" | 

Left eye centered.

**Read/Write capability**: read-only

 | \_ |
| FACE\_REYE\_CENTER12+ | "HwMnoteFaceReyeCenter" | 

Right eye centered.

**Read/Write capability**: read-only

 | \_ |
| FACE\_MOUTH\_CENTER12+ | "HwMnoteFaceMouthCenter" | 

Mouth centered.

**Read/Write capability**: read-only

 | \_ |
| CAPTURE\_MODE10+ | "HwMnoteCaptureMode" | 

Capture mode.

**Read/Write capability**: readable and writable.

 | \_ |
| BURST\_NUMBER12+ | "HwMnoteBurstNumber" | 

Number of burst shooting times.

**Read/Write capability**: read-only

 | \_ |
| FRONT\_CAMERA12+ | "HwMnoteFrontCamera" | 

Whether the front camera is used to take a selfie.

**Read/Write capability**: read-only

 | \_ |
| ROLL\_ANGLE11+ | "HwMnoteRollAngle" | 

Roll angle.

**Read/Write capability**: read-only

 | \_ |
| PITCH\_ANGLE11+ | "HwMnotePitchAngle" | 

Pitch angle.

**Read/Write capability**: read-only

 | \_ |
| PHYSICAL\_APERTURE10+ | "HwMnotePhysicalAperture" | 

Physical aperture.

**Read/Write capability**: read-only

 | \_ |
| FOCUS\_MODE11+ | "HwMnoteFocusMode" | 

Focus mode.

**Read/Write capability**: read-only

 | \_ |

#### FragmentMapPropertyKey13+

Enumerates the fragment map information.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| X\_IN\_ORIGINAL | "XInOriginal" | X coordinate of the top-left corner of the fragment map in the original image. |
| Y\_IN\_ORIGINAL | "YInOriginal" | Y coordinate of the top-left corner of the fragment map in the original image. |
| WIDTH | "FragmentImageWidth" | Width of the fragment map. |
| HEIGHT | "FragmentImageHeight" | Height of the fragment map. |

#### GifPropertyKey20+

Enumerates the GIF image information.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| GIF\_DELAY\_TIME | "GifDelayTime" | Duration for playing each frame of a GIF image, in milliseconds. |
| GIF\_DISPOSAL\_TYPE | "GifDisposalType" | Disposal type of each frame in a GIF image. |

#### ImageFormat9+

Enumerates the image formats.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| YCBCR\_422\_SP | 1000 | YCBCR422 semi-planar format. |
| JPEG | 2000 | JPEG encoding format. |

#### ComponentType9+

Enumerates the color component types of images.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

| Name | Value | Description |
| :-- | :-- | :-- |
| YUV\_Y | 1 | Luminance component. |
| YUV\_U | 2 | Chrominance component. |
| YUV\_V | 3 | Chrominance component. |
| JPEG | 4 | JPEG type. |

#### DecodingDynamicRange12+

Enumerates the desired dynamic range of an image during decoding.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | The image is decoded based on the format. If the image is in HDR format, it is decoded based on the HDR content; otherwise, it is decoded based on the SDR content. The image source created by calling [CreateIncrementalSource](../functions/document.md#imagecreateincrementalsource9) is decoded into SDR content. |
| SDR | 1 | The image is decoded according to the standard dynamic range. |
| HDR | 2 | The image is decoded according to the high dynamic range. The image source created by calling [CreateIncrementalSource](../functions/document.md#imagecreateincrementalsource9) is decoded into SDR content. |

#### PackingDynamicRange12+

Enumerates the desired dynamic range of an image during encoding.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | Adaptive. The [pixelmap](../interface-pixelmap/document.md) is encoded based on the format. If the PixelMap is in HDR format, it is encoded based on the HDR content; otherwise, it is encoded based on the SDR content. |
| SDR | 1 | The image is decoded according to the standard dynamic range. |

#### CropAndScaleStrategy18+

Enumerates the order of cropping and scaling.

If the **cropAndScaleStrategy** parameter is not specified in [DecodingOptions](../interfaces-others/document.md#decodingoptions7) and both **desiredRegion** and **desiredSize** are set, the final decoding result may vary slightly due to differences in decoding algorithms used for different image formats.

For example, if the original image size is 200x200, and you specify **desiredSize:{width: 150, height: 150}, desiredRegion:{x: 0, y: 0, width: 100, height: 100}**, the expectation is to decode the top-left 1/4 region of the original image and then scale the pixelMap size to 150x150.

For JPEG and WebP images (as well as some DNG images that decode a JPEG preview within the file and therefore are treated as JPEG format), the system first performs downsampling. For instance, it might downsample by 7/8 and then crop the region based on a 175x175 image size. As a result, the final cropped region will be slightly larger than the top-left 1/4 of the original image.

For SVG images, which are vector-based and can be scaled without losing clarity, the system scales the image based on the ratio of **desiredSize** to the original image size and then crops the region. This results in a decoded region that may differ from the exact 1/4 region of the original image.

To ensure consistent results when both **desiredRegion** and **desiredSize** are set, set the **cropAndScaleStrategy** parameter to **CROP\_FIRST**.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SCALE\_FIRST | 1 | If both **desiredRegion** and **desiredSize** are specified, the image is first scaled based on **desiredSize** and then cropped based on **desiredRegion**. |
| CROP\_FIRST | 2 | If both **desiredRegion** and **desiredSize** are specified, the image is first cropped based on **desiredRegion** and then scaled based on **desiredSize**. |

#### HdrMetadataKey12+

Enumerates the keys of HDR metadata used by [pixelmap](../interface-pixelmap/document.md).

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| HDR\_METADATA\_TYPE | 0 | Metadata type used by [pixelmap](../interface-pixelmap/document.md). |
| HDR\_STATIC\_METADATA | 1 | Static metadata. |
| HDR\_DYNAMIC\_METADATA | 2 | Dynamic metadata. |
| HDR\_GAINMAP\_METADATA | 3 | Metadata used by gain maps. |

#### HdrMetadataType12+

Enumerates the values available for **HDR\_METADATA\_TYPE** in [HdrMetadataKey](#hdrmetadatakey12).

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No metadata. |
| BASE | 1 | Metadata used for base graphics. |
| GAINMAP | 2 | Metadata used for gain maps. |
| ALTERNATE | 3 | Metadata used for synthesized HDR graphics. |

#### AntiAliasingLevel12+

Enumerates the anti-aliasing levels.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Nearest neighbor interpolation. |
| LOW | 1 | Bilinear interpolation. |
| MEDIUM | 2 | Bilinear interpolation with mipmap enabled. You are advised to use this value when zooming out an image. |
| HIGH | 3 | Cubic interpolation. |

#### AllocatorType15+

Enumerates the types of the memory used for image decoding.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | The system determines whether DMA memory or shared memory is used. |
| DMA | 1 | DMA memory is used. |
| SHARE\_MEMORY | 2 | Shared memory is used. |
