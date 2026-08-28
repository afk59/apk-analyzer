# Attributes

Only the [aspectRatio](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/layout-constraints/document.md#aspectratio), [backdropBlur](../../../../arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#backdropblur), [backgroundColor](../../../../arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundcolor), [bindContentCover](../../../../arkui/arkts-components/universal-attributes/transition/modal-transition/document.md#bindcontentcover), [bindContextMenu](../../../../arkui/arkts-components/universal-attributes/dialog-box-control/menu-control/document.md#bindcontextmenu8), [bindMenu](../../../../arkui/arkts-components/universal-attributes/dialog-box-control/menu-control/document.md#bindmenu), [bindSheet](../../../../arkui/arkts-components/universal-attributes/transition/sheet-transition/document.md#bindsheet), [borderColor](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/border-styling/document.md#bordercolor), [borderRadius](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/border-styling/document.md#borderradius), [borderStyle](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/border-styling/document.md#borderstyle), [borderWidth](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/border-styling/document.md#borderwidth), [clip](../../../../arkui/arkts-components/universal-attributes/visual-effects/shape-clipping/document.md#clip12), [constraintSize](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#constraintsize), [defaultFocus](../../../../arkui/arkts-components/universal-attributes/interaction-properties/focus-control/document.md#defaultfocus9), [focusable](../../../../arkui/arkts-components/universal-attributes/interaction-properties/focus-control/document.md#focusable), [tabIndex](../../../../arkui/arkts-components/universal-attributes/interaction-properties/focus-control/document.md#tabindex9), [groupDefaultFocus](../../../../arkui/arkts-components/universal-attributes/interaction-properties/focus-control/document.md#groupdefaultfocus9), [displayPriority](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/layout-constraints/document.md#displaypriority), [enabled](../../../../arkui/arkts-components/universal-attributes/interaction-properties/enable-disable-control/document.md#enabled), [flexBasis](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/flex-layout/document.md#flexbasis), [flexShrink](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/flex-layout/document.md#flexshrink), [layoutWeight](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#layoutweight), [id](../../../../arkui/arkts-components/universal-attributes/basic-attributes/component-id/document.md#id), [gridOffset](../../../../arkui/arkts-components/components-and-apis-no-longer-maintained/grid/document.md#attributes), [gridSpan](../../../../arkui/arkts-components/components-and-apis-no-longer-maintained/grid/document.md#attributes), [useSizeType](../../../../arkui/arkts-components/components-and-apis-no-longer-maintained/grid/document.md#attributes), [height](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#height), [touchable](../../../../arkui/arkts-components/components-and-apis-no-longer-maintained/click-control/document.md#touchabledeprecated), [margin](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#margin), [markAnchor](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/location/document.md#markanchor), [offset](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/location/document.md#offset), [width](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#width), [zIndex](../../../../arkui/arkts-components/universal-attributes/basic-attributes/z-order-control/document.md#zindex), [visibility](../../../../arkui/arkts-components/universal-attributes/basic-attributes/visibility-control/document.md#visibility), [scale](../../../../arkui/arkts-components/universal-attributes/visual-effects/transformation/document.md#scale), [translate](../../../../arkui/arkts-components/universal-attributes/visual-effects/transformation/document.md#translate), [responseRegion](../../../../arkui/arkts-components/universal-attributes/interaction-properties/touch-interactions/touch-target/document.md#responseregion), [size](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#size), [opacity](../../../../arkui/arkts-components/universal-attributes/visual-effects/opacity-control/document.md#opacity), [shadow](../../../../arkui/arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadow), [sharedTransition](../../../../arkui/arkts-components/animation/shared-element-transition-sharedtransition/document.md), [transition](../../../../arkui/arkts-components/animation/component-transition-transition/document.md), [position](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/location/document.md#position), and [direction](../../../../arkui/arkts-components/universal-attributes/layout-and-borders/location/document.md#direction) attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/SPyrpoGLTS2JVpb3Ki5SVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1C5BC80B5A73391677CAE69B8BAE047C997CEF49E510F1BE814BC9717AC4D45)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The sample effect is subject to the actual device.
    

#### domStorageAccess

domStorageAccess(domStorageAccess: boolean)

Sets whether to enable the DOM Storage API permission. If this attribute is not explicitly called, the DOM Storage API permission is disabled by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domStorageAccess | boolean | Yes | 
Whether to enable the DOM Storage API.

The value **true** means to the DOM Storage API, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/UP0VJ9E3Q5GkuI41t3CceA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73DBC9367B579BF54B4A8E28ECBDD1E22956014D3545A195043066347E6185E1)

-   A web page can be loaded only when its DOM Storage API is set to **true**.

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .domStorageAccess(true)
    }
  }
}

#### fileAccess

fileAccess(fileAccess: boolean)

Sets whether to enable access to the file system in the application. This setting does not affect the access to the files specified through [$rawfile(filepath/filename)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#accessing-resources). For API version 11 and earlier versions, access to the file system in the application is enabled by default if this attribute is not explicitly called. Since API version 12, access to the file system in the application is disabled by default if this attribute is not explicitly called.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fileAccess | boolean | Yes | 
Whether to enable access to the file system in the application.

The value **true** means to enable access to the file system in the application, and **false** means the opposite.

When **fileAccess** is set to **false**, only the resources in the read-only resource directory **/data/storage/el1/bundle/entry/resources/resfile** can be accessed using the file protocol, regardless of the value of **fileAccess**.

For API version 11 and earlier versions, if **undefined** or **null** is passed in, the value is **true**. Since API version 12, if **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(true)
    }
  }
}

#### imageAccess

imageAccess(imageAccess: boolean)

Sets whether to enable automatic image loading. When this attribute is not explicitly called, automatic loading of image resources is allowed.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| imageAccess | boolean | Yes | 
Whether to enable automatic image loading.

The value **true** means to enable automatic image loading, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .imageAccess(true)
    }
  }
}

#### javaScriptProxy

javaScriptProxy(javaScriptProxy: JavaScriptProxy)

Registers an ArkTS object in **javaScriptProxy** with the **Web** component. The object is registered with all frameworks of the web page, including all iframes, using the name specified in **JavaScriptProxy**. This enables JavaScript to invoke methods of the ArkTS object in **javaScriptProxy**. When this attribute is not explicitly called, the ArkTS object in javaScriptProxy is not registered with the **Web** component by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/FqkmR3aUShyeOpcjYYwWJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC60305C3F89D3B96A6AB0082562B00C0D6DC9681AE917AB2DB3FD826577FD42)

The **javaScriptProxy** API must be used in pair with the [deleteJavaScriptRegister9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#deletejavascriptregister) API to prevent memory leaks.

All parameters of the **javaScriptProxy** object cannot be updated.

When registering a **javaScriptProxy** object, select at least one of the synchronous and asynchronous method lists, or both.

Only one object can be registered through this API. To register multiple objects, use [registerJavaScriptProxy9+](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#registerjavascriptproxy).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| javaScriptProxy | [JavaScriptProxy](../interfaces-others/document.md#javascriptproxy12) | Yes | 
Object to be registered. Methods can be declared, but attributes cannot.

When **undefined** or **null** is passed in, the ArkTS object in javaScriptProxy is not registered with the **Web** component.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(data1: string, data2: string, data3: string): string {
    console.info("data1:" + data1);
    console.info("data2:" + data2);
    console.info("data3:" + data3);
    return "AceString";
  }

  asyncTest(data: string): void {
    console.info("async data:" + data);
  }

  toString(): void {
    console.info('toString' + "interface instead.");
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  testObj = new TestObj();
  build() {
    Column() {
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .javaScriptAccess(true)
        .javaScriptProxy({
          object: this.testObj,
          name: "objName",
          methodList: \["test", "toString"\],
          asyncMethodList: \["asyncTest"\],
          controller: this.controller,
      })
    }
  }
}

#### javaScriptAccess

javaScriptAccess(javaScriptAccess: boolean)

Sets whether JavaScript scripts can be executed. When this attribute is not explicitly called, JavaScript scripts can be executed by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| javaScriptAccess | boolean | Yes | 
Whether JavaScript scripts can be executed.

The value **true** indicates that JavaScript scripts can be executed, and **false** indicates the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}

#### overScrollMode11+

overScrollMode(mode: OverScrollMode)

Sets whether to enable overscroll mode. When overscroll mode is enabled and the boundary of the web page is reached, the **Web** component plays a bounce effect animation and return to the page. The internal page on the root page does not trigger bounce. When this attribute is not explicitly called, the overscroll mode is disabled by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [OverScrollMode](../enums/document.md#overscrollmode11) | Yes | 
Whether to enable the overscroll mode.

When **undefined** or **null** is passed in, the value is **OverScrollMode.NEVER**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: OverScrollMode = OverScrollMode.ALWAYS;
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .overScrollMode(this.mode)
    }
  }
}

#### mixedMode

mixedMode(mixedMode: MixedMode)

Sets the behavior when a secure source attempts to load resources from an insecure source. When this attribute is not explicitly called, the default value is **MixedMode.None**, which means that secure sources are not allowed to load content from insecure sources.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mixedMode | [MixedMode](../enums/document.md#mixedmode) | Yes | 
Mixed content mode to be set.

If **undefined** or **null** is passed in, the value **MixedMode.All** is used.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: MixedMode = MixedMode.All;
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .mixedMode(this.mode)
    }
  }
}

#### onlineImageAccess

onlineImageAccess(onlineImageAccess: boolean)

Sets whether to enable access to online images through HTTP and HTTPS. When this attribute is not explicitly called, online image resources can be loaded by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| onlineImageAccess | boolean | Yes | 
Whether to enable access to online images through HTTP and HTTPS.

The value **true** means to enable access to online images through HTTP and HTTPS, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onlineImageAccess(true)
    }
  }
}

#### zoomAccess

zoomAccess(zoomAccess: boolean)

Sets whether to enable zoom gestures. When this attribute is not explicitly called, zoom gestures are supported by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| zoomAccess | boolean | Yes | 
Whether to enable zoom gestures.

The value **true** means to enable zoom gestures, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}

#### overviewModeAccess

overviewModeAccess(overviewModeAccess: boolean)

Sets whether to load web pages by using the overview mode. That is, zoom out the content to fit the screen width. When this attribute is not explicitly called, web pages can be loaded in overview mode by default.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior**: This API has no effect on the PCs/2-in-1 devices and works on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| overviewModeAccess | boolean | Yes | 
Whether to load web pages by using the overview mode.

The value **true** means to load web pages by using the overview mode, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .overviewModeAccess(true)
    }
  }
}

#### databaseAccess

databaseAccess(databaseAccess: boolean)

Sets whether to enable the Web SQL Database storage API permission. If this permission is not explicitly called, it is disabled by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/2q803V67TPaNcvkkCQG_ow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CE0ECA84897027C2042FAFBB4CE3B3D8042B38E91C947AF8BF8A73977D6B2ED)

