# Rcp\_MultipartFormFieldValue

#### Overview

Multi-part form field value, which will be used in [Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9).

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

[Rcp\_MultipartValueType](../../../modules/remotecommunication/document.md#ga76d003b4f9a244c9d11def4128ceeda8) [type](#ae2593c817ecd64051feacb47ea40e647)

 | 

Data type used in the union structure.

 |
| 

union {

 | 

Union structure.

 |
| 

[Rcp\_FormFieldValue](../rcp-formfieldvalue/document.md) [formValue](#a5fa2b6978205158b9df2f332b8de46ee)

 | 

Simple form data field value.

 |
| 

[Rcp\_FormFieldFileValue](../rcp-formfieldfilevalue/document.md) [formFileValue](#ada1b5ea030493ddc6c0b77c0fd6314b7)

 | 

Simple form data field file value.

 |
| 

} **data**

 | 

The **type** variable defines the data type used in **data**.

 |
| 

struct [Rcp\_MultipartFormFieldValue](#) \* [next](#abb8d932651a02819e0a94d6af317f845)

 | 

Pointer to the next [Rcp\_MultipartFormFieldValue](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]formFileValue

[Rcp\_FormFieldFileValue](../rcp-formfieldfilevalue/document.md) Rcp\_MultipartFormFieldValue::formFileValue

**Description**

Simple form data field file value.

#### \[h2\]formValue

[Rcp\_FormFieldValue](../rcp-formfieldvalue/document.md) Rcp\_MultipartFormFieldValue::formValue

**Description**

Simple form data field value.

#### \[h2\]next

struct [Rcp\_MultipartFormFieldValue](#)\* Rcp\_MultipartFormFieldValue::next

**Description**

Pointer to the next [Rcp\_MultipartFormFieldValue](#) in the data chain.

#### \[h2\]type

[Rcp\_MultipartValueType](../../../modules/remotecommunication/document.md#ga76d003b4f9a244c9d11def4128ceeda8) Rcp\_MultipartFormFieldValue::type

**Description**

Data type used in the union structure.
