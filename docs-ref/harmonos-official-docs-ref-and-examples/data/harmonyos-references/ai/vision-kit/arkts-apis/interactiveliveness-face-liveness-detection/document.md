# interactiveLiveness (Face Liveness Detection)

Face liveness detection is a method of determining the real physiological features of an object in certain identity verification scenarios.

Among facial recognition applications, liveness detection can capture faces in real time or trace a user's combined actions of blinking, mouth opening, head shaking, and nodding, and use technologies such as facial keypoint recognition and face tracking to check whether a user is a real live person. This capability effectively defends against common attacks, including print photos, videos, masks, occlusions, and screen recapture, helping to identify fraud and protect user interests.

**Start version**: 5.0.0(12)

#### Module Import

import { interactiveLiveness } from '@kit.VisionKit';

#### DetectionMode

Enumeration of detection modes.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

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

SILENT\_MODE

 | 

SILENT\_MODE

 | 

Silent liveness detection mode, which is not supported currently.

 |
| 

INTERACTIVE\_MODE

 | 

INTERACTIVE\_MODE

 | 

Interactive liveness detection mode.

 |

#### ActionsNumber

Enumeration of the number of actions for face liveness detection.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

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

ONE\_ACTION

 | 

1

 | 

Select one action randomly. Currently, this option is not supported.

 |
| 

TWO\_ACTION

 | 

2

 | 

Select two actions randomly. Currently, this option is not supported.

 |
| 

THREE\_ACTION

 | 

3

 | 

Select three actions randomly.

 |
| 

FOUR\_ACTION

 | 

4

 | 

Select four actions randomly.

 |

#### RouteRedirectionMode

Enumeration of route redirection modes after face liveness detection.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

BACK\_MODE

 | 

back

 | 

Return to the previous screen after face liveness detection is complete.

 |
| 

REPLACE\_MODE

 | 

replace

 | 

Display the success or failure screen after face liveness detection is complete.

 |

#### InteractiveLivenessConfig

Configuration of face liveness detection.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

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

isSilentMode

 | 

