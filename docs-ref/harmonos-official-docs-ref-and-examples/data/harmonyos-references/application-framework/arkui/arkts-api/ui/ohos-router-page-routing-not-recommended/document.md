# @ohos.router (Page Routing) (Not Recommended)

The **Router** module provides APIs to access pages through URLs. You can use the APIs to navigate to a specified page in an application, replace the current page with another one in the same application, and return to the previous page or a specified page.

For routing management, it is recommended that you use the [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation) component instead as your application routing framework.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/J3QJc22GTZecrTwXw-wCBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E68AD86AAE920870ACBF47E9EFFCF9894364E53F7A43C9076EA56B7616C3548)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Page routing APIs can be invoked only after page rendering is complete. Do not call these APIs in **onInit** and **onReady** when the page is still in the rendering phase.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   When using [pushUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushurl-1) or [pushNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushnamedroute-1) with a callback to return the result, be aware that the stack information obtained through the callback using APIs such as [getLength](../ohos-arkui-uicontext-uicontext/class-router/document.md#getlength) represents an intermediate state during the navigation operation. This temporary state might differ from the final stack information available after the stack operation is complete.
    

#### Modules to Import

import { router } from '@kit.ArkUI';

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions): Promise<void>

Navigates to a specified page in the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/3feu8JIIRhq-eTytaZ51Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A40592FA1085D2CBFFF55957FAB5ED88A6265C40348CD5C63A6DB950000E8AA5)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [pushUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushurl) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Page routing parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/QVkY0uO0TWaY-AUD772FCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EA89B8A0ED317D87D42D456AFF20122B1D4A6324EA3FD198A8B12A869B513D9)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', \[123, 456, 789\])
})
  .then(() => {
    console.error(\`pushUrl finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void

Navigates to a specified page in the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/VyGpVQLpRteUjinfZiEWmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40B553DAD458CAF15B3D0635D4846A99E1FEBE7CB943FF96FF0814B1C4DA0BBB)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [pushUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushurl-1) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Page routing parameters. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/LiI97jNeQTK9rhpz5gv4Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00ED8D450BA14401FC5235A7DB0702910835D75230D57C878EA4480415E2AC48)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**Example**

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', \[123, 456, 789\])
}, (err) => {
  if (err) {
    console.error(\`pushUrl failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('pushUrl success');
})

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>

Navigates to a specified page in the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/VGA-sdetQmWbsYuKYf7Lkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2812F5D89A8F58B91B520072A09220EADFD676AD6F9029AD62D6325A9F6340FC)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [pushUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushurl-2) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Page routing parameters. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/k-UGwuviSpar96aSuPWMHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B28EC8BA0E2B595B67D457AB59BF3682D94555FA8276864B75C4BDEFE1733D8)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', \[123, 456, 789\])
}, router.RouterMode.Standard)
  .then(() => {
    console.error(\`pushUrl finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

Navigates to a specified page in the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/o_ur5IqxQ_uJKuEhqDj4nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1665FEE81C2504352678FBA9122D73A6E62B25475F3B3EDBB700F7DD0306B88F)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [pushUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushurl-3) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Page routing parameters. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/XQJPj_XlRgiET50PHeDNOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64AFC05793C6CD7AAE903107CE241B2DA65428583D4EA8C81ED9D7E92B454DC0)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**Example**

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', \[123, 456, 789\])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(\`pushUrl failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('pushUrl success');
})

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions): Promise<void>

Replaces the current page with another one in the application and destroys the current page. This API cannot be used to configure page transition effects. To configure page transition effects, use the [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation) component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/JuXOPMzAQi-7nSHOGoaN5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78805FE0A44FF6742EF2B58F68D5027C1B9EC222A84B08CC3C77A3A66914932A)

-   This API is supported since API version 9 and deprecated since API version 18 except for lite wearables. You are advised to use [replaceUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#replaceurl) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Description of the new page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/BSIf9ImxTvS7YSLzpDgL6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25B123A251EB0942EA471E9C31FD03F05D5311C8AD50D76D49DEB6AA069BF798)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
})
  .then(() => {
    console.error(\`replaceUrl finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void

Replaces the current page with another one in the application and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/4wZHlmqtSzmBN6UuwZ-sJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21E16482B330E466C794501E432CF4D782EE42C95A1B8A4D5D339254C0783481)

-   This API is supported since API version 9 and deprecated since API version 18 except for lite wearables. You are advised to use [replaceUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#replaceurl-1) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Description of the new page. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Y0PfOnkjTfqDAZXYF8DRfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=678180C0F61E03CDC2B57F560F54FAD339E3B827943C3B0AC1A7491B2EFD6DB2)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**Example**

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, (err) => {
  if (err) {
    console.error(\`replaceUrl failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('replaceUrl success');
})

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>

Replaces the current page with another one in the application and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Mt4Hqgi5S66U2VxtacVo4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6578A8CA87AD2DF593C8862937CED5B6AB546734625095BA751DA3DA83A54B7A)

-   This API is supported since API version 9 and deprecated since API version 18 except for lite wearables. You are advised to use [replaceUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#replaceurl-2) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Description of the new page. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/7k2cNbxLQVuAd_P85ClMTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A7E2A795ED3FA1CC1EA0253CAA01E7ABF4C19AFB491130936946E628C1E5063)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1:string;

  constructor(str:string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard)
  .then(() => {
    console.error(\`replaceUrl finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

Replaces the current page with another one in the application and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/HobS3MSpQIyG1UY7NPjpDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11300AA10259C56C134C626D70F204621F54681AC52D29173BB0581F38BAD694)

-   This API is supported since API version 9 and deprecated since API version 18 except for lite wearables. You are advised to use [replaceUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#replaceurl-3) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Description of the new page. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/dHlkoTfJT32aCS3VHkGRuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94EE4312D25727A2A8EC219BD9AF530F0DE05F34D7FB0E672DA04908B3E65DF7)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**Example**

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(\`replaceUrl failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('replaceUrl success');
});

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions): Promise<void>

Navigates to a page using the named route. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/jSoz3p1sSjqGhhIoo3hwMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=114F28EC72B6C08AA49C862A2E3FA03EB33EE9256541F4CE6E03FC55861608A3)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [pushNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushnamedroute) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Page routing parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/ZlfiO_i1QraMUKUNklRHDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=310634E84FC7D2D1AE290467DAA0BC1351795C707DDCB470534DDE0AF8EDB8DB)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', \[123, 456, 789\])
})
  .then(() => {
    console.error(\`pushNamedRoute finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

For details, see [Named Route](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing#named-route).

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

Navigates to a page using the named route. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/DPl-JGzqRVK4dgP2Jwra6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9918A97A20A1FE51C3EC8CCE1763D7CBC2AFC061D09BC60843358926B3317169)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [pushNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushnamedroute-1) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Page routing parameters. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/e1hIRrk6Q3CQ2_YBKPEyBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85284FF53233F6F8AB2BB57DEAF77711306B51174ECB5D3B63602E6F3BC5AE3E)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**Example**

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', \[123, 456, 789\])
}, (err) => {
  if (err) {
    console.error(\`pushNamedRoute failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('pushNamedRoute success');
})

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

Navigates to a page using the named route. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/4WhPvGODSi-p1R0KVCmM7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB3806770A9C5F318294326188D0FCF68F69F99E4FBD571E781A7DE646C07AA9)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [pushNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushnamedroute-2) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Page routing parameters. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Flg_dL5pQ_KvrtDKuYooRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1198A7F8CA8B38584C63B03224D82E62E2A56B66DB698C6D904B3E4BA25462CF)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str
    this.data2 = new innerParams(tuple)
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', \[123, 456, 789\])
}, router.RouterMode.Standard)
  .then(() => {
    console.error(\`pushNamedRoute finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

Navigates to a page using the named route. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/4dvCIIF2R2eg5NAqb-21SA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=558209A1BA6B796372228039DE4E3AE97B6A003F0240B3A8DEEBC2494BB2D449)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [pushNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushnamedroute-3) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Page routing parameters. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/5Wpt69RuTRyRZZvaDY8fnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A81169374786D6C9F7245AC02F612FD91548F9365EAEAB66EEB89F89710AF273)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**Example**

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', \[123, 456, 789\])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(\`pushNamedRoute failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('pushNamedRoute success');
})

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions): Promise<void>

Replaces the current page with another one using the named route and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/NVgvXKO8SdCOaKTLiOGQWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21DF2C22297F09A32E766B103E1155183C6349563A7A627D885276DB9559FE14)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [replaceNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#replacenamedroute) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Description of the new page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/SzVWNnD5T0ms1GS-4BRM1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66696DB3EE527EC93F0B0AE841B3B391CCE4D53BE6DC91A9EB818E842F9937C5)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
})
  .then(() => {
    console.error(\`replaceNamedRoute finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

Replaces the current page with another one using the named route and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ZHMKfIV3Shi8UnUk8yCH_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FD0FEF102A0B196371096897F609D06791278A28C08EA159148741234C7A184)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [replaceNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#replacenamedroute-1) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Description of the new page. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ngUPM83pQ4e6QgHXFjYNxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A52D0E5D0BB893390A5E752DC24A79AE59F7B794824F8CEF440AB425B54C54EB)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**Example**

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, (err) => {
  if (err) {
    console.error(\`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('replaceNamedRoute success');
})

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

Replaces the current page with another one using the named route and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/cAIDpVgrQv2WYw8ZjmWNXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBE3E6F58F6673E0B55E10D2DCA2462F72724850006E46D12715E3D74BFE1475)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [replaceNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#replacenamedroute-2) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Description of the new page. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/-xKW5bvdRYKdl42towWU9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C65D8E84DE6C8F9BE68EE953A69907CA2472345CFCE770519682A5990303FC42)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, router.RouterMode.Standard)
  .then(() => {
    console.error(\`replaceNamedRoute finish\`);
  })
  .catch((err: ESObject) => {
    console.error(\`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
  })

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

Replaces the current page with another one using the named route and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/q7Do-gfTRyqGw5XL7bOycg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95161BD18CC6B3248C6E8670A57D386B4932E86106291AC0213A002F75A0CDEA)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [replaceNamedRoute](../ohos-arkui-uicontext-uicontext/class-router/document.md#replacenamedroute-3) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | Yes | Description of the new page. |
| mode | [RouterMode](#routermode9) | Yes | Routing mode. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Router Error Codes](../../../error-codes/ui/router-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/Fur30KyCRriGy-8qW4Nfpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=036D64E333918D0E598AF66EA0B3269AAE312554CD83829134753168AD954C08)

The following error codes returned by this API are all of the string type.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**Example**

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(\`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('replaceNamedRoute success');
});

#### router.back(deprecated)

back(options?: RouterOptions ): void

Returns to the previous page or a specified page, which deletes all pages between the current page and the target page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/P6A9VIw9RHuZg4Lc8mnu7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27EC1824901D09DBEF1B5FA1D695452C6AC5135F4722503777BF4974B1B33AC6)

-   This API is supported since API version 8 and deprecated since API version 18. You are advised to use [back](../ohos-arkui-uicontext-uicontext/class-router/document.md#back) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | No | Description of the target page. The **url** parameter indicates the URL of the page to return to. If the specified page does not exist in the navigation stack, no action is taken. If no URL is set, the application returns to the previous page, and the page is not rebuilt. Pages are only reclaimed after being popped from the navigation stack. Setting **url** to the special value **"/"** has no effect. If the named route is used, the provided URL must be the name of the named route. |

**Example**

this.getUIContext().getRouter().back({ url: 'pages/detail' });

#### router.back(deprecated)

back(index: number, params?: Object): void;

Returns to the specified page, which deletes all pages between the current page and the target page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/9gRap8hQRu2OEU74X9I91w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAA86A170B351946FB687D31822A08136083776A21FB7C51CCC32850F4D7E6BF)

-   This API is supported since API version 12 and deprecated since API version 18. You are advised to use [back](../ohos-arkui-uicontext-uicontext/class-router/document.md#back12) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 12, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the target page to navigate to. The index starts from 1 from the bottom to the top of the stack. |
| params | Object | No | Parameters carried when returning to the page. |

**Example**

this.getUIContext().getRouter().back(1);

this.getUIContext().getRouter().back(1, { info: 'From Home' }); // Returning with parameters.

#### router.clear(deprecated)

clear(): void

Clears all historical pages in the stack and retains only the current page at the top of the stack.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/7uZnD2DSQoSdN0OwBprdZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E36AB0AC5E0FDDA70B4F064FB202F0301DABF284DF80850EB7336D824C407BBA)

-   This API is supported since API version 8 and deprecated since API version 18. You are advised to use [clear](../ohos-arkui-uicontext-uicontext/class-router/document.md#clear) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

this.getUIContext().getRouter().clear();

#### router.getLength(deprecated)

getLength(): string

Obtains the number of pages in the current stack.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/-wa0Wq2iSlOUSTTjf0Q18g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FC54EF7B3C25E03E665D551C56B20FE4E9810CB6C3F7BAA71F5936611E1E497)

-   This API is supported since API version 8 and deprecated since API version 18. You are advised to use [getLength](../ohos-arkui-uicontext-uicontext/class-router/document.md#getlength) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | Number of pages in the stack. The maximum value is **32**. |

**Example**

let size = this.getUIContext().getRouter().getLength();
console.info('pages stack size = ' + size);

#### router.getState(deprecated)

getState(): RouterState

Obtains state information about the page at the top of the navigation stack.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/dLLlOG1iQcu_UlEseK55hA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91A5BB01B491D2E165DC8ACD1B878D679B1B7A6A3BF3D8304EBAE9CC005D8DCE)

-   This API is supported since API version 8 and deprecated since API version 18. You are advised to use [getState](../ohos-arkui-uicontext-uicontext/class-router/document.md#getstate) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [RouterState](#routerstate) | Page routing state. |

**Example**

let page = this.getUIContext().getRouter().getState();
console.info('current index = ' + page.index);
console.info('current name = ' + page.name);
console.info('current path = ' + page.path);

#### router.getStateByIndex(deprecated)

getStateByIndex(index: number): RouterState | undefined

Obtains the status information about a page by its index.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/PPJwhG8QSKSH_OXroHuOAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A674F7C2254E3B64DFD593D1C646B16A57825E0279FAD5F18E29A45A4E0BE77C)

-   This API is supported since API version 12 and deprecated since API version 18. You are advised to use [getStateByIndex](../ohos-arkui-uicontext-uicontext/class-router/document.md#getstatebyindex12) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 12, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the target page. The index starts from 1 from the bottom to the top of the stack. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RouterState](#routerstate) | undefined | State information about the target page; **undefined** if the specified index does not exist. |

**Example**

let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info(\`params = ${JSON.stringify(options.params)}\`);
}

#### router.getStateByUrl(deprecated)

getStateByUrl(url: string): Array<RouterState>

Obtains the status information about a page by its URL.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/xgaSL_xxQxaHUGptESbVeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=553253E7E8C75832CABEDD247E6B88598CB0BAC6EF1790817D2604E1958582D6)

-   This API is supported since API version 12 and deprecated since API version 18. You are advised to use [getStateByUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#getstatebyurl12) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 12, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the target page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[RouterState](#routerstate)\> | Page routing state. |

**Example**

let options: Array<router.RouterState> = router.getStateByUrl('pages/index');
for (let i: number = 0; i < options.length; i++) {
  console.info('index = ' + options\[i\].index);
  console.info('name = ' + options\[i\].name);
  console.info('path = ' + options\[i\].path);
  console.info('params = ' + options\[i\].params);
}

#### RouterState

Describes the page routing state.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | No | No | 
Index of the current page in the stack. The index starts from 1 from the bottom to the top of the stack.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| name | string | No | No | 

Name of the current page, that is, the file name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| path | string | No | No | 

Path of the current page.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| params12+ | Object | No | No | 

Parameters carried on the current page.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### router.showAlertBeforeBackPage(deprecated)

showAlertBeforeBackPage(options: EnableAlertOptions): void

Enables the display of a confirm dialog box before returning to the previous page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/0e-uXqYSSoiryZpEowJ_wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E999C67A79000B5F3CD0DB5CEEEF1A877343D5D944463A5DC545637C5A8359D)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [showAlertBeforeBackPage](../ohos-arkui-uicontext-uicontext/class-router/document.md#showalertbeforebackpage) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [EnableAlertOptions](#enablealertoptions) | Yes | Description of the dialog box. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  this.getUIContext().getRouter().showAlertBeforeBackPage({
    message: 'Message Info'
  });
} catch (err) {
  console.error(\`showAlertBeforeBackPage failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
}

#### EnableAlertOptions

Describes the confirm dialog box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| message | string | No | No | Content displayed in the confirm dialog box. |

#### router.hideAlertBeforeBackPage(deprecated)

hideAlertBeforeBackPage(): void

Disables the display of a confirm dialog box before returning to the previous page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/txHFW7p2Q9OVwwyqOy5V6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A683C66BEA4A17FB2730C7E09F483877ABD9CCF086C055FBFF989F630B5D8A16)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [hideAlertBeforeBackPage](../ohos-arkui-uicontext-uicontext/class-router/document.md#hidealertbeforebackpage) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

this.getUIContext().getRouter().hideAlertBeforeBackPage();

#### router.getParams(deprecated)

getParams(): Object

Obtains the parameters passed from the page that initiates redirection to the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/LFwsyBblQ1W93QrHP61ayw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7496C2ADA632F6251F93440FA29FC4D4D53FB3FD0550D795A5E441733081F298)

-   This API is supported since API version 8 and deprecated since API version 18. You are advised to use [getParams](../ohos-arkui-uicontext-uicontext/class-router/document.md#getparams) instead. Before calling this API, you need to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) instance using the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Router](../ohos-arkui-uicontext-uicontext/class-router/document.md) object associated with the current UI context.
    

**getParams** obtains only the parameters of the current page and does not clear the parameters associated with the page.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Object | Parameters passed from the page that initiates redirection to the current page. |

**Example**

this.getUIContext().getRouter().getParams();

#### RouterOptions

Describes the page routing options.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| url | string | No | No | 
URL of the target page, in either of the following formats:

\- Absolute path of the page. The value is available in the pages list in the **config.json** file, for example:

\- pages/index/index

\- pages/detail/detail

\- special value. If the value of **url** is **"/"**, the application navigates to the home page. By default, the home page is set to the first item in the **src** value array.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| params | Object | No | Yes | 

Data that needs to be passed to the target page during redirection. The received data becomes invalid when the page is switched to another page. The target page can use **router.getParams()** to obtain the passed parameters, for example, **this.keyValue** (**keyValue** is the value of a key in **params**). In the web-like paradigm, these parameters can be directly used on the target page. If the field specified by **key** already exists on the target page, the passed value of the key will be displayed.

**NOTE**

The **params** parameter can only carry serializable data. Objects returned by methods and system APIs (for example, **PixelMap** objects defined and returned by media APIs) cannot be passed. To pass such objects, extract from them the basic type attributes to be passed, and then construct objects of the object type.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| recoverable14+ | boolean | No | Yes | 

Whether the corresponding page is recoverable.

Default value: **true**.

**true**: The corresponding page is recoverable.

**false**: The corresponding page is not recoverable.

**NOTE**

If an application is switched to the background and is later closed by the system due to resource constraints or other reasons, a page marked as recoverable can be restored by the system when the application is brought back to the foreground. For more details, see [UIAbility Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-recover-guideline).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/40WerbCqSKKVutdRlBkENw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98E648EEEFA8A044E4E6C11A20E6FB38422569B9E8489CFE859C0B1DB505ED70)

The page routing stack supports a maximum of 32 pages.

#### RouterMode9+

Enumerates the routing modes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Standard | 0 | 
Multi-instance mode. It is the default routing mode.

The target page is added to the top of the page stack, regardless of whether a page with the same URL exists in the stack.

**NOTE**

If no routing mode is used, the navigation will be carried out according to the default multi-instance mode.

 |
| Single | 1 | 

Singleton mode.

If the URL of the target page already exists in the page stack, the page is moved to the top of the stack.

If the URL of the target page does not exist in the page stack, the page is redirected to in multi-instance mode.

 |

#### NamedRouterOptions10+

Describes the named route options.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | 
Name of the target named route.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

 |
| params | Object | No | Yes | 

Data that needs to be passed to the target page during redirection. The target page can use **router.getParams()** to obtain the passed parameters, for example, **this.keyValue** (**keyValue** is the value of a key in **params**). In the web-like paradigm, these parameters can be directly used on the target page. If the field specified by **key** already exists on the target page, the passed value of the key will be displayed.

**NOTE**

The **params** parameter cannot pass objects returned by methods and system APIs, for example, **PixelMap** objects defined and returned by media APIs. To pass such objects, extract from them the basic type attributes to be passed, and then construct objects of the object type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

 |
| recoverable14+ | boolean | No | Yes | 

Whether the corresponding page is recoverable.

Default value: **true**.

**true**: The corresponding page is recoverable.

**false**: The corresponding page is not recoverable.

**NOTE**

If an application is switched to the background and is later closed by the system due to resource constraints or other reasons, a page marked as recoverable can be restored by the system when the application is brought back to the foreground. For more details, see [UIAbility Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-recover-guideline).

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

 |

#### Examples

## JavaScript-based Web-like Development Paradigm

The following sample code applies only to JavaScript files, not ArkTS files.

// Current page
export default {
  pushPage() {
    router.pushUrl({
      url: 'pages/detail/detail',
      params: {
        data1: 'message'
      }
    });
  }
}

// detail page
export default {
  onInit() {
    console.info('showData1:' + this.getUIContext().getRouter().getParams()\['data1'\]);
  }
}

## TypeScript-based Declarative Development Paradigm

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/5OsmhKfgTDKYt3d9OorMGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD1F8F9C27EB38519E3AB152B6B804BED7CB50CF7BBD751FC00061705BDAA655)

Directly using **router** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance using **getUIContext**, and then obtain the associated **router** object using [getRouter](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getrouter).

// Navigate to the target page through router.pushUrl with the params parameter carried.
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

// Define the class for passing parameters.
class innerParams {
  array: number\[\];

  constructor(tuple: number\[\]) {
    this.array = tuple;
  }
}

class RouterParams {
  text: string;
  data: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.text = str;
    this.data = new innerParams(tuple);
  }
}

@Entry
@Component
struct Index {
  async routePage() {
    let options: router.RouterOptions = {
      url: 'pages/second',
      params: new RouterParams('This is the value on the first page', \[12, 45, 78\])
    }
    // You are advised to use this.getUIContext().getRouter().pushUrl().
    this.getUIContext().getRouter().pushUrl(options)
      .then(() => {
        console.error(\`pushUrl finish\`);
      })
      .catch((err: ESObject) => {
        console.error(\`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}\`);
      })
    }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('This is the first page.')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage()
      })
    }
    .width('100%')
    .height('100%')
  }
}

// Receive the transferred parameters on the second page.
import { router } from '@kit.ArkUI';

class innerParams {
  array: number\[\];

  constructor(tuple: number\[\]) {
    this.array = tuple;
  }
}

class RouterParams {
  text: string;
  data: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.text = str;
    this.data = new innerParams(tuple);
  }
}

@Entry
@Component
struct Second {
  private content: string = "This is the second page.";
  // You are advised to use this.getUIContext().getRouter().getParams().
  @State text: string = (this.getUIContext().getRouter().getParams() as RouterParams).text;
  @State data: object = (this.getUIContext().getRouter().getParams() as RouterParams).data;
  @State secondData: string = '';

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text(\`${this.content}\`)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
      Text(this.text)
        .fontSize(30)
        .onClick(() => {
          this.secondData = (this.data\['array'\]\[1\]).toString();
        })
        .margin({ top: 20 })
      Text(\`This is the data passed from the first page: ${this.secondData}\`)
        .fontSize(20)
        .margin({ top: 20 })
        .backgroundColor('red')
    }
    .width('100%')
    .height('100%')
  }
}

#### router.push(deprecated)

push(options: RouterOptions): void

Navigates to a specified page in the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/DAeaeWxbRuGsh7zAY6Gqqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA7B408E8E5519C67478EC78A21842F4186E98873C38BF42E11540F38DFC76D3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [pushUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#pushurl) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Page routing parameters. |

**Example**

class innerParams {
  data3: number\[\];

  constructor(tuple: number\[\]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number\[\]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.push({
  url: 'pages/routerpage2',
  params: new RouterParams('message', \[123, 456, 789\])
});

#### router.replace(deprecated)

replace(options: RouterOptions): void

Replaces the current page with another one in the application and destroys the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/1DQsAgdfTYWGzkxKXopmog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2225FA41C57C58B4DFCF9462DBA9763555704AD28260E430CEA76951DAE1BE2C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [replaceUrl](../ohos-arkui-uicontext-uicontext/class-router/document.md#replaceurl) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | Yes | Description of the new page. |

**Example**

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replace({
  url: 'pages/detail',
  params: new RouterParams('message')
});

#### router.enableAlertBeforeBackPage(deprecated)

enableAlertBeforeBackPage(options: EnableAlertOptions): void

Enables the display of a confirm dialog box before returning to the previous page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/r5laLHObTXCRUdevvaAsvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65ACA0A4189B6B802919A17E25F6D502C147D41ADAE8F24F4A424D0B0A1F4C12)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [showAlertBeforeBackPage](../ohos-arkui-uicontext-uicontext/class-router/document.md#showalertbeforebackpage) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [EnableAlertOptions](#enablealertoptions) | Yes | Description of the dialog box. |

**Example**

router.enableAlertBeforeBackPage({
  message: 'Message Info'
});

#### router.disableAlertBeforeBackPage(deprecated)

disableAlertBeforeBackPage(): void

Disables the display of a confirm dialog box before returning to the previous page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/zJkRVF95QDyELgH_B6BNjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5664DB84AE4647297DFE8268A534920976080AA68A9E3288999365D98AE3B16)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hideAlertBeforeBackPage](../ohos-arkui-uicontext-uicontext/class-router/document.md#hidealertbeforebackpage) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

router.disableAlertBeforeBackPage();
