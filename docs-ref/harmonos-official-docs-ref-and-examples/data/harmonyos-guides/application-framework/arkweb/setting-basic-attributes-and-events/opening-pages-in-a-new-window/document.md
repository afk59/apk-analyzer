# Opening Pages in a New Window

The **Web** component provides the capability of opening pages in a new window. You can call [multiWindowAccess()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#multiwindowaccess9) to specify whether to allow a web page to be opened in a new window. When a new window is opened in the **Web** component, the application will receive a new window event through [onWindowNew()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onwindownew9). You need to create a window for processing the window opening request in the event callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/ZRqVL9y-RJaCghr7MjSw-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7A3CBA5C808CEAC68F52F558F947C6356BA27764C72498701C7AFDA2A763C4D)

-   If [allowWindowOpenMethod()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#allowwindowopenmethod10) is set to **true**, you can open a new window in the frontend page by invoking its JavaScript functions.
    
-   When a web page calls **window.open(url, name)** to open a new window, the ArkWeb kernel checks whether a bound **Web** component exists based on **name**. If yes, the **Web** component will receive a notification from the [onActivateContent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onactivatecontent20) API so that the application can display it in the foreground. If no, the ArkWeb kernel will notify the application of creating a new window through the **onWindowNew()** API.
    
-   If a new window is created in the **onWindowNew()** notification and the parameter of the **ControllerHandler.setWebController()** API is set to the **WebviewController** of the new **Web** component, the ArkWeb kernel will bind the **name** with the new **Web** component.
    
-   If you do not create a window in **onWindowNew()**, set the parameter of the **ControllerHandler.setWebController()** API to null.
    

In the following example, when a user clicks the **Open Page in New Window** button, the application receives a window opening event in the **onWindowNew()** callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/-pZ4hKM4SEGJ40V9nSOpPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D7662DA381119628E4F13B1B86F75691FF6EE7BFC1A16A01EE023E3BE2989A9)

-   When a web page requires the user to create a window, the [OnWindowNewEvent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-i#onwindownewevent12) callback is triggered. In this callback, the value **true** of the **isUserTrigger** parameter indicates that the window is triggered by the user, and **false** indicates the opposite.

-   Application code:
    
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
          Web({ src: $rawfile("window.html"), controller: this.controller })
            .javaScriptAccess(true)
              // Enable the multi-window permission.
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
              // Return the WebviewController object corresponding to the new window to the <Web> kernel.
              // If the event.handler.setWebController API is not called, the render process will be blocked.
              // If no new window is created, set the value of event.handler.setWebController to null to notify the Web component that no new window is created.
              event.handler.setWebController(popController);
            })
        }
      }
    }
    
-   Code of the **window.html** page:
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width"/>
        <title>WindowEvent</title>
    </head>
    <body>
    <input type="button" value="Open Page in New Window" onclick="OpenNewWindow()">
    <script type="text/javascript">
        function OpenNewWindow()
        {
            var txt = 'Opened window';
            let openedWindow = window.open("about:blank", "", "location=no,status=no,scrollbars=no");
            openedWindow.document.write("<p>" + "<br><br>" + txt + "</p>");
            openedWindow.focus();
        }
    </script>
    </body>
    </html>
    

**Figure 1** Effect of opening a page in a new window

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/xH-af9V-QgmcVCN62KxGOg/en-us_image_0000002568764723.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9D8EBD5CDABB3AFDBA0AC586E0091CF279319228F70CAFB70929A9BEDC9BA2C)
