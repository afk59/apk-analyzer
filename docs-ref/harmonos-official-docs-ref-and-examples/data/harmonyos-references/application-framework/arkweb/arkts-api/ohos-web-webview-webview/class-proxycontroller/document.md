# Class (ProxyController)

Implements a **ProxyController** object to set a proxy for an application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/_vRa2vkWTo-6XvoY_C0kHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A6DB7BF311720946C6A2FBD4BA5C3C5A9F810C938746132F2AA325257F209E8)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 15.
    
-   The sample effect is subject to the actual device.
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### applyProxyOverride15+

static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void

Sets the proxy used by all web pages in an application. URLs that match the bypass rule inserted through [insertBypassRule](../class-proxyconfig/document.md#insertbypassrule15) do not use the proxy. Instead, their requests are directly sent to the source addresses specified by the URLs. The new proxy may not be used immediately after the network is connected. Before loading the page, wait for the listener to be triggered in the UI thread.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| proxyConfig | [ProxyConfig](../class-proxyconfig/document.md) | Yes | Configuration of the proxy. |
| callback | [OnProxyConfigChangeCallback](../types/document.md#onproxyconfigchangecallback15) | Yes | Callback used when the proxy is successfully set. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

For details about the sample code, see [removeProxyOverride](#removeproxyoverride15).

#### removeProxyOverride15+

static removeProxyOverride(callback: OnProxyConfigChangeCallback): void

Removes the proxy configuration. The new proxy may not be used immediately after the network is connected. Before loading the page, wait for the listener to be triggered in the UI thread.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnProxyConfigChangeCallback](../types/document.md#onproxyconfigchangecallback15) | Yes | Callback used when the proxy is successfully set. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  proxyRules: webview.ProxyRule\[\] = \[\];

  build() {
    Row() {
      Column() {
        Button("applyProxyOverride").onClick(()=>{
          let proxyConfig:webview.ProxyConfig = new webview.ProxyConfig();
          // The first proxy configuration https://proxy.XXX.com is preferentially used.
          // When the proxy fails, insertDirectRule is used.
          try {
            proxyConfig.insertProxyRule("https://proxy.XXX.com", webview.ProxySchemeFilter.MATCH\_ALL\_SCHEMES);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
          try {
            proxyConfig.insertDirectRule(webview.ProxySchemeFilter.MATCH\_HTTP);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
          try {
            proxyConfig.insertBypassRule("\*.example.com");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
          proxyConfig.clearImplicitRules();
          proxyConfig.bypassHostnamesWithoutPeriod();
          try {
            proxyConfig.enableReverseBypass(true);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
          let bypassRules = proxyConfig.getBypassRules();
          for (let i = 0; i < bypassRules.length; i++) {
            console.info("bypassRules: " + bypassRules\[i\]);
          }
          this.proxyRules = proxyConfig.getProxyRules();
          for (let i = 0; i < this.proxyRules.length; i++) {
            console.info("SchemeFilter: " + this.proxyRules\[i\].getSchemeFilter());
            console.info("Url: " + this.proxyRules\[i\].getUrl());
          }
          let isReverseBypassRule = proxyConfig.isReverseBypassEnabled();
          console.info("isReverseBypassRules: " + isReverseBypassRule);
          try {
            webview.ProxyController.applyProxyOverride(proxyConfig, () => {
              console.info("PROXYCONTROLLER proxy changed");
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
        Button("loadUrl-https").onClick(()=>{
          this.controller.loadUrl("https://www.example.com")
        })
        Button("loadUrl-http").onClick(()=>{
          this.controller.loadUrl("http://www.example.com")
        })
        Button("removeProxyOverride").onClick(()=>{
          try {
          webview.ProxyController.removeProxyOverride(() => {
            console.info("PROXYCONTROLLER proxy changed");
          });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
        Web({ src: 'www.example.com', controller: this.controller})
      }
      .width('100%')
    }
    .height('100%')
  }
}
