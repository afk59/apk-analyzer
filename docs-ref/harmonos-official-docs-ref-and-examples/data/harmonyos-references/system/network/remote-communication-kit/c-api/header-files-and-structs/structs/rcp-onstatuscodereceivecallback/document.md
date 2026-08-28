# Rcp\_OnStatusCodeReceiveCallback

#### Overview

Callback function for receiving a response status code. You can call [HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](../../../modules/remotecommunication/document.md#section10194153116201) to set the callback function for a request.

**Start version**: 6.0.1(21)

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

[Rcp\_OnStatusCodeReceiveCallbackFunc](../../../modules/remotecommunication/document.md#section1961611617339)

 | 

Callback function used to receive a response status code during a request.

 |
| 

void \*[usrObject](#section271832410116)

 | 

Custom object, which is used in the callback function.

 |

#### Member Variable Description

#### \[h2\]callback

[Rcp\_OnStatusCodeReceiveCallbackFunc](../../../modules/remotecommunication/document.md#section1961611617339) Rcp\_OnStatusCodeReceiveCallback::callback

**Description**

Callback function for receiving a response status code.

#### \[h2\]usrObject

void\* Rcp\_OnStatusCodeReceiveCallback::usrObject

**Description**

Custom object, which is used in the callback function.
