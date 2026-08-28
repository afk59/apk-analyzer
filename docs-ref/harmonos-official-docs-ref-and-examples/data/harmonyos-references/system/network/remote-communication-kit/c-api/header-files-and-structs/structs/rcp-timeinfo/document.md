# Rcp\_TimeInfo

#### Overview

Response timer information.

It will be collected in [Rcp\_Response.timeInfo](../rcp-response/document.md#a57d437be63e686ada47b96b3126067d8). [Rcp\_TracingConfiguration.collectTimeInfo](../rcp-tracingconfiguration/document.md#aded07a3d27e7524e18362082264b9b94) specifies whether to collect the information.

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

double [totalTime](#a61266aa883f6f7715bc5380c43c6ab28)

 | 

Total time used for HTTP transmission in milliseconds (including host name lookup and TCP connection).

 |
| 

double [nameLookUpTime](#a61499e9621bab228bb6860af13090b68)

 | 

Time elapsed till host name lookup, in milliseconds.

 |
| 

double [connectTime](#a00f71c3e61958a61c5a95763460d53e9)

 | 

Time elapsed till connection to the remote host or proxy server, in milliseconds.

 |
| 

double [preTransferTime](#ae1e72d2680d8edd395b1a80de8d24a39)

 | 

Time elapsed till the begging of data transfer, in milliseconds.

 |
| 

double [fileTime](#aa2ace0fbac885a58100761269720d213)

 | 

Time elapsed since the last time a remote file was modified, in milliseconds.

 |
| 

double [startTransferTime](#ad2373fa86954f501efb5492858ca17f7)

 | 

Time elapsed till the first byte is received, in milliseconds.

 |
| 

double [redirectTime](#a6050b0abb52990b0a0d01b49335a0d53)

 | 

Time spent on all redirection steps (including host name lookup and connection), in milliseconds.

 |
| 

double [tlsHandshakeTime](#ad4ecb9c4812a3f06edad569022a06ec1)

 | 

Time elapsed till the TLS handshake with the remote host or proxy server, in milliseconds.

 |

#### Member Variable Description

#### \[h2\]connectTime

double Rcp\_TimeInfo::connectTime

**Description**

Time elapsed till connection to the remote host or proxy server, in milliseconds.

#### \[h2\]fileTime

double Rcp\_TimeInfo::fileTime

**Description**

Time elapsed since the last time a remote file was modified, in milliseconds.

#### \[h2\]nameLookUpTime

double Rcp\_TimeInfo::nameLookUpTime

**Description**

Time elapsed till host name lookup, in milliseconds.

#### \[h2\]preTransferTime

double Rcp\_TimeInfo::preTransferTime

**Description**

Time elapsed till the begging of data transfer, in milliseconds.

#### \[h2\]redirectTime

double Rcp\_TimeInfo::redirectTime

**Description**

Time spent on all redirection steps (including host name lookup and connection), in milliseconds.

#### \[h2\]startTransferTime

double Rcp\_TimeInfo::startTransferTime

**Description**

Time elapsed till the first byte is received, in milliseconds.

#### \[h2\]tlsHandshakeTime

double Rcp\_TimeInfo::tlsHandshakeTime

**Description**

Time elapsed till the TLS handshake with the remote host or proxy server, in milliseconds.

#### \[h2\]totalTime

double Rcp\_TimeInfo::totalTime

**Description**

Total time used for HTTP transmission in milliseconds (including host name lookup and TCP connection).
