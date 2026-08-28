# privacyManager (Privacy Agreement Management Service)

This module provides functions for querying privacy agreement URLs, querying the privacy agreement signing status, terminating privacy agreements, and launching a standardized privacy agreement pop-up.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/KuekkAr2TuaXOhWETcREYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02E3187D129B6BC6B11CF546D5BE3A3072931A177E3B142AF68E2383D6DFFD6F)

Exceptions need to be captured when an API is called.

**Start version**: 5.0.0(12)

#### Modules to Import

import { privacyManager } from '@kit.AppGalleryKit';

#### AppPrivacyMgmtType

Enumerated privacy agreement management types.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

UNSUPPORTED

 | 

0

 | 

Not supported.

 |
| 

FULL\_MODE

 | 

1

 | 

Full mode.

 |

#### AppPrivacyResultType

Enumerated privacy agreement signing results.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

DISAGREED

 | 

0

 | 

The user has not agreed to the privacy agreement.

 |
| 

FULL\_MODE\_AGREED

 | 

1

 | 

The user has agreed to the privacy agreement for using the full mode.

 |
| 

REQUIRE\_RESIGNING\_VERSION\_UPDATE

 | 

2

 | 

The agreement has changed and needs to be signed again.

 |

#### AppPrivacyLinkType

Enumerated privacy agreement URL types.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

PRIVACY\_STATEMENT\_LINK

 | 

1

 | 

Privacy statement URL.

 |
| 

USER\_AGREEMENT\_LINK

 | 

2

 | 

User agreement URL.

 |

#### AppPrivacyType

Enumerated privacy agreement types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

PRIVACY\_AGREEMENT

 | 

1

 | 

Privacy statement.

 |
| 

USER\_AGREEMENT

 | 

2

 | 

User agreement.

 |

#### AppPrivacyMgmtInfo

Privacy agreement management information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

type

 | 

