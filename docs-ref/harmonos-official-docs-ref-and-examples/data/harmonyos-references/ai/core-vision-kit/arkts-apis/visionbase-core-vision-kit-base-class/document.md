# VisionBase (Core Vision Kit Base Class)

As a basic visual capability library, **visionBase** encapsulates basic resource objects, common objects in visual capability scenarios, data structures, and common methods. It helps reduce the coding workload and simplifies the use of functional APIs. You can consider it as a toolbox containing the most common tools. With this base class, you can implement your functions more efficiently while complying with necessary standards. In addition, **visionBase** provides the infrastructure required by Core Vision Kit AI capabilities, such as data structures, API models, and lifecycle management.

**Start version**: 5.0.0(12)

#### Module Import

import { visionBase } from '@kit.CoreVisionKit';

#### SceneMode

Enumeration of scene modes.

**System capability**: SystemCapability.AI.Vision.VisionBase

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

FOREGROUND

 | 

1

 | 

Foreground mode (default value).

 |
| 

BACKGROUND

 | 

2

 | 

Background mode.

 |

#### ImageData

Visual information object to be recognized.

**System capability**: SystemCapability.AI.Vision.VisionBase

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

pixelMap

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Image to be recognized.

 |

#### InputData

type InputData = ImageData | ImageData\[\]

