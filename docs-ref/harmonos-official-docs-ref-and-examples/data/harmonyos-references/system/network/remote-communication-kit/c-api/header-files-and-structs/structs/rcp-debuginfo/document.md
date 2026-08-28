# Rcp\_DebugInfo

#### Overview

Structure of the debugging information stored in [Rcp\_Response](../rcp-response/document.md).

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

[Rcp\_DebugEvent](../../../modules/remotecommunication/document.md#gadff9eaa1b517bf01defd1273b2eeddbc) [type](#ab4ef1c46103e7faf4c65c188300c5c91)

 | 

Debugging event type.

 |
| 

[Rcp\_Buffer](../rcp-buffer/document.md) [data](#aece86864dfc23ae47580444af9fcdb3c)

 | 

Debugging information.

 |
| 

struct [Rcp\_DebugInfo](#) \* [next](#ab51a791fac9a703013aa3b931dacdcdb)

 | 

Pointer to the next [Rcp\_DebugInfo](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]data

[Rcp\_Buffer](../rcp-buffer/document.md) Rcp\_DebugInfo::data

**Description**

Debugging information.

#### \[h2\]next

struct [Rcp\_DebugInfo](#)\* Rcp\_DebugInfo::next

**Description**

Pointer to the next [Rcp\_DebugInfo](#) in the data chain.

#### \[h2\]type

[Rcp\_DebugEvent](../../../modules/remotecommunication/document.md#gadff9eaa1b517bf01defd1273b2eeddbc) Rcp\_DebugInfo::type

**Description**

Debugging event type.
