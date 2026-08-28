# arkweb\_scheme\_handler.h

#### Overview

Declares the APIs used to intercept requests from ArkWeb.

**File to include**: <web/arkweb\_scheme\_handler.h>

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

**Example**: [ArkWebSchemeHandler](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkWeb/ArkWebSchemeHandler)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_SchemeHandler\_](../../structs/arkweb-schemehandler/document.md) | ArkWeb\_SchemeHandler | Defines a handler used to intercept requests of a specified scheme. |
| [ArkWeb\_ResourceHandler\_](../../structs/arkweb-resourcehandler/document.md) | ArkWeb\_ResourceHandler | Defines a handler for intercepted URL requests. You can use **ArkWeb\_ResourceHandler** to send custom request headers and bodies. |
| [ArkWeb\_Response\_](../../structs/arkweb-response/document.md) | ArkWeb\_Response | Defines an **ArkWeb\_Response** for the intercepted request. |
| [ArkWeb\_ResourceRequest\_](../../structs/arkweb-resourcerequest/document.md) | ArkWeb\_ResourceRequest | Defines a kernel request. You can use **OH\_ArkWeb\_ResourceRequest** to obtain the URL, method, post data, and other information of the request. |
| [ArkWeb\_RequestHeaderList\_](../../structs/arkweb-requestheaderlist/document.md) | ArkWeb\_RequestHeaderList | Defines a request header list. |
| [ArkWeb\_HttpBodyStream\_](../../structs/arkweb-httpbodystream/document.md) | ArkWeb\_HttpBodyStream | Defines the uploaded data of a request. You can use the **OH\_ArkWebHttpBodyStream\_** API to read the uploaded data. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_CustomSchemeOption](#arkweb_customschemeoption) | ArkWeb\_CustomSchemeOption | Enumerates the custom scheme options. |
| [ArkWeb\_ResourceType](#arkweb_resourcetype) | ArkWeb\_ResourceType | Enumerates the resource types of the request. The resource types match the corresponding items of **ResourceType** in Chromium and should not be renumbered. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*ArkWeb\_OnRequestStart)(const ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_ResourceRequest\* resourceRequest,const ArkWeb\_ResourceHandler\* resourceHandler,bool\* intercept)](#arkweb_onrequeststart) | ArkWeb\_OnRequestStart | Called when a request starts. This callback is used on the IO thread. |
| [typedef void (\*ArkWeb\_OnRequestStop)(const ArkWeb\_SchemeHandler\* schemeHandler,const ArkWeb\_ResourceRequest\* resourceRequest)](#arkweb_onrequeststop) | ArkWeb\_OnRequestStop | 
Called when the request stops. This callback is used on the IO thread.

You can use **ArkWeb\_ResourceRequest\_Destroy** to destroy **resourceRequest**,

and **ArkWeb\_ResourceHandler\_Destroy** to destroy the **ArkWeb\_ResourceHandler** received in **ArkWeb\_OnRequestStart**.

 |
| [typedef void (\*ArkWeb\_HttpBodyStreamReadCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream,uint8\_t\* buffer,int bytesRead)](#arkweb_httpbodystreamreadcallback) | ArkWeb\_HttpBodyStreamReadCallback | Called when **OH\_ArkWebHttpBodyStream\_Read** is complete. |
| [typedef void (\*ArkWeb\_HttpBodyStreamAsyncReadCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream,uint8\_t\* buffer,int bytesRead)](#arkweb_httpbodystreamasyncreadcallback) | ArkWeb\_HttpBodyStreamAsyncReadCallback | Called when **OH\_ArkWebHttpBodyStream\_AsyncRead** is complete. |
| [typedef void (\*ArkWeb\_HttpBodyStreamInitCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream, ArkWeb\_NetError result)](#arkweb_httpbodystreaminitcallback) | ArkWeb\_HttpBodyStreamInitCallback | Called when **ArkWeb\_HttpBodyStream** initialization is complete. |
| [void OH\_ArkWebRequestHeaderList\_Destroy(ArkWeb\_RequestHeaderList\* requestHeaderList)](#oh_arkwebrequestheaderlist_destroy) | \- | Destroys an **ArkWeb\_RequestHeaderList** object. |
| [int32\_t OH\_ArkWebRequestHeaderList\_GetSize(const ArkWeb\_RequestHeaderList\* requestHeaderList)](#oh_arkwebrequestheaderlist_getsize) | \- | Obtains the size of a request header list. |
| [void OH\_ArkWebRequestHeaderList\_GetHeader(const ArkWeb\_RequestHeaderList\* requestHeaderList,int32\_t index,char\*\* key,char\*\* value)](#oh_arkwebrequestheaderlist_getheader) | \- | Obtains a specified request header. |
| [int32\_t OH\_ArkWebResourceRequest\_SetUserData(ArkWeb\_ResourceRequest\* resourceRequest, void\* userData)](#oh_arkwebresourcerequest_setuserdata) | \- | Sets user data to the **ArkWeb\_ResourceRequest** object. |
| [void\* OH\_ArkWebResourceRequest\_GetUserData(const ArkWeb\_ResourceRequest\* resourceRequest)](#oh_arkwebresourcerequest_getuserdata) | \- | Obtains user data from **ArkWeb\_ResourceRequest**. |
| [void OH\_ArkWebResourceRequest\_GetMethod(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* method)](#oh_arkwebresourcerequest_getmethod) | \- | Obtains the method of a request. |
| [void OH\_ArkWebResourceRequest\_GetUrl(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* url)](#oh_arkwebresourcerequest_geturl) | \- | Obtains the URL of a request. |
| [void OH\_ArkWebResourceRequest\_GetHttpBodyStream(const ArkWeb\_ResourceRequest\* resourceRequest,ArkWeb\_HttpBodyStream\*\* httpBodyStream)](#oh_arkwebresourcerequest_gethttpbodystream) | \- | Creates an **ArkWeb\_HttpBodyStream** to read the uploaded data of the request. |
| [void OH\_ArkWebResourceRequest\_DestroyHttpBodyStream(ArkWeb\_HttpBodyStream\* httpBodyStream)](#oh_arkwebresourcerequest_destroyhttpbodystream) | \- | Destroys an **ArkWeb\_HttpBodyStream** object. |
| [int32\_t OH\_ArkWebResourceRequest\_GetResourceType(const ArkWeb\_ResourceRequest\* resourceRequest)](#oh_arkwebresourcerequest_getresourcetype) | \- | Obtains the resource type of a request. |
| [void OH\_ArkWebResourceRequest\_GetFrameUrl(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* frameUrl)](#oh_arkwebresourcerequest_getframeurl) | \- | Obtains the URL of the frame that triggers the request. |
| [int32\_t OH\_ArkWebHttpBodyStream\_SetUserData(ArkWeb\_HttpBodyStream\* httpBodyStream, void\* userData)](#oh_arkwebhttpbodystream_setuserdata) | \- | Sets user data to the **ArkWeb\_HttpBodyStream** object. |
| [void\* OH\_ArkWebHttpBodyStream\_GetUserData(const ArkWeb\_HttpBodyStream\* httpBodyStream)](#oh_arkwebhttpbodystream_getuserdata) | \- | Obtains user data from **ArkWeb\_HttpBodyStream**. |
| [int32\_t OH\_ArkWebHttpBodyStream\_SetReadCallback(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamReadCallback readCallback)](#oh_arkwebhttpbodystream_setreadcallback) | \- | 

Sets a callback for **OH\_ArkWebHttpBodyStream\_Read**. The result of **OH\_ArkWebHttpBodyStream\_Read** is notified to the caller through **readCallback**,

which will run in the same thread as **OH\_ArkWebHttpBodyStream\_Read**.

 |
| [int32\_t OH\_ArkWebHttpBodyStream\_SetAsyncReadCallback(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamReadCallback readCallback)](#oh_arkwebhttpbodystream_setasyncreadcallback) | \- | 

Sets a callback for **OH\_ArkWebHttpBodyStream\_AsyncRead**. The result of **OH\_ArkWebHttpBodyStream\_AsyncRead** is notified to the caller through **readCallback**,

which will run in the same thread as **OH\_ArkWebHttpBodyStream\_AsyncRead**.

 |
| [int32\_t OH\_ArkWebHttpBodyStream\_Init(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamInitCallback initCallback)](#oh_arkwebhttpbodystream_init) | \- | Initializes **ArkWeb\_HttpBodyStream**. This function must be called before any other function is called. This API needs to be called in the I/O thread. |
| [void OH\_ArkWebHttpBodyStream\_Read(const ArkWeb\_HttpBodyStream\* httpBodyStream, uint8\_t\* buffer, int bufLen)](#oh_arkwebhttpbodystream_read) | \- | Exports the uploaded data of a request to the buffer. The buffer size must be greater than the value of **bufLen**. The data from the worker thread is exported to the buffer. Therefore, before the callback returns the data, the buffer should not be used in other threads to avoid concurrency problems. |
| [void OH\_ArkWebHttpBodyStream\_AsyncRead(const ArkWeb\_HttpBodyStream\* httpBodyStream, uint8\_t\* buffer, int bufLen)](#oh_arkwebhttpbodystream_asyncread) | \- | Exports the uploaded data of a request to the buffer. The buffer size must be greater than the value of **bufLen**. The data from the worker thread is exported to the buffer. Therefore, before the callback returns the data, the buffer should not be used in other threads to avoid concurrency problems. |
| [uint64\_t OH\_ArkWebHttpBodyStream\_GetSize(const ArkWeb\_HttpBodyStream\* httpBodyStream)](#oh_arkwebhttpbodystream_getsize) | \- | Obtains the size of **httpBodyStream**. When data is chunked or **httpBodyStream** is invalid, **0** is always returned. |
| [uint64\_t OH\_ArkWebHttpBodyStream\_GetPosition(const ArkWeb\_HttpBodyStream\* httpBodyStream)](#oh_arkwebhttpbodystream_getposition) | \- | Obtains the position of **httpBodyStream**. |
| [bool OH\_ArkWebHttpBodyStream\_IsChunked(const ArkWeb\_HttpBodyStream\* httpBodyStream)](#oh_arkwebhttpbodystream_ischunked) | \- | Determines whether **httpBodyStream** is chunked. |
| [bool OH\_ArkWebHttpBodyStream\_IsEof(const ArkWeb\_HttpBodyStream\* httpBodyStream)](#oh_arkwebhttpbodystream_iseof) | \- | Determines whether all data in **httpBodyStream** has been read. **true** is returned if all data in **httpBodyStream** has been read. **false** is returned before the chunked **httpBodyStream** is read for the first time. |
| [bool OH\_ArkWebHttpBodyStream\_IsInMemory(const ArkWeb\_HttpBodyStream\* httpBodyStream)](#oh_arkwebhttpbodystream_isinmemory) | \- | Determines whether all the uploaded data in **httpBodyStream** is in memory and all read requests are synchronized successfully. If yes, **true** is returned. **false** is returned if the data is chunked. |
| [int32\_t OH\_ArkWebResourceRequest\_Destroy(const ArkWeb\_ResourceRequest\* resourceRequest)](#oh_arkwebresourcerequest_destroy) | \- | Destroys an **ArkWeb\_ResourceRequest** object. |
| [void OH\_ArkWebResourceRequest\_GetReferrer(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* referrer)](#oh_arkwebresourcerequest_getreferrer) | \- | Obtains the referrer of a request. |
| [void OH\_ArkWebResourceRequest\_GetRequestHeaders(const ArkWeb\_ResourceRequest\* resourceRequest,ArkWeb\_RequestHeaderList\*\* requestHeaderList)](#oh_arkwebresourcerequest_getrequestheaders) | \- | Obtains an **OH\_ArkWeb\_RequestHeaderList**. |
| [bool OH\_ArkWebResourceRequest\_IsRedirect(const ArkWeb\_ResourceRequest\* resourceRequest)](#oh_arkwebresourcerequest_isredirect) | \- | Determines whether a request is redirected. |
| [bool OH\_ArkWebResourceRequest\_IsMainFrame(const ArkWeb\_ResourceRequest\* resourceRequest)](#oh_arkwebresourcerequest_ismainframe) | \- | Determines whether a request is from main frame. |
| [bool OH\_ArkWebResourceRequest\_HasGesture(const ArkWeb\_ResourceRequest\* resourceRequest)](#oh_arkwebresourcerequest_hasgesture) | \- | Determines whether a request is triggered by a user gesture. |
| [int32\_t OH\_ArkWeb\_RegisterCustomSchemes(const char\* scheme, int32\_t option)](#oh_arkweb_registercustomschemes) | \- | 

Registers a custom scheme with **ArkWeb**. This function should not be called for built-in HTTP, HTTPS, FILE, FTP, ABOUT, and DATA protocols.

This function should be called on the main thread before kernel initialization.

 |
| [bool OH\_ArkWebServiceWorker\_SetSchemeHandler(const char\* scheme, ArkWeb\_SchemeHandler\* schemeHandler)](#oh_arkwebserviceworker_setschemehandler) | \- | 

Sets an **ArkWeb\_SchemeHandler** for a specified scheme to intercept requests of the scheme type triggered by **ServiceWorker**. **SchemeHandler** should be set after **BrowserContext** is created.

You can use **WebviewController.initializeWebEngine** to initialize **BrowserContext** without creating the **Web** component.

 |
| [bool OH\_ArkWeb\_SetSchemeHandler(const char\* scheme, const char\* webTag, ArkWeb\_SchemeHandler\* schemeHandler)](#oh_arkweb_setschemehandler) | \- | 

Sets an **ArkWeb\_SchemeHandler** to intercept requests of a specified scheme type. **SchemeHandler** should be set after **BrowserContext** is created.

You can use **WebviewController.initializeWebEngine** to initialize **BrowserContext** without creating the **Web** component.

 |
| [int32\_t OH\_ArkWebServiceWorker\_ClearSchemeHandlers()](#oh_arkwebserviceworker_clearschemehandlers) | \- | Clears the **SchemeHandler** registered for **ServiceWorker**. |
| [int32\_t OH\_ArkWeb\_ClearSchemeHandlers(const char\* webTag)](#oh_arkweb_clearschemehandlers) | \- | Clears the **SchemeHandler** registered for the specified **Web** component. |
| [void OH\_ArkWeb\_CreateSchemeHandler(ArkWeb\_SchemeHandler\*\* schemeHandler)](#oh_arkweb_createschemehandler) | \- | Creates an **ArkWeb\_SchemeHandler** object. |
| [void OH\_ArkWeb\_DestroySchemeHandler(ArkWeb\_SchemeHandler\* schemeHandler)](#oh_arkweb_destroyschemehandler) | \- | Destroys an **ArkWeb\_SchemeHandler** object. |
| [int32\_t OH\_ArkWebSchemeHandler\_SetUserData(ArkWeb\_SchemeHandler\* schemeHandler, void\* userData)](#oh_arkwebschemehandler_setuserdata) | \- | Sets user data to the **ArkWeb\_SchemeHandler** object. |
| [void\* OH\_ArkWebSchemeHandler\_GetUserData(const ArkWeb\_SchemeHandler\* schemeHandler)](#oh_arkwebschemehandler_getuserdata) | \- | Obtains the user data from **ArkWeb\_SchemeHandler**. |
| [int32\_t OH\_ArkWebSchemeHandler\_SetOnRequestStart(ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_OnRequestStart onRequestStart)](#oh_arkwebschemehandler_setonrequeststart) | \- | Sets an **OnRequestStart** callback for **SchemeHandler**. |
| [int32\_t OH\_ArkWebSchemeHandler\_SetOnRequestStop(ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_OnRequestStop onRequestStop)](#oh_arkwebschemehandler_setonrequeststop) | \- | Sets an **OnRequestStop** callback for **SchemeHandler**. |
| [void OH\_ArkWeb\_CreateResponse(ArkWeb\_Response\*\* response)](#oh_arkweb_createresponse) | \- | Creates an **ArkWeb\_Response** object for the intercepted request. |
| [void OH\_ArkWeb\_DestroyResponse(ArkWeb\_Response\* response)](#oh_arkweb_destroyresponse) | \- | Destroys an **ArkWeb\_Response** object. |
| [int32\_t OH\_ArkWebResponse\_SetUrl(ArkWeb\_Response\* response, const char\* url)](#oh_arkwebresponse_seturl) | \- | Sets a parsed URL that has been redirected or changed due to HSTS. After the setting, redirection is triggered. |
| [void OH\_ArkWebResponse\_GetUrl(const ArkWeb\_Response\* response, char\*\* url)](#oh_arkwebresponse_geturl) | \- | Obtains the parsed URL that has been redirected or changed due to HSTS. |
| [int32\_t OH\_ArkWebResponse\_SetError(ArkWeb\_Response\* response, ArkWeb\_NetError errorCode)](#oh_arkwebresponse_seterror) | \- | Sets an error code for the **ArkWeb\_Response** object. |
| [ArkWeb\_NetError OH\_ArkWebResponse\_GetError(const ArkWeb\_Response\* response)](#oh_arkwebresponse_geterror) | \- | Obtains the error code of **ArkWeb\_Response**. |
| [int32\_t OH\_ArkWebResponse\_SetStatus(ArkWeb\_Response\* response, int status)](#oh_arkwebresponse_setstatus) | \- | Sets an HTTP status code for **ArkWeb\_Response**. |
| [int OH\_ArkWebResponse\_GetStatus(const ArkWeb\_Response\* response)](#oh_arkwebresponse_getstatus) | \- | Obtains the HTTP status code of **ArkWeb\_Response**. |
| [int32\_t OH\_ArkWebResponse\_SetStatusText(ArkWeb\_Response\* response, const char\* statusText)](#oh_arkwebresponse_setstatustext) | \- | Sets a status text for **ArkWeb\_Response**. |
| [void OH\_ArkWebResponse\_GetStatusText(const ArkWeb\_Response\* response, char\*\* statusText)](#oh_arkwebresponse_getstatustext) | \- | Obtains the status text of **ArkWeb\_Response**. |
| [int32\_t OH\_ArkWebResponse\_SetMimeType(ArkWeb\_Response\* response, const char\* mimeType)](#oh_arkwebresponse_setmimetype) | \- | Sets a mime type for **ArkWeb\_Response**. |
| [void OH\_ArkWebResponse\_GetMimeType(const ArkWeb\_Response\* response, char\*\* mimeType)](#oh_arkwebresponse_getmimetype) | \- | Obtains the mime type of **ArkWeb\_Response**. |
| [int32\_t OH\_ArkWebResponse\_SetCharset(ArkWeb\_Response\* response, const char\* charset)](#oh_arkwebresponse_setcharset) | \- | Sets a character set for **ArkWeb\_Response**. |
| [void OH\_ArkWebResponse\_GetCharset(const ArkWeb\_Response\* response, char\*\* charset)](#oh_arkwebresponse_getcharset) | \- | Obtains the character set of **ArkWeb\_Response**. |
| [int32\_t OH\_ArkWebResponse\_SetHeaderByName(ArkWeb\_Response\* response,const char\* name,const char\* value,bool overwrite)](#oh_arkwebresponse_setheaderbyname) | \- | Sets a header for **ArkWeb\_Response**. |
| [void OH\_ArkWebResponse\_GetHeaderByName(const ArkWeb\_Response\* response, const char\* name, char\*\* value)](#oh_arkwebresponse_getheaderbyname) | \- | Obtains the header from **ArkWeb\_Response**. |
| [int32\_t OH\_ArkWebResourceHandler\_Destroy(const ArkWeb\_ResourceHandler\* resourceHandler)](#oh_arkwebresourcehandler_destroy) | \- | Destroys an **ArkWeb\_ResourceHandler** object. |
| [int32\_t OH\_ArkWebResourceHandler\_DidReceiveResponse(const ArkWeb\_ResourceHandler\* resourceHandler,const ArkWeb\_Response\* response)](#oh_arkwebresourcehandler_didreceiveresponse) | \- | Sends a response header to the intercepted request. |
| [int32\_t OH\_ArkWebResourceHandler\_DidReceiveData(const ArkWeb\_ResourceHandler\* resourceHandler,const uint8\_t\* buffer,int64\_t bufLen)](#oh_arkwebresourcehandler_didreceivedata) | \- | Sends a response body to the intercepted request. |
| [int32\_t OH\_ArkWebResourceHandler\_DidFinish(const ArkWeb\_ResourceHandler\* resourceHandler)](#oh_arkwebresourcehandler_didfinish) | \- | Notifies the ArkWeb kernel that the intercepted request has been finished and that no more data is available. |
| [int32\_t OH\_ArkWebResourceHandler\_DidFailWithError(const ArkWeb\_ResourceHandler\* resourceHandler,ArkWeb\_NetError errorCode)](#oh_arkwebresourcehandler_didfailwitherror) | \- | Notifies the ArkWeb kernel that the intercepted request fails. |
| [int32\_t OH\_ArkWebResourceHandler\_DidFailWithErrorV2(const ArkWeb\_ResourceHandler\* resourceHandler,ArkWeb\_NetError errorCode,bool completeIfNoResponse)](#oh_arkwebresourcehandler_didfailwitherrorv2) | \- | Notifies the ArkWeb kernel that the intercepted request fails. Compared with **OH\_ArkWebResourceHandler\_DidFailWithError**, **completeIfNoResponse** is added. With this parameter set to **true**, if **OH\_ArkWebResourceHandler\_DidReceiveResponse** has not been called, a response is automatically generated to complete the network request and the network error code is **\-104**. With this parameter set to **false**, the system waits for the application to call **OH\_ArkWebResourceHandler\_DidReceiveResponse** and transfers the response. |
| [void OH\_ArkWeb\_ReleaseString(char\* string)](#oh_arkweb_releasestring) | \- | Releases the string created by NDK APIs. |
| [void OH\_ArkWeb\_ReleaseByteArray(uint8\_t\* byteArray)](#oh_arkweb_releasebytearray) | \- | Releases the byte array created by NDK APIs. |

#### Enum Description

#### \[h2\]ArkWeb\_CustomSchemeOption

enum ArkWeb\_CustomSchemeOption

**Description**

Enumerates the custom scheme options.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

| Enumerated Value | Description |
| :-- | :-- |
| OH\_ARKWEB\_SCHEME\_OPTION\_NONE = 0 | No special behavior or capability is assigned when the custom scheme is registered. |
| ARKWEB\_SCHEME\_OPTION\_STANDARD = 1 << 0 | The scheme is processed as a standard scheme. |
| ARKWEB\_SCHEME\_OPTION\_LOCAL = 1 << 1 | The scheme is processed using the same security rule as the file URL. |
| ARKWEB\_SCHEME\_OPTION\_DISPLAY\_ISOLATED = 1 << 2 | The request of the scheme can be initiated only by the page that is loaded using the same scheme. |
| ARKWEB\_SCHEME\_OPTION\_SECURE = 1 << 3 | The scheme is processed using the same security rule as the HTTPS URL. |
| ARKWEB\_SCHEME\_OPTION\_CORS\_ENABLED = 1 << 4 | The scheme can send CORS requests. In most cases, this value should be set when **ARKWEB\_SCHEME\_OPTION\_STANDARD** is set. |
| ARKWEB\_SCHEME\_OPTION\_CSP\_BYPASSING = 1 << 5 | The scheme can bypass the Content Security Policy (CSP) check. |
| ARKWEB\_SCHEME\_OPTION\_FETCH\_ENABLED = 1 << 6 | The FETCH API request of the scheme can be initiated. |
| ARKWEB\_SCHEME\_OPTION\_CODE\_CACHE\_ENABLED = 1 << 7 | The JS resources of the scheme support code cache generation. |

#### \[h2\]ArkWeb\_ResourceType

enum ArkWeb\_ResourceType

**Description**

Enumerates the resource types of the request. The resource types match the corresponding items of **ResourceType** in Chromium and should not be renumbered.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

| Enumerated Value | Description |
| :-- | :-- |
| MAIN\_FRAME = 0 | Main frame. |
| SUB\_FRAME = 1 | Frame or iframe. |
| STYLE\_SHEET = 2 | Cascading Style Sheets (CSS). |
| SCRIPT = 3 | External script. |
| IMAGE = 4 | Image (JPG, GIF, PNG, or other format). |
| FONT\_RESOURCE = 5 | Font. |
| SUB\_RESOURCE = 6 | Other sub-resource. If the type is unknown, the default type is used. |
| OBJECT = 7 | The **Object** (or **embed**) tag of the plug-in, or the resource requested by the plug-in. |
| MEDIA = 8 | Media resource. |
| WORKER = 9 | Main resource of the dedicated worker thread. |
| SHARED\_WORKER = 10 | Main resource of a shared worker thread. |
| PREFETCH = 11 | Explicit prefetch request. |
| FAVICON = 12 | Website icon. |
| XHR = 13 | XMLHttpRequest. |
| PING = 14 | Ping request of **/sendBeacon**. |
| SERVICE\_WORKER = 15 | Main resource of a service worker. |
| CSP\_REPORT = 16 | Report of Content Security Policy violation. |
| PLUGIN\_RESOURCE = 17 | Resource requested by the plug-in. |
| NAVIGATION\_PRELOAD\_MAIN\_FRAME = 19 | Main frame redirection request that triggers service worker preloading. |
| NAVIGATION\_PRELOAD\_SUB\_FRAME = 20 | Subframe redirection request that triggers service worker preloading. |

#### Function Description

#### \[h2\]ArkWeb\_OnRequestStart()

typedef void (\*ArkWeb\_OnRequestStart)(const ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_ResourceRequest\* resourceRequest,const ArkWeb\_ResourceHandler\* resourceHandler,bool\* intercept)

**Description**

Called when a request starts. This callback is used on the IO thread.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **ArkWeb\_SchemeHandler**. |
| [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | Object used to obtain the request information. |
| const [ArkWeb\_ResourceHandler](../../structs/arkweb-resourcehandler/document.md)\* resourceHandler | **ArkWeb\_ResourceHandler** of the request. If **intercept** is set to **false**, this parameter should not be used. |
| bool\* intercept | Whether to intercept the request. If the value is **true**, the request will be intercepted. Otherwise, the request will not be intercepted. |

#### \[h2\]ArkWeb\_OnRequestStop()

typedef void (\*ArkWeb\_OnRequestStop)(const ArkWeb\_SchemeHandler\* schemeHandler,const ArkWeb\_ResourceRequest\* resourceRequest)

**Description**

Called when the request stops. This callback is used on the IO thread.

You can use **ArkWeb\_ResourceRequest\_Destroy** to destroy the **resourceRequest** and use **ArkWeb\_ResourceHandler\_Destroy** to destroy the **ArkWeb\_ResourceHandler** received in **ArkWeb\_OnRequestStart**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **ArkWeb\_SchemeHandler**. |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |

#### \[h2\]ArkWeb\_HttpBodyStreamReadCallback()

typedef void (\*ArkWeb\_HttpBodyStreamReadCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream,uint8\_t\* buffer,int bytesRead)

**Description**

Called when **OH\_ArkWebHttpBodyStream\_Read** is complete.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| uint8\_t\* buffer | Buffer for receiving data. |
| int bytesRead | Callback used when **OH\_ArkWebHttpBodyStream\_Read** is complete. If the value of **bytesRead** is greater than 0, the **buffer** is filled with data of the **bytesRead** size. The caller can read data from the **buffer**. If **OH\_ArkWebHttpBodyStream\_IsEOF** is **false**, the caller can continue to read the data left. |

#### \[h2\]ArkWeb\_HttpBodyStreamAsyncReadCallback()

typedef void (\*ArkWeb\_HttpBodyStreamAsyncReadCallback)(const ArkWeb\_HttpBodyStream \*httpBodyStream,uint8\_t \*buffer,int bytesRead)

**Description**

Called when **OH\_ArkWebHttpBodyStream\_AsyncRead** is complete.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| uint8\_t\* buffer | Buffer for receiving data. |
| int bytesRead | Byte count value of the asynchronous read operation result. If the value of **bytesRead** is greater than 0, the **buffer** is filled with data of the **bytesRead** size. You can read data from the **buffer**. If **OH\_ArkWebHttpBodyStream\_IsEOF** is false, you can continue to read the data left. |

#### \[h2\]ArkWeb\_HttpBodyStreamInitCallback()

typedef void (\*ArkWeb\_HttpBodyStreamInitCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream, ArkWeb\_NetError result)

**Description**

Called when **ArkWeb\_HttpBodyStream** initialization is complete.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| [ArkWeb\_NetError](../arkweb-net-error-list-h/document.md#arkweb_neterror) result | Operation result. If the operation is successful, **ARKWEB\_NET\_OK** is returned. Otherwise, see [arkweb\_net\_error\_list.h](../arkweb-net-error-list-h/document.md). |

#### \[h2\]OH\_ArkWebRequestHeaderList\_Destroy()

void OH\_ArkWebRequestHeaderList\_Destroy(ArkWeb\_RequestHeaderList\* requestHeaderList)

**Description**

Destroys an **ArkWeb\_RequestHeaderList** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_RequestHeaderList](../../structs/arkweb-requestheaderlist/document.md)\* requestHeaderList | The **ArkWeb\_RequestHeaderList** to be destroyed. |

#### \[h2\]OH\_ArkWebRequestHeaderList\_GetSize()

int32\_t OH\_ArkWebRequestHeaderList\_GetSize(const ArkWeb\_RequestHeaderList\* requestHeaderList)

**Description**

Obtains the size of a request header list.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_RequestHeaderList](../../structs/arkweb-requestheaderlist/document.md)\* requestHeaderList | Request header list. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Size of the request header. If **requestHeaderList** is invalid, the value is **\-1**. |

#### \[h2\]OH\_ArkWebRequestHeaderList\_GetHeader()

void OH\_ArkWebRequestHeaderList\_GetHeader(const ArkWeb\_RequestHeaderList\* requestHeaderList,int32\_t index,char\*\* key,char\*\* value)

**Description**

Obtains a specified request header.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const ArkWeb\_RequestHeaderList\* requestHeaderList | Request header list. |
| int32\_t index | Index of the request header. |
| char\*\* key | Key of the request header. You should use the **OH\_ArkWeb\_ReleaseString** function to release this string. |
| char\*\* value | Value of the request header. You should use the **OH\_ArkWeb\_ReleaseString** function to release this string. |

#### \[h2\]OH\_ArkWebResourceRequest\_SetUserData()

int32\_t OH\_ArkWebResourceRequest\_SetUserData(ArkWeb\_ResourceRequest\* resourceRequest, void\* userData)

**Description**

Sets user data to the **ArkWeb\_ResourceRequest** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |
| void\* userData | User data to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetUserData()

void\* OH\_ArkWebResourceRequest\_GetUserData(const ArkWeb\_ResourceRequest\* resourceRequest)

**Description**

Obtains user data from **ArkWeb\_ResourceRequest**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | User data. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetMethod()

void OH\_ArkWebResourceRequest\_GetMethod(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* method)

**Description**

Obtains the method of a request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |
| char\*\* method | HTTP request method. This function allocates memory for the **method** string. You should use **OH\_ArkWeb\_ReleaseString** to release the string. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetUrl()

void OH\_ArkWebResourceRequest\_GetUrl(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* url)

**Description**

Obtains the URL of a request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |
| char\*\* url | URL of a request. This function allocates memory for the **url** string. You should release the string using **OH\_ArkWeb\_ReleaseString**. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetHttpBodyStream()

void OH\_ArkWebResourceRequest\_GetHttpBodyStream(const ArkWeb\_ResourceRequest\* resourceRequest,ArkWeb\_HttpBodyStream\*\* httpBodyStream)

**Description**

Creates an **ArkWeb\_HttpBodyStream** to read the uploaded data of the request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |
| [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\*\* httpBodyStream | Uploaded data of the request. This function allocates memory for **httpBodyStream**. You should use **OH\_ArkWebResourceRequest\_DestroyHttpBodyStream** to release **httpBodyStream**. |

#### \[h2\]OH\_ArkWebResourceRequest\_DestroyHttpBodyStream()

void OH\_ArkWebResourceRequest\_DestroyHttpBodyStream(ArkWeb\_HttpBodyStream\* httpBodyStream)

**Description**

Destroys an **ArkWeb\_HttpBodyStream** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | The **httpBodyStream** to be destroyed. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetResourceType()

int32\_t OH\_ArkWebResourceRequest\_GetResourceType(const ArkWeb\_ResourceRequest\* resourceRequest)

**Description**

Obtains the resource type of a request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Resource type of the request. If **resourceRequest** is invalid, the value is **\-1**. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetFrameUrl()

void OH\_ArkWebResourceRequest\_GetFrameUrl(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* frameUrl)

**Description**

Obtains the URL of the frame that triggers this request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |
| char\*\* frameUrl | URL of the frame that triggers the request. This function allocates memory for the URL string. You should release the string using **OH\_ArkWeb\_ReleaseString**. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_SetUserData()

int32\_t OH\_ArkWebHttpBodyStream\_SetUserData(ArkWeb\_HttpBodyStream\* httpBodyStream, void\* userData)

**Description**

Sets user data to the **ArkWeb\_HttpBodyStream** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| void\* userData | User data to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_GetUserData()

void\* OH\_ArkWebHttpBodyStream\_GetUserData(const ArkWeb\_HttpBodyStream\* httpBodyStream)

**Description**

Obtains user data from **ArkWeb\_HttpBodyStream**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | User data. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_SetReadCallback()

int32\_t OH\_ArkWebHttpBodyStream\_SetReadCallback(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamReadCallback readCallback)

**Description**

Sets a callback for **OH\_ArkWebHttpBodyStream\_Read**. The result of **OH\_ArkWebHttpBodyStream\_Read** is notified to the caller through **readCallback**,

which will run in the same thread as **OH\_ArkWebHttpBodyStream\_Read**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| [ArkWeb\_HttpBodyStreamReadCallback](#arkweb_httpbodystreamreadcallback) readCallback | Callback of **OH\_ArkWebHttpBodyStream\_Read**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_SetAsyncReadCallback()

int32\_t OH\_ArkWebHttpBodyStream\_SetAsyncReadCallback(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamAsyncReadCallback readCallback)

**Description**

Sets a callback for **OH\_ArkWebHttpBodyStream\_AsyncRead**. The result of **OH\_ArkWebHttpBodyStream\_AsyncRead** is notified to the caller through **readCallback**,

which runs in the ArkWeb worker thread.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| [ArkWeb\_HttpBodyStreamAsyncReadCallback](#arkweb_httpbodystreamasyncreadcallback) readCallback | Callback of **OH\_ArkWebHttpBodyStream\_AsyncRead**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_Init()

int32\_t OH\_ArkWebHttpBodyStream\_Init(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamInitCallback initCallback)

**Description**

Initializes **ArkWeb\_HttpBodyStream**. This function must be called before any other function is called. This API needs to be called in the I/O thread.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| [ArkWeb\_HttpBodyStreamInitCallback](#arkweb_httpbodystreaminitcallback) initCallback | Callback of the initialization. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_Read()

void OH\_ArkWebHttpBodyStream\_Read(const ArkWeb\_HttpBodyStream\* httpBodyStream, uint8\_t\* buffer, int bufLen)

**Description**

Exports the uploaded data of a request to the buffer. The buffer size must be greater than the value of **bufLen**. The data from the worker thread is exported to the buffer. Therefore, before the callback returns the data, the buffer should not be used in other threads to avoid concurrency problems.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| uint8\_t\* buffer | Buffer for receiving data. |
| int bufLen | Size of the byte to be read. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_AsyncRead()

void OH\_ArkWebHttpBodyStream\_AsyncRead(const ArkWeb\_HttpBodyStream\* httpBodyStream, uint8\_t\* buffer, int bufLen)

**Description**

Exports the uploaded data of a request to the buffer. The buffer size must be greater than **bufLen**. The data from the worker thread is exported to the buffer. Therefore, before the callback returns the data, the buffer should not be used in other threads to avoid concurrency problems.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |
| uint8\_t\* buffer | Buffer for receiving data. |
| int bufLen | Size of the byte to be read. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_GetSize()

uint64\_t OH\_ArkWebHttpBodyStream\_GetSize(const ArkWeb\_HttpBodyStream\* httpBodyStream)

**Description**

Obtains the size of **httpBodyStream**. When data is chunked or **httpBodyStream** is invalid, **0** is always returned.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Size of **httpBodyStream**. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_GetPosition()

uint64\_t OH\_ArkWebHttpBodyStream\_GetPosition(const ArkWeb\_HttpBodyStream\* httpBodyStream)

**Description**

Obtains the position of **httpBodyStream**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Position of **httpBodyStream**. If **httpBodyStream** is invalid, the position value is **0**. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_IsChunked()

bool OH\_ArkWebHttpBodyStream\_IsChunked(const ArkWeb\_HttpBodyStream\* httpBodyStream)

**Description**

Determines whether **httpBodyStream** is chunked.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if **httpBodyStream** is chunked. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_IsEof()

bool OH\_ArkWebHttpBodyStream\_IsEof(const ArkWeb\_HttpBodyStream\* httpBodyStream)

**Description**

Determines whether all data in **httpBodyStream** has been read. **true** is returned if all data in **httpBodyStream** has been read. **false** is returned before the chunked **httpBodyStream** is read for the first time.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if all data has been read. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWebHttpBodyStream\_IsInMemory()

bool OH\_ArkWebHttpBodyStream\_IsInMemory(const ArkWeb\_HttpBodyStream\* httpBodyStream)

**Description**

Determines whether all the uploaded data in **httpBodyStream** is in memory and all read requests are synchronized successfully. If yes, **true** is returned. **false** is returned if the data is chunked.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_HttpBodyStream](../../structs/arkweb-httpbodystream/document.md)\* httpBodyStream | **ArkWeb\_HttpBodyStream**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if all the uploaded data is stored in the memory. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWebResourceRequest\_Destroy()

int32\_t OH\_ArkWebResourceRequest\_Destroy(const ArkWeb\_ResourceRequest\* resourceRequest)

**Description**

Destroys an **ArkWeb\_ResourceRequest** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetReferrer()

void OH\_ArkWebResourceRequest\_GetReferrer(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* referrer)

**Description**

Obtains the referrer of a request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |
| char\*\* referrer | **referrer** of a request. This function allocates memory for the **referrer** string. You should use **OH\_ArkWeb\_ReleaseString** to release the string. |

#### \[h2\]OH\_ArkWebResourceRequest\_GetRequestHeaders()

void OH\_ArkWebResourceRequest\_GetRequestHeaders(const ArkWeb\_ResourceRequest\* resourceRequest,ArkWeb\_RequestHeaderList\*\* requestHeaderList)

**Description**

Obtains an **OH\_ArkWeb\_RequestHeaderList**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |
| [ArkWeb\_RequestHeaderList](../../structs/arkweb-requestheaderlist/document.md)\*\* requestHeaderList | List of request headers. |

#### \[h2\]OH\_ArkWebResourceRequest\_IsRedirect()

bool OH\_ArkWebResourceRequest\_IsRedirect(const ArkWeb\_ResourceRequest\* resourceRequest)

**Description**

Determines whether a request is redirected.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if this request is redirected. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWebResourceRequest\_IsMainFrame()

bool OH\_ArkWebResourceRequest\_IsMainFrame(const ArkWeb\_ResourceRequest\* resourceRequest)

**Description**

Determines whether a request is from main frame.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if this request is from the main framework. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWebResourceRequest\_HasGesture()

bool OH\_ArkWebResourceRequest\_HasGesture(const ArkWeb\_ResourceRequest\* resourceRequest)

**Description**

Determines whether a request is triggered by a user gesture.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceRequest](../../structs/arkweb-resourcerequest/document.md)\* resourceRequest | **ArkWeb\_ResourceRequest**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if this request is triggered by a user gesture. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWeb\_RegisterCustomSchemes()

int32\_t OH\_ArkWeb\_RegisterCustomSchemes(const char\* scheme, int32\_t option)

**Description**

Registers a custom scheme with **ArkWeb**. This function should not be called for built-in HTTP, HTTPS, FILE, FTP, ABOUT, and DATA protocols. This function should be called on the main thread before kernel initialization.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scheme | Scheme to be registered. |
| int32\_t option | Scheme options. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned if the operation is successful. **17100100** is returned if an unknown error occurs. **17100101** is returned if the parameter is invalid. **17100102** is returned if the scheme configuration fails to be registered, which must be registered before the **Web** component is created. |

#### \[h2\]OH\_ArkWebServiceWorker\_SetSchemeHandler()

bool OH\_ArkWebServiceWorker\_SetSchemeHandler(const char\* scheme, ArkWeb\_SchemeHandler\* schemeHandler)

**Description**

Sets an **ArkWeb\_SchemeHandler** for a specified scheme to intercept requests of the scheme type triggered by **ServiceWorker**. **SchemeHandler** should be set after **BrowserContext** is created.

You can use **WebviewController.initializeWebEngine** to initialize **BrowserContext** without creating the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scheme | Scheme to be intercepted. |
| [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **ArkWeb\_SchemeHandler** of the scheme. Only requests triggered by **ServiceWorker** are notified through this **schemeHandler**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if the **SchemeHandler** is successfully set for the specified scheme. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWeb\_SetSchemeHandler()

bool OH\_ArkWeb\_SetSchemeHandler(const char\* scheme, const char\* webTag, ArkWeb\_SchemeHandler\* schemeHandler)

**Description**

Sets an **ArkWeb\_SchemeHandler** to intercept requests of a specified scheme type. **SchemeHandler** should be set after **BrowserContext** is created.

You can use **WebviewController.initializeWebEngine** to initialize **BrowserContext** without creating the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scheme | Scheme to be intercepted. |
| const char\* webTag | Tag that uniquely identifies a **Web** component. Ensure that it is unique. |
| [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **ArkWeb\_SchemeHandler** of the scheme. Only requests triggered from the specified web are notified through this **SchemeHandler**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if the **SchemeHandler** is successfully set for the specified scheme. Otherwise, **false** is returned. |

#### \[h2\]OH\_ArkWebServiceWorker\_ClearSchemeHandlers()

int32\_t OH\_ArkWebServiceWorker\_ClearSchemeHandlers()

**Description**

Clears the **SchemeHandler** registered for **ServiceWorker**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned if the operation is successful. |

#### \[h2\]OH\_ArkWeb\_ClearSchemeHandlers()

int32\_t OH\_ArkWeb\_ClearSchemeHandlers(const char\* webTag)

**Description**

Clears the **SchemeHandler** registered for the specified **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Tag that uniquely identifies a **Web** component. Ensure that it is unique. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWeb\_CreateSchemeHandler()

void OH\_ArkWeb\_CreateSchemeHandler(ArkWeb\_SchemeHandler\*\* schemeHandler)

**Description**

Creates an **ArkWeb\_SchemeHandler** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\*\* schemeHandler | A created **ArkWeb\_SchemeHandler**. Use **OH\_ArkWeb\_DestroyschemeHandler** to destroy it when it is not required. |

#### \[h2\]OH\_ArkWeb\_DestroySchemeHandler()

void OH\_ArkWeb\_DestroySchemeHandler(ArkWeb\_SchemeHandler\* schemeHandler)

**Description**

Destroys an **ArkWeb\_SchemeHandler** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | The **ArkWeb\_SchemeHandler** to be destroyed. |

#### \[h2\]OH\_ArkWebSchemeHandler\_SetUserData()

int32\_t OH\_ArkWebSchemeHandler\_SetUserData(ArkWeb\_SchemeHandler\* schemeHandler, void\* userData)

**Description**

Sets user data to the **ArkWeb\_SchemeHandler** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **ArkWeb\_SchemeHandler**. |
| void\* userData | User data to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebSchemeHandler\_GetUserData()

void\* OH\_ArkWebSchemeHandler\_GetUserData(const ArkWeb\_SchemeHandler\* schemeHandler)

**Description**

Obtains the user data from **ArkWeb\_SchemeHandler**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **ArkWeb\_SchemeHandler**. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | User data. |

#### \[h2\]OH\_ArkWebSchemeHandler\_SetOnRequestStart()

int32\_t OH\_ArkWebSchemeHandler\_SetOnRequestStart(ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_OnRequestStart onRequestStart)

**Description**

Sets an **OnRequestStart** callback for **SchemeHandler**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **SchemeHandler** of the scheme. |
| [ArkWeb\_OnRequestStart](#arkweb_onrequeststart) onRequestStart | The callback function **OnRequestStart**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebSchemeHandler\_SetOnRequestStop()

int32\_t OH\_ArkWebSchemeHandler\_SetOnRequestStop(ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_OnRequestStop onRequestStop)

**Description**

Sets an **OnRequestStop** callback for **SchemeHandler**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_SchemeHandler](../../structs/arkweb-schemehandler/document.md)\* schemeHandler | **SchemeHandler** of the scheme. |
| [ArkWeb\_OnRequestStop](#arkweb_onrequeststop) onRequestStop | The callback function **OnRequestStop**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWeb\_CreateResponse()

void OH\_ArkWeb\_CreateResponse(ArkWeb\_Response\*\* response)

**Description**

Creates an **ArkWeb\_Response** object for the intercepted request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\*\* response | A created **ArkWeb\_Response**. Use **OH\_ArkWeb\_DestroyResponse** to destroy it when it is not required. |

#### \[h2\]OH\_ArkWeb\_DestroyResponse()

void OH\_ArkWeb\_DestroyResponse(ArkWeb\_Response\* response)

**Description**

Destroys an **ArkWeb\_Response** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | The **ArkWeb\_Response** to be destroyed. |

#### \[h2\]OH\_ArkWebResponse\_SetUrl()

int32\_t OH\_ArkWebResponse\_SetUrl(ArkWeb\_Response\* response, const char\* url)

**Description**

Sets a parsed URL that has been redirected or changed due to HSTS. After the setting, redirection is triggered.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| const char\* url | Parsed URL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResponse\_GetUrl()

void OH\_ArkWebResponse\_GetUrl(const ArkWeb\_Response\* response, char\*\* url)

**Description**

Obtains the parsed URL that has been redirected or changed due to HSTS.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| char\*\* url | Parsed URL. |

#### \[h2\]OH\_ArkWebResponse\_SetError()

int32\_t OH\_ArkWebResponse\_SetError(ArkWeb\_Response\* response, ArkWeb\_NetError errorCode)

**Description**

Sets an error code for the **ArkWeb\_Response** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| [ArkWeb\_NetError](../arkweb-net-error-list-h/document.md#arkweb_neterror) errorCode | Error code of the failed request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResponse\_GetError()

ArkWeb\_NetError OH\_ArkWebResponse\_GetError(const ArkWeb\_Response\* response)

**Description**

Obtains the error code of **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_NetError](../arkweb-net-error-list-h/document.md#arkweb_neterror) | Error code of **ArkWeb\_Response**. |

#### \[h2\]OH\_ArkWebResponse\_SetStatus()

int32\_t OH\_ArkWebResponse\_SetStatus(ArkWeb\_Response\* response, int status)

**Description**

Sets an HTTP status code for **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| int status | HTTP status code of the request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResponse\_GetStatus()

int OH\_ArkWebResponse\_GetStatus(const ArkWeb\_Response\* response)

**Description**

Obtains the HTTP status code of **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | HTTP status code of **ArkWeb\_Response**. If **ArkWeb\_Response** is invalid, the value is **\-1**. |

#### \[h2\]OH\_ArkWebResponse\_SetStatusText()

int32\_t OH\_ArkWebResponse\_SetStatusText(ArkWeb\_Response\* response, const char\* statusText)

**Description**

Sets a status text for **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| const char\* statusText | Status text of the request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResponse\_GetStatusText()

void OH\_ArkWebResponse\_GetStatusText(const ArkWeb\_Response\* response, char\*\* statusText)

**Description**

Obtains the status text of **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| char\*\* statusText | Status text of **ArkWeb\_Response**. This function allocates memory for the **statusText** string. You need to release the string using **OH\_ArkWeb\_ReleaseString**. |

#### \[h2\]OH\_ArkWebResponse\_SetMimeType()

int32\_t OH\_ArkWebResponse\_SetMimeType(ArkWeb\_Response\* response, const char\* mimeType)

**Description**

Sets a mime type for **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| const char\* mimeType | Mime type of the request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResponse\_GetMimeType()

void OH\_ArkWebResponse\_GetMimeType(const ArkWeb\_Response\* response, char\*\* mimeType)

**Description**

Obtains the mime type of **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| char\*\* mimeType | Mime type of **ArkWeb\_Response**. This function allocates memory for the **mimeType** string. You need to release the string using **OH\_ArkWeb\_ReleaseString**. |

#### \[h2\]OH\_ArkWebResponse\_SetCharset()

int32\_t OH\_ArkWebResponse\_SetCharset(ArkWeb\_Response\* response, const char\* charset)

**Description**

Sets a character set for **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| const char\* charset | Character set of the request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResponse\_GetCharset()

void OH\_ArkWebResponse\_GetCharset(const ArkWeb\_Response\* response, char\*\* charset)

**Description**

Obtains the character set of **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| char\*\* charset | Character set of **ArkWeb\_Response**. This function allocates memory for the **charset** string. You need to release the string using **OH\_ArkWeb\_ReleaseString**. |

#### \[h2\]OH\_ArkWebResponse\_SetHeaderByName()

int32\_t OH\_ArkWebResponse\_SetHeaderByName(ArkWeb\_Response\* response,const char\* name,const char\* value,bool overwrite)

**Description**

Sets a header for **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| const char\* name | Name of the header. |
| const char\* value | Value of the header. |
| bool overwrite | Whether to overwrite the existing header. The value **true** means to overwrite the existing header, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResponse\_GetHeaderByName()

void OH\_ArkWebResponse\_GetHeaderByName(const ArkWeb\_Response\* response, const char\* name, char\*\* value)

**Description**

Obtains the header from **ArkWeb\_Response**.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response**. |
| const char\* name | Name of the header. |
| char\*\* value | Value of the header. This function allocates memory for the \*\*value \*\*string. You need to release the string using **OH\_ArkWeb\_ReleaseString**. |

#### \[h2\]OH\_ArkWebResourceHandler\_Destroy()

int32\_t OH\_ArkWebResourceHandler\_Destroy(const ArkWeb\_ResourceHandler\* resourceHandler)

**Description**

Destroys an **ArkWeb\_ResourceHandler** object.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceHandler](../../structs/arkweb-resourcehandler/document.md)\* resourceHandler | **ArkWeb\_ResourceHandler**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResourceHandler\_DidReceiveResponse()

int32\_t OH\_ArkWebResourceHandler\_DidReceiveResponse(const ArkWeb\_ResourceHandler\* resourceHandler,const ArkWeb\_Response\* response)

**Description**

Sends a response header to the intercepted request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceHandler](../../structs/arkweb-resourcehandler/document.md)\* resourceHandler | **ArkWeb\_ResourceHandler** of the request. |
| const [ArkWeb\_Response](../../structs/arkweb-response/document.md)\* response | **ArkWeb\_Response** of the intercepted request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResourceHandler\_DidReceiveData()

int32\_t OH\_ArkWebResourceHandler\_DidReceiveData(const ArkWeb\_ResourceHandler\* resourceHandler,const uint8\_t\* buffer,int64\_t bufLen)

**Description**

Sends a response body to the intercepted request.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceHandler](../../structs/arkweb-resourcehandler/document.md)\* resourceHandler | **ArkWeb\_ResourceHandler** of the request. |
| const uint8\_t\* buffer | Buffer data to be sent. |
| int64\_t bufLen | Buffer size. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResourceHandler\_DidFinish()

int32\_t OH\_ArkWebResourceHandler\_DidFinish(const ArkWeb\_ResourceHandler\* resourceHandler)

**Description**

Notifies the ArkWeb kernel that the intercepted request has been finished and that no more data is available.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceHandler](../../structs/arkweb-resourcehandler/document.md)\* resourceHandler | **ArkWeb\_ResourceHandler** of the request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResourceHandler\_DidFailWithError()

int32\_t OH\_ArkWebResourceHandler\_DidFailWithError(const ArkWeb\_ResourceHandler\* resourceHandler,ArkWeb\_NetError errorCode)

**Description**

Notifies the ArkWeb kernel that the intercepted request fails.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceHandler](../../structs/arkweb-resourcehandler/document.md)\* resourceHandler | Handler for intercepted URL requests. You can use **ArkWeb\_ResourceHandler** to send custom request headers and bodies. |
| [ArkWeb\_NetError](../arkweb-net-error-list-h/document.md#arkweb_neterror) errorCode | Error code of the request. For details, see [arkweb\_net\_error\_list.h](../arkweb-net-error-list-h/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWebResourceHandler\_DidFailWithErrorV2()

int32\_t OH\_ArkWebResourceHandler\_DidFailWithErrorV2(const ArkWeb\_ResourceHandler\* resourceHandler,ArkWeb\_NetError errorCode,bool completeIfNoResponse)

**Description**

Notifies the ArkWeb kernel that the intercepted request fails. Compared with the [OH\_ArkWebResourceHandler\_DidFailWithError](#oh_arkwebresourcehandler_didfailwitherror) API, the **completeIfNoResponse** parameter is added. With this parameter set to **true**, if [OH\_ArkWebResourceHandler\_DidReceiveResponse](#oh_arkwebresourcehandler_didreceiveresponse) has not been called, a response is automatically generated to complete the network request and the network error code is **\-104**. With this parameter set to **false**, the system waits for the application to call [OH\_ArkWebResourceHandler\_DidReceiveResponse](#oh_arkwebresourcehandler_didreceiveresponse) and pass the response.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_ResourceHandler](../../structs/arkweb-resourcehandler/document.md)\* resourceHandler | Handler for intercepted URL requests. You can use **ArkWeb\_ResourceHandler** to send custom request headers and bodies. |
| [ArkWeb\_NetError](../arkweb-net-error-list-h/document.md#arkweb_neterror) errorCode | Error code of the request. For details, see [arkweb\_net\_error\_list.h](../arkweb-net-error-list-h/document.md). |
| bool completeIfNoResponse | Whether the network request is complete when [OH\_ArkWebResourceHandler\_DidFailWithErrorV2](#oh_arkwebresourcehandler_didfailwitherrorv2) is called if [OH\_ArkWebResourceHandler\_DidReceiveResponse](#oh_arkwebresourcehandler_didreceiveresponse) is not called before. If the value is **true** and [OH\_ArkWebResourceHandler\_DidReceiveResponse](#oh_arkwebresourcehandler_didreceiveresponse) is not called before, a response is automatically generated to complete the network request, and the network error code is **\-104**. If the value is **false**, the system waits for the application to call [OH\_ArkWebResourceHandler\_DidReceiveResponse](#oh_arkwebresourcehandler_didreceiveresponse) and pass the response. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** is returned when the operation is successful; **17100101** is returned when the parameter is invalid. |

#### \[h2\]OH\_ArkWeb\_ReleaseString()

void OH\_ArkWeb\_ReleaseString(char\* string)

**Description**

Releases the string created by NDK APIs.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* string | String to be released. |

#### \[h2\]OH\_ArkWeb\_ReleaseByteArray()

void OH\_ArkWeb\_ReleaseByteArray(uint8\_t\* byteArray)

**Description**

Releases the byte array created by NDK APIs.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t\* byteArray | Byte array to be released. |
