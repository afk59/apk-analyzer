# native\_gcp\_api.h

#### Overview

Declares the global color picker capability.

**Library:** libcolorpicker\_ndk.z.so

**System capability**: SystemCapability.Stylus.ColorPicker

**Start version**: 5.0.0(12)

**Related module**: [GlobalColorPicker](../../../modules/globalcolorpicker/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [HMS\_GCP\_Color](../../structs/hms-gcp-color/document.md)

 | 

Defines the structure of a color value.

 |
| 

struct [HMS\_GCP\_PickedColorInfo](../../structs/hms-gcp-pickedcolorinfo/document.md)

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

typedef void(\* [HMS\_GCP\_OnResult](../../../modules/globalcolorpicker/document.md#gac06acd25757a5a72f4f8d0aec5821a52)) (void \*userData, [HMS\_GCP\_PickedColorInfo](../../structs/hms-gcp-pickedcolorinfo/document.md) colorInfo, const int32\_t code)

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

[HMS\_GCP\_ColorSpace](../../../modules/globalcolorpicker/document.md#gafad683a86359c6a71ae84f54338e9e28){

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

int32\_t [HMS\_GCP\_StartColorPicker()](../../../modules/globalcolorpicker/document.md#ga4c202f3df255013b9920f26027065176)() (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](../../../modules/globalcolorpicker/document.md#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

 | 

Starts the global color picker.

 |
| 

int32\_t [HMS\_GCP\_StartColorPickerWithColorValue()](../../../modules/globalcolorpicker/document.md#ga8b044a1cfcd3b6eb8461e70c66d2c578)() (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](../../../modules/globalcolorpicker/document.md#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

 | 

Starts the global color picker.

 |
