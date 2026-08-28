# Events

The following universal events are supported: [onAppear](../../../../arkui/arkts-components/universal-events/component-change-events/show-hide-event/document.md#onappear), [onDisAppear](../../../../arkui/arkts-components/universal-events/component-change-events/show-hide-event/document.md#ondisappear), [onBlur](../../../../arkui/arkts-components/universal-events/interaction-response-events/focus-event/document.md#onblur), [onFocus](../../../../arkui/arkts-components/universal-events/interaction-response-events/focus-event/document.md#onfocus), [onDragEnd](../../../../arkui/arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragend10), [onDragEnter](../../../../arkui/arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragenter), [onDragStart](../../../../arkui/arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragstart), [onDragMove](../../../../arkui/arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragmove), [onDragLeave](../../../../arkui/arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragleave), [onDrop](../../../../arkui/arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondrop), [onHover](../../../../arkui/arkts-components/universal-events/interaction-response-events/hover-event/document.md#onhover), [onMouse](../../../../arkui/arkts-components/universal-events/basic-input-events/mouse-event/document.md#onmouse), [onKeyEvent](../../../../arkui/arkts-components/universal-events/basic-input-events/key-event/document.md#onkeyevent), [onTouch](../../../../arkui/arkts-components/universal-events/basic-input-events/touch-event/document.md#ontouch), [onVisibleAreaChange](../../../../arkui/arkts-components/universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/NlkR37usQRu43NMqmiDblg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3725548B88803D1CA2BD12F7E4CBCDA4D19C9076CCDAF157947DA1575DA189F4)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The sample effect is subject to the actual device.
    

#### onAlert

onAlert(callback: Callback<OnAlertEvent, boolean>)

Triggered when **alert()** is invoked to display an alert dialog box on the web page. Call the [handleCancel](../class-jsresult/document.md#handlecancel) or [handleConfirm](../class-jsresult/document.md#handleconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnAlertEvent](../interfaces-others/document.md#onalertevent12), boolean> | Yes | 
Callback used when **alert()** is invoked to display an alert dialog box on the web page.

Return value: boolean

If the callback returns **true**, the application can use the custom dialog box (allows the confirm and cancel operations) and invoke the **JsResult** API to notify the **Web** component the confirmation result. If the callback returns **false**, the processing result of the dialog box is regarded as cancel.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onAlert((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            this.uiContext.showAlertDialog({
              title: 'onAlert',
              message: 'text',
              primaryButton: {
                value: 'ok',
                action: () => {
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            })
          }
          return true;
        })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>WebView onAlert Demo</h1>
  <button onclick="myFunction()">Click here</button>
  <script>
    function myFunction() {
      alert("Hello World");
    }
  </script>
</body>
</html>

#### onBeforeUnload

onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean>)

Called when the page refresh is about to complete or the current page is closed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/qNef4GizR3elUhYrZAs_9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FC621A0459EACF0CC40BA582F381E2F9E207C2966B18494C7D665723F3F95AC)

-   If the current **Web** component does not have the focus, **onBeforeUnload** is not triggered when the page is refreshed or closed.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnBeforeUnloadEvent](../interfaces-others/document.md#onbeforeunloadevent12), boolean> | Yes | 
Callback triggered when the page refresh is about to complete or the current page is closed.

Return value: boolean

If the callback returns **true**, the application can use the custom dialog box (allows the confirm and cancel operations) and invoke the **JsResult** API to notify the **Web** component whether to exit the current page based on the user's operation. The value **false** means that the custom dialog box drawn in the function is ineffective.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onBeforeUnload((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            console.info("event.isReload:" + event?.isReload ?? 'false');
            this.uiContext.showAlertDialog({
              title: 'onBeforeUnload',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  event.result.handleCancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            })
          }
          return true;
        })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body onbeforeunload="return myFunction()">
  <h1>WebView onBeforeUnload Demo</h1>
  <a href="https://www.example.com">Click here</a>
  <script>
    function myFunction() {
      return "onBeforeUnload Event";
    }
  </script>
</body>
</html>

#### onConfirm

onConfirm(callback: Callback<OnConfirmEvent, boolean>)

Triggered when **confirm()** is invoked by the web page. Call the [handleCancel](../class-jsresult/document.md#handlecancel) or [handleConfirm](../class-jsresult/document.md#handleconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnConfirmEvent](../interfaces-others/document.md#onconfirmevent12), boolean> | Yes | 
Callback triggered when **confirm()** is invoked by the web page.

Return value: boolean

If the callback returns **true**, the application can use the custom dialog box (allows the confirm and cancel operations) and invoke the **JsResult** API to notify the **Web** component the confirmation result. If the callback returns **false**, the processing result of the dialog box is regarded as cancel.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onConfirm((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            this.uiContext.showAlertDialog({
              title: 'onConfirm',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  event.result.handleCancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            })
          }
          return true;
        })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
  <h1>WebView onConfirm Demo</h1>
  <button onclick="myFunction()">Click here</button>
  <p id="demo"></p>
  <script>
    function myFunction() {
      let x;
      let r = confirm("click button!");
      if (r == true) {
        x = "ok";
      } else {
        x = "cancel";
      }
      document.getElementById("demo").innerHTML = x;
    }
  </script>
</body>
</html>

#### onPrompt9+

onPrompt(callback: Callback<OnPromptEvent, boolean>)

Triggered when **prompt()** is invoked by the web page. Call the [handleCancel](../class-jsresult/document.md#handlecancel) or [handlePromptConfirm](../class-jsresult/document.md#handlepromptconfirm9) API when this callback is triggered. Otherwise, the render process is blocked.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnPromptEvent](../interfaces-others/document.md#onpromptevent12), boolean> | Yes | 
Callback used when **prompt()** is invoked by the web page.

Return value: boolean

If the callback returns **true**, the application can use the custom dialog box (allows the confirm, cancel, and input operations) and invoke the **JsResult** API to notify the **Web** component the processing result. If the callback returns **false**, the processing result of the dialog box is regarded as cancel.

 |

**Example**

// xxx.ets
import { CustomContentDialog } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State message: string = 'Hello World';
  @State title: string = 'Hello World';
  @State result: JsResult | null = null;
  promptResult: string = '';
  webviewController: webview.WebviewController = new webview.WebviewController();
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomContentDialog({
      primaryTitle: this.title,
      contentBuilder: () => {
        this.buildContent();
      },
      buttons: \[
        {
          value: 'Cancel',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked');
            this.result?.handleCancel()
          }
        },
        {
          value: 'OK',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            this.result?.handlePromptConfirm(this.promptResult);
          }
        }
      \],
    }),
    onWillDismiss: () => {
      this.result?.handleCancel();
      this.dialogController.close();
    }
  });

  // Content area of the custom dialog box
  @Builder
  buildContent(): void {
    Column() {
      Text(this.message)
      TextInput()
        .onChange((value) => {
          this.promptResult = value;
        })
        .defaultFocus(true)
    }
    .width('100%')
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.webviewController })
        .onPrompt((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            console.info("event.value:" + event.value);
            this.title = "Message from" + event.url + "";
            this.message = event.message;
            this.promptResult = event.value;
            this.result = event.result;
            this.dialogController.open();
          }
          return true;
        })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
  <h1>WebView onPrompt Demo</h1>
  <button onclick="myFunction()">Click here</button>
  <p id="demo"></p>
  <script>
    function myFunction() {
      let message = prompt("Message info", "Hello World");
      if (message != null && message != "") {
        document.getElementById("demo").innerHTML = message;
      }
    }
  </script>
</body>
</html>

#### onConsole

onConsole(callback: Callback<OnConsoleEvent, boolean>)

Triggered to notify the host application of a JavaScript console message.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnConsoleEvent](../interfaces-others/document.md#onconsoleevent12), boolean> | Yes | 
Callback used when the web page receives a JavaScript console message.

Return value: boolean

The value **true** means that the message will not be printed to HiLog logs, and **false** means the opposite.

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
      Button('onconsole message')
        .onClick(() => {
          this.controller.runJavaScript('myFunction()');
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onConsole((event) => {
          if (event) {
            console.info('getMessage:' + event.message.getMessage());
            console.info('getSourceId:' + event.message.getSourceId());
            console.info('getLineNumber:' + event.message.getLineNumber());
            console.info('getMessageLevel:' + event.message.getMessageLevel());
          }
          return false;
        })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<script>
    function myFunction() {
        console.info("onconsole printf");
    }
</script>
</body>
</html>

#### onDownloadStart

onDownloadStart(callback: Callback<OnDownloadStartEvent>)

Triggered to instruct the main application to start downloading a file.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnDownloadStartEvent](../interfaces-others/document.md#ondownloadstartevent12)\> | Yes | Callback used when a download starts. |

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
        .onDownloadStart((event) => {
          if (event) {
            console.info('url:' + event.url)
            console.info('userAgent:' + event.userAgent)
            console.info('contentDisposition:' + event.contentDisposition)
            console.info('contentLength:' + event.contentLength)
            console.info('mimetype:' + event.mimetype)
          }
        })
    }
  }
}

#### onErrorReceive

onErrorReceive(callback: Callback<OnErrorReceiveEvent>)

Triggered when an error occurs during web page loading. The error may occur on the main resource or sub-resource. You can use [isMainFrame](../class-webresourcerequest/document.md#ismainframe) to determine whether the error occurs on the main resource. For performance reasons, simplify the implementation logic in the callback. This API is called when there is no network connection.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnErrorReceiveEvent](../interfaces-others/document.md#onerrorreceiveevent12)\> | Yes | Callback used when an error occurs during web page loading. |

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
        .onErrorReceive((event) => {
          if (event) {
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
            console.info('isMainFrame:' + event.request.isMainFrame());
            console.info('isRedirect:' + event.request.isRedirect());
            console.info('isRequestGesture:' + event.request.isRequestGesture());
            console.info('getRequestHeader\_headerKey:' + event.request.getRequestHeader().toString());
            let result = event.request.getRequestHeader();
            console.info('The request header result size is ' + result.length);
            for (let i of result) {
              console.info('The request header key is : ' + i.headerKey + ', value is : ' + i.headerValue);
            }
          }
        })
    }
  }
}

#### onHttpErrorReceive

onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent>)

Called when an HTTP error (the response code is greater than or equal to 400) occurs during web page resource loading.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnHttpErrorReceiveEvent](../interfaces-others/document.md#onhttperrorreceiveevent12)\> | Yes | Callback triggered when an HTTP error occurs during web page resource loading. |

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
        .onHttpErrorReceive((event) => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
            console.info('isMainFrame:' + event.request.isMainFrame());
            console.info('isRedirect:' + event.request.isRedirect());
            console.info('isRequestGesture:' + event.request.isRequestGesture());
            console.info('getResponseData:' + event.response.getResponseData());
            console.info('getResponseEncoding:' + event.response.getResponseEncoding());
            console.info('getResponseMimeType:' + event.response.getResponseMimeType());
            console.info('getResponseCode:' + event.response.getResponseCode());
            console.info('getReasonMessage:' + event.response.getReasonMessage());
            let result = event.request.getRequestHeader();
            console.info('The request header result size is ' + result.length);
            for (let i of result) {
              console.info('The request header key is : ' + i.headerKey + ' , value is : ' + i.headerValue);
            }
            let resph = event.response.getResponseHeader();
            console.info('The response header result size is ' + resph.length);
            for (let i of resph) {
              console.info('The response header key is : ' + i.headerKey + ' , value is : ' + i.headerValue);
            }
          }
        })
    }
  }
}

#### onPageBegin

onPageBegin(callback: Callback<OnPageBeginEvent>)

