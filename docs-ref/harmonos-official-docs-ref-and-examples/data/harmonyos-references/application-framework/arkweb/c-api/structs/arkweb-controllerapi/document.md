# ArkWeb\_ControllerAPI

typedef struct {...} ArkWeb\_ControllerAPI

#### Overview

Defines a native controller API. Before calling this API, you are advised to use [ARKWEB\_MEMBER\_MISSING](../../header-files/arkweb-type-h/document.md#macros) to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The controller APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**.

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t size | Size of the struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [void (\*runJavaScript)(const char\* webTag, const ArkWeb\_JavaScriptObject\* javascriptObject)](#runjavascript) | Injects a JavaScript script. |
| [void (\*registerJavaScriptProxy)(const char\* webTag, const ArkWeb\_ProxyObject\* proxyObject)](#registerjavascriptproxy) | Injects a JavaScript object with the window. Synchronous APIs of this object can then be invoked in the window. |
| [void (\*deleteJavaScriptRegister)(const char\* webTag, const char\* objName)](#deletejavascriptregister) | Deletes a specific application JavaScript object that is registered with the window using **registerJavaScriptProxy**. |
| [void (\*refresh)(const char\* webTag)](#refresh) | Refreshes the web page. The page stack is cleared during the refresh. As a result, the current page cannot be navigated forward or backward. |
| [void (\*registerAsyncJavaScriptProxy)(const char\* webTag, const ArkWeb\_ProxyObject\* proxyObject)](#registerasyncjavascriptproxy) | Injects a JavaScript object with the window. Asynchronous APIs of this object can then be invoked in the window. |
| [ArkWeb\_WebMessagePortPtr\* (\*createWebMessagePorts)(const char\* webTag, size\_t\* size)](#createwebmessageports) | Creates a post message port. |
| [void (\*destroyWebMessagePorts)(ArkWeb\_WebMessagePortPtr\*\* ports, size\_t size)](#destroywebmessageports) | Destroys a message port. |
| [ArkWeb\_ErrorCode (\*postWebMessage)(const char\* webTag, const char\* name, ArkWeb\_WebMessagePortPtr\* webMessagePorts, size\_t size, const char\* url)](#postwebmessage) | Sends a message port to the HTML page. |
| [const char\* (\*getLastJavascriptProxyCallingFrameUrl)()](#getlastjavascriptproxycallingframeurl) | 
Obtains the URL of the last frame that calls **JavaScriptProxy**. This function is invoked on the thread invoked by **JavaScriptProxy**. You can use **registerJavaScriptProxy** or **JavaScriptProxy** to inject a JavaScript object to a window object. This API can be used to obtain the URL of the last frame calls the injected object. You need to save the URL obtained from the invoked function.

**Since**: 14

 |
| [void (\*registerJavaScriptProxyEx)(const char\* webTag, const ArkWeb\_ProxyObjectWithResult\* proxyObject,const char\* permission)](#registerjavascriptproxyex) | 

Injects a JavaScript object with the window. Synchronous APIs of this object can then be invoked in the window. The synchronization method of this object can contain return values.

**Since**: 18

 |
| [void (\*registerAsyncJavaScriptProxyEx)(const char\* webTag, const ArkWeb\_ProxyObject\* proxyObject,const char\* permission)](#registerasyncjavascriptproxyex) | 

Injects a JavaScript object with the window. Asynchronous APIs of this object can then be invoked in the window.

**Since**: 18

 |

#### Member Function Description

#### \[h2\]runJavaScript()

void (\*runJavaScript)(const char\* webTag, const ArkWeb\_JavaScriptObject\* javascriptObject)

**Description**

Injects a JavaScript script.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const ArkWeb\_JavaScriptObject\* javascriptObject | JavaScript object to inject. |

#### \[h2\]registerJavaScriptProxy()

void (\*registerJavaScriptProxy)(const char\* webTag, const ArkWeb\_ProxyObject\* proxyObject)

**Description**

Injects a JavaScript object with the window. Synchronous APIs of this object can then be invoked in the window.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const ArkWeb\_ProxyObject\* proxyObject | Object to be registered. |

#### \[h2\]deleteJavaScriptRegister()

void (\*deleteJavaScriptRegister)(const char\* webTag, const char\* objName)

**Description**

Deletes a specific application JavaScript object that is registered with the window using **registerJavaScriptProxy**.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* objName | Name of the JavaScript object. |

#### \[h2\]refresh()

void (\*refresh)(const char\* webTag)

**Description**

Refreshes the web page. The page stack is cleared during the refresh. As a result, the current page cannot be navigated forward or backward.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |

#### \[h2\]registerAsyncJavaScriptProxy()

void (\*registerAsyncJavaScriptProxy)(const char\* webTag, const ArkWeb\_ProxyObject\* proxyObject)

**Description**

Injects a JavaScript object with the window. Asynchronous APIs of this object can then be invoked in the window.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const ArkWeb\_ProxyObject\* proxyObject | Object to be registered. |

#### \[h2\]createWebMessagePorts()

ArkWeb\_WebMessagePortPtr\* (\*createWebMessagePorts)(const char\* webTag, size\_t\* size)

**Description**

Creates a post message port.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| size\_t\* size | Number of ports, which is an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePortPtr](../arkweb-webmessageport/document.md) | Pointer to the message port. |

#### \[h2\]destroyWebMessagePorts()

void (\*destroyWebMessagePorts)(ArkWeb\_WebMessagePortPtr\*\* ports, size\_t size)

**Description**

Destroys a message port.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePortPtr](../arkweb-webmessageport/document.md)\*\* ports | Double pointer to the message port struct. |
| size\_t size | Number of ports. |

#### \[h2\]postWebMessage()

ArkWeb\_ErrorCode (\*postWebMessage)(const char\* webTag, const char\* name, ArkWeb\_WebMessagePortPtr\* webMessagePorts, size\_t size, const char\* url)

**Description**

Sends a message port to the HTML page.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* name | Name of the message sent to the HTML page. |
| [ArkWeb\_WebMessagePortPtr](../arkweb-webmessageport/document.md)\* webMessagePorts | Pointer to the message port. |
| size\_t size | Number of ports. |
| const char\* url | URL of the page that receives the message. |

**Returns**

| Type | Description |
| :-- | :-- |
| Error code | 
[ARKWEB\_SUCCESS](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The operation is successful.

[ARKWEB\_INVALID\_PARAM](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The parameter is invalid.

[ARKWEB\_INIT\_ERROR](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The initialization fails because the **Web** component bound to **webTag** is not found.

 |

#### \[h2\]getLastJavascriptProxyCallingFrameUrl()

const char\* (\*getLastJavascriptProxyCallingFrameUrl)()

**Description**

Obtains the URL of the last frame that calls **JavaScriptProxy**. This function is invoked on the thread invoked by **JavaScriptProxy**. You can use **registerJavaScriptProxy** or **JavaScriptProxy** to inject a JavaScript object to a window object. This API can be used to obtain the URL of the last frame calls the injected object. You need to save the URL obtained from the invoked function.

**Since**: 14

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | URL of the last frame that calls **JavaScriptProxy**. |

#### \[h2\]registerJavaScriptProxyEx()

void (\*registerJavaScriptProxyEx)(const char\* webTag, const ArkWeb\_ProxyObjectWithResult\* proxyObject,const char\* permission)

**Description**

Injects a JavaScript object with the window. Synchronous APIs of this object can then be invoked in the window. The synchronization method of this object can contain return values.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const [ArkWeb\_ProxyObjectWithResult](../arkweb-proxyobjectwithresult/document.md)\* proxyObject | Object to be registered. |
| const char\* permission | A JSON string used to configure the object and method levels of the JSBridge permission. This value is empty by default. |

#### \[h2\]registerAsyncJavaScriptProxyEx()

void (\*registerAsyncJavaScriptProxyEx)(const char\* webTag, const ArkWeb\_ProxyObject\* proxyObject, const char\* permission)

**Description**

Injects a JavaScript object with the window. Asynchronous APIs of this object can then be invoked in the window.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const ArkWeb\_ProxyObject\* proxyObject | Object to be registered. |
| const char\* permission | A JSON string used to configure the object and method levels of the JSBridge permission. This value is empty by default. |