-   After the ArkWeb kernel is upgraded to M132, the API's control over the Web SQL Database becomes invalid because the kernel discards Web SQL. For details about the ArkWeb kernel version, see [Constraints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-component-overview#constraints).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| databaseAccess | boolean | Yes | 
Whether to enable Web SQL Database storage API permission.

**true** means enabling the detection, and **false** means disabling it.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .databaseAccess(true)
    }
  }
}

#### geolocationAccess

geolocationAccess(geolocationAccess: boolean)

Sets whether to enable geolocation access. When this attribute is not explicitly called, geolocation access is enabled by default. For details, see [Managing Location Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-geolocation-permission).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| geolocationAccess | boolean | Yes | 
Whether to enable geolocation access.

The value **true** means to enable geolocation access, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .geolocationAccess(true)
    }
  }
}

#### mediaPlayGestureAccess9+

mediaPlayGestureAccess(access: boolean)

Sets whether video playback must be started by user gestures. This API is not applicable to muted videos. When this attribute is not explicitly set, users need to click the video to play it by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| access | boolean | Yes | 
Whether video playback must be started by user gestures.

The value **true** indicates that video playback must be started by user gestures, and **false** indicates the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State access: boolean = true;

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .mediaPlayGestureAccess(this.access)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Video Playback Page</title>
</head>
<body>
<h1>Video Playback</h1>
<video id="testVideo" controls autoplay>
    // Configure the autoplay attribute in the video tag to allow automatic video playback.
    // Save an MP4 media file in the rawfile directory of resources and name it example.mp4.
    <source src="example.mp4" type="video/mp4">
</video>
</body>
</html>

#### multiWindowAccess9+

multiWindowAccess(multiWindow: boolean)

Sets whether to enable the multi-window permission.

Enabling the multi-window permission requires implementation of the **onWindowNew** event. For the sample code, see [onWindowNew](../events/document.md#onwindownew9).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| multiWindow | boolean | Yes | 
Whether to enable the multi-window permission.

The value **true** means to enable the multi-window permission, and **false** means the opposite.

The default value is **false**.

 |

#### horizontalScrollBarAccess9+

horizontalScrollBarAccess(horizontalScrollBar: boolean)

Sets whether to display the horizontal scrollbar, including the default system scrollbar and custom scrollbar. When this attribute is not explicitly called, the horizontal scrollbar is displayed by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/DbdlwQ4FSum_Qrl-YANwAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F19E78247A9A2ACA6951959F2920801076C5CC499AC79CB081E96360DBACE35)

-   If an @State decorated variable is used to control the horizontal scrollbar visibility, [controller.refresh()](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#refresh) must be called for the settings to take effect.
-   If the vertical scrollbar visibility changes frequently through an @State decorated variable, it is recommended that the variable correspond to the **Web** component one by one.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| horizontalScrollBar | boolean | Yes | 
Whether to display the horizontal scrollbar.

The value **true** means to display the horizontal scrollbar, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State isShow: boolean = true;
  @State btnMsg: string ="Hide the scrollbar";

  build() {
    Column() {
      // If an @State decorated variable is used to control the horizontal scrollbar visibility, controller.refresh() must be called for the settings to take effect.
      Button('refresh')
        .onClick(() => {
          if(this.isShow){
            this.isShow = false;
            this.btnMsg="Display the scrollbar";
          }else{
            this.isShow = true;
            this.btnMsg="Hide the scrollbar";
          }
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        }).height("10%").width("40%")
      Web({ src: $rawfile('index.html'), controller: this.controller }).height("90%")
        .horizontalScrollBarAccess(this.isShow)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
    <title>Demo</title>
    <style>
        body {
          width:3000px;
          height:6000px;
          padding-right:170px;
          padding-left:170px;
          border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### verticalScrollBarAccess9+

verticalScrollBarAccess(verticalScrollBar: boolean)

Sets whether to display the vertical scrollbar, including the default system scrollbar and custom scrollbar. When this attribute is not explicitly called, the vertical scrollbar is displayed by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/rggIN5SrQ_qkS8hvjxAv-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0787F035AD7D3EF89BCC02DD9C55A640C26234C3C0A0DD4F16201E123DD52FE)

-   If an @State decorated variable is used to control the vertical scrollbar visibility, **controller.refresh()** must be called for the settings to take effect.
-   If the vertical scrollbar visibility changes frequently through an @State decorated variable, it is recommended that the variable correspond to the **Web** component one by one.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| verticalScrollBar | boolean | Yes | 
Whether to display the vertical scrollbar.

The value **true** means to display the vertical scrollbar, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State isShow: boolean = true;
  @State btnMsg: string ="Hide the scrollbar";

  build() {
    Column() {
      // If an @State decorated variable is used to control the vertical scrollbar visibility, controller.refresh() must be called for the settings to take effect.
      Button(this.btnMsg)
        .onClick(() => {
          if(this.isShow){
            this.isShow = false;
            this.btnMsg="Display the scrollbar";
          }else{
            this.isShow = true;
            this.btnMsg="Hide the scrollbar";
          }
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        }).height("10%").width("40%")
      Web({ src: $rawfile('index.html'), controller: this.controller }).height("90%")
        .verticalScrollBarAccess(this.isShow)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
    <title>Demo</title>
    <style>
        body {
          width:3000px;
          height:6000px;
          padding-right:170px;
          padding-left:170px;
          border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### cacheMode

cacheMode(cacheMode: CacheMode)

Sets the cache mode. When this attribute is not explicitly called, the default value **CacheMode.Default** is used.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cacheMode | [CacheMode](../enums/document.md#cachemode) | Yes | 
Cache mode to set.

When **undefined** or **null** is passed in, the value is **CacheMode.Default**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: CacheMode = CacheMode.None;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .cacheMode(this.mode)
    }
  }
}

#### copyOptions11+

copyOptions(value: CopyOptions)

Sets the pasteboard copy options. When this attribute is not explicitly called, the copied content can be pasted in all applications on the current device by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CopyOptions](../../../../arkui/arkts-components/common-definitions/enums/document.md#copyoptions9) | Yes | 
Pasteboard copy options.

When **undefined** or **null** is passed in, the value is **CopyOptions.None**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .copyOptions(CopyOptions.None)
    }
  }
}

#### textZoomRatio9+

textZoomRatio(textZoomRatio: number)

Sets the text zoom ratio of the page. When this attribute is not explicitly called, the default zoom ratio is 100%.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| textZoomRatio | number | Yes | 
Text zoom ratio to set.

The value is an integer. The value range is (0, 2147483647\].

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State ratio: number = 150;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .textZoomRatio(this.ratio)
    }
  }
}

#### initialScale9+

initialScale(percent: number)

Sets the scale factor of the entire page. When this attribute is not explicitly called, the default scale factor is 100%.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| percent | number | Yes | 
Scale factor of the entire page.

Value range: (0, 1000\]

When **undefined** or **null** is passed in, the attribute setting does not take effect.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State percent: number = 100;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .initialScale(this.percent)
    }
  }
}

#### blockNetwork9+

blockNetwork(block: boolean)

Sets whether to block online downloads. When this attribute is not explicitly called, online resources can be loaded by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| block | boolean | Yes | 
Whether to allow online downloads.

The value **true** means to block online downloads, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State block: boolean = true;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .blockNetwork(this.block)
    }
  }
}

#### defaultFixedFontSize9+

defaultFixedFontSize(size: number)

Sets the default fixed font size for the web page. For HTML elements that use the **monospace** font and do not specify **font-size**, the font size is rendered based on this value.

When this attribute is not explicitly called, the default fixed font size is **13**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | 
Default fixed font size to set, in px.

Value range: \[-2^31, 2^31-1\]. In actual rendering, values greater than 72 px are handled as 72 px, and values less than 1 px are handled as 1 px.

When **null** or **undefined** is passed in, the value is **13**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 16;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .defaultFixedFontSize(this.fontSize)
    }
  }
}

#### defaultFontSize9+

defaultFontSize(size: number)

Sets the default font size for the web page. For HTML elements that use non-monospace fonts and do not specify **font-size**, the font size is rendered based on this value.

When this attribute is not explicitly called, the default font size of the web page is **16**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | 
Default font size to set, in px.

Value range: \[-2^31, 2^31-1\]. In actual rendering, values greater than 72 px are handled as 72 px, and values less than 1 px are handled as 1 px.

When **null** or **undefined** is passed in, the value is **16**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 13;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .defaultFontSize(this.fontSize)
    }
  }
}

#### minFontSize9+

minFontSize(size: number)

Sets the minimum font size for the web page. If the font size of HTML elements is smaller than the value set by this API, the font size is rendered based on the value set by this API.

When no attribute is explicitly called, the default minimum font size of the web page is **8**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | 
Minimum font size to set, in px.

Value range: \[-2^31, 2^31-1\]. In actual rendering, values greater than 72 px are handled as 72 px, and values less than 1 px are handled as 1 px.

When **null** or **undefined** is passed in, the value is **8**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 13;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .minFontSize(this.fontSize)
    }
  }
}

#### minLogicalFontSize9+

minLogicalFontSize(size: number)

Sets the minimum logical font size for the web page.

For HTML elements whose font size is not specified:

1.  If the font size of the element is smaller than the value set by this API, the font size is rendered based on the API value.
2.  If **minLogicalFontSize** and **minFontSize** are both set, the larger value of the two will be used for elements whose font size is not specified.

When this attribute is not explicitly called, the default minimum logical font size of the web page is **8**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | 
Minimum logical font size to set, in px.

Value range: \[-2^31, 2^31-1\]. In actual rendering, values greater than 72 px are handled as 72 px, and values less than 1 px are handled as 1 px.

When **null** or **undefined** is passed in, the value is **18**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 13;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .minLogicalFontSize(this.fontSize)
    }
  }
}

#### webFixedFont9+

webFixedFont(family: string)

Sets the fixed font family of the web page to render HTML elements that use the **monospace** font.

When this attribute is not explicitly called, the default fixed font family of the web page is **monospace**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| family | string | Yes | 
Fixed font family to set.

When **null** or **undefined** is passed in, the value is **monospace**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "monospace";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webFixedFont(this.family)
    }
  }
}

#### webSansSerifFont9+

webSansSerifFont(family: string)

Sets the sans-serif font family of the web page to render HTML elements that use the **sans-serif** font.

When this attribute is not explicitly called, the sans-serif font family of the web page is **sans-serif** by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| family | string | Yes | 
Sans-serif font family to set.

When **null** or **undefined** is passed in, the sans-serif font family is **sans-serif**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "sans-serif";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webSansSerifFont(this.family)
    }
  }
}

#### webSerifFont9+

webSerifFont(family: string)

Sets the serif font family of the web page to render HTML elements that use the **serif** font.

When this attribute is not explicitly called, the default serif font family of the web page is **serif**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| family | string | Yes | 
Serif font family to set.

