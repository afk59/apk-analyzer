# Class (AdsBlockManager)

Implements an **AdsBlockManager** instance to set custom ad blocking configurations in the **Web** components and disable the ad blocking feature for specific websites. Each application's **Web** components share an **AdsBlockManager** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/LvKVqqlGTXSMDAWEFYFPHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=442B05F6E1C13716A3874283E399F9C35F2F50A9F351653A7FA0C28B20468FD6)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    
-   Static methods must be used on the user interface (UI) thread.
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### setAdsBlockRules12+

static setAdsBlockRules(rulesFile: string, replace: boolean): void

Sets a custom ad blocking rule file that conforms to the universal EasyList syntax in the **Web** components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/f4CEyrUSTE2sEj3ud-RRrw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9526144944275332A1DAD84BEAD0E26CC6D5908DF2ABF924B6E3C6AB6AF91A94)

The ad blocking rules set by this API will be persistently stored after successful internal parsing; you do not need to set them again after the application is restarted.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rulesFile | string | Yes | Path to the rule file that conforms to the universal EasyList syntax. The application needs to have read permission for this file. |
| replace | boolean | Yes | Whether to replace the built-in default rules. The value **true** indicates that the built-in default rules will be forcibly replaced; **false** indicates that the custom rules will work alongside the built-in default rules. |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/K1dDcalYQgSVYXPrrKX6Mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F1231A3945D68307A8046BA361A704EB3BB2904758D521B487825ECEBC6EF9D)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { picker, fileUri } from '@kit.CoreFileKit';

// This example demonstrates how to click a button to open an EasyList-compliant rule file through filepicker and set the file in the Web component.
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Flex() {
        Button({ type: ButtonType.Capsule }) {
          Text("setAdsBlockRules")
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
  }
}

#### addAdsBlockDisallowedList12+

static addAdsBlockDisallowedList(domainSuffixes: Array<string>): void

Adds an array of domain names to the disallowed list of this **AdsBlockManager** object. When the ad blocking feature is enabled, ad blocking for these websites will be disabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/f4WFPcN9TpKac6BFywVIoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2AD0DED24051840B957388D4E85A22801AD7F5B685E3C1B9575FA82B6AC01A0)

The domain name set by this API is not persistent; they need to be set again after the application is restarted.

The ad blocking feature matches website URLs based on the suffix. For example, if the disallowed list contains **'example.com'** or **'[www.example.com](http://www.example.com)'**, then ad blocking will be disabled for sites **[https://www.example.com](https://www.example.com)** and **[https://m.example.com](https://m.example.com)**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainSuffixes | Array<string> | Yes | Array of domain names, for example, \['example.com', 'abcd.efg.com'\]. |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/LarIvMcJRF6XibE0pKDq6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=916FFBCA2C87530FD49CBCBCE3070915D5973DEA9FB63219A9DB8340DF26A092)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
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
            .id("input\_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text("addAdsBlockDisallowedList") }
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

#### removeAdsBlockDisallowedList12+

static removeAdsBlockDisallowedList(domainSuffixes: Array<string>): void

Removes an array of domain names from the disallowed list of this **AdsBlockManager** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/COVcQuSjRIaBi-Pr9f4Log/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBB0E97F8C6F95B4998C16A39664E2AB9C98987E658376CF74D22C363C864709)

The domain name set by this API is not persistent; they need to be set again after the application is restarted. Removing an entry that does not exist does not trigger an exception.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainSuffixes | Array<string> | Yes | Array of domain names, for example, \['example.com', 'abcd.efg.com'\]. |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/5B78Yv9YTbCoKeXGW7p-qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=679E06D8A582BD7FB0BD620784FAB797A3907576A558FB5AE89DF41D8D37B545)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

