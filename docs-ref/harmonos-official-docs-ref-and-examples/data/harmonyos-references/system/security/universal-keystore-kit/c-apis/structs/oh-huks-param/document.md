# OH\_Huks\_Param

#### Overview

Defines the types of the parameters in a parameter set.

**Since**: 9

**Related module**: [HuksTypeApi](../../modules/hukstypeapi/document.md)

**Header file**: [native\_huks\_type.h](../../header-files/native-huks-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t tag | Tag value. |
| 
union {

bool boolParam

int32\_t int32Param

uint32\_t uint32Param

uint64\_t uint64Param

[struct OH\_Huks\_Blob](../oh-huks-blob/document.md) blob

}

 | 

**boolParam**: The parameter is of the Boolean type.

**int32Param**: The parameter is of the int32\_t type.

**uint32Param**: The parameter is of the uint32\_t type.

**uint64Param**: The parameter is of the uint64\_t type.

**blob**: The parameter is of the OH\_Huks\_Blob type.

 |
