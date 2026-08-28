# Rcp\_ResponseCookies

#### Overview

Response cookies.

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

char \* [name](#a4fb5e327e05b807620387ee2500d314d)

 | 

Response cookie name.

 |
| 

char \* [value](#a7fb6c2177d99ffae4f13f411352196b2)

 | 

Response cookie value.

 |
| 

char \* [domain](#a6f836af033fc293b012d49070c15dbd0)

 | 

Response cookie domain attribute.

 |
| 

char \* [path](#a56c12937ae44e3ecb7d6c85e2d2ded03)

 | 

Response cookie path attribute.

 |
| 

char \* [expires](#ac6870a218b3c8cf7f70d4666e1a9f9ad)

 | 

Response cookie expiration attribute.

 |
| 

uint64\_t [maxAge](#aa3607ffbf45b1d9fb297d826df3b250a)

 | 

Response cookie maxAge attribute.

 |
| 

bool [secure](#a81a2dd49c05c77313928d7843c49950b)

 | 

Response cookie security attribute.

 |
| 

bool [httpOnly](#a9b26fb82d3e441c63128bf1e88c6ce5c)

 | 

Response cookie httpOnly attribute.

 |
| 

char \* [sameSite](#ad4cb031c71dacc43b4deafbbe2c8e5ae)

 | 

Response cookie sameSite attribute.

 |
| 

uint64\_t [rawSize](#a395f93dbd2c0f272495ebcc2fb8aeae5)

 | 

Original size of the response cookies.

 |
| 

char \* [originString](#a29a4b1bfb8eefa5accf5b2844524a80b)

 | 

Original character string.

 |
| 

[Rcp\_CookieAttributes](../../../modules/remotecommunication/document.md#ga08c7b992199bec7e5acdc50ce8ae2651) \* [cookieAttributes](#a355c49aca4e4fe1bc799e83e115c60bf)

 | 

All attributes in the response cookies.

 |
| 

struct [Rcp\_ResponseCookies](#) \* [next](#aed191dfba2a7e291b08df92f48be033f)

 | 

Pointer to the next [Rcp\_ResponseCookies](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]cookieAttributes

[Rcp\_CookieAttributes](../../../modules/remotecommunication/document.md#ga08c7b992199bec7e5acdc50ce8ae2651)\* Rcp\_ResponseCookies::cookieAttributes

**Description**

All attributes in the response cookies.

#### \[h2\]domain

char\* Rcp\_ResponseCookies::domain

**Description**

Response cookie domain attribute.

#### \[h2\]expires

char\* Rcp\_ResponseCookies::expires

**Description**

Response cookie expiration attribute.

#### \[h2\]httpOnly

bool Rcp\_ResponseCookies::httpOnly

**Description**

Response cookie httpOnly attribute.

#### \[h2\]maxAge

uint64\_t Rcp\_ResponseCookies::maxAge

**Description**

Response cookie maxAge attribute.

#### \[h2\]name

char\* Rcp\_ResponseCookies::name

**Description**

Response cookie name.

#### \[h2\]next

struct [Rcp\_ResponseCookies](#)\* Rcp\_ResponseCookies::next

**Description**

Pointer to the next [Rcp\_ResponseCookies](#) in the data chain.

#### \[h2\]originString

char\* Rcp\_ResponseCookies::originString

**Description**

Original character string.

#### \[h2\]path

char\* Rcp\_ResponseCookies::path

**Description**

Response cookie path attribute.

#### \[h2\]rawSize

uint64\_t Rcp\_ResponseCookies::rawSize

**Description**

Original size of the response cookies.

#### \[h2\]sameSite

char\* Rcp\_ResponseCookies::sameSite

**Description**

Response cookie sameSite attribute.

#### \[h2\]secure

bool Rcp\_ResponseCookies::secure

**Description**

Response cookie security attribute.

#### \[h2\]value

char\* Rcp\_ResponseCookies::value

**Description**

Response cookie value.
