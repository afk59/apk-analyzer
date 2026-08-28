# aip\_retrieval\_condition.h

#### Overview

Provides APIs related to retrieval conditions.

**Library**: libnative\_aip\_retrieval\_ndk.so

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

**Related module**: [Retrieval](../../modules/retrieval/document.md)

#### Summary

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [OH\_Retrieval\_Condition](../../modules/retrieval/document.md#gab273fa3774c357b746a8b1f3d223022e) [OH\_Retrieval\_Condition](../../modules/retrieval/document.md#gab273fa3774c357b746a8b1f3d223022e)

 | 

Defines the retrieval condition, which can contain multiple sub-conditions.

 |
| 

typedef struct [OH\_Retrieval\_SubCondition](../../modules/retrieval/document.md#gabf02dc24d39de7926dd144966984b06a) [OH\_Retrieval\_SubCondition](../../modules/retrieval/document.md#gabf02dc24d39de7926dd144966984b06a)

 | 

Defines a retrieval sub-condition, which can be used for vector retrieval.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OH\_Retrieval\_Condition](../../modules/retrieval/document.md#gab273fa3774c357b746a8b1f3d223022e) \* [OH\_Retrieval\_CreateCondition](../../modules/retrieval/document.md#gaf596f89029870da548ab24229ab117d8) ()

 | 

Creates a retrieval condition as the input parameter of the retrieval API.

 |
| 

int [OH\_Retrieval\_DestroyCondition](../../modules/retrieval/document.md#ga494ae3c2094d8c7d7886df7323e07a31) ([OH\_Retrieval\_Condition](../../modules/retrieval/document.md#gab273fa3774c357b746a8b1f3d223022e) \*condition)

 | 

Destroys the retrieval condition obtained through [OH\_Retrieval\_CreateCondition](../../modules/retrieval/document.md#gaf596f89029870da548ab24229ab117d8).

 |
| 

int [OH\_Retrieval\_DestroySubCondition](../../modules/retrieval/document.md#ga9801829d9219eff29dcc372301c3eec4) ([OH\_Retrieval\_SubCondition](../../modules/retrieval/document.md#gabf02dc24d39de7926dd144966984b06a) \*condition)

 | 

Destroys the conditions created through [OH\_Retrieval\_SubCondition](../../modules/retrieval/document.md#gabf02dc24d39de7926dd144966984b06a).

 |
| 

int [OH\_Retrieval\_AddSubCondition](../../modules/retrieval/document.md#ga2a1a77b04c4876fb8f6836fb7c85a3fd) ([OH\_Retrieval\_Condition](../../modules/retrieval/document.md#gab273fa3774c357b746a8b1f3d223022e) \*condition, [OH\_Retrieval\_SubCondition](../../modules/retrieval/document.md#gabf02dc24d39de7926dd144966984b06a) \*subCondition)

 | 

Adds a sub-condition to a retrieval condition.

 |
