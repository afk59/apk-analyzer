# Rcp\_OnVoidCallback

#### Overview

Callback triggered upon transmigration ending or cancellation events, which is configured in [Rcp\_EventsHandler](../rcp-eventshandler/document.md).

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

[Rcp\_OnVoidCallbackFunc](../../../modules/remotecommunication/document.md#ga3d6a448e8f0bdcc2b4e70fa6ca00d475) [callback](#a64fba630d3ca20f3baa3f2184cd4fd99)

 | 

DataEnd or Canceled event callback function.

 |
| 

void \* [usrObject](#ab1d887e227a21e05fb80c407396c3147)

 | 

Custom object, which is used in the callback function.

 |

#### Member Variable Description

#### \[h2\]callback

[Rcp\_OnVoidCallbackFunc](../../../modules/remotecommunication/document.md#ga3d6a448e8f0bdcc2b4e70fa6ca00d475) Rcp\_OnVoidCallback::callback

**Description**

DataEnd or Canceled event callback function.

#### \[h2\]usrObject

void\* Rcp\_OnVoidCallback::usrObject

**Description**

Custom object, which is used in the callback function.
