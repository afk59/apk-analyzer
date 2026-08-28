# Rcp\_TransferRange

#### Overview

HTTP transmission range. This configuration will be converted into the HTTP Range header. An HTTP request with such a header requires the server to return only a part of the HTTP response.

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

int64\_t [from](#af569131d87ba26f923c8238301005f41)

 | 

Transfer start point.

 |
| 

bool [hasZeroFrom](#a49db62d8a3538c872e7d7d73e7c05650)

 | 

Indicates whether to start from zero.

 |
| 

int64\_t [to](#a55a005ae0190dd50949f9d313fb04582)

 | 

Transfer end point.

 |
| 

bool [hasZeroTo](#a47278ecdc6e3e7248f928aab592ad83b)

 | 

Indicates whether to end with zero.

 |
| 

struct [Rcp\_TransferRange](#) \* [next](#ac3942a3eb8fdcfe06fca9d0fd6ae141e)

 | 

Pointer to the next [Rcp\_TransferRange](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]from

int64\_t Rcp\_TransferRange::from

**Description**

Transfer start point.

#### \[h2\]hasZeroFrom

bool Rcp\_TransferRange::hasZeroFrom

**Description**

Indicates whether the range starts from zero.

#### \[h2\]hasZeroTo

bool Rcp\_TransferRange::hasZeroTo

**Description**

Indicates whether to end with zero.

#### \[h2\]next

struct [Rcp\_TransferRange](#)\* Rcp\_TransferRange::next

**Description**

Pointer to the next [Rcp\_TransferRange](#) in the data chain.

#### \[h2\]to

int64\_t Rcp\_TransferRange::to

**Description**

Transfer end point.
