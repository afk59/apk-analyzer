# @ohos.advertising (Ads Kit Framework)

This module provides APIs for requesting and displaying ads.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/2LN-CUFPSlKCIrITmenZQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=884C7FBB3D612920D639FB1EEF56BD43A88DF17F0F2F964FE84667161EBA36A4)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { advertising } from '@kit.AdsKit';

#### advertising.showAd

showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void

Displays a full-screen ad.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ad

 | 

[Advertisement](#advertisement)

 | 

Yes

 | 

Ad object.

 |
| 

options

 | 

[AdDisplayOptions](#addisplayoptions)

 | 

Yes

 | 

Ad display parameters.

 |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

No

 | 

Context of the **UIAbility**. If this parameter is not set, the value is obtained from **@ohos.app.ability.common**.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

 |
| 

21800001

 | 

System internal error.

 |
| 

21800004

 | 

Failed to display the ad.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/DyU7m45bST2zU64ANDDFDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4236A4B754C1891C05A4BC2964D42E2A6E22BE4CE474F97F56CF43C10E248A9D)

1\. To ensure that ads can be correctly displayed, this API must be used together with the ad request API.

2\. This API can be used to display only rewarded ads and interstitial ads.

**Example**:

For details about how to obtain the context, please click [here](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#acquisition-of-context).

import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';

function showAd(ad: advertising.Advertisement, context?: common.UIAbilityContext): void {
  // Ad display parameters, which can be set based on the project requirements.
  const adDisplayOptions: advertising.AdDisplayOptions = {};
  // Call the API for displaying a full-screen ad.
  advertising.showAd(ad, adDisplayOptions, context);
}

#### advertising.getAdRequestBody12+

getAdRequestBody(adParams: AdRequestParams\[\], adOptions: AdOptions): Promise<string>

Obtains the ad request body. This API returns the result asynchronously through a promise. (This API is available only to some pre-installed system apps.)

**System capability**: SystemCapability.Advertising.Ads

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

adParams

 | 

[AdRequestParams](#adrequestparams)\[\]

 | 

Yes

 | 

Ad request parameters.

**Note**: The **adId** parameter can be left empty for this API.

 |
| 

adOptions

 | 

[AdOptions](#adoptions)

 | 

Yes

 | 

Ad configuration parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Ad data of the string type returned by a promise.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

Device not supported.

 |
| 

21800001

 | 

System internal error.

 |

**Example**:

import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getAdRequestBody(adRequestParamsArray: advertising.AdRequestParams\[\]): Promise<void> {
  // Ad configuration parameters, which can be set based on the project requirements.
  const adOptions: advertising.AdOptions = {};
  await advertising.getAdRequestBody(adRequestParamsArray, adOptions).then((data: string) => {
    hilog.info(0x0000, 'testTag', \`Succeeded in getting ad request body. Data is ${data}\`);
  }).catch((error: BusinessError) => {
    hilog.info(0x0000, 'testTag', \`Failed to get ad request body. Code is ${error.code}, message is ${error.message}\`);
  });
}

#### advertising.parseAdResponse12+

parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, context: common.UIAbilityContext): void

Parses and processes the ad response body. (This API is available only to some pre-installed system apps.)

**System capability**: SystemCapability.Advertising.Ads

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

adResponse

 | 

string

 | 

Yes

 | 

Ad response body.

 |
| 

listener

 | 

[MultiSlotsAdLoadListener](#multislotsadloadlistener)

 | 

Yes

 | 

Ad request callback listener.

 |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

Device not supported.

 |
| 

21800001

 | 

System internal error.

 |
| 

21800005

 | 

Failed to parse the ad response.

 |

**Example**:

For details about how to obtain the context, please click [here](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#acquisition-of-context).

import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function parseAdResponse(adResponse: string, context: common.UIAbilityContext): void {
  // Ad parsing and processing callback listener.
  const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
    onAdLoadFailure: (errorCode: number, errorMsg: string) => {
      hilog.error(0x0000, 'testTag', \`Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}\`);
    },
    onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
      // Save the ad content that has been parsed and processed for display.
      const returnAds: advertising.Advertisement\[\] = \[\];
      ads.forEach((adsArray) => returnAds.push(...adsArray));
    }
  };
  // Call the API to parse the response body.
  advertising.parseAdResponse(adResponse, multiSlotsAdLoaderListener, context);
}

#### advertising.registerWebAdInterface12+

registerWebAdInterface(controller: web\_webview.WebviewController, context: common.UIAbilityContext): void

Injects a JavaScript ad object to the **Web** component. (This API is available only for some pre-installed apps.)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

controller

 | 

web\_webview.[WebviewController](../../../../application-framework/arkweb/arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md)

 | 

Yes

 | 

**Web** component controller.

 |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

 |
| 

21800001

 | 

System internal error.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private webViewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('registerWebAdInterface')
        .onClick(() => {
          advertising.registerWebAdInterface(this.webViewController, this.context);
        })
      // ...

      Web({ src: 'https://www.example.com', controller: this.webViewController })
    }
    .width('100%')
    .height('100%')
  }
}

#### advertising.registerWebAdInterface16+

registerWebAdInterface(controller: web\_webview.WebviewController, context: common.UIAbilityContext, needRefresh: boolean): void

Injects a JavaScript ad object to the **Web** component. (This API is available only for some pre-installed apps.)

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.Advertising.Ads

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

controller

 | 

web\_webview.[WebviewController](../../../../application-framework/arkweb/arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md)

 | 

Yes

 | 

**Web** component controller.

 |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |
| 

needRefresh

 | 

boolean

 | 

Yes

 | 

Indicates whether to refresh a page. **true**: yes; **false**: no.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes: Mandatory parameters are left unspecified.

 |
| 

21800001

 | 

System internal error.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private webViewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // ...
      Button('registerWebAdInterface')
        .onClick(() => {
          advertising.registerWebAdInterface(this.webViewController, this.context, true);
        })

      Web({ src: 'https://www.example.com', controller: this.webViewController })
    }
    .width('100%')
    .height('100%')
  }
}

#### advertising.deleteWebAdInterface16+

deleteWebAdInterface(controller: web\_webview.WebviewController, needRefresh: boolean): void

Deletes the JavaScript ad object injected through **registerWebAdInterface**. (This API is available only to some pre-installed apps.)

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.Advertising.Ads

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

controller

 | 

web\_webview.[WebviewController](../../../../application-framework/arkweb/arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md)

 | 

Yes

 | 

**Web** component controller.

 |
| 

needRefresh

 | 

boolean

 | 

Yes

 | 

Indicates whether to refresh a page. **true**: yes; **false**: no.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes: Mandatory parameters are left unspecified.

 |
| 

21800001

 | 

System internal error.

 |

**Example**:

import { advertising } from '@kit.AdsKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  private webViewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('deleteWebAdInterface')
        .onClick(() => {
          advertising.deleteWebAdInterface(this.webViewController, true);
        })

      Web({ src: 'https://www.example.com', controller: this.webViewController })
    }
    .width('100%')
    .height('100%')
  }
}

#### AdLoader

Provides the function of loading ads.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

#### \[h2\]constructor

constructor(context: common.Context)

Constructor.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of **ability** or **application**.

 |

**Example**:

For details about how to obtain the context, please click [here](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#acquisition-of-context).

import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
// ...

function createAdLoader(context: common.Context): void {
  const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
}

#### \[h2\]loadAd

loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void

Requests an ad from one ad unit.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

adParam

 | 

[AdRequestParams](#adrequestparams)

 | 

Yes

 | 

Ad request parameters.

 |
| 

adOptions

 | 

[AdOptions](#adoptions)

 | 

Yes

 | 

Ad configuration parameters.

 |
| 

listener

 | 

[AdLoadListener](#adloadlistener)

 | 

Yes

 | 

Ad request callback listener.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

Device not supported.

 |
| 

21800001

 | 

System internal error.

 |
| 

21800003

 | 

Failed to load the ad request.

 |

**Example**:

For details about how to obtain the context, please click [here](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#acquisition-of-context).

import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// ...
function loadAd(context: common.Context, adRequestParams: advertising.AdRequestParams): void {
  // Ad configuration parameters, which can be set based on the project requirements.
  const adOptions: advertising.AdOptions = {};
  // Ad request callback listener.
  const adLoaderListener: advertising.AdLoadListener = {
    onAdLoadFailure: (errorCode: number, errorMsg: string) => {
      hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
    },
    onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
      // Save the requested ad content for display.
      const returnAds: advertising.Advertisement\[\] = ads;
    }
  };
  // Create an **AdLoader** ad object.
  const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
  // Call the API for requesting ads.
  adLoader.loadAd(adRequestParams, adOptions, adLoaderListener);
}

#### \[h2\]loadAdWithMultiSlots

loadAdWithMultiSlots(adParams: AdRequestParams\[\], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void

Requests ads from multiple ad units.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

adParams

 | 

[AdRequestParams](#adrequestparams)\[\]

 | 

Yes

 | 

Ad request parameters.

 |
| 

adOptions

 | 

[AdOptions](#adoptions)

 | 

Yes

 | 

Ad configuration parameters.

 |
| 

listener

 | 

[MultiSlotsAdLoadListener](#multislotsadloadlistener)

 | 

Yes

 | 

Ad request callback listener.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/ads-kit-framework-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

Device not supported.

 |
| 

21800001

 | 

System internal error.

 |
| 

21800003

 | 

Failed to load the ad request.

 |

**Example**:

For details about how to obtain the context, please click [here](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#acquisition-of-context).

import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// ...
function loadAdWithMultiSlots(context: common.Context, adRequestParamsArray: advertising.AdRequestParams\[\]): void {
  // Ad configuration parameters, which can be set based on the project requirements.
  const adOptions: advertising.AdOptions = {};
  // Ad request callback listener.
  const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
    onAdLoadFailure: (errorCode: number, errorMsg: string) => {
      hilog.error(0x0000, 'testTag', \`Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}\`);
    },
    onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
      // Save the requested ad content for display.
      const returnAds: advertising.Advertisement\[\] = \[\];
      ads.forEach((adsArray) => returnAds.push(...adsArray));
    }
  };
  // Create an **AdLoader** ad object.
  const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
  // Call the API for requesting ads.
  adLoader.loadAdWithMultiSlots(adRequestParamsArray, adOptions, multiSlotsAdLoaderListener);
}

#### AdLoadListener

Callback for requesting an ad from a single ad unit.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

#### \[h2\]onAdLoadFailure

onAdLoadFailure(errorCode: number, errorMsg: string): void

Called when an ad request fails.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

errorCode

 | 

number

 | 

Yes

 | 

Error code indicating an ad request failure.

 |
| 

errorMsg

 | 

string

 | 

Yes

 | 

Message indicating an ad request failure.

 |

**Example**:

import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const adLoaderListener: advertising.AdLoadListener = {
  onAdLoadFailure: (errorCode: number, errorMsg: string) => {
    hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
  },
  onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
  }
}

#### \[h2\]onAdLoadSuccess

onAdLoadSuccess(ads: Array<Advertisement>): void

Called upon ad request success.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ads

 | 

Array<[Advertisement](#advertisement)\>

 | 

Yes

 | 

Ad data.

 |

**Example**:

import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const adLoaderListener: advertising.AdLoadListener = {
  onAdLoadFailure: (errorCode: number, errorMsg: string) => {
    hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
  },
  onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
  }
}

#### MultiSlotsAdLoadListener

Callback for requesting ads from multiple ad units.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

#### \[h2\]onAdLoadFailure

onAdLoadFailure(errorCode: number, errorMsg: string): void

Called upon failure to request ads from multiple ad units.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

errorCode

 | 

number

 | 

Yes

 | 

Error code indicating an ad request failure.

 |
| 

errorMsg

 | 

string

 | 

Yes

 | 

Message indicating an ad request failure.

 |

**Example**:

import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const multiSlotsAdLoadListener: advertising.MultiSlotsAdLoadListener = {
  onAdLoadFailure: (errorCode: number, errorMsg: string) => {
    hilog.info(0x0000, 'testTag', \`onAdLoadFailure errorCode is: ${errorCode},errorMsg is: ${errorMsg}\`);
  },
  onAdLoadSuccess: (adsMap: Map<string, Array<advertising.Advertisement>>) => {
    hilog.info(0x0000, 'testTag', 'onAdLoadSuccess');
  }
}

#### \[h2\]onAdLoadSuccess

onAdLoadSuccess(adsMap: Map<string, Array<Advertisement>>): void

Called upon success to request ads from multiple ad units.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

adsMap

 | 

Map<string, Array<[Advertisement](#advertisement)\>>

 | 

Yes

 | 

Ad data.

 |

**Example**:

import { advertising } from '@kit.AdsKit';

const multiSlotsAdLoadListener: advertising.MultiSlotsAdLoadListener = {
  onAdLoadFailure: (errorCode: number, errorMsg: string) => {
  },
  onAdLoadSuccess: (adsMap: Map<string, Array<advertising.Advertisement>>) => {
  }
}

#### AdInteractionListener

Ad status change callback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

#### \[h2\]onStatusChanged

onStatusChanged(status: string, ad: Advertisement, data: string)

Ad status callback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

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

status

 | 

string

 | 

Yes

 | 

Ad display status.

-   **onAdLoad**: An ad is loaded successfully.
-   **onAdFail**: An ad fails to be loaded.

-   **onAdOpen**: An ad is opened.
-   **onAdClick**: An ad is clicked.
-   **onAdClose**: An ad is closed.
-   **onMediaProgress**: The ad playback progress changes.
-   **onMediaStart**: An ad starts to be played.
-   **onMediaPause**: An ad playback is paused.
-   **onMediaStop**: An ad playback stops.
-   **onMediaComplete**: An ad playback is complete.
-   **onMediaCountDown**: The ad playback countdown is updated.
-   **onMediaError**: An ad fails to be played.
-   **onLandscape**: The full screen button is tapped when the device is in portrait mode.
-   **onPortrait**: The back button is tapped when the device is in full screen mode.
-   **onBackClicked**: The back button is tapped.

 |
| 

ad

 | 

[Advertisement](#advertisement)

 | 

Yes

 | 

Content of the ad whose status changes.

 |
| 

data

 | 

string

 | 

Yes

 | 

Extended information.

When **status** is set to **onAdClose**, **data** indicates the ad closing reason. The possible reasons are as follows:

-   **adShowEnded**: The ad display ends.
-   **adCloseBtnClicked**: The user tapped the close button.
-   **adSkipBtnClicked**: The user tapped the skip button.
-   **adFeedbackClosed**: The ad was closed due to negative feedback.
-   **adBackgroundClosed**: The splash ad was closed when the app switched to the background.

 |

**Example**:

import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const adInteractionListener: advertising.AdInteractionListener = {
  onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
    switch (status) {
      case 'onAdLoad':
        hilog.info(0x0000, 'testTag', 'Status is onAdLoad');
        break;
      case 'onAdFail':
        hilog.error(0x0000, 'testTag', 'Status is onAdFail');
        break;
      case 'onAdOpen':
        hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
        break;
      case 'onAdClick':
        hilog.info(0x0000, 'testTag', 'Status is onAdClick');
        break;
      case 'onAdClose':
        // The value of **data** indicates the reason for closing ads.
        hilog.info(0x0000, 'testTag', \`Status is onAdClose, Close Reason is ${data}\`);
        if (data === 'adShowEnded') {
          // The ad is closed because the ad display ends. You can add processing logic based on the actual scenario.
        }
        break;
      case 'onMediaProgress':
        hilog.info(0x0000, 'testTag', 'Status is onMediaProgress');
        break;
      case 'onMediaStart':
        hilog.info(0x0000, 'testTag', 'Status is onMediaStart');
        break;
      case 'onMediaPause':
        hilog.info(0x0000, 'testTag', 'Status is onMediaPause');
        break;
      case 'onMediaStop':
        hilog.info(0x0000, 'testTag', 'Status is onMediaStop');
        break;
      case 'onMediaComplete':
        hilog.info(0x0000, 'testTag', 'Status is onMediaComplete');
        break;
      case 'onMediaCountDown':
        hilog.info(0x0000, 'testTag', 'Status is onMediaCountDown');
        break;
      case 'onMediaError':
        hilog.info(0x0000, 'testTag', 'Status is onMediaError');
        break;
      case 'onLandscape':
        hilog.info(0x0000, 'testTag', 'Status is onLandscape');
        break;
      case 'onPortrait':
        hilog.info(0x0000, 'testTag', 'Status is onPortrait');
        break;
      case 'onBackClicked':
        hilog.info(0x0000, 'testTag', 'Status is onBackClicked');
        break;
      default:
        break;
    }
  }
}

#### AdOptions

Ad configuration parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

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

tagForChildProtection

 | 

number

 | 

No

 | 

Indicates whether you want your ad content to be treated as child-directed according to the regulations of COPPA.

-   **\-1** (default value): uncertain.

-   **0**: No.

-   **1**: Yes.

The default value is **\-1**.

 |
| 

adContentClassification

 | 

string

 | 

No

 | 

Maximum ad content rating.

-   **W**: aged 3 and up

-   **PI**: aged 7 and up, under parental guidance

-   **J**: teenagers aged 12 and up

-   **A**: adults aged 16 or 18 and up

If this parameter is left empty, the relevant setting in the service logic will be used.

 |
| 

nonPersonalizedAd

 | 

number

 | 

No

 | 

Indicates whether to request only non-personalized ads.

-   **0**: Request both personalized and non-personalized ads.

-   **1**: Request only non-personalized ads.

If this parameter is left empty, the relevant setting in the service logic will be used.

 |
| 

\[key: string\]

 | 

number | boolean | string | undefined

 | 

No

 | 

Custom parameters.

-   **totalDuration**: The value is of the number type, in seconds. This parameter is mandatory for roll ads and is used to set the roll ad display duration.

-   **allowMobileTraffic**: The value is of the number type. This parameter is optional. It specifies whether ad assets can be downloaded using mobile data. The options are **0** (no) and **1** (yes). If this parameter is not set, the advertiser's setting will be used.

-   **tagForUnderAgeOfPromise**: The value is of the number type. This parameter is optional. It specifies whether you want the ad request to be processed in a way that is suitable for users in the European Economic Area (EEA) who are below the legal age of consent. The options are as follows: **\-1** (default value): uncertain; **0**: no; **1**: yes.

 |

#### AdRequestParams

Ad request parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

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

adId

 | 

string

 | 

Yes

 | 

Ad unit ID.

**Note**: This parameter does not need to be passed for the [getAdRequestBody](#section85125201812) API.

 |
| 

adType

 | 

number

 | 

No

 | 

Requested ad type.

-   **1**: splash ad
-   **3**: native ad
-   **7**: rewarded ad
-   **8**: banner ad
-   **12**: interstitial ad
-   **60**: roll ad

If this parameter is left empty, the native ad is used by default.

 |
| 

adCount

 | 

number

 | 

No

 | 

Number of requested ads. If this parameter is left empty, the relevant setting in the service logic will be used.

 |
| 

adWidth

 | 

number

 | 

No

 | 

Expected creative width in the ad request, in vp. This parameter is mandatory for banner ads. If this parameter is left empty, the relevant setting in the service logic will be used.

 |
| 

adHeight

 | 

number

 | 

No

 | 

Expected creative height in the ad request, in vp. This parameter is mandatory for banner ads. If this parameter is left empty, the relevant setting in the service logic will be used.

 |
| 

adSearchKeyword

 | 

string

 | 

No

 | 

Ad keyword. If this parameter is left empty, **""** is used by default.

**Note**: Not supported currently.

 |
| 

\[key: string\]

 | 

number | boolean | string | undefined

 | 

No

 | 

Custom parameters.

-   **isPreload**: The value is of the boolean type. It specifies whether a roll ad request is a common online request or an asset preload request. **true**: asset preload request; **false**: common online request. The default value is **false**. This parameter is valid only for roll ads. It is not parsed in the requests of other ad types.
-   **enableDirectReturnVideoAd**: The value is of the boolean type. This is an extended parameter for native ads, specifying whether to directly return the ad without waiting for the download of all ad assets. **true**: Load assets online when displaying the ad without waiting for the download of all ad assets. **false**: Wait for the download of all ad assets and load them from the local cache when displaying the ad. If this parameter is left empty, the cloud-side configuration prevails. This parameter is valid only for native ads. It is not parsed in the requests of other ad types.
-   **oaid**: OAID, of the string type, which is used to precisely push ads. If this parameter is left empty, personalized ads cannot be obtained. The default value is **""**.
-   **tMax**: of the number type, indicating the maximum transaction timeout interval (including the network delay), in milliseconds.
-   **cur**: of the string type, indicating the currency supported by the bidding request. If there are multiple currencies, separate them with a comma (,). Currently, the following options are supported: **CNY**, **USD**, **EUR**, **GBP**, and **JPY**. If this parameter is left empty, the default value **CNY** will be used.
-   **bidFloor**: of the number type, indicating the minimum bid price for a real-time bidding ad unit.
-   **bidFloorCur**: of the string type, indicating the currency used for the minimum bid price of the ad unit. If **bidFloor** is not empty, **bidFloorCur** cannot be empty, either. Select one from the following options: **CNY**, **USD**, **EUR**, **GBP**, and **JPY**. If this parameter is left empty, the default value **CNY** will be used.
-   **bpkgName**: of the string type, indicating package names of apps that cannot be advertised. If there are multiple package names, separate them with a comma (,).
-   **orientation**: of the number type, indicating the screen orientation of the ad requested by the app. **1**: portrait mode; **0**: landscape mode. If this parameter is not set, the default value **1** will be used. Currently, no landscape-mode splash ad creatives are available. Therefore, if the orientation is set to landscape, no splash ad will be displayed. If the app is configured to always display in landscape mode, but **orientation** is not set or is set to **1**, the display effect will be affected.

 |

#### AdDisplayOptions

Ad display parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

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

customData

 | 

string

 | 

No

 | 

Custom data of the media. It is used by the Ads Kit server to notify the media server that a user should be rewarded for interacting with a rewarded video ad, so as to avoid spoofing. If this parameter is left empty, no notification is sent.

 |
| 

userId

 | 

string

 | 

No

 | 

Custom user ID. It is used by the Ads Kit server to notify the media server that a user should be rewarded for interacting with a rewarded video ad, so as to avoid spoofing. If this parameter is left empty, no notification is sent.

 |
| 

useMobileDataReminder

 | 

boolean

 | 

No

 | 

Indicates whether to display a pop-up to notify users when they use mobile data to play a video or download an app.

-   **true**: yes
-   **false**: no
-   This parameter depends on the mobile data pop-up function. Currently, the complete function is not supported, and therefore the default value is uncertain.

 |
| 

mute

 | 

boolean

 | 

No

 | 

Indicates whether to mute the ad video.

-   **true**: yes
-   **false**: no

If this parameter is left empty, the relevant setting in the service logic will be used.

 |
| 

audioFocusType

 | 

number

 | 

No

 | 

Scenario in which the audio focus can be obtained during video playback.

-   **0**: The focus is obtained when the video is played in mute or non-mute mode.
-   **1**: The focus is not obtained when the video is played in mute mode.
-   **2**: The focus is not obtained no matter whether the video is played in mute or non-mute mode.
-   Currently, the function on which this API depends is not supported, and therefore the default value is uncertain.

 |
| 

\[key: string\]

 | 

number | boolean | string | undefined

 | 

No

 | 

Custom parameters.

-   **refreshTime**: The value is of the number type, in ms. The value ranges from 30000 to 120000. This parameter is optional for **AutoAdComponent** and specifies the interval at which the ads rotate. If this parameter is set, ads are rotated at the interval specified by this parameter. Otherwise, ads are not rotated and only the first ad in the ad response is displayed.

 |

#### Advertisement

Ad content obtained.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads

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

adType

 | 

number

 | 

No

 | 

No

 | 

Ad type.

-   **1**: splash ad
-   **3**: native ad
-   **7**: rewarded ad
-   **8**: banner ad
-   **12**: interstitial ad
-   **60**: roll ad

If this parameter is left empty, the native ad is used by default.

 |
| 

uniqueId

 | 

string

 | 

No

 | 

No

 | 

Unique ID of an ad.

 |
| 

rewarded

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether users get rewarded for watching or clicking an ad.

-   **true**: yes
-   **false**: no

 |
| 

shown

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to display an ad.

-   **true**: yes
-   **false**: no

 |
| 

clicked

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether an ad can be clicked.

-   **true**: yes
-   **false**: no

 |
| 

rewardVerifyConfig

 | 

Map<string, string>

 | 

No

 | 

No

 | 

Server-side verification parameters.

{

customData: "test",

userId: "12345"

}

 |
| 

\[key: string\]

 | 

Object

 | 

No

 | 

Yes

 | 

Custom parameters.

-   **isFullScreen**: The value is of the boolean type. It specifies whether a splash ad is in full-screen mode. The value **true** means that the ad is in full-screen mode, and **false** means that the ad is in half-screen mode.
-   **biddingInfo**: of the Object type, used to obtain the real-time bidding result.
-   **biddingInfo.price**: The value is of the number type. It specifies the effective cost per mille (eCPM) for this ad, which represents the revenue generated for every 1000 impressions.
-   **biddingInfo.cur**: The value is of the string type. It specifies the currency of the ad price. Supported currencies: **CNY**, **USD**, **EUR**, **GBP**, and **JPY**.
-   **biddingInfo.nurl**: The value is of the string type. It specifies the URL used by the app to post back the bidding success result.
-   **biddingInfo.lurl**: The value is of the string type. It specifies the URL used by the app to notify Huawei of its bidding failure and the success of another vendor.

 |
