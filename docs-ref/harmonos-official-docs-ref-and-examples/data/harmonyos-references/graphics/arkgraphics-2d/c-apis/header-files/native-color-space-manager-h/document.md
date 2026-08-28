# native\_color\_space\_manager.h

#### Overview

This file declares the functions for creating and using a color space.

**File to include**: <native\_color\_space\_manager/native\_color\_space\_manager.h>

**Library**: libnative\_color\_space\_manager.so

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Since**: 13

**Related module**: [NativeColorSpaceManager](../../modules/nativecolorspacemanager/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ColorSpacePrimaries](../../structs/colorspaceprimaries/document.md) | ColorSpacePrimaries | Describes the color space primaries. |
| [WhitePointArray](../../structs/whitepointarray/document.md) | \- | Describes a white point array. Each white point indicates the coordinates of white in the active color space. |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) | OH\_NativeColorSpaceManager | Provides the declaration of an **OH\_NativeColorSpaceManager** struct. |

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ColorSpaceName](#colorspacename) | ColorSpaceName | Defines an enum for the color space names. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_NativeColorSpaceManager\* OH\_NativeColorSpaceManager\_CreateFromName(ColorSpaceName colorSpaceName)](#oh_nativecolorspacemanager_createfromname) | 
Creates an **OH\_NativeColorSpaceManager** instance based on a color space name.

A new **OH\_NativeColorSpaceManager** instance is created each time this function is called.

 |
| [OH\_NativeColorSpaceManager\* OH\_NativeColorSpaceManager\_CreateFromPrimariesAndGamma(ColorSpacePrimaries primaries, float gamma)](#oh_nativecolorspacemanager_createfromprimariesandgamma) | 

Creates an **OH\_NativeColorSpaceManager** instance based on the color primaries and gamma value.

A new **OH\_NativeColorSpaceManager** instance is created each time this function is called.

 |
| [void OH\_NativeColorSpaceManager\_Destroy(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](#oh_nativecolorspacemanager_destroy) | Destroys an **OH\_NativeColorSpaceManager** instance. |
| [int OH\_NativeColorSpaceManager\_GetColorSpaceName(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](#oh_nativecolorspacemanager_getcolorspacename) | Obtains the color space name. |
| [WhitePointArray OH\_NativeColorSpaceManager\_GetWhitePoint(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](#oh_nativecolorspacemanager_getwhitepoint) | Obtains the white points. |
| [float OH\_NativeColorSpaceManager\_GetGamma(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](#oh_nativecolorspacemanager_getgamma) | Obtains the gamma value. |

#### Enum Description

#### \[h2\]ColorSpaceName

enum ColorSpaceName

**Description**

Defines an enum for the color space names.

**Since**: 13

| Value | Description |
| :-- | :-- |
| NONE = 0 | Unknown color space. |
| ADOBE\_RGB = 1 | Color space based on Adobe RGB. |
| DCI\_P3 = 2 | Color space based on SMPTE RP 431-2-2007 and IEC 61966-2.1:1999. |
| DISPLAY\_P3 = 3 | Color space based on SMPTE RP 431-2-2007 and IEC 61966-2.1:1999. |
| SRGB = 4 | Standard Red Green Blue (SRGB) color space based on IEC 61966-2.1:1999. |
| BT709 = 6 | Color space based on ITU-R BT.709. |
| BT601\_EBU = 7 | Color space based on ITU-R BT.601. |
| BT601\_SMPTE\_C = 8 | Color space based on ITU-R BT.601. |
| BT2020\_HLG = 9 | Color space based on ITU-R BT.2020. |
| BT2020\_PQ = 10 | Color space based on ITU-R BT.2020. |
| P3\_HLG = 11 | Color space with the color primaries of P3\_D65, the transfer characteristics of Hybrid Log-Gamma (HLG), and the color range of FULL. |
| P3\_PQ = 12 | Color space with the color primaries of P3\_D65, the transfer characteristics of Perceptual Quantizer (PQ), and the color range of FULL. |
| ADOBE\_RGB\_LIMIT = 13 | Color space with the color primaries of ADOBE\_RGB, the transfer characteristics of ADOBE\_RGB, and the color range of LIMIT. |
| DISPLAY\_P3\_LIMIT = 14 | Color space with the color primaries of P3\_D65, the transfer characteristics of SRGB, and the color range of LIMIT. |
| SRGB\_LIMIT = 15 | Color space with the color primaries of SRGB, the transfer characteristics of SRGB, and the color range of LIMIT. |
| BT709\_LIMIT = 16 | Color space with the color primaries of BT.709, the transfer characteristics of BT.709, and the color range of LIMIT. |
| BT601\_EBU\_LIMIT = 17 | Color space with the color primaries of BT.601\_P, the transfer characteristics of BT.709, and the color range of LIMIT. |
| BT601\_SMPTE\_C\_LIMIT = 18 | Color space with the color primaries of BT.601\_N, the transfer characteristics of BT.709, and the color range of LIMIT. |
| BT2020\_HLG\_LIMIT = 19 | Color space with the color primaries of BT.2020, the transfer characteristics of HLG, and the color range of LIMIT. |
| BT2020\_PQ\_LIMIT = 20 | Color space with the color primaries of BT.2020, the transfer characteristics of PQ, and the color range of LIMIT. |
| P3\_HLG\_LIMIT = 21 | Color space with the color primaries of P3\_D65, the transfer characteristics of HLG, and the color range of LIMIT. |
| P3\_PQ\_LIMIT = 22 | Color space with the color primaries of P3\_D65, the transfer characteristics of PQ, and the color range of LIMIT. |
| LINEAR\_P3 = 23 | Color space with the color primaries of P3\_D65 and the transfer characteristic of LINEAR. |
| LINEAR\_SRGB = 24 | Color space with the color primaries of SRGB and the transfer characteristic of LINEAR. |
| LINEAR\_BT709 = LINEAR\_SRGB | Color space with the color primaries of BT.709 and the transfer characteristic of LINEAR. |
| LINEAR\_BT2020 = 25 | Color space with the color primaries of BT.2020 and the transfer characteristic of LINEAR. |
| DISPLAY\_SRGB = SRGB | Color space with the color primaries of SRGB, the transfer characteristics of SRGB, and the color range of FULL. |
| DISPLAY\_P3\_SRGB = DISPLAY\_P3 | Color space with the color primaries of P3\_D65, the transfer characteristics of SRGB, and the color range of FULL. |
| DISPLAY\_P3\_HLG = P3\_HLG | Color space with the color primaries of P3\_D65, the transfer characteristics of Hybrid Log-Gamma (HLG), and the color range of FULL. |
| DISPLAY\_P3\_PQ = P3\_PQ | Color space with the color primaries of P3\_D65, the transfer characteristics of Perceptual Quantizer (PQ), and the color range of FULL. |
| CUSTOM = 5 | Custom color space. |

#### Function Description

#### \[h2\]OH\_NativeColorSpaceManager\_CreateFromName()

OH\_NativeColorSpaceManager\* OH\_NativeColorSpaceManager\_CreateFromName(ColorSpaceName colorSpaceName)

**Description**

Creates an **OH\_NativeColorSpaceManager** instance based on a color space name.

A new **OH\_NativeColorSpaceManager** instance is created each time this function is called.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ColorSpaceName](#colorspacename) colorSpaceName | Color space name of the created [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md)\* | Returns a pointer to the [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) instance. If the memory is insufficient, the **OH\_NativeColorSpaceManager** instance fails to be created. |

#### \[h2\]OH\_NativeColorSpaceManager\_CreateFromPrimariesAndGamma()

OH\_NativeColorSpaceManager\* OH\_NativeColorSpaceManager\_CreateFromPrimariesAndGamma(ColorSpacePrimaries primaries, float gamma)

**Description**

Creates an **OH\_NativeColorSpaceManager** instance based on the color primaries and gamma value.

A new **OH\_NativeColorSpaceManager** instance is created each time this function is called.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ColorSpacePrimaries](../../structs/colorspaceprimaries/document.md) primaries | Primary color of the created [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) instance. |
| float gamma | 
Gamma value of the created [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) instance. The gamma value is a floating point number used to correct the brightness range.

Generally, the gamma value is positive. A negative value results in increased brightness in low-light areas and decreased brightness in high-light areas. The value **0** indicates a linear color space.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md)\* | 
Returns a pointer to the [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) instance.

If the memory is insufficient, the **OH\_NativeColorSpaceManager** instance fails to be created.

 |

#### \[h2\]OH\_NativeColorSpaceManager\_Destroy()

void OH\_NativeColorSpaceManager\_Destroy(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)

**Description**

Destroys an **OH\_NativeColorSpaceManager** instance.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md)\* nativeColorSpaceManager | Pointer to an **OH\_NativeColorSpaceManager** instance. |

#### \[h2\]OH\_NativeColorSpaceManager\_GetColorSpaceName()

int OH\_NativeColorSpaceManager\_GetColorSpaceName(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)

**Description**

Obtains the color space name.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md)\* nativeColorSpaceManager | Pointer to an **OH\_NativeColorSpaceManager** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the color space name, which is defined in [ColorSpaceName](#colorspacename). The return value **0** means that the function call fails. |

#### \[h2\]OH\_NativeColorSpaceManager\_GetWhitePoint()

WhitePointArray OH\_NativeColorSpaceManager\_GetWhitePoint(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)

**Description**

Obtains the white points.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md)\* nativeColorSpaceManager | Pointer to an **OH\_NativeColorSpaceManager** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [WhitePointArray](../../structs/whitepointarray/document.md) | Returns a float array of white points. The value **<0.0, 0.0>** means that the function call fails. |

#### \[h2\]OH\_NativeColorSpaceManager\_GetGamma()

float OH\_NativeColorSpaceManager\_GetGamma(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)

**Description**

Obtains the gamma value.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md)\* nativeColorSpaceManager | Pointer to an **OH\_NativeColorSpaceManager** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns a float value. The value **0.0** means that the function call fails. |
