# rcp

This module provides the HTTP data request capability. With this capability, your app can send data requests using HTTP. Common HTTP methods include GET, POST, HEAD, PUT, DELETE, PATCH, and OPTIONS.

**Start version**: 4.1.0(11)

#### Module Import

import { rcp } from '@kit.RemoteCommunicationKit';

#### rcp.createSession

createSession(sessionConfiguration?: SessionConfiguration): Session

Creates an HTTP session. This is the main method for starting an HTTP interaction. You can use this API and [SessionConfiguration](#section18613443123412) together to create and configure a session.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/rrstQOyESUyt-ZlWBe2oYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062351Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45CB57EFFCE674E3D8C52A9B09FBD34F9CDA84BCB2F19B8DD65CA9ADE01F5A35)

A maximum of 1024 session instances can be created in this version. The requirement has been changed since version 5.1.0(18). To ensure efficient resource utilization, your app should promptly close sessions after completing network requests using these created session instances.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

sessionConfiguration

 | 

[SessionConfiguration](#section18613443123412)

 | 

No

 | 

Configurations to be applied to a session.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Session](#section1671892662116)

 | 

Represents a session, for sending HTTP requests and managing the lifecycle of the session.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007900994

 | 

Sessions number reached limit.

 |

**Example**:

const session = rcp.createSession();

#### Session

Represents a communication session that can be used to initiate HTTP requests. It supports various HTTP methods, such as FETCH, GET, POST, PUT, HEAD, DELETE, CANCEL and CLOSE.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

string

 | 

Yes

 | 

No

 | 

Session identifier.

 |
| 

configuration

 | 

[SessionConfiguration](#section18613443123412) | undefined

 | 

Yes

 | 

No

 | 

Session configurations.

 |

#### \[h2\]fetch

fetch(request: Request): Promise<Response>

Sends an HTTP request and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

Yes

 | 

Request to be sent.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
let req = new rcp.Request("http://example.com/fetch", "POST");
session.fetch(req).then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]fetchForSendable

fetchForSendable(request: Request): Promise<ResponseSendable>

Sends an HTTP request and returns the HTTP response from the server. The response message supports Sendable. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

Yes

 | 

Request to be sent.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ResponseSendable](#section92642282211)\>

 | 

Promise object, which is used to return the response object from the server. The response message supports Sendable.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';
import { ArkTSUtils, collections, taskpool, util } from '@kit.ArkTS';
import utils from '@arkts.utils';

@Concurrent
async function taskFunc(sendableResponse: rcp.ResponseSendable) {
  console.info(\`sendableResponse: ${ArkTSUtils.ASON.stringify(sendableResponse)}\`);  
  // Print the body data of the Sendable type.
  if (utils.isSendable(sendableResponse.body) && sendableResponse.body != undefined) {
    const decoder = util.TextDecoder.create('utf-8');
    let arr: collections.Uint8Array = new collections.Uint8Array(sendableResponse.body);
    let str = decoder.decodeToString(arr as Object as Uint8Array).trim();
    console.info(\`body:${ArkTSUtils.ASON.stringify(str)}\`);
  }
}

async function test() {
  try {
    const session = rcp.createSession();
    let request = new rcp.Request('https://www.example.com'); // Replace the URL with the actual one.
    let sendableResponse = await session.fetchForSendable(request);
    let isSendable = utils.isSendable(sendableResponse);
    if (isSendable) {
      console.info(\`Succeeded in getting the response, the response is sendable\`);
    } else {
      console.info(\`Succeeded in getting the response, the response is not sendable\`);
    }
    let task: taskpool.Task = new taskpool.Task(taskFunc, sendableResponse);
    await taskpool.execute(task);
  } catch (err) {
    console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err)}\`);
  }
}

#### \[h2\]get

get(url: URLOrString, destination?: ResponseBodyDestination): Promise<Response>

Sends an HTTP GET request carrying default HTTP parameters and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP GET request.

 |
| 

destination

 | 

[ResponseBodyDestination](#section9250173916506)

 | 

No

 | 

Destination of the HTTP response.

**Start version**: 5.0.0(12)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.get("http://example.com/get").then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]post

post(url: URLOrString, content?: RequestContent, destination?: ResponseBodyDestination): Promise<Response>

Sends an HTTP POST request carrying default HTTP parameters and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP POST request.

 |
| 

content

 | 

[RequestContent](#section18971142565016)

 | 

No

 | 

Request content. The default value is **undefined**.

 |
| 

destination

 | 

[ResponseBodyDestination](#section9250173916506)

 | 

No

 | 

Destination of the HTTP response.

**Start version**: 5.0.0(12)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.post("http://example.com/post", "data to send").then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]put

put(url: URLOrString, content?: RequestContent, destination?: ResponseBodyDestination): Promise<Response>

Sends an HTTP PUT request carrying default HTTP parameters and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP PUT request.

 |
| 

content

 | 

[RequestContent](#section18971142565016)

 | 

No

 | 

Content of the request body. The default value is **undefined**.

 |
| 

destination

 | 

[ResponseBodyDestination](#section9250173916506)

 | 

No

 | 

Destination of the HTTP response.

**Start version**: 5.0.0(12)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.put("http://example.com/put", "data to send").then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]downloadToFile

downloadToFile(url: URLOrString, downloadTo: DownloadToFile): Promise<Response>

Sends an HTTP DOWNLOADTOFILE request carrying default HTTP parameters and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP DOWNLOADTOFILE request.

 |
| 

downloadTo

 | 

[DownloadToFile](#section298118136197)

 | 

Yes

 | 

Location in the local file system for storing files downloaded from the server via HTTP.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let downloadToFile: rcp.DownloadToFile = {
  kind: 'folder',
  path: "/path/dir" // Set the path based on your service needs.
} as rcp.DownloadToFile
const session = rcp.createSession();
session.downloadToFile("http://www.example.com", downloadToFile).then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`DownloadToFile failed, the error message is ${JSON.stringify(err)}\`);
});

#### \[h2\]uploadFromFile

uploadFromFile(url: URLOrString, uploadFrom: UploadFromFile): Promise<Response>

Sends an HTTP UPLOADFROMFILE request carrying default HTTP parameters to complete file upload and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP UPLOADFROMFILE request.

 |
| 

uploadFrom

 | 

[UploadFromFile](#section1753162618375)

 | 

Yes

 | 

HTTP request for uploading a local file to the server.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let fileDir = "/path/dir/"; // Define the path based on the service requirements.
let uploadFromFile: rcp.UploadFromFile = {
  fileOrPath: fileDir
};
const session = rcp.createSession();
session.uploadFromFile("http://example.com/head", uploadFromFile).then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]downloadToStream

downloadToStream(url: URLOrString, downloadTo: DownloadToStream): Promise<Response>

Sends an HTTP DOWNLOADTOSTREAM request carrying default HTTP parameters and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP DOWNLOADTOSTREAM request.

 |
| 

downloadTo

 | 

[DownloadToStream](#section1790033215431)

 | 

Yes

 | 

HTTP request for downloading a file from the server to the client and writing the file to a data stream.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit'

const streamData: rcp.WriteStream = {
  write(buffer: ArrayBuffer): Promise<void | number> {
    return Promise.resolve(buffer.byteLength)
  }
};

let downloadToStream: rcp.DownloadToStream = {
  kind: 'stream',
  stream: streamData
}
const session = rcp.createSession();
session.downloadToStream("http://example.com/head", downloadToStream).then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]uploadFromStream

uploadFromStream(url: URLOrString, uploadFrom: UploadFromStream): Promise<Response>

Sends an HTTP UPLOADFROMSTREAM request carrying default HTTP parameters to complete file upload and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP UPLOADFROMSTREAM request.

 |
| 

uploadFrom

 | 

[UploadFromStream](#section187981940151318)

 | 

Yes

 | 

HTTP request for uploading data from an input stream to the server.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

let uploadFromStream: rcp.UploadFromStream = {
  stream : object // Define an object of the **Stream**, **ReadStream**, or **SyncReadStream** type.
}
const session = rcp.createSession();
session.uploadFromStream("http://example.com/head", uploadFromStream).then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]head

head(url: URLOrString): Promise<Response>

Sends an HTTP HEAD request carrying default HTTP parameters and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP HEAD request.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.head("http://example.com/head").then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]delete

delete(url: URLOrString): Promise<Response>

Sends an HTTP DELETE request carrying default HTTP parameters and obtains an HTTP response from the server. This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.INTERNET (If the **cellular** option of [PathPreference](#section828055885811) is used, the **ohos.permission.GET\_NETWORK\_INFO** permission is also required.)

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL of the target resource in the HTTP DELETE request.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
session.delete("http://example.com/delete").then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]cancel

cancel(requestToCancel?: Request | Request\[\]): void

Cancels a specified request or all ongoing requests in a session.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

requestToCancel

 | 

[Request](#section10768169134510) | [Request](#section10768169134510)\[\]

 | 

No

 | 

Request or array of requests to be canceled. If [Request](#section10768169134510) is not specified, all requests are canceled by default.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
let req = new rcp.Request("http://example.com/fetch", "GET");
session.fetch(req).then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
  session.cancel(req);
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]close

close(): void

Closes a session. This API frees up resources related to this session.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
let req = new rcp.Request("http://example.com/fetch", "GET");
session.fetch(req).then((response) => {
  console.info(\`Succeeded in getting the response ${response}\`);
  session.close();
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
  session.close();
});

#### RequestHandler

Provides the interceptor handler.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]handle

handle(context: RequestContext): Promise<Response>

Handler that returns the result asynchronously using a promise. In the framework, two types of handlers are preconfigured: one calls the [intercept](#section527252111410) function of the interceptor and the other calls **fetchInternal**.

For example, the interceptor chain \[A, B, C, D\] is constructed as follows:

A {handler->B{handler->C{handler-D{handler->System capability}}

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[RequestContext](#section08792411316)

 | 

Yes

 | 

Request context.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

Promise object, which is used to return the response object from the server.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

class RequestHandler implements rcp.RequestHandler {
  handle(context: rcp.RequestContext): Promise<rcp.Response> {
    let handlerRequest = new rcp.Request("https://www.example.com", 'GET');
    let handlerSession = rcp.createSession();
    context.request = handlerRequest;
    context.session = handlerSession;
    return new Promise<rcp.Response>((resolve, reject) => {
      handlerSession.get("https://www.example.com").then((response: rcp.Response) => {
        resolve(response);
      }).catch((error: Error) => {
        reject(error);
      })
    });
  }
}

#### RequestContext

Defines the interceptor request context.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

No

 | 

HTTP request.

 |
| 

session

 | 

[Session](#section1671892662116)

 | 

No

 | 

No

 | 

Session that holds this interceptor.

 |

#### Interceptor

Defines an interceptor.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]intercept

intercept(context: RequestContext, next: RequestHandler): Promise<Response>

Interceptor, which is used to modify requests, modify responses, or directly return responses. It uses a promise to return the result asynchronously.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[RequestContext](#section08792411316)

 | 

Yes

 | 

Request context.

 |
| 

next

 | 

[RequestHandler](#section83672138232)

 | 

Yes

 | 

Next request handler.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Response](#section156381815599)\>

 | 

**Promise** object or the value of the next interceptor.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

class ResponseCache {
  private readonly cache: Record<string, rcp.Response> = {};

  getResponse(url: string): rcp.Response {
    return this.cache\[url\];
  }

  setResponse(url: string, response: rcp.Response): void {
    this.cache\[url\] = response;
  }
}

class ResponseCachingInterceptor implements rcp.Interceptor {
  private readonly cache: ResponseCache;

  constructor(cache: ResponseCache) {
    this.cache = cache;
  }

  async intercept(context: rcp.RequestContext, next: rcp.RequestHandler): Promise<rcp.Response> {
    const url = context.request.url.href;
    const responseFromCache = this.cache.getResponse(url);
    if (responseFromCache) {
      return Promise.resolve(responseFromCache);
    }
    const promise = next.handle(context);
    promise.then((resp) => {
      resp.statusCode;
      cache.setResponse(url, resp);
    });
    return promise;
  }
}

const cache = new ResponseCache();

async function testInterceptor() {
  const session = rcp.createSession({
    interceptors: \[new ResponseCachingInterceptor(cache)\]
  });

  await session.get('https://www.example.com').then((response: rcp.Response) => {
    console.info(\`Response succeeded: ${response}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Response failed: error message is ${JSON.stringify(error)}\`);
  });

  let request = new rcp.Request("https://www.example.com", 'GET');
  const response2 = await session.fetch(request).then((response: rcp.Response) => {
    console.info(\`Response succeeded: ${response}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Response failed: error message is ${JSON.stringify(error)}\`);
  });
}

#### SessionConfiguration

Defines session configurations to facilitate refined control over HTTP sessions.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

interceptors

 | 

[Interceptor](#section1385412349596)\[\]

 | 

No

 | 

Yes

 | 

Request/Response interceptor.

**Start version**: 5.0.0(12)

 |
| 

requestConfiguration

 | 

[Configuration](#section1898141153617)

 | 

No

 | 

Yes

 | 

Settings of HTTP requests associated with the session, including transfer, proxy, DNS, connection, and security settings.

 |
| 

baseAddress

 | 

[URLOrString](#section320653742718)

 | 

No

 | 

Yes

 | 

Base URL in a session. You can define a common base URL for multiple requests in a session. If a request URL is not an absolute URL, the base URL is appended before the request URL. For example, in the URL **https://example.com?name=value**, **https://example.com** is the base URL and **?name=value** is the request URL.

 |
| 

headers

 | 

[RequestHeaders](#section16586132194914)

 | 

No

 | 

Yes

 | 

Custom headers of HTTP requests sent in a session. You can customize headers based on your service needs.

 |
| 

cookies

 | 

[RequestCookies](#section127791738567)

 | 

No

 | 

Yes

 | 

Custom cookies that you can include in HTTP requests associated with a session based on your service needs. Cookies must be manually configured to record user behavior.

 |
| 

sessionListener

 | 

[SessionListener](#section1872726111319)

 | 

No

 | 

Yes

 | 

Listener that you can use to listen on cancellation and closing events of a specified session, so you can handle session-related events for your app.

 |
| 

connectionConfiguration

 | 

[ConnectionConfiguration](#section4802256134519)

 | 

No

 | 

Yes

 | 

Connection settings, including the total number of concurrent TCP connections allowed in a session and the maximum number of concurrent TCP connections allowed to a single host.

**Start version**: 5.0.0(12)

 |
| 

cacheControl

 | 

[CacheControl](#section191412521521)

 | 

No

 | 

Yes

 | 

Cache settings. This configuration is used to control the cache verification policy in a session, affecting how the server or proxy responds to requests.

**Start version**: 6.0.0(20)

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

const sessionConfig: rcp.SessionConfiguration = {
  requestConfiguration: {
    transfer: {
      autoRedirect: true,
      timeout: {
        connectMs: 5000,
        transferMs: 10000
      }
    },
    tracing: {
      verbose: true
    }
  },
  baseAddress: "http://api.example.com",
  headers: {
    "Authorization": "Bearer YOUR\_ACCESS\_TOKEN",
    "Content-Type": "application/json"
  },
  cookies: {
    "user": "john\_doe",
    "session\_id": "abc123"
  },
  sessionListener: {
    onCanceled: () => console.info("Session was cancelled"),
    onClosed: () => console.info("Session was closed")
  },
  // Sample code.
};

const session = rcp.createSession(sessionConfig);

**Parameter example of interceptors:**

import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

class ResponseCache {
  private readonly cache: Record<string, rcp.Response> = {};

  getResponse(url: string): rcp.Response {
    return this.cache\[url\];
  }

  setResponse(url: string, response: rcp.Response): void {
    this.cache\[url\] = response;
  }
}

class ResponseCachingInterceptor implements rcp.Interceptor {
  private readonly cache: ResponseCache;

  constructor(cache: ResponseCache) {
    this.cache = cache;
  }

  async intercept(context: rcp.RequestContext, next: rcp.RequestHandler): Promise<rcp.Response> {
    const url = context.request.url.href;
    const responseFromCache = this.cache.getResponse(url);
    if (responseFromCache) {
      return Promise.resolve(responseFromCache);
    }
    const promise = next.handle(context);
    promise.then((resp) => {
      this.cache.setResponse(url, resp);
    });
    return promise;
  }
}

const cache = new ResponseCache();

async function testInterceptor() {
  const session = rcp.createSession({
    interceptors: \[new ResponseCachingInterceptor(cache)\]
  });

  await session.get('https://www.example.com').then((response: rcp.Response) => {
    console.info(\`Response succeeded: ${response}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Response failed: error message is ${JSON.stringify(error)}\`);
  });

  let request = new rcp.Request("https://www.example.com", 'GET');
  const response2 = await session.fetch(request).then((response: rcp.Response) => {
    console.info(\`Response succeeded: ${response}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Response failed: error message is ${JSON.stringify(error)}\`);
  });
}

#### Configuration

Defines parameters that you can use to define HTTP requests in a session, including transmission, tracing, proxy, DNS, and security settings.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

transfer

 | 

[TransferConfiguration](#section59321354193610)

 | 

No

 | 

Yes

 | 

Data transmission settings for HTTP request processing, including automatic redirection and timeout settings.

 |
| 

tracing

 | 

[TracingConfiguration](#section557714186379)

 | 

No

 | 

Yes

 | 

Tracing settings of HTTP requests, that can help you perform debugging and performance analysis.

 |
| 

proxy

 | 

[ProxyConfiguration](#section731665213712)

 | 

No

 | 

Yes

 | 

Proxy settings for a session. The options are **system**, **no-proxy**, and **WebProxy**.

 |
| 

dns

 | 

[DnsConfiguration](#section9677185417382)

 | 

No

 | 

Yes

 | 

DNS settings, where you can either customize your DNS rule or use DNS over HTTPS.

 |
| 

security

 | 

[SecurityConfiguration](#section1597118916425)

 | 

No

 | 

Yes

 | 

Security settings, including certificate and server identity verification settings.

 |
| 

processing

 | 

[ProcessingConfiguration](#section163971034123120)

 | 

No

 | 

Yes

 | 

Response processing configuration.

**Start version**: 5.0.0(12)

 |
| 

cache

 | 

[ResponseCache](#section1124718239340)

 | 

No

 | 

Yes

 | 

HTTP caching settings.

**Start version**: 6.0.0(20)

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

const cache: rcp.ResponseCache = new rcp.ResponseCache({
  persistent: {
    kind: 'file-system',
    pathToFolder: "/path/dir/" // Specify the cache path based on your service needs.
  }
});
const requestConfig: rcp.Configuration = {
  transfer: {
    autoRedirect: true,
    timeout: {
      connectMs: 5000,
      transferMs: 10000
    },
    assumesHTTP3Capable: true,
    pathPreference: "cellular"
  },
  tracing: {
    verbose: true
  },
  proxy: "system",
  dns: {
    dnsRules: \[
      { host: "https://example.com", port: 443, ipAddresses: \["192.168.1.1", "192.168.1.2"\] }
    \]
  },

  security: {
    certificate: {
      content: "-----BEGIN CERTIFICATE-----\\n...",
      type: "PEM",
      key: "/path/dir/", // Change the key based on your service needs.
      keyPassword: "your-password"
    },
    serverAuthentication: {
      credential: {
        username: "your-username",
        password: "your-password"
      },
      authenticationType: "basic"
    }
  },
  cache: cache
};

// Use the configuration in the session creation
const session = rcp.createSession({ requestConfiguration: requestConfig });

#### ConnectionConfiguration

Sets the total number of concurrent TCP connections and the maximum number of TCP connections allowed to a single host in a session.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxConnectionsPerHost

 | 

number

 | 

Yes

 | 

Yes

 | 

Maximum number of concurrent TCP connections allowed to a single host (identified by the combination of the host name and port number). The default value is **6** and the maximum value is **2147483647**.

 |
| 

maxTotalConnections

 | 

number

 | 

Yes

 | 

Yes

 | 

Maximum number of concurrent TCP connections allowed in a session. The default value is **64** and the maximum value is **2147483647**.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit'

const connectionConfig: rcp.ConnectionConfiguration = {
  maxConnectionsPerHost: 6,
  maxTotalConnections: 64
}
const session = rcp.createSession({ connectionConfiguration: connectionConfig });

#### TcpConfiguration

Enables settings of TCP options.

When any of the **keepIdleSec**, **keepCnt**, and **keepIntervalSec** parameters is set, the client sends a probe packet proactively. Parameters that are not set will use their default value. If the server does not respond to the probe packet within the specified duration in seconds (keepIdleSec + (keepCnt + 1) x keepIntervalSec), the TCP connection will be terminated.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

keepIdleSec

 | 

number

 | 

No

 | 

Yes

 | 

A timer that, when triggered, initiates the sending of a probe packet over the TCP connection.

Unit: second

Value range: 1 to 7200

Default value: **7200**

 |
| 

userTimeoutMs

 | 

number

 | 

No

 | 

Yes

 | 

Timeout interval. If no acknowledgment from the server is received for the transmitted data within this interval, the TCP connection will be terminated.

Unit: millisecond

Value range: 1 to 3,600,000

Default value: It is the same as the value of [Timeout](#section253517541009).**transferMs**.

 |
| 

keepCnt

 | 

number

 | 

No

 | 

Yes

 | 

Number of times that probe packets are sent.

Unit: integer

Value range: 1 to 9

Default value: **9**

 |
| 

keepIntervalSec

 | 

number

 | 

No

 | 

Yes

 | 

Interval between each two probe packets.

Unit: second

Value range: 1 to 75

Default value: **75**

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

const transferConfig: rcp.TransferConfiguration = {
  tcp: {
    keepIdleSec: 20,
    userTimeoutMs: 3000,
    keepCnt: 6,
    keepIntervalSec: 30,
  }
};

// Use the configuration in the session creation.
const session = rcp.createSession({
  requestConfiguration: {
    transfer: transferConfig
  }
});

// Use the configuration in the request.
const request = new rcp.Request('https://example.com');
request.configuration = {
  transfer: transferConfig
};

#### TransferConfiguration

Defines data transmission settings for HTTP requests in a session, including automatic redirection and timeout settings.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

autoRedirect

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the HTTP client needs to automatically follow redirects. The value **true** indicates yes. The default value is **true**.

 |
| 

timeout

 | 

[Timeout](#section253517541009)

 | 

No

 | 

Yes

 | 

HTTP request timeout settings for connection and data transmission. If this parameter is not set, the default value is used.

 |
| 

assumesHTTP3Capable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a connection supports HTTP/3. The options are **true** (yes) and **false** (no).

 |
| 

pathPreference

 | 

[PathPreference](#section828055885811)

 | 

No

 | 

Yes

 | 

Request path preferences. The configuration is only for system reference and the final path is determined by the system. The path preference can be configured as either automatic or cellular. The automatic option is used by default.

 |
| 

serviceType

 | 

[ServiceType](#section4811141807)

 | 

No

 | 

Yes

 | 

Service type. The default value is **undefined**.

 |
| 

maxAutoRedirects

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of redirections allowed, which needs to be specified when the **autoRedirect** parameter is set to **true**. The default value is **50** and the maximum value is **2147483647**.

**Start version**: 5.0.0(12)

 |
| 

pausePolicy

 | 

[PausePolicy](#section195053616613)

 | 

No

 | 

Yes

 | 

Request suspension policy.

**Start version**: 5.0.0(12)

 |
| 

tcp

 | 

[TcpConfiguration](#section1376921132812)

 | 

No

 | 

Yes

 | 

TCP connection settings.

**Start version**: 6.0.0(20)

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

const transferConfig: rcp.TransferConfiguration = {
  autoRedirect: true,
  timeout: {
    connectMs: 5000,
    transferMs: 10000
  },
  assumesHTTP3Capable: true,
  pathPreference: "cellular"
};

// Use the configuration in the session creation
const session = rcp.createSession({ requestConfiguration: { transfer: transferConfig } });

#### TracingConfiguration

Defines tracing settings for HTTP requests in a session, so you can collect information that can be used for data stream tracing, debugging, and performance analysis.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

verbose

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable tracing to collect HTTP request/response stream details. The options are **true** (yes) and **false** (no). The default value is **false**.

 |
| 

infoToCollect

 | 

[InfoToCollect](#section12292010397)

 | 

No

 | 

Yes

 | 

Events to be collected. By default, no event needs to be collected.

 |
| 

collectTimeInfo

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect time-related information. The options are **true** (yes) and **false** (no). The default value is **false**.

 |
| 

httpEventsHandler

 | 

[HttpEventsHandler](#section87603011401)

 | 

No

 | 

Yes

 | 

Callback triggered for specific operations during HTTP request/response processing. The default value is **undefined**.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

// Define a custom response handler
const customHttpEventsHandler: rcp.HttpEventsHandler = {
  onDataReceive: (incomingData: ArrayBuffer) => {
    // Custom logic for handling incoming data
    console.info("Received data:", incomingData);
    return incomingData.byteLength;
  },
  onUploadProgress: (totalSize: number, transferredSize: number) => {
    // Custom logic for handling upload progress
    console.info("Upload progress:", transferredSize, "of", totalSize);
  },
  onDownloadProgress: (totalSize: number, transferredSize: number) => {
    // Custom logic for handling download progress
    console.info("Download progress:", transferredSize, "of", totalSize);
  },
  onHeaderReceive: (headers: rcp.ResponseHeaders) => {
    // Custom logic for handling response headers
    console.info("Received headers:", headers);
  },
  onDataEnd: () => {
    // Custom logic for handling data transfer completion
    console.info("Data transfer complete");
  },
  onCanceled: () => {
    // Custom logic for handling cancellation
    console.info("Request/response canceled");
  },
  onStatusCodeReceive: (statusCode: number, request?: rcp.Request) => {
    // Custom logic for handling statusCode
    console.info("Received statusCode:", statusCode);
  }
};

// Configure tracing settings
const tracingConfig: rcp.TracingConfiguration = {
  verbose: true,
  infoToCollect: {
    textual: true,
    incomingHeader: true,
    outgoingHeader: true,
    incomingData: true,
    outgoingData: true,
    incomingSslData: true,
    outgoingSslData: true
  },
  collectTimeInfo: true,
  httpEventsHandler: customHttpEventsHandler
};

// Use the configuration in the session creation
const session = rcp.createSession({ requestConfiguration: { tracing: tracingConfig } });

#### ProxyConfiguration

type ProxyConfiguration = 'system' | 'no-proxy' | [WebProxy](#section750717273598)

Defines proxy settings for HTTP requests in a session, so you can flexibly choose between the options of system proxy, custom proxy, and no proxy.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Proxy Type

 | 

Description

 |
| :-- | :-- |
| 

'system'

 | 

HTTP proxy settings. **system**: The system proxy configuration is used.

 |
| 

'no-proxy'

 | 

HTTP proxy settings. **no-proxy**: No proxy is used.

 |
| 

[WebProxy](#section750717273598)

 | 

HTTP proxy settings. **WebProxy**: The custom proxy configuration is used.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

// Configure system proxy (default)
const systemProxyConfig = "system";

// Configure custom proxy
const customProxyConfig: rcp.WebProxy = {
  url: "http://custom-proxy.example.com",
  createTunnel: "always",
  exclusions: \["http://exclude.example.com"\],
  security: {
    certificate: {
      content: "-----BEGIN CERTIFICATE-----\\n...",
      type: "PEM",
      key: "-----BEGIN PRIVATE KEY-----\\n...", // Set the key based on your service needs.
      keyPassword: "your-password"
    },
    serverAuthentication: {
      credential: {
        username: "proxy-username",
        password: "proxy-password"
      },
      authenticationType: "basic"
    }
  }
};

// Configure no proxy
const noProxyConfig = "no-proxy";

// Use the proxy configuration in the session creation
const sessionWithSystemProxy = rcp.createSession({ requestConfiguration: { proxy: systemProxyConfig } });
const sessionWithCustomProxy = rcp.createSession({ requestConfiguration: { proxy: customProxyConfig } });
const sessionWithNoProxy = rcp.createSession({ requestConfiguration: { proxy: noProxyConfig } });

#### DnsConfiguration

Defines DNS settings for HTTP requests in a session. You can configure DNS rules flexibly, including customizing the DNS server or static DNS rules.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dnsRules

 | 

[DnsServers](#section520311317520) | [StaticDnsRules](#section8646352103418) | [DynamicDnsRule](#section8160554134811)

 | 

No

 | 

Yes

 | 

DNS rule. The default value is **undefined**. Other options are as follows:

**DnsServers**: A specified DNS server is preferentially used to resolve the host name.

**StaticDnsRules**: If the host name is matched, a specified address is used preferentially.

**DynamicDnsRule**: The address returned in the function is used preferentially.

CAUTION:

If multiple static or dynamic DNS rules are configured for the same domain name, only the last IP address takes effect by default. Since version 6.0.0(20), you can make multiple IP addresses effective at the same time by setting **happyEyeballOnDnsRule** to **true**.

 |
| 

dnsOverHttps

 | 

[DnsOverHttpsConfiguration](#section13705867403)

 | 

No

 | 

Yes

 | 

DNS over HTTPS. The default value is **undefined**.

If this parameter is set, DNS-resolved addresses will be used by priority.

 |
| 

happyEyeballOnDnsRule

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable Happy Eyeballs connection racing.

When the network path to a specific address or address family (IPv4 or IPv6) is blocked, unreachable, or suffers from poor network quality, the Happy Eyeballs connection racing mechanism helps establish a connection more quickly. The options are as follows:

**true**: Enable Happy Eyeballs connection racing when DNS rules are configured (defined by the **dnsRules** parameters).

**false**: Disable Happy Eyeballs connection racing when DNS rules are configured (defined by the **dnsRules** parameters).

The default value is **false**.

**Start version**: 6.0.0(20)

CAUTION:

This parameter takes effect only when **dnsRules** is set. If **dnsRules** is not set, the Happy Eyeballs connection racing is enabled by default and cannot be disabled.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

// Configure custom DNS servers
const customDnsServers: rcp.DnsServers = \[
  { ip: "8.8.8.8" },
  { ip: "8.8.4.4", port: 53 }
\];

// Configure static DNS rules
const staticDnsRules: rcp.StaticDnsRules = \[
  { host: "example.com", port: 80, ipAddresses: \["192.168.1.1", "192.168.1.2"\] },
  { host: "sub.example.com", port: 443, ipAddresses: \["192.168.2.1"\] }
\];

// Configure DNS over HTTPS
const dohConfig: rcp.DnsOverHttpsConfiguration = {
  url: "https://dns.example.com/dns-query",
  skipCertificatesValidation: true
};

// Use DNS configuration in the session creation.
const sessionWithCustomDns = rcp.createSession({ requestConfiguration: { dns: { dnsRules: customDnsServers } } });
const sessionWithStaticDns = rcp.createSession({
  requestConfiguration: {
    dns: {
      // for example.com, '192.168.1.2' is effective.
      // for sub.example.com, '192.168.2.1' is effective.
      dnsRules: staticDnsRules,
    }
  }
});
const sessionWithDoh = rcp.createSession({ requestConfiguration: { dns: { dnsOverHttps: dohConfig } } });

// Enable happy eyeball in the session creation when dns rules is set.
const sessionWithStaticDnsRulesAndHappyEyeball = rcp.createSession({
  requestConfiguration: {
    dns: {
      dnsRules: staticDnsRules, // Set dns rules here.
      happyEyeballOnDnsRule: true, // Enable happy eyeball here.
    }
  }
});

// Enable happy eyeball in the request configuration when dns rules is set.
const request = new rcp.Request('https://example.com');
request.configuration = {
  dns: {
    dnsRules: staticDnsRules, // Set dns rule here.
    happyEyeballOnDnsRule: true, // Enable happy eyeball here.
  }
};

#### DnsOverHttpsConfiguration

Defines DNS over HTTPS settings, allowing for secure DNS resolution via HTTPS endpoints.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

No

 | 

No

 | 

URL or string used to specify the DoH endpoint.

 |
| 

skipCertificatesValidation

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to skip SSL/TLS certificate verification for a DoH endpoint. The options are **true** (yes) and **false** (no). The default value is **false**.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

// Configure DNS over HTTPS settings
const dohConfig: rcp.DnsOverHttpsConfiguration = {
  url: "https://dns.example.com/dns-query",
  skipCertificatesValidation: true
};

// Use the DNS over HTTPS configuration in the session creation
const sessionWithDoh = rcp.createSession({ requestConfiguration: { dns: { dnsOverHttps: dohConfig } } });

#### SecurityConfiguration

Defines security-related settings for a session, including certificate and server identity verification settings.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

remoteValidation

 | 

'system' | 'skip' | [CertificateAuthority](#section1191716433375) | [ValidationCallback](#section209691249748)

 | 

No

 | 

Yes

 | 

Certificate authority (CA), which is used to verify the identity of a remote server. The default value is **system**.

If the parameter is not set, the default value is used. The options are as follows:

**system** (default): The system CA is used.

**skip**: Verification is skipped.

**CertificateAuthority**: The specific CA is used.

**ValidationCallback**: The certificate verification is customized.

NOTE:

In 5.0.0(12) and later versions, the option **ValidationCallback** is also supported.

 |
| 

certificate

 | 

[ClientCertificate](#section134001711153819)

 | 

No

 | 

Yes

 | 

Client certificate, which will be sent to the remote server to verify the identity of the client. The default value is **undefined**, indicating that verification is not required.

 |
| 

tlsOptions

 | 

'system' | [CipherSuite](#section184507292518)\[\] | [TlsV13Option](#section2816178141816) | [TlsV12Option](#section177701532908)| [TlsV11Option](#section147673411215) | [TlsV10Option](#section1638114214316)

 | 

No

 | 

Yes

 | 

TLS version selector. The options are as follows:

**system** (default): TLS version used by the system

[CipherSuite](#section184507292518)\[\]: array used to declare the cipher suite types

[TlsV13Option](#section2816178141816): TLS 1.3

[TlsV12Option](#section177701532908): TLS 1.2

[TlsV11Option](#section147673411215): TLS 1.1

[TlsV10Option](#section1638114214316): TLS 1.0

**Start version**: 5.0.0(12)

 |
| 

tlsRange

 | 

[TlsVersionRangeOptions](#section1023912106245)

 | 

No

 | 

Yes

 | 

TLS version range configurator, which can be used to define the TLS version range that can be used by the client. By default, this attribute is not set.

**Start version**: 6.0.0(20)

 |
| 

serverAuthentication

 | 

[ServerAuthentication](#section523243163818)

 | 

No

 | 

Yes

 | 

Indicates whether to verify the server identity during a secure connection. The identity is not verified by default.

 |
| 

certificatePinning

 | 

[CertificatePinning](#section930513513227)| [CertificatePinning](#section930513513227)\[\]

 | 

No

 | 

Yes

 | 

Certificate pinning settings.

**Start version**: 5.0.0(12)

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

// Configure security settings
const securityConfig: rcp.SecurityConfiguration = {
  remoteValidation: "system",
  certificate: {
    content: "-----BEGIN CERTIFICATE-----\\n...",
    type: "PEM",
    key: "-----BEGIN PRIVATE KEY-----\\n...", // Set the key based on your service needs.
    keyPassword: "your-password"
  },
  serverAuthentication: {
    credential: {
      username: "exampleUser",
      password: "examplePassword"
    },
    authenticationType: "basic"
  }
};

// Use the security configuration in the session creation
const sessionWithSecurityConfig = rcp.createSession({ requestConfiguration: { security: securityConfig } });

#### CertificateAuthority

CA used to verify the identity of a remote server.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

content

 | 

string | ArrayBuffer

 | 

No

 | 

Yes

 | 

A bundle of CA certificates for peer verification, in PEM format.

 |
| 

filePath

 | 

string

 | 

No

 | 

Yes

 | 

CA certificate path for peer verification. The certificate file must be in PEM format.

 |
| 

folderPath

 | 

string

 | 

No

 | 

Yes

 | 

Path to the directory storing multiple CA certificates used for peer verification. Files in this directory must be in PEM format.

 |

#### ClientCertificate

Defines certificate-related settings for secure connections in a session.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

content

 | 

string | ArrayBuffer

 | 

No

 | 

Yes

 | 

Content of the certificate issued by the CA. It is either a string or ArrayBuffer.

 |
| 

filePath

 | 

string

 | 

No

 | 

Yes

 | 

Path of the certificate file, which includes the CA that issues the certificate. The default value is **undefined**.

 |
| 

type

 | 

'PEM' | 'DER' | 'P12'

 | 

No

 | 

Yes

 | 

Encoding format of the client certificate. The default value is **undefined**.

 |
| 

key

 | 

string

 | 

No

 | 

Yes

 | 

Path of the private key file of the client certificate. The default value is **undefined**.

 |
| 

keyPassword

 | 

string

 | 

No

 | 

Yes

 | 

Password of the client certificate. The default value is **undefined**.

 |

#### ServerAuthentication

Defines HTTP server identity verification information.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

credential

 | 

[Credential](#section721442771710)

 | 

No

 | 

No

 | 

Server credential. The default value is **undefined**.

 |
| 

authenticationType

 | 

[AuthenticationType](#section5757123313210)

 | 

No

 | 

Yes

 | 

Server identity verification type. If the type is not set, negotiation with the server is required.

 |

#### TlsVersionRangeOptions

Sets the available TLS version range. You can define the minimum and maximum bounds of supported TLS versions for security purposes, and specify the list of cipher suites available within the range.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

min

 | 

[TlsVersion](#section9929122918293)

 | 

No

 | 

Yes

 | 

Minimum TLS version. By default, the system automatically selects a value and the parameter does not need to be set.

 |
| 

max

 | 

[TlsVersion](#section9929122918293)

 | 

No

 | 

Yes

 | 

Maximum TLS version. By default, the system automatically selects a value and the parameter does not need to be set.

 |
| 

cipherSuite

 | 

[CipherSuite](#section184507292518)\[\]

 | 

No

 | 

Yes

 | 

List of cipher suites available within the TLS version range. By default, the system automatically specifies the range and the parameter does not need to be set.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The minimum TLS version is greater than the maximum TLS version. This error code indicates a parameter error.

 |

#### Request

Defines an HTTP request.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

string

 | 

Yes

 | 

No

 | 

Unique request object ID, which is generated by the system.

 |
| 

url

 | 

[URL](#section66401230152412)

 | 

No

 | 

No

 | 

HTTP request URL.

 |
| 

method

 | 

[HttpMethod](#section20787153164810)

 | 

No

 | 

No

 | 

HTTP method to be used. The default value is **GET**.

 |
| 

headers

 | 

[RequestHeaders](#section16586132194914)

 | 

No

 | 

Yes

 | 

HTTP request header. The default value is **undefined**.

 |
| 

content

 | 

[RequestContent](#section18971142565016)

 | 

No

 | 

Yes

 | 

HTTP request content. The default value is **undefined**.

 |
| 

cookies

 | 

[RequestCookies](#section127791738567)

 | 

No

 | 

Yes

 | 

HTTP request cookies. This configuration will be converted into the HTTP Cookies header. The default value is **undefined**.

 |
| 

transferRange

 | 

[TransferRange](#section838945575618) | [TransferRange](#section838945575618)\[\]

 | 

No

 | 

Yes

 | 

HTTP transmission range. This configuration will be converted into the HTTP Range header. An HTTP request with the Range header requires the server to return only a part of the HTTP response. The default value is **undefined**.

 |
| 

configuration

 | 

[Configuration](#section1898141153617)

 | 

No

 | 

Yes

 | 

HTTP request configuration, which will be used to replace the default or session-range configuration. The default value is **undefined**.

 |
| 

destination

 | 

[ResponseBodyDestination](#section9250173916506)

 | 

No

 | 

Yes

 | 

Destination of the HTTP response body.

**Start version**: 5.0.0(12)

 |
| 

cacheControl

 | 

[CacheControl](#section191412521521)

 | 

No

 | 

Yes

 | 

HTTP request cache settings. If this attribute is set, the cache settings in [SessionConfiguration](#section18613443123412) do not take effect. The default value is **undefined**.

**Start version**: 6.0.0(20)

 |

#### \[h2\]constructor

constructor(url: URLOrString, method?: HttpMethod, headers?: RequestHeaders, content?: RequestContent, cookies?: RequestCookies, transferRange?: TransferRange | TransferRange\[\], configuration?: Configuration)

Provides the constructor used to create a **Request** object.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

Request address type. In a constructor, a character string that represents a URL needs to be converted into a URL.

 |
| 

method

 | 

[HttpMethod](#section20787153164810)

 | 

No

 | 

HTTP request method. The default value is **GET**.

 |
| 

headers

 | 

[RequestHeaders](#section16586132194914)

 | 

No

 | 

HTTP request header.

 |
| 

content

 | 

[RequestContent](#section18971142565016)

 | 

No

 | 

HTTP request body.

 |
| 

cookies

 | 

[RequestCookies](#section127791738567)

 | 

No

 | 

HTTP request cookies. This configuration will be converted into the HTTP Cookies header.

 |
| 

transferRange

 | 

[TransferRange](#section838945575618)| [TransferRange](#section838945575618)\[\]

 | 

No

 | 

HTTP transmission range. This configuration will be converted into the HTTP Range header.

 |
| 

configuration

 | 

[Configuration](#section1898141153617)

 | 

No

 | 

HTTP request configuration. For details, please refer to [Configuration](#section1898141153617).

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let content = "data to send";
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };
let req = new rcp.Request("http://example.com", "POST", headers, content, cookies, transferRange, configuration);

#### URL

type URL = url.URL

Request address type, which links to **URL** in @[ohos.url](../../../../../application-framework/arkts/arkts-apis/ohos-url-url-string-parsing/document.md).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

url.URL

 | 

@ohos.url.URL type, indicating the request URL type. The value can be any value of this type.

 |

#### X509Cert

type X509Cert = cert.X509Cert

x509 certificate type, which links to **X509Cert** in @[ohos.security.cert](../../../../security/device-certificate-kit/arkts-apis/ohos-security-cert-certificate/document.md).

The following table describes the value range.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

cert.X509Cert

 | 

@ohos.security.cert.X509Cert type. The value can be any value of this type.

 |

#### File

type File = fs.File

File in the file system, which links to **File** in @[ohos.file.fs](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

fs.File

 | 

@ohos.file.fs.File type. The value can be any value of this type.

 |

#### RandomAccessFile

type RandomAccessFile = fs.RandomAccessFile

File that can be accessed randomly, which links to **RandomAccessFile** in @[ohos.file.fs](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

fs.RandomAccessFile

 | 

@ohos.file.fs.RandomAccessFile type. The value can be any value of this type.

 |

#### Stream

type Stream = fs.Stream

Data stream type, which links to **Stream** in @[ohos.file.fs](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

fs.Stream

 | 

@ohos.file.fs.Stream type. The value can be any value of this type.

 |

#### RawDataContent

type RawDataContent = string | ArrayBuffer | object

Basic data types of ArkTs.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Text string, which can be any value of this type.

 |
| 

ArrayBuffer

 | 

Binary data, which can be any value of this type.

 |
| 

object

 | 

Object, which can be any value of this type.

 |

#### FileDescriptor

type FileDescriptor = number

Descriptor of a file, which is an abstract representation for accessing a file or I/O device.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Number type. The value can be any number.

 |

#### LocalFile

type LocalFile = [FileDescriptor](#section21886214126) | [File](#section627313541711) | [RandomAccessFile](#section5384161714342)

A file-like object that enables users to interact with it using various file descriptors or file objects.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[FileDescriptor](#section21886214126)

 | 

Descriptor of a file, which is an integer that identifies an open file.

 |
| 

[File](#section627313541711)

 | 

A file in a file system, which can be used to obtain the file descriptor, path, and name, as well as to perform locking and unlocking operations on the file.

 |
| 

[RandomAccessFile](#section5384161714342)

 | 

Type for implementing random access to files, including operations such as reading file descriptors and file pointers, setting file pointers, and writing files.

 |

#### WriteFile

Provides the function of writing data to a file.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]write

write(buffer: ArrayBuffer): Promise<void | number>

Writes data to a file. This API uses a promise to return the result asynchronously.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

Data to be written to a file.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void | number>

 | 

Promise object that contains the written data of the number type or no value. The promise is returned asynchronously.

 |

#### ReadFile

Provides the function for reading data from a file.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]read

read(buffer: ArrayBuffer): Promise<number>

Reads data from a file.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

File from which data needs to be read.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise object, which is used to return the data read from the file. The value is of the number type.

 |

#### WriteStream

Provides the function of writing data to a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]write

write(buffer: ArrayBuffer): Promise<void | number>

Writes data from a file to a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

Data to be written to the data stream.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void | number>

 | 

Promise object that contains the written data of the number type or no value.

 |

#### SyncWriteStream

Provides the function of synchronously writing data to a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]writeSync

writeSync(buffer: ArrayBuffer): void | number

Writes data to a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

Data to be written to the data stream.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Written data of the number type.

 |

#### ReadStream

Provides the function of reading data from a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]read

read(buffer: ArrayBuffer): Promise<number>

Reads data from a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

Data to be written to the data stream.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise object, which is used to return the data read from the file. The value is of the number type.

 |

#### SyncReadStream

Provides the function of synchronously reading data from a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]readSync

readSync(buffer: ArrayBuffer): number

Reads data from a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

Data to be written to the data stream.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Written data of the number type.

 |

#### DownloadedTo

Saves the downloaded content to the path specified in the DOWNLOADTOFILE request.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

path

 | 

[Path](#section173755717538)

 | 

No

 | 

No

 | 

If [Request.destination](#section10768169134510) specifies that content needs to be downloaded to a file, **path** indicates the path for storing the file.

 |
| 

requestSkipped

 | 

true

 | 

No

 | 

Yes

 | 

Currently, only the **true** option is provided, indicating that the request is skipped. If you do not want to skip the request, do not select this option.

 |

#### TargetFile

Saves data to either a specified directory or the default directory.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

path

 | 

[Path](#section173755717538)

 | 

No

 | 

No

 | 

Target path for data download.

 |
| 

skipRequest

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to skip the request. The value **true** indicates yes and the value **false** indicates no. The default value is **false**.

 |

#### TargetFileCallback

type TargetFileCallback = (request: [Request](#section10768169134510), suggestedPath: [Path](#section173755717538)) => [TargetFile](#section1522633761218) | Promise<[TargetFile](#section1522633761218)\>

Callback function that returns a [TargetFile](#section1522633761218) object asynchronously using a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

Yes

 | 

HTTP request.

 |
| 

suggestedPath

 | 

[Path](#section173755717538)

 | 

Yes

 | 

[Path](#section173755717538) specified in the request.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TargetFile](#section1522633761218) | Promise<[TargetFile](#section1522633761218)\>

 | 

[TargetFile](#section1522633761218) directly returned or returned using a promise. It indicates the target directory of downloaded data.

 |

#### IncomingDataCallback

type IncomingDataCallback = (incomingData: ArrayBuffer) => void | Promise<void>

Callback function for processing downloaded data.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

incomingData

 | 

ArrayBuffer

 | 

Yes

 | 

ArrayBuffer data to be processed.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

No value is returned. The called API returns results asynchronously through a promise.

 |

#### UploadFromFile

Uploads a file from the client to the server.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fileOrPath

 | 

[Path](#section173755717538) | [LocalFile](#section19493339161418) | [ReadFile](#section4363132325017)

 | 

Yes

 | 

No

 | 

File to be uploaded or the path of the file to be uploaded. For details, please refer to [Application Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file).

 |

#### \[h2\]constructor

constructor(fileOrPath: Path | LocalFile | ReadFile)

Provides the constructor used to create an **UploadFromFile** object.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fileOrPath

 | 

[Path](#section173755717538) | [LocalFile](#section19493339161418) | [ReadFile](#section4363132325017)

 | 

Yes

 | 

File to be uploaded or the path of the file to be uploaded. For details, please refer to [Application Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file).

 |

#### UploadFromStream

Uploads a file in stream mode.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

stream

 | 

[Stream](#section17454218451) | [ReadStream](#section14397920517) | [SyncReadStream](#section121694408513)

 | 

Yes

 | 

No

 | 

Stream to be uploaded.

 |

#### \[h2\]constructor

constructor(stream: Stream | ReadStream | SyncReadStream)

Provides the constructor used to create an **UploadFromStream** object.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

stream

 | 

[Stream](#section17454218451) | [ReadStream](#section14397920517) | [SyncReadStream](#section121694408513)

 | 

Yes

 | 

Stream to be uploaded.

 |

#### DownloadToFile

type DownloadToFile = { kind: 'file'; file: TargetFileCallback; } | { kind: 'file'; file: Path; keepLocal?: boolean; } | { kind: 'file'; file: LocalFile | WriteFile; } | { kind: 'folder'; path: Path; keepLocal?: boolean; }

Downloads a file to a specified directory or file. If a file is downloaded to a directory, its name on the server will be retained. The value contains all types in the following table. The **kind** option is used to specify whether the data will be downloaded to a file or a directory, and the **file** parameter specifies the target file or directory for the download. For details, please refer to [Application Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file).

The value contains all types in the following table.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

{ kind: 'file'; file: [TargetFileCallback](#section205374351176); }

 | 

The value of the key **kind** is **file** and the value of the key **file** is [TargetFileCallback](#section205374351176).

 |
| 

{ kind: 'file'; file: [Path](#section173755717538); keepLocal?: boolean; }

 | 

The value of the key **kind** is **file** and the value of the key **file** is a [Path](#section173755717538) object. **keepLocal** is optional, indicating whether to download a file with the same name as that of a local file that already exists.

 |
| 

{ kind: 'file'; file: [LocalFile](#section19493339161418)| [WriteFile](#section1372525722415); }

 | 

The value of the key **kind** is **file** and the value of the key **file** is a [LocalFile](#section19493339161418) or [WriteFile](#section1372525722415) object.

 |
| 

{ kind: 'folder'; path: [Path](#section173755717538); keepLocal?: boolean; }

 | 

The value of the key **kind** is **folder** and the value of the key **path** is a [Path](#section173755717538) object. **keepLocal** is optional, indicating whether to download a file folder with the same name as that of a local file folder that already exists.

 |

#### DownloadToStream

type DownloadToStream = { kind: 'stream'; stream: Stream | WriteStream | SyncWriteStream; }

Downloads a file to a data stream.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

{ kind: 'stream'; stream: [Stream](#section17454218451)| [WriteStream](#section113874918253)| [SyncWriteStream](#section27539206460) }

 | 

The value of the key **kind** is **stream** and the value of the key **stream** is:

[Stream](#section17454218451), [WriteStream](#section113874918253), or [SyncWriteStream](#section27539206460) object

 |

#### PausePolicy

Defines the request suspension policy.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

receiving

 | 

[ReceivingPausePolicy](#section0636945286)

 | 

No

 | 

Yes

 | 

Policy for suspending response body reception.

 |
| 

sending

 | 

[SendingPausePolicy](#section6701585215)

 | 

No

 | 

Yes

 | 

Policy for suspending request body sending.

 |

#### ReceivingPauseByTimeout

Defines the policy for suspending request reception by timeout.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'timeout'

 | 

No

 | 

No

 | 

Policy type.

 |
| 

timeoutMs

 | 

number

 | 

No

 | 

No

 | 

Timeout interval, in milliseconds. If the framework does not receive data from the server within the timeout interval, requests are suspended.

 |

#### ReceivingPauseByCache

Defines the policy for suspending request reception by cached data size.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'cacheSize'

 | 

No

 | 

No

 | 

Policy type.

 |
| 

size

 | 

number

 | 

No

 | 

No

 | 

Maximum cached data size. If the cached data size reaches this value, requests are suspended. Value range: \[0, 1048576\]

 |

#### ReceivingPausePolicy

type ReceivingPausePolicy = ReceivingPauseByCache | ReceivingPauseByTimeout

Defines the policy for suspending request reception.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ReceivingPauseByCache](#section73638218812)

 | 

Maximum cache size of the suspension policy.

 |
| 

[ReceivingPauseByTimeout](#section46402018173)

 | 

Timeout interval of the suspension policy.

 |

#### NetworkOutputQueue

const NetworkOutputQueue: NetworkOutputQueueConstructor

Call **new NetworkInputQueue()** to create an [INetworkOutputQueue](#section13239201618464).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### NetworkOutputQueueConstructor

**NetworkOutputQueueConstructor** is a constructor of [INetworkOutputQueue](#section13239201618464).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]new

new (): INetworkOutputQueue

Creates an [INetworkOutputQueue](#section13239201618464).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[INetworkOutputQueue](#section13239201618464)

 | 

Synchronous read queue object.

 |

#### \[h2\]new

new (maxSize: number): INetworkOutputQueue

Creates an [INetworkOutputQueue](#section13239201618464).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

maxSize

 | 

number

 | 

Yes

 | 

Queue size, which indicates the maximum number of bytes that can be written.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[INetworkOutputQueue](#section13239201618464)

 | 

Synchronous read queue object.

 |

#### \[h2\]new

new (maxSize: number, pausePolicyOverride: ReceivingPausePolicy): INetworkOutputQueue

Creates an [INetworkOutputQueue](#section13239201618464).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

maxSize

 | 

number

 | 

Yes

 | 

Queue size, which indicates the maximum number of bytes that can be written.

 |
| 

pausePolicyOverride

 | 

[ReceivingPausePolicy](#section0636945286)

 | 

Yes

 | 

Policy for suspending request reception.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[INetworkOutputQueue](#section13239201618464)

 | 

Synchronous read queue object.

 |

#### INetworkOutputQueue

Defines a read queue for synchronously reading response bodies, which is constructed using new [NetworkOutputQueue](#section165642074433)().

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]read

read(maxBytesToRead: number): ArrayBuffer

Reads a data segment from a queue.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

maxBytesToRead

 | 

number

 | 

Yes

 | 

Maximum number of bytes to read.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

ArrayBuffer

 | 

Binary data that is read.

 |

#### \[h2\]readInto

readInto(buffer: ArrayBuffer): number

Reads data from the queue and stores the data in the specified buffer.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

Buffer to which data is read.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Number of bytes in the read binary data.

 |

#### \[h2\]getStoredBytes

getStoredBytes(): number

Obtains the size of the data in the queue.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Obtains the size of the data in the queue.

 |

#### ResponseBodyDestination

type ResponseBodyDestination = 'array-buffer'| IncomingDataCallback | DownloadToFile | DownloadToStream | INetworkOutputQueue

Sets the destination of a response, so the HTTP client can send response data to the destination.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'array-buffer'

 | 

Data of the ArrayBuffer type. By default, the response body is written to the memory.

 |
| 

[IncomingDataCallback](#section1421528202712)

 | 

Data of the [IncomingDataCallback](#section1421528202712) type. The response body is written to the callback function.

 |
| 

[DownloadToFile](#section298118136197)

 | 

Data of the [DownloadToFile](#section298118136197) type. The response body is written to a file.

 |
| 

[DownloadToStream](#section1790033215431)

 | 

Data of the [DownloadToStream](#section1790033215431) type. The response body is written to a custom stream.

 |
| 

[INetworkOutputQueue](#section13239201618464)

 | 

Data of the [INetworkOutputQueue](#section13239201618464) type. The response body is written to the queue.

 |

#### URLOrString

type URLOrString = [URL](#section66401230152412) | string

Union set of URL objects or strings representing URLs. It can be used as an input parameter of the HTTP/HTTPS address.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[URL](#section66401230152412)

 | 

URL object, which can be used as an input parameter of the HTTP/HTTPS address.

 |
| 

string

 | 

URL string, which can be used as an input parameter of the HTTP/HTTPS address.

 |

#### PathPreference

Makes settings about HTTP request path preferences. This setting is only for system reference and the final path is determined by the system.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'auto'

 | 

The system selects a path automatically.

 |
| 

'cellular'

 | 

The cellular network path is used.

 |

#### IpAddress

type IpAddress = string

IP address type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

IP address of the string type, which can be an IPv4 or IPv6 address.

 |

#### DnsServers

type DnsServers = IpAndPort\[\]

Sets the custom DNS server in **DnsConfiguration**. It provides a flexible way to define a list of IP addresses and associated port numbers.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[IpAndPort](#section842181319618)\[\]

 | 

[IpAndPort](#section842181319618) array. The array contains pairs of IP addresses and port number.

 |

#### IpAndPort

Defines IP addresses and mapping port numbers in scenarios where the pairs of IP addresses and port numbers need to be specified, such as DNS server customization in the **DnsServers** API.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

ip

 | 

[IpAddress](#section1489910532316)

 | 

No

 | 

No

 | 

IP address to be associated, which is an IPv4 or IPv6 address.

 |
| 

port

 | 

number

 | 

No

 | 

Yes

 | 

Mapping port number. The value ranges from 0 to 65535. The default value is **53**.

 |

#### ServiceType

type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser'

Defines the network service type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'default'

 | 

Default service type. This type is suitable for most general service requirements.

NOTE:

All options except **default** are new options in version 5.0.0(12).

 |
| 

'background'

 | 

Background service type. This type is suitable for tasks running in the background, including scheduled tasks, background data synchronization, and notification push.

 |
| 

'realtimeVoice'

 | 

Real-time voice service type. This type is suitable for real-time voice services such as voice call, video conference, and instant call.

 |
| 

'realtimeVideo'

 | 

Real-time video service type. This type is suitable for real-time video services.

 |
| 

'callSignaling'

 | 

Signaling service type. This type is suitable for transmitting and managing call signaling in calls, including call setup, disconnection, and transfer.

 |
| 

'realtimeGame'

 | 

Real-time game service type. This type is suitable for real-time multi-player games that need to prioritize low latency and high reliability to ensure smooth and synchronized gameplay experiences for all players.

 |
| 

'normalGame'

 | 

Common game service type. This type is suitable for non-real-time game services, such as single-player games, offline games, and non-battle games.

 |
| 

'shortVideo'

 | 

Short video service type. This type is suitable for uploading, downloading, and playing short videos.

 |
| 

'longVideo'

 | 

Long video service type. This type is suitable for long video services.

 |
| 

'livestreamingAnchor'

 | 

Live TV playback control service type. This type is suitable for the streamer end of live streaming platforms.

 |
| 

'livestreamingWatcher'

 | 

Live TV playback service type. This type is suitable for the viewer end of live streaming platforms.

 |
| 

'download'

 | 

Download service type. This type is suitable for resource download services.

 |
| 

'upload'

 | 

Upload service type. This type is suitable for resource upload services.

 |
| 

'browser'

 | 

Browser service type. This type is suitable for web page loading and interaction in a browser.

 |

#### HttpMethod

type HttpMethod = 'GET' | 'POST' | 'HEAD' | 'PUT' | 'DELETE' | 'PATCH' | 'OPTIONS' | (string & NonNullable<unknown>)

Represents various HTTP methods used in network requests. An HTTP method defines the operation to be performed on a specified resource.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'GET'

 | 

GET network request method. This method is used to obtain data such as web pages, images, and API data from the server.

 |
| 

'POST'

 | 

POST network request method. This method is used to submit data such as forms and files to the server.

 |
| 

'HEAD'

 | 

HEAD network request method. This method is similar to GET but only retrieves the header information of the resource without returning the resource body. It is usually used to check whether a resource exists and obtain the metadata of a resource.

 |
| 

'PUT'

 | 

PUT network request method. This method is usually used to update existing resources on the server.

 |
| 

'DELETE'

 | 

DELETE network request method. This method is usually used to delete existing resources on the server.

 |
| 

'PATCH'

 | 

PATCH network request method. This method is usually used to partially update existing resources on the server.

 |
| 

'OPTIONS'

 | 

OPTIONS network request method. This method is usually used to query the communication options of a target resource and is commonly used in cross-domain requests to determine the HTTP methods supported by the server.

 |
| 

(string & NonNullable<unknown>)

 | 

Option used to ensure that the value of the HttpMethod type is a non-empty string.

 |

#### RequestHeaders

type RequestHeaders = { \[k: string\]: string | string\[\] | undefined; 'authorization'?: string; 'accept'?: ContentType | ContentType\[\]; 'accept-charset'?: string | string\[\]; 'accept-encoding'?: ContentCoding | ContentCoding\[\]; 'accept-language'?: string | string\[\]; 'cache-control'?: string | string\[\]; 'cookie'?: string | string\[\]; 'range'?: string | string\[\]; 'upgrade'?: string | string\[\]; 'user-agent'?: string; 'content-type'?: ContentType; }

Defines the request header type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

{ \[k: string\]: string | string\[\] | undefined;

'authorization'?: string;

'accept'?: [ContentType](#section535112587019) | [ContentType](#section535112587019)\[\];

'accept-charset'?: string | string\[\];

'accept-encoding'?: [ContentCoding](#section2719142017119) | [ContentCoding](#section2719142017119)\[\];

'accept-language'?: string | string\[\];

'cache-control'?: string | string\[\];

'cookie'?: string | string\[\];

'range'?: string | string\[\];

'upgrade'?: string | string\[\];

'user-agent'?: string;

'content-type'?: [ContentType](#section535112587019); }

 | 

If the key is **\[k: string\]: string | string\[\] | undefined**, the value contains one or more key-value pairs. In a key-value pair, the key can be any string and the value can be a string, string array, or **undefined**.

If the key is **authorization**, the value can be any string.

If the key is **accept**, the value can be any value of the [ContentType](#section535112587019) or [ContentType](#section535112587019) type.

If the key is **accept-charset**, the value can be any string or string array.

If the key is **accept-encoding**, the value can be any value of the [ContentCoding](#section2719142017119) or [ContentCoding](#section2719142017119) type.

If the key is **accept-language**, the value can be any string or string array.

If the key is **cache-control**, the value can be any string or string array.

If the key is **cookie**, the value can be any string or string array.

If the key is **range**, the value can be any string or string array.

If the key is **upgrade**, the value can be any string or string array.

If the key is **user-agent**, the value can be any string.

If the key is **content-type**, the value can be any value of the [ContentType](#section535112587019) type.

 |

#### SendingPausePolicy

Defines the policy for suspending request sending.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'timeout'

 | 

No

 | 

No

 | 

Policy type.

 |
| 

timeoutMs

 | 

number

 | 

No

 | 

No

 | 

Timeout interval, in milliseconds. If the framework does not receive data from the app within the timeout interval, requests are suspended.

 |

#### NetworkInputQueue

const NetworkInputQueue: NetworkInputQueueConstructor

Calls **new NetworkInputQueue()** to create an [INetworkInputQueue](#section882732713562).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### NetworkInputQueueConstructor

Constructs an [INetworkInputQueue](#section882732713562).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]new

new (): INetworkInputQueue

Creates an [INetworkInputQueue](#section882732713562).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[INetworkInputQueue](#section882732713562)

 | 

Synchronous write queue object.

 |

#### \[h2\]new

new (maxSize: number): INetworkInputQueue

Creates an [INetworkInputQueue](#section882732713562).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

maxSize

 | 

number

 | 

Yes

 | 

Queue size, which indicates the maximum number of bytes that can be written.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[INetworkInputQueue](#section882732713562)

 | 

Synchronous write queue object.

 |

#### \[h2\]new

new (maxSize: number, pausePolicyOverride: SendingPausePolicy): INetworkInputQueue

Creates an [INetworkInputQueue](#section882732713562).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

maxSize

 | 

number

 | 

Yes

 | 

Queue size, which indicates the maximum number of bytes that can be written.

 |
| 

pausePolicyOverride

 | 

[SendingPausePolicy](#section6701585215)

 | 

Yes

 | 

Policy for suspending request sending.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[INetworkInputQueue](#section882732713562)

 | 

Synchronous write queue object.

 |

#### INetworkInputQueue

Defines a write queue for synchronously writing request bodies, which is constructed using new [NetworkInputQueue](#section127952271692)().

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]write

write(buffer: string | ArrayBuffer): void

Writes a data segment to the queue, which will be sent by an I/O thread of the framework at a proper time.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

string | ArrayBuffer

 | 

Yes

 | 

Request to be sent.

 |

#### \[h2\]close

close(): void

Closes the synchronous write queue. Then an I/O thread no longer reads data from the queue.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]getFreeSpace

getFreeSpace(): number

Obtains the remaining writable space.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Remaining writable space.

 |

#### RequestContent

type RequestContent = RawDataContent | Form | MultipartForm | GetDataCallback | UploadFromFile | UploadFromStream | INetworkInputQueue

Represents the content of an HTTP request. It supports various forms that to send data based on service needs.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[RawDataContent](#section12323181618910)

 | 

Defines basic data types of ArkTs.

 |
| 

[Form](#section1188301010515)

 | 

Defines HTTP simple form data.

 |
| 

[MultipartForm](#section1420174317517)

 | 

Defines HTTP multi-part form data.

 |
| 

[GetDataCallback](#section78781933114)

 | 

Obtains any data. The input parameter is the maximum number of bytes allowed.

 |
| 

[UploadFromStream](#section187981940151318)

 | 

Uploads a file in stream mode.

**Start version**: 5.0.0(12)

 |
| 

[UploadFromFile](#section1753162618375)

 | 

Uploads a file from the client to the server.

**Start version**: 5.0.0(12)

 |
| 

[INetworkInputQueue](#section882732713562)

 | 

Defines a write queue for synchronously writing request bodies,

**Start version**: 5.0.0(12)

 |

#### Form

Defines HTTP simple form data.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fields

 | 

[FormFields](#section16427123712526)

 | 

No

 | 

No

 | 

HTTP simple form data fields.

 |
| 

keys

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Sequence in which keys in the form are sent.

If this parameter is set, the keys are sent based on this sequence list. Keys not in the list are not sent. If this parameter is not set, the default sending order follows the hash sequence of each key.

**Start version**: 6.0.1(21)

 |

#### \[h2\]constructor

constructor(fields: FormFields)

Provides the constructor used to create a **Form** object.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fields

 | 

[FormFields](#section16427123712526)

 | 

Yes

 | 

HTTP simple form data fields.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };

const simpleForm = new rcp.Form({
  "key1": "value1",
  "key2": \["valueList0", "valueList1"\],
});
simpleForm.keys = \["key2", "key1"\];
let req = new rcp.Request("http://example.com", "POST", headers, simpleForm, cookies, transferRange, configuration);
req.content = simpleForm;

#### MultipartForm

Defines HTTP multi-part form data.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fields

 | 

[MultipartFormFields](#section103661472920)

 | 

No

 | 

No

 | 

HTTP multi-part form data fields.

 |
| 

boundary

 | 

string

 | 

No

 | 

Yes

 | 

Custom separator for an HTTP multi-part form. You can customize the **boundary** field to accurately separate and transfer form data when uploading a multi-part form. The **boundary** field cannot exceed 46 characters. Otherwise, a parameter error code will be reported.

**Start version**: 5.1.0(18)

 |
| 

keys

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Key sequence in multi-part form data.

If this parameter is set, the keys are sent based on this sequence list. Keys not in the list are not sent. If this parameter is not set, the default sending order follows the hash sequence of each key.

**Start version**: 6.0.1(21)

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |

#### \[h2\]constructor

constructor(fields: MultipartFormFields)

Provides the constructor used to create a **MultipartForm** object.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fields

 | 

[MultipartFormFields](#section103661472920)

 | 

Yes

 | 

HTTP multi-part form data fields.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };

const multiForm = new rcp.MultipartForm({
  "key1": "value1",
  "key2": \["valueList0", "valueList1"\],
  "key3": {
    contentType: "text/plain",
    remoteFileName: "RemoteFileName",
    contentOrPath: "/file/to/Path",
  },
});
multiForm.keys = \["key3", "key1", "key2"\];
let req = new rcp.Request("http://example.com", "POST", headers, multiForm, cookies, transferRange, configuration);
req.content = multiForm;

#### \[h2\]constructor

constructor(fields: MultipartFormFields, boundary: string)

Provides the constructor used to create a **MultipartForm** object.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.1.0(18)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fields

 | 

[MultipartFormFields](#section103661472920)

 | 

Yes

 | 

HTTP multi-part form data fields.

 |
| 

boundary

 | 

string

 | 

Yes

 | 

Custom separator for an HTTP multi-part form. You can customize the **boundary** field to accurately separate and transfer form data when uploading a multi-part form.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

let headers: rcp.RequestHeaders = {
  "accept": "application/json"
};
let configuration: rcp.Configuration = {
  transfer: {
    timeout: { connectMs: 60000, transferMs: 60000 }
  }
};
let cookies: rcp.RequestCookies = { 'name1': 'value1', 'name2': 'value2' };
let transferRange: rcp.TransferRange = { from: 100, to: 200 };
let Boundary: string = "--MULTIPARTFORM BEGIN AND END BOUNDARY"

const multiForm = new rcp.MultipartForm({
  "key1": "value1",
  "key2": \["valueList0", "valueList1"\],
  "key3": {
    contentType: "text/plain",
    remoteFileName: "RemoteFileName",
    contentOrPath: "/file/to/Path",
  },
}, Boundary)
multiForm.keys = \["key3", "key1", "key2"\];

let req = new rcp.Request("http://example.com", "POST", headers, multiForm, cookies, transferRange, configuration);
req.content = multiForm;

#### MultipartFormFields

type MultipartFormFields = { \[k: string\]: MultipartFormFieldValue | MultipartFormFieldValue\[\]; }

Defines fields in the HTTP multi-part form.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

{ \[k: string\]: [MultipartFormFieldValue](#section7241730104213) | [MultipartFormFieldValue](#section7241730104213)\[\] }

 | 

[MultipartFormFieldValue](#section7241730104213) or [MultipartFormFieldValue](#section7241730104213) array, indicating any multi-part form field or an array of multi-part form fields, respectively.

 |

#### MultipartFormFieldValue

type MultipartFormFieldValue = FormFieldValue | FormFieldFileValue

Defines the values of fields in the HTTP multi-part form.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[FormFieldValue](#section620319167532)

 | 

[FormFieldValue](#section620319167532) type, indicating a field value in the HTTP simple form.

 |
| 

[FormFieldFileValue](#section1497311813556)

 | 

[FormFieldFileValue](#section1497311813556) type, indicating file form data.

 |

#### FormFields

type FormFields = { \[k: string\]: FormFieldValue | FormFieldValue\[\]; }

Defines fields in the HTTP simple form.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

{ \[k: string\]: [FormFieldValue](#section620319167532) | [FormFieldValue](#section620319167532)\[\] }

 | 

HTTP multi-part form data field or field array.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

const simpleForm: rcp.FormFields = {
  "key1": "value1",
  "key2": \["valueList0", "valueList1"\],
};

#### FormFieldValue

type FormFieldValue = string | number | boolean | bigint

Defines the values of fields in the HTTP simple form.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Field value of the string type.

 |
| 

number

 | 

Field value of the number type, which can be an integer or a floating point number. If the input value is greater than 2147483647, use the big integer type.

 |
| 

boolean

 | 

Field value of the Boolean type.

 |
| 

bigint

 | 

Field value of the big integer type. Use this type to input integers greater than 32 bits.

 |

#### Path

type Path = string

Defines the file path type in the HTTP form data.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

String type. The value can be any string.

 |

#### FileContent

Defines the file content type in the HTTP form data.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

content

 | 

string | ArrayBuffer

 | 

No

 | 

No

 | 

Content to be sent to the remote server. It can be any value.

 |

#### FormFieldFileValue

Defines file form data.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

contentType

 | 

[ContentType](#section535112587019)

 | 

No

 | 

Yes

 | 

Content type of HTTP multi-part form data. The default value is **undefined**.

 |
| 

remoteFileName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the file saved to a remote server. The default value is **undefined**.

 |
| 

contentOrPath

 | 

[Path](#section173755717538) | [FileContent](#section1126712263547) | [GetDataCallback](#section78781933114)

 | 

No

 | 

No

 | 

Content or path of the file to be sent to a remote server.

 |

**Example**

import { rcp } from '@kit.RemoteCommunicationKit';

const formFieldFileValue: rcp.FormFieldFileValue = {
  contentType: "image/png",
  remoteFileName: "remoteFile1",
  contentOrPath: "/path/to/file",
};

#### RequestCookies

Defines cookies in an HTTP request.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

\[name: string\]

 | 

string

 | 

No

 | 

No

 | 

Cookies data.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

const cookies: rcp.RequestCookies = {
  "sessionID": "abc123",
  "userToken": "xyz789",
  // Additional cookies can be added here
};

#### TransferRange

Sets the data transmission range. An HTTP request with this data requires the server to return only a part of the HTTP response.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

from

 | 

number

 | 

No

 | 

Yes

 | 

Start byte of the data to be transmitted. The default value is **undefined**.

 |
| 

to

 | 

number

 | 

No

 | 

Yes

 | 

End byte of the data to be transmitted. The default value is **undefined**.

 |

#### Response

Response to an HTTP request.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

Yes

 | 

No

 | 

HTTP request content to which the response is returned.

 |
| 

statusCode

 | 

number

 | 

Yes

 | 

No

 | 

Result code of an HTTP request. If the callback function is successfully executed, the result code defined in **ResponseCode** is returned. Otherwise, an error code is returned in the **error** field in **AsyncCallback**.

 |
| 

headers

 | 

[ResponseHeaders](#section253714181004)

 | 

Yes

 | 

No

 | 

Response header.

 |
| 

effectiveUrl

 | 

[URL](#section66401230152412)

 | 

Yes

 | 

Yes

 | 

Valid URL to which a request is redirected. The default value is **undefined**.

 |
| 

body

 | 

ArrayBuffer

 | 

Yes

 | 

Yes

 | 

The response content aligns with **Content-type** in the response header. The response content must be of the same data type returned by the server. The default maximum download byte limit is 50 MB. If the size exceeds 50 MB, to mitigate memory overflow, you need to stream the data using [OnDataReceive](#section9264115918536).

 |
| 

downloadedTo

 | 

[DownloadedTo](#section1166941712103)

 | 

Yes

 | 

Yes

 | 

Path for downloading content. When downloading to a file object or using a file descriptor, no callback information is set by default.

**Start version**: 5.0.0(12)

 |
| 

debugInfo

 | 

[DebugInfo](#section175663117434)\[\]

 | 

Yes

 | 

Yes

 | 

Debugging information associated with a response. The default value is **undefined**.

 |
| 

timeInfo

 | 

[TimeInfo](#section183911041803)

 | 

Yes

 | 

Yes

 | 

Timer information in each phase of HTTP request processing. The default value is **undefined**.

 |
| 

cookies

 | 

[ResponseCookie](#section295119276014)\[\]

 | 

Yes

 | 

Yes

 | 

Cookie array in a response.

 |
| 

httpVersion

 | 

[HttpVersion](#section14719175117590)

 | 

Yes

 | 

Yes

 | 

HTTP version.

**Start version**: 5.0.0(12)

 |
| 

reasonPhrase

 | 

string

 | 

Yes

 | 

Yes

 | 

**reasonPhrase** of an HTTP status line, which provides a descriptive message associated with a numerical status code.

**Start version**: 5.0.0(12)

 |
| 

cacheInfo

 | 

[CacheInfo](#section19758103145620)

 | 

Yes

 | 

Yes

 | 

Cache information, including the cache duration and original HTTP request ID. This attribute has a value only when an HTTP response is obtained from the cache. Otherwise, the value is **undefined**.

**Start version**: 6.0.0(20)

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

// The following describes how to modify the response, which is for reference only.
interface ChangeableResponse {
  request: rcp.Request;
  statusCode: number;
  headers: rcp.ResponseHeaders;
  effectiveUrl?: rcp.URL;
  body?: ArrayBuffer;
  downloadedTo?: rcp.DownloadedTo;
  debugInfo?: rcp.DebugInfo\[\];
  timeInfo?: rcp.TimeInfo;
  cookies?: rcp.ResponseCookie\[\];
  httpVersion?: rcp.HttpVersion;
  reasonPhrase?: string;
  cacheInfo?: rcp.CacheInfo;
}

async function TestRcp() {
  const session = rcp.createSession();
  const resp = await session.get('https://www.example.com');
  const changeableResponse = resp as ChangeableResponse;
 changeableResponse.headers = HEADERS // Define this information based on your service needs.
 changeableResponse.statusCode = STATUSCODE // Define this information based on your service needs.
}

#### \[h2\]toString

toString(): string | null

Converts a response body into a character string. If the conversion fails, null is returned.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string | null

 | 

UTF-8 character string (if the HTTP response body is not in UTF-8 format) or null value.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
const request = new rcp.Request("https://www.example.com");
session.fetch(request).then((response: rcp.Response) => {
  if (response) {
    console.info("response: " + response.toString());
  }
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### \[h2\]toJSON

toJSON(): object | null

Returns the default JSON deserialization result. For details about how to customize the JSON deserialization mode, please refer to [JSON Parsing and Generation](../../../../../application-framework/arkts/arkts-apis/ohos-util-json-json-parsing-and-generation/document.md).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

object | null

 | 

JSON character string containing **toString()** (if no exception occurs) or null value (if the body is not in JSON format).

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { rcp } from '@kit.RemoteCommunicationKit';

const session = rcp.createSession();
const request = new rcp.Request("https://www.example.com");
session.fetch(request).then((response: rcp.Response) => {
  if (response) {
    console.info("response: ", response.toJSON());
  }
}).catch((err: BusinessError) => {
  console.error(\`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
});

#### ResponseSendable

Defines HTTP response data, which conforms to the Sendable protocol.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

Yes

 | 

No

 | 

Sequence number of the request to be sent.

 |
| 

statusCode

 | 

number

 | 

Yes

 | 

No

 | 

Status code of the HTTP request.

 |
| 

headers

 | 

[ResponseHeaders](#section253714181004)

 | 

Yes

 | 

No

 | 

Response header.

 |
| 

effectiveUrl

 | 

string

 | 

Yes

 | 

Yes

 | 

Valid URL to which a request is redirected, which is a character string. The default value is **undefined**.

 |
| 

body

 | 

ArrayBuffer

 | 

Yes

 | 

Yes

 | 

The response content is returned based on **content-type** in the response header and must match the data type returned by the server.

 |
| 

downloadedTo

 | 

[DownloadedTo](#section1166941712103)

 | 

Yes

 | 

Yes

 | 

Path for downloading content. When downloading to a file object or using a file descriptor, no callback information is set by default.

 |
| 

debugInfo

 | 

[DebugInfo](#section175663117434)\[\]

 | 

Yes

 | 

Yes

 | 

Debugging information associated with a response. The default value is **undefined**.

 |
| 

timeInfo

 | 

[TimeInfo](#section183911041803)

 | 

Yes

 | 

Yes

 | 

Timer information in each phase of HTTP request processing. The default value is **undefined**.

 |
| 

cookies

 | 

[ResponseCookie](#section295119276014)\[\]

 | 

Yes

 | 

Yes

 | 

Cookie array in a response.

 |
| 

httpVersion

 | 

[HttpVersion](#section14719175117590)

 | 

Yes

 | 

Yes

 | 

HTTP version.

 |
| 

reasonPhrase

 | 

string

 | 

Yes

 | 

Yes

 | 

Text description about an HTTP request status code.

 |
| 

cacheInfo

 | 

[CacheInfo](#section19758103145620)

 | 

Yes

 | 

Yes

 | 

Cache information, including the cache duration and original HTTP request ID. This attribute has a value only when an HTTP response is obtained from the cache. Otherwise, the value is **undefined**.

 |

#### ResponseHeaders

type ResponseHeaders = { \[k: string\]: string | string\[\] | undefined; 'accept-ranges'?: 'none' | 'bytes' | (string & NonNullable<unknown>); 'allow'?: HttpMethod | HttpMethod\[\]; 'cache-control'?: string | string\[\]; 'content-encoding'?: ContentCoding; 'content-range'?: string; 'content-type'?: ContentType; 'date'?: string; 'etag'?: string; 'expires'?: string; 'location'?: string; 'retry-after'?: string; 'set-cookie'?: string | string\[\]; 'server'?: string; 'www-authenticate'?: string | string\[\]; }

Defines the response header type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

{ \[k: string\]: string | string\[\] | undefined;

'accept-ranges'?: 'none' | 'bytes' | (string & NonNullable<unknown>);

'allow'?: HttpMethod | HttpMethod\[\];

'cache-control'?: string | string\[\];

'content-encoding'?: ContentCoding;

'content-range'?: string;

'content-type'?: ContentType;

'date'?: string;

'etag'?: string;

'expires'?: string;

'location'?: string;

'retry-after'?: string;

'set-cookie'?: string | string\[\];

'server'?: string;

'www-authenticate'?: string | string\[\]; }

 | 

If the key is **\[k: string\]: string | string\[\] | undefined**, the value contains one or more key-value pairs. In a key-value pair, the key can be any string and the value can be a string, string array, or **undefined**.

**accept-ranges** indicates the **accept-ranges** data in the response header.

If the key is **allow**, the value can be any value of the **HttpMethod** or **HttpMethod\[\]** type.

If the key is **cache-control**, the value can be any string or string array.

If the key is **content-encoding**, the value can be any value of the **ContentCoding** type.

If the key is **content-range**, the value can be any string.

If the key is **content-type**, the value can be any value of the **ContentType** type.

If the key is **date**, the value can be any string.

If the key is **etag**, the value can be any string.

If the key is **expires**, the value can be any string.

If the key is **location**, the value can be any string.

If the key is **retry-after**, the value can be any string.

If the key is **set-cookie**, the value can be any string or string array.

If the key is **server**, the value can be any string.

If the key is **www-authenticate**, the value can be any string or string array.

 |

#### ResponseCookie

Defines cookies in an HTTP response.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Cookie name.

 |
| 

value

 | 

string

 | 

No

 | 

Yes

 | 

Cookie value.

 |
| 

domain

 | 

string

 | 

No

 | 

Yes

 | 

Cookie domain name.

 |
| 

path

 | 

string

 | 

No

 | 

Yes

 | 

Cookie path.

 |
| 

expires

 | 

string

 | 

No

 | 

Yes

 | 

Cookie expiration date.

 |
| 

maxAge

 | 

number

 | 

No

 | 

Yes

 | 

Maximum storage duration of cookies, in seconds.

 |
| 

isSecure

 | 

true

 | 

No

 | 

Yes

 | 

Indicates whether cookies can be sent only through secure connections. The default value is **true**.

 |
| 

httpOnly

 | 

true

 | 

No

 | 

Yes

 | 

Indicates whether cookies can be accessed only through HTTP requests. The default value is **true**.

 |
| 

sameSite

 | 

string

 | 

No

 | 

Yes

 | 

Specifies when cookies are sent in cross-site requests.

 |
| 

rawSize

 | 

number

 | 

No

 | 

Yes

 | 

Cookie size.

 |
| 

cookieAttributes

 | 

[CookieAttributes](#section162175111013)

 | 

No

 | 

Yes

 | 

All attributes in the response cookies.

 |

#### DebugInfo

Processes debugging information in a request/response.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[DebugEvent](#section1295195318118)

 | 

No

 | 

No

 | 

Debugging information type.

 |
| 

data

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Debugging information.

 |

#### HttpVersion

type HttpVersion = '1.0' | '1.1' | '2' | '3' | 'unknown'

Defines the HTTP version.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'1.0'

 | 

HTTP version 1.0. The value is a character string.

 |
| 

'1.1'

 | 

HTTP version 1.1. The value is a character string.

 |
| 

'2'

 | 

HTTP version 2. The value is a character string.

 |
| 

'3'

 | 

HTTP version 3. The value is a character string.

 |
| 

'unknown'

 | 

Unknown HTTP version. The value is a character string.

 |

#### TimeInfo

Defines time-related information for HTTP network requests in each request phase.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

nameLookupTimeMs

 | 

number

 | 

No

 | 

No

 | 

Time required for DNS resolution, in milliseconds.

 |
| 

connectTimeMs

 | 

number

 | 

No

 | 

No

 | 

Connection setup time, in milliseconds.

 |
| 

tlsHandshakeTimeMs

 | 

number

 | 

No

 | 

No

 | 

Time elapsed till the TLS handshake with the remote host or proxy server, in milliseconds.

**Start version**: 5.0.0(12)

 |
| 

preTransferTimeMs

 | 

number

 | 

No

 | 

No

 | 

Time elapsed till the transmission starts, in milliseconds.

 |
| 

startTransferTimeMs

 | 

number

 | 

No

 | 

No

 | 

Transmission start time, in milliseconds.

 |
| 

totalTimeMs

 | 

number

 | 

No

 | 

No

 | 

Total duration of a request, in milliseconds.

 |
| 

redirectTimeMs

 | 

number

 | 

No

 | 

No

 | 

Time required for redirection, in milliseconds.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/cxXIzahcTcuTRwFHowbnrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062351Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DF6246BBB4C8BF4900FF636C34000B17C3C9354CE8764417DC2C1B00791B373)

TimeInfo timeline: request initiation (time 0) -> nameLookupTimeMs (DNS resolution) -> connectTimeMs (connection establishment) -> tlsHandshakeTimeMs (TLS handshake) -> data request arriving at the server (preTransferTimeMs) -> first packet received from the server (startTransferTimeMs). All time points are measured from the request initiation (0). For example, if **tlsHandshakeTimeMs** is 150.1ms, it means that the time taken from the request initiation (time 0) until the completion of the TLS handshake is 150.1 milliseconds.

Methods for calculating the durations of key phases in network requests are as follows:

-   First packet delivery duration: startTransferTimeMs – preTransferTimeMs
-   TLS handshake duration (excluding the connection setup time): tlsHandshakeTimeMs – connectTimeMs
-   Duration for receiving the remaining data: totalTimeMs – startTransferTimeMs

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1. Create a session and define the request URL.
const session = rcp.createSession();
const requestURL = "https://www.example.com";

// 2. To track and analyze the time consumed for each phase during a request, enable this switch.
const configuration: rcp.Configuration = {
  tracing: {
    collectTimeInfo: true
  }
}

// 3. Create a request.
const request = new rcp.Request(requestURL, "GET");
request.configuration = configuration;

// 4. Use FETCH to initiate a network request carrying the configuration.
session.fetch(request).then((response: rcp.Response) => {
// Parameters in timeInfo may be undefined. Therefore, before performing calculation based on any two parameters, add the logic to determine whether the parameters are undefined.
  if (!response.timeInfo) {
    console.error(\`TimeInfo is undefined ${response.timeInfo}\`);
    return;
  }
  let remainderDataTime = response.timeInfo?.totalTimeMs - response.timeInfo?.startTransferTimeMs;
  let firstPackageTime = response.timeInfo?.startTransferTimeMs - response.timeInfo?.preTransferTimeMs;
  let TLSTime = response.timeInfo?.tlsHandshakeTimeMs - response.timeInfo?.connectTimeMs;
  
  console.info(\`First packet delivery duration${firstPackageTime}\`);
  console.info(\`TLS handshake duration (excluding the connection setup time)${TLSTime}\`);
  console.info(\`Duration for receiving the remaining data${remainderDataTime}\`);
}).catch((err: BusinessError) => {
  console.error(\`Response err, the err is ${JSON.stringify(err)}\`);
})

#### CookieAttributes

type CookieAttributes = { \[k: string\]: string | undefined; }

Defines the cookie attribute type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

{ \[k: string\]: string | undefined; }

 | 

Object containing one or more key-value pairs. In a key-value pair, the key can be any string and the value can be any string or **undefined**.

 |

#### ContentType

type ContentType = 'application/json' | 'text/plain' | 'multipart/form-data' | 'application/octet-stream' | 'application/x-www-form-urlencoded' | (string & NonNullable<unknown>)

Defines the content type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'application/json'

 | 

**application/json**: The content is a JSON string.

 |
| 

'text/plain'

 | 

**text/plain**: The content is text.

 |
| 

'multipart/form-data'

 | 

**multipart/form-data**: The content is form data.

 |
| 

'application/octet-stream'

 | 

**application/octet-stream**: The content is a binary data stream.

 |
| 

'application/x-www-form-urlencoded'

 | 

**application/x-www-form-urlencoded**: The content is form data.

 |
| 

(string & NonNullable<unknown>)

 | 

**string & NonNullable<unknown>**: The content can be any non-empty string.

 |

#### ValidationContext

Defines the certificate context.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

pemCerts

 | 

string\[\]

 | 

No

 | 

No

 | 

PEM-format certificate.

 |
| 

x509Certs

 | 

[X509Cert](#section136572026194112)\[\]

 | 

No

 | 

No

 | 

X.509 certificate object.

 |
| 

host

 | 

string

 | 

No

 | 

No

 | 

Domain name of the server to which a connection is set up.

 |
| 

ip

 | 

string

 | 

No

 | 

No

 | 

IP address of the server to which a connection is set up.

 |

#### ValidationCallback

type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>

Defines the custom certificate validation function.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[ValidationContext](#section7263163111816)

 | 

Yes

 | 

Certificate context.

 |

**Returns**:

| 
Value Range

 | 

Description

 |
| :-- | :-- |
| 

boolean | Promise<boolean>

 | 

Boolean value that indicates whether the verification is successful, result returned using a promise, or **Promise.reject()** that indicates verification failure.

 |

#### TlsV13SpecificCipherSuite

type TlsV13SpecificCipherSuite = 'TLS\_AES\_128\_GCM\_SHA256' | 'TLS\_AES\_256\_GCM\_SHA384' | 'TLS\_CHACHA20\_POLY1305\_SHA256'

Cipher suite supported by TLS 1.3 or later. This framework has built-in cipher suite priorities, where custom options are also recorded.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'TLS\_AES\_128\_GCM\_SHA256'

 | 

Supported cipher suite: TLS\_AES\_128\_GCM\_SHA256. The value is a character string.

 |
| 

'TLS\_AES\_256\_GCM\_SHA384'

 | 

Supported cipher suite: TLS\_AES\_256\_GCM\_SHA384. The value is a character string.

 |
| 

'TLS\_CHACHA20\_POLY1305\_SHA256'

 | 

Supported cipher suite: TLS\_CHACHA20\_POLY1305\_SHA256. The value is a character string.

 |

#### TlsV12SpecificCipherSuite

type TlsV12SpecificCipherSuite = 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384' | 'TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | 'TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | 'TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | 'TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384';

Cipher suite supported by TLS 1.2 or later.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256'

 | 

Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256. The value is a character string.

 |
| 

'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256'

 | 

Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256. The value is a character string.

 |
| 

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384'

 | 

Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384. The value is a character string.

 |
| 

'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384'

 | 

Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384. The value is a character string.

 |
| 

'TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256'

 | 

Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256. The value is a character string.

 |
| 

'TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256'

 | 

Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256. The value is a character string.

 |
| 

'TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256'

 | 

Supported cipher suite: TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256. The value is a character string.

 |
| 

'TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384'

 | 

Supported cipher suite: TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384. The value is a character string.

 |

#### TlsV10SpecificCipherSuite

type TlsV10SpecificCipherSuite = 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA' | 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA' | 'TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA'

Cipher suite supported by TLS 1.0 or later.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA'

 | 

Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA. The value is a character string.

 |
| 

'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA'

 | 

Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA. The value is a character string.

 |
| 

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA'

 | 

Supported cipher suite: TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA. The value is a character string.

 |
| 

'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA'

 | 

Supported cipher suite: TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA. The value is a character string.

 |
| 

'TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA'

 | 

Supported cipher suite: TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA. The value is a character string.

 |
| 

'TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA'

 | 

Supported cipher suite: TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA. The value is a character string.

 |
| 

'TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA'

 | 

Supported cipher suite: TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA. The value is a character string.

 |

#### CipherSuite

type CipherSuite = TlsV13CipherSuite

Declares the cipher suite.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TlsV13CipherSuite](#section593594720197)

 | 

[TlsV13CipherSuite](#section593594720197) type.

 |

#### TlsV13CipherSuite

type TlsV13CipherSuite = TlsV12CipherSuite | TlsV13SpecificCipherSuite

Declares the cipher suite for TLS 1.3, which is also compatible with TLS 1.2.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TlsV12CipherSuite](#section79896219610)

 | 

[TlsV12CipherSuite](#section79896219610) type.

 |
| 

[TlsV13SpecificCipherSuite](#section3129163617819)

 | 

[TlsV13SpecificCipherSuite](#section3129163617819) type.

 |

#### TlsV12CipherSuite

type TlsV12CipherSuite = TlsV11CipherSuite | TlsV12SpecificCipherSuite

Declares the cipher suite for TLS 1.2, which is also compatible with TLS 1.1.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TlsV11CipherSuite](#section3358251787)

 | 

[TlsV11CipherSuite](#section3358251787) type.

 |
| 

[TlsV12SpecificCipherSuite](#section14955113664814)

 | 

[TlsV12SpecificCipherSuite](#section14955113664814) type.

 |

#### TlsV11CipherSuite

type TlsV11CipherSuite = TlsV10CipherSuite

Declares the cipher for TLS 1.1, which is the same as that of TLS 1.0.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TlsV10CipherSuite](#section1451210179125)

 | 

[TlsV10CipherSuite](#section1451210179125) type.

 |

#### TlsV10CipherSuite

type TlsV10CipherSuite = TlsV10SpecificCipherSuite

Declares the cipher suite for TLS 1.0.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TlsV10SpecificCipherSuite](#section18083613205)

 | 

[TlsV10SpecificCipherSuite](#section18083613205) type.

 |

#### TlsV13Option

TLS 1.3 selector function, which is used to select the TLS version and matching cipher suite.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tlsVersion

 | 

'TlsV1.3'

 | 

No

 | 

No

 | 

TLS 1.3.

 |
| 

cipherSuite

 | 

[TlsV13CipherSuite](#section593594720197)\[\]

 | 

No

 | 

Yes

 | 

Cipher suite for TLS 1.3.

 |

#### TlsV12Option

TLS 1.2 selector function, which is used to select the TLS version and matching cipher suite.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tlsVersion

 | 

'TlsV1.2'

 | 

No

 | 

No

 | 

TLS 1.2.

 |
| 

cipherSuite

 | 

[TlsV12CipherSuite](#section79896219610)\[\]

 | 

No

 | 

Yes

 | 

Cipher suite for TLS 1.2.

 |

#### TlsV11Option

TLS 1.1 selector function, which is used to select the TLS version and matching cipher suite.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tlsVersion

 | 

'TlsV1.1'

 | 

No

 | 

No

 | 

TLS 1.1.

 |
| 

cipherSuite

 | 

[TlsV11CipherSuite](#section3358251787)\[\]

 | 

No

 | 

Yes

 | 

Cipher suite for TLS 1.1.

 |

#### TlsV10Option

TLS 1.0 selector function, which is used to select the TLS version and matching cipher suite.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tlsVersion

 | 

'TlsV1.0'

 | 

No

 | 

No

 | 

TLS 1.0.

 |
| 

cipherSuite

 | 

[TlsV10CipherSuite](#section1451210179125)\[\]

 | 

No

 | 

Yes

 | 

Cipher suite for TLS 1.0.

 |

#### ContentCoding

type ContentCoding = 'aes128gcm' | 'br' | 'compress' | 'deflate' | 'exi' | 'gzip' | 'pack200-gzip' | 'x-compress' | 'x-gzip' | 'zstd' | (string & NonNullable<unknown>)

Pre-defines the content encoding type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Value Range

 | 

Description

 |
| :-- | :-- |
| 

'aes128gcm'

 | 

Encode content using the AES-128-GCM encryption algorithm for symmetric encryption.

 |
| 

'br'

 | 

Encode content using the Brotli algorithm, which is designed for high compression ratios, especially suitable for web pages and documents.

 |
| 

'compress'

 | 

Encode content using the Unix compress algorithm.

 |
| 

'deflate'

 | 

Encode content using the DEFLATE algorithm, which offers high compression ratios and relatively fast compression speeds.

 |
| 

'exi'

 | 

Encode content using the Efficient XML Interchange (EXI) format, which is designed for high compression ratios of XML data.

 |
| 

'gzip'

 | 

Encode content using the GZIP algorithm, which is a widely used compression method for web servers and apps.

 |
| 

'pack200-gzip'

 | 

Encode content using the Pack200 and GZIP algorithms.

 |
| 

'x-compress'

 | 

Encode content using Zlib's compress method.

 |
| 

'x-gzip'

 | 

Encode content using Zlib's gzip method, which employs the DEFLATE compression algorithm to achieve high compression ratios and fast compression speeds.

 |
| 

'zstd'

 | 

Encode content using the Zstandard algorithm, which is designed for high compression ratios, especially suitable for databases and files.

 |
| 

(string & NonNullable<unknown>)

 | 

Option used to ensure that the value of the ContentCoding type is a non-empty string.

 |

#### ResponseValidationCallback

type ResponseValidationCallback = (response: Response) => boolean | Promise<boolean>

Response verification callback function.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

response

 | 

[Response](#section156381815599)

 | 

Yes

 | 

Response transferred by the framework, which needs to be verified.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean | Promise<boolean>

 | 

Verification result, which can be returned directly or through a **Promise** object asynchronously. The options are **true** (successful) and **false** (failed).

 |

#### ProcessingConfiguration

Defines processing settings.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

validateResponse

 | 

'default' | [ResponseValidationCallback](#section1619313413298)

 | 

No

 | 

Yes

 | 

Response processing type. Either no processing is performed (default type) or [ResponseValidationCallback](#section1619313413298) is called to verify the response.

 |

#### GetDataCallback

type GetDataCallback = (maxSize: number) => ArrayBuffer | Promise<ArrayBuffer>

Obtains any data. The input parameter is the maximum number of bytes allowed.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

maxSize

 | 

number

 | 

Yes

 | 

Maximum number of bytes.

The returned value is an ArrayBuffer value returned directly or asynchronously using a promise. The return value can be any value of the ArrayBuffer type.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

ArrayBuffer

 | 

ArrayBuffer data containing the type of the obtained callback method.

 |
| 

Promise<ArrayBuffer>

 | 

Promise used to return the ArrayBuffer data. The data contains the type of the obtained callback method.

NOTE:

The return value **Promise<ArrayBuffer>** is newly added in version 5.0.0(12).

 |

#### DynamicExclusionRule

type DynamicExclusionRule = (url: URLOrString) => boolean

Obtains whether to exclude input URLs from proxy processing.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

Union set of URL objects or strings representing URLs.

Method whose input parameter type is [URLOrString](#section320653742718) and return value is of the boolean value. The return value is **true** or **false**.

 |

**Table 1** **Returns**:
| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether to use the proxy. The return value is **true** or **false**.

 |

#### StaticDnsRule

Represents a single static DNS rule that associates a specific IP address with a host name and a port number. This configuration is used in **StaticDnsRule** for defining DNS mapping information.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

host

 | 

string

 | 

No

 | 

No

 | 

Host name to which the static DNS rule is applied.

 |
| 

port

 | 

number

 | 

No

 | 

No

 | 

Port number to which the static DNS rule is applied. The value ranges from 0 to 65535.

 |
| 

ipAddresses

 | 

[IpAddress](#section1489910532316)\[\]

 | 

No

 | 

No

 | 

IP addresses to associate with the specified host name and port number.

 |

#### StaticDnsRules

type StaticDnsRules = StaticDnsRule\[\]

Associates specified IP addresses with host names and port numbers. This configuration applies to scenarios where IP mapping needs to be customized for specific domain names and port numbers.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[StaticDnsRule](#section47911616155511)\[\]

 | 

[StaticDnsRule](#section47911616155511) array.

 |

#### DynamicDnsRule

type DynamicDnsRule = (host: string, port: number) => IpAddress\[\]

Obtains IP addresses based on the specified host name and port number.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

host

 | 

string

 | 

Yes

 | 

Host name.

 |
| 

port

 | 

number

 | 

Yes

 | 

Port number.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[IpAddress](#section1489910532316)\[\]

 | 

An array of IP addresses.

 |

#### WebProxy

Defines custom proxy settings in [ProxyConfiguration](#section731665213712), including the proxy server URL, exclusions, and other security settings.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

No

 | 

No

 | 

Custom proxy server URL.

 |
| 

createTunnel

 | 

'auto' | 'always'

 | 

No

 | 

Yes

 | 

Indicates when a proxy tunnel needs to be established. Tunneling is a process where an HTTP CONNECT request is sent to a proxy server, instructing it to establish a connection to the remote host of a specified port number. Once this connection is set up, all subsequent traffic is routed through the proxy. The default value is **auto**.

**auto**: A tunnel will be created for HTTPS traffic but not for HTTP traffic.

**always**: Tunneling is enabled for all traffic.

 |
| 

exclusions

 | 

[URLOrString](#section320653742718) | [URLOrString](#section320653742718)\[\] | [DynamicExclusionRule](#section1037054954)

 | 

No

 | 

Yes

 | 

URLs to be excluded from proxy processing (for example, "[http://exclude.example.com](http://exclude.example.com/)" or \["[http://exclude1.com](http://exclude1.com/)", "[http://exclude2.com](http://exclude2.com/)"\]). The default value is **undefined**.

 |
| 

security

 | 

[SecurityConfiguration](#section1597118916425)

 | 

No

 | 

Yes

 | 

Proxy security settings. The default value is **undefined**.

 |

#### InfoToCollect

Collects detailed information events. The collected information events are returned in the **debugInfo** field of [Response](#section156381815599).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

textual

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect text events. The default value is **false**.

 |
| 

incomingHeader

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect header transfer-in events. The default value is **false**.

 |
| 

outgoingHeader

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect header transfer-out events. The default value is **false**.

 |
| 

incomingData

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect data transfer-in events. The default value is **false**.

 |
| 

outgoingData

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect data transfer-out events. The default value is **false**.

 |
| 

incomingSslData

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect SSL/TLS data transfer-in events. The default value is **false**.

 |
| 

outgoingSslData

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect SSL/TLS data transfer-out events. The default value is **false**.

 |
| 

srcAddr

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect client address information.

**true**: The client address and port number are collected.

**false**: The client address and port number are not collected.

The default value is **false**.

**Start version**: 6.0.0(20)

 |
| 

dstAddr

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to collect server address information.

**true**: The server address and port number are collected.

**false**: The server address and port number are not collected.

The default value is **false**.

**Start version**: 6.0.0(20)

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/e2wks42CSjC2Et8Fnku3jA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062351Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19C0BA6C94DB88B3AB62F089046449F0EF30C4CB54D69F688EE54694D3E53861)

This API will occupy memory resources. You are advised to call it only in the development and debugging phases.

#### HttpEventsHandler

Applies custom logic to handle various operations during HTTP request/response processing.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

onDataReceive

 | 

[OnDataReceive](#section9264115918536)

 | 

No

 | 

Yes

 | 

Callback triggered when a part of an HTTP response body is returned. The default value is **undefined**. Use this callback to receive data when the data size exceeds 50 MB. Then the **body** field of the returned [Response](#section156381815599) object will no longer contain data.

 |
| 

onUploadProgress

 | 

[OnUploadProgress](#section1596171465719)

 | 

No

 | 

Yes

 | 

Callback triggered to process the upload progress in a response. The default value is **undefined**.

 |
| 

onDownloadProgress

 | 

[OnDownloadProgress](#section832314187551)

 | 

No

 | 

Yes

 | 

Callback triggered to process the download progress in a response. The default value is **undefined**.

 |
| 

onHeaderReceive

 | 

[OnHeaderReceive](#section13232139165012)

 | 

No

 | 

Yes

 | 

Callback triggered to process headers received in a response. The default value is **undefined**.

 |
| 

onDataEnd

 | 

[OnDataEnd](#section1356075625115)

 | 

No

 | 

Yes

 | 

Callback triggered when data transfer is completed. The default value is **undefined**.

 |
| 

onCanceled

 | 

[OnCanceled](#section844405416446)

 | 

No

 | 

Yes

 | 

Callback triggered when a request or response is canceled. The default value is **undefined**.

 |
| 

onTimeInfo

 | 

[OnTimeInfo](#section254219518422)

 | 

No

 | 

Yes

 | 

Callback triggered when an HTTP request fails or succeeds. The default value is **undefined**.

**Start version**: 5.0.3(15)

 |
| 

onStatusCodeReceive

 | 

[OnStatusCodeReceive](#section829213325618)

 | 

No

 | 

Yes

 | 

Callback triggered to process the status code received in a response. The default value is **undefined**.

**Start version**: 6.0.0(20)

 |

#### Timeout

Defines HTTP request timeout settings for connection and data transmission.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

connectMs

 | 

number

 | 

No

 | 

Yes

 | 

Maximum duration for establishing a connection, in milliseconds. If the connection setup duration exceeds this limit, the connection times out. The default value is **60000**.

 |
| 

transferMs

 | 

number

 | 

No

 | 

Yes

 | 

Maximum duration for data transmission, in milliseconds. If the data transmission duration exceeds this limit, the transmission times out. The default value is **60000**.

 |
| 

inactivityMs

 | 

number

 | 

No

 | 

Yes

 | 

Maximum duration for allowing no data transmission or connection activity. This setting is used to prevent long-idle connections in cases where the time interval between receiving or sending data to the server cannot exceed a certain value. By default, no timeout is set, indicating that the duration is not limited.

**Start version**: 5.0.0(12)

 |

#### CertificatePinning

Verifies the authenticity of a server's certificate by comparing its public key's SHA-256 hash to a predefined value.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'public-key'

 | 

No

 | 

No

 | 

Certification verification type.

 |
| 

publicKeyHash

 | 

string

 | 

No

 | 

No

 | 

Public key hash.

 |
| 

hashAlgorithm

 | 

'SHA-256'

 | 

No

 | 

No

 | 

Algorithm used to calculate the public key hash value.

 |

#### SessionListener

Defines a session listener.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

onCanceled

 | 

[OnCanceled](#section844405416446)

 | 

No

 | 

Yes

 | 

Callback triggered when a session is canceled. The default value is **undefined**.

 |
| 

onClosed

 | 

[OnClosed](#section334964220501)

 | 

No

 | 

Yes

 | 

Callback triggered when a session is closed. The default value is **undefined**.

 |

#### Credential

Represents the credential used for server identity verification in a session, including the user name and password.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

username

 | 

string

 | 

No

 | 

No

 | 

User name used for verification. It is left empty by default.

 |
| 

password

 | 

string

 | 

No

 | 

No

 | 

Password used for verification. It is left empty by default.

 |

#### TlsVersion

type TlsVersion = 'TlsV1.0' | 'TlsV1.1' | 'TlsV1.2' | 'TlsV1.3'

Defines the available TLS version options.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

| 
Value Range

 | 

Description

 |
| :-- | :-- |
| 

'TlsV1.0'

 | 

TLS 1.0.

 |
| 

'TlsV1.1'

 | 

TLS 1.1.

 |
| 

'TlsV1.2'

 | 

TLS 1.2.

 |
| 

'TlsV1.3'

 | 

TLS 1.3.

 |

#### DebugEvent

type DebugEvent = 'text' | 'headerIn' | 'headerOut' | 'dataIn' | 'dataOut' | 'sslDataIn' | 'sslDataOut' | 'srcAddr' | 'dstAddr'

Defines the debugging event type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'text'

 | 

The debugging event is related to the text content of the HTTP response.

 |
| 

'headerIn'

 | 

The debugging event is related to the header information of the HTTP response received by the client.

 |
| 

'headerOut'

 | 

The debugging event is related to the header information of the HTTP request sent by the client.

 |
| 

'dataIn'

 | 

The debugging event is related to the body information of the HTTP response received by the client.

 |
| 

'dataOut'

 | 

The debugging event is related to the body information of the HTTP request sent by the client.

 |
| 

'sslDataIn'

 | 

The debugging event is related to the HTTP response data received through the SSL/TLS protocol.

 |
| 

'sslDataOut'

 | 

The debugging event is related to the HTTP request data sent through the SSL/TLS protocol.

 |
| 

'srcAddr'

 | 

The debugging event is related to obtaining the client address and port.

**Start version**: 6.0.0(20)

 |
| 

'dstAddr'

 | 

The debugging event is related to obtaining the server address and port.

**Start version**: 6.0.0(20)

 |

#### AuthenticationType

type AuthenticationType = 'basic' | 'ntlm' | 'digest'

Defines different identity verification types in a session.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'basic'

 | 

The basic identity authentication mode is used. The input user name and password are combined into a character string and encoded using Base64 for authentication.

 |
| 

'ntlm'

 | 

The NT LAN Manager authentication mode is used.

 |
| 

'digest'

 | 

The HTTP digest authentication mode is used, generating authentication information by hashing the user name, password, and other information.

 |

#### OnCanceled

type OnCanceled = (request?: Request) => void

Callback triggered when a request or session is canceled.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

**Start version**: 6.0.0(20)

 |

#### OnClosed

type OnClosed = () => void

Callback triggered when a session is closed.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

#### OnDataReceive

type OnDataReceive = (incomingData: ArrayBuffer, request?: Request) => number | void | Promise<void>

Callback triggered when an HTTP body is returned. Use this callback to receive data when the data size exceeds 50 MB. Then the **body** field of the returned [Response](#section156381815599) object will no longer contain data.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

incomingData

 | 

ArrayBuffer

 | 

Yes

 | 

HTTP data that is received.

 |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

**Start version**: 6.0.0(20)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Number of processed bytes. The value is of the number type.

 |
| 

Promise<void>

 | 

Empty value returned using a promise.

NOTE:

In 5.0.0(12) and later versions, the option **void | Promise<void>** is also supported.

 |

#### OnUploadProgress

type OnUploadProgress = (totalSize: number, transferredSize: number, request?: Request) => void

Callback triggered when the upload progress is displayed.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

totalSize

 | 

number

 | 

Yes

 | 

Total size of the data to be uploaded.

 |
| 

transferredSize

 | 

number

 | 

Yes

 | 

Size of the data that has been uploaded.

 |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

**Start version**: 6.0.0(20)

 |

#### OnDownloadProgress

type OnDownloadProgress = (totalSize: number, transferredSize: number, request?: Request) => void

Callback triggered when the download progress is displayed.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

totalSize

 | 

number

 | 

Yes

 | 

Total size of the data to be downloaded.

 |
| 

transferredSize

 | 

number

 | 

Yes

 | 

Size of the data that has been downloaded.

 |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

**Start version**: 6.0.0(20)

 |

#### OnHeaderReceive

type OnHeaderReceive = (headers: ResponseHeaders, request?: Request) => void

Callback triggered when an HTTP header is returned.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

headers

 | 

[ResponseHeaders](#section253714181004)

 | 

Yes

 | 

The HTTP response header is passed, and no value is returned.

 |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

**Start version**: 6.0.0(20)

 |

#### OnDataEnd

type OnDataEnd = (request?: Request) => void

Callback triggered when HTTP transmission is completed.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

**Start version**: 6.0.0(20)

 |

#### OnTimeInfo

type OnTimeInfo = (timeInfo: TimeInfo, request?: Request) => void

Represents the callback triggered when an HTTP request is successful or fails. If a request is successful, the timer information of each phase of the request can be obtained. If a request fails, the timer of each phase before the failure can be obtained.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.3(15)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

timeInfo

 | 

[TimeInfo](#section183911041803)

 | 

Yes

 | 

Time consumed in each HTTP request phase.

 |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

**Start version**: 6.0.0(20)

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1. Create a session and define the request URL and request.
const session = rcp.createSession();
const requestURL = "https://www.example.com";
const request = new rcp.Request(requestURL);

// 2. Set **configuration** for the request, in which you need to configure the **onTimeInfo** callback function to obtain time information related to the network request.
request.configuration = {
  tracing: {
    httpEventsHandler: {
      onTimeInfo: (timeInfo: rcp.TimeInfo) => {
        console.log('Time information for each phase in the HTTP request. ', JSON.stringify(timeInfo));
        let remainderDataTime = timeInfo?.totalTimeMs - timeInfo?.startTransferTimeMs;
        let firstPackageTime = timeInfo?.startTransferTimeMs - timeInfo?.preTransferTimeMs;
        let TLSTime = timeInfo?.tlsHandshakeTimeMs - timeInfo?.connectTimeMs;
        console.info(\`First packet delivery duration${firstPackageTime}\`);
        console.info(\`TLS handshake duration (excluding the connection setup time)${TLSTime}\`);
        console.info(\`Duration for receiving the remaining data${remainderDataTime}\`);
      },
    },
  },
};
// 3. Use FETCH to initiate a network request carrying the **configuration** defined above.
session.fetch(request).then((response) => {
  if (response) {
    console.info(\`The request was successful. The statusCode of the response is ${response.statusCode}\`);
    session.close();
  }
}).catch((err: BusinessError) => {
  console.error(\`Response err, the err is ${JSON.stringify(err)}\`);
})

#### OnStatusCodeReceive

type OnStatusCodeReceive = (statusCode: number, request?: Request) => void

Defines the callback triggered when an HTTP request is successful or fails, from which you can obtain the response status code.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

statusCode

 | 

number

 | 

Yes

 | 

HTTP status code.

 |
| 

request

 | 

[Request](#section10768169134510)

 | 

No

 | 

HTTP request that triggers the callback.

 |

#### CacheControl

Precisely controls the caching behavior relevant to HTTP requests in a session, including the resource cache policy, update mechanism, and storage rules.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

expirationPolicy

 | 

[TimeLimitedExpirationPolicy](#section1915682752214)

 | 

No

 | 

Yes

 | 

Expiration policy of cache records created for HTTP requests. This setting takes precedence over the HTTP response expiration policy.

 |
| 

keepCache

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to retain the cache. The default value is **false** (no). If this parameter is set to **true**, cache resources will not be cleared for requests using insecure HTTP methods (PUT, POST, or DELETE).

 |
| 

noCache

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to add **no-cache** to the request header. The default value is **false** (no). If this parameter is set to **true**, the client must verify the validity of a resource with the server before using the cache record.

 |
| 

noStore

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to add **no-store** to the request header. The default value is **false** (no). If this parameter is set to **true**, all caching of request or response content is strictly prohibited, ensuring that sensitive data is not persisted.

 |
| 

maxAge

 | 

[TimeInterval](#section202412166407)

 | 

No

 | 

Yes

 | 

Validity period of a cached resource, during which the client can use the cached data directly without requesting it from the server again.

 |
| 

maxStale

 | 

[TimeInterval](#section202412166407)

 | 

No

 | 

Yes

 | 

Time window, in seconds, during which the client can use an expired cache record. This improves data availability.

 |
| 

minFresh

 | 

[TimeInterval](#section202412166407)

 | 

No

 | 

Yes

 | 

Required duration for a keeping a response from the server fresh.

 |
| 

noTransform

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to add **no-transform** to the request header. The default value is **false** (no). If this parameter is set to **true**, the cache server is prohibited from converting the response content (for example, compressing), ensuring consistency with the original response content.

 |
| 

onlyIfCached

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to add **only-if-cached** to the request header. The default value is **false** (no). If this parameter is set to **true**, the client can use only cached resources. If no cached resource is found, the request directly fails and the client cannot request the resource from the server again.

 |

#### CacheInfo

Defines cache information, including the original HTTP request ID and the cache duration of a cache record.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

originalRequestId

 | 

string

 | 

No

 | 

No

 | 

Original HTTP request ID used when a cache record is created.

 |
| 

age

 | 

[TimeInterval](#section202412166407)

 | 

No

 | 

No

 | 

Elapsed cache duration.

 |

#### ExpirationPolicy

type ExpirationPolicy = NeverExpirationPolicy | TimeLimitedExpirationPolicy

Defines the cache expiration policy types.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[NeverExpirationPolicy](#section9834444133020)

 | 

Permanent cache expiration policy.

 |
| 

[TimeLimitedExpirationPolicy](#section1915682752214)

 | 

Time-constrained expiration policy.

 |

#### NeverExpirationPolicy

Defines the permanent cache expiration policy. Under this policy, cache records will be stored until the cache size limit is reached.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'never'

 | 

No

 | 

No

 | 

Cache expiration policy type. The key value is **never**, indicating that the permanent expiration policy is used.

 |

#### TimeLimitedExpirationPolicy

type TimeLimitedExpirationPolicy = AbsoluteTimeExpirationPolicy | RelativeTimeExpirationPolicy | SlidingTimeExpirationPolicy

Time-constrained expiration policy.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AbsoluteTimeExpirationPolicy](#section1756102119351)

 | 

Defines the absolute time-based expiration policy. A cache record expires when a specific time is reached.

 |
| 

[RelativeTimeExpirationPolicy](#section1655411614379)

 | 

Defines the relative time-based expiration policy. A cache record expires after a specified period.

 |
| 

[SlidingTimeExpirationPolicy](#section18501111511392)

 | 

Defines the sliding time window-based expiration policy. A cache record expires if it is not accessed within a specified time period. Each time it is accessed, its expiration timer is reset.

 |

#### AbsoluteTimeExpirationPolicy

Defines the absolute time-based expiration policy. A cache record expires when a specific time is reached.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'absolute'

 | 

No

 | 

No

 | 

Cache expiration policy type. The key value is **absolute**, indicating that the absolute time-based expiration policy is used.

 |
| 

time

 | 

Date

 | 

No

 | 

No

 | 

Absolute time when a cache record expires.

 |

#### RelativeTimeExpirationPolicy

Defines the relative time-based expiration policy. A cache record expires after a specified period.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'relative'

 | 

No

 | 

No

 | 

Cache expiration policy type. The key value is **relative**, indicating that the relative time-based expiration policy is used.

 |
| 

time

 | 

[TimeInterval](#section202412166407)

 | 

No

 | 

No

 | 

Period after which a cache record expires.

 |

#### SlidingTimeExpirationPolicy

Defines the sliding time window-based expiration policy. A cache record expires if it is not accessed within a specified time period. Each time it is accessed, its expiration timer is reset.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'sliding'

 | 

No

 | 

No

 | 

Cache expiration policy type. The key value is **sliding**, indicating that the sliding time window-based expiration policy is used.

 |
| 

time

 | 

[TimeInterval](#section202412166407)

 | 

No

 | 

No

 | 

Period after which a cache record expires.

 |

#### TimeInterval

Defines time interval settings.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

units

 | 

[TimeIntervalUnits](#section32011352124313)

 | 

No

 | 

No

 | 

Time interval unit.

 |
| 

value

 | 

number

 | 

No

 | 

No

 | 

Time interval length.

 |

#### TimeIntervalUnits

type TimeIntervalUnits = 'seconds' | 'minutes' | 'hours' | 'days'

Time interval unit.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'seconds'

 | 

Time unit: second.

 |
| 

'minutes'

 | 

Time unit: minute.

 |
| 

'hours'

 | 

Time unit: hour.

 |
| 

'days'

 | 

Time unit: day.

 |

#### CachedResponse

Defines the information about HTTP response data stored in the cache.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

timeStamp

 | 

Date

 | 

No

 | 

No

 | 

Time when an HTTP response is obtained from the network.

 |
| 

originalRequestId

 | 

string

 | 

No

 | 

No

 | 

Original HTTP request ID.

 |
| 

statusCode

 | 

number

 | 

No

 | 

No

 | 

HTTP response status code.

 |
| 

headers

 | 

[ResponseHeaders](#section253714181004)

 | 

No

 | 

No

 | 

HTTP response headers.

 |
| 

body

 | 

ArrayBuffer

 | 

No

 | 

Yes

 | 

HTTP response content.

 |
| 

effectiveUrl

 | 

string

 | 

No

 | 

Yes

 | 

Valid URL to which a request is redirected. The default value is **undefined**.

 |
| 

httpVersion

 | 

[HttpVersion](#section14719175117590)

 | 

No

 | 

Yes

 | 

HTTP version.

 |
| 

reasonPhrase

 | 

string

 | 

No

 | 

Yes

 | 

**reasonPhrase** of an HTTP status line, which provides a descriptive message associated with a numerical status code.

 |
| 

extra

 | 

ArrayBuffer

 | 

No

 | 

Yes

 | 

Additional information.

 |

#### ResponseCacheKey

Defines the key that identifies an HTTP response cache record.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

No

 | 

No

 | 

Request URL.

 |
| 

method

 | 

[HttpMethod](#section20787153164810)

 | 

No

 | 

No

 | 

HTTP method.

 |
| 

extra

 | 

string

 | 

No

 | 

Yes

 | 

Additional information. Multiple response cache records to be stored for the same combination of a URL and an HTTP method. You can use this attribute to distinguish between them. For example, you can use this field to store a language type string to identify the response content of the corresponding language.

 |

#### ResponseCacheRecord

Defines the information of a cache record.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

expirationPolicy

 | 

[ExpirationPolicy](#section962212143274)

 | 

No

 | 

No

 | 

Cache expiration policy.

 |
| 

response

 | 

[CachedResponse](#section49322045124710)

 | 

No

 | 

No

 | 

Cached response.

 |
| 

key

 | 

[ResponseCacheKey](#section12431163985515)

 | 

No

 | 

No

 | 

Cache key of the cached response.

 |

#### CacheConfiguration

Defines cache configurations. You can call this API to control the cache behavior by performing configurations such as the memory and disk cache configuration, maximum cache size, maxim number of cache records, and default expiration policy type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

persistent

 | 

[PersistentStorageConfiguration](#section187463325215)

 | 

No

 | 

No

 | 

Persistent cache configuration.

 |
| 

inMemory

 | 

[InMemoryCacheConfiguration](#section101531755759)

 | 

No

 | 

Yes

 | 

Memory cache configuration.

 |
| 

maxItems

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of cache records for in-memory/persistent storage. When the parameter is set and the number of cache records exceeds this upper limit, an eviction policy based on the Least Recently Used (LRU) algorithm will be executed. It will first evict cache records that apply the time-constrained expiration policy, and then, if necessary, evict those applying the permanent expiration policy.

 |
| 

maxSize

 | 

number

 | 

No

 | 

Yes

 | 

Upper limit of in-memory/persistent storage. When the parameter is set and the cache size exceeds this upper limit, an eviction policy based on the Least Recently Used (LRU) algorithm will be executed. It will first evict cache records that apply the time-constrained expiration policy, and then, if necessary, evict those applying the permanent expiration policy.

Unit: MB

Default value: **50**

 |
| 

defaultExpirationPolicy

 | 

[TimeLimitedExpirationPolicy](#section1915682752214)

 | 

No

 | 

Yes

 | 

Default cache expiration policy.

The specified cache expiration policy applies to each new response generated after it is set.

If this attribute is not set, the [SlidingTimeExpirationPolicy](#section18501111511392) with the 1-hour time window will be used by default.

The cache expiration policy specified using the [set](#section1187111165016) method will overwrite the default cache expiration policy specified by this API.

 |

#### PersistentStorageConfiguration

type PersistentStorageConfiguration = FileSystemStorageConfiguration

Defines persistent cache storage configurations.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[FileSystemStorageConfiguration](#section1765861216411)

 | 

File system-based cache storage configurations.

 |

#### FileSystemStorageConfiguration

Defines file system-based cache storage configurations.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

kind

 | 

'file-system'

 | 

No

 | 

No

 | 

Persistent cache storage medium type. The key value is **file-system**, indicating file system-based medium storage.

 |
| 

pathToFolder

 | 

string

 | 

No

 | 

No

 | 

File path for cache storage. For details, please refer to [Application Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file).

 |

#### InMemoryCacheConfiguration

Defines in-memory cache storage configurations.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxItems

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of records in the in-memory cache.

 |
| 

maxSize

 | 

number

 | 

No

 | 

Yes

 | 

Maximum memory allocated for the in-memory cache. If this attribute is set, the **maxSize** attribute configured in [CacheConfiguration](#section139991413145915) does not take effect for the in-memory cache.

Unit: MB

Default value: **10**.

 |

#### CacheState

Defines cache status information, including the current number of cache records, cache size, and cache hit count.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

size

 | 

number

 | 

No

 | 

No

 | 

Number of bytes in the persistent cache storage.

Unit: byte

 |
| 

count

 | 

number

 | 

No

 | 

No

 | 

Number of cache records in the persistent cache storage.

 |
| 

hitCount

 | 

number

 | 

No

 | 

No

 | 

Number of cache hits.

 |

#### ResponseCache

Records and manages HTTP response caching.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

#### \[h2\]constructor

constructor(configuration: CacheConfiguration)

Creates an HTTP response cache instance.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

configuration

 | 

[CacheConfiguration](#section139991413145915)

 | 

Yes

 | 

Cache configurations.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

const cache = new rcp.ResponseCache({
  persistent: {
    kind: 'file-system',
    pathToFolder: "/path/dir" // Set the path based on your service needs.
  }
});

#### \[h2\]close

close(): Promise<void>

Closes the HTTP response cache instance and terminates all pending cache operations. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1007900985

 | 

File system IO error.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  await cache.close();
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### \[h2\]set

set(key: ResponseCacheKey, response: CachedResponse, expirationPolicy?: ExpirationPolicy): Promise<void>

Adds or replaces the cache content based on a cache key. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

[ResponseCacheKey](#section12431163985515)

 | 

Yes

 | 

Cache key.

 |
| 

response

 | 

[CachedResponse](#section49322045124710)

 | 

Yes

 | 

HTTP response cache content to be added or replaced with.

 |
| 

expirationPolicy

 | 

[ExpirationPolicy](#section962212143274)

 | 

No

 | 

Defines the cache expiration policy types. The policy defined by this attribute will overwrite the default cache expiration policy (**defaultExpirationPolicy**) in [CacheConfiguration](#section139991413145915).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1007900401

 | 

Parameter error.

 |
| 

1007900985

 | 

File system IO error.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  const session: rcp.Session = rcp.createSession({
    requestConfiguration: {
      cache: cache
    }
  });
  const key: rcp.ResponseCacheKey = {
    url: 'https://www.example.com',
    method: 'GET'
  };
  const response = await session.get('https://www.example.com');
  const cachedRecord = rcp.createCachedResponse(response);
  const policy: rcp.TimeLimitedExpirationPolicy = {
    kind: 'relative',
    time: {
      units: 'seconds',
      value: 3
    }
  };
  cache.set(key, cachedRecord, policy).then(() => {
  })
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### \[h2\]get

get(key: ResponseCacheKey): Promise<ResponseCacheRecord>

Obtains an HTTP response cache record based on the cache key. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

[ResponseCacheKey](#section12431163985515)

 | 

Yes

 | 

Cache key.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ResponseCacheRecord](#section13850182925713)\>

 | 

Promise object, which returns the target HTTP response cache record.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1007900401

 | 

Parameter error.

 |
| 

1007900985

 | 

File system IO error.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  const record = await cache.get({
    url: 'https://www.example.com',
    method: 'GET'
  });
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### \[h2\]clear

clear(): Promise<void>

Clears the HTTP response cache. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1007900985

 | 

File system IO error.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  await cache.clear();
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### \[h2\]getState

getState(): Promise<CacheState>

Obtains cache status information. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CacheState](#section29031836872)\>

 | 

Promise object, which returns the cache status information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1007900985

 | 

File system IO error.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  const cacheState = await cache.getState();
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### \[h2\]remove

remove(key: ResponseCacheKey): Promise<boolean>

Deletes an HTTP response cache record based on the specified cache key. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

[ResponseCacheKey](#section12431163985515)

 | 

Yes

 | 

Cache key.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object, which returns either **true** (deletion successful) or **false** (deletion failed).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1007900401

 | 

Parameter error.

 |
| 

1007900985

 | 

File system IO error.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  const key: rcp.ResponseCacheKey = {
    url: 'https://www.example.com',
    method: 'GET'
  };
  const result = await cache.remove(key);
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### \[h2\]removeMultiple

removeMultiple(url: URLOrString, matchKind: URLMatchKind, method?: HttpMethod): Promise<boolean>

Searches for and then deletes one or more HTTP response cache records by URL matching. You can specify the URL matching type by setting **matchKind**. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

url

 | 

[URLOrString](#section320653742718)

 | 

Yes

 | 

URL, which is used to match the URL in the cache key.

 |
| 

matchKind

 | 

[URLMatchKind](#section13928831917)

 | 

Yes

 | 

URL matching type.

 |
| 

method

 | 

[HttpMethod](#section20787153164810)

 | 

No

 | 

HTTP request method.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object, which returns either **true** (deletion successful) or **false** (deletion failed).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1007900401

 | 

Parameter error.

 |
| 

1007900985

 | 

File system IO error.

 |

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  const result = await cache.removeMultiple('https://www.example.com', 'exact', 'GET');
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### URLMatchKind

type URLMatchKind = 'exact' | 'as-substring'

URL matching type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'exact'

 | 

Exact URL matching. A URL can be matched only if it is exactly the same as the passed URL.

 |
| 

'as-substring'

 | 

Substring URL matching. A URL can be matched if it contains the specified URL as a substring.

 |

#### rcp.createResponse

createResponse(request: Request, cachedResponse: CachedResponse, currentTime: Date): Response

Creates an HTTP response based on the HTTP response cache record.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[Request](#section10768169134510)

 | 

Yes

 | 

HTTP request for which a response needs to be created.

 |
| 

cachedResponse

 | 

[CachedResponse](#section49322045124710)

 | 

Yes

 | 

HTTP response cache record that is stored.

 |
| 

currentTime

 | 

Date

 | 

Yes

 | 

Current time.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Response](#section156381815599)

 | 

HTTP response.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir" // Set the path based on your service needs.
    }
  });
  const request = new rcp.Request('https://www.example.com', 'GET');
  const key: rcp.ResponseCacheKey = {
    url: request.url,
    method: request.method,
  };
  // Obtain the HTTP response cache result.
  const responseInCache = await cache.get(key);
  if (responseInCache) {
    // Create an HTTP response based on the HTTP response cache record.
    const response = rcp.createResponse(request, responseInCache.response, new Date());
  }
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}

#### rcp.createCachedResponse

createCachedResponse(response: Response, timeStamp?: Date): CachedResponse

Creates an HTTP response cache record based on the HTTP response.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

response

 | 

[Response](#section156381815599)

 | 

Yes

 | 

HTTP response.

 |
| 

timeStamp

 | 

Date

 | 

No

 | 

Timestamp of the cached response. The current system time is used by default.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[CachedResponse](#section49322045124710)

 | 

HTTP response cache.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

**Example**:

import { rcp } from '@kit.RemoteCommunicationKit';

try {
  const cache = new rcp.ResponseCache({
    persistent: {
      kind: 'file-system',
      pathToFolder: "/path/dir", // Set the path based on your service needs.
    }
  });
  const session = rcp.createSession();
  const key: rcp.ResponseCacheKey = {
    url: 'https://www.example.com',
    method: 'GET'
  };
  // Obtain the HTTP response.
  const response = await session.get('https://www.example.com');
  // Create an HTTP response cache record based on the HTTP response.
  const cachedRecord = rcp.createCachedResponse(response);
} catch (err) {
  console.error(\`Error: error code is ${err.code}, error message is ${JSON.stringify(err.data)}\`);
}
