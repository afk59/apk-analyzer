# Class (WebController)

Implements a **WebController** to control the behavior of the **Web** component. A **WebController** can control only one **Web** component, and the APIs in the **WebController** can be invoked only after it has been bound to the target **Web** component.

This API is deprecated since API version 9. You are advised to use [WebviewController9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md) instead.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Ssmco25NRDulo4FIp2hZpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2E9B225091A2E5AF8B41E3DFC1D4F05BB3D1D4D7B354FA25297C81998371B52)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### Creating an Object

let webController: WebController = new WebController()

#### constructor(deprecated)

constructor()

Constructs a **WebController** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/JJoz83V4RYipd5KhY7kM7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0B3876D8578F08BE342C7804E0D277662044FEEB218658BDFFC7B93A4E292B3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [constructor11+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#constructor11) instead.

**System capability**: SystemCapability.Web.Webview.Core

#### getCookieManager(deprecated)

getCookieManager(): WebCookie

Obtains the cookie management object of the **Web** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/b6SqXkwjTgm3xUTnFCpV5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=130EC743CA07AF088040AD24A4BAF40F1BF2E2E3B0CCBB76455C000A5466FF29)

This API is supported since API version 9 and deprecated since API version 9. You are advised to use [getCookie](../../../arkts-api/ohos-web-webview-webview/class-webcookiemanager/document.md#getcookiedeprecated) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| WebCookie | Cookie management object of the **Web** component. For details, see [WebCookie](../class-webcookie/document.md). |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('getCookieManager')
        .onClick(() => {
          let cookieManager = this.controller.getCookieManager()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### requestFocus(deprecated)

requestFocus()

Requests focus for this web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/N9hcKC8URpqD4R3xHZk-MA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91A8AD8A0C39C6B74FC540FB3C05B0D7549558ADB764EF5B52F0FDD74C304D2E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [requestFocus9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#requestfocus) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('requestFocus')
        .onClick(() => {
          this.controller.requestFocus()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### accessBackward(deprecated)

accessBackward(): boolean

Checks whether going to the previous page can be performed on the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/TR2mDj8oQ4OMJD3HPTPvUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=049905E9BDB65E9C15F706DD12E90097D9E143EFCEBC3E69FABF5D0182BF8829)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [accessBackward9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#accessbackward) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** is returned if going to the previous page can be performed on the current page; otherwise, **false** is returned. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('accessBackward')
        .onClick(() => {
          let result = this.controller.accessBackward()
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### accessForward(deprecated)

accessForward(): boolean

Checks whether going to the next page can be performed on the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/4zJBZUIMQnCSyTyN1YqnUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4914EBE6C7DB8FAF6A7B36E437A397FD43FC12D61FC5518D544F47C17522E10B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [accessForward9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#accessforward) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | If going to the next page can be performed on the current page, **true** is returned; otherwise, **false** is returned. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('accessForward')
        .onClick(() => {
          let result = this.controller.accessForward()
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### accessStep(deprecated)

accessStep(step: number): boolean

Performs a specific number of steps forward or backward from the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/yJ9uQOGPT2Wcn7DCwaP7gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13A295B0728691A388E3C3FF8801643350C3512D29AF46FC618A31479C54C1B4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [accessStep9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#accessstep) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| step | number | Yes | Number of the steps to take. A positive number means to go forward, and a negative number means to go backward. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether going forward or backward from the current page is successful. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State steps: number = 2

  build() {
    Column() {
      Button('accessStep')
        .onClick(() => {
          let result = this.controller.accessStep(this.steps)
          console.info('result:' + result)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### backward(deprecated)

backward()

Goes to the previous page based on the history stack. This API is generally used together with **accessBackward**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/A4ANxw_tQFGd_FrkHkaCAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=760100B5846ECEC238FDC44B40A4226B5CA428AB4DCD01550FD4919EB81FBED8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [backward9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#backward) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('backward')
        .onClick(() => {
          this.controller.backward()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### forward(deprecated)

forward()

Goes to the next page based on the history stack. This API is generally used together with **accessForward**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/vPa4YlCASrSfqUGpOPOANA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34B164954D8F239D48AE9449705E95EDD178BFA28230A5B9B27F37DA22CA0689)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [forward9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#forward) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('forward')
        .onClick(() => {
          this.controller.forward()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### deleteJavaScriptRegister(deprecated)

deleteJavaScriptRegister(name: string)

Deletes a specific application JavaScript object that is registered with the window through **registerJavaScriptProxy**. The deletion takes effect immediately, with no need for invoking the [refresh](#refreshdeprecated) API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/uAC5NaYDTguUFCe2MaMhXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C62C437D9ECE225EEDB3CBAB78394AFC6E716805D39094A63B890CCEE9116A0)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [deleteJavaScriptRegister9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#deletejavascriptregister) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the registered JavaScript object, which can be used to invoke the corresponding object on the application side from the web side. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State name: string = 'Object'

  build() {
    Column() {
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          this.controller.deleteJavaScriptRegister(this.name)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getHitTest(deprecated)

getHitTest(): HitTestType

Obtains the element type of the area being clicked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/6ZtjkKhtSbSyThNB7LNqpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1684ABBBD80A4BE160C5B8A3897F9201B66CAEA7545369C8235738180EA32D75)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getHitTest9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#gethittestdeprecated) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [HitTestType](../enums/document.md#hittesttypedeprecated) | Element type of the area being clicked. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('getHitTest')
        .onClick(() => {
          let hitType = this.controller.getHitTest()
          console.info("hitType: " + hitType)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### loadData(deprecated)

loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })

Loads data. If **baseUrl** is empty, the specified character string will be loaded using the data protocol.

If **baseUrl** is set to a data URL, the encoded string will be loaded by the **Web** component using the data protocol.

If **baseUrl** is set to an HTTP or HTTPS URL, the encoded string will be processed by the **Web** component as a non-encoded string in a manner similar to **loadUrl**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/fw3cEOkKR0GVvPVpYFaycA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41455171A2FAECCBC7038342413334644D42DF1C79B1B82450BC62814FE0B371)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [loadData9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#loaddata) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | Yes | Character string obtained after being Base64 or URL encoded. |
| mimeType | string | Yes | Media type (MIME). |
| encoding | string | Yes | Encoding type, which can be Base64 or URL. |
| baseUrl | string | No | URL (HTTP/HTTPS/data compliant), which is assigned by the **Web** component to **window.origin**. |
| historyUrl | string | No | Historical record URL. If this parameter is not empty, it can be managed in historical records to implement page going backward and forward. This parameter is invalid when **baseUrl** is left empty. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          this.controller.loadData({
            data: "<html><body bgcolor=\\"white\\">Source:<pre>source</pre></body></html>",
            mimeType: "text/html",
            encoding: "UTF-8"
          })
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### loadUrl(deprecated)

loadUrl(options: { url: string | Resource, headers?: Array<Header> })

Loads a URL using the specified HTTP header.

The object injected through **loadUrl** is valid only in the current document. It will be invalid on a new page navigated to through **loadUrl**.

The object injected through **registerJavaScriptProxy** is still valid on a new page redirected through **loadUrl**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/v7gJQ7XVRB6CnGqoSOwqow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AD4C27583C3DA2BA6710010D427116981EB247408CB96D3893402406CCB9A89)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [loadUrl9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#loadurl) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Resource | Yes | URL to load. |
| headers | Array<[Header](../interfaces-others/document.md#header)\> | No | 
Additional HTTP request header of the URL.

The default value is **\[\]**.

 |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          this.controller.loadUrl({ url: 'www.example.com' })
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### onActive(deprecated)

onActive(): void

Called when the **Web** component enters the active state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/OYeFPcrpR7ilScH5Qy8d1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95608F7026D0EDD350F314E06E057045FA821C32FDCD1CB786A824F4B255583A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [onActive9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#onactive) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('onActive')
        .onClick(() => {
          this.controller.onActive()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### onInactive(deprecated)

onInactive(): void

Called when the **Web** component enters the inactive state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/4y796LHyRBGWTnaQGACx1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0873C7E945D59F9C97CF052C8DFE4E5741B4756799E8DC8F73740CB7B55484C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [onInactive9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#oninactive) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('onInactive')
        .onClick(() => {
          this.controller.onInactive()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### zoom(deprecated)

zoom(factor: number): void

Sets a zoom factor for the current web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/dCmsxE9ARZCOx2XJ6ViNoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5052F9C8E92F602F52A947D7C54797A4A2068090D745DA7D1142F0D7B4F0D35A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [zoom9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#zoom) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| factor | number | Yes | Zoom factor to set. A positive value indicates zoom-in, and a negative value indicates zoom-out. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State factor: number = 1

  build() {
    Column() {
      Button('zoom')
        .onClick(() => {
          this.controller.zoom(this.factor)
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### refresh(deprecated)

refresh()

Called when the **Web** component refreshes the web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/RguLSNekTZuWriMSau7bLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=731D185679C4E9D7E349FCAC854C3811D6A6ED54EC0823FAB5ACC80DBBF98D6A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [refresh9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#refresh) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          this.controller.refresh()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### registerJavaScriptProxy(deprecated)

registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })

Registers a JavaScript object with the window. APIs of this object can then be invoked in the window. You must invoke the [refresh](#refreshdeprecated) API for the registration to take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/EyZYXSQjSj64qgj_kM5r_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06937E17CCB978FE8AD58135AC9BA0A730B46F4280D0E39A98401896D2C4115A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [registerJavaScriptProxy9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#registerjavascriptproxy) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| object | object | Yes | Application-side JavaScript object to be registered. Methods and attributes can be declared, but cannot be directly called on HTML5. The parameters and return value can only be of the string, number, or Boolean type. |
| name | string | Yes | Name of the object to be registered, which is the same as that invoked in the window. After registration, the window can use this name to access the JavaScript object at the application side. |
| methodList | Array<string> | Yes | Methods of the JavaScript object to be registered at the application side. |

**Example**

// xxx.ets
class TestObj {
  constructor() {
  }

  test(): string {
    return "ArkUI Web Component"
  }

  toString(): void {
    console.info('Web Component toString')
  }
}

@Entry
@Component
struct Index {
  controller: WebController = new WebController()
  testObj = new TestObj();
  build() {
    Column() {
      Row() {
        Button('Register JavaScript To Window').onClick(() => {
          this.controller.registerJavaScriptProxy({
            object: this.testObj,
            name: "objName",
            methodList: \["test", "toString"\],
          })
        })
      }
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        Hello world!
        <script type="text/javascript">
            function htmlTest() {
                str = objName.test("test function")
                console.info('objName.test result:'+ str)
            }
        </script>
    </body>
</html>

#### runJavaScript(deprecated)

runJavaScript(options: { script: string, callback?: (result: string) => void })

Executes a JavaScript script. This API uses an asynchronous callback to return the script execution result. **runJavaScript** can be invoked only after **loadUrl** is executed. For example, it can be invoked in **onPageEnd**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/RL1TSFclSx6CfTI3kBECRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE470172353EDD01581728C95C4CA1BEC4471544C8BF46885ACCCDE73293D4A3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [runJavaScript9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#runjavascript) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| script | string | Yes | JavaScript script. |
| callback | (result: string) => void | No | Callback used to return the result. Returns **null** if the JavaScript script fails to be executed or no value is returned. |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State webResult: string = ''
  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
      .javaScriptAccess(true)
      .onPageEnd((event) => {
        this.controller.runJavaScript({
          script: 'test()',
          callback: (result: string)=> {
            this.webResult = result
            console.info(\`The test() return value is: ${result}\`)
          }})
        if (event) {
          console.info('url: ', event.url)
        }
      })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8">
  </head>
  <body>
      Hello world!
      <script type="text/javascript">
          function test() {
              console.info('Ark WebComponent')
              return "This value is from index.html"
          }
      </script>
  </body>
</html>

#### stop(deprecated)

stop()

Stops page loading.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/sd99dH5bS9yDqDOz8IwK9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E0349BF896F39AE7023FC116BAA571D0DD84F44D498D8D23CBD0B0C2A171B7A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [stop9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#stop) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('stop')
        .onClick(() => {
          this.controller.stop()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearHistory(deprecated)

clearHistory(): void

Clears the browsing history.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/LWMiNwQfRp6P4yfyb_2Bgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EC066AD278D18E57F5F9879577FEF4D1D07893E9F16F0BAFD67E9123C66F02C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [clearHistory9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#clearhistory) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()

  build() {
    Column() {
      Button('clearHistory')
        .onClick(() => {
          this.controller.clearHistory()
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
