# arkweb\_type.h

#### Overview

Defines the native common types of ArkWeb.

**File to include**: <web/arkweb\_type.h>

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_JavaScriptBridgeData](../../structs/arkweb-javascriptbridgedata/document.md) | ArkWeb\_JavaScriptBridgeData | Defines the JavaScript Bridge data. |
| [ArkWeb\_WebMessage\*](../../structs/arkweb-webmessage/document.md) | ArkWeb\_WebMessagePtr | Defines a pointer to the post message. |
| [ArkWeb\_JavaScriptValue\*](../../structs/arkweb-javascriptvalue/document.md) | ArkWeb\_JavaScriptValuePtr | Defines a pointer to the JavaScript data. |
| [ArkWeb\_WebMessagePort\*](../../structs/arkweb-webmessageport/document.md) | ArkWeb\_WebMessagePortPtr | Defines a pointer to the message port. |
| [ArkWeb\_JavaScriptObject](../../structs/arkweb-javascriptobject/document.md) | ArkWeb\_JavaScriptObject | Defines a JavaScript object to inject. |
| [ArkWeb\_ProxyMethod](../../structs/arkweb-proxymethod/document.md) | ArkWeb\_ProxyMethod | Defines a proxy method to inject. |
| [ArkWeb\_ProxyMethodWithResult](../../structs/arkweb-proxymethodwithresult/document.md) | ArkWeb\_ProxyMethodWithResult | Defines a proxy method with result to inject. |
| [ArkWeb\_ProxyObject](../../structs/arkweb-proxyobject/document.md) | ArkWeb\_ProxyObject | Defines a proxy object to inject. |
| [ArkWeb\_ProxyObjectWithResult](../../structs/arkweb-proxyobjectwithresult/document.md) | ArkWeb\_ProxyObjectWithResult | Defines a proxy object with result to inject. |
| [ArkWeb\_ControllerAPI](../../structs/arkweb-controllerapi/document.md) | ArkWeb\_ControllerAPI | Defines a native controller API. Before calling the API, you are advised to use **ARKWEB\_MEMBER\_MISSING** to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The controller APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**. |
| [ArkWeb\_ComponentAPI](../../structs/arkweb-componentapi/document.md) | ArkWeb\_ComponentAPI | Defines a native component API. |
| [ArkWeb\_WebMessagePortAPI](../../structs/arkweb-webmessageportapi/document.md) | ArkWeb\_WebMessagePortAPI | Defines a native message port API. Before calling the API, you are advised to use **ARKWEB\_MEMBER\_MISSING** to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The WebMessagePort APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**. |
| [ArkWeb\_WebMessageAPI](../../structs/arkweb-webmessageapi/document.md) | ArkWeb\_WebMessageAPI | Defines a native post message API. Before calling the API, you are advised to use **ARKWEB\_MEMBER\_MISSING** to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The WebMessage APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**. |
| [ArkWeb\_CookieManagerAPI](../../structs/arkweb-cookiemanagerapi/document.md) | ArkWeb\_CookieManagerAPI | Defines the CookieManager API of ArkWeb. Before calling the API, you are advised to use **ARKWEB\_MEMBER\_MISSING** to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The CookieManager APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**. |
| [ArkWeb\_JavaScriptValueAPI](../../structs/arkweb-javascriptvalueapi/document.md) | ArkWeb\_JavaScriptValueAPI | Defines the JavaScriptValue API of ArkWeb. Before calling the API, you are advised to use **ARKWEB\_MEMBER\_MISSING** to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_WebMessageType](#arkweb_webmessagetype) | ArkWeb\_WebMessageType | Enumerates the data types of post message. |
| [ArkWeb\_JavaScriptValueType](#arkweb_javascriptvaluetype) | ArkWeb\_JavaScriptValueType | Enumerates the JavaScript data types. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*ArkWeb\_OnJavaScriptCallback)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* data, void\* userData)](#arkweb_onjavascriptcallback) | ArkWeb\_OnJavaScriptCallback | Called when the injected JavaScript is executed. |
| [typedef void (\*ArkWeb\_OnJavaScriptProxyCallback)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* dataArray, size\_t arraySize, void\* userData)](#arkweb_onjavascriptproxycallback) | ArkWeb\_OnJavaScriptProxyCallback | Called when the proxy method is executed. |
| [typedef ArkWeb\_JavaScriptValuePtr (\*ArkWeb\_OnJavaScriptProxyCallbackWithResult)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* dataArray, size\_t arraySize, void\* userData)](#arkweb_onjavascriptproxycallbackwithresult) | ArkWeb\_OnJavaScriptProxyCallbackWithResult | Called when the proxy method is executed. |
| [typedef void (\*ArkWeb\_OnComponentCallback)(const char\* webTag, void\* userData)](#arkweb_oncomponentcallback) | ArkWeb\_OnComponentCallback | Called when a component event notification is sent. |
| [typedef void (\*ArkWeb\_OnScrollCallback)(const char\* webTag, void\* userData, double x, double y)](#arkweb_onscrollcallback) | ArkWeb\_OnScrollCallback | Called when the **Web** component is scrolled. |
| [typedef void (\*ArkWeb\_OnMessageEventHandler)(const char\* webTag, const ArkWeb\_WebMessagePortPtr port, const ArkWeb\_WebMessagePtr message, void\* userData)](#arkweb_onmessageeventhandler) | ArkWeb\_OnMessageEventHandler | Called when a post message is sent from the HTML page. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| ARKWEB\_MEMBER\_EXISTS(s, f) ((intptr\_t) & ((s)->f) - (intptr\_t)(s) + sizeof((s)->f) <= \*reinterpret\_cast<size\_t\*>(s)) | 
Whether a member variable exists in the struct.

**Since**: 12

 |
| ARKWEB\_MEMBER\_MISSING(s, f) (!ARKWEB\_MEMBER\_EXISTS(s, f) || !((s)->f)) | 

If the member variable exists in the struct, **false** is returned. Otherwise, **true** is returned.

**Since**: 12

 |

#### Enum Description

#### \[h2\]ArkWeb\_WebMessageType

enum ArkWeb\_WebMessageType

**Description**

Enumerates the data types of post message.

**Since**: 12

| Enumerated Value | Description |
| :-- | :-- |
| ARKWEB\_NONE = 0 | Error data. |
| ARKWEB\_STRING | String data. |
| ARKWEB\_BUFFER | Byte stream data. |

#### \[h2\]ArkWeb\_JavaScriptValueType

enum ArkWeb\_JavaScriptValueType

**Description**

Enumerates the JavaScript data types.

**Since**: 18

| Enumerated Value | Description |
| :-- | :-- |
| ARKWEB\_JAVASCRIPT\_NONE = 0 | Error data. |
| ARKWEB\_JAVASCRIPT\_STRING | String data. |
| ARKWEB\_JAVASCRIPT\_BOOL | Boolean data. |

#### Function Description

#### \[h2\]ArkWeb\_OnJavaScriptCallback()

typedef void (\*ArkWeb\_OnJavaScriptCallback)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* data, void\* userData)

**Description**

Called when the injected JavaScript is executed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const [ArkWeb\_JavaScriptBridgeData](../../structs/arkweb-javascriptbridgedata/document.md)\* data | JavaScriptBridge data. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]ArkWeb\_OnJavaScriptProxyCallback()

typedef void (\*ArkWeb\_OnJavaScriptProxyCallback)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* dataArray, size\_t arraySize, void\* userData)

**Description**

Called when the proxy method is executed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const [ArkWeb\_JavaScriptBridgeData](../../structs/arkweb-javascriptbridgedata/document.md)\* dataArray | Pointer to data array. |
| size\_t arraySize | Array size. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]ArkWeb\_OnJavaScriptProxyCallbackWithResult()

typedef ArkWeb\_JavaScriptValuePtr (\*ArkWeb\_OnJavaScriptProxyCallbackWithResult)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* dataArray, size\_t arraySize, void\* userData)

