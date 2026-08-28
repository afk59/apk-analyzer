# How do I set multiple cookies in batches?

You can use [configCookieSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookiesync11) and [configCookie](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookie11) provided by [Class (WebCookieManager)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager) to set cookie values synchronously or asynchronously. However, the API does not support setting multiple cookies at a time. You are advised to set multiple cookies by using **configCookie** or **configCookieSync**.

import { webview } from '@kit.ArkWeb';

webview.once("webInited", () => {
  console.info("webInited setCookie");
  webview.WebCookieManager.configCookie("https://www.example.com", 'a=b');
  webview.WebCookieManager.configCookie("https://www.example.com", 'c=d');
  webview.WebCookieManager.configCookie("https://www.example.com", 'e=f');
})

@Entry
@Component
struct LoginCookieConfig {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('fetchCookieSync')
        .onClick(() => {
          try {
            let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
            console.log(\`fetchCookieSync cookie value is: ${value}\`);
          } catch (error) {
            console.error(\`fetchCookieSync failed,error is: ${JSON.stringify(error)}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
