# Rcp\_Urls

#### Overview

URLs, which are used to determine whether a host is using a proxy.

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

const char \* [url](#affd57b9b241b419c449bd85b6e881be2)

 | 

Matched URL.

 |
| 

struct [Rcp\_Urls](#) \* [next](#ab15dafafb47202da262f9bbb2f1c23bd)

 | 

Pointer to the next [Rcp\_Urls](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]next

struct [Rcp\_Urls](#)\* Rcp\_Urls::next

**Description**

Pointer to the next [Rcp\_Urls](#) in the data chain.

#### \[h2\]url

const char\* Rcp\_Urls::url

**Description**

Matched URL.
