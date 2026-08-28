# How do I adapt ArkWeb to multiple devices?

During web page development, use the **@media** query in the CSS, and set different styles based on different screen sizes. You can refer to Responsive Web Design (RWD), such as the percentage unit and viewport unit. In addition, you can use a mature frontend framework, in which components can adapt to multiple devices. For details, please refer to [Responsive Layout on Web](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-web-adaptation).

If the third-party web page has used the UA to adapt to the mobile device but the effect is incorrect on the HarmonyOS device, the possible cause is that the UA of the HarmonyOS device is not adapted. You can use [getUserAgent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#getuseragent) on the ArkTS side to view the UA of a HarmonyOS device for adaptation, or use [setCustomUserAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setcustomuseragent10) to define the UA.

Reference

[Default User-Agent Structure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-default-useragent#default-user-agent-structure)

[setCustomUserAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setcustomuseragent10)