Triggered when the web page starts to be loaded. This callback is called only for the main frame content, and not for the iframe or frameset content.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnPageBeginEvent](../interfaces-others/document.md#onpagebeginevent12)\> | Yes | Callback triggered when a web page loading starts. |

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
        .onPageBegin((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}

#### onPageEnd

onPageEnd(callback: Callback<OnPageEndEvent>)

Triggered when the web page loading is finished. This callback is called only for the main frame content, and not for the iframe or frameset content.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnPageEndEvent](../interfaces-others/document.md#onpageendevent12)\> | Yes | Callback triggered when the web page loading is complete. |

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
        .onPageEnd((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}

#### onLoadStarted20+

onLoadStarted(callback: Callback<OnLoadStartedEvent>)

Triggered to notify the host application that the page loading starts. This method is called once each time the main frame content is loaded. Therefore, for pages that contain iframes or frameset, **onLoadStarted** is called only once for the main frame. This means that when the content of the embedded frame changes, for example, a link or a fragment navigation in the iframe is clicked (navigation to **#fragment\_id**), **onLoadStarted** is not invoked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/mxHmQc41TIe8nvGvWZr0dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32F4375053F2282AABF447368DD8F96B11D9D623E1785790A271F6EE3DBA1E5F)

-   When the document of the pop-up window is modified by JavaScript before being loaded, **onLoadStarted** is simulated and the URL is set to null, because displaying the URL that is being loaded may be insecure. **onPageBegin** will not be simulated.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnLoadStartedEvent](../interfaces-others/document.md#onloadstartedevent20)\> | Yes | Callback triggered when a web page loading starts. |

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
        .onLoadStarted((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}

#### onLoadFinished20+

onLoadFinished(callback: Callback<OnLoadFinishedEvent>)

Triggered to notify the host application that the page has been loaded. This method is called only when the main frame loading is complete. For fragment navigations (navigations to **#fragment\_id**), **onLoadFinished** is also triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/2pTMUPUBTP-af0vy34Xbvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CEEC6A341E6AC6FF47906AFAFBBF6BBA6EDEBF1EB294FB86D03D4E4A03C74F0)

-   Fragment navigation also triggers **onLoadFinished**, but **onPageEnd** is not triggered.
-   If the main frame is automatically redirected before the page is fully loaded, **onLoadFinished** is triggered only once. **onPageEnd** is triggered each time the main frame is navigated.
-   When the document of the pop-up window is modified by JavaScript before being loaded, **onLoadStarted** is simulated and the URL is set to null, because displaying the URL that is being loaded may be insecure. **onPageBegin** will not be simulated.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnLoadFinishedEvent](../interfaces-others/document.md#onloadfinishedevent20)\> | Yes | Callback triggered when the web page loading is complete. |

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
        .onLoadFinished((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}

#### onProgressChange

onProgressChange(callback: Callback<OnProgressChangeEvent>)

Triggered when the web page loading progress changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnProgressChangeEvent](../interfaces-others/document.md#onprogresschangeevent12)\> | Yes | Callback triggered when the page loading progress changes. |

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
        .onProgressChange((event) => {
          if (event) {
            console.info('newProgress:' + event.newProgress);
          }
        })
    }
  }
}

#### onTitleReceive

onTitleReceive(callback: Callback<OnTitleReceiveEvent>)

Called when the **<title>** element of the page document changes. If no title is set on the current page, ArkWeb generates a title based on the page URL and returns it to the application before the loading is complete.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnTitleReceiveEvent](../interfaces-others/document.md#ontitlereceiveevent12)\> | Yes | Callback triggered when the document title on the page is changed. |

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
        .onTitleReceive((event) => {
          if (event) {
            console.info('title:' + event.title);
            console.info('isRealTitle:' + event.isRealTitle);
          }
        })
    }
  }
}

#### onRefreshAccessedHistory

onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent>)

Triggered for the application to update its access history when the navigation is complete.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnRefreshAccessedHistoryEvent](../interfaces-others/document.md#onrefreshaccessedhistoryevent12)\> | Yes | Callback triggered when the navigation is complete. |

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
        .onRefreshAccessedHistory((event) => {
          if (event) {
            console.info('url:' + event.url + ' isReload:' + event.isRefreshed);
            console.info('isMainFrame:' + event.isMainFrame);
          }
        })
    }
  }
}

#### onRenderExited9+

onRenderExited(callback: Callback<OnRenderExitedEvent>)

Triggered when the rendering process exits abnormally.

A rendering process may be shared by multiple **Web** components. Each affected **Web** component triggers this callback.

You can call the bound **webviewController** APIs to restore the web page when this callback is triggered. For example, [refresh](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#refresh) and [loadUrl](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#loadurl).

For details about the component lifecycle, see [Lifecycle of the Web Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-event-sequence).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnRenderExitedEvent](../interfaces-others/document.md#onrenderexitedevent12)\> | Yes | Callback triggered when the rendering process exits abnormally. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'chrome://crash/', controller: this.controller })
        .onRenderExited((event) => {
          if (event) {
            console.info('reason:' + event.renderExitReason);
          }
        })
    }
  }
}

#### onRenderProcessNotResponding12+

onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback)

Triggered when the rendering process does not respond. If the **Web** component cannot process the input event or navigate to a new URL within a proper time range, the web page process is considered unresponsive and the callback is triggered.

If the web page process does not respond, this callback may be triggered until the web page process responds again. In this case, [onRenderProcessResponding](#onrenderprocessresponding12) is triggered.

You can terminate the associated rendering process through [terminateRenderProcess](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#terminaterenderprocess12), which may affect other **Web** components in the same rendering process.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnRenderProcessNotRespondingCallback](../types/document.md#onrenderprocessnotrespondingcallback12) | Yes | Callback triggered when the rendering process does not respond. |

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
        .onRenderProcessNotResponding((data) => {
          console.info("onRenderProcessNotResponding: \[jsStack\]= " + data.jsStack +
            ", \[process\]=" + data.pid + ", \[reason\]=" + data.reason);
        })
    }
  }
}

#### onRenderProcessResponding12+

onRenderProcessResponding(callback: OnRenderProcessRespondingCallback)

Triggered when the rendering process transitions back to a normal operating state from an unresponsive state. This callback indicates that the web page was not actually frozen.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnRenderProcessRespondingCallback](../types/document.md#onrenderprocessrespondingcallback12) | Yes | Callback triggered when the rendering process transitions back to a normal operating state from an unresponsive state. |

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
        .onRenderProcessResponding(() => {
          console.info("onRenderProcessResponding again");
        })
    }
  }
}

#### onShowFileSelector9+

onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean>)

