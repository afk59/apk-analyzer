# Rcp\_OnProgressCallback

#### Overview

Callback triggered upon data transmission events, which is configured in [Rcp\_EventsHandler](../rcp-eventshandler/document.md).

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

[Rcp\_OnProgressCallbackFunc](../../../modules/remotecommunication/document.md#gaaf74ce6d5578d28829955208318d3fbe) [callback](#a899177e3d91f73c817ccdb2edafbcd8f)

 | 

Callback function triggered during data transmission.

 |
| 

void \* [usrObject](#a4ad524ee058227acd02fdc1beebde386)

 | 

Custom object, which is used in the callback function.

 |

#### Member Variable Description

#### \[h2\]callback

[Rcp\_OnProgressCallbackFunc](../../../modules/remotecommunication/document.md#gaaf74ce6d5578d28829955208318d3fbe) Rcp\_OnProgressCallback::callback

**Description**

Callback function triggered during data transmission.

#### \[h2\]usrObject

void\* Rcp\_OnProgressCallback::usrObject

**Description**

Custom object, which is used in the callback function.
