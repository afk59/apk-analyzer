# Rcp\_HeaderEntry

#### Overview

All key-value pairs in the request or response header.

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

char \* [key](#a5fe5651c6fb34ca1c58f9ef27f8b3236)

 | 

Key. If you want to support all predefined options of **content-type** in your **content-type** customization, ensure that the key contains **content-type** in lowercase.

 |
| 

[Rcp\_HeaderValue](../rcp-headervalue/document.md) \* [value](#a3535a6d660132530e59c62d651648455)

 | 

Value.

 |
| 

struct [Rcp\_HeaderEntry](#) \* [next](#a9f821c0572ebb0e1ad391a13b6db3d4c)

 | 

Pointer to the next [Rcp\_HeaderEntry](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]key

char\* Rcp\_HeaderEntry::key

**Description**

Key of a key-value pair in the header. If you want to support all predefined options of **content-type** in your **content-type** customization, ensure that the key contains **content-type** in lowercase.

#### \[h2\]next

struct [Rcp\_HeaderEntry](#)\* Rcp\_HeaderEntry::next

**Description**

Pointer to the next [Rcp\_HeaderEntry](#) in the data chain.

#### \[h2\]value

[Rcp\_HeaderValue](../rcp-headervalue/document.md)\* Rcp\_HeaderEntry::value

**Description**

Value of a key-value pair in the header.
