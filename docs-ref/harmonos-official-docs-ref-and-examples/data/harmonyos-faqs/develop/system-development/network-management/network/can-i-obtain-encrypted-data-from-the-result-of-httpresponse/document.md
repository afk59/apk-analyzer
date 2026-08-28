# Can I obtain encrypted data from the result of httpResponse?

You can use HTTP requests to transmit encrypted data and obtain the result.

Response content returned based on \*\*Content-type\*\* in the response header. If **HttpRequestOptions** does not contain the **expectDataType** field, the response content is returned according to the following rules:

-   application/json: string in JSON format
-   application/octet-stream: ArrayBuffer
-   image: ArrayBuffer
-   Others: string

If **HttpRequestOptions** contains the **expectDataType** field, the response content must be of the same type as the data returned by the server.

**Reference**

[request](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-http#request)
