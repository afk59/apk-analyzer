# xeg\_gles\_extension.h

#### Overview

(OpenGL ES) API for querying extensions of XEngine.

**File to include**: <xengine/xeg\_gles\_extension.h>

**Library:** libxengine.so

**Syscap:** SystemCapability.Graphic.XEngine

**Since:** 5.0.0(12)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

#### Summary

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_EXTENSIONS](../../../modules/xengine/document.md#xeg_extensions) 0x01U

 | 

Input parameter of the [HMS\_XEG\_GetString](../../../modules/xengine/document.md#hms_xeg_getstring) API, which is used to obtain OpenGL ES extensions supported by XEngine.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef const GLubyte \*(GL\_APIENTRYP [PFN\_HMS\_XEG\_GETSTRING](../../../modules/xengine/document.md#pfn_hms_xeg_getstring)) (GLenum name)

 | 

Defines the function pointer of the OpenGL ES API for querying extensions of XEngine.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

const GLubyte \* [HMS\_XEG\_GetString](../../../modules/xengine/document.md#hms_xeg_getstring) (GLenum name)

 | 

OpenGL ES API for querying extensions of XEngine.

 |