[AppPrivacyMgmtType](#section45163241117)

 | 

Yes

 | 

No

 | 

Privacy agreement management type.

 |
| 

privacyInfo

 | 

[AppPrivacyLink](#section1387252994814)\[\]

 | 

Yes

 | 

No

 | 

Privacy agreement URL information.

 |

#### AppPrivacyLink

Privacy agreement URL.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

type

 | 

[AppPrivacyLinkType](#section620013574390)

 | 

Yes

 | 

No

 | 

Privacy agreement URL type.

 |
| 

versionCode

 | 

number

 | 

Yes

 | 

No

 | 

Agreement version.

 |
| 

url

 | 

string

 | 

Yes

 | 

No

 | 

URL.

 |
| 

id

 | 

string

 | 

Yes

 | 

No

 | 

Privacy agreement ID.

 |
| 

name

 | 

string

 | 

Yes

 | 

Yes

 | 

User agreement name. This parameter is mandatory when [AppPrivacyLinkType](#section620013574390) is set to **USER\_AGREEMENT\_LINK**.

NOTE:

**Start version**: 5.0.2(14)

 |

#### AppPrivacyResult

Privacy agreement signing result.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

type

 | 

[AppPrivacyType](#section1678973094110)

 | 

Yes

 | 

No

 | 

Privacy agreement type.

 |
| 

versionCode

 | 

number

 | 

Yes

 | 

No

 | 

Agreement version.

 |
| 

result

 | 

[AppPrivacyResultType](#section194882568246)

 | 

Yes

 | 

No

 | 

Privacy agreement signing result.

 |
| 

id

 | 

string

 | 

Yes

 | 

No

 | 

Privacy agreement ID.

 |
| 

signingTimestamp

 | 

number

 | 

Yes

 | 

Yes

 | 

Privacy agreement signing time, in milliseconds.

NOTE:

**Start version**: 5.0.2(14)

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |

#### ConsentResult

Result of launching the standardized privacy agreement pop-up.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

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

results

 | 

[AppPrivacyResult](#section12860134614530)\[\]

 | 

Yes

 | 

No

 | 

Privacy agreement signing result.

 |

#### privacyManager.getAppPrivacyMgmtInfo

getAppPrivacyMgmtInfo(): AppPrivacyMgmtInfo

Queries privacy agreement URLs.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AppPrivacyMgmtInfo](#section1535385414136)

 | 

Privacy agreement URL information.

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

1006700001

 | 

System internal error.

 |
| 

1006700003

 | 

The application does not use privacy manager service.

 |

**Example**:

import { privacyManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let appPrivacyManageInfo: privacyManager.AppPrivacyMgmtInfo = privacyManager.getAppPrivacyMgmtInfo();
  hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyManageInfo type: " + appPrivacyManageInfo\["type"\]);
  let privacyLinkInfoArray : privacyManager.AppPrivacyLink\[\] = appPrivacyManageInfo.privacyInfo;
  hilog.info(0, 'TAG', "GetAppPrivacyManageInfo size = " + privacyLinkInfoArray.length);
  for (let i = 0; i < privacyLinkInfoArray.length; i++) {
    hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyManageInfo type = " + privacyLinkInfoArray\[i\]\["type"\] + ", version = " + privacyLinkInfoArray\[i\]\["versionCode"\] + ", url = " + privacyLinkInfoArray\[i\]\["url"\]);
  }
} catch (error) {
  hilog.error(0, 'TAG', "GetAppPrivacyManageInfoPublic exception code: " + error.code + ", exception message: " + error.message);
}

#### privacyManager.getAppPrivacyResult

getAppPrivacyResult(): AppPrivacyResult\[\]

Queries the privacy agreement signing status.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AppPrivacyResult](#section12860134614530)\[\]

 | 

Privacy agreement signing result.

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

1006700001

 | 

System internal error.

 |
| 

1006700003

 | 

The application does not use privacy manager service.

 |

**Example**:

import { privacyManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let appPrivacyResults: privacyManager.AppPrivacyResult\[\] = privacyManager.getAppPrivacyResult();
  hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyResult size = " + appPrivacyResults.length);
  for (let i = 0; i < appPrivacyResults.length; i++) {
    hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyResult type = " + appPrivacyResults\[i\]\["type"\] + ", version = " + appPrivacyResults\[i\]\["versionCode"\] + ", result = "+appPrivacyResults\[i\]\["result"\]);
  }
} catch (error) {
  hilog.error(0, 'TAG', "GetAppPrivacyResultPublic exception code: " + error.code + ", exception message: " + error.message);
}

#### privacyManager.disableService

disableService(): void

Terminates privacy agreements.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1006700001

 | 

System internal error.

 |
| 

1006700002

 | 

The specified service extension connect failed.

 |
| 

1006700003

 | 

The application does not use privacy manager service.

 |

**Example**:

import { privacyManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  privacyManager.disableService();
  hilog.info(0, 'TAG', "Succeeded in disabling service.");
} catch (error) {
  hilog.error(0, 'TAG', "DisableService exception code: " + error.code + ", exception message: " + error.message);
}

#### privacyManager.requestAppPrivacyConsent

requestAppPrivacyConsent(context:common.UIAbilityContext):Promise<ConsentResult>

Launches the standardized privacy agreement pop-up and returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.PrivacyManager

**Start version**: 5.0.2(14)

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

context

 |    | 

Yes

 | 

Context of the app that calls the API.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ConsentResult](#section5439151165618)\>

 | 

Pop-up launch result returned through a promise.

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

1006700001

 | 

System internal error.

 |
| 

1006700003

 | 

The application does not use privacy manager service.

 |

**Example**:

import { privacyManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'requestAppPrivacyConsent test'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
              privacyManager.requestAppPrivacyConsent(uiContext).then((consentResult : privacyManager.ConsentResult) => {
                let appPrivacyResults: privacyManager.AppPrivacyResult\[\] = consentResult\["results"\];
                for (let i = 0; i < appPrivacyResults.length; i++) {
                  hilog.info(0, 'TAG', "GetAppPrivacyResult type = " + appPrivacyResults\[i\]\["type"\] + ", version = " + appPrivacyResults\[i\]\["versionCode"\] + ", result = " + appPrivacyResults\[i\]\["result"\] + ", signingTimeStamp = " + appPrivacyResults\[i\]\["signingTimeStamp"\]);
                }
              }).catch((error: BusinessError<Object>) => {
                hilog.error(0, 'TAG', \`requestAppPrivacyConsent failed, Code: ${error.code}, message: ${error.message}\`);
              });
            } catch (error) {
              hilog.error(0, 'TAG', "requestAppPrivacyConsent exception code: " + error.code + ", exception message: " + error.message);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
