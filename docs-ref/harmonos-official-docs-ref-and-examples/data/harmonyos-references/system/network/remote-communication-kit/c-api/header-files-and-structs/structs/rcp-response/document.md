# Rcp\_Response

#### Overview

Response to a network request.

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

const [Rcp\_Request](../rcp-request/document.md) \* [request](#ac840978bf352227f8dc889dd74b9ba18)

 | 

Request that triggers the creation of a response.

 |
| 

char \* [effectiveUrl](#a70b36ed43793ef7b2316e6651e70bb02)

 | 

Valid URL used last time.

 |
| 

[Rcp\_StatusCode](../../../modules/remotecommunication/document.md#ga97929a5349f04300f50318f50393b93e) [statusCode](#a49900c34bb1ce245916a9afa53d1cf29)

 | 

Response status code.

 |
| 

[Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \* [headers](#a270f2855aa008069d5ae45284f00a7eb)

 | 

Response header.

 |
| 

[Rcp\_Buffer](../rcp-buffer/document.md) [body](#a2ef03d4c3fbd3eb2b39063cdad784c9f)

 | 

Response body.

 |
| 

[Rcp\_DebugInfo](../rcp-debuginfo/document.md) \* [debugInfo](#ab42553d48543d390dc3e168daa6679fc)

 | 

Debugging information about request/response processing.

 |
| 

[Rcp\_TimeInfo](../rcp-timeinfo/document.md) \* [timeInfo](#a57d437be63e686ada47b96b3126067d8)

 | 

Response time information.

 |
| 

[Rcp\_ResponseCookies](../rcp-responsecookies/document.md) \* [cookies](#a8faaf3b941ee3ea71ea9a5f29f0cba0d)

 | 

Response cookies.

 |
| 

const [Rcp\_ResponseCallbackObject](../rcp-responsecallbackobject/document.md) \* [responseCallback](#a3280f7e39349795a5545663ce573798f)

 | 

Response callback.

 |
| 

void(\* [destroyResponse](#a1fed4fc16ee61a226a4a3cc52d9775bb) )(struct [Rcp\_Response](#) \*response)

 | 

Method used to destroy a response.

 |
| 

void \* [responsePrivate](#a0fc41a839e5d0646410fc11d46f7fd40)

 | 

Extended fields.

 |

#### Member Variable Description

#### \[h2\]body

[Rcp\_Buffer](../rcp-buffer/document.md) Rcp\_Response::body

**Description**

Response body.

#### \[h2\]cookies

[Rcp\_ResponseCookies](../rcp-responsecookies/document.md)\* Rcp\_Response::cookies

**Description**

Response cookies.

#### \[h2\]debugInfo

[Rcp\_DebugInfo](../rcp-debuginfo/document.md)\* Rcp\_Response::debugInfo

**Description**

Debugging information about request/response processing.

Whether to collect the information is subject to [Rcp\_TracingConfiguration](../rcp-tracingconfiguration/document.md).

#### \[h2\]destroyResponse

void(\* Rcp\_Response::destroyResponse) (struct [Rcp\_Response](#) \*response)

**Description**

Method used to destroy a response.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

response

 | 

Pointer to the [Rcp\_Response](#) to be destroyed.

 |

#### \[h2\]effectiveUrl

char\* Rcp\_Response::effectiveUrl

**Description**

Valid URL used last time.

If redirection is performed or [Rcp\_SessionConfiguration.baseUrl](../rcp-sessionconfiguration/document.md#a8cb997b4f5fdcdf28aad95f975ed2a0c) is set, the URL may be different from [Rcp\_Request.url](../rcp-request/document.md#a39a1cc0a1ad666d8d9ad40eec4b52de7).

#### \[h2\]headers

[Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982)\* Rcp\_Response::headers

**Description**

Response header.

#### \[h2\]request

const [Rcp\_Request](../rcp-request/document.md)\* Rcp\_Response::request

**Description**

Request that triggers the creation of a response.

#### \[h2\]responseCallback

const [Rcp\_ResponseCallbackObject](../rcp-responsecallbackobject/document.md)\* Rcp\_Response::responseCallback

**Description**

Response callback.

#### \[h2\]responsePrivate

void\* Rcp\_Response::responsePrivate

**Description**

Extended fields.

#### \[h2\]statusCode

[Rcp\_StatusCode](../../../modules/remotecommunication/document.md#ga97929a5349f04300f50318f50393b93e) Rcp\_Response::statusCode

**Description**

Response status code.

#### \[h2\]timeInfo

[Rcp\_TimeInfo](../rcp-timeinfo/document.md)\* Rcp\_Response::timeInfo

**Description**

Response time information.

Whether to collect the information is subject to the configuration in [Rcp\_TracingConfiguration.collectTimeInfo](../rcp-tracingconfiguration/document.md#aded07a3d27e7524e18362082264b9b94).
