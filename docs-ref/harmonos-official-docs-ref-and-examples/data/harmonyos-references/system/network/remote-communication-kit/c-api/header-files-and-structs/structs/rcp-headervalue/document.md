# Rcp\_HeaderValue

#### Overview

Value type of a mapped value in a request or response header.

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

char \* [value](#a2808b89bd4ee544a9167315c782d5dc0)

 | 

Value of a key-value pair in the header.

 |
| 

struct [Rcp\_HeaderValue](#) \* [next](#a6f80339bd4632840890dbed4516a2c7c)

 | 

Pointer to the next [Rcp\_HeaderValue](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]next

struct [Rcp\_HeaderValue](#)\* Rcp\_HeaderValue::next

**Description**

Pointer to the next [Rcp\_HeaderValue](#) in the data chain.

#### \[h2\]value

char\* Rcp\_HeaderValue::value

**Description**

Value.
