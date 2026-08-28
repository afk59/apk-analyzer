# Rcp\_FormFieldValue

#### Overview

Simple form data field value. For details, please refer to [Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) and [Rcp\_MultipartFormFieldValue](../rcp-multipartformfieldvalue/document.md).

**Start version**: 5.0.0(12)

**Related module**: [RemoteCommunication](../../../modules/remotecommunication/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Rcp\_FormValueType](../../../modules/remotecommunication/document.md#ga9d851389347a39bd4bb849ac31cfa478) [type](#aa2f5ee901ec18d3a45a3a4b32ce648a0)

 | 

Data type used in the union structure.

 |
| 

union {

 | 

Union structure.

 |
| 

uint8\_t [varBool](#adfd646a1efd2853ce64eee38cc1f2cc2)

 | 

Boolean data type.

 |
| 

int32\_t [varInt32](#ad63df8004b42c748ea9e43e33dc63f6d)

 | 

Int32 data type.

 |
| 

int64\_t [varInt64](#a5392f4cacec7a90c59c5e857f022da4b)

 | 

Int64 data type.

 |
| 

double [varDouble](#ae1dd3fa224b13f7a3daefddffda41721)

 | 

Double data type.

 |
| 

[Rcp\_Buffer](../rcp-buffer/document.md) [varStr](#a0e38aaf495895692510bc46b36acf4ad)

 | 

String data type.

 |
| 

} **data**

 | 

The **type** variable defines the data type used in **data**.

 |
| 

struct [Rcp\_FormFieldValue](#) \* [next](#a3ceed646c6f06c8249ff962782da0068)

 | 

Pointer to the next [Rcp\_FormFieldValue](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]next

struct [Rcp\_FormFieldValue](#)\* Rcp\_FormFieldValue::next

**Description**

Pointer to the next [Rcp\_FormFieldValue](#) in the data chain.

#### \[h2\]type

[Rcp\_FormValueType](../../../modules/remotecommunication/document.md#ga9d851389347a39bd4bb849ac31cfa478) Rcp\_FormFieldValue::type

**Description**

Data type used in the union structure.

#### \[h2\]varBool

uint8\_t Rcp\_FormFieldValue::varBool

**Description**

Boolean value.

#### \[h2\]varDouble

double Rcp\_FormFieldValue::varDouble

**Description**

Double value.

#### \[h2\]varInt32

int32\_t Rcp\_FormFieldValue::varInt32

**Description**

32-bit integer.

#### \[h2\]varInt64

int64\_t Rcp\_FormFieldValue::varInt64

**Description**

64-bit integer.

#### \[h2\]varStr

[Rcp\_Buffer](../rcp-buffer/document.md) Rcp\_FormFieldValue::varStr

**Description**

String.