// This example demonstrates how to click a button to remove an array of domain names from the disallowed list.
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
            .id("input\_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text("removeAdsBlockDisallowedList") }
          .onClick(() => {
            let arrDomainSuffixes = new Array<string>();
            arrDomainSuffixes.push('example.com');
            arrDomainSuffixes.push('abcdefg.cn');
            webview.AdsBlockManager.removeAdsBlockDisallowedList(arrDomainSuffixes);
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

#### clearAdsBlockDisallowedList12+

static clearAdsBlockDisallowedList(): void

Clears the disallowed list of this **AdsBlockManager** object.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/N1abvp1oQDmDEYpgvnmG-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF2F296C366076F4A5FDEA5EE0A3B677CAE3A650310D0C64198723F0D6EC4B5C)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

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
            .id("input\_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text("clearAdsBlockDisallowedList") }
          .onClick(() => {
            webview.AdsBlockManager.clearAdsBlockDisallowedList();
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

#### addAdsBlockAllowedList12+

static addAdsBlockAllowedList(domainSuffixes: Array<string>): void

Adds an array of domain names to the allowed list of this **AdsBlockManager** object. This API is typically used to re-enable ad blocking for certain websites that were previously added to the disallowed list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/hpeUFqYWRdC7E8hb4kmulQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B57B5C24806EC033A2FB8FEA3A095275E47AA8A8B69D1228C3E4CEDC8789627)

The domain name set by this API is not persistent; they need to be set again after the application is restarted.

The priority of the allowed list is higher than that of the disallowed list. For example, if the disallowed list includes **\['example.com'\]**, all pages under the **example.com** domain will have their ad blocking disabled; to re-enable ad blocking for the subdomain **news.example.com**, you can use the **addAdsBlockAllowedList(\['news.example.com'\])** API.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainSuffixes | Array<string> | Yes | Array of domain names, for example, \['example.com', 'abcd.efg.com'\]. |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/gVYJ751YQ6-bTOJHmrFM6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73EA38445A29658686916DCDB29B3D0A2D88830C8FC465F930C6CC05F219ECD6)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
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
            .id("input\_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text("addAdsBlockAllowedList") }
          .onClick(() => {
            let arrDisallowDomainSuffixes = new Array<string>();
            arrDisallowDomainSuffixes.push('example.com');
            webview.AdsBlockManager.addAdsBlockDisallowedList(arrDisallowDomainSuffixes);

            let arrAllowedDomainSuffixes = new Array<string>();
            arrAllowedDomainSuffixes.push('news.example.com');
            webview.AdsBlockManager.addAdsBlockAllowedList(arrAllowedDomainSuffixes);
          })
        }
      }
      Web({ src: this.main\_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true)
        })
    }
  }
}

#### removeAdsBlockAllowedList12+

static removeAdsBlockAllowedList(domainSuffixes: Array<string>): void

Removes an array of domain names from the allowed list of this **AdsBlockManager** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Q2Cz3AvCRJGDIoPC8od1Ig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57DE94FBE11DD6760E14FE419A08E308C7AEA620CB0774F2BA9D77CF85568C3E)

The domain name set by this API is not persistent; they need to be set again after the application is restarted. Removing an entry that does not exist does not trigger an exception.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainSuffixes | Array<string> | Yes | Array of domain names, for example, \['example.com', 'abcd.efg.com'\]. |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/O0QOboWmT7GgJ7JhC6ZGsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B7496458BEC39A5EA287A0FF5DD2530CDBFEA3B29376F2EEDA86533417EFA5E)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

// This example demonstrates how to click a button to remove an array of domain names from the allowed list.
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
            .id("input\_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text("removeAdsBlockAllowedList") }
          .onClick(() => {
            let arrDomainSuffixes = new Array<string>();
            arrDomainSuffixes.push('example.com');
            arrDomainSuffixes.push('abcdefg.cn');
            webview.AdsBlockManager.removeAdsBlockAllowedList(arrDomainSuffixes);
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

#### clearAdsBlockAllowedList12+

static clearAdsBlockAllowedList(): void

Clears the allowed list of this **AdsBlockManager** object.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/_cAFPNawSHKIRGIO32zC4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=594BC83E70D99F8106930A0585FD068326840938F714A3E850588EB5EFCD42F3)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

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
            .id("input\_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input\_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input\_text);
          })

          Button({type: ButtonType.Capsule}) { Text("clearAdsBlockAllowedList") }
          .onClick(() => {
            webview.AdsBlockManager.clearAdsBlockAllowedList();
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
