# How do I send HTTP requests in JSON format in ArkTS?

In the HTTP message header, **Content-Type** is used to specify the media type.

Set **Content-Type** to **application/json** so that the data in the HTTP request is transmitted in JSON format. The code snippet is as follows:

import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;
  constructor(contentType: string) {
    this.contentType = contentType;
  }
}
let httpRequest = http.createHttp();
let promise = httpRequest.request("EXAMPLE\_URL", {
  method: http.RequestMethod.GET,
  connectTimeout: 60000,
  readTimeout: 60000,
  header: new Header('application/json')
});

**Reference**

[request](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-http#request)
