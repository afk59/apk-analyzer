# Rcp\_TracingConfiguration

#### Overview

Request tracing configuration.

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

bool [verbose](#aa239b1c1f3cf8618d07c2a8582224fc8)

 | 

Indicates whether to record detailed logs for an ongoing request. The default value is **false**. If the corresponding option is enabled in **infoToCollect**, collection is performed automatically.

 |
| 

[Rcp\_InfoToCollect](../rcp-infotocollect/document.md) [infoToCollect](#a5495e16d1ce7b0d75c25150c0ac0f711)

 | 

Request processing events to be collected. You can check the response object for collected events.

 |
| 

bool [collectTimeInfo](#aded07a3d27e7524e18362082264b9b94)

 | 

Indicates whether to collect request timer information. The default value is **false**.

 |
| 

[Rcp\_EventsHandler](../rcp-eventshandler/document.md) [httpEventsHandler](#ac7621467d197c2df3c4da27f69e8a2fd)

 | 

Callback function for listening on various HTTP events.

 |

#### Member Variable Description

#### \[h2\]collectTimeInfo

bool Rcp\_TracingConfiguration::collectTimeInfo

**Description**

Indicates whether to collect request timer information. The default value is **false**.

#### \[h2\]httpEventsHandler

[Rcp\_EventsHandler](../rcp-eventshandler/document.md) Rcp\_TracingConfiguration::httpEventsHandler

**Description**

Callback function for listening on various HTTP events.

#### \[h2\]infoToCollect

[Rcp\_InfoToCollect](../rcp-infotocollect/document.md) Rcp\_TracingConfiguration::infoToCollect

**Description**

Request processing events to be collected. You can check the response object for collected events.

#### \[h2\]verbose

bool Rcp\_TracingConfiguration::verbose

**Description**

Indicates whether to record detailed logs for an ongoing request. The default value is **false**. If the corresponding option is enabled in **infoToCollect**, collection is performed automatically.
