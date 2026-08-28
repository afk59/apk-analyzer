# native\_interface\_arkweb.h

#### Overview

Declares APIs used to register objects and execute JavaScript code.

**File to include**: <web/native\_interface\_arkweb.h>

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Related module**: [Web](../../modules/web/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_BlanklessInfo](../../structs/arkweb-blanklessinfo/document.md) | ArkWeb\_BlanklessInfo | Defines the prediction information about blankless loading, including the first screen similarity, first screen loading duration, and error code. The application determines whether to enable frame insertion for blankless loading based on the prediction information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWebEngineVersion](#arkwebengineversion) | ArkWebEngineVersion | For details about the ArkWeb kernel version, see [Adaptation Guide for the M114 Kernel on HarmonyOS 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md). |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*NativeArkWeb\_OnJavaScriptCallback)(const char\*)](#nativearkweb_onjavascriptcallback) | NativeArkWeb\_OnJavaScriptCallback | Called to return the result after the JavaScript code is executed. |
| [typedef char\* (\*NativeArkWeb\_OnJavaScriptProxyCallback)(const char\*\* argv, int32\_t argc)](#nativearkweb_onjavascriptproxycallback) | NativeArkWeb\_OnJavaScriptProxyCallback | Called when a JavaScript proxy is registered. |
| [typedef void (\*NativeArkWeb\_OnValidCallback)(const char\*)](#nativearkweb_onvalidcallback) | NativeArkWeb\_OnValidCallback | Called when a **Web** component is valid. |
| [typedef void (\*NativeArkWeb\_OnDestroyCallback)(const char\*)](#nativearkweb_ondestroycallback) | NativeArkWeb\_OnDestroyCallback | Called when a **Web** component is destroyed. |
| [typedef void (\*OH\_ArkWeb\_OnCookieSaveCallback)(ArkWeb\_ErrorCode errorCode)](#oh_arkweb_oncookiesavecallback) | OH\_ArkWeb\_OnCookieSaveCallback | 
Called when a cookie is saved.

**Since**: 20

 |
| [void OH\_NativeArkWeb\_RunJavaScript(const char\* webTag, const char\* jsCode, NativeArkWeb\_OnJavaScriptCallback callback)](#oh_nativearkweb_runjavascript) | \- | Loads and asynchronously executes a JavaScript code in the current page. |
| [void OH\_NativeArkWeb\_RegisterJavaScriptProxy(const char\* webTag, const char\* objName, const char\*\* methodList,NativeArkWeb\_OnJavaScriptProxyCallback\* callback, int32\_t size, bool needRefresh)](#oh_nativearkweb_registerjavascriptproxy) | \- | Displays the list of registered objects and function names. |
| [void OH\_NativeArkWeb\_UnregisterJavaScriptProxy(const char\* webTag, const char\* objName)](#oh_nativearkweb_unregisterjavascriptproxy) | \- | Deletes a registered object and its callback. |
| [void OH\_NativeArkWeb\_SetJavaScriptProxyValidCallback(const char\* webTag, NativeArkWeb\_OnValidCallback callback)](#oh_nativearkweb_setjavascriptproxyvalidcallback) | \- | Sets a callback used when an object is valid. |
| [NativeArkWeb\_OnValidCallback OH\_NativeArkWeb\_GetJavaScriptProxyValidCallback(const char\* webTag)](#oh_nativearkweb_getjavascriptproxyvalidcallback) | \- | Obtains the callback used when a registered object is valid. |
| [void OH\_NativeArkWeb\_SetDestroyCallback(const char\* webTag, NativeArkWeb\_OnDestroyCallback callback)](#oh_nativearkweb_setdestroycallback) | \- | Sets a callback used when a component is destroyed. |
| [NativeArkWeb\_OnDestroyCallback OH\_NativeArkWeb\_GetDestroyCallback(const char\* webTag)](#oh_nativearkweb_getdestroycallback) | \- | Obtains the callback used when a registered component is destroyed. |
| [ArkWeb\_ErrorCode OH\_NativeArkWeb\_LoadData(const char\* webTag,const char\* data,const char\* mimeType,const char\* encoding,const char\* baseUrl,const char\* historyUrl)](#oh_nativearkweb_loaddata) | \- | Loads data or URLs. This function must be called in the main thread. |
| [void OH\_NativeArkWeb\_RegisterAsyncThreadJavaScriptProxy(const char\* webTag,const ArkWeb\_ProxyObjectWithResult\* proxyObject, const char\* permission)](#oh_nativearkweb_registerasyncthreadjavascriptproxy) | \- | Registers a JavaScript object that contains callback methods, which can have return values. This object will be registered into all frames of the current page, including all iframes, and can be accessed by using the name specified in **ArkWeb\_ProxyObjectWithResult**. The object takes effect in JavaScript only after the page is loaded or reloaded next time. Its methods are executed in the worker thread of ArkWeb. |
| [ArkWeb\_ErrorCode OH\_ArkWebCookieManager\_SaveCookieSync()](#oh_arkwebcookiemanager_savecookiesync) | \- | 

Saves all cookies that can be accessed through the **CookieManager** API to disks. To use this API in a non-UI thread, you need to use **OH\_ArkWeb\_GetNativeAPI** to initialize the **CookieManager** API.

**Since**: 20

 |
| [void OH\_ArkWebCookieManager\_SaveCookieAsync(OH\_ArkWeb\_OnCookieSaveCallback callback)](#oh_arkwebcookiemanager_savecookieasync) | \- | 

Saves all cookies that can be accessed through the **CookieManager** API to disks. If the **CookieManager** API is not initialized, this API is automatically executed on the UI thread.

**Since**: 20

 |
| [ArkWeb\_BlanklessInfo OH\_NativeArkWeb\_GetBlanklessInfoWithKey(const char\* webTag, const char\* key)](#oh_nativearkweb_getblanklessinfowithkey) | \- | Obtains the first screen loading prediction information, and starts to generate the loading transition frame. The application determines whether to enable blankless loading based on the information. For details, see [ArkWeb\_BlanklessInfo](../../structs/arkweb-blanklessinfo/document.md). This API must be used together with the [OH\_NativeArkWeb\_SetBlanklessLoadingWithKey](#oh_nativearkweb_setblanklessloadingwithkey) API and must be called before the page loading API is triggered and after **WebViewController** is bound to the **Web** component. |
| [ArkWeb\_BlanklessErrorCode OH\_NativeArkWeb\_SetBlanklessLoadingWithKey(const char\* webTag, const char\* key, bool isStarted)](#oh_nativearkweb_setblanklessloadingwithkey) | \- | Sets whether to enable blankless loading. This API must be used together with the [OH\_NativeArkWeb\_GetBlanklessInfoWithKey](#oh_nativearkweb_getblanklessinfowithkey) API. |
| [void OH\_NativeArkWeb\_ClearBlanklessLoadingCache(const char\* key\[\], uint32\_t size)](#oh_nativearkweb_clearblanklessloadingcache) | \- | Clears the blankless loading cache of the page with a specified key value. |
| [uint32\_t OH\_NativeArkWeb\_SetBlanklessLoadingCacheCapacity(uint32\_t capacity)](#oh_nativearkweb_setblanklessloadingcachecapacity) | \- | Sets the persistent cache capacity of the blankless loading solution and returns the value that takes effect. The default cache capacity is 30 MB, and the maximum cache capacity is 100 MB. When this limit is exceeded, transition frames that are not frequently used are eliminated. |
| [void OH\_NativeArkWeb\_SetActiveWebEngineVersion(ArkWebEngineVersion webEngineVersion)](#oh_nativearkweb_setactivewebengineversion) | \- | Sets the ArkWeb kernel version. If the system does not support the specified version, the setting is invalid. This API is a global static method and must be called before **initializeWebEngine** is called. If any **Web** component has been loaded, the setting of this API is invalid. |
| [ArkWebEngineVersion OH\_NativeArkWeb\_GetActiveWebEngineVersion()](#oh_nativearkweb_getactivewebengineversion) | \- | Obtain the current ArkWeb kernel version. |
| [void OH\_NativeArkWeb\_LazyInitializeWebEngineInCookieManager(bool lazy)](#oh_nativearkweb_lazyinitializewebengineincookiemanager) | \- | Sets whether to delay the initialization of the ArkWeb kernel. If this method is not called, the ArkWeb kernel is not delayed by default. |

#### Enum Description

#### \[h2\]ArkWebEngineVersion

enum ArkWebEngineVersion

**Description**

For details about the ArkWeb kernel version, see [Adaptation Guide for the M114 Kernel on HarmonyOS 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md).

| **Kernel Type** | **Name** | **Description** |
| :-- | :-- | :-- |
| Evergreen kernel | EVERGREEN WebCore | Latest Web kernel of the system, based on which the complete functionalities are implemented. This kernel is recommended for applications. |
| Legacy kernel | LEGACY WebCore | A previous-release kernel that receives only security and PR-related fixes, used solely for compatibility rollback, and is supported for a fixed duration only. |

**Since**: 20

| Enum | Description |
| :-- | :-- |
| SYSTEM\_DEFAULT = 0 | Default system kernel. For HarmonyOS 6.0, the default kernel is M132. |
| ARKWEB\_M114 = 1 | Legacy kernel of HarmonyOS 6.0. You can select this legacy kernel. If it does not exist, the setting is invalid. |
| ARKWEB\_M132 = 2 | Evergreen kernel of HarmonyOS 6.0, which is M132 by default. If it does not exist, the setting is invalid. |

#### Function Description

#### \[h2\]NativeArkWeb\_OnJavaScriptCallback()

typedef void (\*NativeArkWeb\_OnJavaScriptCallback)(const char\*)

**Description**

Called to return the result after the JavaScript code is executed.

**Since**: 11

#### \[h2\]NativeArkWeb\_OnJavaScriptProxyCallback()

typedef char\* (\*NativeArkWeb\_OnJavaScriptProxyCallback)(const char\*\* argv, int32\_t argc)

**Description**

Called when a JavaScript proxy is registered.

**Since**: 11

#### \[h2\]NativeArkWeb\_OnValidCallback()

typedef void (\*NativeArkWeb\_OnValidCallback)(const char\*)

**Description**

Called when a **Web** component is valid.

**Since**: 11

#### \[h2\]NativeArkWeb\_OnDestroyCallback()

typedef void (\*NativeArkWeb\_OnDestroyCallback)(const char\*)

**Description**

Called when a **Web** component is destroyed.

**Since**: 11

#### \[h2\]OH\_ArkWeb\_OnCookieSaveCallback()

typedef void (\*OH\_ArkWeb\_OnCookieSaveCallback)(ArkWeb\_ErrorCode errorCode)

**Description**

Called when a cookie is saved.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode](../arkweb-error-code-h/document.md#arkweb_errorcode) errorCode | 
[ARKWEB\_SUCCESS](../arkweb-error-code-h/document.md#arkweb_errorcode): The cookie is successfully saved.

[ARKWEB\_COOKIE\_SAVE\_FAILED](../arkweb-error-code-h/document.md#arkweb_errorcode): Failed to save the cookie.

[ARKWEB\_COOKIE\_MANAGER\_INITIALIZE\_FAILED](../arkweb-error-code-h/document.md#arkweb_errorcode): The **CookieManager** initialization failed.

 |

#### \[h2\]OH\_NativeArkWeb\_RunJavaScript()

void OH\_NativeArkWeb\_RunJavaScript(const char\* webTag, const char\* jsCode, NativeArkWeb\_OnJavaScriptCallback callback)

**Description**

Loads and asynchronously executes a JavaScript code in the current page.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* jsCode | A piece of JavaScript code script. |
| [NativeArkWeb\_OnJavaScriptCallback](#nativearkweb_onjavascriptcallback) callback | Callback for notifying the code execution result. |

#### \[h2\]OH\_NativeArkWeb\_RegisterJavaScriptProxy()

void OH\_NativeArkWeb\_RegisterJavaScriptProxy(const char\* webTag, const char\* objName, const char\*\* methodList,NativeArkWeb\_OnJavaScriptProxyCallback\* callback, int32\_t size, bool needRefresh)

**Description**

Displays the list of registered objects and function names.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* objName | Name of the registered object. |
| const char\*\* methodList | Name of the registered method list. |
| [NativeArkWeb\_OnJavaScriptProxyCallback](#nativearkweb_onjavascriptproxycallback)\* callback | Registered callback. |
| int32\_t size | Number of registered callbacks. |
| bool needRefresh | Whether a page need to be refreshed. The value **true** indicates that the page needs to be refreshed, and **false** indicates the opposite. |

#### \[h2\]OH\_NativeArkWeb\_UnregisterJavaScriptProxy()

void OH\_NativeArkWeb\_UnregisterJavaScriptProxy(const char\* webTag, const char\* objName)

**Description**

Deletes a registered object and its callback.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* objName | Name of the registered object. |

#### \[h2\]OH\_NativeArkWeb\_SetJavaScriptProxyValidCallback()

void OH\_NativeArkWeb\_SetJavaScriptProxyValidCallback(const char\* webTag, NativeArkWeb\_OnValidCallback callback)

**Description**

Sets a callback used when an object is valid.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| [NativeArkWeb\_OnValidCallback](#nativearkweb_onvalidcallback) callback | Callback used when an object is valid. |

#### \[h2\]OH\_NativeArkWeb\_GetJavaScriptProxyValidCallback()

NativeArkWeb\_OnValidCallback OH\_NativeArkWeb\_GetJavaScriptProxyValidCallback(const char\* webTag)

**Description**

Obtains the callback used when a registered object is valid.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NativeArkWeb\_OnValidCallback](#nativearkweb_onvalidcallback) | Callback used when a registered object is valid. If no valid callback function is set for the **webTag** parameter, a null pointer is returned. |

#### \[h2\]OH\_NativeArkWeb\_SetDestroyCallback()

void OH\_NativeArkWeb\_SetDestroyCallback(const char\* webTag, NativeArkWeb\_OnDestroyCallback callback)

**Description**

Sets a callback used when a component is destroyed.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| [NativeArkWeb\_OnDestroyCallback](#nativearkweb_ondestroycallback) callback | Callback used when a component is destroyed. |

#### \[h2\]OH\_NativeArkWeb\_GetDestroyCallback()

NativeArkWeb\_OnDestroyCallback OH\_NativeArkWeb\_GetDestroyCallback(const char\* webTag)

**Description**

Obtains the callback used when a registered component is destroyed.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NativeArkWeb\_OnDestroyCallback](#nativearkweb_ondestroycallback) | Callback used when a registered component is destroyed. If no destroy callback function is set for the **webTag** parameter, a null pointer is returned. |

#### \[h2\]OH\_NativeArkWeb\_LoadData()

ArkWeb\_ErrorCode OH\_NativeArkWeb\_LoadData(const char\* webTag,const char\* data,const char\* mimeType,const char\* encoding,const char\* baseUrl,const char\* historyUrl)

**Description**

Loads data or URLs. This function must be called in the main thread.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* data | String being base64 or URL encoded, which cannot be empty. |
| const char\* mimeType | Media type, such as **text/html**, which cannot be empty. |
| const char\* encoding | Encoding type, such as **UTF-8**, which cannot be empty. |
| const char\* baseUrl | URL (HTTP/HTTPS/Data), which is assigned by the **Web** component to **window.origin**. |
| const char\* historyUrl | Historical URL. If this parameter is not empty, it can be managed in historical records to implement backward and forward navigation. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode](../arkweb-error-code-h/document.md#arkweb_errorcode) | 
Error codes of **LoadData**.

[ARKWEB\_SUCCESS](../arkweb-error-code-h/document.md#arkweb_errorcode): The data is successfully loaded.

[ARKWEB\_INVALID\_PARAM](../arkweb-error-code-h/document.md#arkweb_errorcode): The mandatory parameter is not specified, the parameter type is incorrect, or the parameter verification fails.

[ARKWEB\_INIT\_ERROR](../arkweb-error-code-h/document.md#arkweb_errorcode): The initialization failed because no valid **Web** component is found based on the input **webTag**.

[ARKWEB\_LIBRARY\_OPEN\_FAILURE](../arkweb-error-code-h/document.md#arkweb_errorcode): Failed to open the dynamic link library.

[ARKWEB\_LIBRARY\_SYMBOL\_NOT\_FOUND](../arkweb-error-code-h/document.md#arkweb_errorcode): The required symbol is not found in the dynamic link library.

 |

#### \[h2\]OH\_NativeArkWeb\_RegisterAsyncThreadJavaScriptProxy()

void OH\_NativeArkWeb\_RegisterAsyncThreadJavaScriptProxy(const char\* webTag,const ArkWeb\_ProxyObjectWithResult\* proxyObject, const char\* permission)

**Description**

Registers a JavaScript object that contains callback methods, which can have return values. This object will be registered into all frames of the current page, including all iframes, and can be accessed by using the name specified in **ArkWeb\_ProxyObjectWithResult**. The object takes effect in JavaScript only after the page is loaded or reloaded next time. Its methods are executed in the worker thread of ArkWeb.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const [ArkWeb\_ProxyObjectWithResult](../../structs/arkweb-proxyobjectwithresult/document.md)\* proxyObject | Object to be registered. |
| const char\* permission | A JSON string used to configure the object and method levels of the JSBridge permission. This value is empty by default. |

#### \[h2\]OH\_ArkWebCookieManager\_SaveCookieSync()

ArkWeb\_ErrorCode OH\_ArkWebCookieManager\_SaveCookieSync()

**Description**

Saves all cookies that can be accessed through the **CookieManager** API to disks. To use this API in a non-UI thread, you need to use **OH\_ArkWeb\_GetNativeAPI** to initialize the **CookieManager** API.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode](../arkweb-error-code-h/document.md#arkweb_errorcode) | 
Error codes of **SaveCookieSync**.

[ARKWEB\_SUCCESS](../arkweb-error-code-h/document.md#arkweb_errorcode): The cookie is successfully saved.

[ARKWEB\_COOKIE\_SAVE\_FAILED](../arkweb-error-code-h/document.md#arkweb_errorcode): Failed to save the cookie.

[ARKWEB\_COOKIE\_MANAGER\_INITIALIZE\_FAILED](../arkweb-error-code-h/document.md#arkweb_errorcode): The **CookieManager** initialization failed.

[ARKWEB\_COOKIE\_MANAGER\_NOT\_INITIALIZED](../arkweb-error-code-h/document.md#arkweb_errorcode): This API cannot be invoked in a non-UI thread without initializing the **CookieManager** API. You need to use **OH\_ArkWeb\_GetNativeAPI** to initialize the **CookieManager** API first.

 |

#### \[h2\]OH\_ArkWebCookieManager\_SaveCookieAsync()

void OH\_ArkWebCookieManager\_SaveCookieAsync(OH\_ArkWeb\_OnCookieSaveCallback callback)

**Description**

Saves all cookies that can be accessed through the **CookieManager** API to disks. If the **CookieManager** API is not initialized, this API is automatically executed on the UI thread.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkWeb\_OnCookieSaveCallback](#oh_arkweb_oncookiesavecallback)\* callback | Callback triggered when cookies are saved. |

#### \[h2\]OH\_NativeArkWeb\_GetBlanklessInfoWithKey()

ArkWeb\_BlanklessInfo OH\_NativeArkWeb\_GetBlanklessInfoWithKey(const char\* webTag, const char\* key)

**Description**

Obtains the first screen loading prediction information, and starts to generate the loading transition frame. The application determines whether to enable blankless loading based on the information. For details, see [ArkWeb\_BlanklessInfo](../../structs/arkweb-blanklessinfo/document.md). This API must be used together with the [OH\_NativeArkWeb\_SetBlanklessLoadingWithKey](#oh_nativearkweb_setblanklessloadingwithkey) API and must be called before the page loading API is triggered and after **WebViewController** is bound to the **Web** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/wxC32MwxQSmOv4IYpVULOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66A71B9C17FD630FB9D8670CACCC3E4168F65A66C6C3E21ACD9BCA31F85C1C3F)

-   The default size of the persistent cache capacity is 30 MB (about 30 pages). You can set the cache capacity by calling [OH\_NativeArkWeb\_SetBlanklessLoadingCacheCapacity](#oh_nativearkweb_setblanklessloadingcachecapacity). For details, see the description of this API. When the maximum capacity is exceeded, the cache is updated based on the Least Recently Used (LRU) mechanism. The persistent cache data that has been stored for more than seven days is automatically cleared. After the cache is cleared, the optimization effect appears when the page is loaded for the third time.
-   If the value of **similarity** in [ArkWeb\_BlanklessInfo](../../structs/arkweb-blanklessinfo/document.md) is extremely low, check whether the key value is correctly passed.
-   After this API is called, page loading snapshot detection and transition frame generation calculation are enabled, which generates certain resource overhead.
-   Blankless loading consumes resources, which depends on the resolution of the **Web** component. It is assumed that a width and a height of the resolution are respectively **w** and **h**. When a page is opened, the peak memory usage increases by about **12×w×h** B. After the page is opened, the memory is reclaimed, which does not affect the stable memory usage. When the size of the solid-state application cache is increased, the increased cache of each page is about **w×h/10** B and the cache is located in the application cache.

**Required permissions**: **ohos.permission.INTERNET** and **ohos.permission.GET\_NETWORK\_INFO**

**Since**: 20

**Device behavior differences**: This API can be called on phones. For other device types, error code **801** is returned.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* key | 
Key value that uniquely identifies the page.

The value cannot be empty and can contain a maximum of 2048 characters.

Invalid values do not take effect.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_BlanklessInfo](../../structs/arkweb-blanklessinfo/document.md) | Prediction information about blankless loading, including the first screen similarity and first screen loading duration. The application determines whether to enable blankless loading based on the prediction information. |

#### \[h2\]OH\_NativeArkWeb\_SetBlanklessLoadingWithKey()

ArkWeb\_BlanklessErrorCode OH\_NativeArkWeb\_SetBlanklessLoadingWithKey(const char\* webTag, const char\* key, bool isStarted)

**Description**

Sets whether to enable blankless loading. This API must be used together with the [OH\_NativeArkWeb\_GetBlanklessInfoWithKey](#oh_nativearkweb_getblanklessinfowithkey) API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Q1FLFXNsQumEXEyNEWrXow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B36480C57E81FA3FBCBA8F4449A3C7A8F8E57178C59C37B728C409B9D7B3BC8)

-   This API must be called after the page loading API is triggered. Other constraints are the same as those of [OH\_NativeArkWeb\_GetBlanklessInfoWithKey](#oh_nativearkweb_getblanklessinfowithkey).
-   The page must be loaded in the component that calls this set of APIs.
-   When the similarity is low, the system will deem the scene change too abrupt and frame insertion will fail.

**Required permissions**: **ohos.permission.INTERNET** and **ohos.permission.GET\_NETWORK\_INFO**

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| const char\* key | 
Key value that uniquely identifies the page. The value must be the same as the key value of the [OH\_NativeArkWeb\_GetBlanklessInfoWithKey](#oh_nativearkweb_getblanklessinfowithkey) API.

The value cannot be empty and can contain a maximum of 2048 characters.

When an invalid value is set, the error code [ArkWeb\_BlanklessErrorCode](../arkweb-error-code-h/document.md#arkweb_blanklesserrorcode) is returned and the frame insertion does not take effect.

 |
| bool isStarted | 

Whether to enable frame insertion. The value **true** indicates to enable frame insertion, and **false** indicates the opposite.

The default value is **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_BlanklessErrorCode](../arkweb-error-code-h/document.md#arkweb_blanklesserrorcode) | Whether the API is successfully called. For details, see [ArkWeb\_BlanklessErrorCode](../arkweb-error-code-h/document.md#arkweb_blanklesserrorcode). |

#### \[h2\]OH\_NativeArkWeb\_ClearBlanklessLoadingCache()

void OH\_NativeArkWeb\_ClearBlanklessLoadingCache(const char\* key\[\], uint32\_t size)

**Description**

Clears the blankless loading cache of the page with a specified key value.

In an applet or web application, when the content changes significantly during page loading, an obvious scene change may occur. If you are concerned about this change, you can use this API to clear the page cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/LjFjjrV6SlWkV7ZdQk2MPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A1F9621C091C64375DB187F378681CC2F6BA814E43144212AA5E231F622198B)

-   After the page is cleared, the optimization effect appears when the page is loaded for the third time.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* key\[\] | 
Key value list on the pages using the blankless optimization solution. The key value has been specified in [OH\_NativeArkWeb\_GetBlanklessInfoWithKey](#oh_nativearkweb_getblanklessinfowithkey).

Default value: key value list of all pages cached by the blankless optimization solution.

The key length cannot exceed 2048 characters, and the number of keys must be less than or equal to 100. The key value is the same as that input to the **Web** component during page loading.

If the key length exceeds 2048 characters, the key does not take effect. If the key length exceeds 100 characters, the first 100 characters are used. If the key length is NULL, the default value is used.

 |
| uint32\_t size | 

Size of the key array.

The default value is **0**.

The value ranges from 0 to 100. If the size exceeds 100, the first 100 keys are used.

When an invalid value is set, the value **0** is used.

 |

#### \[h2\]OH\_NativeArkWeb\_SetBlanklessLoadingCacheCapacity()

uint32\_t OH\_NativeArkWeb\_SetBlanklessLoadingCacheCapacity(uint32\_t capacity)

**Description**

Sets the persistent cache capacity of the blankless loading solution and returns the value that takes effect. The default cache capacity is 30 MB, and the maximum cache capacity is 100 MB. When this limit is exceeded, transition frames that are not frequently used are eliminated.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t capacity | 
Persistent cache capacity, in MB. The maximum value is 100 MB.

The default value is 30 MB.

The value ranges from 0 to 100. If this parameter is set to **0**, no cache capacity is available and the functionality is disabled globally.

When a value less than 0 is set, the value **0** takes effect. When a value greater than 100 is set, the value **100** takes effect.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | 
The effective value that ranges from 0 MB to 100 MB.

When a value less than 0 is set, the value **0** takes effect. When a value greater than 100 is set, the value **100** takes effect.

 |

#### \[h2\]OH\_NativeArkWeb\_SetActiveWebEngineVersion()

void OH\_NativeArkWeb\_SetActiveWebEngineVersion(ArkWebEngineVersion webEngineVersion)

**Description**

Sets the ArkWeb kernel version. If the system does not support the specified version, the setting is invalid.

This API is a global static method and must be called before **initializeWebEngine** is called. If any **Web** component has been loaded, the setting of this API is invalid.

**Legacy kernel adaptation**

Since HarmonyOS 6.0, some ArkWeb APIs do not take effect when the legacy kernel is used. For details, see [Adaptation Guide for the M114 Kernel on HarmonyOS 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| ArkWebEngineVersion webEngineVersion | ArkWeb kernel version. For details, see [ArkWebEngineVersion](#arkwebengineversion). |

#### \[h2\]OH\_NativeArkWeb\_GetActiveWebEngineVersion()

ArkWebEngineVersion OH\_NativeArkWeb\_GetActiveWebEngineVersion()

**Description**

Obtains the current ArkWeb kernel version.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| ArkWebEngineVersion | The current ArkWeb kernel version defined by [ArkWebEngineVersion](#arkwebengineversion). |

#### \[h2\]OH\_NativeArkWeb\_LazyInitializeWebEngineInCookieManager()

void OH\_NativeArkWeb\_LazyInitializeWebEngineInCookieManager(bool lazy)

**Description**

Sets whether to delay the initialization of the ArkWeb kernel. If this method is not called, the ArkWeb kernel is not delayed by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/d9APnWZNQSG1kI8elOHeAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFE46FD683705F603054332947AC83E14B6CEC69766EFA45DBC91C3902B9284E)

-   This API is a global static method and must be called before the **Web** component is used and the ArkWeb kernel is initialized. Otherwise, the setting is invalid.
-   This API is applicable only to APIs that initialize the CookieManager after being called, for example, the [ArkWeb\_CookieManagerAPI](../../structs/arkweb-cookiemanagerapi/document.md) APIs. When this API is called, the ArkWeb kernel is not initialized during the initialization of CookieManager. You need to initialize the ArkWeb kernel later.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| bool lazy | Whether to delay the initialization of the ArkWeb kernel. The value **true** means to delay the initialization, and **false** means the opposite. |
