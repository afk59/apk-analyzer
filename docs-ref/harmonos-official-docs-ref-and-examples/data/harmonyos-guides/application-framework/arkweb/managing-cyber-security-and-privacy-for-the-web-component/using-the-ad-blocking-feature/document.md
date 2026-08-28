# Using the Ad Blocking Feature

ArkWeb provides the ad blocking feature for applications, supporting default EasyList rules pushed by the cloud and custom rule files set by applications through APIs. It can intercept the advertisement resource download at the network layer or inject CSS rules into the web page to hide specific advertisement elements.

The current configuration file format uses [EasyList](https://easylist-downloads.adblockplus.org/easylist.txt).

#### Common EasyList Rules

| Type | Description | Example |
| :-- | :-- | :-- |
| URL blocking rule | Blocks all sub-resource requests whose URLs match **example.com/js/\*\_tv.js**. This rule is used to block a specified domain name and all its subdomain names. | ||example.com/js/\*\_tv.js |
| URL blocking rule | Blocks third-party resources whose URLs match **alimama.cn** on websites whose domain names are neither **alimama.com** nor **taobao.com**. **$third\_party** is an options syntax used to match third-party resources. A tilde (~) before a domain name indicates that the domain name is not included. | ||alimama.cn^$third-party,domain=~alimama.com|~taobao.com |
| Exception rule | Disables ad blocking on **example.com**. **@@** is the syntax keyword that indicates no blocking. | @@||example.com^$document |
| Exception rule | Disables the blocking of sub-resources that match **.adserver** in the web page whose domain name is **litv.tv**. | @@.adserver.$domain=litv.tv |
| Element hiding rule | Hides all elements whose class is **i528** in the web page whose domain name is **myabandonware.com** or **myware.com**. **##** is used to hide an element. | myabandonware.com, myware.com##.i528 |
| Element hiding exception rule | Disables the hiding of elements whose IDs are **ad\_1** in **sdf-event.sakura.ne.jp**. | sdf-event.sakura.ne.jp#@##ad\_1 |

Exception rules are usually used together with common rules. In some specific scenarios, common rules are not applicable, and exception rules do not have effects.

For example, if you configure a blocking rule **||abc.com/js/123.js** to block websites, but some websites are blocked by mistake or cannot be blocked, you can configure exception rules for these websites.

#### Constraints

-   In the [WebviewController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller) class, the [enableAdsBlock()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#enableadsblock12) API is added for enabling or disabling the ad blocking feature at the web instance level.
    
-   The [AdsBlockManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager) global singleton class is added to provide the capabilities of customizing ad blocking configurations and controlling website-level features.
    
-   The web instance provides [onAdsBlocked()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#onadsblocked12) callback to notify the upper-layer application of the interception information.
    
-   Only one custom configuration can be set by the [setAdsBlockRules()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#setadsblockrules12) API of [AdsBlockManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager). The configuration is persistent and does not need to be reconfigured during cold start of the application. This prevents the compilation and parsing of the ad blocking rule from being triggered again.
    
-   The data operated by the [addAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#addadsblockdisallowedlist12), [removeAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#removeadsblockdisallowedlist12), [clearAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#clearadsblockdisallowedlist12), [addAdsBlockAllowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#addadsblockallowedlist12), [removeAdsBlockAllowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#removeadsblockallowedlist12) and [clearAdsBlockAllowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#clearadsblockallowedlist12) APIs of the [AdsBlockManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager) API is not persistent. The data needs to be reset during cold start of the application.
    
-   If the ad blocking feature is enabled for a web instance but the [addAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#addadsblockdisallowedlist12), [removeAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#removeadsblockdisallowedlist12), [clearAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#clearadsblockdisallowedlist12), [addAdsBlockAllowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#addadsblockallowedlist12), [removeAdsBlockAllowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#removeadsblockallowedlist12), and [clearAdsBlockAllowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#clearadsblockallowedlist12) APIs of the [AdsBlockManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager) API are not called to set disallowlist and allowlist, the ad blocking feature is enabled for all websites.
    
-   When both allowlist and disallowlist are used, allowlist has a higher priority than disallowlist. That is, allowlist is used for matching first. If the matching is successful, disallowlist is not used, and the ad blocking feature is enabled for the website.
    
-   If the ad blocking feature is not enabled for the application, the **Web** component does not request the default built-in EasyList file from the server.
    
-   The disallowlist and allowlist use suffix matching. For example, if the domain name of an application is **xxyy.com**, the website whose URL is **wwsstt.xxyy.com** can be matched.
    

#### Application Scenarios

## Enabling Ad Blocking

You can use [setAdsBlockRules()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#setadsblockrules12) provided by **AdsBlockManager** to set blocking rules in EasyList and use [enableAdsBlock()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#enableadsblock12) of the **Web** component to enable the ad blocking feature.

The following example shows how to select the EasyList file using the file picker and how to enable the ad blocking feature in an application.

import { webview } from '@kit.ArkWeb';
import { picker, fileUri } from '@kit.CoreFileKit';

// This example demonstrates how to click a button to open the EasyList using file picker and set the file in the Web component.
@Entry
@Component
struct WebComponent {
  main\_url: string = 'https://www.example.com';
  controller: webview.WebviewController = new webview.WebviewController();

  @State input\_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          Button({type: ButtonType.Capsule}) {
            Text('setAdsBlockRules')
          }
          .onClick(() => {
            try {
              let documentSelectionOptions: ESObject = new picker.DocumentSelectOptions();
              let documentPicker: ESObject = new picker.DocumentViewPicker();
              documentPicker.select(documentSelectionOptions).then((documentSelectResult: ESObject) => {
                if (documentSelectResult && documentSelectResult.length > 0) {
                  let fileRealPath = new fileUri.FileUri(documentSelectResult\[0\]);
                  console.info('DocumentViewPicker.select successfully, uri: ' + fileRealPath);
                  webview.AdsBlockManager.setAdsBlockRules(fileRealPath.path, true);
                }
              })
            } catch (err) {
              console.error('DocumentViewPicker.select failed with err:' + err);
            }
          })
        }
      }
      Web({ src: this.main\_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true);
        })
    }
  }
}

When the component has a built-in EasyList, you can set the **replace** parameter of the [setAdsBlockRules()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#setadsblockrules12) API to disable the built-in EasyList. When the **replace** parameter is set to **false**, the built-in and custom rules work at the same time. If the built-in rules conflict with the custom rules, set the **replace** parameter to **true**.

The custom rule file is a global configuration file for the application that it takes effect for all **Web** components in the application processes. In addition, the file is persistent that it continues to work when the application is restarted.

## Disabling Ad Blocking on Pages with Specific Domain Names

When the ad blocking feature of a **Web** component is enabled, in addition to the custom EasyList, you can also use [addAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#addadsblockdisallowedlist12) provided by **AdsBlockManager** to disable the ad blocking feature.

import { webview } from '@kit.ArkWeb';

// This example demonstrates how to click a button to add an array of domain names to the disallowed list.
@Entry
@Component
struct WebComponent {
  main\_url: string = 'https://www.example.com';
  text\_input\_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();

  @State input\_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input\_text, placeholder: this.main\_url, controller: this.text\_input\_controller})
            .id('input\_url')
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text('Go') }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text('addAdsBlockDisallowedList') }
          .onClick(() => {
            let arrDomainSuffixes = new Array<string>();
            arrDomainSuffixes.push('example.com');
            arrDomainSuffixes.push('abcdefg.cn');
            webview.AdsBlockManager.addAdsBlockDisallowedList(arrDomainSuffixes);
          })
        }
      }
      Web({ src: this.main\_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true);
        })
    }
  }
}

