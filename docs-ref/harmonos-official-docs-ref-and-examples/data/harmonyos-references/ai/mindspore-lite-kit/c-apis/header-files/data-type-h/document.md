# data\_type.h

#### Overview

Declares tensor data types.

**File to include**: <mindspore/data\_type.h>

**Library**: libmindspore\_lite\_ndk.so

**System capability**: SystemCapability.Ai.MindSpore

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AI\_DataType](#oh_ai_datatype) | OH\_AI\_DataType | Enumerates data types supported by MSTensor. |

#### Enum Description

#### \[h2\]OH\_AI\_DataType

enum OH\_AI\_DataType

**Description**

Enumerates data types supported by MSTensor.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_DATATYPE\_UNKNOWN = 0 | Unknown data type. |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_STRING = 12 | String data. |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_LIST = 13 | List data. |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_TUPLE = 14 | Tuple data. |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_TENSOR = 17 | TensorList data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_BEGIN = 29 | Begin of the number type. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_BOOL = 30 | Bool data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT8 = 32 | Int8 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT16 = 33 | Int16 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT32 = 34 | Int32 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT64 = 35 | Int64 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT8 = 37 | UInt8 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT16 = 38 | UInt16 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT32 = 39 | UInt32 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT64 = 40 | UInt64 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT16 = 42 | Float16 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT32 = 43 | Float32 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT64 = 44 | Float64 data. |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_END = 46 | End of the number type. |
| OH\_AI\_DataTypeInvalid = INT32\_MAX | Invalid data type. |
