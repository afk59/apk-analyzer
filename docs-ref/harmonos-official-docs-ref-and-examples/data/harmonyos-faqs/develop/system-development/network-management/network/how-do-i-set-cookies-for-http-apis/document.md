# How do I set cookies for HTTP APIs?

The header in **HttpRequestOptions** is of the object type. You can directly set the cookie in the header. To call **httpRequest.request()**, you need to declare the **ohos.permission.INTERNET** permission. When calling this API, replace **EXAMPLE\_URL** in the API with the actual request address. The sample code is as follows:

import { http } from '@kit.NetworkKit';

@Entry
@Component
struct HttpRequest {
  @State message: string = 'initiates a request';

  request() {
    let httpRequest = http.createHttp();
    let options: http.HttpRequestOptions = {
      method: http.RequestMethod.POST,
      extraData: 'data to send',
      expectDataType: http.HttpDataType.STRING,
      priority: 1,
      header: {
        'cookie': 'key1=value1;key2=value2'
      }
    };
    httpRequest.request("EXAMPLE\_URL", options, (err: Error, data: http.HttpResponse) => {
      if (!err) {
        console.info('Result:' + data.result);
        console.info('code:' + data.responseCode);
        console.info('type:' + JSON.stringify(data.resultType));
        console.info('header:' + JSON.stringify(data.header));
        console.info('cookies:' + data.cookies); // Starting from API version 8, cookies are supported
      } else {
        console.info('error:' + JSON.stringify(err));
      }
    });
  }

  build() {
    Row() {
      Column() {
        Button(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.request();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[@ohos.net.http (Data Request)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-http)
