# How do I use the alert function of H5 in the WebView?

**Reference code**

Use the [onAlert](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onalert) attribute of the **Web** component to monitor the alert dialog box displayed when a web page triggers **alert()**. Then use the [AlertDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-alert-dialog-box) method to implement the effect and logic of the dialog box.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebviewAlert {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('WebviewAlert.html'), controller: this.controller })
        .onAlert((event) => {
          if (event) {
            console.log('event.url:' + event.url);
            console.log('event.message:' + event.message);
            this.getUIContext().showAlertDialog({
              title: 'onAlert',
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

HTML5 side:

<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
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
