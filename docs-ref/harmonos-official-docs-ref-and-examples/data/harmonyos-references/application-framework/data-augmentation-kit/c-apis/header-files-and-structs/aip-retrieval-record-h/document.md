# aip\_retrieval\_record.h

#### Overview

Provides APIs related to retrieval results.

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

typedef struct [OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952) [OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952)

 | 

Defines the retrieval result, including the fields returned from the knowledge base and their values.

 |
| 

typedef struct [OH\_Retrieval\_RecordItem](../../modules/retrieval/document.md#gab0ce809958f4e406378fe926a8a9269f) [OH\_Retrieval\_RecordItem](../../modules/retrieval/document.md#gab0ce809958f4e406378fe926a8a9269f)

 | 

Defines the database bucket array in the retrieval result.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int [OH\_Retrieval\_DestroyRecord](../../modules/retrieval/document.md#ga92addac70c2eeb71b2ebf370d982aa48) ([OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record)

 | 

Destroys the retrieval result obtained through the retrieval API [OH\_Retrieval\_Retrieve](../../modules/retrieval/document.md#ga9b5b65705a02d8817f65dd01955cfe77).

 |
| 

int [OH\_Retrieval\_GetRecordLength](../../modules/retrieval/document.md#gae806d473b297a2d3accd5b34aca68bd9) (const [OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record, uint32\_t \*length)

 | 

Obtains the length of the database bucket array in the retrieval result [OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952).

 |
| 

int [OH\_Retrieval\_GetRecordItem](../../modules/retrieval/document.md#ga41b814740cf743acf9c3ee6edbc0bed4) (const [OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record, uint32\_t index, const [OH\_Retrieval\_RecordItem](../../modules/retrieval/document.md#gab0ce809958f4e406378fe926a8a9269f) \*\*item)

 | 

Obtains the database bucket array in the retrieval result [OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952).

 |
| 

int [OH\_Retrieval\_GetItemSize](../../modules/retrieval/document.md#gaa2e5538a14e0d33ef3315551314a9044) (const [OH\_Retrieval\_RecordItem](../../modules/retrieval/document.md#gab0ce809958f4e406378fe926a8a9269f) \*items, const char \*fieldName, size\_t \*size)

 | 

Obtains the size of the value of a specified field in the database bucket array [OH\_Retrieval\_RecordItem](../../modules/retrieval/document.md#gab0ce809958f4e406378fe926a8a9269f). The **size** value contains the null terminator.

 |
| 

int [OH\_Retrieval\_GetItemText](../../modules/retrieval/document.md#ga273f6ae58af8630fec0f8d9c1472c659) (const [OH\_Retrieval\_RecordItem](../../modules/retrieval/document.md#gab0ce809958f4e406378fe926a8a9269f) \*items, const char \*fieldName, char \*value, size\_t size)

 | 

Obtains the value of a specified field in the database bucket array [OH\_Retrieval\_RecordItem](../../modules/retrieval/document.md#gab0ce809958f4e406378fe926a8a9269f).

 |
