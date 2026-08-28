# effect\_types.h

#### Overview

This file declares the data types of the image effect filter.

**File to include**: <native\_effect/effect\_types.h>

**Library**: libnative\_effect.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 12

**Related module**: [effectKit](../../modules/effectkit/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Filter\_ColorMatrix](../../structs/oh-filter-colormatrix/document.md) | \- | Describes a matrix used to create an effect filter. |
| [OH\_Filter](../../structs/oh-filter/document.md) | OH\_Filter | Defines a struct for a filter used to generate a filter PixelMap. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) | OH\_PixelmapNative | Defines a struct for a PixelMap. |

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [EffectErrorCode](#effecterrorcode) | EffectErrorCode | Enumerates the status codes that may be used by the effect filter. |
| [EffectTileMode](#effecttilemode) | EffectTileMode | Enumerates the tile modes of the shader effect. |

#### Enum Description

#### \[h2\]EffectErrorCode

enum EffectErrorCode

**Description**

Enumerates the status codes that may be used by the effect filter.

**Since**: 12

| Value | Description |
| :-- | :-- |
| EFFECT\_SUCCESS = 0 | Operation successful. |
| EFFECT\_BAD\_PARAMETER = 401 | Invalid parameter. |
| EFFECT\_UNSUPPORTED\_OPERATION = 7600201 | Unsupported operation. |
| EFFECT\_UNKNOWN\_ERROR = 7600901 | Unknown error. |

#### \[h2\]EffectTileMode

enum EffectTileMode

**Description**

Enumerates the tile modes of the shader effect.

**Since**: 14

| Value | Description |
| :-- | :-- |
| CLAMP = 0 | Replicates the edge color if the shader effect draws outside of its original boundary. |
| REPEAT | Repeats the shader effect in both horizontal and vertical directions. |
| MIRROR | Repeats the shader effect in both horizontal and vertical directions, alternating mirror images. |
| DECAL | Renders the shader effect only within the original boundary. |
