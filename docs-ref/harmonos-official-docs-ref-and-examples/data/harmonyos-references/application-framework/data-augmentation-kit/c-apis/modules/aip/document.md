# AIP

#### Overview

The ArkData Intelligence Platform (AIP) provides apps with the capabilities of vectorization, knowledge retrieval, and knowledge Q&A, and helps build on-device intelligent solutions.

**Start version**: 6.0.0(20)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[aip\_error\_code.h](../../header-files-and-structs/aip-error-code-h/document.md)

 | 

Describes error code information.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [OH\_Aip\_ErrCode](#ga1eb26b856dc8a8f5ed5c815f9a4b3417) [OH\_Aip\_ErrCode](#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

 | 

Defines an enum of error codes.

 |

#### \[h2\]Enums

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OH\_Aip\_ErrCode](#ga1eb26b856dc8a8f5ed5c815f9a4b3417) {

AIP\_OK = 0,

AIP\_E\_EXEC\_ERR = 1021200005,

AIP\_E\_OUT\_OF\_RANGE = 1021200006,

AIP\_E\_NO\_SUCH\_FIELD = 1021200007,

AIP\_E\_OVER\_LIMIT = 1021200008,

AIP\_E\_CONDITION\_OVER\_LIMIT = 1021200009,

AIP\_E\_INVALID\_ARGS = 1021200010,

AIP\_E\_EMBEDDING\_ERR = 1021200012

}

 | 

Enumerates error codes.

 |

#### Type Description

#### \[h2\]OH\_Aip\_ErrCode

typedef enum [OH\_Aip\_ErrCode](#ga1eb26b856dc8a8f5ed5c815f9a4b3417) [OH\_Aip\_ErrCode](#ga1eb26b856dc8a8f5ed5c815f9a4b3417);

**Description**

Defines an enum of error codes.

**Start version**: 6.0.0(20)

#### Enumeration Description

#### \[h2\]OH\_Aip\_ErrCode

enum [OH\_Aip\_ErrCode](#ga1eb26b856dc8a8f5ed5c815f9a4b3417);

**Description**

Enumerates error codes.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

AIP\_OK

 | 

The operation succeeded.

 |
| 

AIP\_E\_EXEC\_ERR

 | 

An execution error occurred.

 |
| 

AIP\_E\_OUT\_OF\_RANGE

 | 

The index number exceeds the allowed range.

 |
| 

AIP\_E\_NO\_SUCH\_FIELD

 | 

The field does not exist.

 |
| 

AIP\_E\_OVER\_LIMIT

 | 

The array length exceeds 512 bytes.

 |
| 

AIP\_E\_CONDITION\_OVER\_LIMIT

 | 

The number of conditions exceeds the maximum (**1**).

 |
| 

AIP\_E\_INVALID\_ARGS

 | 

Invalid parameter.

 |
| 

AIP\_E\_EMBEDDING\_ERR

 | 

Failed to generate an embedding vector.

 |
