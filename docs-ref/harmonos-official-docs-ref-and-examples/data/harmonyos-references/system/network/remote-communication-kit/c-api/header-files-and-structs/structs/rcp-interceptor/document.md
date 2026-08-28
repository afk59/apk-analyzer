# Rcp\_Interceptor

#### Overview

Asynchronous interceptor.

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

uint32\_t(\* [intercept](#a479e39838d2b1c2792ee0152d2735cf6) )([Rcp\_Request](../rcp-request/document.md) \*request, const [Rcp\_RequestHandler](../../../modules/remotecommunication/document.md#ga5ac080855c3aaef66c58d5b5b371be2b) \*next, const [Rcp\_ResponseCallbackObject](../rcp-responsecallbackobject/document.md) \*responseCallback)

 | 

Pointer to the asynchronous interceptor function. To use an interceptor, you need to implement this function.

 |

#### Member Variable Description

#### \[h2\]intercept

uint32\_t(\* Rcp\_Interceptor::intercept) ([Rcp\_Request](../rcp-request/document.md) \*request, const [Rcp\_RequestHandler](../../../modules/remotecommunication/document.md#ga5ac080855c3aaef66c58d5b5b371be2b) \*next, const [Rcp\_ResponseCallbackObject](../rcp-responsecallbackobject/document.md) \*responseCallback)

**Description**

Pointer to the asynchronous interceptor function. To use an interceptor, you need to implement this function.

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

Pointer to the next asynchronous handler [Rcp\_RequestHandler](../../../modules/remotecommunication/document.md#ga5ac080855c3aaef66c58d5b5b371be2b).

 |
| 

responseCallback

 | 

Pointer to [Rcp\_ResponseCallbackObject](../rcp-responsecallbackobject/document.md).

 |

**Returns**:

Return value of the interceptor, of the uint32\_t type.