When **null** or **undefined** is passed in, the sans-serif font family is **serif**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "serif";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webSerifFont(this.family)
    }
  }
}

#### webStandardFont9+

webStandardFont(family: string)

Sets the standard font family of the web page to render HTML elements whose font style is not specified.

When this attribute is not explicitly called, the default standard font family of the web page is **sans-serif**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| family | string | Yes | 
Standard font family to set.

When **null** or **undefined** is passed in, the sans-serif font family is **sans-serif**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "sans-serif";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webStandardFont(this.family)
    }
  }
}

#### webFantasyFont9+

webFantasyFont(family: string)

Sets the fantasy font family of the web page to render HTML elements that use the **fantasy** font.

When this attribute is not explicitly called, the default fantasy font family of the web page is **fantasy**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| family | string | Yes | 
Fantasy font family to set.

When **null** or **undefined** is passed in, the value is **fantasy**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "fantasy";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webFantasyFont(this.family)
    }
  }
}

#### webCursiveFont9+

webCursiveFont(family: string)

Sets the cursive font family of the web page to render HTML elements that use the **cursive** font.

When this attribute is not explicitly called, the default cursive font family of the web page is **cursive**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| family | string | Yes | 
Cursive font family to set.

When **null** or **undefined** is passed in, the value is **cursive**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "cursive";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webCursiveFont(this.family)
    }
  }
}

#### darkMode9+

darkMode(mode: WebDarkMode)

Sets dark mode for the web page. When this attribute is not explicitly called, dark mode is disabled by default.

When dark mode is enabled, the **Web** component enables the dark style defined in the media query **prefers-color-scheme** of the web page. If it is not defined, the web page remains unchanged. To enable forcible dark mode, use this API with [forceDarkAccess](#forcedarkaccess9). For details about how to use dark mode, see [Setting Dark Mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-set-dark-mode).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [WebDarkMode](../enums/document.md#webdarkmode9) | Yes | 
Dark mode for the web page, which can be set to **Off**, **On**, or **Auto**.

When **null** or **undefined** is passed, the value is **WebDarkMode.Off**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: WebDarkMode = WebDarkMode.On;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .darkMode(this.mode)
    }
  }
}

#### forceDarkAccess9+

forceDarkAccess(access: boolean)

Sets whether to enable forcible dark mode for the web page. This API is applicable only when [darkMode](#darkmode9) is enabled. When this attribute is not explicitly called, forcible dark mode is disabled for the web page by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| access | boolean | Yes | 
Whether to enable forcible dark mode for the web page.

The value **true** means to enable forcible dark mode for the web page, and **false** means the opposite.

When **null** or **undefined** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: WebDarkMode = WebDarkMode.On;
  @State access: boolean = true;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .darkMode(this.mode)
        .forceDarkAccess(this.access)
    }
  }
}

#### pinchSmooth9+

pinchSmooth(isEnabled: boolean)

Sets whether to enable pinch smooth mode for the web page. When this attribute is not explicitly called, pinch smooth mode is disabled by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | boolean | Yes | 
Whether to enable pinch smooth mode for the web page.

The value **true** means to enable pinch smooth mode, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .pinchSmooth(true)
    }
  }
}

#### allowWindowOpenMethod10+

allowWindowOpenMethod(flag: boolean)

Sets whether to allow a new window to automatically open through JavaScript.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/CyOk2LkHS1uI2Y7ssUH5Bw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3FAFF909CF7C483D945AEDDCB2E788FE1A7EF9756114494B81FE89269DF66E1)

-   This API takes effect only when [javaScriptAccess](#javascriptaccess) is enabled.
-   This API opens a new window when [multiWindowAccess](#multiwindowaccess9) is enabled, and a local window when it is disabled.
-   The default value of **flag** is subject to the settings of the **persist.web.allowWindowOpenMethod.enabled** system attribute. If this attribute is not set, the default value of **flag** is **false**.
-   Run the **hdc shell param get persist.web.allowWindowOpenMethod.enabled** command to check whether the system attribute **persist.web.allowWindowOpenMethod.enabled** is enabled. If the attribute value is **1**, the system attribute is enabled. If the attribute value is **0** or does not exist, the system attribute is disabled. You can run the **hdc shell param set persist.web.allowWindowOpenMethod.enabled 1** command to enable the system attribute.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flag | boolean | Yes | 
Whether to allow a new window to automatically open through JavaScript. The value **true** means to allow a new window to automatically open through JavaScript, and **false** means only to allow a new window to automatically open through JavaScript using user behaviors.

The user behavior here refers to a user requests to open a new window (**window.open**) within 5 seconds after operating the **Web** component.

The default value of **flag** is subject to the settings of the **persist.web.allowWindowOpenMethod.enabled** system attribute. If this attribute is set to **true**, the default value of **flag** is **true**. If this attribute is not set, the default value of **flag** is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

// There are two Web components on the same page. When the WebComponent object opens a new window, the NewWebViewComp object is displayed.
@CustomDialog
struct NewWebViewComp {
    controller?: CustomDialogController;
    webviewController1: webview.WebviewController = new webview.WebviewController();

    build() {
        Column() {
            Web({ src: "", controller: this.webviewController1 })
                .javaScriptAccess(true)
                .multiWindowAccess(false)
                .onWindowExit(() => {
                    console.info("NewWebViewComp onWindowExit");
                    if (this.controller) {
                        this.controller.close();
                    }
                })
                .onActivateContent(() => {
                    // To display the web page to the foreground, the application should perform a tab or window switch.
                    console.info("NewWebViewComp onActivateContent")
                })
        }
    }
}

@Entry
@Component
struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();
    dialogController: CustomDialogController | null = null;

    build() {
        Column() {
            Web({ src: $rawfile("index.html"), controller: this.controller })
                .javaScriptAccess(true)
                // MultiWindowAccess needs to be enabled.
                .multiWindowAccess(true)
                .allowWindowOpenMethod(true)
                .onWindowNew((event) => {
                    if (this.dialogController) {
                        this.dialogController.close()
                    }
                    let popController: webview.WebviewController = new webview.WebviewController();
                    this.dialogController = new CustomDialogController({
                        builder: NewWebViewComp({ webviewController1: popController }),
                        // Set isModal to false to prevent the new window from being destroyed, so that the onActivateContent callback can be triggered.
                        isModal: false
                    })
                    this.dialogController.open();
                    // Return the WebviewController object corresponding to the new window to the web kernel.
                    // If the event.handler.setWebController API is not called, the render process will be blocked.
                    // If no new window is created, set the value of event.handler.setWebController to null to notify the Web component that no new window is created.
                    event.handler.setWebController(popController);
                })
        }
    }
}

**Example of the HTML file**

<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<div>
    <button type="button" onclick="delayOpenwindow(5000)">delayOpenwindow\_5s</button>
</div>

<script>
    function openwindowAll(){
        open("https://www.example.com","\_blank","height=400,width=600,top=100,left=100,scrollbars=no")
    }
    function delayOpenwindow(t){
        setTimeout(openwindowAll, t);
    }
</script>
</body>
</html>

#### mediaOptions10+

mediaOptions(options: WebMediaOptions)

Sets the web-based media playback policy, including the validity period for automatically resuming a paused web audio, and whether the audio of multiple **Web** instances in an application is exclusive. When this attribute is not explicitly set, the web audio cannot be automatically resumed after regaining the focus by default, and the audio of multiple **Web** instances in an application is exclusive.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/JWWJ5utzTbuPb1DDqfLtlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08BD391EBC4744C9CD9679BD6C14D984782D32837FBCA67C439F5FD9392B3A9F)

-   Audios in the same **Web** instance are considered as the same audio.
-   The media playback policy controls videos with an audio track.
-   You are advised to set [audioExclusive](../interfaces-others/document.md#webmediaoptions10) to the same value for all **Web** components.
-   Audio and video interruption takes effect within an application and between applications, and playback resumption takes effect only between applications.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [WebMediaOptions](../interfaces-others/document.md#webmediaoptions10) | Yes | 
Web-based media playback policy.

After the parameter settings are updated, the playback must be started again for the settings to take effect.

When **undefined** or **null** is passed in, **{resumeInterval: 0, audioExclusive: true}** is used.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State options: WebMediaOptions = {resumeInterval: 10, audioExclusive: true};

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .mediaOptions(this.options)
    }
  }
}

#### javaScriptOnDocumentStart11+

javaScriptOnDocumentStart(scripts: Array<ScriptItem>)

Injects a JavaScript script into the **Web** component. When the specified page or document starts to be loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/ezXIqZ4NRt20K5Sh-LvVjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=814B70DD93FF0CBF82D247EAA41B452224F3F85DF38125F3A7F4494FE67D901B)

-   Inject the script after the root element (HTML Element) of the web page file is created, but before any other content is loaded.
    
