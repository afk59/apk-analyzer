# GlobalColorPicker

#### Overview

Provides the global color picker capability.

**System capability**: SystemCapability.Stylus.ColorPicker

**Start version**: 5.0.0(12)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[native\_gcp\_api.h](../../header-files-and-structs/header-file/native-gcp-api-h/document.md)

 | 

Declares the global color picker capability.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [HMS\_GCP\_Color](../../header-files-and-structs/structs/hms-gcp-color/document.md)

 | 

Defines the structure of a color value.

 |
| 

struct [HMS\_GCP\_PickedColorInfo](../../header-files-and-structs/structs/hms-gcp-pickedcolorinfo/document.md)

 | 

Defines the structure of picked color information.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef void(\* [HMS\_GCP\_OnResult](#gac06acd25757a5a72f4f8d0aec5821a52)) (void \*userData, [HMS\_GCP\_PickedColorInfo](../../header-files-and-structs/structs/hms-gcp-pickedcolorinfo/document.md) colorInfo, const int32\_t code)

 | 

Callback used to receive the picked color result.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HMS\_GCP\_ColorSpace](#gafad683a86359c6a71ae84f54338e9e28) {

HMS\_GCP\_UNKNOWN = 0,

HMS\_GCP\_ADOBE\_RGB\_1998 = 1,

HMS\_GCP\_DCI\_P3 = 2,

HMS\_GCP\_DISPLAY\_P3 = 3,

HMS\_GCP\_SRGB = 4,

HMS\_GCP\_BT709 = 6,

HMS\_GCP\_BT601\_EBU = 7,

HMS\_GCP\_BT601\_SMPTE\_C = 8,

HMS\_GCP\_BT2020\_HLG = 9,

HMS\_GCP\_BT2020\_PQ = 10,

HMS\_GCP\_P3\_HLG = 11,

HMS\_GCP\_P3\_PQ = 12,

HMS\_GCP\_ADOBE\_RGB\_1998\_LIMIT = 13,

HMS\_GCP\_DISPLAY\_P3\_LIMIT = 14,

HMS\_GCP\_SRGB\_LIMIT = 15,

HMS\_GCP\_BT709\_LIMIT = 16,

HMS\_GCP\_BT601\_EBU\_LIMIT = 17,

HMS\_GCP\_BT601\_SMPTE\_C\_LIMIT = 18,

HMS\_GCP\_BT2020\_HLG\_LIMIT = 19,

HMS\_GCP\_BT2020\_PQ\_LIMIT = 20,

HMS\_GCP\_P3\_HLG\_LIMIT = 21,

HMS\_GCP\_P3\_PQ\_LIMIT = 22,

HMS\_GCP\_LINEAR\_P3 = 23,

HMS\_GCP\_LINEAR\_SRGB = 24,

HMS\_GCP\_LINEAR\_BT2020 = 25,

CUSTOM = 5

}

 | 

Enumeration of color space.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_GCP\_StartColorPicker](#ga4c202f3df255013b9920f26027065176) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

 | 

Starts the global color picker. This API is used to start the color picker. The color value is not displayed when the color picker is moved.

 |
| 

int32\_t [HMS\_GCP\_StartColorPickerWithColorValue](#ga8b044a1cfcd3b6eb8461e70c66d2c578) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

 | 

Starts the global color picker. This API is used to start the color picker. The color value is displayed when the color picker is moved.

**Start version**: 5.1.0(18)

 |

#### Type Description

#### \[h2\]HMS\_GCP\_OnResult

typedef void(\* [HMS\_GCP\_OnResult](#gac06acd25757a5a72f4f8d0aec5821a52)) (void \*userData, [HMS\_GCP\_PickedColorInfo](../../header-files-and-structs/structs/hms-gcp-pickedcolorinfo/document.md) colorInfo, const int32\_t code)

**Description**

Callback used to receive the picked color result.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

userData

 | 

Pointer to user data. It can be a null pointer.

 |
| 

colorInfo

 | 

Picked color information that needs to be saved by the user.

 |
| 

code

 | 

Result code.

**0**: Color successfully picked.

**1013900001**: IPC failed.

**1013900002**: Insufficient memory.

**1013900003**: Invalid service.

**1013900004**: Multi-app calling.

**1013900005**: Background service call.

 |

#### Enumeration Type Description

#### \[h2\]HMS\_GCP\_ColorSpace

enum HMS\_GCP\_ColorSpace

**Description**

Enumeration of color space.

**Start version**: 5.0.0(12)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

HMS\_GCP\_UNKNOWN

 | 

Unknown color space.

 |
| 

HMS\_GCP\_ADOBE\_RGB\_1998

 | 

Color space based on Adobe RGB.

 |
| 

HMS\_GCP\_DCI\_P3

 | 

Color space based on SMPTE RP 431-2-2007 and IEC 61966-2.1:1999.

 |
| 

HMS\_GCP\_DISPLAY\_P3

 | 

Color space based on SMPTE RP 431-2-2007 and IEC 61966-2.1:1999.

 |
| 

HMS\_GCP\_SRGB

 | 

Color space based on the standard red, green, and blue (sRGB) of IEC 61966-2.1:1999.

 |
| 

HMS\_GCP\_BT709

 | 

Color space based on ITU-R BT.709, PRIMARY\_BT709, TRANSFUNC\_BT709, and Range\_FULL.

 |
| 

HMS\_GCP\_BT601\_EBU

 | 

Color space based on ITU-R BT.601, PRIMARY\_BT601\_P, TRANSFUNC\_BT709, and Range\_FULL.

 |
| 

HMS\_GCP\_BT601\_SMPTE\_C

 | 

Color space based on ITU-R BT.601, PRIMARY\_BT601\_N, TRANSFUNC\_BT709, and Range\_FULL.

 |
| 

HMS\_GCP\_BT2020\_HLG

 | 

Color space based on ITU-R BT.2020, PRIMARY\_BT2020, TRANSFUNC\_HLG, and Range\_FULL.

 |
| 

HMS\_GCP\_BT2020\_PQ

 | 

Color space based on ITU-R BT.2020, PRIMARY\_BT2020, TRANSFUNC\_PQ, and Range\_FULL.

 |
| 

HMS\_GCP\_P3\_HLG

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_P3\_D65, TRANSFUNC\_HLG, and Range\_FULL.

 |
| 

HMS\_GCP\_P3\_PQ

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_P3\_D65, TRANSFUNC\_PQ, and Range\_FULL.

 |
| 

HMS\_GCP\_ADOBE\_RGB\_1998\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_ADOBE\_RGB, TRANSFUNC\_ADOBE\_RGB, and Range\_LIMIT.

 |
| 

HMS\_GCP\_DISPLAY\_P3\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_P3\_D65, TRANSFUNC\_SRGB, and Range\_LIMIT.

 |
| 

HMS\_GCP\_SRGB\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_SRGB, TRANSFUNC\_SRGB, and Range\_LIMIT.

 |
| 

HMS\_GCP\_BT709\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_BT709, TRANSFUNC\_BT709, and Range\_LIMIT.

 |
| 

HMS\_GCP\_BT601\_EBU\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_BT601\_P, TRANSFUNC\_BT709, and Range\_LIMIT.

 |
| 

HMS\_GCP\_BT601\_SMPTE\_C\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_BT601\_N, TRANSFUNC\_BT709, and Range\_LIMIT.

 |
| 

HMS\_GCP\_BT2020\_HLG\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_BT2020, TRANSFUNC\_HLG, and Range\_LIMIT.

 |
| 

HMS\_GCP\_BT2020\_PQ\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_BT2020, TRANSFUNC\_PQ, and Range\_LIMIT.

 |
| 

HMS\_GCP\_P3\_HLG\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_P3\_D65, TRANSFUNC\_HLG, and Range\_LIMIT.

 |
| 

HMS\_GCP\_P3\_PQ\_LIMIT

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_P3\_D65, TRANSFUNC\_PQ, and Range\_LIMIT.

 |
| 

HMS\_GCP\_LINEAR\_P3

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_P3\_D65, and TRANSFUNC\_LINEAR.

 |
| 

HMS\_GCP\_LINEAR\_SRGB

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_SRGB, and TRANSFUNC\_LINEAR.

 |
| 

HMS\_GCP\_LINEAR\_BT2020

 | 

Color space based on ITU-R BT.2020, PRIMARIES\_BT2020, and TRANSFUNC\_LINEAR.

 |
| 

CUSTOM

 | 

Custom color space.

 |

#### Function Description

#### \[h2\]HMS\_GCP\_StartColorPicker()

int32\_t [HMS\_GCP\_StartColorPicker](#ga4c202f3df255013b9920f26027065176) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

**Description**

Starts the global color picker. The color value is not displayed when the color picker is moved.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

initialPosX

 | 

X coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen width, in pixels.

 |
| 

initialPosY

 | 

Y coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen height, in pixels.

 |
| 

onResultCallback

 | 

Callback for receiving the picked color information.

 |
| 

userData

 | 

Pointer to user data. It can be a null pointer.

 |

#### \[h2\]HMS\_GCP\_StartColorPickerWithColorValue()

int32\_t [HMS\_GCP\_StartColorPickerWithColorValue](#ga8b044a1cfcd3b6eb8461e70c66d2c578) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

**Description**

Starts the global color picker.

This API is used to start the color picker. The color value is displayed when the color picker is moved.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

initialPosX

 | 

X coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen width, in pixels.

 |
| 

initialPosY

 | 

Y coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen height, in pixels.

 |
| 

onResultCallback

 | 

Callback for receiving the picked color information.

 |
| 

userData

 | 

Pointer to user data. It can be a null pointer.

 |

Result code.

**0**: Color successfully picked.

**1013900001**: IPC failed.

**1013900002**: Insufficient memory.

**1013900003**: Invalid service.

**1013900004**: Multi-app calling.

**1013900005**: Background service call.
