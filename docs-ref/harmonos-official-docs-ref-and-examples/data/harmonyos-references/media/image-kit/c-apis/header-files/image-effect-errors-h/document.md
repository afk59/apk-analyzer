# image\_effect\_errors.h

#### Overview

The file declares the error codes used by the image effector.

**Library**: libimage\_effect.so

**File to include**: <multimedia/image\_effect/image\_effect\_errors.h>

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Related module**: [ImageEffect](../../modules/imageeffect/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ImageEffect\_ErrorCode](#imageeffect_errorcode) | ImageEffect\_ErrorCode | Enumerates the error codes used by the image effector. |

#### Enum Description

#### \[h2\]ImageEffect\_ErrorCode

enum ImageEffect\_ErrorCode

**Description**

Enumerates the error codes used by the image effector.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| EFFECT\_SUCCESS = 0 | The operation is successful. |
| EFFECT\_ERROR\_PERMISSION\_DENIED = 201 | Permission verification fails. |
| EFFECT\_ERROR\_PARAM\_INVALID = 401 | Parameter check fails. |
| EFFECT\_BUFFER\_SIZE\_NOT\_MATCH = 29000001 | The output buffer size does not match. |
| EFFECT\_COLOR\_SPACE\_NOT\_MATCH = 29000002 | The input and output color spaces do not match. |
| EFFECT\_INPUT\_OUTPUT\_NOT\_MATCH = 29000101 | The input and output configurations do not match. For example, the input is a surface, but the output is a PixelMap. |
| EFFECT\_EFFECT\_NUMBER\_LIMITED = 29000102 | The maximum number is reached. |
| EFFECT\_INPUT\_OUTPUT\_NOT\_SUPPORTED = 29000103 | The input or output configuration is not supported. |
| EFFECT\_ALLOCATE\_MEMORY\_FAILED = 29000104 | Memory allocation fails. |
| EFFECT\_PARAM\_ERROR = 29000121 | Invalid parameter value. For example, the filter parameter value is invalid. |
| EFFECT\_KEY\_ERROR = 29000122 | Invalid parameter. For example, the filter parameter is invalid. |
| EFFECT\_UNKNOWN = 29000199 | Undefined error. |