-   This script is executed in lexicographical order in this API. To execute the script in array order, you are advised to use the [runJavaScriptOnDocumentStart](#runjavascriptondocumentstart15) API.
    
-   You are not advised to use this API together with [runJavaScriptOnDocumentStart](#runjavascriptondocumentstart15).
    
-   If a script with the same content is injected for multiple times, the script is silently deduplicated, not displayed, and no notification is displayed. The **scriptRules** of the first injection is used.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scripts | Array<[ScriptItem](../interfaces-others/document.md#scriptitem11)\> | Yes | 
Script item array to be injected.

When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components.

 |

**Example of the .ets file**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
    controller: webview.WebviewController = new webview.WebviewController();
    private localStorage: string =
        "if (typeof(Storage) !== 'undefined') {" +
        "   localStorage.setItem('color', 'Red');" +
        "}";
    @State scripts: Array<ScriptItem> = \[
        { script: this.localStorage, scriptRules: \["\*"\] }
    \];

    build() {
        Column({ space: 20 }) {
            Web({ src: $rawfile('index.html'), controller: this.controller })
                .javaScriptAccess(true)
                .domStorageAccess(true)
                .backgroundColor(Color.Grey)
                .javaScriptOnDocumentStart(this.scripts)
                .width('100%')
                .height('100%')
        }
    }
}

**Example of the HTML file**

<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
      Hello world!
      <div id="result"></div>
  </body>
  <script type="text/javascript">
    function bodyOnLoadLocalStorage() {
      if (typeof(Storage) !== 'undefined') {
        document.getElementById('result').innerHTML = localStorage.getItem('color');
      } else {
        document.getElementById('result').innerHTML = 'Your browser does not support localStorage.';
      }
    }
  </script>
</html>

#### javaScriptOnDocumentEnd11+

javaScriptOnDocumentEnd(scripts: Array<ScriptItem>)

Injects a JavaScript script into the **Web** component. When the specified page or document has been loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/0jSoUSXTSu-yIbno1_LnGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9341DA8BC59ACB551772574B3E0D2D5496EB730E51CC65559D5B1A455D6F9049)

-   The script runs before any JavaScript code of the page, when the DOM tree has been loaded and rendered.
    
-   The script is executed in the lexicographical order, not the array order.
    
-   You are not advised to use this API together with [runJavaScriptOnDocumentEnd](#runjavascriptondocumentend15).
    
-   If a script with the same content is injected for multiple times, the script is silently deduplicated, not displayed, and no notification is displayed. The **scriptRules** of the first injection is used.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scripts | Array<[ScriptItem](../interfaces-others/document.md#scriptitem11)\> | Yes | 
Script item array to be injected.

When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  private jsStr: string =
    "window.document.getElementById(\\"result\\").innerHTML = 'this is msg from javaScriptOnDocumentEnd'";
  @State scripts: Array<ScriptItem> = \[
    { script: this.jsStr, scriptRules: \["\*"\] }
  \];

  build() {
    Column({ space: 20 }) {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .javaScriptOnDocumentEnd(this.scripts)
        .width('100%')
        .height('100%')
    }
  }
}

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;">
Hello world!
<div id="result">test msg</div>
</body>
</html>

#### runJavaScriptOnDocumentStart15+

runJavaScriptOnDocumentStart(scripts: Array<ScriptItem>)

Injects a JavaScript script into the **Web** component. When the specified page or document starts to be loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/wlABINXgT5651AU4CAdzyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5326214B16A2535AC85ECC37C532700FA8FEB3BEA1F23869D2257887E52BA806)

-   Inject the script after the root element (HTML Element) of the web page file is created, but before any other content is loaded.
    
-   This script is executed in the array order.
    
-   You are advised not to use this API together with [javaScriptOnDocumentStart](#javascriptondocumentstart11).
    
-   If a script with the same content is injected for multiple times, the script is silently deduplicated, not displayed, and no notification is displayed. The **scriptRules** of the first injection is used.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scripts | Array<[ScriptItem](../interfaces-others/document.md#scriptitem11)\> | Yes | 
Script item array to be injected.

When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components.

 |

**Example of the .ets file**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
    controller: webview.WebviewController = new webview.WebviewController();
    private localStorage: string =
        "if (typeof(Storage) !== 'undefined') {" +
        "   localStorage.setItem('color', 'Red');" +
        "}";
    @State scripts: Array<ScriptItem> = \[
        { script: this.localStorage, scriptRules: \["\*"\] }
    \];

    build() {
        Column({ space: 20 }) {
            Web({ src: $rawfile('index.html'), controller: this.controller })
                .javaScriptAccess(true)
                .domStorageAccess(true)
                .backgroundColor(Color.Grey)
                .runJavaScriptOnDocumentStart(this.scripts)
                .width('100%')
                .height('100%')
        }
    }
}

**Example of the HTML file**

<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
      Hello world!
      <div id="result"></div>
  </body>
  <script type="text/javascript">
    function bodyOnLoadLocalStorage() {
      if (typeof(Storage) !== 'undefined') {
        document.getElementById('result').innerHTML = localStorage.getItem('color');
      } else {
        document.getElementById('result').innerHTML = 'Your browser does not support localStorage.';
      }
    }
  </script>
</html>

#### runJavaScriptOnDocumentEnd15+

runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem>)

Injects a JavaScript script into the **Web** component. When the specified page or document has been loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/QyuYzNzZQymIhcmXo5c-1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3822B19E736F6B960B180A7200E43FE3B0632CEB5F81A118A00F2675D422413)

-   The script runs before any JavaScript code of the page, when the DOM tree has been loaded and rendered.
    
-   This script is executed in the array order.
    
-   You are advised not to use this API together with [javaScriptOnDocumentEnd](#javascriptondocumentend11).
    
-   If a script with the same content is injected for multiple times, the script is silently deduplicated, not displayed, and no notification is displayed. The **scriptRules** of the first injection is used.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scripts | Array<[ScriptItem](../interfaces-others/document.md#scriptitem11)\> | Yes | 
Script item array to be injected.

When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  private jsStr: string =
    "window.document.getElementById(\\"result\\").innerHTML = 'this is msg from runJavaScriptOnDocumentEnd'";
  @State scripts: Array<ScriptItem> = \[
    { script: this.jsStr, scriptRules: \["\*"\] }
  \];

  build() {
    Column({ space: 20 }) {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .runJavaScriptOnDocumentEnd(this.scripts)
        .width('100%')
        .height('100%')
    }
  }
}

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;">
Hello world!
<div id="result">test msg</div>
</body>
</html>

#### runJavaScriptOnHeadEnd15+

runJavaScriptOnHeadEnd(scripts: Array<ScriptItem>)

Injects a JavaScript script into the **Web** component. When the **head** tag of the DOM tree is parsed, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/cOtwZH3LTy2JsG1T5uQEWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34CAF7F709D99029290E682055205AF569E8E3D237DBBC6881FB75128E5F5FB5)

-   This script is executed in the array order.
    
-   If a script with the same content is injected for multiple times, the script is silently deduplicated, not displayed, and no notification is displayed. The **scriptRules** of the first injection is used.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scripts | Array<[ScriptItem](../interfaces-others/document.md#scriptitem11)\> | Yes | 
Script item array to be injected.

When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  private jsStr: string =
    "window.document.getElementById(\\"result\\").innerHTML = 'this is msg from runJavaScriptOnHeadEnd'";
  @State scripts: Array<ScriptItem> = \[
    { script: this.jsStr, scriptRules: \["\*"\] }
  \];

  build() {
    Column({ space: 20 }) {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .runJavaScriptOnHeadEnd(this.scripts)
        .width('100%')
        .height('100%')
    }
  }
}

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;">
Hello world!
<div id="result">test msg</div>
</body>
</html>

#### layoutMode11+

layoutMode(mode: WebLayoutMode)

Sets the web layout mode. When this attribute is not explicitly called, the web layout follows the system mode by default. For details, see [Fitting In the Page Content Layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-fit-content).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/HjvTPDLdSfKez6Kn1GyFEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2545A96E12A49B159E52CDC46A33A6F4A0012F2A7D4C50DBEAA378FC034E14A)

Currently, only two web layout modes are supported: **WebLayoutMode.NONE** and **WebLayoutMode.FIT\_CONTENT**.

The following restrictions apply with the usage of **WebLayoutMode.FIT\_CONTENT**:

-   If the **Web** component is wider or longer than 7680 px, specify the **RenderMode.SYNC\_RENDER** mode when creating the **Web** component; otherwise, the screen may be blank.
-   After the **Web** component is created, dynamic switching of the **layoutMode** is not supported.
-   When the **RenderMode.ASYNC\_RENDER** mode is specified, the width and height of a **Web** component cannot exceed 7680 px.
-   Frequent changes to the page width and height will trigger a re-layout of the **Web** component, which can affect the user experience.
-   Waterfall web pages are not supported (pull down to the bottom to load more).
-   Width adaptation is not supported. Only height adaptation is supported.
-   Because the height is adaptive to the web page height, the component height cannot be changed by modifying the component height attribute.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [WebLayoutMode](../enums/document.md#weblayoutmode11) | Yes | 
Web layout mode.

When **null** or **undefined** is passed in, the value is **WebLayoutMode.NONE**.

 |

**Example**

1.  After specifying the **layoutMode** to **WebLayoutMode.FIT\_CONTENT**, you need to explicitly specify the **renderMode** to **RenderMode.SYNC\_RENDER**. Otherwise, rendering errors may occur when the viewport height exceeds 7680 px in the default **RenderMode.ASYNC\_RENDER**.

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  mode: WebLayoutMode = WebLayoutMode.FIT\_CONTENT;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC\_RENDER })
        .layoutMode(this.mode)
    }
  }
}

1.  After specifying the layoutMode to **WebLayoutMode.FIT\_CONTENT**, you are advised to specify [overScrollMode](#overscrollmode11) to **OverScrollMode.NEVER**. Otherwise, when the web page scrolls to the edge in the nested scrolling scenario, the rebounding effect is triggered first, which affects user experience.

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  layoutMode: WebLayoutMode = WebLayoutMode.FIT\_CONTENT;
  @State overScrollMode: OverScrollMode = OverScrollMode.NEVER;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC\_RENDER })
        .layoutMode(this.layoutMode)
        .overScrollMode(this.overScrollMode)
    }
  }
}

#### nestedScroll11+

nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt)

Sets nested scrolling options.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/aw4OHUcTTfKXk_5pZpuDrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AA0B81259265885FE5607C455FCE11DC764470C0CBE131A3B330952698E0783)

