# attributionManager (App Attribution Service)

This module enables media apps and distribution platforms to register attribution sources with the app attribution service, and allows developers and attribution monitoring platforms to register conversion events with the app attribution service.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Hj2cn_PvTR25KYdsOfeUhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF254D3991CFB30BAC3D4C1D9F836274DE6D5205D343FDE152E2BC8D1C6A4E34)

Exceptions need to be captured when an API is called.

**Start version**: 5.0.0(12)

#### Modules to Import

import { attributionManager } from '@kit.AppGalleryKit';

#### AdSourceInfo

Attribution source information registered by the media app or distribution platform.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.AttributionManager

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

adTechId

 | 

string

 | 

No

 | 

No

 | 

Attribution role ID of a distribution platform. This identifier specifies the distribution platform to which the marketing task of the registered attribution source belongs.

This ID is assigned by the app attribution service when a distribution platform [registers an attribution role](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-register#section11218192952612) on the cloud platform of the app attribution service. It has a fixed length of eight characters.

 |
| 

campaignId

 | 

string

 | 

No

 | 

No

 | 

Marketing task ID, which is the ID of the marketing task corresponding to the registered attribution source. The value contains a maximum of six characters.

 |
| 

destinationId

 | 

string

 | 

No

 | 

No

 | 

ID of the app released on AppGallery. The value contains a maximum of 64 characters.

NOTE:

For details about how to obtain your app ID, please refer to [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

 |
| 

sourceType

 | 

[SourceType](#section648111185221)

 | 

No

 | 

No

 | 

Attribution source.

-   **0**: impression
-   **1**: click

 |
| 

mmpIds

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Attribution role ID of the attribution monitoring platform used in the current ad delivery task. A maximum of two IDs can be configured. Each ID contains eight characters.

If the caller passes the attribution monitoring platform ID, the app attribution service will post back the attribution result to the attribution monitoring platform. Without this ID, the attribution monitoring platform cannot receive the attribution result.

 |
| 

serviceTag

 | 

string

 | 

No

 | 

Yes

 | 

Business information that a distribution platform focuses on, such as creatives and assets. The value should not exceed 32 characters.

If the caller specifies **serviceTag**, the app attribution service will add this parameter to a trustlist (for details, please contact Huawei operations staff) and open it to the distribution platform. If the caller does not specify **serviceTag**, the distribution platform will not receive it.

 |
| 

nonce

 | 

string

 | 

No

 | 

No

 | 

Random number, used for signature calculations. The value of **nonce** is unique for each ad request and has a fixed length of 32 characters.

For the same **adTechId**, a single **nonce** can be used to register the attribution source information of up to five impressions and five clicks.

 |
| 

timestamp

 | 

number

 | 

No

 | 

No

 | 

Unix timestamp in milliseconds, representing the time when the ad is requested, that is, the time when the ad is delivered. Attribution source registration requires that the value not deviate from the current time by more than 10 minutes.

 |
| 

signature

 | 

string

 | 

No

 | 

No

 | 

Signature. A distribution platform or media app generates a signature based on the ad information and [attribution source signature calculation rules](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/appgallery-attribution-appendix-triger#section4208115642013). The value contains a maximum of 800 characters.

 |

#### AdTriggerInfo

Information about the conversion events registered by a developer.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.AttributionManager

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

businessScene

 | 

number

 | 

No

 | 

Yes

 | 

Business scene value, which is used to identify the business scenarios of a developer when the developer registers conversion events.

The value ranges from 0 to 99.

 |
| 

triggerData

 | 

number

 | 

No

 | 

No

 | 

Conversion event ID.

For [standard conversion events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-trigger-standard), the value ranges from 1 to 200.

For [custom conversion events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-trigger-custom), the value ranges from 501 to 600.

 |

#### SourceType

Enumerated attribution sources.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.AttributionManager

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

IMPRESSION

 | 

0

 | 

Impression.

 |
| 

CLICK

 | 

1

 | 

Click.

 |

#### attributionManager.registerSource

registerSource(adSourceInfo: AdSourceInfo): Promise<void>

Registers attribution sources, which is called by a media app or distribution platform. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.AttributionManager

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

adSourceInfo

 | 

[AdSourceInfo](#section0594928105511)

 | 

Yes

 | 

Attribution source information registered by the media app or distribution platform.

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

401

 | 

Parameter error.

 |
| 

1009300001

 | 

The specified service extension connect failed.

 |
| 

1009300002

 | 

System internal error.

 |
| 

1009300003

 | 

The identity check error.

 |
| 

1009300004

 | 

The sign check error.

 |

**Example**:

import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionManager } from '@kit.AppGalleryKit';
import { SignUtil } from '../common/utils/SignUtil';  // Refer to the code of the [signature generation method](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/appgallery-attribution-appendix-triger#section5203225132112) in the appendix of the development guide.
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = 'Attribution';

class  Attribution {
  async registerSource(): Promise<void> {
    try {
      // Private key corresponding to the public key provided during role registration on the cloud platform of the app attribution service.
      let privateKey: string =" ";
      // Allocated by the app attribution service during role registration on the cloud platform of the app attribution service.
      let adTechId: string = '20\*\*\*\*8';
      // ID of the marketing task created by the distribution platform.
      let campaignId: string = '123456';
      // ID of the developer's app released on AppGallery, without letter C.
      let destinationId: string = '691\*\*\*\*4';
      // ID of the attribution monitoring platform.
      let mmpIds: string\[\] = \['2f76e815'\];
      // Business information that the distribution platform focuses on.
      let serviceTag: string = 'testServiceTag';
      // Random number without hyphens (-), used for signature calculations.
      let nonce: string = util.generateRandomUUID().replace(/-/g, '');
      // Timestamp.
      let timestamp: number = Date.now()
      let adSourceInfo: attributionManager.AdSourceInfo = {
        adTechId: adTechId,
        campaignId: campaignId,
        destinationId: destinationId,
        // Attribution source: impression.
        sourceType: attributionManager.SourceType.IMPRESSION,
        mmpIds: mmpIds,
        serviceTag: serviceTag,
        nonce: nonce,
        timestamp: timestamp,
        // Signature.
        signature: await SignUtil.getSign(SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp), privateKey)
      };

      attributionManager.registerSource(adSourceInfo).then(() => {
        hilog.info(0, TAG, 'Succeeded in registering source.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, \`registerSource error.code is ${error.code}, message is ${error.message}\`);
      })
    } catch (error) {
      hilog.error(0, TAG, \`registerSource error.code is ${error.code}, message is ${error.message}\`);
    }
  }
}

#### attributionManager.registerTrigger

registerTrigger(adTriggerInfo: AdTriggerInfo): Promise<void>

Registers conversion events, which is called by developers. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.AttributionManager

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

adTriggerInfo

 | 

[AdTriggerInfo](#section6127112918554)

 | 

Yes

 | 

Conversion event information.

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

401

 | 

Parameter error.

 |
| 

1009300001

 | 

The specified service extension connect failed.

 |
| 

1009300002

 | 

System internal error.

 |
| 

1009300003

 | 

The identity check error.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionManager } from '@kit.AppGalleryKit';

const TAG: string = 'Attribution';

class Attribution {
  registerTrigger(): void {
    try {
      let adTriggerInfo: attributionManager.AdTriggerInfo = {
        businessScene: 5,
        // Conversion event ID, which is obtained from the cloud platform of the app attribution service.
        triggerData: 123
      };

      attributionManager.registerTrigger(adTriggerInfo).then(() => {
        hilog.info(0, TAG, 'Succeeded in registering triggerdata.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, \`registerTrigger error.code is ${error.code}, message is ${error.message}\`);
      })
    } catch (error) {
      hilog.error(0, TAG, \`registerTrigger error.code is ${error.code}, message is ${error.message}\`);
    }
  }
}
