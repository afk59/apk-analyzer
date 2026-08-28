# Rcp\_TransferConfiguration

#### Overview

Transmission configuration.

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

bool [autoRedirect](#a80c7d591979b9538f847a9d4bd2109a1)

 | 

Indicates whether to automatically follow HTTP redirect responses. The default value is **True**.

 |
| 

[Rcp\_Timeout](../rcp-timeout/document.md) [timeout](#a9ffa3456e4f7e056eb93887091b7fb04)

 | 

Timeout settings. If this variable is not set, the default timeout setting is applied.

 |
| 

bool [assumesHTTP3Capable](#ae5f8dd2f74c11b558e0aa6761feefbed)

 | 

Indicates whether the target server is assumed to support HTTP/3. The default value is **false**.

 |
| 

[Rcp\_PathPreference](../../../modules/remotecommunication/document.md#ga9498d24addbd529f258fd6faacfd9c67) [pathPreference](#a169a9f44d629000efe1e54ea953efcf1)

 | 

Request path preferences.

 |

#### Member Variable Description

#### \[h2\]assumesHTTP3Capable

bool Rcp\_TransferConfiguration::assumesHTTP3Capable

**Description**

Indicates whether the target server is assumed to support HTTP/3. The default value is **false**.

#### \[h2\]autoRedirect

bool Rcp\_TransferConfiguration::autoRedirect

**Description**

Indicates whether to automatically follow HTTP redirect responses. The default value is **True**.

#### \[h2\]pathPreference

[Rcp\_PathPreference](../../../modules/remotecommunication/document.md#ga9498d24addbd529f258fd6faacfd9c67) Rcp\_TransferConfiguration::pathPreference

**Description**

Request path preferences.

#### \[h2\]timeout

[Rcp\_Timeout](../rcp-timeout/document.md) Rcp\_TransferConfiguration::timeout

**Description**

Timeout settings. If this variable is not set, the default timeout setting is applied. Otherwise, the specified timeout setting is used.