-   You can set the up, down, left, and right directions, or set the forward and backward nested scrolling modes to implement scrolling linkage with the parent component.
-   Containers that support nested scrolling: [Grid](../../../../arkui/arkts-components/scroll-and-swipe/grid/document.md), [List](../../../../arkui/arkts-components/scroll-and-swipe/list/document.md), [Scroll](../../../../arkui/arkts-components/scroll-and-swipe/scroll/document.md), [Swiper](../../../../arkui/arkts-components/scroll-and-swipe/swiper/document.md), [Tabs](../../../../arkui/arkts-components/navigation-and-switching/tabs/document.md), [WaterFlow](../../../../arkui/arkts-components/scroll-and-swipe/waterflow/document.md), [Refresh](../../../../arkui/arkts-components/scroll-and-swipe/refresh/document.md) and [bindSheet](../../../../arkui/arkts-components/universal-attributes/transition/sheet-transition/document.md#bindsheet).
-   Input sources that support nested scrolling: gestures, mouse device, and touchpad.
-   In nested scrolling scenarios, since the **Web** component's over-scrolling to the edge will trigger the over-scroll bounce effect first, it is recommended that you set [overScrollMode](#overscrollmode11) to **OverScrollMode.NEVER** to avoid undermining user experience.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NestedScrollOptions](../../../../arkui/arkts-components/scroll-and-swipe/scrollable-component-common-apis/document.md#nestedscrolloptions10)| [NestedScrollOptionsExt](../interfaces-others/document.md#nestedscrolloptionsext14)14+ | Yes | 
Nested scrolling options.

When the value is of the **NestedScrollOptions** type (forward and backward), the default nested scrolling mode of the **scrollForward** and **scrollBackward** options is [NestedScrollMode.SELF\_FIRST](../../../../arkui/arkts-components/common-definitions/enums/document.md#nestedscrollmode10).

When the value is of the **NestedScrollOptionsExt** type (up, down, left, and right), the default nested scrolling mode of the **scrollUp**, **scrollDown**, **scrollLeft**, and **scrollRight** options is **NestedScrollMode.SELF\_FIRST**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .nestedScroll({
          scrollForward: NestedScrollMode.SELF\_FIRST,
          scrollBackward: NestedScrollMode.SELF\_FIRST,
        })
    }
  }
}

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  build() {
    Scroll(){
      Column() {
        Text("Nested Web")
          .height("25%")
          .width("100%")
          .fontSize(30)
          .backgroundColor(Color.Yellow)
        Web({ src: $rawfile('index.html'),
              controller: this.controller })
          .nestedScroll({
            scrollUp: NestedScrollMode.SELF\_FIRST,
            scrollDown: NestedScrollMode.PARENT\_FIRST,
            scrollLeft: NestedScrollMode.SELF\_FIRST,
            scrollRight: NestedScrollMode.SELF\_FIRST,
          })
      }
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
        font-size:16px;
        height:200px;
        text-align: center;       /\* Horizontally centered \*/
        line-height: 200px;       /\* Vertically centered (the height matches the container height) \*/
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>

#### bypassVsyncCondition20+

bypassVsyncCondition(condition: WebBypassVsyncCondition)

Sets the rendering process to bypass vsync (vertical synchronization) scheduling and directly trigger drawing when the **scrollBy** API is called to scroll the page. When this attribute is not explicitly called, vsync scheduling is not skipped by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| condition | [WebBypassVsyncCondition](../enums/document.md#webbypassvsynccondition20) | Yes | 
Condition for triggering the rendering process to bypass vsync scheduling.

When **undefined** or **null** is passed in, the value is **NONE**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  condition: WebBypassVsyncCondition = WebBypassVsyncCondition.SCROLLBY\_FROM\_ZERO\_OFFSET;

  build() {
    Column() {
      Button('scrollBy')
        .onClick(() => {
          this.controller.scrollBy(0, 5);
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .bypassVsyncCondition(this.condition)
    }
  }
}

#### enableNativeEmbedMode11+

enableNativeEmbedMode(mode: boolean)

Sets whether to enable the same-layer rendering feature. When this attribute is not explicitly called, the same-layer rendering feature is disabled by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | boolean | Yes | 
Whether to enable the same-layer rendering feature.

The value **true** means to enable the same-layer rendering feature, and **false** means the opposite.

When **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeEmbedMode(true)
    }
  }
}

#### forceDisplayScrollBar14+

forceDisplayScrollBar(enabled: boolean)

Sets whether the scroll bar is always visible. Under the always-visible settings, when the page size exceeds one page, the scroll bar appears and remains visible. When this attribute is not explicitly called, the scroll bar is not always visible by default.

When **layoutMode** is set to **WebLayoutMode.FIT\_CONTENT**, the **enabled** parameter is set to **false**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether the scroll bar is always visible.

The value **true** indicates that the scroll bar is always visible, and **false** indicates the opposite.

When **undefined** or **null** is passed in, the attribute setting does not take effect.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .forceDisplayScrollBar(true)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <style>
      body {
        width:2560px;
        height:2560px;
        padding-right:170px;
        padding-left:170px;
        border:5px solid blueviolet;
      }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### registerNativeEmbedRule12+

registerNativeEmbedRule(tag: string, type: string)

Registers the HTML tag name and type for same-layer rendering. The tag name only supports <object> and <embed>. The tag type only supports visible ASCII characters.

If the specified type is the same as the W3C standard <object> or <embed> type, the ArkWeb kernel identifies the type as a non-same-layer tag.

This API is also controlled by **enableNativeEmbedMode** and does not take effect when same-layer rendering is disabled. When this API is not used, the ArkWeb kernel recognizes the <embed> tags with the "native/" prefix as same-layer tags.

For details, see [Using Same-Layer Rendering](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-same-layer#rendering-text-boxes-at-the-same-layer-on-web-pages).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tag | string | Yes | Tag name. |
| type | string | Yes | Tag type. The ArkWeb kernel uses a prefix to match this parameter. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from '@kit.ArkUI';

declare class Params {
  text: string;
  width: number;
  height: number;
}

declare class NodeControllerParams {
  surfaceId: string;
  renderType: NodeRenderType;
  width: number;
  height: number;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | undefined | null;
  private surfaceId\_: string = "";
  private renderType\_: NodeRenderType = NodeRenderType.RENDER\_TYPE\_DISPLAY;
  private width\_: number = 0;
  private height\_: number = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId\_ = params.surfaceId;
    this.renderType\_ = params.renderType;
    this.width\_ = params.width;
    this.height\_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId\_, type: this.renderType\_ });
    this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width\_, height: this.height\_ });
    return this.rootNode.getFrameNode();
  }

  postInputEvent(event: TouchEvent | MouseEvent | undefined): boolean {
    return this.rootNode?.postInputEvent(event) as boolean;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params;
  @State bkColor: Color = Color.Red;

  build() {
    Column() {
      Button(this.params.text)
        .height(50)
        .width(200)
        .border({ width: 2, color: Color.Red })
        .backgroundColor(this.bkColor)
    }
    .width(this.params.width)
    .height(this.params.height)
  }
}

@Builder
function ButtonBuilder(params: Params) {
  ButtonComponent({ params: params })
    .backgroundColor(Color.Green)
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile('index.html'), controller: this.controller })
           // Enable same-layer rendering.
          .enableNativeEmbedMode(true)
           // Register the same-layer tag as <object> with the type prefixed by "native".
          .registerNativeEmbedRule("object", "native")
           // Obtain the lifecycle change data of the <object> tag.
          .onNativeEmbedLifecycleChange((object) => {
            if (object.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: object.surfaceId as string,
                renderType: NodeRenderType.RENDER\_TYPE\_TEXTURE,
                width: this.uiContext!.px2vp(object.info?.width),
                height: this.uiContext!.px2vp(object.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
      }
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<div>
    <div id="bodyId">
        <object id="nativeButton" type ="native/button" width="300" height="300" style="background-color:red">
        </object>
    </div>
</div>
</body>
</html>

#### defaultTextEncodingFormat12+

defaultTextEncodingFormat(textEncodingFormat: string)

Sets the default text encoding format for the web page. When this attribute is not explicitly called, the default character encoding of the web page is UTF-8.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| textEncodingFormat | string | Yes | 
Default text encoding format.

When **null** or **undefined** is passed in, the value is **UTF-8**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        // Set the height.
        .height(500)
        .defaultTextEncodingFormat("UTF-8")
        .javaScriptAccess(true)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width" />
    <title>My test html5 page</title>
</head>
<body>
    <p>Hello world!</p>
</body>
</html>

#### metaViewport12+

metaViewport(enabled: boolean)

Sets whether the **viewport** attribute of the **meta** tag is enabled. When this attribute is not explicitly called, the **viewport** attribute of the **meta** tag is supported by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/fXDYpCkLQwKJavwGGdAofg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=785B1C5AB9E66AFC33A5E1F2759AF6ADB7C653AFA2D5993C5C514427B08B6AD9)

-   Currently, the **viewport** attribute of the **meta** tag on the frontend HTML page is enabled or disabled based on whether **User-Agent** contains the **Mobile** field. If a **User-Agent** does not contain the **Mobile** field, the **viewport** attribute in the **meta** tag is disabled by default. In this case, you can explicitly set the **metaViewport** attribute to **true** to overwrite the disabled state.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior difference:** This API can be called on phones, wearables, and TVs, but does not work on PCs or 2in1 devices. For tablets, the **viewport-fit** attribute in the **meta** tag will be parsed no matter whether this parameter is set to **true** or **false**. When **viewport-fit** is set to **cover**, the size of the safe area can be obtained through the CSS attribute.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether the **viewport** attribute of the **meta** tag is enabled.

The value **true** indicates that the **viewport** attribute of the **meta** tag is enabled and parsed, and the layout is performed based on the **viewport** attribute.

The value **false** indicates the **viewport** attribute of the **meta** tag is disabled and not parsed, and the default layout is used.

When **null** or **undefined** is passed in, the value is **true**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .metaViewport(true)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <p>Hello world!</p>
</body>
</html>

#### textAutosizing12+

textAutosizing(textAutosizing: boolean)

Sets whether to enable automatic font sizing for the **Web** component. When no attribute is explicitly called, automatic font sizing is enabled for the **Web** component by default.

After automatic font sizing takes effect, any text smaller than 16 px is enlarged to fall between 16 px and 32 px. This eliminates readability issues on narrow screens (viewport < 980 px) where mobile-specific layouts are absent.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nwn7iyqtTwiG64JPtexNmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37E5F15864C243C3403B8965A0CBCE9D7695A851DFD3530DDD1D79FBDAA5EDC4)

-   The preconditions for automatic font sizing to take effect are as follows:
    -   The device type should be phone, tablet, wearable, or TV.
    -   The viewport width of the **Web** component is less than 980 px.
    -   The page is text-heavy: font size (px) × character count ≥ 3920.
    -   **metaViewport** is not set on the frontend, or the **metaViewport** does not contain the **width** and **initial-scale** attributes.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior**: This API has no effect on the PCs/2-in-1 devices and works on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| textAutosizing | boolean | Yes | 
Whether to enable automatic text resizing.

The value **true** means to enable automatic text resizing, and **false** means the opposite.

When **undefined** or **null** is passed in, the value is **true**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .textAutosizing(false)
    }
  }
}

#### enableNativeMediaPlayer12+

enableNativeMediaPlayer(config: NativeMediaPlayerConfig)

Sets whether to enable the [application to take over web page media playback](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-takeovers-web-media). When this attribute is not explicitly called, the web page media playback takeover feature is disabled by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [NativeMediaPlayerConfig](../interfaces-others/document.md#nativemediaplayerconfig12) | Yes | 
**enable**: whether to enable the feature.

**shouldOverlay**: whether the image of the video player taken over by the application will overlay the web page content, if this feature is enabled.

When **undefined** or **null** is passed in, the value is **{enable: false, shouldOverlay: false}**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
    }
  }
}

#### onAdsBlocked12+

onAdsBlocked(callback: OnAdsBlockedCallback)

