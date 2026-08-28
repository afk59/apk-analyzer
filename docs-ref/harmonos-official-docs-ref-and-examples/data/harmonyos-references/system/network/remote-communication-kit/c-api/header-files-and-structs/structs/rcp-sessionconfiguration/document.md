# Rcp\_SessionConfiguration

#### Overview

Session configuration.

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

[Rcp\_SessionType](../../../modules/remotecommunication/document.md#ga4fa3aa6821b16425c260d837deace956) [type](#aa8a73daba70f67827cac073d5d159de2)

 | 

Session type.

 |
| 

[Rcp\_InterceptorArray](../rcp-interceptorarray/document.md) [interceptors](#a1f3ed29c8781479e514020921933fa77)

 | 

Custom asynchronous interceptor array.

 |
| 

[Rcp\_SyncInterceptorArray](../rcp-syncinterceptorarray/document.md) [syncInterceptors](#a2ae808955d10d5fdf3bf91950ff8a2c9)

 | 

Custom synchronous interceptor array.

 |
| 

const char \* [baseUrl](#a8cb997b4f5fdcdf28aad95f975ed2a0c)

 | 

Base URL.

 |
| 

[Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \* [headers](#a83eabab4e8f469be1d4fe9afa5a885e8)

 | 

Request header.

 |
| 

[Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50) \* [cookies](#a16b3f819c4b51898edb1da8cf6341752)

 | 

Request cookies.

 |
| 

[Rcp\_SessionListener](../rcp-sessionlistener/document.md) [sessionListener](#a76757231607687f3c609d4563dfdd401)

 | 

Callback function for listening on **close()** and **cancel()** events of sessions.

 |
| 

[Rcp\_Configuration](../rcp-configuration/document.md) \* [requestConfiguration](#acdfb8368e9de0b0383286a082f90d973)

 | 

Default request configuration. The configurations can be overridden with **[Request.configuration](../rcp-request/document.md#ac932aa050c8e51b76783f27a07273b05)**.

 |
| 

[Rcp\_ConnectionConfiguration](../rcp-connectionconfiguration/document.md) [connectionConfiguration](#a5867f7ed6493d37300c5146bf07b8e4a)

 | 

Connection configuration.

 |

#### Member Variable Description

#### \[h2\]baseUrl

const char\* Rcp\_SessionConfiguration::baseUrl

**Description**

Base URL.

For example, if the requested URL is **? Name=value** and the base URL is https://example.com, the final URL would be https://example.com?name=value.

#### \[h2\]connectionConfiguration

[Rcp\_ConnectionConfiguration](../rcp-connectionconfiguration/document.md) Rcp\_SessionConfiguration::connectionConfiguration

**Description**

Connection configuration.

This variable specifies the maximum number of concurrent connections allowed in the session and the maximum number of concurrent connections to a single host.

#### \[h2\]cookies

[Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50)\* Rcp\_SessionConfiguration::cookies

**Description**

Request cookies.

If [HMS\_Rcp\_Fetch](../../../modules/remotecommunication/document.md#ga7ea546b69b9ea60ea4716ee64e8b04cb) or [HMS\_Rcp\_FetchSync](../../../modules/remotecommunication/document.md#ga48a83535a4658e9872ded4b0dd8c812f) is called and [Rcp\_Request](../rcp-request/document.md) does not contain [Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50), [Rcp\_SessionConfiguration.cookies](#a16b3f819c4b51898edb1da8cf6341752) will be used. If both [Rcp\_Request.cookies](../rcp-request/document.md#a4233d0d064ac2209accfb25a701047c9) and [Rcp\_SessionConfiguration.cookies](#a16b3f819c4b51898edb1da8cf6341752) exist, they will be merged.

#### \[h2\]headers

[Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982)\* Rcp\_SessionConfiguration::headers

**Description**

Request header.

If [HMS\_Rcp\_Fetch](../../../modules/remotecommunication/document.md#ga7ea546b69b9ea60ea4716ee64e8b04cb) or [HMS\_Rcp\_FetchSync](../../../modules/remotecommunication/document.md#ga48a83535a4658e9872ded4b0dd8c812f) is called and [Rcp\_Request](../rcp-request/document.md) does not contain [Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982), [Rcp\_SessionConfiguration.headers](#a83eabab4e8f469be1d4fe9afa5a885e8) will be used. If both [Rcp\_SessionConfiguration.headers](#a83eabab4e8f469be1d4fe9afa5a885e8) and [Rcp\_Request.headers](../rcp-request/document.md#a4ebc6011dc454a18c04eca049f8e95cd) exist, they will be merged.

#### \[h2\]interceptors

[Rcp\_InterceptorArray](../rcp-interceptorarray/document.md) Rcp\_SessionConfiguration::interceptors

**Description**

Custom asynchronous interceptor array.

Asynchronous interceptors will be converted into an interceptor chain.

If the input is \[A, B, C, D\], the processing logic will be A -> B -> C -> D -> defaultHandler.

#### \[h2\]requestConfiguration

[Rcp\_Configuration](../rcp-configuration/document.md)\* Rcp\_SessionConfiguration::requestConfiguration

**Description**

Default request configuration. The configurations can be overridden with **Request.configuration**.

#### \[h2\]sessionListener

[Rcp\_SessionListener](../rcp-sessionlistener/document.md) Rcp\_SessionConfiguration::sessionListener

**Description**

Callback function for listening on **close()** and **cancel()** events of sessions.

#### \[h2\]syncInterceptors

[Rcp\_SyncInterceptorArray](../rcp-syncinterceptorarray/document.md) Rcp\_SessionConfiguration::syncInterceptors

**Description**

Custom synchronous interceptor array.

Synchronous interceptors will be converted into an interceptor chain.

If the input is \[A, B, C, D\], the processing logic will be A -> B -> C -> D -> defaultHandler.

#### \[h2\]type

[Rcp\_SessionType](../../../modules/remotecommunication/document.md#ga4fa3aa6821b16425c260d837deace956) Rcp\_SessionConfiguration::type

**Description**

Session type.