Array consisting of multiple pieces of image data.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ImageData](#section674171818172) | [ImageData](#section674171818172)\[\]

 | 

Array of images to be recognized. You can input one or more images.

 |

#### BoundingBox

Bounding box for AI visual capabilities.

**System capability**: SystemCapability.AI.Vision.VisionBase

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

left

 | 

number

 | 

No

 | 

No

 | 

X coordinate of the upper left corner of a bounding box.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of the upper left corner of a bounding box.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Height of a bounding box, in pixels.

 |
| 

width

 | 

number

 | 

No

 | 

No

 | 

Width of a bounding box, in pixels.

 |

#### Point

Point on a 2D plane.

**System capability**: SystemCapability.AI.Vision.VisionBase

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

x

 | 

number

 | 

No

 | 

No

 | 

X coordinate of a point.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of a point.

 |

#### Orientation

Orientation on a 3D plane.

**System capability**: SystemCapability.AI.Vision.VisionBase

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

yaw

 | 

number

 | 

No

 | 

No

 | 

Yaw angle of rotating an object around the vertical axis (Y axis), which determines the direction of the object on the horizontal plane. Value range: \[–180, 180\]

 |
| 

pitch

 | 

number

 | 

No

 | 

No

 | 

Pitch angle of rotating an object around the horizontal axis (X axis), which determines the direction of the object on the vertical plane. Value range: \[–180, 180\]

 |
| 

roll

 | 

number

 | 

No

 | 

No

 | 

Roll angle of rotating an object around the Z axis, which determines the direction of the object on the plane perpendicular to the X and Y planes. Value range: \[–180, 180\]

 |

#### DownloadStartData

Data structure of download start events triggered when AI model download starts. It is used to inform you of the resource that starts to be downloaded. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

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

resId

 | 

string

 | 

No

 | 

No

 | 

Resource ID, which is used to identify the model that is being downloaded.

 |

#### DownloadCompleteData

Data structure of download completion events triggered when model download is complete. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

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

resId

 | 

string

 | 

No

 | 

No

 | 

Resource ID.

 |
| 

resVersion

 | 

string

 | 

No

 | 

No

 | 

Resource version number.

 |

#### DownloadCancelData

Data structure of download cancellation events triggered when the download process is canceled. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

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

resId

 | 

string

 | 

No

 | 

No

 | 

Resource ID.

 |

#### DownloadStatusData

Data structure of download status events, which is used to report various statuses during the download process, such as network errors and invalid parameters. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

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

resId

 | 

string

 | 

No

 | 

No

 | 

Resource ID.

 |
| 

statusCode

 | 

[downloadStatusCode](#section547617344513)

 | 

No

 | 

No

 | 

Status code.

 |
| 

message

 | 

string

 | 

No

 | 

No

 | 

Status description. The description is not fixed.

 |

#### DownloadProgressData

Data structure of download progress events, which is used to report the download progress so that you can display the progress in real time. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

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

resId

 | 

string

 | 

No

 | 

No

 | 

Resource ID.

 |
| 

progressInfo

 | 

string

 | 

No

 | 

No

 | 

Progress information.

 |

#### downloadStatusCode

Enumeration of download statuses. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PARAMETER\_INVALID

 | 

0

 | 

Incorrect input download parameter. For example, the resource ID format is incorrect. You are advised to check the format and validity of input parameters.

 |
| 

NO\_NETWORK\_STATUS

 | 

1

 | 

The device is offline or the network is unavailable. You are advised to ask the user to check the network connection.

 |
| 

NO\_MODEL

 | 

2

 | 

The corresponding model file cannot be found on the server. You are advised to check whether the model's resource ID is correct and whether the model file exists on the server.

 |
| 

COPY\_FILE\_FAILED

 | 

3

 | 

A downloaded model file cannot be copied to the specified location. You are advised to check the storage permission and available space.

 |
| 

DOWNLOAD\_NOT\_ALLOWED

 | 

4

 | 

The user has chosen to reject the download in the scenario where user confirmation is required.

 |
| 

DOWNLOAD\_TIME\_OUT

 | 

5

 | 

The network is slow or the server response is delayed.

 |
| 

DOWNLOAD\_EXCEPTION

 | 

6

 | 

An error occurs during the download process. This value is used to refer to any other unspecified errors.

 |
| 

DOWNLOAD\_BACK\_TO\_DESKTOP

 | 

7

 | 

The user switches out of the app during the download process.

 |
| 

TASK\_BUSY

 | 

8

 | 

The system is busy and is currently executing another task.

**Start version**: 6.0.0(20)

 |

#### Request

Base class of input parameters.

**System capability**: SystemCapability.AI.Vision.VisionBase

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

inputData

 | 

[InputData](#section1515014491877)

 | 

No

 | 

No

 | 

One or more images to be recognized. The value can be an object or an object array.

 |
| 

scene

 | 

[SceneMode](#section4298938144913)

 | 

No

 | 

Yes

 | 

Scene mode.

This parameter is reserved and not implemented currently.

 |
| 

requestId

 | 

string

 | 

No

 | 

Yes

 | 

Request ID. You can use it to trace and manage your requests.

This parameter is reserved and not implemented currently.

 |

#### Response

Response base class, which is used as the returned result of a capability request.

**System capability**: SystemCapability.AI.Vision.VisionBase

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

requestId

 | 

string

 | 

No

 | 

Yes

 | 

Unique request ID. You can use it to trace and manage your requests.

 |

#### Analyzer

Base class which functions as the capability engine.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.0(12)

#### \[h2\]destroy

destroy(): Promise<void>

Destroys the processes of multiple visual capabilities. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.0(12)

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

Promise object. This API does not return any value.

 |

**Example**:

For details, please refer to [ObjectDetection.destroy](../objectdetection-multi-object-detection/document.md#section1623412106322).

#### on('downloadStart')

on(type: 'downloadStart', callback: Callback<DownloadStartData>): void

Listens to download start events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadStart**, indicating listening to download start events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadStartData](#section106991634151312)\>

 | 

Yes

 | 

Callback used to return the resource that starts to be downloaded.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

visionBase.on('downloadStart', (data) => {
    console.info(\`Resource ${data.resId} starts to be downloaded\`);
});

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### on('downloadComplete')

on(type: 'downloadComplete', callback: Callback<DownloadCompleteData>): void

Listens to download completion events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadComplete**, indicating listening to download completion events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadCompleteData](#section1377410113590)\>

 | 

Yes

 | 

Callback used to return the ID and version of a downloaded resource.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

visionBase.on('downloadComplete', (data) => {
    console.info(\`Resource ${data.resId} has been downloaded. Version: ${data.resVersion}\`);
});

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### on( 'downloadCancel')

on(type: 'downloadCancel', callback: Callback<DownloadCancelData>): void

Listens to download cancellation events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadCancel**, indicating listening to download cancellation events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadCancelData](#section4395143020014)\>

 | 

Yes

 | 

Callback used to return the resource whose download has been canceled.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

visionBase.on('downloadCancel', (data) => {
    console.info(\`Download of resource ${data.resId} has been canceled\`);
});

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### on( 'downloadStatus')

on(type: 'downloadStatus', callback: Callback<DownloadStatusData>): void

Listens to download status events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadStatus**, indicating listening to download status events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadStatusData](#section207922221711)\>

 | 

Yes

 | 

Callback used to return the download status.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

visionBase.on('downloadStatus', (data) => {
    console.info(\`Download status of resource ${data.resId}: ${data.statusCode}, ${data.message}\`);
});

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### on('downloadProgress')

on(type: 'downloadProgress', callback: Callback<DownloadProgressData>): void

Listens to download progress events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadProgress**, indicating listening to download progress events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadProgressData](#section167614491024)\>

 | 

Yes

 | 

Callback used to return the download progress.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

visionBase.on('downloadProgress', (data) => {
    console.info(\`Download progress of resource ${data.resId}: ${data.progressInfo}\`);
})

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### off('downloadStart')

off(type: 'downloadStart', callback?: Callback<DownloadStartData>): void

Cancels the listening to download start events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadStart**, indicating canceling the listening to download start events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadStartData](#section106991634151312)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

// Define a callback.
const startCallback = (data: visionBase.DownloadStartData) => {
  console.info(\`Resource ${data.resId} starts to be downloaded\`);
};
// Register a listener.
visionBase.on('downloadStart', startCallback);
// Unregister the listener.
visionBase.off('downloadStart', startCallback);

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### off('downloadComplete')

off(type: 'downloadComplete', callback?: Callback<DownloadCompleteData>): void

Cancels the listening to download completion events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadComplete**, indicating canceling the listening to download completion events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadCompleteData](#section1377410113590)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

// Define a callback.
const callback = (data: visionBase.DownloadCompleteData) => {
  console.info(\`Resource ${data.resId} has been downloaded\`);
};
// Register a listener.
visionBase.on('downloadComplete', callback);
// Unregister the listener.
visionBase.off('downloadComplete', callback);

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### off('downloadCancel')

off(type: 'downloadCancel', callback?: Callback<DownloadCancelData>): void

Cancels the listening to download cancellation events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadCancel**, indicating canceling the listening to download cancellation events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadCancelData](#section4395143020014)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

// Define a callback.
const callback = (data: visionBase.DownloadCancelData) => {
  console.info(\`Download of resource ${data.resId} has been canceled\`);
};
// Register a listener.
visionBase.on('downloadCancel', callback);
// Unregister the listener.
visionBase.off('downloadCancel', callback);

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### off('downloadStatus')

off(type: 'downloadStatus', callback?: Callback<DownloadStatusData>): void

Cancels the listening to download status events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadStatus**, indicating canceling the listening to download status events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadStatusData](#section207922221711)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

// Define a callback.
const callback = (data: visionBase.DownloadStatusData) => {
  console.info(\`Download status of resource ${data.resId}\`);
};
// Register a listener.
visionBase.on('downloadStatus', callback);
// Unregister the listener.
visionBase.off('downloadStatus', callback);

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}

#### off('downloadProgress')

off(type: 'downloadProgress', callback?: Callback<DownloadProgressData>): void

Cancels the listening to download progress events. This API is reserved and is not supported in the current version.

**System capability**: SystemCapability.AI.Vision.VisionBase

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

The value is always **downloadProgress**, indicating canceling the listening to download progress events.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[DownloadProgressData](#section167614491024)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

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

The parameter check failed.

 |

**Example**:

import { visionBase } from '@kit.CoreVisionKit';

// Define a callback.
const callback = (data: visionBase.DownloadProgressData) => {
  console.info(\`Download progress of resource ${data.resId}\`);
};
// Register a listener.
visionBase.on('downloadProgress', callback);
// Unregister the listener.
visionBase.off('downloadProgress', callback);

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Button').onClick(() => {

      })
    }
  }
}
