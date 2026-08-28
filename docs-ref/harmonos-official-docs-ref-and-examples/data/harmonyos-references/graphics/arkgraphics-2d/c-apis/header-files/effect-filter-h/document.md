# effect\_filter.h

#### Overview

This file declares the APIs of an image effect filter.

**File to import**: <native\_effect/effect\_filter.h>

**Library**: libnative\_effect.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 12

**Related module**: [effectKit](../../modules/effectkit/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [EffectErrorCode OH\_Filter\_CreateEffect(OH\_PixelmapNative\* pixelmap, OH\_Filter\*\* filter)](#oh_filter_createeffect) | Creates an **OH\_Filter** object. |
| [EffectErrorCode OH\_Filter\_Release(OH\_Filter\* filter)](#oh_filter_release) | Releases an **OH\_Filter** object. |
| [EffectErrorCode OH\_Filter\_Blur(OH\_Filter\* filter, float radius)](#oh_filter_blur) | Creates the frosted glass effect and adds it to a filter. |
| [EffectErrorCode OH\_Filter\_BlurWithTileMode(OH\_Filter\* filter, float radius, EffectTileMode tileMode)](#oh_filter_blurwithtilemode) | Creates the frosted glass effect and adds it to a filter. It supports the tiling mode of the shader effect. |
| [EffectErrorCode OH\_Filter\_Brighten(OH\_Filter\* filter, float brightness)](#oh_filter_brighten) | Creates the brightening effect and adds it to a filter. |
| [EffectErrorCode OH\_Filter\_GrayScale(OH\_Filter\* filter)](#oh_filter_grayscale) | Creates the grayscale effect and adds it to a filter. |
| [EffectErrorCode OH\_Filter\_Invert(OH\_Filter\* filter)](#oh_filter_invert) | Creates the inverted color effect and adds it to a filter. |
| [EffectErrorCode OH\_Filter\_SetColorMatrix(OH\_Filter\* filter, OH\_Filter\_ColorMatrix\* matrix)](#oh_filter_setcolormatrix) | Creates a custom effect through a matrix and adds it to a filter. |
| [EffectErrorCode OH\_Filter\_GetEffectPixelMap(OH\_Filter\* filter, OH\_PixelmapNative\*\* pixelmap)](#oh_filter_geteffectpixelmap) | Obtains the PixelMap used to create a filter. |

#### Function Description

#### \[h2\]OH\_Filter\_CreateEffect()

EffectErrorCode OH\_Filter\_CreateEffect(OH\_PixelmapNative\* pixelmap, OH\_Filter\*\* filter)

**Description**

Creates an **OH\_Filter** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* pixelmap | Pointer to the PixelMap. |
| [OH\_Filter](../../structs/oh-filter/document.md)\*\* filter | Double pointer to the filter created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |

#### \[h2\]OH\_Filter\_Release()

EffectErrorCode OH\_Filter\_Release(OH\_Filter\* filter)

**Description**

Releases an **OH\_Filter** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |

#### \[h2\]OH\_Filter\_Blur()

EffectErrorCode OH\_Filter\_Blur(OH\_Filter\* filter, float radius)

**Description**

Creates the frosted glass effect and adds it to a filter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |
| float radius | Blur radius of the frosted glass effect, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |

#### \[h2\]OH\_Filter\_BlurWithTileMode()

EffectErrorCode OH\_Filter\_BlurWithTileMode(OH\_Filter\* filter, float radius, EffectTileMode tileMode)

**Description**

Creates the frosted glass effect and adds it to a filter. It supports the tiling mode of the shader effect.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |
| float radius | Blur radius of the frosted glass effect, in px. |
| [EffectTileMode](../effect-types-h/document.md#effecttilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [EffectTileMode](../effect-types-h/document.md#effecttilemode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | 
Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode).

If the operation is successful, **EFFECT\_SUCCESS** is returned.

If a parameter is invalid, **EFFECT\_BAD\_PARAMETER** is returned.

 |

#### \[h2\]OH\_Filter\_Brighten()

EffectErrorCode OH\_Filter\_Brighten(OH\_Filter\* filter, float brightness)

**Description**

Creates the brightening effect and adds it to a filter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |
| float brightness | Brightness value of the brightening effect, ranging from 0 to 1. When the value is 0, the image brightness remains unchanged. When the value is 1, the image becomes fully brightened. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |

#### \[h2\]OH\_Filter\_GrayScale()

EffectErrorCode OH\_Filter\_GrayScale(OH\_Filter\* filter)

**Description**

Creates the grayscale effect and adds it to a filter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |

#### \[h2\]OH\_Filter\_Invert()

EffectErrorCode OH\_Filter\_Invert(OH\_Filter\* filter)

**Description**

Creates the inverted color effect and adds it to a filter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |

#### \[h2\]OH\_Filter\_SetColorMatrix()

EffectErrorCode OH\_Filter\_SetColorMatrix(OH\_Filter\* filter, OH\_Filter\_ColorMatrix\* matrix)

**Description**

Creates a custom effect through a matrix and adds it to a filter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |
| [OH\_Filter\_ColorMatrix](../../structs/oh-filter-colormatrix/document.md)\* matrix | Custom [OH\_Filter\_ColorMatrix](../../structs/oh-filter-colormatrix/document.md) used to create the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |

#### \[h2\]OH\_Filter\_GetEffectPixelMap()

EffectErrorCode OH\_Filter\_GetEffectPixelMap(OH\_Filter\* filter, OH\_PixelmapNative\*\* pixelmap)

**Description**

Obtains the PixelMap used to create a filter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Filter](../../structs/oh-filter/document.md)\* filter | Pointer to the filter. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\*\* pixelmap | Double pointer to the PixelMap obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [EffectErrorCode](../effect-types-h/document.md#effecterrorcode) | Returns a status code. For details, see [EffectErrorCode](../effect-types-h/document.md#effecterrorcode). |
