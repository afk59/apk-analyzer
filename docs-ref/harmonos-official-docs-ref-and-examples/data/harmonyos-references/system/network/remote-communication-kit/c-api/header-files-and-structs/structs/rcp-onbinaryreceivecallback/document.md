# Rcp\_OnBinaryReceiveCallback

#### Overview

Callback function for receiving binary data in a response. You can call [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](../../../modules/remotecommunication/document.md#section207321113884) to set the callback function for a request.

**Start version**: 5.0.1(13)

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

[Rcp\_OnBinaryReceiveCallbackFunc](../../../modules/remotecommunication/document.md#section1476912410533) [callback](#a3c40fdbb12e9ace486f03ca31df05ea5)

 | 

Callback function for receiving binary data upon a request.

 |
| 

void \*[usrObject](#ab2e8cda5e0a617a6911360f28b31585a)

 | 

Custom object, which is used in the callback function.

 |

#### Member Variable Description

#### \[h2\]callback

[Rcp\_OnBinaryReceiveCallbackFunc](../../../modules/remotecommunication/document.md#section1476912410533) Rcp\_OnBinaryReceiveCallback::callback

**Description**

Callback function for receiving binary data.

#### \[h2\]usrObject

void\* Rcp\_OnBinaryReceiveCallback::usrObject

**Description**

Custom object, which is used in the callback function.
