# @system.router (Page Routing)

The **Router** module provides APIs to access pages through URIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Phnp42O4TfaeYI20GFzrbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EE9B548DA4785A6220CEFD3855A83D6575772E42232CC1428ADDBCF413A7DE3)

-   The APIs of this module are no longer maintained since API version 8. You are advised to use [@ohos.router](../../ui/ohos-router-page-routing-not-recommended/document.md) instead.
    
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    

#### Modules to Import

import router from '@system.router';

#### router.push

push(options: RouterOptions): void

Navigates to a specified page in the application.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Page routing parameters. For details, see **RouterOptions**. |

**Example**

// Current page
import router from '@system.router';
class A{
  pushPage() {
    router.push({
      uri: 'pages/routerpage2/routerpage2',
      params: {
        data1: 'message',
        data2: {
          data3: \[123, 456, 789\]
        }
      }
    });
  }
}
export default new A()

// routerpage2 page
class B{
  data:Record<string,string> = {'data1': 'default'}
  data2:Record<string,number\[\]> = {'data3': \[1, 2, 3\]}
  onInit() {
    console.info('showData1:' + this.data.data1);
    console.info('showData3:' + this.data2.data3);
  }
}
export default new B()

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/IZMXLHdGRnCxFb1a-hf0aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C23E5910666DFB62903CB6AE04129D891FCD68735B0DA315D1B60CDF17A02C6)

The page routing stack supports a maximum of 32 pages.

#### router.replace

replace(options: RouterOptions): void

Replaces the current page with another one in the application and destroys the current page.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Page routing parameters. For details, see **RouterOptions**. |

**Example**

// Current page
import router from '@system.router';
class C{
  replacePage() {
    router.replace({
      uri: 'pages/detail/detail',
      params: {
        data1: 'message'
      }
    });
  }
}
export default new C()