Add the domain name to **DisallowedList** of **AdsBlockManager** through [addAdsBlockDisallowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#addadsblockdisallowedlist12). When the page is loaded, the system matches the suffix of the web page URL with the domain name in **DisallowedList**. If the matching is successful, the system does not block ads on the page. In addition, [addAdsBlockAllowedList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-adsblockmanager#addadsblockallowedlist12) is provided to be used with **DisallowedList()** to set domain names and determine whether to enable ad blocking.

**AdsBlockManager** caches two lists of domain names, including **DisallowedList** and **AllowList**. **DisallowedList** is used to disable ad blocking on web pages, and **AllowList** is used to enable ad blocking disabled by **DisallowedList**. **AllowList** has a higher priority. When a web page is loaded, the system matches the web page URL with **AllowList**. If the matching is successful, the ad blocking feature is enabled. Otherwise, the system continues to match the web page URL with **DisallowedList**. If the matching is successful, the ad blocking feature is disabled. If the accessed web page is neither list in **AllowList** nor in **DisallowedList**, the ad blocking feature for this web page is enabled by default.

For example, if you want to enable ad blocking for **news.example.com** and **sport.example.com** in an application, but not for other web pages under the **example.com** domain, you can use **addAdsBlockDisallowedList()** to add **example.com** to **DisallowedList**, and then use **addAdsBlockAllowedList()** to add **news.example.com** and **sport.example.com** to **AllowedList**.

import { webview } from '@kit.ArkWeb';

// In the following example, \*\*addAdsBlockAllowedList()\*\* and \*\*addAdsBlockDisallowedList()\*\* are used together to set the ad blocking feature for web pages.
@Entry
@Component
struct WebComponent {
  main\_url: string = 'https://www.example.com';
  text\_input\_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();

  @State input\_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input\_text, placeholder: this.main\_url, controller: this.text\_input\_controller})
            .id('input\_url')
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text('Go') }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text('addAdsBlockAllowedList') }
          .onClick(() => {
            let arrDisallowDomainSuffixes = new Array<string>();
            arrDisallowDomainSuffixes.push('example.com');
            webview.AdsBlockManager.addAdsBlockDisallowedList(arrDisallowDomainSuffixes);

            let arrAllowedDomainSuffixes = new Array<string>();
            arrAllowedDomainSuffixes.push('news.example.com');
            arrAllowedDomainSuffixes.push('sport.example.com');
            webview.AdsBlockManager.addAdsBlockAllowedList(arrAllowedDomainSuffixes);
          })
        }
      }
      Web({ src: this.main\_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true);
        })
    }
  }
}

Note that the **DisallowedList** and **AllowedList** of the **AdsBlockManager** are not persisted. Therefore, the lists are reset to empty when the application is restarted.

If the ad blocking feature of the **Web** component is not enabled through [enableAdsBlock()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#enableadsblock12), the preceding APIs do not take effect in the **Web** component.

## Collecting Ad Blocking Information

When ad blocking is enabled on the **Web** component, if any ad is blocked on the accessed web page, the [onAdsBlocked()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#onadsblocked12) callback of the **Web** component notifies the application. You can collect blocking information and statistics as needed.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State totalAdsBlockCounts: number = 0;

  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
        .onAdsBlocked((details: AdsBlockedDetails) => {
          if (details) {
            console.info(' Blocked ' + details.adsBlocked.length + ' in ' + details.url);
            let adList: Array<string> = Array.from(new Set(details.adsBlocked));
            this.totalAdsBlockCounts += adList.length;
            console.info('Total blocked counts :' + this.totalAdsBlockCounts);
          }
        })
    }
  }
}

To reduce the frequency of notifications and minimize the impact on the page loading process, only the first notification is made when the page is fully loaded. Subsequent blocking events are reported at intervals of 1 second, and no notifications are sent if there is no ads blocked.
