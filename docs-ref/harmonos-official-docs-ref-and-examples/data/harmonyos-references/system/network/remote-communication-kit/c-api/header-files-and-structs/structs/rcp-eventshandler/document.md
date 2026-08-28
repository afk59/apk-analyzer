# Rcp\_EventsHandler

#### Overview

Callback function for listening on various HTTP events.

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

[Rcp\_OnDataReceiveCallback](../rcp-ondatareceivecallback/document.md) [onDataReceive](#adbe4eae15e9325332c4723041c956ca1)

 | 

Callback function triggered when a response body is returned.

 |
| 

[Rcp\_OnProgressCallback](../rcp-onprogresscallback/document.md) [onUploadProgress](#a2ed016a986b6813c6983ffbeac55827f)

 | 

Callback function triggered upon upload.

 |
| 

[Rcp\_OnProgressCallback](../rcp-onprogresscallback/document.md) [onDownloadProgress](#a9f8a879701150c07720137a61945fcb5)

 | 

Callback function triggered upon download.

 |
| 

[Rcp\_OnHeaderReceiveCallback](../rcp-onheaderreceivecallback/document.md) [onHeaderReceive](#a8431cdb73925f4df6213ec6385b2f0f9)

 | 

Callback function triggered when a header is returned.

 |
| 

[Rcp\_OnVoidCallback](../rcp-onvoidcallback/document.md) [onDataEnd](#a7dfa76b63d826eddafc885b79813d226)

 | 

Callback function triggered when transmission ends.

 |
| 

[Rcp\_OnVoidCallback](../rcp-onvoidcallback/document.md) [onCanceled](#aff228ac71317d81091f0ded4a2164624)

 | 

Callback function triggered when a request or session is canceled.

 |

#### Member Variable Description

#### \[h2\]onCanceled

[Rcp\_OnVoidCallback](../rcp-onvoidcallback/document.md) Rcp\_EventsHandler::onCanceled

**Description**

Callback function triggered when a request or session is canceled.

#### \[h2\]onDataEnd

[Rcp\_OnVoidCallback](../rcp-onvoidcallback/document.md) Rcp\_EventsHandler::onDataEnd

**Description**

Callback function triggered when transmission ends.

#### \[h2\]onDataReceive

[Rcp\_OnDataReceiveCallback](../rcp-ondatareceivecallback/document.md) Rcp\_EventsHandler::onDataReceive

**Description**

Callback function triggered when a response body is returned.

#### \[h2\]onDownloadProgress

[Rcp\_OnProgressCallback](../rcp-onprogresscallback/document.md) Rcp\_EventsHandler::onDownloadProgress

**Description**

Callback function triggered upon download.

#### \[h2\]onHeaderReceive

[Rcp\_OnHeaderReceiveCallback](../rcp-onheaderreceivecallback/document.md) Rcp\_EventsHandler::onHeaderReceive

**Description**

Callback function triggered when a header is returned.

#### \[h2\]onUploadProgress

[Rcp\_OnProgressCallback](../rcp-onprogresscallback/document.md) Rcp\_EventsHandler::onUploadProgress

**Description**

Callback function triggered upon upload.