**Description**

Called when the proxy method is executed.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const [ArkWeb\_JavaScriptBridgeData](../../structs/arkweb-javascriptbridgedata/document.md)\* dataArray | Pointer to data array. |
| size\_t arraySize | Array size. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]ArkWeb\_OnComponentCallback()

typedef void (\*ArkWeb\_OnComponentCallback)(const char\* webTag, void\* userData)

**Description**

Called when a component event notification is sent.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]ArkWeb\_OnScrollCallback()

typedef void (\*ArkWeb\_OnScrollCallback)(const char\* webTag, void\* userData, double x, double y)

**Description**

Called when the **Web** component is scrolled.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| void\* userData | Pointer to user-defined data. |
| double x | Scrolling offset of the X axis. |
| double y | Scrolling offset of the Y axis. |

#### \[h2\]ArkWeb\_OnMessageEventHandler()

typedef void (\*ArkWeb\_OnMessageEventHandler)(const char\* webTag, const ArkWeb\_WebMessagePortPtr port, const ArkWeb\_WebMessagePtr message, void\* userData)

**Description**

Called when a post message is sent from the HTML page.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const [ArkWeb\_WebMessagePortPtr](../../structs/arkweb-webmessageport/document.md) port | Post message port. |
| const [ArkWeb\_WebMessagePtr](../../structs/arkweb-webmessage/document.md) message | Post message data. |
| void\* userData | Pointer to user-defined data. |