// detail page
class Area {
  data:Record<string,string> = {'data1': 'default'}
  onInit() {
    console.info(\`showData1: ${JSON.stringify(this.data)}\`);
  }
}
export default new Area()

#### router.back

back(options?: BackRouterOptions): void

Returns to the previous page or a specified page.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [BackRouterOptions](#backrouteroptions) | No | For details, see **BackRouterOptions**. |

**Example**

// index page
import router from '@system.router';
class D{
  indexPushPage() {
    router.push({
      uri: 'pages/detail/detail'
    });
  }
}
export default new D()

// detail page
import router from '@system.router';
class E{
  detailPushPage() {
    router.push({
      uri: 'pages/mall/mall'
    });
  }
}
export default new E()

// Navigate from the mall page to the detail page through router.back().
import router from '@system.router';
class F{
  mallBackPage() {
    router.back();
  }
}
export default new F()

// Navigate from the detail page to the index page through router.back().
import router from '@system.router';
class G{
  defaultBack() {
    router.back();
  }
}
export default new G()

// Return to the detail page through router.back().
import router from '@system.router';
class H{
  backToDetail() {
    router.back({uri:'pages/detail/detail'});
  }
}
export default new H()

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/T4uVR1ApQTmqf5TXMrYO-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C29EF0F37AA35974292950D0CDB1A1295140C86CFF242AE8EF1B7F67FD449F51)

In the example, the **uri** field indicates the page route, which is specified by the **pages** list in the configuration file.

#### router.getParams7+

getParams(): ParamsInterface

Obtains parameter information about the current page.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [ParamsInterface](#paramsinterface) | For details, see **ParamsInterface**. |

#### router.clear

clear(): void

Clears all historical pages in the stack and retains only the current page at the top of the stack.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

import router from '@system.router';
class I{
  clearPage() {
    router.clear();
  }
}
export default new I()

#### router.getLength

getLength(): string

Obtains the number of pages in the current stack.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | Number of pages in the stack. The maximum value is **32**. |

**Example**

import router from '@system.router';
class J{
  getLength() {
    let size = router.getLength();
    console.info('pages stack size = ' + size);
  }
}
export default new J()

#### router.getState

getState(): RouterState

Obtains state information about the current page.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [RouterState](#routerstate) | For details, see **RouterState**. |

**Example**

import router from '@system.router';
class K{
  getState() {
    let page = router.getState();
    console.info('current index = ' + page.index);
    console.info('current name = ' + page.name);
    console.info('current path = ' + page.path);
  }
}
export default new K()

#### router.enableAlertBeforeBackPage6+

enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void

Enables the display of a confirm dialog box before returning to the previous page.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [EnableAlertBeforeBackPageOptions](#enablealertbeforebackpageoptions6) | Yes | For details, see **EnableAlertBeforeBackPageOptions**. |

**Example**

import router from '@system.router';
class L{
  enableAlertBeforeBackPage() {
    router.enableAlertBeforeBackPage({
      message: 'Message Info',
      success: ()=> {
        console.info('success');
      },
      cancel: ()=> {
        console.info('cancel');
      }
    });
  }
}
export default new L()

#### router.disableAlertBeforeBackPage6+

disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void

Disables the display of a confirm dialog box before returning to the previous page.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DisableAlertBeforeBackPageOptions](#disablealertbeforebackpageoptions6) | No | For details, see **DisableAlertBeforeBackPageOptions**. |

**Example**

import router from '@system.router';
class Z{
  disableAlertBeforeBackPage() {
    router.disableAlertBeforeBackPage({
      success: ()=> {
        console.info('success');
      },
      cancel: ()=> {
        console.info('cancel');
      }
    });
  }
}
export default new Z()

#### RouterOptions

Defines the page routing parameters.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | 
URI of the target page, in either of the following formats:

1\. Absolute path, which is provided by the page list in the **config.json** file. Examples:

\- pages/index/index

\- pages/detail/detail

2\. Specific path. If the URI is a slash (/), the home page is displayed.

 |
| params | Object | No | Data that needs to be passed to the target page during redirection. The target page can use **router.getParams()** to obtain the passed parameters, for example, **this.keyValue** (**keyValue** is the value of a key in **params**). In the web-like paradigm, these parameters can be directly used on the target page. If the field specified by **key** already exists on the target page, the passed value of the key will be displayed. |

#### BackRouterOptions

Defines the parameters for routing back.

**System capability**: The items in the table below require different system capabilities. For details, see the table.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri7+ | string | No | 
URI of the page to return to. If the specified page does not exist in the page stack, the application does not respond. If this parameter is not set, the application returns to the previous page.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

 |
| params7+ | object | No | 

Data that needs to be passed to the target page during redirection.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

 |

#### RouterState

Defines the routing state.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the current page in the stack. The index starts from 1 from the bottom to the top of the stack. |
| name | string | Yes | Name of the current page, that is, the file name. |
| path | string | Yes | Path of the current page. |

#### EnableAlertBeforeBackPageOptions6+

Defines the **EnableAlertBeforeBackPage** parameter.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | string | Yes | Content displayed in the confirm dialog box. |
| success | (errMsg: string) => void | No | Called when the **OK** button in the confirm dialog box is clicked. **errMsg** indicates the returned information. |
| cancel | (errMsg: string) => void | No | Called when the **Cancel** button in the confirm dialog box is clicked. **errMsg** indicates the returned information. |
| complete | () => void | No | Called when the dialog box is closed. |

#### DisableAlertBeforeBackPageOptions6+

Defines the **DisableAlertBeforeBackPage** parameter.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | (errMsg: string) => void | No | Called when the dialog box is closed. **errMsg** indicates the returned information. |
| cancel | (errMsg: string) => void | No | Called when the dialog box fails to be closed. **errMsg** indicates the returned information. |
| complete | () => void | No | Called when the dialog box is closed. |

#### ParamsInterface

| Name | Type | Description |
| :-- | :-- | :-- |
| \[key: string\] | object | List of routing parameters. |
