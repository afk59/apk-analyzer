# status.h

#### Overview

Provides the status codes of MindSpore Lite.

**File to include**: <mindspore/status.h>

**Library**: libmindspore\_lite\_ndk.so

**System capability**: SystemCapability.Ai.MindSpore

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AI\_CompCode](#oh_ai_compcode) | \- | Defines MindSpore component codes. |
| [OH\_AI\_Status](#oh_ai_status) | OH\_AI\_Status | Defines MindSpore status codes. |

#### Enum Description

#### \[h2\]OH\_AI\_CompCode

enum OH\_AI\_CompCode

**Description**

Defines MindSpore component codes.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_COMPCODE\_CORE = 0x00000000u | MindSpore Core code. |
| OH\_AI\_COMPCODE\_MD = 0x10000000u | MindSpore MindData code. |
| OH\_AI\_COMPCODE\_ME = 0x20000000u | MindSpore MindExpression code. |
| OH\_AI\_COMPCODE\_MC = 0x30000000u | MindSpore code. |
| OH\_AI\_COMPCODE\_LITE = 0xF0000000u | MindSpore Lite code. |

#### \[h2\]OH\_AI\_Status

enum OH\_AI\_Status

**Description**

Defines MindSpore status codes.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_STATUS\_SUCCESS = 0 | Success. |
| OH\_AI\_STATUS\_CORE\_FAILED = OH\_AI\_COMPCODE\_CORE | 0x1 | MindSpore Core failure. |
| OH\_AI\_STATUS\_LITE\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -1) | MindSpore Lite error. |
| OH\_AI\_STATUS\_LITE\_NULLPTR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -2) | MindSpore Lite null pointer. |
| OH\_AI\_STATUS\_LITE\_PARAM\_INVALID = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -3) | MindSpore Lite invalid parameters. |
| OH\_AI\_STATUS\_LITE\_NO\_CHANGE = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -4) | MindSpore Lite no change. |
| OH\_AI\_STATUS\_LITE\_SUCCESS\_EXIT = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -5) | MindSpore Lite exit without errors. |
| OH\_AI\_STATUS\_LITE\_MEMORY\_FAILED = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -6) | MindSpore Lite memory allocation failure. |
| OH\_AI\_STATUS\_LITE\_NOT\_SUPPORT = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -7) | MindSpore Lite function not supported. |
| OH\_AI\_STATUS\_LITE\_THREADPOOL\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -8) | MindSpore Lite thread pool error. |
| OH\_AI\_STATUS\_LITE\_UNINITIALIZED\_OBJ = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -9) | MindSpore Lite uninitialized. |
| OH\_AI\_STATUS\_LITE\_OUT\_OF\_TENSOR\_RANGE = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -100) | MindSpore Lite tensor overflow. |
| OH\_AI\_STATUS\_LITE\_INPUT\_TENSOR\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -101) | MindSpore Lite input tensor error. |
| OH\_AI\_STATUS\_LITE\_REENTRANT\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -102) | MindSpore Lite reentry error. |
| OH\_AI\_STATUS\_LITE\_GRAPH\_FILE\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -200) | MindSpore Lite file error. |
| OH\_AI\_STATUS\_LITE\_NOT\_FIND\_OP = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -300) | MindSpore Lite operator not found. |
| OH\_AI\_STATUS\_LITE\_INVALID\_OP\_NAME = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -301) | MindSpore Lite invalid operators. |
| OH\_AI\_STATUS\_LITE\_INVALID\_OP\_ATTR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -302) | MindSpore Lite invalid operator hyperparameters. |
| OH\_AI\_STATUS\_LITE\_OP\_EXECUTE\_FAILURE = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -303) | MindSpore Lite operator execution failure. |
| OH\_AI\_STATUS\_LITE\_FORMAT\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -400) | MindSpore Lite tensor format error. |
| OH\_AI\_STATUS\_LITE\_INFER\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -500) | MindSpore Lite shape inference error. |
| OH\_AI\_STATUS\_LITE\_INFER\_INVALID = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -501) | MindSpore Lite invalid shape inference. |
| OH\_AI\_STATUS\_LITE\_INPUT\_PARAM\_INVALID = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -600) | MindSpore Lite invalid input parameters. |
