# What knowledge do I need to know for using HTTP network connections?

You need to declare the **ohos.permission.INTERNET** permission for initiating HTTP requests. For details about the error codes, see [libcurl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

The GET and POST methods are commonly used for HTTP requests. If a request is successful, the returned service data is encapsulated in **data.result** and the cookie information in **data.cookies**. To change the character set, add the following parameter to the request header:

'Content-Type': "application/json; charset=UTF-8"

For a web request, the returned data is sometimes ultra-long text and cannot be completely logged in the **console.log** file.

**Reference**

[@ohos.net.http (Data Request)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-http)
