# How do I write extraData in the HTTP request sample code?

1.  **extraData** is defined as **extraData?: string | Object | ArrayBuffer** in the documentation. That is, **extraData** can be of the string, Object, or ArrayBuffer type.
2.  You can use one of the following methods:
    
    extraData:"data to send";
    extraData:{ data: "data to send", };
    extraData:{ data: new ArrayBuffer(1)};
    

**Reference**

[HttpRequestOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-http#httprequestoptions)