[DetectionMode](#section143611912403)

 | 

No

 | 

No

 | 

Face liveness detection mode. The default mode is interactive liveness detection.

**INTERACTIVE\_MODE**: interactive liveness detection

 |
| 

actionsNum

 | 

[ActionsNumber](#section156871424104118)

 | 

No

 | 

Yes

 | 

Number of actions for interactive liveness detection. The value can be **3** or **4**. The default value is **3**. The value is randomly generated based on the following rules:

If the value of **actionsNum** is **3**, actions in combination \[Blink,Gaze\] do not coexist, and adjacent actions are different.

If the value of **actionsNum** is **4**, the Blink action must exist and appear only once, the Gaze action can appear at most once, actions in combination \[Blink,Gaze\] are not adjacent to each other, and adjacent actions are different.

This parameter is valid only when **isSilentMode** is set to **INTERACTIVE\_MODE**.

 |
| 

successfulRouteUrl

 | 

string

 | 

No

 | 

Yes

 | 

Path of the screen displayed after face liveness detection is successful. If a screen is customized, this parameter takes effect when **routeMode** is set to **replace**.

If this parameter is left empty, the system displays a default detection success screen.

 |
| 

failedRouteUrl

 | 

string

 | 

No

 | 

Yes

 | 

Path of the screen displayed after face liveness detection fails. If a screen is customized, this parameter takes effect when **routeMode** is set to **replace**.

If this parameter is left empty, the system displays a default detection failure screen.

 |
| 

routeMode

 | 

[RouteRedirectionMode](#section6129163245310)

 | 

No

 | 

Yes

 | 

Redirection mode after face liveness detection is complete.

 |
| 

challenge

 | 

string

 | 

No

 | 

Yes

 | 

Challenge value. This parameter is used only for liveness detection in the image security verification scenario (corresponding to **userData** in the [initializeAttestContext](../../../../system/security/device-security-kit/arkts-apis/trustedappservice/document.md#section166716269293) method).

To use image security verification, ensure that [Device Security Kit has been enabled](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice).

The value is a string of 16 to 128 characters. (For a scenario other than image security verification, **challenge** is left empty or undefined.)

For details about device models supported by image security verification, please refer to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-taas-securecamera#section104414218221).

 |
| 

speechSwitch

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable voice broadcast.

-   **true**: yes
-   **false**: no

Voice broadcast is enabled by default.

 |
| 

isPrivacyMode

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the privacy mode.

-   **true**: yes
-   **false**: no

The default value is **false**.

NOTE:

To enable the privacy mode, you need to apply for the **ohos.permission.PRIVACY\_WINDOW** permission.

 |

**Example**:

import { interactiveLiveness } from '@kit.VisionKit';

let isSilentMode = "INTERACTIVE\_MODE" as interactiveLiveness.DetectionMode;
let routeMode = "replace" as interactiveLiveness.RouteRedirectionMode;
let actionsNum = 3 as interactiveLiveness.ActionsNumber;
let routerOptions: interactiveLiveness.InteractiveLivenessConfig= {
  isSilentMode: isSilentMode,
  routeMode: routeMode,
  actionsNum: actionsNum,
  failedRouteUrl: "pages/FailPage",
  successfulRouteUrl: "pages/SuccessPage"
}

#### startLivenessDetection

startLivenessDetection(config: InteractiveLivenessConfig): Promise<boolean>

Entry for redirecting to the face liveness detection screen. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.CAMERA

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

**Start version**: 5.0.0(12)

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

config

 | 

[InteractiveLivenessConfig](#section16532153115517)

 | 

Yes

 | 

Configuration for redirecting to the face liveness detection screen.

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

Result of redirecting to the face liveness detection screen, which is returned through a promise.

-   **true**: The redirection is successful.
-   **false**: The redirection fails.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1008301002

 | 

Route switching failed.

 |

**Example**:

import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let isSilentMode = "INTERACTIVE\_MODE" as interactiveLiveness.DetectionMode;
let actionsNum = 3 as interactiveLiveness.ActionsNumber;
let routerOptions: interactiveLiveness.InteractiveLivenessConfig= {
  actionsNum: actionsNum,
  isSilentMode: isSilentMode
};

interactiveLiveness.startLivenessDetection(routerOptions).then((DetectState: boolean) => {
  hilog.info(0x0001, "LivenessCollectionIndex", \`Succeeded in jumping.\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0001, "LivenessCollectionIndex", \`Failed to jump. Code: ${err.code}, message: ${err.message}\`);
})

#### startLivenessDetection

startLivenessDetection(config: InteractiveLivenessConfig, callback: AsyncCallback<InteractiveLivenessResult | undefined>): Promise<boolean>

Entry for redirecting to the face liveness detection screen. This API returns the redirection result asynchronously through a promise and returns the detection result through a callback.

**Required permission**: ohos.permission.CAMERA

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

**Start version**: 5.0.0(12)

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

config

 | 

[InteractiveLivenessConfig](#section16532153115517)

 | 

Yes

 | 

Configuration for redirecting to the face liveness detection screen.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[InteractiveLivenessResult](#section173751154134515) | undefined>

 | 

Yes

 | 

Callback function, which is used to return the liveness detection result. Currently, it applies only to the **RouteRedirectionMode.BACK\_MODE** redirection mode.

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

Result of redirecting to the face liveness detection screen, which is returned through a promise.

-   **true**: The redirection is successful.
-   **false**: The redirection fails.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error.

 |
| 

1008301002

 | 

Route switching failed.

 |
| 

1008302000

 | 

Detection algorithm initialization.

 |
| 

1008302001

 | 

Detection timeout.

 |
| 

1008302002

 | 

Action mutual exclusion error.

 |
| 

1008302003

 | 

Continuity Check Failure.

 |
| 

1008302004

 | 

The test is not complete.

 |

**Example**:

import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let isSilentMode = "INTERACTIVE\_MODE" as interactiveLiveness.DetectionMode;
let actionsNum = 3 as interactiveLiveness.ActionsNumber;
let routerOptions: interactiveLiveness.InteractiveLivenessConfig= {
  actionsNum: actionsNum,
  isSilentMode: isSilentMode,
  routeMode: "back" as interactiveLiveness.RouteRedirectionMode
};

interactiveLiveness.startLivenessDetection(routerOptions, (err: BusinessError, 
  result: interactiveLiveness.InteractiveLivenessResult | undefined) => { // Failed to obtain the result when the route redirection is incorrect. The result **undefined** is returned.
  if(err.code !== 0 && !result) { // An error code is returned when an error occurs, such as route redirection failure, parameter error, or permission denied. For details, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).
    hilog.error(0x0001, "LivenessCollectionIndex", \`Failed to detect. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  hilog.info(0x0001, 'LivenessCollectionIndex', \`Succeeded in detecting result: ${result}\`);
})

#### LivenessType

Enumeration of liveness detection modes.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

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

INTERACTIVE\_LIVENESS

 | 

0

 | 

Interactive liveness detection.

 |
| 

SILENT\_LIVENESS

 | 

1

 | 

Silent liveness detection, which is not supported currently.

 |
| 

NOT\_LIVENESS

 | 

2

 | 

The detected object is a non-live object. The failure screen will be displayed, and no error information is returned. If you have configured your own failure screen or back route redirection, you are not advised to perform the detection again.

 |

#### InteractiveLivenessResult

Parameters of the face liveness detection result.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

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

livenessType

 | 

[LivenessType](#section15262164419435)

 | 

No

 | 

No

 | 

Liveness detection mode.

 |
| 

mPixelMap

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

Yes

 | 

Image with the most liveness features, which is returned after successful detection.

 |
| 

securedImageBuffer

 | 

ArrayBuffer

 | 

No

 | 

Yes

 | 

Secure stream, which is returned in the image security verification scenario.

 |
| 

certificate

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Certificate chain, which is returned in the image security verification scenario.

 |

#### getInteractiveLivenessResult

getInteractiveLivenessResult(): Promise<InteractiveLivenessResult>

Obtains the face liveness detection result. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.LivenessDetect

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[InteractiveLivenessResult](#section173751154134515)\>

 | 

Face liveness detection result, which is returned through a promise. If the detection is successful, the liveness detection mode and a detection image are returned. If the detection fails, the error code and message are returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1008302000

 | 

Detection algorithm initialization.

 |
| 

1008302001

 | 

Detection timeout.

 |
| 

1008302002

 | 

Action mutual exclusion error.

 |
| 

1008302003

 | 

Continuity Check Failure.

 |
| 

1008302004

 | 

The test is not complete.

 |

**Example**:

import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

interactiveLiveness.getInteractiveLivenessResult().then(data => {
  hilog.info(0x0001, "LivenessCollectionIndex", \`Succeeded in detecting.\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0001, "LivenessCollectionIndex", \`Failed to detect. Code: ${err.code}, message: ${err.message}\`);
})

#### Action Description

| 
Action

 | 

Description

 |
| :-- | :-- |
| 

1

 | 

Nod.

 |
| 

2

 | 

Open mouth.

 |
| 

3

 | 

Blink.

 |
| 

4

 | 

Turn face left.

 |
| 

5

 | 

Turn face right.

 |
| 

6

 | 

Gaze.

 |
