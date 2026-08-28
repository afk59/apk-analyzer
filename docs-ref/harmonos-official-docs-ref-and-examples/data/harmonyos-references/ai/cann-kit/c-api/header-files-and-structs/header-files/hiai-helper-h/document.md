# hiai\_helper.h

#### Overview

Defines the APIs for querying the CANN Kit version and checking the model compatibility.

**Library:** libhiai\_foundation.so

**Syscap:** SystemCapability.AI.HiAIFoundation

**Since:** 4.1.0(11)

**Related Modules:**[CANN](../../../modules/cann/document.md)

#### Summary

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_Compatibility](../../../modules/cann/document.md#hiai_compatibility) {

HIAI\_COMPATIBILITY\_COMPATIBLE = 0,

HIAI\_COMPATIBILITY\_INCOMPATIBLE = 1

}

 | 

Model compatibility.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

const char \* [HMS\_HiAI\_GetVersion](../../../modules/cann/document.md#hms_hiai_getversion) (void)

 | 

Obtains the CANN Kit version number. The result is in _hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3_ format, where **X****1** indicates whether NPU is supported. The value **0** indicates no and other values indicate yes.

 |
| 

[HiAI\_Compatibility](../../../modules/cann/document.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromFile](../../../modules/cann/document.md#hms_hiaicompatibility_checkfromfile) (const char \*file)

 | 

Queries the compatibility of the model stored in the file.

 |
| 

[HiAI\_Compatibility](../../../modules/cann/document.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromBuffer](../../../modules/cann/document.md#hms_hiaicompatibility_checkfrombuffer) (const void \*data, size\_t size)

 | 

Queries the compatibility of the model stored in the memory.

 |
