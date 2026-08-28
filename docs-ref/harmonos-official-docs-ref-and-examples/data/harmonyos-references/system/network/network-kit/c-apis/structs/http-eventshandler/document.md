# Http\_EventsHandler

typedef struct Http\_EventsHandler {...} Http\_EventsHandler

#### Overview

Defines the callback for various HTTP events.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Http\_OnDataReceiveCallback](../../header-files/net-http-type-h/document.md#http_ondatareceivecallback) onDataReceive | Callback invoked when a response body is received. For details, see [Http\_OnDataReceiveCallback](../../header-files/net-http-type-h/document.md#http_ondatareceivecallback). |
| [Http\_OnProgressCallback](../../header-files/net-http-type-h/document.md#http_onprogresscallback) onUploadProgress | Callback invoked when an upload is triggered. For details, see [Http\_OnProgressCallback](../../header-files/net-http-type-h/document.md#http_onprogresscallback). |
| [Http\_OnProgressCallback](../../header-files/net-http-type-h/document.md#http_onprogresscallback) onDownloadProgress | Callback invoked when a download is triggered. For details, see [Http\_OnProgressCallback](../../header-files/net-http-type-h/document.md#http_onprogresscallback). |
| [Http\_OnHeaderReceiveCallback](../../header-files/net-http-type-h/document.md#http_onheaderreceivecallback) onHeadersReceive | Callback invoked when a header is received. For details, see [Http\_OnHeaderReceiveCallback](../../header-files/net-http-type-h/document.md#http_onheaderreceivecallback). |
| [Http\_OnVoidCallback](../../header-files/net-http-type-h/document.md#http_onvoidcallback) onDataEnd | Callback invoked when the transmission is complete. For details, see [Http\_OnVoidCallback](../../header-files/net-http-type-h/document.md#http_onvoidcallback). |
| [Http\_OnVoidCallback](../../header-files/net-http-type-h/document.md#http_onvoidcallback) onCanceled | Callback invoked when the request is canceled. For details, see [Http\_OnVoidCallback](../../header-files/net-http-type-h/document.md#http_onvoidcallback). |
