# Class (ProxyRule)

Implements a **ProxyRule** object used in [insertProxyRule](../class-proxyconfig/document.md#insertproxyrule15).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/WyVPKi_RSmeHpSfN2N9Exw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2958369F40E8DF31BAB305706AE0B343439F653352F9941B67782E287DFD0186)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 15.
    
-   The sample effect is subject to the actual device.
    

#### getSchemeFilter15+

getSchemeFilter(): ProxySchemeFilter

Obtains the **ProxySchemeFilter** information in the proxy rule.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ProxySchemeFilter](../enums/document.md#proxyschemefilter15) | **ProxySchemeFilter** in the proxy rule. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### getUrl15+

getUrl(): string

Obtains the URL specified in the proxy rule.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL specified in the proxy rule. |

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).
