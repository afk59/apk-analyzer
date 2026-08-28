# aip\_retrieval\_condition\_vector.h

#### Overview

Provides APIs related to vector conditions.

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

typedef struct [OH\_Retrieval\_SubCondition](../../modules/retrieval/document.md#gabf02dc24d39de7926dd144966984b06a) [OH\_Retrieval\_VectorCondition](../../modules/retrieval/document.md#ga7d0df66cb913d5948c58223864774b10)

 | 

Defines a vector retrieval condition, including the retrieval parameters and filter conditions.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OH\_Retrieval\_VectorCondition](../../modules/retrieval/document.md#ga7d0df66cb913d5948c58223864774b10) \* [OH\_Retrieval\_CreateVectorCondition](../../modules/retrieval/document.md#ga9ba9d25126a97b67197b3f7b6fa90bfc) ()

 | 

Creates a vector retrieval condition.

 |
| 

int [OH\_Retrieval\_DestroyVectorCondition](../../modules/retrieval/document.md#ga94ffaaedc2262aeeb5a98cc53d309b89) ([OH\_Retrieval\_VectorCondition](../../modules/retrieval/document.md#ga7d0df66cb913d5948c58223864774b10) \*condition)

 | 

Destroys the retrieval condition obtained through [OH\_Retrieval\_CreateVectorCondition](../../modules/retrieval/document.md#ga9ba9d25126a97b67197b3f7b6fa90bfc).

 |
| 

int [OH\_Retrieval\_SetVectorRecallLimit](../../modules/retrieval/document.md#ga3add0883ce112a17432b44733a965b60) ([OH\_Retrieval\_VectorCondition](../../modules/retrieval/document.md#ga7d0df66cb913d5948c58223864774b10) \*condition, uint32\_t limit)

 | 

Sets the maximum number of vector retrieval results in the retrieval conditions.

 |
| 

int [OH\_Retrieval\_SetSimilarityThreshold](../../modules/retrieval/document.md#gad92af7e32a48d8429bf06a587501e244) ([OH\_Retrieval\_VectorCondition](../../modules/retrieval/document.md#ga7d0df66cb913d5948c58223864774b10) \*condition, double threshold)

 | 

Sets the similarity threshold of vector retrieval in a retrieval condition.

 |
