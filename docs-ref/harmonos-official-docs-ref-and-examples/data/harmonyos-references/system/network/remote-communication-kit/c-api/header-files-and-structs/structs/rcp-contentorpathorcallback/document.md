# Rcp\_ContentOrPathOrCallback

#### Overview

Simple form data field value used in [Rcp\_FormFieldFileValue](../rcp-formfieldfilevalue/document.md).

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

[Rcp\_ContentOrPathOrCallbackType](../../../modules/remotecommunication/document.md#gaa5a592f4e68a1dd43f5f41e95199a5e4) [type](#ab083ea1a78b6bb4d37728fdb63258ac9)

 | 

Data type used in the union structure.

 |
| 

union {

 | 

Union structure. The **type** variable defines the data type used in **data**.

 |
| 

[Rcp\_Buffer](../rcp-buffer/document.md) [content](#a9a98334505537018eec3356254ef6340)

 | 

**content**: text data.

 |
| 

char [path](#a3c4cb1ec63c7e30ef25f3e8c04007639) \[[RCP\_MAX\_PATH\_LEN](../../../modules/remotecommunication/document.md#ga3dac667ae8b6fa64f2fede1e77804e12)\]

 | 

**path**: file path.

 |
| 

[Rcp\_GetDataCallback](../../../modules/remotecommunication/document.md#gac0ac73f33252239ff47a648fe3aa6bd5) [callback](#a307b3cb12a976b3e3555b20dc0f5d0bd)

 | 

**callback**: callback function used to obtain data.

 |
| 

} **data**

 | 

The **type** variable defines the data type used in **data**.

 |

#### Member Variable Description

#### \[h2\]callback

[Rcp\_GetDataCallback](../../../modules/remotecommunication/document.md#gac0ac73f33252239ff47a648fe3aa6bd5) Rcp\_ContentOrPathOrCallback::callback

**Description**

Callback function used to obtain data.

#### \[h2\]content

[Rcp\_Buffer](../rcp-buffer/document.md) Rcp\_ContentOrPathOrCallback::content

**Description**

Text data.

#### \[h2\]path

char Rcp\_ContentOrPathOrCallback::path\[[RCP\_MAX\_PATH\_LEN](../../../modules/remotecommunication/document.md#ga3dac667ae8b6fa64f2fede1e77804e12)\]

**Description**

File path.

#### \[h2\]type

[Rcp\_ContentOrPathOrCallbackType](../../../modules/remotecommunication/document.md#gaa5a592f4e68a1dd43f5f41e95199a5e4) Rcp\_ContentOrPathOrCallback::type

**Description**

Data type used in the union structure.
