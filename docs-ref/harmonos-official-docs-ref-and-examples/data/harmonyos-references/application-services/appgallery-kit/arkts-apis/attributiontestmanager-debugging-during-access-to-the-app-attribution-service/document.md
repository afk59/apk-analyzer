# attributionTestManager (Debugging During Access to the App Attribution Service)

This module offers debugging capabilities that include verifying attribution sources, configuring attribution result postback, and initiating the postback of attribution results.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/bGckmzsQSvOuBjpzP_bhkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE3C38570F2401F67D65EF9A048BFAB1AA7575AEED7A5AA5E45038ECC1DE49D2)

Exceptions need to be captured when an API is called.

**Start version**: 5.0.0(12)

#### Modules to Import

import { attributionTestManager } from '@kit.AppGalleryKit'; 

#### attributionTestManager.validateSource

validateSource(adSourceInfo: AdSourceInfo, publicKey: string): Promise<void>

Verifies attribution sources registered by the media app or distribution platform. This API returns the result asynchronously through a promise.

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

[AdSourceInfo](#section1262013338292)

 | 

Yes

 | 

Attribution source information registered by the media app or distribution platform.

 |
| 

publicKey

 | 

string

 | 

Yes

 | 

Public key obtained from [Generating a Key Pair](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-register#section1810151768). It is provided for the cloud platform of the app attribution service during attribution role registration.

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

1009300101

 | 

AdTechId is missing in the request.

 |
| 

1009300102

 | 

CampaignId is missing in the request.

 |
| 

1009300104

 | 

DestinationId is missing in the request.

 |
| 

1009300105

 | 

SourceType is missing in the request.

 |
| 

1009300106

 | 

Nonce is missing in the request.

 |
| 

1009300107

 | 

Timestamp is missing in the request.

 |
| 

1009300108

 | 

Signature is missing in the request.

 |
| 

1009300111

 | 

AdSourceInfo is missing in the request.

 |
| 

1009300112

 | 

PublicKey is missing in the request.

 |
| 

1009300114

 | 

The signature verification failed in the testing environment.

 |

**Example**:

import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionTestManager } from '@kit.AppGalleryKit';
import { SignUtil } from '../common/utils/SignUtil'; // Refer to the code of the [signature generation method](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/appgallery-attribution-appendix-triger#section5203225132112) in the appendix of the development guide.
import { util } from '@kit.ArkTS';

const TAG: string = 'AttributionTest';

class  AttributionTest {

  async validateSource(): Promise<void> {
    try {
      // Public key provided during role registration on the cloud platform of the app attribution service, along with its corresponding private key. You can customize the values for debugging purposes.
      let privateKey: string = '';
      let publicKey: string = '';
      // Allocated by the app attribution service during role registration on the cloud platform of the app attribution service.
      let adTechId: string = '12345678';
      // ID of the marketing task created by the distribution platform.
      let campaignId: string = '123456';
      // ID of the developer's app released on AppGallery, without letter C.
      let destinationId: string = '102345678';
      // ID of the attribution monitoring platform.
      let mmpIds: string\[\] = \['12345678', '23456789'\];
      // Business information that the distribution platform focuses on.
      let serviceTag: string = 'testServiceTag';
      // Random number without hyphens (-), used for signature calculations.
      let nonce: string = util.generateRandomUUID().replace(/-/g, '');
      // Timestamp.
      let timestamp: number = Date.now()
      let adSourceInfo: attributionTestManager.AdSourceInfo = {
        adTechId: adTechId,
        campaignId: campaignId,
        destinationId: destinationId,
        // Attribution source: impression.
        sourceType: attributionTestManager.SourceType.IMPRESSION,
        mmpIds: mmpIds,
        serviceTag: serviceTag,
        nonce: nonce,
        timestamp: timestamp,
        // Signature.
        signature: await SignUtil.getSign(SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp), privateKey)
      };

      await attributionTestManager.validateSource(adSourceInfo, publicKey);
      hilog.info(0, TAG, 'Succeeded in validating source.');
    } catch (error) {
      hilog.error(0, TAG, \`validateSource error.code is ${error.code}, message is ${error.message}\`);
    }
  }
}

#### attributionTestManager.setPostback

setPostback(postbackInfo: PostbackInfo): Promise<void>

Sets attribution result postback. It is used for verifying the validity of **triggerData** and setting the attribution result that can be posted back for debugging purposes. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/L5FZajxSTlS1AQZaqL_xkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B1E015CACEDD97552873650E515CB54D10A101065D26E53F0CBF607E3E1AC6E)

For a single **adTechId**, the number of **postbackInfo** records to be posted back for debugging purposes should not exceed 5.

For a single device, the number of **postbackInfo** records to be posted back for debugging purposes should not exceed 100.

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

postbackInfo

 | 

[PostbackInfo](#section1812319373298)

 | 

Yes

 | 

Attribution result information that can be posted back.

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

1009300101

 | 

AdTechId is missing in the request.

 |
| 

1009300102

 | 

CampaignId is missing in the request.

 |
| 

1009300103

 | 

SourceId is missing in the request.

 |
| 

1009300104

 | 

DestinationId is missing in the request.

 |
| 

1009300109

 | 

TriggerData is missing in the request.

 |
| 

1009300110

 | 

PostbackUrl is missing in the request.

 |
| 

1009300113

 | 

PostbackInfo is missing in the request.

 |
| 

1009300115

 | 

Too many postbacks setting to the testing environment.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionTestManager } from '@kit.AppGalleryKit';

const TAG: string = 'AttributionTest';

class AttributionTest {

  setPostback(): void {
    try {
      let postbackInfo: attributionTestManager.PostbackInfo = {
        adTechId: '12345678',
        campaignId: '123456',
        sourceId: '112345678',
        destinationId: '102345678',
        serviceTag: 'testServiceTag',
        businessScene: 5,
        triggerData: 123,
        postbackUrl: 'https://xxx.com'
      };
      attributionTestManager.setPostback(postbackInfo).then(() => {
        hilog.info(0, TAG, 'Succeeded in setting postback.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, \`setPostback onError.code is ${error.code}, message is ${error.message}\`);
      })
    } catch (error) {
      hilog.error(0, TAG, \`setPostback onError.code is ${error.code}, message is ${error.message}\`);
    }
  }
}

#### attributionTestManager.flushPostbacks

flushPostbacks(adTechId: string): Promise<void>

Triggers attribution result postback. It checks whether the logic of your server for receiving and processing the attribution result is correct and returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/5WeNYt-zRi-pI16ar_td7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A92A6E462BD5EDBB0250B17EF608EFD6E5D7A0B185DB54EA60551BB555D1636)

On a single device, this API can be called at most once every 5 seconds.

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

adTechId

 | 

string

 | 

Yes

 | 

Attribution role ID of a distribution platform. This identifier specifies the distribution platform to which the marketing task of the registered attribution source belongs. The value must consist of eight characters.

Use the value of **adTechId** that is successfully set in the **setPostback()** API.

NOTE:

The debugging process does not depend on the registration on the cloud platform. You can use a virtual value of **adTechId**.

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

1009300101

 | 

AdTechId is missing in the request.

 |
| 

1009300116

 | 

There is no postback to be sent of this adTechId.

 |
| 

1009300117

 | 

Failed to send postbacks to the postbackUrl.

 |
| 

1009300119

 | 

Network error.

 |
| 

1009300120

 | 

Request too frequent.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { attributionTestManager } from '@kit.AppGalleryKit';

const TAG: string = 'AttributionTest';

class AttributionTest {
  flushPostbacks(): void {
    try {
      let adTechId: string = '12345678';
      attributionTestManager.flushPostbacks(adTechId).then(() => {
        hilog.info(0, TAG, 'Succeeded in flushing postbacks.');
      }).catch((error: BusinessError) => {
        hilog.error(0, TAG, \`flushPostbacks onError.code is ${error.code}, message is ${error.message}\`);
      })
    } catch (error) {
      hilog.error(0, TAG, \`flushPostbacks onError.code is ${error.code}, message is ${error.message}\`);
    }
  }
}

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

NOTE:

The debugging process does not depend on the registration on the cloud platform. You can use a virtual value of **adTechId**.

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

[SourceType](#section142399205014)

 | 

No

 | 

No

 | 

Attribution source.

**0**: impression

**1**: click

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

Unix timestamp in milliseconds, representing the time when the ad is requested, that is, the time when the ad is delivered. The deviation from the current time should not exceed 10 minutes.

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

#### PostbackInfo

Data to be posted back.

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

Use the value of **adTechId** that is successfully set in the **setPostback()** API.

NOTE:

The debugging process does not depend on the registration on the cloud platform. You can use a virtual value of **adTechId**.

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

sourceId

 | 

string

 | 

No

 | 

No

 | 

Media app ID. The value contains a maximum of 64 characters.

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

If the caller specifies **serviceTag**, the app attribution service will post back this parameter to the distribution platform. If the caller does not specify **serviceTag**, the distribution platform cannot receive it.

 |
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

The value ranges from 0 to 999.

 |
| 

postbackUrl

 | 

string

 | 

No

 | 

No

 | 

URL for receiving attribution results. HTTPS is recommended.

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