Triggered to process an HTML form whose input type is **file**. If this function is not called or returns **false**, the **Web** component provides the default **Select file** UI. If it returns **true**, the application can customize the response behavior for **Select file**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnShowFileSelectorEvent](../interfaces-others/document.md#onshowfileselectorevent12), boolean> | Yes | 
Callback triggered to notify the **Web** component of the file selection result.

Return value: boolean

The value **true** means that you can invoke the system-provided dialog box. The value **false** means that the custom dialog box drawn in the function is ineffective.

 |

**Example**

1.  Start the file selector.
    
    // xxx.ets
    import { webview } from '@kit.ArkWeb';
    import { picker } from '@kit.CoreFileKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController()
    
      build() {
        Column() {
          Web({ src: $rawfile('index.html'), controller: this.controller })
            .onShowFileSelector((event) => {
              console.info('MyFileUploader onShowFileSelector invoked')
              const documentSelectOptions = new picker.DocumentSelectOptions();
              let uri: string | null = null;
              const documentViewPicker = new picker.DocumentViewPicker();
              documentViewPicker.select(documentSelectOptions).then((documentSelectResult) => {
                uri = documentSelectResult\[0\];
                console.info('documentViewPicker.select to file succeed and uri is:' + uri);
                if (event) {
                  event.result.handleFileList(\[uri\]);
                }
              }).catch((err: BusinessError) => {
                console.error(\`Invoke documentViewPicker.select failed, code is ${err.code},  message is ${err.message}\`);
              })
              return true;
            })
        }
      }
    }
    
2.  Start the photo selector.
    
    // xxx.ets
    import { webview } from '@kit.ArkWeb';
    import { picker } from '@kit.CoreFileKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      async selectFile(result: FileSelectorResult): Promise<void> {
        let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
        let photoPicker = new photoAccessHelper.PhotoViewPicker();
        // Set the mime file type to IMAGE\_VIDEO.
        photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE;
        // Set the maximum number of media files that can be selected.
        photoSelectOptions.maxSelectNumber = 5;
        let chooseFile: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
        // Obtain the list of selected files.
        result.handleFileList(chooseFile.photoUris);
      }
    
      build() {
        Column() {
          Web({ src: $rawfile('index.html'), controller: this.controller })
            .onShowFileSelector((event) => {
              if (event) {
                this.selectFile(event.result);
              }
              return true;
            })
        }
      }
    }
    
3.  Start the camera picker.
    
    // xxx.ets
    import { webview } from '@kit.ArkWeb';
    import { cameraPicker, camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
    async function openCamera(callback: Callback<string>, uiContext: UIContext) {
     let mContext = uiContext.getHostContext() as common.Context;
      try {
        let pickerProfile: cameraPicker.PickerProfile = {
          cameraPosition: camera.CameraPosition.CAMERA\_POSITION\_BACK
        };
        let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(mContext,
          \[cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO\], pickerProfile);
        callback(pickerResult.resultUri);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`the pick call failed. error code: ${err.code}\`);
      }
    }
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Web({ src: $rawfile('index.html'), controller: this.controller })
            .onShowFileSelector((event) => {
              openCamera((result) => {
                if (event) {
                  console.info('Title is ' + event.fileSelector.getTitle());
                  console.info('Mode is ' + event.fileSelector.getMode());
                  console.info('Accept types are ' + event.fileSelector.getAcceptType());
                  console.info('Capture is ' + event.fileSelector.isCapture());
                  console.info('Mime types are ' + event.fileSelector.getMimeTypes());
                  event.result.handleFileList(\[result\]);
                }
              }, this.getUIContext())
              return true;
            })
        }
      }
    }
    
    HTML file to be loaded:
    
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
      <form id="upload-form" enctype="multipart/form-data">
        <input type="file" id="upload" name="upload" accept="image/\*, video/\*"/>
        </form>
    </body>
    </html>
    

#### onResourceLoad9+

onResourceLoad(callback: Callback<OnResourceLoadEvent>)

Triggered to notify the **Web** component of the URL of the resource file to load.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnResourceLoadEvent](../interfaces-others/document.md#onresourceloadevent12)\> | Yes | Callback triggered when a URL is loaded. |

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
        .onResourceLoad((event) => {
          console.info('onResourceLoad: ' + event.url);
        })
    }
  }
}

#### onScaleChange9+

onScaleChange(callback: Callback<OnScaleChangeEvent>)

Called when the page display scale changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnScaleChangeEvent](../interfaces-others/document.md#onscalechangeevent12)\> | Yes | Callback triggered when the page display scale changes. |

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
        .onScaleChange((event) => {
          console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
        })
    }
  }
}

#### onInterceptRequest9+

onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse>)

Triggered when the **Web** component is about to access a URL. This API is used to block the URL and return the response data. The **onInterceptRequest** API can intercept all redirection requests and return response data, but cannot access POST request body content and obtain buffer data. In this scenario, use [WebSchemeHandler](../../../arkts-api/ohos-web-webview-webview/class-webschemehandler/document.md) based on service requirements.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnInterceptRequestEvent](../interfaces-others/document.md#oninterceptrequestevent12), [WebResourceResponse](../class-webresourceresponse/document.md)\> | Yes | 
Callback invoked when the **Web** component is about to load a URL.

The return value is [WebResourceResponse](../class-webresourceresponse/document.md). If response data is returned, the data is loaded based on the response data. If no response data is returned, null is returned, indicating that the data is loaded in the original mode.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  heads: Header\[\] = new Array();
  webData: string = "<!DOCTYPE html>\\n" +
    "<html>\\n" +
    "<head>\\n" +
    "<title>intercept test</title>\\n" +
    "</head>\\n" +
    "<body>\\n" +
    "<h1>intercept test</h1>\\n" +
    "</body>\\n" +
    "</html>";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onInterceptRequest((event) => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
          }
          let head1: Header = {
            headerKey: "Connection",
            headerValue: "keep-alive"
          }
          let head2: Header = {
            headerKey: "Cache-Control",
            headerValue: "no-cache"
          }
          // Add a new element to the end of the array and return the length of the new array.
          let length = this.heads.push(head1);
          length = this.heads.push(head2);
          console.info('The response header result length is :' + length);
          const promise: Promise<String> = new Promise((resolve: Function, reject: Function) => {
            this.responseWeb.setResponseHeader(this.heads);
            this.responseWeb.setResponseData(this.webData);
            this.responseWeb.setResponseEncoding('utf-8');
            this.responseWeb.setResponseMimeType('text/html');
            this.responseWeb.setResponseCode(200);
            this.responseWeb.setReasonMessage('OK');
            resolve("success");
          })
          promise.then(() => {
            console.info("prepare response ready");
            this.responseWeb.setResponseIsReady(true);
          })
          this.responseWeb.setResponseIsReady(false);
          return this.responseWeb;
        })
    }
  }
}

#### onHttpAuthRequest9+

onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean>)

Triggered when an HTTP authentication request is received.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnHttpAuthRequestEvent](../interfaces-others/document.md#onhttpauthrequestevent12), boolean> | Yes | 
Callback invoked when the browser requires user credentials.

Return value: boolean

The value **true** means that the HTTP authentication is successful, and **false** means the opposite.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();
  httpAuth: boolean = false;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onHttpAuthRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'onHttpAuthRequest',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  event.handler.cancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  this.httpAuth = event.handler.isHttpAuthInfoSaved();
                  if (this.httpAuth == false) {
                    webview.WebDataBase.saveHttpAuthCredentials(
                      event.host,
                      event.realm,
                      "2222",
                      "2222"
                    )
                    event.handler.cancel();
                  }
                }
              },
              cancel: () => {
                event.handler.cancel();
              }
            })
          }
          return true;
        })
    }
  }
}

#### onSslErrorEventReceive9+

onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent>)

Triggered to notify the host application when an SSL error occurs while loading the main-frame resource.

To support errors for loading subframe resources, use the [OnSslErrorEvent](#onsslerrorevent12) API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/z2Li3-CJRY2JOfcW75Isuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53843D2286DDA81A22C39504758307E67E501542CEB8AF52C2B2AD41B1CCE0EE)

-   Main resource: Entry file for the browser to load web pages, which is usually an HTML document.
-   Subresource: Dependency file referenced by the main resource, which is loaded when a specific tag is encountered during main resource parsing.
-   The application needs to call [handler.handleCancel()](../class-sslerrorhandler/document.md#handlecancel9) or [handler.handleConfirm()](../class-sslerrorhandler/document.md#handleconfirm9) to process the callback. Otherwise, resource loading is canceled by default. The behavior of **handleConfirm()** or **handleCancel()** may be recorded to respond to future SSL errors.
-   The application can display a custom error page or silently record the problem.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnSslErrorEventReceiveEvent](../interfaces-others/document.md#onsslerroreventreceiveevent12)\> | Yes | Callback invoked when the web page receives an SSL error. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { cert } from '@kit.DeviceCertificateKit';

function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
  if (!(certChainData instanceof Array)) {
    console.error('failed, cert chain data type is not array');
    return;
  }

  for (let i = 0; i < certChainData.length; i++) {
    let encodeBlobData: cert.EncodingBlob = {
      data: certChainData\[i\],
      encodingFormat: cert.EncodingFormat.FORMAT\_DER
    }
    cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
      if (error) {
        console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      } else {
        console.info('createX509Cert success');
        console.info(ParseX509CertInfo(x509Cert));
      }
    });
  }
  return;
}

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray\[i\]);
  }
  return dataString;
}

function ParseX509CertInfo(x509Cert: cert.X509Cert) {
  let res: string = 'getCertificate success, '
    + 'issuer name = '
    + Uint8ArrayToString(x509Cert.getIssuerName().data) + ', subject name = '
    + Uint8ArrayToString(x509Cert.getSubjectName().data) + ', valid start = '
    + x509Cert.getNotBeforeTime()
    + ', valid end = ' + x509Cert.getNotAfterTime();
  return res;
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSslErrorEventReceive((event) => {
          LogCertInfo(event.certChainData);
          this.uiContext.showAlertDialog({
            title: 'onSslErrorEventReceive',
            message: 'text',
            primaryButton: {
              value: 'confirm',
              action: () => {
                event.handler.handleConfirm();
              }
            },
            secondaryButton: {
              value: 'cancel',
              action: () => {
                event.handler.handleCancel();
              }
            },
            cancel: () => {
              event.handler.handleCancel();
            }
          })
        })
    }
  }
}

#### onSslErrorEvent12+

onSslErrorEvent(callback: OnSslErrorEventCallback)

Triggered to notify users when an SSL error occurs during the loading of main-frame or subframe resources. To handle SSL errors for loading the main-frame resources, use the [isMainFrame](../class-webresourcerequest/document.md#ismainframe) field to distinguish.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/KW8bTa4fQtiz2rCapaQbeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48427102510CF60A4BC2A2779D147F26B4E7C18F12075D35B964788FC694F66F)

-   Main resource: Entry file for the browser to load web pages, which is usually an HTML document.
-   Subresource: Dependency file referenced by the main resource, which is loaded when a specific tag is encountered during main resource parsing.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnSslErrorEventCallback](../types/document.md#onsslerroreventcallback12) | Yes | Callback invoked when an SSL error occurs during resource loading. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { cert } from '@kit.DeviceCertificateKit';

function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
  if (!(certChainData instanceof Array)) {
    console.error('failed, cert chain data type is not array');
    return;
  }

  for (let i = 0; i < certChainData.length; i++) {
    let encodeBlobData: cert.EncodingBlob = {
      data: certChainData\[i\],
      encodingFormat: cert.EncodingFormat.FORMAT\_DER
    }
    cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
      if (error) {
        console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      } else {
        console.info('createX509Cert success');
        console.info(ParseX509CertInfo(x509Cert));
      }
    });
  }
  return;
}

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray\[i\]);
  }
  return dataString;
}

function ParseX509CertInfo(x509Cert: cert.X509Cert) {
  let res: string = 'getCertificate success, '
    + 'issuer name = '
    + Uint8ArrayToString(x509Cert.getIssuerName().data) + ', subject name = '
    + Uint8ArrayToString(x509Cert.getSubjectName().data) + ', valid start = '
    + x509Cert.getNotBeforeTime()
    + ', valid end = ' + x509Cert.getNotAfterTime();
  return res;
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSslErrorEvent((event: SslErrorEvent) => {
          console.info("onSslErrorEvent url: " + event.url);
          console.info("onSslErrorEvent error: " + event.error);
          console.info("onSslErrorEvent originalUrl: " + event.originalUrl);
          console.info("onSslErrorEvent referrer: " + event.referrer);
          console.info("onSslErrorEvent isFatalError: " + event.isFatalError);
          console.info("onSslErrorEvent isMainFrame: " + event.isMainFrame);
          LogCertInfo(event.certChainData);
          this.uiContext.showAlertDialog({
            title: 'onSslErrorEvent',
            message: 'text',
            primaryButton: {
              value: 'confirm',
              action: () => {
                event.handler.handleConfirm();
              }
            },
            secondaryButton: {
              value: 'cancel',
              action: () => {
                // The value true indicates that the page loading is stopped and the current page is displayed. The value false indicates that the page loading is continued and an error page is displayed.
                event.handler.handleCancel(true);
              }
            },
            cancel: () => {
              event.handler.handleCancel();
            }
          })
        })
    }
  }
}

#### onClientAuthenticationRequest9+

onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent>)

Triggered when an SSL client certificate request is received.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/ON9fKfoGQK-jWeVbln60jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94EB9729A5256C096AB4C5B09296F87F2620688CCAA0A0C8FA3DE330DAB6A0B6)

-   The **Web** component can respond with [ClientAuthenticationHandler.confirm](../class-clientauthenticationhandler/document.md#confirm10), [ClientAuthenticationHandler.cancel](../class-clientauthenticationhandler/document.md#cancel9), or [ClientAuthenticationHandler.ignore](../class-clientauthenticationhandler/document.md#ignore9).
-   If **ClientAuthenticationHandler.confirm** or **ClientAuthenticationHandler.cancel** is called, the **Web** component stores the authentication result in the memory (within the application lifecycle) and does not call **onClientAuthenticationRequest()** again for the same host and port. If **onClientAuthenticationRequest.ignore** is called, the **Web** component does not store the authentication result.
-   The **ohos.permission.ACCESS\_CERT\_MANAGER** permission is required.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnClientAuthenticationEvent](../interfaces-others/document.md#onclientauthenticationevent12)\> | Yes | Callback invoked when an SSL client certificate is required. |

**Example**

Install a private credential to implement two-way authentication.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { certificateManager } from '@kit.DeviceCertificateKit';
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: WebviewController = new webview.WebviewController();
  uiContext : UIContext = this.getUIContext();
  context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
  uri: string = ''

  aboutToAppear(): void {
    webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
  }

  build() {
    Column() {
      Button("installPrivateCertificate").onClick(() => {
        if (!this.context) {
          return;
        }

        // Note: Replace badssl.com-client.p12 with the actual certificate file.
        let value: Uint8Array = this.context.resourceManager.getRawFileContentSync("badssl.com-client.p12");
        certificateManager.installPrivateCertificate(value, 'badssl.com', "1",
          async (err: BusinessError, data: certificateManager.CMResult) => {
            console.info(\`installPrivateCertificate, uri==========${JSON.stringify(data.uri)}\`)
            if (!err && data.uri) {
              this.uri = data.uri;
            }
          });
      })
      Button('Load the website that requires the client SSL certificate')
        .onClick(() => {
          this.controller.loadUrl("https://client.badssl.com")
        })
      Web({
        src: "https://www.bing.com/",
        controller: this.controller,
      }).domStorageAccess(true)
        .fileAccess(true)
        .onPageBegin(event => {
          console.info("extensions onpagebegin url " + event.url);
        })
        .onClientAuthenticationRequest((event) => {
          console.info("onClientAuthenticationRequest ");
          event.handler.confirm(this.uri);
          return true;
        })
        .onSslErrorEventReceive(e => {
          console.info(\`onSslErrorEventReceive->${e.error.toString()}\`);
        })
        .onErrorReceive((event) => {
          if (event) {
            this.getUIContext().getPromptAction().showToast({
              message: \`ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}\`,
              alignment: Alignment.Center
            })
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
          }
        })
        .onTitleReceive(event  => {
          console.info("title received " + event.title);
        })

    }
  }
}

Interconnect with certificate management to implement two-way authentication.

1.  Construct the singleton object **GlobalContext**.
    
    // GlobalContext.ets
    export class GlobalContext {
      private constructor() {}
      private static instance: GlobalContext;
      private \_objects = new Map<string, Object>();
    
      public static getContext(): GlobalContext {
        if (!GlobalContext.instance) {
          GlobalContext.instance = new GlobalContext();
        }
        return GlobalContext.instance;
      }
    
      getObject(value: string): Object | undefined {
        return this.\_objects.get(value);
      }
    
      setObject(key: string, objectClass: Object): void {
        this.\_objects.set(key, objectClass);
      }
    }
    
2.  Construct a **CertManagerService** object to interconnect with certificate management.
    
    // CertMgrService.ets
    import { bundleManager, common, Want } from "@kit.AbilityKit";
    import { BusinessError } from "@kit.BasicServicesKit";
    import { GlobalContext } from './GlobalContext';
    
    export default class CertManagerService {
      private static sInstance: CertManagerService;
      private authUri = "";
      private appUid = "";
    
      public static getInstance(): CertManagerService {
        if (CertManagerService.sInstance == null) {
          CertManagerService.sInstance = new CertManagerService();
        }
        return CertManagerService.sInstance;
      }
    
      async grantAppPm(): Promise<string> {
        let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_DEFAULT | bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION;
        // Note: Replace com.example.myapplication with the actual application name.
        try {
          const data = await bundleManager.getBundleInfoForSelf(bundleFlags)
            .catch((err: BusinessError) => {
              console.error('getBundleInfoForSelf failed. Cause: %{public}s', err.message);
              return null;
            });
          this.appUid = data?.appInfo?.uid?.toString() ?? '';
          console.info('getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
        } catch (err) {
          let message = (err as BusinessError).message;
          console.error('getBundleInfoForSelf failed: %{public}s', message);
        }
    
        // Note: Add GlobalContext.getContext().setObject("AbilityContext", this.context) to the onCreate function in the MainAbility.ts file.
        let abilityContext = GlobalContext.getContext().getObject("AbilityContext") as common.UIAbilityContext;
        await abilityContext.startAbilityForResult(
          {
            bundleName: "com.ohos.certmanager",
            abilityName: "MainAbility",
            uri: "requestAuthorize",
            parameters: {
              appUid: this.appUid, // Pass the UID of the requesting application.
            }
          } as Want)
          .then((data: common.AbilityResult) => {
            if (!data.resultCode && data.want) {
              if (data.want.parameters) {
                this.authUri = data.want.parameters.authUri as string; // Obtain the returned authUri after successful authorization.
              }
            }
          })
        return this.authUri;
      }
    }
    
3.  Store the context of the current ability to GlobalContext.
    
    // EntryAbility.ets
    import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { window } from '@kit.ArkUI';
    import { GlobalContext } from '../pages/GlobalContext';
    
    const DOMAIN = 0x0000;
    
    export default class EntryAbility extends UIAbility {
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
          this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
          GlobalContext.getContext().setObject("AbilityContext", this.context);
        } catch (err) {
          hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
        }
        hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
      }
    
      onDestroy(): void {
        hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
      }
    
      onWindowStageCreate(windowStage: window.WindowStage): void {
        // Main window is created, set main page for this ability
        hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    
        windowStage.loadContent('pages/Index', (err) => {
          if (err.code) {
            hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
            return;
          }
          hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
        });
      }
    
      onWindowStageDestroy(): void {
        // Main window is destroyed, release UI related resources
        hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
      }
    
      onForeground(): void {
        // Ability has brought to foreground
        hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
      }
    
      onBackground(): void {
        // Ability has back to background
        hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
      }
    }
    
4.  Implement two-way authentication.
    
    import { webview } from '@kit.ArkWeb';
    import CertManagerService from './CertMgrService';
    import { promptAction } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct Index {
      controller: WebviewController = new webview.WebviewController();
      certManager = CertManagerService.getInstance();
    
      aboutToAppear(): void {
        webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
      }
    
      build() {
        Column() {
          Button('Load the website that requires the client SSL certificate')
            .onClick(() => {
              this.controller.loadUrl("https://client.badssl.com")
            })
          Web({
            src: "https://www.bing.com/",
            controller: this.controller,
          }).domStorageAccess(true)
            .fileAccess(true)
            .onPageBegin(event => {
              console.info("extensions onpagebegin url " + event.url);
            })
            .onClientAuthenticationRequest((event) => {
              console.info("onClientAuthenticationRequest ");
    
              this.certManager.grantAppPm().then(result => {
                console.info(\`grantAppPm, URI==========${result}\`);
                event.handler.confirm(result);
              })
              return true;
            })
            .onSslErrorEventReceive(e => {
              console.info(\`onSslErrorEventReceive->${e.error.toString()}\`);
            })
            .onErrorReceive((event) => {
              if (event) {
                this.getUIContext().getPromptAction().showToast({
                  message: \`ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}\`,
                  alignment: Alignment.Center
                })
                console.info('getErrorInfo:' + event.error.getErrorInfo());
                console.info('getErrorCode:' + event.error.getErrorCode());
                console.info('url:' + event.request.getRequestUrl());
              }
            })
            .onTitleReceive(event  => {
              console.info("title received " + event.title);
            })
    
        }
      }
    }
    

#### onVerifyPin22+

onVerifyPin(callback: OnVerifyPinCallback)

Triggered to notify the user of PIN verification. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnVerifyPinCallback](../types/document.md#onverifypincallback22) | Yes | Callback triggered to notify the user of PIN authentication. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: WebviewController = new webview.WebviewController();
  uiContext : UIContext = this.getUIContext();
  context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
  }

  build() {
    Column() {
      Button('Load the website that requires the client SSL certificate')
        .onClick(() => {
          this.controller.loadUrl("https://client.badssl.com")
        })
      Web({
        src: "https://www.bing.com/",
        controller: this.controller,
      }).domStorageAccess(true)
        .fileAccess(true)
        .onPageBegin(event => {
          console.info("extensions onpagebegin url " + event.url);
        })
        .onClientAuthenticationRequest((event) => {
          // Receive the client certificate request event.
          console.info(\`onClientAuthenticationRequest\`);
          try {
            let certTypes: Array<certificateManagerDialog.CertificateType> = \[
              certificateManagerDialog.CertificateType.CREDENTIAL\_UKEY
            \];
            // Invoke the certificate management to open the certificate selection dialog box.
            certificateManagerDialog.openAuthorizeDialog(this.context, { certTypes: certTypes })
              .then((data: certificateManagerDialog.CertReference) => {
                console.info(\`openAuthorizeDialog request cred auth success\`)
                // Notify the web page that the UKey certificate is selected.
                event.handler.confirm(data.keyUri, CredentialType.CREDENTIAL\_UKEY);
              }).catch((err: BusinessError) => {
              console.error(\`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(err)}\`);
            })
          } catch (e) {
            console.error(\`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(e)}\`);
          }
          return true;
        })
        .onVerifyPin((event) => {
          // Receive the PIN verification request event.
          console.info(\`onVerifyPin\`);
          // Invoke the certificate management to open the PIN input box.
          certificateManagerDialog.openUkeyAuthDialog(this.context, {keyUri: event.identity})
            .then(() => {
              // Notify the web page that the PIN verification is successful.
              console.info(\`onVerifyPin success\`);
              event.handler.confirm(PinVerifyResult.PIN\_VERIFICATION\_SUCCESS);
            }).catch((err: BusinessError) => {
            // Notify the web page that the PIN verification fails.
            console.info(\`onVerifyPin fail\`);
            event.handler.confirm(PinVerifyResult.PIN\_VERIFICATION\_FAILED);
          })
        })
        .onSslErrorEventReceive(e => {
          console.info(\`onSslErrorEventReceive->${e.error.toString()}\`);
        })
        .onErrorReceive((event) => {
          if (event) {
            this.getUIContext().getPromptAction().showToast({
              message: \`ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}\`,
              alignment: Alignment.Center
            })
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
          }
        })
        .onTitleReceive(event  => {
          console.info("title received " + event.title);
        })

    }
  }
}

#### onPermissionRequest9+

onPermissionRequest(callback: Callback<OnPermissionRequestEvent>)

Triggered when a permission request is received. To call this API, you need to declare the **ohos.permission.CAMERA** and **ohos.permission.MICROPHONE** permissions.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnPermissionRequestEvent](../interfaces-others/document.md#onpermissionrequestevent12)\> | Yes | Callback invoked when a permission request is received. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear() {
    // Enable web frontend page debugging.
    webview.WebviewController.setWebDebuggingAccess(true);
    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.uiContext.getHostContext(), \['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'\])
      .then((data) => {
        console.info('data:' + JSON.stringify(data));
        console.info('data permissions:' + data.permissions);
        console.info('data authResults:' + data.authResults);
      }).catch((error: BusinessError) => {
      console.error(\`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}\`);
    })
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
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
   <meta charset="UTF-8">
 </head>
 <body>
 <video id="video" width="500px" height="500px" autoplay></video>
 <canvas id="canvas" width="500px" height="500px"></canvas>
 <br>
 <input type="button" title="HTML5 Camera" value="Enable Camera" onclick="getMedia()"/>
 <script>
   function getMedia()
   {
     let constraints = {
       video: {width: 500, height: 500},
       audio: true
     };
     // Obtain the video camera area.
     let video = document.getElementById("video");
     // Returned Promise object.
     let promise = navigator.mediaDevices.getUserMedia(constraints);
     // then() is asynchronous. Invoke the MediaStream object as a parameter.
     promise.then(function (MediaStream) {
       video.srcObject = MediaStream;
       video.play();
     }).catch(function(error) {
       console.error("Error accessing media devices.", error);
     });
   }
 </script>
 </body>
 </html>

#### onContextMenuShow9+

onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean>)

Triggered when a context menu is displayed after the user clicks the right mouse button or long presses a specific element, such as an image or a link.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnContextMenuShowEvent](../interfaces-others/document.md#oncontextmenushowevent12), boolean> | Yes | 
Callback invoked during a call to allow for the display of a custom context menu.

Return value: boolean

The value **true** means that a custom menu is triggered, and **false** means that the custom menu is ineffective.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { pasteboard } from '@kit.BasicServicesKit';

const TAG = 'ContextMenu';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  private result: WebContextMenuResult | undefined = undefined;
  @State linkUrl: string = '';
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State showMenu: boolean = false;
  uiContext: UIContext = this.getUIContext();

  @Builder
  // Build and trigger a custom menu.
  MenuBuilder() {
    // A component that is used to present a vertical list of items to the user.
    Menu() {
      // A component that is used to represent an item in a menu.
      MenuItem({
        content: 'Cancel',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.undo();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Redo',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.redo();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Paste as plain text',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.pasteAndMatchStyle();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy image',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copyImage();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Cut',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.cut();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copy();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Paste',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.paste();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy link',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          let pasteData = pasteboard.createData('text/plain', this.linkUrl);
          pasteboard.getSystemPasteboard().setData(pasteData, (error) => {
            if (error) {
              return;
            }
          })
          this.showMenu = false;
        })
      MenuItem({
        content: 'Select all',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.selectAll();
          this.showMenu = false;
        })
    }
    .width(150)
    .height(450)
  }

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        // Trigger a custom dialog box.
        .onContextMenuShow((event) => {
          if (event) {
            this.result = event.result
            console.info(TAG + "x coord = " + event.param.x());
            console.info(TAG + "link url = " + event.param.getLinkUrl());
            this.linkUrl = event.param.getLinkUrl();
          }
          console.info(TAG, \`x: ${this.offsetX}, y: ${this.offsetY}\`);
          this.showMenu = true;
          this.offsetX = 0;
          this.offsetY = Math.max(this.uiContext!.px2vp(event?.param.y() ?? 0) - 0, 0);
          return true;
        })
        .bindPopup(this.showMenu,
          {
            builder: this.MenuBuilder(),
            enableArrow: false,
            placement: Placement.LeftTop,
            offset: { x: this.offsetX, y: this.offsetY },
            mask: false,
            onStateChange: (e) => {
              if (!e.isVisible) {
                this.showMenu = false;
                this.result!.closeContextMenu();
              }
            }
          })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<body>
  <h1>onContextMenuShow</h1>
  <a href="http://www.example.com" style="font-size:27px">URL www.example.com</a>
  <!-- Place any image in the rawfile directory and name it example.png. -->
  <div><img src="example.png"></div>
  <p>Right-click text to display the context menu</p>
</body>
</html>

#### onContextMenuHide11+

onContextMenuHide(callback: OnContextMenuHideCallback)

Triggered when a context menu is hidden after the user clicks the right mouse button or long presses a specific element, such as an image or a link.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnContextMenuHideCallback](../types/document.md#oncontextmenuhidecallback11) | Yes | Callback related to menus. |

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
        .onContextMenuHide(() => {
          console.info("onContextMenuHide callback");
        })
    }
  }
}

#### onScroll9+

onScroll(callback: Callback<OnScrollEvent>)

Triggered to notify the global scrolling position of the web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/A86rtr5EQwavJ494GIqU9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EC06087DEB9E463687DCC6DA9828F3D616D680E4EA41FF24B5EBF5782C88850)

The change of the partial scrolling position cannot trigger this callback.

To determine whether a page is globally scrolled, print **window.pagYOffset** or **window.pagXOffset** before and after scrolling.

If the web page is scrolled globally, the value of **window.pagYOffset** or **window.pagXOffset** changes after the web page is scrolled. Otherwise, the value does not change.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnScrollEvent](../interfaces-others/document.md#onscrollevent12)\> | Yes | Callback triggered when the page is scrolled to a specified position. |

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
        .onScroll((event) => {
          console.info("x = " + event.xOffset);
          console.info("y = " + event.yOffset);
        })
    }
  }
}

#### onGeolocationShow

onGeolocationShow(callback: Callback<OnGeolocationShowEvent>)

Called to notify the user that the geolocation information obtaining request is received. To use this API, the **ohos.permission.LOCATION** and **ohos.permission.APPROXIMATELY\_LOCATION** permissions must be configured. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnGeolocationShowEvent](../interfaces-others/document.md#ongeolocationshowevent12)\> | Yes | Callback triggered when the geolocation permission is requested, returning the geolocation information request object. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';

let atManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  // Component lifecycle function, which is triggered after a component instance is created.
  aboutToAppear(): void {
    let context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    if (!context) {
      console.error("context is undefined");
      return;
    }
    // Request the location permission from the user.
    atManager.requestPermissionsFromUser(context, \["ohos.permission.LOCATION", "ohos.permission.APPROXIMATELY\_LOCATION"\]).then((data) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}\`);
    })
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .geolocationAccess(true)
        .onGeolocationShow((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              confirm: {
                value: 'onConfirm',
                action: () => {
                  // The third parameter of invoke indicates whether to remember the selection status of the current dialog box. If the value is true, the dialog box will not be displayed next time.
                  event.geolocation.invoke(event.origin, true, false);
                }
              },
              cancel: () => {
                // The third parameter of invoke indicates whether to remember the selection status of the current dialog box. If the value is true, the dialog box will not be displayed next time.
                event.geolocation.invoke(event.origin, false, false);
              }
            })
          }
        })
    }
  }
}

HTML file to be loaded:

<!DOCTYPE html>
<html>
<body>
<p id="locationInfo">Location information</p>
<button onclick="getLocation()">Obtain Location</button>
<script>
var locationInfo=document.getElementById("locationInfo");
function getLocation(){
  if (navigator.geolocation) {
    // Access to the device location by the frontend page
    navigator.geolocation.getCurrentPosition(showPosition);
  }
}
function showPosition(position){
  locationInfo.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;
}
</script>
</body>
</html>

#### onGeolocationHide

onGeolocationHide(callback: () => void)

Triggered to notify the user that the request for obtaining the geolocation information received when [onGeolocationShow](#ongeolocationshow) is called has been canceled.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Callback invoked when the request for obtaining geolocation information has been canceled. |

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
        .onGeolocationHide(() => {
          console.info("onGeolocationHide...");
        })
    }
  }
}

#### onFullScreenEnter9+

onFullScreenEnter(callback: OnFullScreenEnterCallback)

Triggered when the **Web** component enters full screen mode.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnFullScreenEnterCallback](../types/document.md#onfullscreenentercallback12) | Yes | Callback invoked when the **Web** component enters full screen mode. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  handler: FullScreenExitHandler | null = null;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFullScreenEnter((event) => {
          console.info("onFullScreenEnter videoWidth: " + event.videoWidth +
            ", videoHeight: " + event.videoHeight);
          // The application can proactively exit fullscreen mode by calling this.handler.exitFullScreen().
          this.handler = event.handler;
        })
    }
  }
}

#### onFullScreenExit9+

onFullScreenExit(callback: () => void)

Triggered when the **Web** component exits full screen mode.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Callback invoked when the component exits full screen mode. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  handler: FullScreenExitHandler | null = null;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFullScreenExit(() => {
          console.info("onFullScreenExit...")
          if (this.handler) {
            this.handler.exitFullScreen();
          }
        })
        .onFullScreenEnter((event) => {
          this.handler = event.handler;
        })
    }
  }
}

#### onWindowNew9+

onWindowNew(callback: Callback<OnWindowNewEvent>)

Triggered to notify the user of a new window creation request, when **multiWindowAccess** is enabled.

If the [setWebController](../class-controllerhandler/document.md#setwebcontroller9) API is not called, the render process will be blocked.

If no new window is created, set this parameter to **null** when invoking the [setWebController](../class-controllerhandler/document.md#setwebcontroller9) API to notify the **Web** component that no new window is created.

The new window cannot be directly overlaid on the original **Web** component, and its URL (for example, address bar) must be clearly displayed in the same way as the main page to prevent confusion. If visible management of trusted URLs cannot be implemented, consider prohibiting the creation of new windows.

Note that the source of a new window request cannot be reliably traced. The request may be initiated by a third-party iframe. By default, the application needs to take defense measures such as sandbox isolation and permission restriction to ensure security.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnWindowNewEvent](../interfaces-others/document.md#onwindownewevent12)\> | Yes | Callback invoked when the web page requests the user to create a window. |

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
      Web({ src: "www.example.com", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(false)
        .onWindowExit(() => {
          console.info("NewWebViewComp onWindowExit");
          if (this.controller) {
            this.controller.close();
          }
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
      Web({ src: $rawfile("window.html"), controller: this.controller })
        .javaScriptAccess(true)
        // MultiWindowAccess needs to be enabled.
        .multiWindowAccess(true)
        .allowWindowOpenMethod(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController.close();
          }
          let popController: webview.WebviewController = new webview.WebviewController();
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController })
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

<!-- Code of the window.html page -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<a href="#" onclick="openNewWindow('https://www.example.com')">Open a new page</a>
<script type="text/javascript">
    function openNewWindow(url) {
      window.open(url, 'example');
      return false;
    }
</script>
</body>
</html>

#### onActivateContent20+

onActivateContent(callback: Callback<void>)

Triggered to check whether a bound **Web** instance exists based on the name when a web page triggers **window.open(url, name)**. If the instance exists, it receives this callback to notify the application of displaying it on the front end. If it does not exist, the application is notified to create a new **Web** instance through [onWindowNew](#onwindownew9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/J_DT6n2MSQWL0z64NIe-tw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D2AB4991559F4D9F86002FAFF9B03BCC0D5826A9E3FF179D4ABFF7E069B6654)

-   Binding a **Web** instance by name: Call the **event.handler.setWebController** method in the \[onWindowNew\] (#onwindownew9) callback and transfer the controller of the new **Web** instance.
-   The name must comply with the regular expression **\[a-zA-Z0-9\_\]+**. When the name is used as the value of the **target** attribute of the <a> or <form> tag, the bound **Web** instance also triggers this callback function.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | Yes | Callback triggered on a new page after **window.open** is triggered on the original page. |

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
      Web({ src: "https://www.example.com", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(false)
        .onWindowExit(() => {
          if (this.controller) {
            this.controller.close();
          }
        })
        .onActivateContent(() => {
          // The Web component needs to be displayed in the front. It is recommended that the application switch between tabs or windows to display the Web component.
          console.info("NewWebViewComp onActivateContent")
        })
    }.height("50%")
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  dialogController: CustomDialogController | null = null;

  build() {
    Column() {
      Web({ src: $rawfile("window.html"), controller: this.controller })
        .javaScriptAccess(true)
        .allowWindowOpenMethod(true)
        // MultiWindowAccess needs to be enabled.
        .multiWindowAccess(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController.close()
          }
          let popController: webview.WebviewController = new webview.WebviewController();
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController }),
            isModal: false
          })
          this.dialogController.open();
          // Return the WebviewController object corresponding to the new window to the web kernel.
          // If the event.handler.setWebController API is not called, the render process will be blocked.
          event.handler.setWebController(popController);
        })
    }
  }
}

<!-- Code of the window.html page -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ActivateContentEvent</title>
</head>
<body>
<a href="#" onclick="openNewWindow('https://www.example.com')">Open a new page</a>
<script type="text/javascript">
    function openNewWindow(url) {
      window.open(url, 'example');
      return false;
    }
</script>
</body>
</html>

#### onWindowExit9+

onWindowExit(callback: () => void)

Triggered when this window is closed. This API works in the same way as [onWindowNew](#onwindownew9). For security, applications should notify users that the pages they interact with are closed.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Callback invoked when the window is closed. |

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
        .onWindowExit(() => {
          console.info("onWindowExit...");
        })
    }
  }
}

#### onSearchResultReceive9+

onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent>)

Triggered to notify the caller of the search result on the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnSearchResultReceiveEvent](../interfaces-others/document.md#onsearchresultreceiveevent12)\> | Yes | Callback invoked to notify the caller of the search result on the web page. |

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
        .onSearchResultReceive(ret => {
          if (ret) {
            console.info("on search result receive:" + "\[cur\]" + ret.activeMatchOrdinal +
              "\[total\]" + ret.numberOfMatches + "\[isDone\]" + ret.isDoneCounting);
          }
        })
    }
  }
}

#### onDataResubmitted9+

onDataResubmitted(callback: Callback<OnDataResubmittedEvent>)

Triggered when the web form data can be resubmitted.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnDataResubmittedEvent](../interfaces-others/document.md#ondataresubmittedevent12)\> | Yes | Callback invoked when the web form data can be resubmitted. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // After you click Submit on the web page, you can click Refresh to trigger the function again.
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onDataResubmitted((event) => {
          console.info('onDataResubmitted');
          event.handler.resend();
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
   <form action="http://httpbin.org/post" method="post">
     <input type="text" name="username">
     <input type="submit" name="Submit">
   </form>
 </body>
 </html>

#### onPageVisible9+

onPageVisible(callback: Callback<OnPageVisibleEvent>)

Triggered when the old page is not displayed and the new page is about to be visible.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnPageVisibleEvent](../interfaces-others/document.md#onpagevisibleevent12)\> | Yes | Callback invoked when the old page is not displayed and the new page is about to be visible. |

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
        .onPageVisible((event) => {
          console.info('onPageVisible url:' + event.url);
        })
    }
  }
}

#### onInterceptKeyEvent9+

onInterceptKeyEvent(callback: (event: KeyEvent) => boolean)

Triggered when the key event is intercepted and before it is consumed by the webview.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event:[KeyEvent](../../../../arkui/arkts-components/universal-events/basic-input-events/key-event/document.md#keyevent)) => boolean | Yes | 
Key event that is triggered.

The return value is of the Boolean type. The value **true** means to pass the **KeyEvent** to the Webview kernel, and **false** means the opposite.

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
        .onInterceptKeyEvent((event) => {
          if (event.keyCode == 2017 || event.keyCode == 2018) {
            console.info(\`onInterceptKeyEvent get event.keyCode ${event.keyCode}\`);
            return true;
          }
          return false;
        })
    }
  }
}

#### onTouchIconUrlReceived9+

onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent>)

Triggered when an apple-touch-icon URL is received.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnTouchIconUrlReceivedEvent](../interfaces-others/document.md#ontouchiconurlreceivedevent12)\> | Yes | Callback invoked when an apple-touch-icon URL is received. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.baidu.com', controller: this.controller })
        .onTouchIconUrlReceived((event) => {
          console.info('onTouchIconUrlReceived:' + JSON.stringify(event));
        })
    }
  }
}

#### onFaviconReceived9+

onFaviconReceived(callback: Callback<OnFaviconReceivedEvent>)

Triggered when this web page receives a new favicon.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnFaviconReceivedEvent](../interfaces-others/document.md#onfaviconreceivedevent12)\> | Yes | Callback invoked when the current web page receives a new favicon. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State icon: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFaviconReceived((event) => {
          console.info('onFaviconReceived');
          this.icon = event.favicon;
        })
    }
  }
}

#### onAudioStateChanged10+

onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent>)

Triggered when the audio playback status on the web page changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnAudioStateChangedEvent](../interfaces-others/document.md#onaudiostatechangedevent12)\> | Yes | Callback invoked when the audio playback status on the web page changes. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State playing: boolean = false;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onAudioStateChanged(event => {
          this.playing = event.playing;
          console.info('onAudioStateChanged playing: ' + this.playing);
        })
    }
  }
}

#### onFirstContentfulPaint10+

onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent>)

Triggered when the first content paint occurs on the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnFirstContentfulPaintEvent](../interfaces-others/document.md#onfirstcontentfulpaintevent12)\> | Yes | Callback invoked when the first content paint occurs on the web page. |

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
        .onFirstContentfulPaint(event => {
          if (event) {
            console.info("onFirstContentfulPaint:" + "\[navigationStartTick\]:" +
            event.navigationStartTick + ", \[firstContentfulPaintMs\]:" +
            event.firstContentfulPaintMs);
          }
        })
    }
  }
}

#### onFirstMeaningfulPaint12+

onFirstMeaningfulPaint(callback: [OnFirstMeaningfulPaintCallback](../types/document.md#onfirstmeaningfulpaintcallback12))

Triggered when the first meaningful paint occurs on the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnFirstMeaningfulPaintCallback](../types/document.md#onfirstmeaningfulpaintcallback12) | Yes | Callback invoked when the First Meaningful Paint occurs on the web page. |

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
        .onFirstMeaningfulPaint((details) => {
          console.info("onFirstMeaningfulPaint: \[navigationStartTime\]= " + details.navigationStartTime +
            ", \[firstMeaningfulPaintTime\]=" + details.firstMeaningfulPaintTime);
        })
    }
  }
}

#### onLargestContentfulPaint12+

onLargestContentfulPaint(callback: [OnLargestContentfulPaintCallback](../types/document.md#onlargestcontentfulpaintcallback12))

Triggered when the largest content paint occurs on the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnLargestContentfulPaintCallback](../types/document.md#onlargestcontentfulpaintcallback12) | Yes | Callback invoked when the largest content paint occurs on the web page. |

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
        .onLargestContentfulPaint((details) => {
          console.info("onLargestContentfulPaint: \[navigationStartTime\]= " + details.navigationStartTime +
            ", \[largestImagePaintTime\]=" + details.largestImagePaintTime +
            ", \[largestTextPaintTime\]=" + details.largestTextPaintTime +
            ", \[largestImageLoadStartTime\]=" + details.largestImageLoadStartTime +
            ", \[largestImageLoadEndTime\]=" + details.largestImageLoadEndTime +
            ", \[imageBPP\]=" + details.imageBPP);
        })
    }
  }
}

#### onLoadIntercept10+

onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean>)

Triggered when the **Web** component is about to access a URL. This API is used to determine whether to block the access.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnLoadInterceptEvent](../interfaces-others/document.md#onloadinterceptevent12), boolean> | Yes | 
Callback triggered when a navigation (including iframe navigation) occurs, allowing the application to approve or cancel it.

The return value is of the Boolean type. The value **true** means to cancel the navigation, and **false** means the opposite.

If **undefined** or **null** is returned, the value is **false**.

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
        .onLoadIntercept((event) => {
          console.info('url:' + event.data.getRequestUrl());
          console.info('isMainFrame:' + event.data.isMainFrame());
          console.info('isRedirect:' + event.data.isRedirect());
          console.info('isRequestGesture:' + event.data.isRequestGesture());
          return true;
        })
    }
  }
}

#### onRequestSelected

onRequestSelected(callback: () => void)

Triggered when the **Web** component obtains the focus. If the **Web** component loads a web page in the unfocused state and successfully obtains the focus, the callback is triggered twice.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Callback triggered when a web page obtains the focus. |

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
        .onRequestSelected(() => {
          console.info('onRequestSelected');
        })
    }
  }
}

#### onScreenCaptureRequest10+

onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent>)

Triggered when a screen capture request is received.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnScreenCaptureRequestEvent](../interfaces-others/document.md#onscreencapturerequestevent12)\> | Yes | Callback invoked when a screen capture request is received. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScreenCaptureRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title: ' + event.handler.getOrigin(),
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.handler.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.handler.grant({ captureMode: WebCaptureMode.HOME\_SCREEN });
                }
              },
              cancel: () => {
                event.handler.deny();
              }
            })
          }
        })
    }
  }
}

#### onOverScroll10+

onOverScroll(callback: Callback<OnOverScrollEvent>)

Triggered when the web page is overscrolled. It is used to notify the application of the overscroll offset.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnOverScrollEvent](../interfaces-others/document.md#onoverscrollevent12)\> | Yes | Callback invoked when the web page is overscrolled. |

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
        .onOverScroll((event) => {
          console.info("x = " + event.xOffset);
          console.info("y = " + event.yOffset);
        })
    }
  }
}

#### onControllerAttached10+

onControllerAttached(callback: () => void)

Triggered when the controller is successfully bound to the **Web** component. The controller must be **WebviewController**. Do not call APIs related to the **Web** component before this callback event. Otherwise, a js-error exception will be thrown.

The web page has not been loaded when the callback is called. Therefore, APIs related to web page operations, such as [zoomIn](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#zoomin), [zoomOut](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#zoomout), cannot be used in the callback. You can use APIs irrelevant to web page operations, such as [loadUrl](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#loadurl), [getWebId](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#getwebid).

For details about the component lifecycle, see [Lifecycle of the Web Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-event-sequence).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Callback invoked when the ArkWeb controller is successfully initialized. |

**Example**

The following example uses **loadUrl** in the callback to load the web page.

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: '', controller: this.controller })
        .onControllerAttached(() => {
          this.controller.loadUrl($rawfile("index.html"));
        })
    }
  }
}

The following example uses **getWebId** in the callback.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onControllerAttached(() => {
          try {
            let id = this.controller.getWebId();
            console.info("id: " + id);
          } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`ErrorCode: ${code},  Message: ${message}\`);
          }
        })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
    <body>
        <p>Hello World</p>
    </body>
</html>

#### onNavigationEntryCommitted11+

onNavigationEntryCommitted(callback: [OnNavigationEntryCommittedCallback](../types/document.md#onnavigationentrycommittedcallback11))

Triggered when a web page redirection request is submitted.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnNavigationEntryCommittedCallback](../types/document.md#onnavigationentrycommittedcallback11) | Yes | Callback invoked when a web page redirection request is submitted. |

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
        .onNavigationEntryCommitted((details) => {
          console.info("onNavigationEntryCommitted: \[isMainFrame\]= " + details.isMainFrame +
            ", \[isSameDocument\]=" + details.isSameDocument +
            ", \[didReplaceEntry\]=" + details.didReplaceEntry +
            ", \[navigationType\]=" + details.navigationType +
            ", \[url\]=" + details.url);
        })
    }
  }
}

#### onSafeBrowsingCheckResult11+

onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback)

Called when the safe browsing check result is received.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/74t_ToZ7Qaul3Lxqq0NOUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B7E0DA69A7F8BF3BC879ECBD8F9FA3FABA57FF49073422410B6DD3058CE77A3)

-   The release package is required. The debug package does not take effect.
-   Callback triggered when minor mode is enabled and web content blocking is set.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnSafeBrowsingCheckResultCallback](../types/document.md#onsafebrowsingcheckresultcallback11) | Yes | Callback invoked when the safe browsing check result is received. |

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
        .onSafeBrowsingCheckResult((callback) => {
          let json: ThreatType = JSON.parse(JSON.stringify(callback)).threatType;
          console.info("onSafeBrowsingCheckResult: \[threatType\]= " + json);
        })
    }
  }
}

#### onSafeBrowsingCheckFinish21+

onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback)

Called when the safe browsing check is complete.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Y5KdbWYKRICikAQhu-hoBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3C378E9A1C80D23C1643471A8B44ABC1BF59214532C4039EBE545D006F2E262)

-   The release package is required. The debug package does not take effect.
-   Callback triggered when minor mode is enabled and web content blocking is set.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnSafeBrowsingCheckResultCallback](../types/document.md#onsafebrowsingcheckresultcallback11) | Yes | Callback invoked when the safe browsing check result is received. |

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
        .onSafeBrowsingCheckFinish((callback) => {
          let json: ThreatType = JSON.parse(JSON.stringify(callback)).threatType;
          console.info("onSafeBrowsingCheckFinish: \[threatType\]= " + json);
        })
    }
  }
}

#### onNativeEmbedLifecycleChange11+

onNativeEmbedLifecycleChange(callback: (event: NativeEmbedDataInfo) => void)

Triggered when the lifecycle of the same-layer tag changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event: [NativeEmbedDataInfo](../interfaces-others/document.md#nativeembeddatainfo11)) => void | Yes | Callback invoked when the lifecycle of the same-layer tag changes. |

**Example**

// EntryAbility.ets

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    // Added in API version 12: feature to enable the back/forward cache for same-layer rendering.
    let features = new webview.BackForwardCacheSupportedFeatures();
    features.nativeEmbed = true;
    features.mediaTakeOver = true;
    webview.WebviewController.enableBackForwardCache(features);
    webview.WebviewController.initializeWebEngine();
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  @State embedStatus: string = '';
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Default behavior: Click the button to navigate to a new page, close the index page, and destroy the same-layer tag.
      // Added in API version 12: When BFCache is enabled for the page that supports same-layer rendering, clicking the button navigates to a new page, closes the index page, and puts the same-layer tag into BFCache.
      Button('Destroy')
      .onClick(() => {
        try {
          this.controller.loadUrl("www.example.com");
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })

      // Added in API version 12: When BFCache is enabled for the page that supports same-layer rendering, clicking the button to return to the page causes the same-layer tag to exit BFCache.
      Button('backward')
      .onClick(() => {
        try {
          this.controller.backward();
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })

      // Added in API version 12: When BFCache is enabled for the page that supports same-layer rendering, clicking a button to advance to the next page causes the same-layer tag to enter BFCache.
      Button('forward')
      .onClick(() => {
        try {
          this.controller.forward();
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })

      // Added in API version 12: The web kernel does not allow web pages loaded with non-HTTP and non-HTTPS protocols to enter BFCache.
      // Therefore, to test the ENTER\_BFCACHE/LEAVE\_BFCACHE states, you need to place the index.html on a web server and load it using the HTTP or HTTPS protocol. Example:
      // Web({ src: "http://xxxx/index.html", controller: this.controller })
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableNativeEmbedMode(true)
        .onNativeEmbedLifecycleChange((event) => {
          // The Create event is triggered when the same-layer tag is detected on the loaded page.
          if (event.status == NativeEmbedStatus.CREATE) {
            this.embedStatus = 'Create';
          }
          // The Update event is triggered when the same-layer tag on the page is moved or scaled.
          if (event.status == NativeEmbedStatus.UPDATE) {
            this.embedStatus = 'Update';
          }
          // The Destroy event is triggered when a user exit the page.
          if (event.status == NativeEmbedStatus.DESTROY) {
            this.embedStatus = 'Destroy';
          }
          // The Enter BFCache event is triggered when the page with the same-layer tag enters BFCache.
          if (event.status == NativeEmbedStatus.ENTER\_BFCACHE) {
            this.embedStatus = 'Enter BFCache';
          }
          // The Leave BFCache event is triggered when the page with the same-layer tag leaves BFCache.
          if (event.status == NativeEmbedStatus.LEAVE\_BFCACHE) {
            this.embedStatus = 'Leave BFCache';
          }
          console.info("status = " + this.embedStatus);
          console.info("surfaceId = " + event.surfaceId);
          console.info("embedId = " + event.embedId);
          if (event.info) {
            console.info("id = " + event.info.id);
            console.info("type = " + event.info.type);
            console.info("src = " + event.info.src);
            console.info("width = " + event.info.width);
            console.info("height = " + event.info.height);
            console.info("url = " + event.info.url);
          }
        })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test HTML</title>
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
        <embed id="nativeButton" type = "native/button" width="800" height="800" src="test? params1=1" style = "background-color:red"/>
    </div>
</div>
</body>
</html>

#### onNativeEmbedGestureEvent11+

onNativeEmbedGestureEvent(callback: (event: NativeEmbedTouchInfo) => void)

Triggered when a finger touches a same-layer tag.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event: [NativeEmbedTouchInfo](../interfaces-others/document.md#nativeembedtouchinfo11)) => void | Yes | Callback invoked when a finger touches a same-layer tag. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

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

  postEvent(event: TouchEvent | undefined): boolean {
    return this.rootNode?.postTouchEvent(event) as boolean;
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
  @State eventType: string = '';
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile("index.html"), controller: this.controller })
          .enableNativeEmbedMode(true)
          .onNativeEmbedLifecycleChange((embed) => {
            if (embed.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: embed.surfaceId as string,
                renderType: NodeRenderType.RENDER\_TYPE\_TEXTURE,
                width: this.uiContext!.px2vp(embed.info?.width),
                height: this.uiContext!.px2vp(embed.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedGestureEvent((event) => {
            if (event && event.touchEvent) {
              if (event.touchEvent.type == TouchType.Down) {
                this.eventType = 'Down'
              }
              if (event.touchEvent.type == TouchType.Up) {
                this.eventType = 'Up'
              }
              if (event.touchEvent.type == TouchType.Move) {
                this.eventType = 'Move'
              }
              if (event.touchEvent.type == TouchType.Cancel) {
                this.eventType = 'Cancel'
              }
              let ret = this.nodeController.postEvent(event.touchEvent)
              if (event.result) {
                event.result.setGestureEventResult(ret, true);
              }
              console.info("embedId = " + event.embedId);
              console.info("touchType = " + this.eventType);
              console.info("x = " + event.touchEvent.touches\[0\].x);
              console.info("y = " + event.touchEvent.touches\[0\].y);
              console.info("Component globalPos:(" + event.touchEvent.target.area.globalPosition.x + "," + event.touchEvent.target.area.globalPosition.y + ")");
              console.info("width = " + event.touchEvent.target.area.width);
              console.info("height = " + event.touchEvent.target.area.height);
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
    <title>Same-Layer Rendering Test HTML</title>
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
       <embed id="nativeButton" type = "native/button" width="800" height="800" src="test?params1=1" style = "background-color:red"/>
    </div>
</div>
</body>
</html>

#### onIntelligentTrackingPreventionResult12+

onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback)

Triggered when the intelligent tracking prevention feature is enabled and the tracker cookie is blocked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/1DHSvpjrSXunqfIxDCDlNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37F8DDA45FE5532C759E7D95FDBE085914CB7B9977B099207AC5E09901AFE157)

-   The release package is required. The debug package does not take effect.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnIntelligentTrackingPreventionCallback](../types/document.md#onintelligenttrackingpreventioncallback12) | Yes | Callback invoked when the intelligent tracking prevention feature is enabled and the tracker cookie is blocked. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // The onIntelligentTrackingPreventionResult callback is triggered only when the intelligent tracking prevention feature is enabled.
      Button('enableIntelligentTrackingPrevention')
        .onClick(() => {
          try {
            this.controller.enableIntelligentTrackingPrevention(true);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onIntelligentTrackingPreventionResult((details) => {
          console.info("onIntelligentTrackingPreventionResult: \[websiteHost\]= " + details.host +
            ", \[trackerHost\]=" + details.trackerHost);
        })
    }
  }
}

#### onOverrideUrlLoading12+

onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback)

Triggered when the URL is about to be loaded in the current web page, allowing the host application to obtain control and determine whether to prevent the web page from loading the URL.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/u-cI4PelTLSN96nsphAGzQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39DE3A45A0621FA14CB8E224E1C4EB2A80F57FC6B82D5496B4EFA1AC328C4E04)

-   POST requests do not trigger this callback.
-   This callback is triggered when the iframe loads a non-HTTP(S) document. It is not triggered for HTTP(S) documents, **about:blank**, or for any redirection that is started via **loadUrl(url: string)**.
-   Do not call **loadUrl(url: string)** with the same URL in the callback and return **true**. Doing so would unnecessarily cancel the current loading and start an identical one. To continue loading the current request URL, return **false** instead of calling **loadUrl(url: string)**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnOverrideUrlLoadingCallback](../types/document.md#onoverrideurlloadingcallback12) | Yes | 
Callback for **onOverrideUrlLoading**.

Return value: boolean

The value **true** means to stop loading the URL, and the value **false** means the opposite.

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
        .onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
          if (webResourceRequest && webResourceRequest.getRequestUrl() == "about:blank") {
            return true;
          }
          return false;
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
  <h1>onOverrideUrlLoading Demo</h1>
  <a href="about:blank">Click here</a>// to visit about:blank.
</body>
</html>

#### onViewportFitChanged12+

onViewportFitChanged(callback: OnViewportFitChangedCallback)

Triggered when the **viewport-fit** configuration in the web page's **meta** tag changes. The application can adapt its layout to the viewport within this callback.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnViewportFitChangedCallback](../types/document.md#onviewportfitchangedcallback12) | Yes | Callback invoked when the **viewport-fit** configuration in the web page's **meta** tag changes. |

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
        .onViewportFitChanged((data) => {
          let jsonData = JSON.stringify(data);
          let viewportFit: ViewportFit = JSON.parse(jsonData).viewportFit;
          if (viewportFit === ViewportFit.COVER) {
            // The index.html web page supports immersive layout. You can call expandSafeArea to adjust the Web component layout viewport to cover the safe area (status bar or navigation bar).
          } else if (viewportFit === ViewportFit.CONTAINS) {
            // The index.html web page does not support immersive layout. You can call expandSafeArea to adjust the Web component layout viewport as a safe area.
          } else {
            // Default value. No processing is required.
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
    <meta name="viewport" content="width=device-width,viewport-fit=cover">
  </head>
  <body>
    <div style="position: absolute; bottom: 0; margin-bottom: env(safe-area-inset-bottom)"></div>
  </body>
</html>

#### onInterceptKeyboardAttach12+

onInterceptKeyboardAttach(callback: WebKeyboardCallback)

Triggered before any editable element (such as the **input** tag) on the web page invokes the soft keyboard. The application can use this API to intercept the display of the system's soft keyboard and configure a custom soft keyboard. (With this API, the application can determine whether to use the system's default soft keyboard, a system soft keyboard with a custom Enter key, or a completely application-defined soft keyboard).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [WebKeyboardCallback](../types/document.md#webkeyboardcallback12) | Yes | Callback invoked for intercepting the soft keyboard started by the web page. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { inputMethodEngine } from '@kit.IMEKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  webKeyboardController: WebKeyboardController = new WebKeyboardController()
  inputAttributeMap: Map<string, number> = new Map(\[
      \['UNSPECIFIED', inputMethodEngine.ENTER\_KEY\_TYPE\_UNSPECIFIED\],
      \['GO', inputMethodEngine.ENTER\_KEY\_TYPE\_GO\],
      \['SEARCH', inputMethodEngine.ENTER\_KEY\_TYPE\_SEARCH\],
      \['SEND', inputMethodEngine.ENTER\_KEY\_TYPE\_SEND\],
      \['NEXT', inputMethodEngine.ENTER\_KEY\_TYPE\_NEXT\],
      \['DONE', inputMethodEngine.ENTER\_KEY\_TYPE\_DONE\],
      \['PREVIOUS', inputMethodEngine.ENTER\_KEY\_TYPE\_PREVIOUS\]
    \])

    /\*\*
     \* Builder for a custom keyboard component.
     \*/
    @Builder
    customKeyboardBuilder() {
        // Implement a custom keyboard component and connect it to WebKeyboardController to implement operations such as input, deletion, and close.
      Row() {
        Text("Finish")
          .fontSize(20)
          .fontColor(Color.Blue)
          .onClick(() => {
            this.webKeyboardController.close();
          })
        // Insert characters.
        Button("insertText").onClick(() => {
          this.webKeyboardController.insertText('insert ');
        }).margin({
          bottom: 200,
        })
        // Delete characters from the end to the beginning for the length specified by the length parameter.
        Button("deleteForward").onClick(() => {
          this.webKeyboardController.deleteForward(1);
        }).margin({
          bottom: 200,
        })
        // Delete characters from the beginning to the end for the length specified by the length parameter.
        Button("deleteBackward").onClick(() => {
          this.webKeyboardController.deleteBackward(1);
        }).margin({
          left: -220,
        })
        // Insert a function key.
        Button("sendFunctionKey").onClick(() => {
          this.webKeyboardController.sendFunctionKey(6);
        })
      }
    }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
      .onInterceptKeyboardAttach((KeyboardCallbackInfo) => {
        // Initialize option. By default, the default keyboard is used.
        let option: WebKeyboardOptions = {
          useSystemKeyboard: true,
        };
        if (!KeyboardCallbackInfo) {
          return option;
        }

        // Save the WebKeyboardController. When a custom keyboard is used, this handler is required to control behaviors such as input, deletion, and closing of the keyboard.
        this.webKeyboardController = KeyboardCallbackInfo.controller
        let attributes: Record<string, string> = KeyboardCallbackInfo.attributes
        // Traverse attributes.
        let attributeKeys = Object.keys(attributes)
        for (let i = 0; i < attributeKeys.length; i++) {
          console.info('WebCustomKeyboard key = ' + attributeKeys\[i\] + ', value = ' + attributes\[attributeKeys\[i\]\])
        }

        if (attributes) {
          if (attributes\['data-keyboard'\] == 'customKeyboard') {
            // Determine the soft keyboard to use based on the attributes of editable HTML elements. For example, if the attribute includes data-keyboard and its value is customKeyboard, custom keyboard is used.
            console.info('WebCustomKeyboard use custom keyboard')
            option.useSystemKeyboard = false;
            // Set the custom keyboard builder.
            option.customKeyboard = () => {
              this.customKeyboardBuilder()
            }
            return option;
          }

          if (attributes\['keyboard-return'\] != undefined) {
            // Determine the soft keyboard to use based on the attributes of editable HTML elements. For example, if the attribute includes keyboard-return, use the system keyboard and specify the type of the system soft keyboard's Enter key.
            option.useSystemKeyboard = true;
            let enterKeyType: number | undefined = this.inputAttributeMap.get(attributes\['keyboard-return'\])
            if (enterKeyType != undefined) {
              option.enterKeyType = enterKeyType
            }
            return option;
          }
        }

        return option;
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
      <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0">
  </head>

  <body>

  <p style="font-size:12px">input tag. Original default behavior: </p>
  <input type="text" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as UNSPECIFIED: </p>
  <input type="text" keyboard-return="UNSPECIFIED" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as GO: </p>
  <input type="text" keyboard-return="GO" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as SEARCH: </p>
  <input type="text" keyboard-return="SEARCH" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as SEND: </p>
  <input type="text" keyboard-return="SEND" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as NEXT: </p>
  <input type="text" keyboard-return="NEXT" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as DONE: </p>
  <input type="text" keyboard-return="DONE" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as PREVIOUS: </p>
  <input type="text" keyboard-return="PREVIOUS" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. Custom keyboard: </p>
  <input type="text" data-keyboard="customKeyboard" style="width: 300px; height: 20px"><br>

  </body>

  </html>

#### onNativeEmbedVisibilityChange12+

onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback)

Triggered when the visibility of a same-layer tag (such as an **<embed>** tag or an **<object>** tag) on a web page changes in the viewport. Same-layer tags are invisible by default. If a tag is visible when the page is loaded for the first time, it is reported. If a tag is invisible, it is not reported. Same-layer tags are considered invisible only when they are all invisible. Partially visible or all visible tags are considered visible. To obtain the visible status change caused by the CSS attributes (including visibility, display, and size change) of the same-layer tag, configure [nativeEmbedOptions](../attributes/document.md#nativeembedoptions16) and set **supportCssDisplayChange** in [EmbedOptions](../interfaces-others/document.md#embedoptions16) to **true**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnNativeEmbedVisibilityChangeCallback](../types/document.md#onnativeembedvisibilitychangecallback12) | Yes | Callback invoked when the visibility of a same-layer tag changes. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

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

  postEvent(event: TouchEvent | undefined): boolean {
    return this.rootNode?.postTouchEvent(event) as boolean;
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
  @State embedVisibility: string = '';
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile("index.html"), controller: this.controller })
          .enableNativeEmbedMode(true)
          .onNativeEmbedLifecycleChange((embed) => {
            if (embed.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: embed.surfaceId as string,
                renderType: NodeRenderType.RENDER\_TYPE\_TEXTURE,
                width: this.uiContext!.px2vp(embed.info?.width),
                height: this.uiContext!.px2vp(embed.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedVisibilityChange((embed) => {
            if (embed.visibility) {
              this.embedVisibility = 'Visible';
            } else {
              this.embedVisibility = 'Hidden';
            }
            console.info("embedId = " + embed.embedId);
            console.info("visibility = " + embed.visibility);
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
    <title>Same-Layer Rendering Test HTML</title>
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
        <embed id="nativeButton" type = "native/button" width="800" height="800" src="test?params1=1" style = "background-color:red"/>
    </div>
</div>
</body>
</html>

#### onNativeEmbedMouseEvent20+

onNativeEmbedMouseEvent(callback: MouseInfoCallback)

Triggered when the following operations are performed on the same-layer tag:

-   Tapping or holding with the left, middle, or right mouse button.
-   Tapping or holding the left, middle, or right mouse button using the touchpad.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [MouseInfoCallback](../types/document.md#mouseinfocallback20) | Yes | Callback triggered when a same-layer tag is clicked using the mouse or touchpad. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

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
  @State mouseAction: string = '';
  @State mouseButton: string = '';
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile("index.html"), controller: this.controller })
          .enableNativeEmbedMode(true)
          .onNativeEmbedLifecycleChange((embed) => {
            if (embed.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: embed.surfaceId as string,
                renderType: NodeRenderType.RENDER\_TYPE\_TEXTURE,
                width: this.uiContext!.px2vp(embed.info?.width),
                height: this.uiContext!.px2vp(embed.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedMouseEvent((event) => {
            if (event && event.mouseEvent) {
              let ret = this.nodeController.postInputEvent(event.mouseEvent)
              if (event.result) {
                event.result.setMouseEventResult(ret, true);
              }
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
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
        <embed id="nativeButton" type ="native/button" width="800" height="800" style="background-color:red"/>
    </div>
</div>
</body>
</html>

#### onNativeEmbedObjectParamChange21+

onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback)

Called when the **param** element embedded in the same-layer rendering tag **object** changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnNativeEmbedObjectParamChangeCallback](../types/document.md#onnativeembedobjectparamchangecallback21) | Yes | Callback triggered when the **param** element embedded in the same-layer rendering tag **object** is added, modified, or deleted. |

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
            .enableNativeEmbedMode(true)
            .registerNativeEmbedRule("object", "native")
            .onNativeEmbedLifecycleChange((embed) => {
              if (embed.status == NativeEmbedStatus.CREATE) {
                this.nodeController.setRenderOption({
                  surfaceId: embed.surfaceId as string,
                  renderType: NodeRenderType.RENDER\_TYPE\_TEXTURE,
                  width: this.uiContext!.px2vp(embed.info?.width),
                  height: this.uiContext!.px2vp(embed.info?.height)
                });
                this.nodeController.rebuild();
              }
            })
            .onNativeEmbedObjectParamChange((event) => {
              console.info("embed id: " + event.embedId);
              let paramItems = event.paramItems;
              if (paramItems) {
                for (let i = 0; i < paramItems.length; ++i) {
                  console.info("param info: " + JSON.stringify(paramItems\[i\]));
                }
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
          <param id="param-1" name="name-1" value="value1"/>
        </object>
    </div>
</div>
</body>
</html>

#### onOverrideErrorPage20+

onOverrideErrorPage(callback: OnOverrideErrorPageCallback)

Triggered when an error occurs during web page loading of main resources. You can use this API to customize the error display page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/9RIRVrvBQFq0yuY49Rcu9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06FCE63E17F2BA6BFB8E1B627D2D1AF9CE42490EB1730190D53DAF27FCE8B0B3)

This feature takes effect only after the default error page is enabled by calling the [setErrorPageEnabled](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#seterrorpageenabled20) API.

If the error code obtained through [errorPageEvent.error.getErrorCode()](../class-webresourceerror/document.md#geterrorcode) is greater than 0, it indicates an HTTP error. If the error code is less than 0, it indicates a network error.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnOverrideErrorPageCallback](../types/document.md#onoverrideerrorpagecallback20) | Yes | Callback triggered when an error occurs during web page loading. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: "www.error-test.com", controller: this.controller })
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
        .onOverrideErrorPage(event => {
              let htmlStr = "<html><h1>error occur : ";
              htmlStr += event.error.getErrorCode();
              htmlStr += "</h1></html>";
              return htmlStr;
        })
    }
  }
}

#### onSslErrorReceive(deprecated)

onSslErrorReceive(callback: (event?: { handler: Function, error: object }) => void)

Triggered when an SSL error occurs during resource loading.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/5PnVLVdAQC6MjHUURO1hpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E48BC6E4EC2307354C0CBFFF789620441EAB32B2B77AD795C0772E0AD576EDC0)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [onSslErrorEventReceive9+](#onsslerroreventreceive9) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event?: { handler: Function, error: object }) => void | Yes | Callback triggered when a web page detects an SSL error. |

#### onFileSelectorShow(deprecated)

onFileSelectorShow(callback: (event?: { callback: Function, fileSelector: object }) => void)

Triggered to process an HTML form whose input type is **file**, in response to the tapping of the **Select File** button.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/7uPGAVAcS56Gk-5HvJ1_TQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B2AC9422CD53F6404E4E1E9BE02E25B82D13A6AC399253150B1D48A12033352)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [onShowFileSelector9+](#onshowfileselector9) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event?: { callback: Function, fileSelector: object }) => void | Yes | Callback to be executed when the file selector is triggered. |

#### onUrlLoadIntercept(deprecated)

onUrlLoadIntercept(callback: (event?: { data:string | WebResourceRequest }) => boolean)

Triggered when the **Web** component is about to access a URL. This API is used to determine whether to block the access.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/bnMiPhakSsahrbmpemJYRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02D35DC6C2924EB85F8293B53F28DE1F5660DD614A6AD1DC0A44A7A6109C2532)

This API is supported since API version 8 and deprecated since API version 10. You are advised to use [onLoadIntercept10+](#onloadintercept10) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event?: { data:string | [WebResourceRequest](../class-webresourcerequest/document.md) }) => boolean | Yes | 
URL information.

The return value is of the Boolean type. If **true** is returned, the access is blocked. Otherwise, the access is allowed.

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
        .onUrlLoadIntercept((event) => {
          if (event) {
            console.info('onUrlLoadIntercept ' + event.data.toString());
          }
          return true
        })
    }
  }
}

#### onPdfLoadEvent20+

onPdfLoadEvent(callback: Callback<OnPdfLoadEvent>)

Called to notify the user of whether the PDF page is successfully loaded.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnPdfLoadEvent](../interfaces-others/document.md#onpdfloadevent20)\> | Yes | Callback triggered to notify users of whether the PDF page is successfully loaded. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Replace 'https://www.example.com/xxx.pdf' with the actual accessible address.
      Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
        .onPdfLoadEvent((eventInfo: OnPdfLoadEvent) => {
          console.info(\`Load event callback called. url: ${eventInfo.url}, result: ${eventInfo.result}.\`)
        })
    }
  }
}

#### onPdfScrollAtBottom20+

onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent>)

Called to notify the user that the PDF page has been scrolled to the bottom.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[OnPdfScrollEvent](../interfaces-others/document.md#onpdfscrollevent20)\> | Yes | Callback triggered to notify the user that the PDF page has been scrolled to the bottom. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Replace 'https://www.example.com/xxx.pdf' with the actual accessible address.
      Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
        .onPdfScrollAtBottom((eventInfo: OnPdfScrollEvent) => {
          console.info(\`Scroll at bottom callback called. url: ${eventInfo.url}.\`)
        })
    }
  }
}

#### onDetectedBlankScreen22+

onDetectedBlankScreen(callback: OnDetectBlankScreenCallback)

Called when the **Web** component detects a blank screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/kKsvnY8xS-GZgvqMM9Ri1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=802916E7B9FF509539DB229EB012CCC33C4256D38F383CF80D665976DBBC8B71)

-   This method must be used with [blankScreenDetectionConfig](../attributes/document.md#blankscreendetectionconfig22). Otherwise, the blank screen detection is disabled by default, and the callback is not returned when a blank screen is detected.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnDetectBlankScreenCallback](../types/document.md#ondetectblankscreencallback22) | Yes | Callback triggered when the **Web** component detects a blank screen. |

**Example**

// onDetectedBlankScreen.ets
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

#### onRenderExited(deprecated)

onRenderExited(callback: (event?: { detail: object }) => boolean)

Triggered when the rendering process exits due to an error or crash.

A rendering process may be shared by multiple **Web** components. Each affected **Web** component triggers this callback.

You can call the bound **WebViewController** APIs to restore the web page when this callback is triggered. For example, [refresh](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#refresh) and [loadUrl](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md#loadurl).

For details, see [Lifecycle of the Web Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-event-sequence).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/XFJ3I-kHTE-kf14LfI6-lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE006C183CEF7B466474C206B91DF870516F8E849A1A42B704A7EDE50DCFE34E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [onRenderExited9+](#onrenderexited9) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event?: { detail: object }) => boolean | Yes | Callback triggered when the rendering process exits abnormally. |
