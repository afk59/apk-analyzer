# @ohos.net.http (Data Request)

The **http** module provides APIs for implementing HTTP data request capabilities. An application can initiate a data request over HTTP. Common HTTP methods include **GET**, **POST**, **OPTIONS**, **HEAD**, **PUT**, **DELETE**, **TRACE**, and **CONNECT**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/BONxdQbtSbOe8fbEN0-jxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=930E4D817212BDA3E6587EAC35A2B51CE83B97855DC8BAFB7A08698D4EF9606B)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { http } from '@kit.NetworkKit';

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/bS3qHUjbQvW0z_GN2MU5nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BDB219E586F0A07468CB0709B937E7F1E3012340121DBD6F508AA81DB8BBB65)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// Import the http namespace.
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
// Each httpRequest corresponds to an HTTP request task and cannot be reused.
let httpRequest = http.createHttp();
// This API is used to listen for HTTP Response Header events, which is returned earlier than the result of the HTTP request. It is up to you whether to listen for HTTP response header events.
// on('headerReceive', AsyncCallback) is replaced by on('headersReceive', Callback) since API version 8.
httpRequest.on('headersReceive', (header: Object) => {
  console.info('header: ' + JSON.stringify(header));
});

httpRequest.request(// Customize EXAMPLE\_URL in extraData on your own. It is up to you whether to add parameters to the URL.
  "EXAMPLE\_URL",
  {
    method: http.RequestMethod.POST, // Optional. The default value is http.RequestMethod.GET.
    // This field is used to transfer the request body when a POST request is used. Its format needs to be negotiated with the server.
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // Optional. This parameter specifies the type of the return data.
    usingCache: true, // Optional. The default value is true.
    priority: 1, // Optional. The default value is 1.
    // You can add header fields based on service requirements. Note that map objects cannot be passed to header fields.
    header: { 'Accept' : 'application/json' },
    readTimeout: 60000, // Optional. The default value is 60000, in ms.
    connectTimeout: 60000 // Optional. The default value is 60000, in ms.
    usingProtocol: http.HttpProtocol.HTTP1\_1, // Optional. The default protocol type is automatically specified by the system.
    usingProxy: false, // Optional. By default, network proxy is not used. This field is supported since API version 10.
    caPath: '/path/to/cacert.pem', // Optional. The preset CA certificate is used by default. This field is supported since API version 10.
    caData: '-----BEGIN CERTIFICATE-----\\n' +
        'MIIDaTCCAlGgAwIBAgIICN287lmB2cMwDQYJKoZIhvcNAQELBQAwgYoxCzAJBgNV\\n' +
        'BAYTAkNOMRMwEQYDVQQDDApleGFtcGxlLmNuMRAwDgYDVQQKDAdDb21wYW55MREw\\n' +
        'DwYDVQQLDAhEaXZpc2lvbjEOMAwGA1UECAwFQW5IdWkxDjAMBgNVBAcMBUhlRmVp\\n' +
        'MSEwHwYJKoZIhvcNAQkBFhJleGFtcGxlQGV4YW1wbGUuY24wHhcNMjUwNDEzMDAy\\n' +
        'MjQxWhcNMjgwNDEzMDAyMjQxWjBeMQswCQYDVQQGEwJDTjESMBAGA1UEAwwJMTI3\\n' +
        'LjAuMC4xMQkwBwYDVQQKDAAxCTAHBgNVBAsMADEJMAcGA1UECAwAMQkwBwYDVQQH\\n' +
        'DAAxDzANBgkqhkiG9w0BCQEWADCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC\\n' +
        'ggEBANN/JrQC8dy7sxUk+TDJlGlq4h8lajdqSASkFbWVBadU4eMCbRrKejXuFX/n\\n' +
        'Yu4J3wkgni0NKRejdWu/M+LLibQEIF9RUGNR/OgdlR4AKr8ZxmG44+7Ps2aiDcOy\\n' +
        'Z95UcxYj59ctfFk63cacbBi19aq200spjl/H0jTVsQ2/JvwMVEH62WbyjIJ3KXgq\\n' +
        'yyjf75rKbR9CdVdGk+OoR4S4c6nY5cTZP6T7iCupYR6MpKEtIR2bbams/N5GxQEh\\n' +
        '9+7YxswTQn4EkVhi+UOFZolYLhtIdoLThmStN+WiSL5VDvchAkTUmwUBTGV21WnH\\n' +
        'qo6J1t7XtwUpAZF6OuWl85R8D50CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAqjKq\\n' +
        'gwR+4B6bwdAOZ6k0cutLqxvVgBaktX28omuYtoiYagM0zfB8/8WijXL8jT1VLEFx\\n' +
        'wPaojwegqYWANfQkPd7A6rjsabgOH7oYBCDoCH52cjzGlJunC0BL6w5g3z6MCOB4\\n' +
        'Ciz8rnYMvYqQJiMqrO7Po9onoFBHiRQGO4Wva3O8ErEmd2dKvXb3vN02P3T7CtwM\\n' +
        'Z6D0rtZbzdsSOQfGcX08WFIfvfpz6tdU/X/6VqKrt5oiaNQH7ded6gJ3C6RM/Q/x\\n' +
        'I2j/hSKy0yU7FoCFSOnlhxbm3TlbIvtjZKQ9ymK4x7iE0VKqExUAA6Z8qsIUBUt4\\n' +
        'aqNDeZWXFBqrSujLJA==\\n' +
        '-----END CERTIFICATE-----', // Optional. The preset CA certificate is used by default. This field is supported since API version 20.
    clientCert: { // Optional. The client certificate is not used by default. This field is supported since API version 11.
      certPath: '/path/to/client.pem', // The client certificate is not used by default. This field is supported since API version 11.
      keyPath: '/path/to/client.key', // If the certificate contains key information, an empty string is passed. This field is supported since API version 11.
      certType: http.CertType.PEM, // Certificate type, optional. A certificate in the PEM format is used by default. This field is supported since API version 11.
      keyPassword: "passwordToKey" // Password of the key file, optional. It is supported since API version 11.
    },
    certificatePinning: \[ // Optional. It determines whether to enable dynamic configuration of certificate pinning. This attribute is supported since API version 12.
      {
        publicKeyHash: 'Pin1', // Certificate PIN passed by the application. This attribute is supported since API version 12.
        hashAlgorithm: 'SHA-256' // Encryption algorithm. Currently, it can only be set to SHA-256. This attribute is supported since API version 12.
      }, {
        publicKeyHash: 'Pin2', // Certificate PIN passed by the application. This attribute is supported since API version 12.
        hashAlgorithm: 'SHA-256' // Encryption algorithm. Currently, it can only be set to SHA-256. This attribute is supported since API version 12.
      }
    \],
    multiFormDataList: \[ // Optional. This field is valid only when content-Type in the header is multipart/form-data. It is supported since API version 11.
      {
        name: "Part1", // Data name. This field is supported since API version 11.
        contentType: 'text/plain', // Data type. This field is supported since API version 11.
        data: 'Example data', // Data content, optional. This field is supported since API version 11.
        remoteFileName: 'example.txt' // Optional. This field is supported since API version 11.
      }, {
        name: "Part2", // Data name. This field is supported since API version 11.
        contentType: 'text/plain', // Data type. This field is supported since API version 11.
        // data/app/el2/100/base/com.example.myapplication/haps/entry/files/fileName.txt
        filePath: \`${context.filesDir}/fileName.txt\`, // File path, optional. This field is supported since API version 11.
        remoteFileName: 'fileName.txt' // Optional. This field is supported since API version 11.
      }
    \],
    addressFamily: http.AddressFamily.DEFAULT // Optional. By default, the IPv4 or IPv6 address of the target domain name is selected. This attribute is supported since API version 15.
  },
  (err: BusinessError, data: http.HttpResponse) => {
    if (!err) {
      // data.result carries the HTTP response. Parse the response based on service requirements.
      console.info('Result:' + JSON.stringify(data.result));
      console.info('code:' + JSON.stringify(data.responseCode));
      console.info('type:' + JSON.stringify(data.resultType));
      // data.header carries the HTTP response header. Parse the content based on service requirements.
      console.info('header:' + JSON.stringify(data.header));
      console.info('cookies:' + JSON.stringify(data.cookies)); // Cookies are supported since API version 8.
      // Unsubscribe from HTTP Response Header events.
      httpRequest.off('headersReceive');
      // Call destroy() to release resources when the request is no longer needed, preventing memory leaks.
      httpRequest.destroy();
    } else {
      console.error('error:' + JSON.stringify(err));
      // Unsubscribe from HTTP Response Header events.
      httpRequest.off('headersReceive');
      // Call destroy() to release resources when the request is no longer needed, preventing memory leaks.
      httpRequest.destroy();
    }
  });

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/AWlsJR_KS6ePQeudebvGjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=028E8BFEEFE4C75F663FC6F351CDBD8E5A435E2D96B2025E5B169E74AFBCAB76)

If the data in **console.info()** contains a newline character, the data will be truncated.

HTTP responses compressed by the brotli algorithm are supported since API version 12.

#### http.createHttp

createHttp(): HttpRequest

Creates an HTTP request. You can use this API to initiate or destroy an HTTP request, or enable or disable listening for HTTP Response Header events. To initiate multiple HTTP requests, you must create an **HttpRequest** object for each HTTP request. An **HttpRequest** object corresponds to an HTTP request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/MoJhn1cQRMeGKruC9X9xtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C210554FF825B9CB87A46E4107D65A1E378B4FF12E0FA20690062EE02F53730)

When the request is no longer needed, call destroy() to release resources. Otherwise, memory leakage may occur.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| HttpRequest | An **HttpRequest** object, which contains the **request**, **requestInStream**, **destroy**, **on**, or **off** method. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();

#### HttpRequest

Defines an HTTP request task. Before invoking APIs provided by **HttpRequest**, you must call [createHttp()](#httpcreatehttp) to create an **HttpRequestTask** object.

#### \[h2\]request

request(url: string, callback: AsyncCallback<HttpResponse>): void

Initiates an HTTP request to a given URL. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/FTGcLJEvR-CPUua1cxroVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=329612373D1B4CD0E8A47C2CF180EEBF4315E25FD125D663F434747F4D0F81A3)

(1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set **maxLimit** to a larger value in [HttpRequestOptions](#httprequestoptions) or call [requestInStream](#requestinstream10) to initiate a streaming request.

(2) If you need to pass in cookies, add them to the **options** parameter.

(3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an HTTP request.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for initiating an HTTP request. |
| callback | AsyncCallback<[HttpResponse](#httpresponse)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE\_URL", (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});

#### \[h2\]request

request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>):void

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/9wLzsua-QkaLQGSzp2fViA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B455839109D80FB363893F8B078802AB513587DECF5AB96286CEB28AC23E2AA)

(1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set **maxLimit** to a larger value in [HttpRequestOptions](#httprequestoptions) or call [requestInStream](#requestinstream10) to initiate a streaming request.

(2) If you need to pass in cookies, add them to the **options** parameter.

(3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an HTTP request.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | HttpRequestOptions | Yes | Request options. For details, see [HttpRequestOptions](#httprequestoptions). |
| callback | AsyncCallback<[HttpResponse](#httpresponse)\> | Yes | Callback used to return the result. If the operation is successful, the callback content is an [HttpResponse](#httpresponse) object; otherwise, the callback content is undefined. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**Example**

import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
    method: http.RequestMethod.POST, // Optional. The default value is http.RequestMethod.GET.
    // This field is used to transfer the request body when a POST request is used. Its format needs to be negotiated with the server.
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // Optional. This parameter specifies the type of the return data.
    usingCache: true, // Optional. The default value is true.
    priority: 1, // Optional. The default value is 1.
    // You can add header fields based on service requirements.
    header: new Header('application/json'),
    readTimeout: 60000, // Optional. The default value is 60000, in ms.
    connectTimeout: 60000 // Optional. The default value is 60000, in ms.
    usingProtocol: http.HttpProtocol.HTTP1\_1, // Optional. The default protocol type is automatically specified by the system.
    usingProxy: false, // Optional. By default, network proxy is not used. This field is supported since API version 10.
};

httpRequest.request("EXAMPLE\_URL", options, (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  } else {
    console.error('error:' + JSON.stringify(err));
  }
});

#### \[h2\]request

request(url: string, options? : HttpRequestOptions): Promise<HttpResponse>

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/li3vn--YQ7ecwERpviazDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BF2F46C16594C54BA9A25F3FCCA2631D81BBDA3E8C4EEF8D6816AA984EB4AC7)

(1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set **maxLimit** to a larger value in [HttpRequestOptions](#httprequestoptions) or call [requestInStream](#requestinstream10) to initiate a streaming request.

(2) If you need to pass in cookies, add them to the **options** parameter.

(3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an HTTP request.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | HttpRequestOptions | No | Request options. For details, see [HttpRequestOptions](#httprequestoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[HttpResponse](#httpresponse)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**Example**

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
promise.then((data:http.HttpResponse) => {
  console.info('Result:' + data.result);
  console.info('code:' + data.responseCode);
  console.info('type:' + JSON.stringify(data.resultType));
  console.info('header:' + JSON.stringify(data.header));
  console.info('cookies:' + data.cookies); // Cookies are supported since API version 8.
  console.info('header.content-Type:' + data.header);
  console.info('header.Status-Line:' + data.header);
}).catch((err:Error) => {
  console.error('error:' + JSON.stringify(err));
});

#### \[h2\]destroy

destroy(): void

Stops an HTTP request task and releases system resources.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Example**

import { http } from '@kit.NetworkKit';
let httpRequest = http.createHttp();

httpRequest.destroy();

#### \[h2\]requestInStream10+

requestInStream(url: string, callback: AsyncCallback<number>): void

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for initiating an HTTP request. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the request is successful, **err** is **undefined**, and the HTTP result code is returned. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**Example**

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.requestInStream("EXAMPLE\_URL", (err: BusinessError, data: number) => {
  if (!err) {
    console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
  } else {
    console.error("requestInStream ERROR : err = " + JSON.stringify(err));
  }
})

#### \[h2\]requestInStream10+

requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void

Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to return the result, which is a streaming response.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | HttpRequestOptions | Yes | Request options. For details, see [HttpRequestOptions](#httprequestoptions). |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the request is successful, **err** is **undefined**, and the [HTTP result code](#responsecode) is returned. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**Example**

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
    method: http.RequestMethod.POST, // Optional. The default value is http.RequestMethod.GET.
    // This field is used to transfer the request body when a POST request is used. Its format needs to be negotiated with the server.
    extraData: 'data to send',
    expectDataType: http.HttpDataType.STRING, // Optional. This parameter specifies the type of the return data.
    usingCache: true, // Optional. The default value is true.
    priority: 1, // Optional. The default value is 1.
    // You can add header fields based on service requirements.
    header: new Header('application/json'),
    readTimeout: 60000, // Optional. The default value is 60000, in ms.
    connectTimeout: 60000 // Optional. The default value is 60000, in ms.
    usingProtocol: http.HttpProtocol.HTTP1\_1, // Optional. The default protocol type is automatically specified by the system.
    usingProxy: false, // Optional. By default, network proxy is not used. This field is supported since API version 10.
};
httpRequest.requestInStream("EXAMPLE\_URL", options, (err: BusinessError<void> , data: number) => {
  if (!err) {
    console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
  } else {
    console.error("requestInStream ERROR : err = " + JSON.stringify(err));
  }
})

#### \[h2\]requestInStream10+

requestInStream(url: string, options? : HttpRequestOptions): Promise<number>

Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the result, which is a streaming response.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for initiating an HTTP request. |
| options | HttpRequestOptions | No | Request options. For details, see [HttpRequestOptions](#httprequestoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the [result](#responsecode). |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**Example**

import { http } from '@kit.NetworkKit';

class Header {
  public contentType: string;

  constructor(contentType: string) {
    this.contentType = contentType;
  }
}

let httpRequest = http.createHttp();
let promise = httpRequest.requestInStream("EXAMPLE\_URL", {
  method: http.RequestMethod.GET,
  connectTimeout: 60000,
  readTimeout: 60000,
  header: new Header('application/json')
});
promise.then((data: number) => {
  console.info("requestInStream OK!" + data);
}).catch((err: Error) => {
  console.error("requestInStream ERROR : err = " + JSON.stringify(err));
});

#### \[h2\]on("headerReceive")(deprecated)

on(type: "headerReceive", callback: AsyncCallback<Object>): void

Registers an observer for HTTP Response Header events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/hbY7IzrsSu-Ei3io739Nzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC30E80AD66B4A92C448C0E2ACA7AFAE33CEBD761E97CA16F7B218AA0AC84554)

This API is supported since API version 6 and deprecated since API version 8. You are advised to use [on("headersReceive")](#onheadersreceive8) instead.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **headerReceive**. |
| callback | AsyncCallback<Object> | Yes | Callback used to return the result. If the operation is successful, **error** is **undefined**, and **data** is the received HTTP response header. Otherwise, **error** is an error object. |

**Example**

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.on("headerReceive", (data: BusinessError) => {
  console.error("error:" + JSON.stringify(data));
});

#### \[h2\]off("headerReceive")(deprecated)

off(type: "headerReceive", callback?: AsyncCallback<Object>): void

Unregisters the observer for HTTP Response Header events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ciP-61OtQDSxAyGzF76MRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D959C8CDFDFCE4A224859C0C48802F615C5CEF149BB499D162F9C23F3F63CDBF)

This API is supported since API version 6 and deprecated since API version 8. You are advised to use [off("headersReceive")](#offheadersreceive8) instead.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **headerReceive**. |
| callback | AsyncCallback<Object> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.off("headerReceive");

#### \[h2\]on("headersReceive")8+

on(type: "headersReceive", callback: Callback<Object>): void

Registers an observer for HTTP Response Header events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **headersReceive**. |
| callback | Callback<Object> | Yes | Callback used to return the HTTP response header. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");

#### \[h2\]off("headersReceive")8+

off(type: "headersReceive", callback?: Callback<Object>): void

Unregisters the observer for HTTP Response Header events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **headersReceive**. |
| callback | Callback<Object> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});
httpRequest.off("headersReceive");

#### \[h2\]once("headersReceive")8+

once(type: "headersReceive", callback: Callback<Object>): void

Registers a one-time observer for HTTP Response Header events. Once triggered, the observer will be removed. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **headersReceive**. |
| callback | Callback<Object> | Yes | Callback used to return the HTTP response header. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.once("headersReceive", (header: Object) => {
  console.info("header: " + JSON.stringify(header));
});

#### \[h2\]on("dataReceive")10+

on(type: "dataReceive", callback: Callback<ArrayBuffer>): void

Registers an observer for events indicating receiving of HTTP streaming responses.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataReceive**. |
| callback | Callback<ArrayBuffer> | Yes | Callback used to return the result. If the operation is successful, **error** is **undefined**, and **data** is the received HTTP streaming data of the ArrayBuffer type. Otherwise, **error** is an error object. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");

#### \[h2\]off("dataReceive")10+

off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void

Unregisters the observer for events indicating receiving of HTTP streaming responses.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataReceive**. |
| callback | Callback<ArrayBuffer> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  console.info("dataReceive length: " + JSON.stringify(data.byteLength));
});
httpRequest.off("dataReceive");

#### \[h2\]on("dataEnd")10+

on(type: "dataEnd", callback: Callback<void>): void

Registers an observer for events indicating completion of receiving HTTP streaming responses.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataEnd**. |
| callback | Callback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an **Error** object. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");

#### \[h2\]off("dataEnd")10+

off(type: "dataEnd", callback?: Callback<void>): void

Unregisters the observer for events indicating completion of receiving HTTP streaming responses.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataEnd**. |
| callback | Callback<void> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
});
httpRequest.off("dataEnd");

#### \[h2\]on('dataReceiveProgress')10+

on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void

Registers an observer for events indicating progress of receiving HTTP streaming responses.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataReceiveProgress**. |
| callback | Callback<[DataReceiveProgressInfo](#datareceiveprogressinfo11)\> | Yes | Callback used to return the result. If the operation is successful, the callback content is a [DataReceiveProgressInfo](#datareceiveprogressinfo11) object; otherwise, the callback content is **undefined**. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");

#### \[h2\]off('dataReceiveProgress')10+

off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void

Unregisters the observer for events indicating progress of receiving HTTP streaming responses.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataReceiveProgress**. |
| callback | Callback<[DataReceiveProgressInfo](#datareceiveprogressinfo11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
  console.info("dataReceiveProgress:" + JSON.stringify(data));
});
httpRequest.off("dataReceiveProgress");

#### \[h2\]on('dataSendProgress')11+

on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void

Registers an observer for events indicating progress of sending HTTP requests.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataSendProgress**. |
| callback | Callback<[DataSendProgressInfo](#datasendprogressinfo11)\> | Yes | Callback used to return the result. If the operation is successful, the callback content is a [DataSendProgressInfo](#datasendprogressinfo11) object; otherwise, the callback content is **undefined**. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");

#### \[h2\]off('dataSendProgress')11+

off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void

Unregisters the observer for events indicating progress of sending HTTP requests.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **dataSendProgress**. |
| callback | Callback<[DataSendProgressInfo](#datasendprogressinfo11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
  console.info("dataSendProgress:" + JSON.stringify(data));
});
httpRequest.off("dataSendProgress");

#### HttpRequestOptions

Defines the options for initiating an HTTP request.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| method | [RequestMethod](#requestmethod) | No | Yes | 
Request method. The default value is **GET**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| extraData | string | Object | ArrayBuffer | No | Yes | 

Additional data for sending a request. This parameter is not used by default.

**Note**: Do not add this parameter if no extra data is available. If this parameter must be added, set it to **undefined** or **null**. Do not pass the parameter as "".

\- If the HTTP request uses a POST, PUT, or DELETE method, this field serves as the content of the HTTP request and is encoded in UTF-8 format.

Example:

(1) If **content-Type** is **application/x-www-form-urlencoded**, the data in the request body must be encoded in the format of **key1=value1&key2=value2&key3=value3** after URL transcoding (**encodeURIComponent/encodeURI**) and this field is usually in the String format.

(2) If **content-Type** is **text/xml**, this field is usually in the String format.

(3) If **content-Type** is **application/json**, this field is usually in the Object format.

(4) If **content-Type** is **application/octet-stream**, this field is usually in the ArrayBuffer format.

(5) If **content-Type** is **multipart/form-data** and the content to be uploaded is a file, this field is usually in the ArrayBuffer format.

The preceding information is for reference only and may vary according to the actual situation.

\- If the HTTP request uses the GET, OPTIONS, TRACE, or CONNECT method, this parameter serves as a supplement to HTTP request parameters. Parameters of the string type need to be encoded before being passed to the HTTP request. Parameters of the object type do not need to be precoded and will be directly concatenated to the URL. Parameters of the ArrayBuffer type will not be concatenated to the URL.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| expectDataType9+ | [HttpDataType](#httpdatatype9) | No | Yes | 

Type of the returned data. This parameter is not used by default. If this parameter is set, the system returns the specified type of data preferentially. If the specified type is **Object**, the value can contain a maximum of 65536 characters.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| usingCache9+ | boolean | No | Yes | 

Whether to use the cache. The value **true** indicates that the cache is preferentially read when a request is initiated, and the value **false** indicates that the cache is not used. The default value is **true**. The cache function takes effect when the process is started. The new cached data will replace the existing cached data.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| priority9+ | number | No | Yes | 

Priority of concurrent HTTP/HTTPS requests. A larger value indicates a higher priority. The value range is \[1, 1000\]. The default value is **1**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| header | Object | No | Yes | 

HTTP request header. If the request method is POST, PUT, DELETE, or null, the default value is {'content-Type': 'application/json'}. Otherwise, the default value is {'content-Type': 'application/x-www-form-urlencoded'}.

If the header contains fields of numeric type, the maximum value must be an int64 integer.

The header field supports the JSON format (as shown in [Example](#example)) and the Record<string, string> format.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| readTimeout | number | No | Yes | 

Read timeout duration. The default value is **60000**, in ms. The input value must be an uint32\_t integer.

The value **0** indicates no timeout.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| connectTimeout | number | No | Yes | 

Connection timeout interval. The default value is **60000**, in ms. The input value must be an uint32\_t integer.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| usingProtocol9+ | [HttpProtocol](#httpprotocol9) | No | Yes | 

Protocol. The default value is automatically specified by the system.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| usingProxy10+ | boolean | [HttpProxy](../ohos-net-connection-network-connection-management/document.md#httpproxy10) | No | Yes | 

HTTP proxy configuration. If this item is not configured, the system proxy is used by default.

\- If **usingProxy** is set to **true**, the default network proxy is used. If **usingProxy** is set to **false**, no proxy is used.

\- If **usingProxy** is of the **HttpProxy** type, the specified network proxy is used. The HttpProxy supports the **username** and **password** fields from API version 22.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| caPath10+ | string | No | Yes | 

CA certificate data. If this parameter is set and the certificate is valid, the system uses the specified CA certificate and the preset CA certificate. Otherwise, the system uses only the preset CA certificate. The CA certificate path is the sandbox mapping path, which can be obtained by using **UIAbilityContext** APIs. Currently, only **.pem** certificates are supported.

The preset CA certificate is available at **/etc/ssl/certs/cacert.pem**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| caData20+ | string | No | Yes | 

CA certificate data. If this parameter is set and the certificate is valid, the system uses the specified CA certificate and the preset CA certificate. Otherwise, the system uses only the preset CA certificate. If both **caPath** and **caData** are set, **caData** is ignored by the system. Currently, only certificates in **.pem** format are supported. The maximum length is 8000 bytes. Only one certificate can be specified. A certificate chain is not allowed.

The preset CA certificate is available at **/etc/ssl/certs/cacert.pem**. This path is the sandbox mapping path, which can be obtained by using **UIAbilityContext** APIs.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| resumeFrom11+ | number | No | Yes | 

Download start position. This field can be used only for the GET method. As stipulated in section 3.1 of RFC 7233, servers are allowed to ignore range requests.

\- If the HTTP PUT method is used, do not use this option because it may conflict with other options.

\- The value ranges from **1** to **4294967296** (4 GB). If the value is out of this range, this field does not take effect.

 |
| resumeTo11+ | number | No | Yes | 

Download end position. This field can be used only for the GET method. As stipulated in section 3.1 of RFC 7233, servers are allowed to ignore range requests.

\- If the HTTP PUT method is used, do not use this option because it may conflict with other options.

\- The value ranges from **1** to **4294967296** (4 GB). If the value is out of this range, this field does not take effect.

 |
| clientCert11+ | [ClientCert](#clientcert11) | No | Yes | Client certificate. |
| dnsOverHttps11+ | string | No | Yes | 

Whether to use an HTTPS server for DNS resolution.

\- The value must be URL-encoded in the following format: "https:// host:port/path".

 |
| dnsServers11+ | Array<string> | No | Yes | 

Array of DNS servers used for DNS resolution.

\- A maximum of three DNS servers can be set. If there are more than three DNS servers, only the first three DNS servers are used.

\- The DNS servers must be expressed as IPv4 or IPv6 addresses.

 |
| maxLimit11+ | number | No | Yes | 

Maximum number of bytes in a response.

The default value is 5\*1024\*1024, in bytes. The maximum value is **100\*1024\*1024**.

 |
| multiFormDataList11+ | Array<[MultiFormData](#multiformdata11)\> | No | Yes | Form data list. This field is valid when **content-Type** is set to **multipart/form-data**. |
| certificatePinning12+ | [CertificatePinning](#certificatepinning12) | CertificatePinning\[\] | No | Yes | Dynamic configuration of certificate pinning. One or more certificate PINs can be specified. |
| addressFamily15+ | [AddressFamily](#addressfamily15) | No | Yes | IP address family. You can specify an address type for domain name resolution. |
| remoteValidation18+ | [RemoteValidation](#remotevalidation18) | No | Yes | 

Certificate authority (CA), which is used to verify the identity of a remote server. If the parameter is not set, the default value is used. The options are as follows:

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| tlsOptions18+ | [TlsOptions](#tlsoptions18) | No | Yes | 

TLS configuration.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| serverAuthentication18+ | [ServerAuthentication](#serverauthentication18) | No | Yes | 

Whether to verify the server identity during a secure connection. The identity is not verified by default.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| sslType20+ | [SslType](#ssltype20) | No | Yes | 

Security communication protocol. You can use TLS (default) or TLCP. If TLCP is used, the related options (such as **caPath**, **clientCert**, and **clientEncCert**) must be set to valid values.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| clientEncCert20+ | [ClientCert](#clientcert11) | No | Yes | 

Client certificate, which is used by the server to verify the client identity.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### RequestMethod

Defines an HTTP request method.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| OPTIONS | "OPTIONS" | Describes the communication options of the target resource. |
| GET | "GET" | Requests the representation of the specified resource. The GET request should only retrieve data and should not contain the request content. |
| HEAD | "HEAD" | Requests the same response (but does not have a response body) as the GET request. |
| POST | "POST" | Submits an entity to a specified resource, which usually causes a status change on the server. |
| PUT | "PUT" | Replaces all current representations of the target resource with the requested content. |
| DELETE | "DELETE" | Deletes the specified resource. |
| TRACE | "TRACE" | Performs a message loopback test along the path to the target resource. |
| CONNECT | "CONNECT" | Establishes a tunnel to the server identified by the target resource. |

#### ResponseCode

Enumerates the response codes for an HTTP request.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| OK | 200 | 
The request is successful. This return code is generally used for GET and POST requests.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CREATED | 201 | 

"Created." The request has been successfully sent and a new resource is created.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ACCEPTED | 202 | 

"Accepted." The request has been accepted for processing, but the processing has not been completed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NOT\_AUTHORITATIVE | 203 | 

"Non-Authoritative Information." The request is successful.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NO\_CONTENT | 204 | 

"No Content." The server has successfully fulfilled the request but there is no additional content to send in the response payload body.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| RESET | 205 | 

"Reset Content." The server has successfully fulfilled the request and desires that the user agent reset the content.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PARTIAL | 206 | 

"Partial Content." The server has successfully fulfilled the partial GET request for a given resource.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MULT\_CHOICE | 300 | 

"Multiple Choices." The requested resource corresponds to any one of a set of representations.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MOVED\_PERM | 301 | 

"Moved Permanently." The requested resource has been assigned a new permanent URI and any future references to this resource will be redirected to this URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MOVED\_TEMP | 302 | 

"Moved Temporarily." The requested resource is moved temporarily to a different URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SEE\_OTHER | 303 | 

"See Other." The response to the request can be found under a different URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NOT\_MODIFIED | 304 | 

"Not Modified." The client has performed a conditional GET request and access is allowed, but the content has not been modified.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| USE\_PROXY | 305 | 

"Use Proxy." The requested resource can only be accessed through the proxy.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BAD\_REQUEST | 400 | 

"Bad Request." The request could not be understood by the server due to incorrect syntax.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| UNAUTHORIZED | 401 | 

"Unauthorized." The request requires user authentication.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PAYMENT\_REQUIRED | 402 | 

"Payment Required." This code is reserved for future use.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FORBIDDEN | 403 | 

"Forbidden." The server understands the request but refuses to process it.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NOT\_FOUND | 404 | 

"Not Found." The server does not find anything matching the Request-URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BAD\_METHOD | 405 | 

"Method Not Allowed." The method specified in the request is not allowed for the resource identified by the Request-URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NOT\_ACCEPTABLE | 406 | 

"Not Acceptable." The server cannot fulfill the request according to the content characteristics of the request.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PROXY\_AUTH | 407 | 

"Proxy Authentication Required." The request requires user authentication with the proxy.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CLIENT\_TIMEOUT | 408 | 

"Request Timeout." The client fails to generate a request within the timeout period.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CONFLICT | 409 | 

"Conflict." The request cannot be fulfilled due to a conflict with the current state of the resource. Conflicts are most likely to occur in response to a PUT request.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GONE | 410 | 

"Gone." The requested resource has been deleted permanently and is no longer available.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LENGTH\_REQUIRED | 411 | 

"Length Required." The server refuses to process the request without a defined Content-Length.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PRECON\_FAILED | 412 | 

"Precondition Failed." The precondition in the request is incorrect.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ENTITY\_TOO\_LARGE | 413 | 

"Request Entity Too Large." The server refuses to process a request because the request entity is larger than the server is able to process.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| REQ\_TOO\_LONG | 414 | 

"Request-URI Too Long." The Request-URI is too long for the server to process.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| UNSUPPORTED\_TYPE | 415 | 

"Unsupported Media Type." The server is unable to process the media format in the request.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| RANGE\_NOT\_SATISFIABLE12+ | 416 | 

"Range Not Satisfiable." The server cannot serve the requested ranges.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INTERNAL\_ERROR | 500 | 

"Internal Server Error." The server encounters an unexpected error that prevents it from fulfilling the request.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NOT\_IMPLEMENTED | 501 | 

"Not Implemented." The server does not support the function required to fulfill the request.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BAD\_GATEWAY | 502 | 

"Bad Gateway." The server acting as a gateway or proxy receives an invalid response from the upstream server.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| UNAVAILABLE | 503 | 

"Service Unavailable." The server is currently unable to process the request due to a temporary overload or system maintenance.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GATEWAY\_TIMEOUT | 504 | 

"Gateway Timeout." The server acting as a gateway or proxy does not receive requests from the remote server within the timeout period.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| VERSION | 505 | 

The server does not support the HTTP protocol version used in the client request.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### HttpResponse

Defines the response to an HTTP request.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| result | string | Object | ArrayBuffer | No | No | 
Response content returned based on **Content-type** in the response header. If **HttpRequestOptions** does not contain the **expectDataType** field, the response content is returned according to the following rules:

\- application/json: string in JSON format

\- application/octet-stream: ArrayBuffer

\- image: ArrayBuffer

\- Others: string

If **HttpRequestOptions** contains the **expectDataType** field, the response content must be of the same type as the data returned by the server.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| resultType9+ | [HttpDataType](#httpdatatype9) | No | No | 

Type of the return value.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| responseCode | [ResponseCode](#responsecode) | number | No | No | 

Result code for an HTTP request. If the callback function is successfully executed, a result code defined in [ResponseCode](#responsecode) will be returned. Otherwise, an error code will be returned in the **err** field in **AsyncCallback**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| header | Object | No | No | 

Response header. The return value is a string in JSON format. If you want to use specific content in the response, you need to implement parsing of that content. Common fields and parsing methods are as follows:

\- content-type: header\['content-type'\]

\- status-line: header\['status-line'\]

\- date: header.date/header\['date'\]

\- server: header.server/header\['server'\]

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| cookies8+ | string | No | No | 

Original cookies returned by the server. How to process the cookies is up to your decision.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| performanceTiming11+ | [PerformanceTiming](#performancetiming11) | No | No | Time consumed in each phase of an HTTP request. |

#### ClientCert11+

Defines the client certificate type.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| certPath | string | No | No | Path of the certificate file. |
| certType | [CertType](#certtype11) | No | Yes | Certificate type. The default value is **PEM**. |
| keyPath | string | No | No | Path of the certificate key file. |
| keyPassword | string | No | Yes | Password of the certificate key file. The default value is an empty string. |

#### PerformanceTiming11+

Configures the timing for performance tracing, in ms.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dnsTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the DNS resolution is complete. |
| tcpTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the TCP connection is complete. |
| tlsTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the TLS connection is complete. |
| firstSendTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the first byte is sent. |
| firstReceiveTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the first byte is received. |
| totalFinishTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the request is complete. |
| redirectTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when all redirection steps are complete. |
| responseHeaderTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the header resolution is complete. |
| responseBodyTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when the body resolution is complete. |
| totalTiming | number | No | No | Duration from the time when the [request](#request) is sent to the time when a callback is returned to the application. |

#### DataReceiveProgressInfo11+

Defines the data receiving progress information.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| receiveSize | number | No | No | Amount of data that has been received, in bytes. |
| totalSize | number | No | No | Amount of data to be received, in bytes. |

#### DataSendProgressInfo11+

Defines the data sending progress information.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetStack

## Attributes

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sendSize | number | No | No | Amount of data to be sent each time, in bytes. |
| totalSize | number | No | No | Amount of data to be sent, in bytes. |

#### MultiFormData11+

Defines the type of multi-form data.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Data name. |
| contentType | string | No | No | Data type, for example, **text/plain**, **image/png**, **image/jpeg**, **audio/mpeg**, or **video/mp4**. |
| remoteFileName | string | No | Yes | 
Name of the file uploaded to the server.

**Note**: If this field is specified, the **filename** field is added to the request header, indicating the name of the file uploaded to the server.

(1) If the data to be uploaded is a file and the file content is specified via the **data** field, the **remoteFileName** field usually needs to be set to specify the name of the file to be uploaded to the server (the actual result depends on the server). If the file path is specified via the **filePath** field, the **filename** field will be automatically added to the request header. Its default value is the file name in the **filePath** field. If a different name is required, it can also be changed via this field.

(2) When the data to be uploaded is in binary format, the **remoteFileName** field must be set.

 |
| data | string | Object | ArrayBuffer | No | Yes | Form data content. |
| filePath | string | No | Yes | 

File path of the form data. If **data** is not specified, **filePath** must be set.

**Note**: The file format supported by the file management module must be passed. You can call [access](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsaccess) to check whether the file exists and is accessible.

 |

#### http.createHttpResponseCache9+

createHttpResponseCache(cacheSize?: number): HttpResponseCache

Creates an **HttpResponseCache** object that stores the response data of HTTP requests. You can call [flush](#flush9) and [delete](#delete9) in the object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cacheSize | number | No | Cache size. The maximum value is 10\*1024\*1024 (10 MB). The maximum value is used by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| [HttpResponseCache](#httpresponsecache9) | Object that stores the response to the HTTP request. |

**Example**

import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();

#### HttpResponseCache9+

Defines an object that stores the response to an HTTP request. Before invoking APIs provided by **HttpResponseCache**, you must call [createHttpResponseCache()](#httpcreatehttpresponsecache9) to create an **HttpRequestTask** object.

**Usage of Keywords in the Response Header**

-   **Cache-Control**: specifies the cache policy, for example, no-cache, no-store, max-age, public, or private.
    
-   **Expires**: specifies the expiration time of a resource. The value is in the GMT format.
    
-   **ETag**: identifies the resource version. The client can use the If-None-Match request header to check whether the resource has been modified.
    
-   **Last-Modified**: specifies the last modification time of a resource. The client can use the If-Modified-Since request header to check whether a resource has been modified.
    
-   **Vary**: specifies the parts of the request header that affect the cached response. This field is used to distinguish different cache versions.
    

When using these keywords, ensure that the response header is correctly configured on the server. The client determines whether to use the cached resource and how to verify whether the resource is the latest based on the response header. Correct cache policies help to improve application performance and user experience.

**How to Set the Cache-Control Header**

Cache-Control is a common header, but it is usually used on the server. It allows you to define when, how, and how long a response should be cached. The following are some common Cache-Control directives:

-   **no-cache**: indicates that the response can be stored in the cache, but it must be verified with the origin server before each reuse. If the resource remains unchanged, the response status code is 304 (Not Modified). In this case, the resource content is not sent, and the resource in the cache is used. If the resource has expired, the response status code is 200 and the resource content is sent.
    
-   no-store: indicates that resources cannot be cached. Resources must be obtained from the server for each request.
    
-   max-age: specifies the maximum cache duration, in seconds. For example, Cache-Control: max-age=3600 indicates that the valid cache duration is 3,600 seconds (that is, 1 hour).
    
-   public: indicates that the response can be cached by any object, for example, the client that sends the request or the proxy server.
    
-   private: indicates that the response can be cached only by a single user and cannot be used as a shared cache (that is, the response cannot be cached by the proxy server).
    
-   must-revalidate: indicates that a resource must be revalidated with the origin server once it has become stable.
    
-   **no-transform**: indicates that the proxy server is not allowed to modify the response content.
    
-   **proxy-revalidate**: works in a way similar to must-revalidate, but applies only to shared caches.
    
-   **s-maxage**: works in a way similar to max-age, but applies only to shared caches.
    

#### \[h2\]flush9+

flush(callback: AsyncCallback<void>): void

Flushes data in the cache to the file system so that the cached data can be accessed in the next HTTP request. This API uses an asynchronous callback to return the result. Cached data includes the response header (header), response body (result), cookies, request time (requestTime), and response time (responseTime).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpResponseCache = http.createHttpResponseCache();
let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE\_URL", (err: BusinessError, data: http.HttpResponse) => {
  if (!err) {
    httpResponseCache.flush((err: BusinessError) => {
      if (err) {
        console.error('flush fail');
      }
      console.info('flush success');
    });
    httpRequest.destroy();
  } else {
    console.error('error:' + JSON.stringify(err));
    // Call destroy() to release resources when the request is no longer needed, preventing memory leaks.
    httpRequest.destroy();
  }
});

#### \[h2\]flush9+

flush(): Promise<void>

Flushes data in the cache to the file system so that the cached data can be accessed in the next HTTP request. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
let httpResponseCache = http.createHttpResponseCache();
let promise = httpRequest.request("EXAMPLE\_URL");

promise.then((data: http.HttpResponse) => {
  httpResponseCache.flush().then(() => {
    console.error('flush success');
  }).catch((err: BusinessError) => {
    console.error('flush fail');
  });
}).catch((err: Error) => {
  console.error('error:' + JSON.stringify(err));
});

#### \[h2\]delete9+

delete(callback: AsyncCallback<void>): void

Disables the cache and deletes the data in it. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE\_URL").then(data => {
  const httpResponseCache = http.createHttpResponseCache();
  httpResponseCache.delete((err: BusinessError) => {
    try {
      if (err) {
        console.error('fail: ' + err);
      } else {
        console.info('success');
      }
    } catch (err) {
      console.error('error: ' + err);
    }
  });
  httpRequest.destroy();
}).catch((error: BusinessError) => {
  console.error("errcode" + JSON.stringify(error));
});

#### \[h2\]delete9+

delete(): Promise<void>

Disables the cache and deletes the data in it. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE\_URL").then(data => {
  const httpResponseCache = http.createHttpResponseCache();
  httpResponseCache.delete().then(() => {
    console.info("success");
  }).catch((err: BusinessError) => {
    console.error("fail");
  });
  httpRequest.destroy();
}).catch((error: BusinessError) => {
  console.error("errcode" + JSON.stringify(error));
});

#### HttpDataType9+

Enumerates HTTP data types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| STRING | 0 | String type. |
| OBJECT | 1 | Object type. |
| ARRAY\_BUFFER | 2 | Binary array type. |

#### HttpProtocol9+

Enumerates HTTP protocol versions.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| HTTP1\_1 | 0 | 
HTTP1.1.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| HTTP2 | 1 | 

HTTP2.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| HTTP311+ | 2 | 

HTTP3. If the system or server does not support HTTP3, the HTTP protocol of an earlier version is used.

**Note**: This parameter takes effect only for HTTPS URLs. If this parameter is set to HTTP, the request will fail.

 |

#### CertType11+

Enumerates certificate types.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| PEM | PEM | PEM certificate. |
| DER | DER | DER certificate. |
| P12 | P12 | P12 certificate. |

#### CertificatePinning12+

Defines the dynamic configuration of certificate pinning.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| publicKeyHash | string | No | No | Certificate PIN of the string type. |
| hashAlgorithm | 'SHA-256' | No | No | Encryption algorithm. Currently, only SHA-256 is supported. |

#### HttpProxy10+

type HttpProxy = connection.HttpProxy

Defines the network proxy configuration.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| connection.HttpProxy | Network proxy configuration. |

#### AddressFamily15+

Enumerates IP address families of the target domain name.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | CURL\_IPRESOLVE\_WHATEVER | Automatically selects the IPv4 or IPv6 address of the target domain name. |
| ONLY\_V4 | CURL\_IPRESOLVE\_V4 | Resolves only the IPv4 address of the target domain name and ignores the IPv6 address. |
| ONLY\_V6 | CURL\_IPRESOLVE\_V6 | Resolves only the IPv6 address of the target domain name and ignores the IPv4 address. |

#### Credential18+

Represents the credential used for server identity verification in a session, including the user name and password.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| username | string | No | No | User name used for verification. The default value is **''**. |
| password | string | No | No | Password used for verification. The default value is **''**. |

#### ServerAuthentication18+

Defines HTTP server identity verification information.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| credential | [Credential](#credential18) | No | No | Server credential. The default value is **undefined**. |
| authenticationType | [AuthenticationType](#authenticationtype18) | No | Yes | Server identity verification type. If the type is not set, negotiation with the server is required. |

#### TlsConfig18+

Defines the TLS configuration, including the version and cipher suite.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| tlsVersionMin | [TlsVersion](#tlsversion18) | No | No | Earliest TLS version. |
| tlsVersionMax | [TlsVersion](#tlsversion18) | No | No | Latest TLS version. |
| cipherSuites | [CipherSuite](#ciphersuite18)\[\] | No | Yes | Array of cipher suite types. If no cipher suite type is set, all supported cipher suite types are carried by default. For details about the cipher suite types, see [TlsV13SpecificCipherSuite](#tlsv13specificciphersuite18), [TlsV12SpecificCipherSuite](#tlsv12specificciphersuite18) and [TlsV10SpecificCipherSuite](#tlsv10specificciphersuite18). |

#### TlsVersion18+

Enumerates TLS versions.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| TLS\_V\_1\_0 | 4 | TLS version 1.0. |
| TLS\_V\_1\_1 | 5 | TLS version 1.1. |
| TLS\_V\_1\_2 | 6 | TLS version 1.2. |
| TLS\_V\_1\_3 | 7 | TLS version 1.3. |

#### TlsOptions18+

type TlsOptions = 'system' | TlsConfig

Defines the TLS configuration.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'system' | TLS version of the system. This field is defaulted to **system** when the value is not set. |
| TlsConfig | Custom TLS version and cipher suites. |

#### RemoteValidation18+

type RemoteValidation = 'system' | 'skip'

Enumerates the identity verification modes of the remote server.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'system' | Use of the system CA. This field is defaulted to **system** when the value is not set. |
| 'skip' | Skipping of CA verification. This field has a fixed value of **skip**. |

#### AuthenticationType18+

type AuthenticationType = 'basic' | 'ntlm' | 'digest'

Enumerates server authentication modes in a session.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'basic' | Basic authentication mode. This field has a fixed value of **basic**. |
| 'ntlm' | NTLM authentication mode. This field has a fixed value of **ntlm**. |
| 'digest' | Digest authentication mode. This field has a fixed value of **digest**. |

#### CipherSuite18+

type CipherSuite = TlsV13CipherSuite

Declares the cipher suite.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| TlsV13CipherSuite | Cipher suite defined in [TlsV13CipherSuite](#tlsv13ciphersuite18). |

#### TlsV13CipherSuite18+

type TlsV13CipherSuite = TlsV12CipherSuite | TlsV13SpecificCipherSuite

Declares the cipher suite for TLS 1.3, which is also compatible with TLS 1.2.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| TlsV12CipherSuite | [TlsV11CipherSuite](#tlsv11ciphersuite18). |
| TlsV13SpecificCipherSuite | [TlsV13SpecificCipherSuite](#tlsv13specificciphersuite18). |

#### TlsV12CipherSuite18+

type TlsV12CipherSuite = TlsV11CipherSuite | TlsV12SpecificCipherSuite

Declares the cipher suite for TLS 1.2, which is also compatible with TLS 1.1.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| TlsV11CipherSuite | [TlsV11CipherSuite](#tlsv11ciphersuite18). |
| TlsV12SpecificCipherSuite | [TlsV12SpecificCipherSuite](#tlsv12specificciphersuite18). |

#### TlsV11CipherSuite18+

type TlsV11CipherSuite = TlsV10CipherSuite

Declares the cipher suite for TLS 1.1, which is the same as that for TLS1.0.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| TlsV10CipherSuite | [TlsV10CipherSuite](#tlsv10ciphersuite18). |

#### TlsV10CipherSuite18+

type TlsV10CipherSuite = TlsV10SpecificCipherSuite

Declares the cipher suite for TLS 1.0.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| TlsV10SpecificCipherSuite | [TlsV10SpecificCipherSuite](#tlsv10specificciphersuite18). |

#### TlsV13SpecificCipherSuite18+

type TlsV13SpecificCipherSuite = 'TLS\_AES\_128\_GCM\_SHA256' | 'TLS\_AES\_256\_GCM\_SHA384' | 'TLS\_CHACHA20\_POLY1305\_SHA256'

Enumerates cipher suites supported by TLS 1.3 or later.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'TLS\_AES\_128\_GCM\_SHA256' | Supported cipher suite: TLS\_AES\_128\_GCM\_SHA256. The value is a string. |
| 'TLS\_AES\_256\_GCM\_SHA384' | Supported cipher suite: TLS\_AES\_256\_GCM\_SHA384. The value is a string. |
| 'TLS\_CHACHA20\_POLY1305\_SHA256' | Supported cipher suite: TLS\_CHACHA20\_POLY1305\_SHA256. The value is a string. |

#### TlsV12SpecificCipherSuite18+

type TlsV12SpecificCipherSuite = 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256' |

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384' |

'TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | 'TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256' |

'TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | 'TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384'

Enumerates cipher suites supported by TLS 1.2 or later.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256' | Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256. The value is a string. |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256. The value is a string. |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384' | Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384. The value is a string. |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384' | Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384. The value is a string. |
| 'TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256. The value is a string. |
| 'TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256. The value is a string. |
| 'TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | Supported cipher suite: TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256. The value is a string. |
| 'TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384' | Supported cipher suite: TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384. The value is a string. |

#### TlsV10SpecificCipherSuite18+

type TlsV10SpecificCipherSuite = 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA' |

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA' |

'TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA'

Enumerates cipher suites supported by TLS 1.0 or later.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA' | Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA. The value is a string. |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA' | Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA. The value is a string. |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA' | Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA. The value is a string. |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA' | Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA. The value is a string. |
| 'TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA' | Supported cipher suite: TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA. The value is a string. |
| 'TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA' | Supported cipher suite: TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA. The value is a string. |
| 'TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA' | Supported cipher suite: TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA. The value is a string. |

#### SslType20+

type SslType = 'TLS' | 'TLCP'

Defines the secure communications protocol.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'TLS' | TLS protocol. The value is fixed to **TLS**. |
| 'TLCP' | 
TLCP protocol. The value is fixed to **TLCP**.

**NOTE**

(1) The certificate supports the following string specifications:

\- UTF8String (English character set)

\- PrintableString

\- IA5String

Supported since API Version 22:

\- TeletexString

(2) The certificate supports the following extended specifications:

\- BasicConstraints (OID 2.5.29.19)

\- KeyUsage (OID2.5.29.15)

\- SubjectKeyIdentifier (OID2.5.29.14)

\- AuthorityKeyIdentifier (OID2.5.29.35)

Supported since API Version 22:

\- SubjectAltName (OID 2.5.29.17)

\- ExtendedKeyUsage (OID 2.5.29.37)

 |

#### InterceptorType22+

Enumerates the types of HTTP interceptors.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| INITIAL\_REQUEST | 'INITIAL\_REQUEST' | Intercepts after the initial HTTP request is assembled. |
| REDIRECTION | 'REDIRECTION' | Intercepts when a redirection response is received. |
| CACHE\_CHECKED | 'READ\_CACHE' | Intercepts when the HTTP cache is checked and hit. |
| NETWORK\_CONNECT | 'CONNECT\_NETWORK' | Intercepts before the network request is sent. |
| FINAL\_RESPONSE | 'FINAL\_RESPONSE' | Intercepts when the final HTTP response is obtained. |

#### HttpRequestContext22+

Defines HTTP request context data. The object instance is passed as a parameter in the [interceptorHandle](#interceptorhandle22) method of the interceptor. You can use this object to obtain and modify the information about the HTTP request.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

## Attributes

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| url | string | No | No | URL obtained by the HTTP interceptor from the HTTP request, which can be modified in the interceptor. |
| header | Object | No | No | Request header obtained by the HTTP interceptor from the HTTP request, which can be modified in the interceptor. |
| body | Object | No | No | Request body obtained by the HTTP interceptor from the HTTP request, which can be modified in the interceptor. |

#### ChainContinue22+

type ChainContinue = boolean

Specifies whether to continue to process the interceptor chain.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates that the interceptor chain continues to be processed, and the value **false** indicates that the interceptor chain is terminated and an HTTP response is returned. |

#### HttpInterceptor22+

Defines the HTTP interceptor API, which is used to define the interception processing function.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

## Attributes

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interceptorType | [InterceptorType](#interceptortype22) | No | No | Interceptor type, which defines when the interceptor is called. |

#### \[h2\]interceptorHandle22+

interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>

Intercepts the HTTP processing process and modifies it as required.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reqContext | [HttpRequestContext](#httprequestcontext22) | Yes | Context of the request parameters passed through the HTTP interceptor. |
| rspContext | [HttpResponse](#httpresponse) | Yes | Context of the return result passed through the HTTP interceptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ChainContinue](#chaincontinue22)\> | Continues the HTTP processing or stops and returns an HTTP response. |

**Example**

import { http } from '@kit.NetworkKit';

// Create a custom interceptor.
class CustomInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.INITIAL\_REQUEST;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Add the authentication header in the initial request phase.
    reqContext.header\['Authorization'\] = 'Bearer token';
    console.info('Interceptor: Added authorization header');
    return true; // Continue to process the interceptor chain.
  }
}

let customInterceptor = new CustomInterceptor();

#### HttpInterceptorChain22+

Defines HTTP interceptor chain.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

**Example**

import { http } from '@kit.NetworkKit';

let interceptorChain = new http.HttpInterceptorChain();

#### \[h2\]addChain22+

addChain(chain: HttpInterceptor\[\]): boolean

Adds an interceptor to the HTTP client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/WYBWSSaBQmSEFTloIdjK2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82E9223315081E2E870A7AD46B9A8D8D0FB930AD8B1ACBF6BD47A25ECD722F93)

An interceptor chain cannot contain interceptor instances of the same type. If interceptors of the same type are passed in, the error code **2300802** (Duplicated interceptor type in the chain) is reported.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| chain | [HttpInterceptor](#httpinterceptor22)\[\] | Yes | Interception chain composed of interceptor instances. A single interceptor or multiple interceptors of different types can be passed in. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the interceptor is added successfully. The value **true** indicates that the interceptor is successfully added, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 2300801 | Parameter type not supported by the interceptor. |
| 2300802 | Duplicated interceptor type in the chain. |
| 2300999 | Internal error. |

**Example**

import { http } from '@kit.NetworkKit';

// Create an authentication interceptor.
class AuthInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.INITIAL\_REQUEST;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Add the authentication header in the initial request phase.
    reqContext.header\['Authorization'\] = 'Bearer token';
    console.info('Interceptor: Added authorization header');
    return true; // Continue to process the interceptor chain.
  }
}

class LoggingInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.FINAL\_RESPONSE;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Record logs in the final response phase.
    console.info(\`LoggingInterceptor: Request to ${reqContext.url} completed with status ${rspContext.responseCode}\`);
    return true; // Continue to process the interceptor chain.
  }
}

// Create an interceptor chain and apply the interceptor chain to the request.
let interceptorChain = new http.HttpInterceptorChain();
let authInterceptor = new AuthInterceptor();
let loggingInterceptor = new LoggingInterceptor();

// Add the interceptor to the chain.
try {
  let success = interceptorChain.addChain(\[authInterceptor, loggingInterceptor\]);
  if (!success) {
    console.error('Failed to add interceptor chain');
  }
} catch (e) {
  console.error(\`Interceptor chain add failed: code=${e.code}, message=${e.message}\`);
}

#### \[h2\]getChain22+

getChain(): HttpInterceptor\[\]

Obtains all interceptor instances in the current interceptor chain.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [HttpInterceptor](#httpinterceptor22)\[\] | Returns all interceptor instances added by the [addChain](#addchain22) method. |

**Example**

import { http } from '@kit.NetworkKit';

// Create a custom interceptor.
class CustomInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.INITIAL\_REQUEST;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Add the authentication header in the initial request phase.
    reqContext.header\['Authorization'\] = 'Bearer token';
    console.info('Interceptor: Added authorization header');
    return true; // Continue to process the interceptor chain.
  }
}

// Create an interceptor chain and apply the interceptor chain to the request.
let interceptorChain = new http.HttpInterceptorChain();
let customInterceptor = new CustomInterceptor();

// Add the interceptor to the chain.
try {
  let success = interceptorChain.addChain(\[customInterceptor\]);
  if (!success) {
    console.error('Failed to add interceptor chain');
  }
} catch (e) {
  console.error(\`Interceptor chain add failed: code=${e.code}, message=${e.message}\`);
}

// Obtain all interceptors in the current interceptor chain.
let chain = interceptorChain.getChain();
console.info(\`Current interceptor chain has ${chain.length} interceptors\`);

#### \[h2\]apply22+

apply(httpRequest: HttpRequest): boolean

Adds an interceptor chain to the target HTTP request. Each HTTP request instance can have only one interceptor chain attached.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/TsGBt8hDTamPaF9tTK3x7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57165C642C08C60E5BA53F467A1D323B9F7C4B72A8DC7A353588442A65585B03)

After an interceptor chain is attached to an [HttpRequest](#httprequest) instance, when the instance initiates an HTTP request, interceptors of the corresponding type in the attached interceptor chain are triggered.

For more information about how to trigger interceptors using HTTP requests, see [HTTP Interceptor Function Code Example](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/http-request#http-interceptor).

The HTTP interceptor feature is supported only by [HttpRequest.request](#request) APIs, and is not supported by [HttpRequest.requestInStream](#requestinstream10) APIs (streaming transmission).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| httpRequest | [HttpRequest](#httprequest) | Yes | [HttpRequest](#httprequest) that initiates an HTTP request. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the interceptor is attached successfully. The value **true** indicates that the interceptor is successfully added, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [HTTP Error Codes](../../error-codes/http-error-codes/document.md).

The HTTP error code mapping is in the format of 2300000 + Curl error code. For more common error codes, see [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

| ID | Error Message |
| :-- | :-- |
| 2300801 | Parameter type not supported by the interceptor. |
| 2300999 | Internal error. |

**Example**

import { http } from '@kit.NetworkKit';

// Create an authentication interceptor.
class AuthInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.INITIAL\_REQUEST;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Add the authentication header in the initial request phase.
    reqContext.header\['Authorization'\] = 'Bearer token';
    console.info('Interceptor: Added authorization header');
    return true; // Continue to process the interceptor chain.
  }
}

class LoggingInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.FINAL\_RESPONSE;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Record logs in the final response phase.
    console.info(\`LoggingInterceptor: Request to ${reqContext.url} completed with status ${rspContext.responseCode}\`);
    return true; // Continue to process the interceptor chain.
  }
}

// Create an interceptor chain.
let interceptorChain = new http.HttpInterceptorChain();
let authInterceptor = new AuthInterceptor();
let loggingInterceptor = new LoggingInterceptor();

// Create an HTTP request.
let httpRequest = http.createHttp();

try {
  // Add the interceptor to the chain.
  let success = interceptorChain.addChain(\[authInterceptor, loggingInterceptor\]);
  if (!success) {
    console.error('Failed to add interceptor chain');
  }

  // Apply the interceptor chain to the HTTP request.
  let applySuccess = interceptorChain.apply(httpRequest);
  if (!applySuccess) {
    console.error('Failed to apply interceptor chain');
  }
} catch (e) {
  console.error(\`Interceptor chain add failed: code=${e.code}, message=${e.message}\`);
}

// Initiate an HTTP request. If interception is required, the request can be initiated only through the request API.
httpRequest.request("EXAMPLE\_URL", {
  method: http.RequestMethod.GET,
  header: { 'Content-Type': 'application/json' }
}, (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Request completed with response code: ' + data.responseCode);
  } else {
    console.error('Request failed: ' + JSON.stringify(err));
  }
  httpRequest.destroy();
});
