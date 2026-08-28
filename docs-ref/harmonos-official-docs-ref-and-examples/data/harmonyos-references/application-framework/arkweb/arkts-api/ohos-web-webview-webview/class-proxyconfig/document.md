# Class (ProxyConfig)

Implements a **ProxyConfig** object to configure proxies.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/VS1FUTn0REGCos1OtNtz0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=803D9924661B29BA556FFF384D44CB7D297C03D9C9E536FCECA102672D14D3B4)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 15.
    
-   The sample effect is subject to the actual device.
    

#### insertProxyRule15+

insertProxyRule(proxyRule: string, schemeFilter?: ProxySchemeFilter): void

Inserts a proxy rule for URLs matching **schemeFilter**. If **schemeFilter** is empty, all URLs use the specified proxy.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| proxyRule | string | Yes | The specified proxy. |
| schemeFilter | [ProxySchemeFilter](../enums/document.md#proxyschemefilter15) | No | 
Filter used to specify URLs that use the proxy.

Default value: **MATCH\_ALL\_SCHEMES**.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### insertDirectRule15+

insertDirectRule(schemeFilter?: ProxySchemeFilter): void

Inserts a proxy rule to specify that URLs matching **schemeFilter** are directly connected to the server.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| schemeFilter | [ProxySchemeFilter](../enums/document.md#proxyschemefilter15) | No | 
Filter used to specify URLs to be directly connected to the server.

Default value: **MATCH\_ALL\_SCHEMES**.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### insertBypassRule15+

insertBypassRule(bypassRule: string): void

Inserts a bypass rule to specify the URLs that should bypass the proxy and directly connect to the server.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bypassRule | string | Yes | Bypass rule used to specify the URLs that should bypass the proxy. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### bypassHostnamesWithoutPeriod15+

bypassHostnamesWithoutPeriod(): void

Specifies that host names without a period should bypass the proxy and directly connect to the server.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### clearImplicitRules15+

clearImplicitRules(): void

Overrides the default behavior and forcibly sends the local host address or local IP address through the proxy. (By default, if host names are local IP addresses or local host addresses, they bypass the proxy.)

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### enableReverseBypass15+

enableReverseBypass(reverse: boolean): void

Reverses the bypass rule.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reverse | boolean | Yes | Whether to reverse the bypass rule. The default value is **false**, indicating the bypass rule set in [insertBypassRule](#insertbypassrule15) is not reversed. The value **true** indicates the opposite. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### getBypassRules15+

getBypassRules(): Array<string>

Obtains the list of URLs that do not use the proxy.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of URLs that do not use the proxy. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### getProxyRules15+

getProxyRules(): Array<ProxyRule>

Obtains proxy rules.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[ProxyRule](../class-proxyrule/document.md)\> | Proxy rules. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### isReverseBypassEnabled15+

isReverseBypassEnabled(): boolean

Obtains the value of [enableReverseBypass](#enablereversebypass15). For details, see [enableReverseBypass](#enablereversebypass15).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Value of [enableReverseBypass](#enablereversebypass15). The default value is **false**, indicating the bypass rule set in [insertBypassRule](#insertbypassrule15) is not reversed. The value **true** indicates the opposite. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).
