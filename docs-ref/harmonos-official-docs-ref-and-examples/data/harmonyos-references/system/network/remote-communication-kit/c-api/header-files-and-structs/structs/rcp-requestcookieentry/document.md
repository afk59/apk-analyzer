# Rcp\_RequestCookieEntry

#### Overview

All cookie key-value pairs in the request.

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

char \* [key](#a3412ddb3fe8dd53fdfd78cdc64606dde)

 | 

Key in a cookie key-value pair.

 |
| 

char \* [value](#a9107385a3fbbfc9f224e41b62b6840a2)

 | 

Value in a cookie key-value pair.

 |
| 

struct [Rcp\_RequestCookieEntry](#) \* [next](#a0ad803719fa8dabb2e92099b956188c6)

 | 

Pointer to the next [Rcp\_RequestCookieEntry](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]key

char\* Rcp\_RequestCookieEntry::key

**Description**

Key in a cookie key-value pair.

#### \[h2\]next

struct [Rcp\_RequestCookieEntry](#)\* Rcp\_RequestCookieEntry::next

**Description**

Pointer to the next [Rcp\_RequestCookieEntry](#) in the data chain.

#### \[h2\]value

char\* Rcp\_RequestCookieEntry::value

**Description**

Value in a cookie key-value pair.
