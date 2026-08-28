# Rcp\_SyncInterceptor

#### Overview

Synchronous interceptor.

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

[Rcp\_Response](../rcp-response/document.md) \*(\* [intercept](#a4422febd3ef69e443ab4514d4c579aa8) )([Rcp\_Request](../rcp-request/document.md) \*request, const [Rcp\_SyncRequestHandler](../../../modules/remotecommunication/document.md#ga2067d1b09b33afa0b8237a049687e9ea) \*next, uint32\_t \*errCode)

 | 

Pointer to the synchronous interceptor function. To use an interceptor, you need to implement this function.

 |

#### Member Variable Description

#### \[h2\]intercept

[Rcp\_Response](../rcp-response/document.md)\*(\* Rcp\_SyncInterceptor::intercept) ([Rcp\_Request](../rcp-request/document.md) \*request, const [Rcp\_SyncRequestHandler](../../../modules/remotecommunication/document.md#ga2067d1b09b33afa0b8237a049687e9ea) \*next, uint32\_t \*errCode)

**Description**

Pointer to the synchronous interceptor function. To use an interceptor, you need to implement this function.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

request

 | 

Pointer to [Rcp\_Request](../rcp-request/document.md).

 |
| 

next

 | 

Pointer to the next synchronous handler [Rcp\_SyncRequestHandler](../../../modules/remotecommunication/document.md#ga2067d1b09b33afa0b8237a049687e9ea).

 |
| 

errCode

 | 

Return value of the interceptor.

 |

**Returns**:

**Rcp\_Response\***: pointer to the response.
