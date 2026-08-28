# How do I add a header to a web request?

Use the **loadUrl** method to set the **headers**. **loadUrl** receives two parameters. **url** indicates the URL to be loaded, and **headers** indicates the additional HTTP request header of the array type.

// With parameter headers
this.controller.loadUrl('www.example.com', \[{ headerKey: "headerKey", headerValue: "headerValue" }\]);

**Reference**

[loadUrl](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl >)

[WebHeader](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-i#webheader >)