Called after an ad is blocked on the web page to notify the user of detailed information about the blocked ad. To reduce the frequency of notifications and minimize the impact on the page loading process, only the first notification is made when the page is fully loaded. Subsequent blocking events are reported at intervals of 1 second, and no notifications are sent if there is no ad blocked.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnAdsBlockedCallback](../types/document.md#onadsblockedcallback12) | Yes | Callback of **onAdsBlocked**. |

**Example**

// xxx.ets
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

#### keyboardAvoidMode12+

keyboardAvoidMode(mode: WebKeyboardAvoidMode)

Sets the custom soft keyboard avoidance mode.

If the keyboard avoidance mode set in **UIContext** is [KeyboardAvoidMode.RESIZE](../../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/enums/document.md#keyboardavoidmode11), this API does not take effect.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [WebKeyboardAvoidMode](../enums/document.md#webkeyboardavoidmode12) | Yes | 
Web soft keyboard avoidance mode.

In the nested scrolling scenario, the soft keyboard avoidance mode of the **Web** component is not recommended, including **RESIZE\_VISUAL** and **RESIZE\_CONTENT**.

Default value: **WebKeyboardAvoidMode.RESIZE\_CONTENT**

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State avoidMode: WebKeyboardAvoidMode = WebKeyboardAvoidMode.RESIZE\_VISUAL;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .keyboardAvoidMode(this.avoidMode)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>

#### editMenuOptions12+

editMenuOptions(editMenu: EditMenuOptions)

Sets the custom menu options of the **Web** component.

You can use this attribute to customize a text menu.

You can use [onCreateMenu](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#oncreatemenu12) to modify, add, and delete menu options. If you do not want to display the text menu, return an empty array.

You can use [onMenuItemClick](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#onmenuitemclick12) to customize the callback for menu options. This function is triggered after a menu option is clicked and determines whether to execute the default callback based on the return value. If **true** is returned, the system callback is not executed. If **false** is returned, the system callback is executed.

In [onPrepareMenu20+](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#properties-1), this callback is triggered after the text selection area changes and before the menu is displayed. You can modify, add, or delete menu options in the callback to dynamically update the menu.

If this method is used together with [selectionMenuOptions(deprecated)](#selectionmenuoptionsdeprecated), the **selectionMenuOptions (deprecated)** method does not take effect.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| editMenu | [EditMenuOptions](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#editmenuoptions) | Yes | 
Custom menu options of the **Web** component.

The number of menu options, menu content size, and icon size must be the same as those of the ArkUI [Menu](../../../../arkui/arkts-components/menus/menu/document.md) component.

The values of ([TextMenuItemId](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12)) supported by the **Web** component are **CUT**, **COPY**, **PASTE**, **SELECT\_ALL**, **TRANSLATE**, **SEARCH**, and **AI\_WRITER**.

**textRange** in **onMenuItemClick()** is meaningless in the **Web** component. The input value is **\-1**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

let selectText:string = '';
class TestClass {
  setSelectText(param: String) {
    selectText = param.toString();
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObj: TestClass = new TestClass();

  onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
    let items = menuItems.filter((menuItem) => {
      // Filter the menu items as required.
      return (
        menuItem.id.equals(TextMenuItemId.CUT) ||
        menuItem.id.equals(TextMenuItemId.COPY) ||
        menuItem.id.equals((TextMenuItemId.PASTE)) ||
        menuItem.id.equals((TextMenuItemId.TRANSLATE)) ||
        menuItem.id.equals((TextMenuItemId.SEARCH)) ||
        menuItem.id.equals((TextMenuItemId.AI\_WRITER))
      )
    });
    let customItem1: TextMenuItem = {
      content: 'customItem1',
      id: TextMenuItemId.of('customItem1'),
      icon: $r('app.media.icon')
    };
    let customItem2: TextMenuItem = {
      content: $r('app.string.customItem2'),
      id: TextMenuItemId.of('customItem2'),
      icon: $r('app.media.icon')
    };
    items.push(customItem1);// Add an item to the end of the item list.
    items.unshift(customItem2);// Add an item to the beginning of the item list.

    return items;
  }

  onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
    if (menuItem.id.equals(TextMenuItemId.CUT)) {
      // Custom behavior
      console.info("Intercept ID: CUT")
      return true; // Return true to not execute the system callback.
    } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
      // Custom behavior
      console.info("Not intercept ID: COPY")
      return false; // Return false to execute the system callback.
    } else if (menuItem.id.equals(TextMenuItemId.of('customItem1'))) {
      // Custom behavior
      console.info("Intercept ID: customItem1")
      return true;// Custom menu item. If true is returned, the menu is not closed after being clicked. If false is returned, the menu is closed.
    } else if (menuItem.id.equals((TextMenuItemId.of($r('app.string.customItem2'))))){
      // Custom behavior
      console.info("Intercept ID: app.string.customItem2")
      return true;
    }
    return false;// Return the default value false.
  }

   onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'prepare1',
      id: TextMenuItemId.of('prepareMenu1'),
    };
    let item2: TextMenuItem = {
      content: 'prepare2' + selectText,
      id: TextMenuItemId.of('prepareMenu2'),
    };
    menuItems.push(item1);// Add an item to the end of the item list.
    menuItems.unshift(item2);// Add an item to the beginning of the item list.

    return menuItems;
  }

  @State EditMenuOptions: EditMenuOptions =
    { onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick, onPrepareMenu:this.onPrepareMenu }

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .editMenuOptions(this.EditMenuOptions)
        .javaScriptProxy({
          object: this.testObj,
          name: "testObjName",
          methodList: \["setSelectText"\],
          controller: this.controller,
        })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>editMenuOptions Demo</h1>
    <span>edit menu options</span>
    <script>
      document.addEventListener('selectionchange', () => {
        var selection = window.getSelection();
        if (selection.rangeCount > 0) {
          var selectedText = selection.toString();
          testObjName.setSelectText(selectedText);
        }
      });
  </script>
  </body>
</html>

#### enableHapticFeedback13+

enableHapticFeedback(enabled: boolean)

Sets whether to enable haptic feedback for long-pressed text in the **Web** component. Requires the **ohos.permission.VIBRATE** permission. When this attribute is not explicitly called, haptic feedback is enabled by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to enable haptic feedback for long-pressed text in the **Web** component.

The value **true** means to enable haptic feedback for long-pressed text in the **Web** component, and **false** means the opposite.

When **undefined** or **null** is passed in, the attribute setting does not take effect.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .enableHapticFeedback(true)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>enableHapticFeedback Demo</h1>
    <span>enable haptic feedback</span>
  </body>
</html>

#### bindSelectionMenu13+

bindSelectionMenu(elementType: WebElementType, content: CustomBuilder, responseType: WebResponseType, options?: SelectionMenuOptionsExt)

Sets the custom selection menu.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementType | [WebElementType](../enums/document.md#webelementtype13) | Yes | Menu type. |
| content | [CustomBuilder](../../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8) | Yes | Menu content. |
| responseType | [WebResponseType](../enums/document.md#webresponsetype13) | Yes | Response type of the menu. |
| options | [SelectionMenuOptionsExt](../interfaces-others/document.md#selectionmenuoptionsext13) | No | Menu options. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { pasteboard } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface PreviewBuilderParam {
  width: number;
  height: number;
  url:Resource | string | undefined;
}

interface PreviewBuilderParamForImage {
  previewImage: Resource | string | undefined;
  width: number;
  height: number;
}

@Builder function PreviewBuilderGlobalForImage($$: PreviewBuilderParamForImage) {
  Column() {
    Image($$.previewImage)
      .objectFit(ImageFit.Fill)
      .autoResize(true)
  }.width($$.width).height($$.height)
}

@Entry
@Component
struct SelectionMenuLongPress {
  controller: webview.WebviewController = new webview.WebviewController();
  previewController: webview.WebviewController = new webview.WebviewController();
  @Builder PreviewBuilder($$: PreviewBuilderParam){
    Column() {
      Stack(){
        Text("") // Select whether to display the URL.
          .padding(5)
          .width('100%')
          .textAlign(TextAlign.Start)
          .backgroundColor(Color.White)
          .copyOption(CopyOptions.LocalDevice)
          .maxLines(1)
          .textOverflow({overflow:TextOverflow.Ellipsis})
        Progress({ value: this.progressValue, total: 100, type: ProgressType.Linear }) // Display the progress bar.
          .style({ strokeWidth: 3, enableSmoothEffect: true })
          .backgroundColor(Color.White)
          .opacity(this.progressVisible?1:0)
          .backgroundColor(Color.White)
      }.alignContent(Alignment.Bottom)
      Web({src:$$.url,controller: new webview.WebviewController()})
        .javaScriptAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .domStorageAccess(true)
        .onPageBegin(()=>{
          this.progressValue = 0;
          this.progressVisible = true;
        })
        .onProgressChange((event)=>{
          this.progressValue = event.newProgress;
        })
        .onPageEnd(()=>{
          this.progressVisible = false;
        })
        .hitTestBehavior(HitTestMode.None) // Disable the gesture response during web page preview.
    }.width($$.width).height($$.height) // Set the preview width and height.
  }

  private result: WebContextMenuResult | undefined = undefined;
  @State previewImage: Resource | string | undefined = undefined;
  @State previewWidth: number = 1;
  @State previewHeight: number = 1;
  @State previewWidthImage: number = 1;
  @State previewHeightImage: number = 1;
  @State linkURL:string = "";
  @State progressValue:number = 0;
  @State progressVisible:boolean = true;
  uiContext: UIContext = this.getUIContext();
  enablePaste = false;

  clearSelection() {
    try {
      this.controller.runJavaScript(
        'clearSelection()',
        (error, result) => {
          if (error) {
            console.error(\`run clearSelection JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
            return;
          }
          if (result) {
            console.info(\`The clearSelection() return value is: ${result}\`);
          }
        });
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  @Builder
  LinkMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy Link', })
        .onClick(() => {
          const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, this.linkURL);
          const systemPasteboard = pasteboard.getSystemPasteboard();
          systemPasteboard.setData(pasteboardData);
        })
      MenuItem({content:'Open Link'})
        .onClick(()=>{
          this.controller.loadUrl(this.linkURL);
        })
    }
  }
  @Builder
  ImageMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy Image', })
        .onClick(() => {
          this.result?.copyImage();
          this.result?.closeContextMenu();
        })
    }
  }
  @Builder
  TextMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy', })
        .onClick(() => {
          try {
            this.controller.runJavaScript(
              'copySelectedText()',
              (error, result) => {
                if (error) {
                  console.error(\`run copySelectedText JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                  return;
                }
                if (result) {
                  console.info(\`The copySelectedText() return value is: ${result}\`);
                }
              });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
          this.clearSelection()
        }).backgroundColor(Color.Pink)
    }
  }
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .javaScriptAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .domStorageAccess(true)
        .bindSelectionMenu(WebElementType.TEXT, this.TextMenuBuilder, WebResponseType.LONG\_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {},
            menuType: MenuType.SELECTION\_MENU,
          })
        .bindSelectionMenu(WebElementType.LINK, this.LinkMenuBuilder, WebResponseType.LONG\_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: this.PreviewBuilder({
              width: 500,
              height: 400,
              url:this.linkURL
            }),
            menuType: MenuType.PREVIEW\_MENU
          })
        .bindSelectionMenu(WebElementType.IMAGE, this.ImageMenuBuilder, WebResponseType.LONG\_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: PreviewBuilderGlobalForImage({
              previewImage: this.previewImage,
              width: this.previewWidthImage,
              height: this.previewHeightImage,
            }),
            menuType: MenuType.PREVIEW\_MENU,
          })
        .zoomAccess(true)
        .onContextMenuShow((event) => {
          if (event) {
            this.result = event.result;
            this.previewWidthImage = this.uiContext!.px2vp(event.param.getPreviewWidth());
            this.previewHeightImage = this.uiContext!.px2vp(event.param.getPreviewHeight());
            if (event.param.getSourceUrl().indexOf("resource://rawfile/") == 0) {
              this.previewImage = $rawfile(event.param.getSourceUrl().substring(19));
            } else {
              this.previewImage = event.param.getSourceUrl();
            }
            this.linkURL = event.param.getLinkUrl()
            return true;
          }
          return false;
        })
    }

  }
  // Swipe back
  onBackPress(): boolean | void {
    if (this.controller.accessStep(-1)) {
      this.controller.backward();
      return true;
    } else {
      return false;
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Touch and hold to copy text</title>
    <style>
        .container {
            background-color: white;
            padding: 30px;
            margin: 20px 0;
        }

        .context {
            line-height: 1.8;
            font-size: 18px;
        }

        .context span {
            border-radius: 8px;
            background-color: #f8f9fa;
        }

        .context a {
            color: #3498db;
            text-decoration: none;
            font-size: 18px;
            font-weight: 600;
            padding: 12px 24px;
            border: 2px solid #3498db;
            border-radius: 30px;
            display: inline-block;
            position: relative;
            overflow: hidden;
            margin-bottom: 20px;
        }

        .context img {
            max-width: 100%;
            height: auto;
            display: block;
            margin-bottom: 20px;
        }

        .context:hover img {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
<div class="container">

    <div class="context">
        <!--img.png is in the same directory as the html file-->
        <img src="img.png">
    </div>

    <div class="context">
        <a  href="https://www.example.com">Touch and hold the link to display the menu</a>
    </div>

    <div class="context">
        <span>In this digital age, the text copying functionality has grown increasingly important. Whether quoting famous remarks, saving key information, or sharing interesting content, copying text is an integral part of our daily operations.</span>
    </div>

</div>
<br>

<script>
    function copySelectedText() {
        const selectedText = window.getSelection().toString();
        if (selectedText.length > 0) {
            // Use the Clipboard API to copy text.
            navigator.clipboard.writeText(selectedText)
                .then(() => {
                    showNotification();
                })
                .catch(err => {
                    console.error('Copy failed:', err);
                });
        }
    }
     function clearSelection() {
        if (window.getSelection) {
            window.getSelection().removeAllRanges();
        }
    }
</script>
</body>
</html>

#### blurOnKeyboardHideMode14+

blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode)

Sets whether to enable blur mode for the web element when soft keyboard is hidden.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [BlurOnKeyboardHideMode](../enums/document.md#bluronkeyboardhidemode14) | Yes | Whether to enable blur mode of the web element when soft keyboard is hidden. The default value is **BlurOnKeyboardHideMode.SILENT**. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State blurMode: BlurOnKeyboardHideMode = BlurOnKeyboardHideMode.BLUR;
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .blurOnKeyboardHideMode(this.blurMode)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>blurOnKeyboardHideMode Demo</h1>
    <input type="text" id="input\_a">
    <script>
      const inputElement = document.getElementById('input\_a');
      inputElement.addEventListener('blur', function() {
        console.info('Input has lost focus');
      });
    </script>
  </body>
</html>

#### enableFollowSystemFontWeight18+

enableFollowSystemFontWeight(follow: boolean)

Sets whether the **Web** component can change the font weight according to the system settings. When this attribute is not explicitly called, the **Web** component can change the font weight according to the system settings by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/p6nwtJ1KT46N9pUfaERdag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E1CDC8DDC3DFCA0C1DDD19905ABB64D0F3D5C6AB871AB99003FFB0EF4CD0C21)

Currently, only front-end text elements support this capability. The **canvas** element and embedded .docx and .pdf texts do not support this capability.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| follow | boolean | Yes | 
Whether the **Web** component can change the font weight according to the system settings.

The value **true** means that the **Web** component can change the font weight according to the system settings, and **false** means the opposite.

When **undefined** or **null** is passed in, the value is **true**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: "www.example.com", controller: this.controller })
        .enableFollowSystemFontWeight(true)
    }
  }
}

#### optimizeParserBudget15+

optimizeParserBudget(optimizeParserBudget: boolean)

Sets whether to enable segment-based HTML parsing optimization. If no attribute is explicitly called, the parsing time is used as the segment point by default.

To avoid occupying too many main thread resources and enable progressive loading of web pages, the ArkWeb kernel uses the segment-based parsing policy when parsing the HTML files. By default, the ArkWeb kernel uses the parsing time as the segment point. When the parsing time exceeds the threshold, the parsing is interrupted and then the layout and rendering operations are performed.

After this optimization is enabled, the ArkWeb kernel checks whether the parsing time exceeds the limit and whether the number of parsed tokens (minimum parsing unit of HTML files, such as <div> and attr="xxx") exceeds the threshold specified by the kernel. If yes, the ArkWeb kernel decreases the threshold. When the First Contentful Paint (FCP) of the page is triggered, the default interrupt judgment logic is restored. In this way, the web page is parsed more frequently before the FCP is triggered, thereby the first-frame content may be parsed in advance and enter a rendering phase, effectively reducing the workload of first-frame rendering, and finally advancing the FCP.

When the FCP of a page is triggered, the default segment parsing logic is restored. Therefore, the segment-based HTML parsing optimization takes effect only for the first page loaded by each **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| optimizeParserBudget | boolean | Yes | 
Whether to enable segment-based HTML parsing optimization.

The value **true** means to use the number of parsed records instead of the parsing time as the segment point for HTML segment parsing, and reduce the upper limit of the number of parsed records in each segment. The value **false** means to use the parsing time as the segment point for HTML segment parsing.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .optimizeParserBudget(true)
    }
  }
}

#### enableWebAVSession18+

enableWebAVSession(enabled: boolean)

Sets whether to support an application to connect to media controller. If this attribute is not explicitly set, the application can connect to media controller by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to support an application to connect to media controller.

The value **true** means to support an application to connect to media controller, and **false** means the opposite.

When **undefined** or **null** is passed in, the value is **true**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .enableWebAVSession(true)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Video Playback Page</title>
</head>
<body>
    <h1>Video Playback</h1>
    <video id="testVideo" controls>
        <!--Save an MP4 media file in the rawfile directory of resources and name it example.mp4.-->
        <source src="example.mp4" type="video/mp4">
    </video>
</body>
</html>

#### nativeEmbedOptions16+

nativeEmbedOptions(options?: EmbedOptions)

Sets the same-layer rendering configuration. This attribute takes effect only when [enableNativeEmbedMode](#enablenativeembedmode11) is enabled and cannot be dynamically modified. If this attribute is not explicitly called, the default value **{supportDefaultIntrinsicSize: false}** is used.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [EmbedOptions](../interfaces-others/document.md#embedoptions16) | No | 
Configuration options of the same-layer rendering.

If **undefined** or **null** is passed in, the value **{supportDefaultIntrinsicSize: false}** is used.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  options: EmbedOptions = {supportDefaultIntrinsicSize: true};

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableNativeEmbedMode(true)
        .nativeEmbedOptions(this.options)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendered Fixed-Size HTML Test</title>
</head>
<body>
<div>
    <embed id="input" type = "native/view" style = "background-color:red"/>
</div>
</body>
</html>

#### enableDataDetector20+

enableDataDetector(enable: boolean)

Sets whether to recognize special entities of web texts, such as emails, phone numbers, and URLs. This API depends on the text recognition capability at the bottom layer of the device. Otherwise, the setting is invalid. When this attribute is not explicitly called, the detector is disabled by default.

If **enableDataDetector** is set to **true** and [dataDetectorConfig](#datadetectorconfig20) is not set, all types of entities will be recognized, and the **color** and **decoration** attributes of the recognized entities will be changed to the following styles:

color: '#ff0a59f7',
decoration:{
  type: TextDecorationType.Underline,
  color: '#ff0a59f7',
  style: TextDecorationStyle.SOLID
}

When **enableDataDetector** is set to **true** and [copyOptions](#copyoptions11) is set to **CopyOptions.LocalDevice**, the AI menu is activated. In this case, after the text on the web page is selected, the text selection menu can display the corresponding AI menu items, including **url** (opening a link), **email** (creating an email), **phoneNumber** (calling), **address** (navigating to the location), and **dateTime** (creating a schedule reminder) in [TextMenuItemId](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12).

When the AI menu takes effect, the corresponding option can be displayed only when the selection contains a complete AI entity. This menu item and the askAI menu item in [TextMenuItemId](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12) do not appear at the same time.

For details about the application scenario, see [Using Smart Text Data Detector](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-data-detector).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable web text recognition. The value **true** means to enable web text recognition, and **false** means the opposite.

When **undefined** or **null** is passed in, the attribute setting does not take effect.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Po26C-nCTQGQe08mLKySFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2A14D40CF4D525382AE4B163DE800FB437C3B6FD15F74CC6B2B1417EB63E747)

Dynamically updating the **enableDataDetector** status does not affect the current page immediately. You need to refresh the page for the new configuration to take effect.

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableDataDetector(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Example enableDataDetector</title>;
</head>
<body>
    <p> Telephone: 400-123-4567 </p>
    <p>Email: example@example.com </p>
</body>
</html>

#### dataDetectorConfig20+

dataDetectorConfig(config: TextDataDetectorConfig)

Configures text recognition settings.

This API must be used together with [enableDataDetector](#enabledatadetector20). It takes effect only when **enableDataDetector** is set to **true**.

When entities A and B overlap, the following rules are followed:

1.  If A is a subset of B (A ⊂ B), then B is retained; otherwise, A is retained.
    
2.  If A is not a subset of B (A ⊄ B) and B is not a subset of A (B ⊄ A), and if the starting point of A is earlier than that of B (A.start < B.start), then A is retained; otherwise, B is retained.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [TextDataDetectorConfig](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#textdatadetectorconfig11) | Yes | Text recognition configuration. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3WddUd66SRmL1Nnl95s2Uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F14FB84307502284F23BCD51FA9175EEAB3BF6BA2DE07BD1C7C186964F70BADB)

The **onDetectResultUpdate** method in **TextDataDetectorConfig** is not supported in the **Web** component. The configured callback will not be called.

When [copyOptions](#copyoptions11) is set to **CopyOptions.None**, the **enablePreviewMenu** item in **TextDataDetectorConfig** is invalid.

Dynamically updating the **TextDataDetectorConfig** configuration does not affect the current page immediately. You need to refresh the page for the new configuration to take effect.

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableDataDetector(true)
        .dataDetectorConfig({
          types: \[
            TextDataDetectorType.PHONE\_NUMBER,
            TextDataDetectorType.EMAIL
          \],
          color: Color.Red,
          decoration: {
            type: TextDecorationType.LineThrough,
            color: Color.Green,
            style: TextDecorationStyle.WAVY
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
    <title>Example dataDetectorConfig</title>;
</head>
<body>
    <p> Telephone: 400-123-4567 </p>
    <p> Email: 12345678901@example.com </p>
    <p> Website: www.example.com (cannot be identified) </p>
</body>
</html>

#### enableSelectedDataDetector22+

enableSelectedDataDetector(enable: boolean)

Sets whether to enable the AI menu feature for text selection menu. After the AI menu feature is enabled, the email, phone number, website, date, and address in the selection can be identified, and the corresponding AI menu items are displayed in the text selection menu. By default, the AI menu feature is enabled.

When the AI menu feature is enabled, the corresponding AI menu items can be displayed in the text selection menu after text is selected on the web page, including **url** (opening a link), **email** (creating an email), **phoneNumber** (calling), **address** (navigating to the address), and **dateTime** (creating an event) in [TextMenuItemId](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12).

When the AI menu takes effect, the corresponding option can be displayed only when the selection contains a complete AI entity. This menu item and the askAI menu item in [TextMenuItemId](../../../../arkui/arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12) do not appear at the same time.

For details about the application scenario, see [Using Smart Text Data Detector](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-data-detector).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable web text recognition. The value **true** means to enable web text recognition, and **false** means the opposite.

If **undefined** or **null** is passed in, the attribute is reset to the default value.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/5wNQTAF2SG6Ua6ZgZVCZdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE473256C8435BC14A68161E8F48DDF53699211D4028DAFB84B102AA7F71B6DF)

If **enableSelectedDataDetector** is not set or is set to **true**, the **types** in [dataDetectorConfig](#datadetectorconfig20) are used. If **dataDetectorConfig** is not set, all types are recognized by default.

If **enableSelectedDataDetector** is set to false, the AI menu for text selection is not activated.

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableSelectedDataDetector(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>enableSelectedDataDetector Example</title>
</head>
<body>
    <p> Telephone: 400-123-4567 </p>
    <p>Email: example@example.com </p>
</body>
</html>

#### gestureFocusMode20+

gestureFocusMode(mode: GestureFocusMode)

Sets the gesture focus mode of the **Web** component. If this attribute is not explicitly called, the **Web** component will be focused by any gesture.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [GestureFocusMode](../enums/document.md#gesturefocusmode20) | Yes | Gesture focus mode of the **Web** component. If **undefined** or **null** is passed in, the value **GestureFocusMode.DEFAULT** is used. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: GestureFocusMode = GestureFocusMode.DEFAULT;
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .gestureFocusMode(this.mode)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>

#### rotateRenderEffect22+

rotateRenderEffect(effect: WebRotateEffect)

Sets how the content of the **Web** component is filled during the width and height animation when the component is rotated. If this attribute is not explicitly called, by default, the component's content stays at the final size and always aligned with the upper left corner of the component.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [WebRotateEffect](../enums/document.md#webrotateeffect22) | Yes | Sets how the content of the **Web** component is filled during the width and height animation when the component is rotated. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State effect: WebRotateEffect = WebRotateEffect.TOPLEFT\_EFFECT;
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .rotateRenderEffect(this.effect)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <p>Test Web Page</p>
</body>
</html>

#### forceEnableZoom21+

forceEnableZoom(enable: boolean)

Sets whether to enable the forcible zoom functionality for the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to comply with the zoom restriction specified by the <meta name="viewport"> tag on the web page.

The value **true** means to not comply with the web page zoom restriction, and **false** means the opposite.

When **undefined** or **null** is passed in, the attribute setting does not take effect.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .forceEnableZoom(true)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
  <title>Test Web Page</title>
</head>
<body>
  <h1>forceEnableZoom Demo</h1>
  <span>You can scale page when forceEnableZoom is true.</span>
</body>
</html>

#### backToTop22+

backToTop(backToTop: boolean)

Sets whether to enable the back-to-top feature for the **Web** component when the status bar is touched. When this attribute is not explicitly called, the back-to-top feature for the status bar is enabled by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| backToTop | boolean | Yes | 
Whether to enable the back-to-top feature. The value **true** means to enable the feature, and **false** means the opposite.

When **undefined** or **null** is passed in, the value is **true**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .backToTop(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /\* Horizontally centered \*/
         line-height: 200px;       /\* Vertically centered (the height matches the container height) \*/
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>

#### blankScreenDetectionConfig22+

blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig)

Sets the blank screen detection configuration, such as whether to enable the detection, detection time, and detection policy. When this attribute is not explicitly called, blank screen detection is disabled by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/9eH6XxcXSwqruORODVglfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B853948DF8034030D2F62D0B8A604B33BD822720873A6CCB6A6CF2CA855D190B)

-   Based on the configuration of **detectConfig**, [onDetectedBlankScreen](../events/document.md#ondetectedblankscreen22) may be triggered when a blank screen or near-blank screen is detected after a web page is loaded.
-   The setting takes effect in the next navigation.
-   After the user interacts with the web page, the system does not check whether a blank screen occurs.
-   This feature is not supported when **layoutMode** is set to **WebLayoutMode.FIT\_CONTENT**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| detectConfig | [BlankScreenDetectionConfig](../interfaces-others/document.md#blankscreendetectionconfig22) | Yes | Blank screen detection policy. |

**Example**

// blankScreenDetectionConfig.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .blankScreenDetectionConfig({
          enable: true,
          detectionTiming: \[2, 4, 6, 8\],
          contentfulNodesCountThreshold: 4,
          detectionMethods:\[BlankScreenDetectionMethod.DETECTION\_CONTENTFUL\_NODES\_SEVENTEEN\]
        })
        .onDetectedBlankScreen((event: BlankScreenDetectionEventInfo)=>{
          console.info(\`Found blank screen on ${event.url}.\`);
          console.info(\`The blank screen reason is ${event.blankScreenReason}.\`);
          console.info(\`The blank screen detail is ${event.blankScreenDetails?.detectedContentfulNodesCount}.\`);
        })
    }
  }
}

#### password(deprecated)

password(password: boolean)

Sets whether to save the password. This API is an empty API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/3rjXET2YQeKliwzz8dGFlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2365AF22FD433C56A60970E5C9DE3FC9C68AD1B19806694F12D7309B080FA0E2)

This API is supported since API version 8 and deprecated since API version 10. No substitute API is provided.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| password | boolean | Yes | 
Whether the password can be saved on the web page. The value **true** indicates that the password can be saved on the web page.

The value **false** indicates the opposite.

 |

#### textZoomAtio(deprecated)

textZoomAtio(textZoomAtio: number)

Sets the text zoom ratio of the page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ngtOdOXhTUqC4vO5hyMiAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4808341007A81D36CF3657B218ADD655AE8EF3E0CF916910E0B5BC9470A611BB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [textZoomRatio9+](#textzoomratio9) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| textZoomAtio | number | Yes | 
Text zoom ratio to set.

The value is a positive integer.

Default value: **100**

 |

**Example**

// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State ratio: number = 150
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .textZoomAtio(this.ratio)
    }
  }
}

#### userAgent(deprecated)

userAgent(userAgent: string)

Sets the user agent.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/EwY5cJbJQFKTIkn3mGvgAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2E41615109C1137A3E7615B5D527B890A1B354BFE0D37CEEC906E57AA7CF64E)

This API is supported since API version 8 and deprecated since API version 10. You are advised to use [setCustomUserAgent](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#setcustomuseragent10)10+ instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| userAgent | string | Yes | User agent to set. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State userAgent:string = 'Mozilla/5.0 (Phone; OpenHarmony 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 ArkWeb/4.1.6.1 Mobile DemoApp';

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .userAgent(this.userAgent)
    }
  }
}

#### tableData(deprecated)

tableData(tableData: boolean)

Sets whether to save form data. When this attribute is not explicitly called, the **Web** component is allowed to save form data by default. This API is an empty API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/XYydeCrWReCdRrOzXjv75g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EB176D2FDF3DC8F1A8F604CB56111AD00CBB38D1D7AD591473F44DA8934AD65)

This API is supported since API version 8 and deprecated since API version 10. No substitute API is provided.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tableData | boolean | Yes | 
Whether to save form data. The value **true** means to save form data on the web page.

The value **false** means the opposite.

 |

#### wideViewModeAccess(deprecated)

wideViewModeAccess(wideViewModeAccess: boolean)

Sets whether to support the **viewport** attribute of the HTML **<meta>** tag. This API is an empty API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5GQIM1qNQym9dQBPPQ882A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D568CFB1A33394EE8211C3E6F7C4A244682F00B79549D3FAB273A887DB7B05D)

This API is supported since API version 8 and deprecated since API version 10. No substitute API is provided.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wideViewModeAccess | boolean | Yes | 
Whether to support the **viewport** attribute of the HTML **<meta>** tag.

The value **true** means to support the **viewport** attribute of the HTML **<meta>** tag, and **false** means the opposite.

 |

#### selectionMenuOptions(deprecated)

selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>)

Sets the extended options of the custom context menu on selection, including the text content, icon, and callback.

The API only supports the selection of plain text; if the selected content contains images or other non-text elements, the **action** information may display garbled content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/fapvndWSSPeOsqrD-7zEkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66588F7A85E2C9C9963F89B13E4852C5B2758FFB32E2653C67C6B054A7611171)

This API is supported since API version 12 and deprecated since API version 20. You are advised to use [editMenuOptions12+](#editmenuoptions12) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| expandedMenuOptions | Array<[ExpandedMenuItemOptions](../interfaces-others/document.md#expandedmenuitemoptionsdeprecated)\> | Yes | 
Extended options of the custom context menu on selection.

The number of menu options, menu content size, and start icon size must be the same as those of the ArkUI [Menu](../../../../arkui/arkts-components/menus/menu/document.md) component.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State menuOptionArray: Array<ExpandedMenuItemOptions> = \[
    {content: 'Apple', startIcon: $r('app.media.icon'), action: (selectedText) => {
      console.info('select info ' + selectedText.toString());
    }},
    {content: 'Banana', startIcon: $r('app.media.icon'), action: (selectedText) => {
      console.info('select info ' + selectedText.toString());
    }}
  \];

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .selectionMenuOptions(this.menuOptionArray)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <h1>selectionMenuOptions Demo</h1>
  <span>selection menu options</span>
</body>
</html>

#### zoomControlAccess22+

zoomControlAccess(zoomControlAccess: boolean)

Sets whether to allow zooming by pressing **Ctrl + '-/+'** or **Ctrl** + mouse wheel/touchpad.

If this attribute is not explicitly called, zooming by pressing **Ctrl + '-/+'** or **Ctrl** + mouse wheel/touchpad is allowed by default.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| zoomControlAccess | boolean | Yes | Whether to support the default zooming behavior by pressing the combination keys. The value **true** means to support the default zooming behavior by pressing the combination keys, and **false** means the opposite. When **null** or **undefined** is passed in, the value is **false**. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .zoomControlAccess(true)
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Web Page</title>
</head>
<body>
  <h1>zoomControlAccess Demo</h1>
  <span>You can zoom in/out page when zoomControlAccess is true.</span>
</body>
</html>
