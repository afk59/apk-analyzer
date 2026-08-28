# sceneManager (Ecosystem Query Service)

This module allows you to query scene values of your app or atomic service, and obtain information about ad signature verification.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/OdBn_ff-TkCV4A-Lh7gnLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD5C1693EAAF6DE8B60A430FC963DF060B9ABBACF13715A9609A94B8A3B10589)

Exceptions need to be captured when an API is called.

**Start version**: 4.1.0(11)

#### Modules to Import

import { sceneManager } from '@kit.AppGalleryKit';

#### sceneManager.getSelfSceneCode

getSelfSceneCode(): string

Obtains the scene value of your app or atomic service. Exceptions need to be captured when this API is called.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.BundleManager.EcologicalRuleManager.SceneManager

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Scene value of your app or atomic service.

 |

**Example**:

import { sceneManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const selfSceneCode: string = sceneManager.getSelfSceneCode();
  hilog.info(0, 'TAG', "Succeeded in getting SelfSceneCode res = " + selfSceneCode);
} catch (err) {
  hilog.error(0, 'TAG', \`get self sceneCode failed.code is ${err.code}, message is ${err.message}\`);
}

#### sceneManager.getAdsVerificationVersion

getAdsVerificationVersion(): number

Obtains the ad signature verification version. Exceptions need to be captured when this API is called.

**System capability**: SystemCapability.BundleManager.EcologicalRuleManager.SceneManager

**Start version**: 4.1.0(11)

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

Ad signature verification version. The return value is **1**.

In the advertising scenario, you need to include the following parameters in the **want** parameter: **ohos.market.param.signature**, **ohos.market.param.ad\_networkid**, **ohos.market.param.timestamp**, **ohos.market.param.verify\_version**, and **ohos.market.param.ad\_nonce**. These parameters and the public key will be used for signature verification.

 |

**Example**:

import { sceneManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const version: number = sceneManager.getAdsVerificationVersion();
  hilog.info(0, 'TAG', "Succeeded in getting AdsVerificationVersion res = " + version);
} catch (err) {
  hilog.error(0, 'TAG', \`get ads verification version failed.code is ${err.code}, message is ${err.message}\`);
}
