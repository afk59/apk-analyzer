# Rcp\_SessionListener

#### Overview

Callback function for listening on session closing or cancellation events.

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

void(\* [onClosed](#a5ca868b964814af3121f2f6fd4b71706) )(void)

 | 

Function called when [Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) closes.

 |
| 

void(\* [onCanceled](#a3e9cf1cb6445a5b06c96ffefb547d129) )(void)

 | 

Function called when [Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) is canceled.

 |

#### Member Variable Description

#### \[h2\]onCanceled

void(\* Rcp\_SessionListener::onCanceled) (void)

**Description**

Function called when [Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) is canceled.

#### \[h2\]onClosed

void(\* Rcp\_SessionListener::onClosed) (void)

**Description**

Function called when [Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) closes.
