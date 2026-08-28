# Rcp\_RequestContent

#### Overview

Request content.

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

[Rcp\_ContentType](../../../modules/remotecommunication/document.md#ga05daeab5ad8d265834b4a1b4e61cd8fa) [type](#a46cdb54d4c402f9eca88b46c3746f913)

 | 

Data type used in the union structure.

 |
| 

union {

 | 

Union structure. The **type** variable defines the data type used in **data**.

 |
| 

[Rcp\_Buffer](../rcp-buffer/document.md) [contentStr](#a81dfde6bdcabe53dd1ca25f85173d19a)

 | 

**contentStr**: text.

 |
| 

[Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) \* [form](#a385cd35b8a47800f13a6ef5520842c58)

 | 

**form**: form data.

 |
| 

[Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9) \* [multipartForm](#afb9b3ece4b637e347bafc3d98899ae45)

 | 

**multipartForm**: multi-part form data.

 |
| 

[Rcp\_GetDataCallback](../../../modules/remotecommunication/document.md#gac0ac73f33252239ff47a648fe3aa6bd5) [getDataCallback](#a042146cb217fe387a22d8538de6b147c)

 | 

**getDataCallback**: data obtained through a callback function.

 |
| 

} **data**

 | 

The **type** variable defines the data type used in **data**.

 |

#### Member Variable Description

#### \[h2\]contentStr

[Rcp\_Buffer](../rcp-buffer/document.md) Rcp\_RequestContent::contentStr

**Description**

String content.

#### \[h2\]form

[Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be)\* Rcp\_RequestContent::form

**Description**

Form content.

#### \[h2\]getDataCallback

[Rcp\_GetDataCallback](../../../modules/remotecommunication/document.md#gac0ac73f33252239ff47a648fe3aa6bd5) Rcp\_RequestContent::getDataCallback

**Description**

Callback function.

#### \[h2\]multipartForm

[Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9)\* Rcp\_RequestContent::multipartForm

**Description**

Multi-part form content.

#### \[h2\]type

[Rcp\_ContentType](../../../modules/remotecommunication/document.md#ga05daeab5ad8d265834b4a1b4e61cd8fa) Rcp\_RequestContent::type

**Description**

Data type used in the union structure.
