# aip\_retrieval\_query.h

#### Overview

Provides APIs related to retrieval queries.

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

typedef struct [OH\_Retrieval\_Query](../../modules/retrieval/document.md#ga754a8a9b14076a9cfd7be8dacbcae38e) [OH\_Retrieval\_Query](../../modules/retrieval/document.md#ga754a8a9b14076a9cfd7be8dacbcae38e)

 | 

Defines a retrieval keyword. Currently, only plaintext retrieval is supported.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OH\_Retrieval\_Query](../../modules/retrieval/document.md#ga754a8a9b14076a9cfd7be8dacbcae38e) \* [OH\_Retrieval\_CreateQuery](../../modules/retrieval/document.md#gad5182c984d2e5d85171fd93205ea785f) ()

 | 

Creates a retrieval keyword as the input parameter of the retrieval API.

 |
| 

int [OH\_Retrieval\_DestroyQuery](../../modules/retrieval/document.md#ga8810c6250f69bcb4ef1d5f9b6084a42b) ([OH\_Retrieval\_Query](../../modules/retrieval/document.md#ga754a8a9b14076a9cfd7be8dacbcae38e) \*query)

 | 

Destroys the retrieval keyword obtained through [OH\_Retrieval\_CreateQuery](../../modules/retrieval/document.md#gad5182c984d2e5d85171fd93205ea785f).

 |
| 

int [OH\_Retrieval\_SetOriginalQuestion](../../modules/retrieval/document.md#ga967b4d6fd7de85f9299529598dce72e4) ([OH\_Retrieval\_Query](../../modules/retrieval/document.md#ga754a8a9b14076a9cfd7be8dacbcae38e) \*query, const char \*question)

 | 

Sets retrieval keywords in [OH\_Retrieval\_Query](../../modules/retrieval/document.md#ga754a8a9b14076a9cfd7be8dacbcae38e).

 |
