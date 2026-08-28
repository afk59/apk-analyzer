# cloudFunction (Cloud Functions Module)

This module provides the capability of calling cloud functions.

**Start version**: 5.0.0(12)

#### Modules to Import

import { cloudFunction } from '@kit.CloudFoundationKit';

#### call

call(parameters: FunctionParams, callback: AsyncCallback<FunctionResult>): void

Calls a cloud function to use features implemented by the cloud function. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

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

parameters

 | 

[FunctionParams](#section14128318216)

 | 

Yes

 | 

Mandatory parameters for calling a cloud function.

 |
| 

callback

 | 

AsyncCallback<[FunctionResult](#section4550131697)\>

 | 

Yes

 | 

Callback function. If the cloud function is called successfully, **err** is **undefined** and **data** is the **FunctionResult** obtained; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008210001

 | 

Network connection error.

 |
| 

1008210009

 | 

Client internal error.

 |
| 

1008211001

 | 

Server error.

 |

**Example**:

import { cloudFunction } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

cloudFunction.call({
  name: 'my-handler-xxxx',
  version: '$latest',
  timeout: 10 \* 1000,
  data: {
    param1: 'val1',
    param2: 'val2'
  }
}, (err: BusinessError, value: cloudFunction.FunctionResult) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to call the function, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  hilog.info(0x0000, 'testTag', \`Succeeded in calling the function, result: ${JSON.stringify(value.result)}\`);
})

#### call

call(parameters: FunctionParams): Promise<FunctionResult>

Calls a cloud function to use features implemented by the cloud function. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

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

parameters

 | 

[FunctionParams](#section14128318216)

 | 

Yes

 | 

Mandatory parameters for calling a cloud function.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[FunctionResult](#section4550131697)\>

 | 

Function call result returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008210001

 | 

Network connection error.

 |
| 

1008210009

 | 

Client internal error.

 |
| 

1008211001

 | 

Server error.

 |

**Example**:

import { cloudFunction } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

cloudFunction.call({
  name: 'my-handler-xxxx',
  version: '$latest',
  timeout: 10 \* 1000,
  data: {
    param1: 'val1',
    param2: 'val2'
  }
}).then((value: cloudFunction.FunctionResult) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in calling the function, result: ${JSON.stringify(value.result)}\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to call the function, code: ${err.code}, message: ${err.message}\`);
})

#### FunctionParams

Parameters for calling a cloud function.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

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

name

 | 

string

 | 

No

 | 

No

 | 

Cloud function name.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

data

 | 

string | Object

 | 

No

 | 

Yes

 | 

Function request body.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

version

 | 

string

 | 

No

 | 

Yes

 | 

Cloud function version. The default value is **$latest**, indicating the latest version.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

timeout

 | 

number

 | 

No

 | 

Yes

 | 

Timeout interval for requesting a function, in milliseconds. The default interval is 70 x 1000 milliseconds.

The value range is unrestricted, and the value will be converted to the unsigned long type.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

loadMode

 | 

[LoadMode](#section68131056112513)

 | 

No

 | 

Yes

 | 

Function loading mode. The default value is **NORMAL**.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

localUrl

 | 

string

 | 

No

 | 

Yes

 | 

URL of the cloud function that is locally started. The format is **http://_Domain name_:_Port number_**, for example, **http://localhost:18090**.

This parameter is used only when you debug a local cloud function. After the cloud function is deployed to the cloud, this parameter cannot be used.

**Start version**: 6.0.1(21)

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

 |

#### LoadMode

Enumerated function loading modes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NORMAL

 | 

0

 | 

Normal mode, in which the server is requested to obtain data each time the **call** method is called.

 |
| 

PRELOAD

 | 

1

 | 

Preload mode, in which the result data is returned only once when the app is installed. An error will be returned when the **call** method is called later.

**Device behavior differences**: This parameter is supported on phones and tablets. On other devices, passing this parameter will return error code 1008211001.

 |

#### FunctionResult

Result returned by the cloud function.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

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

result

 | 

string | Object

 | 

No

 | 

No

 | 

Result returned by the cloud function.

 |
