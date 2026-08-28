# @ohos.app.ability.continueManager (Cross-Device Migration)

The continueManager module provides capabilities for managing cross-device application migration. For example, it allows you to obtain the result of quickly launching the target application during the cross-device migration process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/n9JBrrBpRW6TvN_olcdLpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92840C67C3C79CB819DC723AA991FB576BCF11B0B67503282C1080CBDA169402)

The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { continueManager } from '@kit.AbilityKit';

#### continueManager.on

on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void

Registers a callback to obtain the quick start result when an application is launched quickly. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/THIV06d0Syi1d3ErMd-lgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9252CBDAD120E8088D459CAFB1B10E852898DE5CEE04181936DF31628525DC1F)

The quick start feature allows the application to start concurrently while the user triggers migration and waits for the migration data to return, reducing wait time. To enable the quick start feature, add the suffix **\_ContinueQuickStart** to the **continueType** value in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file of the source application.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AbilityRuntime.Mission

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | The value is fixed at **prepareContinue**. |
| context | [Context](../../dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Context of the ability. |
| callback | AsyncCallback<[ContinueResultInfo](#continueresultinfo)\> | Yes | Callback used to return the result. If obtaining the quick start result is successful, **err** is undefined, and **ContinueResultInfo** is the obtained quick startup result. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed Scheduler Error Codes](../../../error-codes/distributed-scheduler-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16300501 | the system ability work abnormally. |

**Example**

import { AbilityConstant, UIAbility, Want, continueManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '\[MigrationAbility\]';
const DOMAIN\_NUMBER: number = 0xFF00;

export default class MigrationAbility extends UIAbility {
    storage : LocalStorage = new LocalStorage();

    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        hilog.info(DOMAIN\_NUMBER, TAG, '%{public}s', 'Ability onCreate');

        // 1. Quick start is configured. Trigger the lifecycle callback when the application is launched immediately.
        if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE\_CONTINUATION) {
            // Register the callback to obtain the quick start result.
            try {
              continueManager.on("prepareContinue", this.context, (err, continueResultInfo) => {
                if (err.code != 0) {
                  console.error('register failed, cause: ' + JSON.stringify(err));
                  return;
                }
                console.info('register finished, ' + JSON.stringify(continueResultInfo));
              });
            } catch (e) {
              console.error('register failed, cause: ' + JSON.stringify(e));
            }
            // If the application data to migrate is large, add a loading screen here (for example, displaying "loading" on the screen).
            // Handle issues related to custom redirection and timing.
            // ...
        }
    }
}

#### continueManager.off

off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void

Unregisters the callback used to obtain the quick start result when an application is launched quickly. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/x_bSr5a7RGeTK6KKyPEAQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D657ADF60C1C9313DE98AF2A9FAA5B5195784662D11C153B159E222116D62C26)

The quick start feature allows the application to start concurrently while the user triggers migration and waits for the migration data to return, reducing wait time. To enable the quick start feature, add the suffix **\_ContinueQuickStart** to the **continueType** value in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file of the source application.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AbilityRuntime.Mission

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | The value is fixed at **prepareContinue**. |
| context | [Context](../../dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Context of the ability. |
| callback | AsyncCallback<[ContinueResultInfo](#continueresultinfo)\> | No | Callback used to return the result. If the callback is unregistered, **err** is undefined, and **ContinueResultInfo** is the callback unregistration result. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed Scheduler Error Codes](../../../error-codes/distributed-scheduler-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16300501 | the system ability work abnormally. |

**Example**

import { AbilityConstant, UIAbility, Want, continueManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '\[MigrationAbility\]';
const DOMAIN\_NUMBER: number = 0xFF00;

export default class MigrationAbility extends UIAbility {
    storage : LocalStorage = new LocalStorage();

    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        hilog.info(DOMAIN\_NUMBER, TAG, '%{public}s', 'Ability onCreate');

        // 1. Quick start is configured. Trigger the lifecycle callback when the application is launched immediately.
        if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE\_CONTINUATION) {
            // Unregister the callback used to obtain the quick start result.
            try {
              continueManager.off("prepareContinue", this.context, (err, continueResultInfo) => {
                if (err.code != 0) {
                  console.error('unregister failed, cause: ' + JSON.stringify(err));
                  return;
                }
                console.info('unregister finished, ' + JSON.stringify(continueResultInfo));
              });
            } catch (e) {
              console.error('unregister failed, cause: ' + JSON.stringify(e));
            }
            // If the application data to migrate is large, add a loading screen here (for example, displaying "loading" on the screen).
            // Handle issues related to custom redirection and timing.
            // ...
        }
    }
}

#### ContinueResultInfo

Describes the quick start result returned by the callback.

**System capability**: SystemCapability.Ability.AbilityRuntime.Mission

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| resultState | [ContinueStateCode](#continuestatecode) | No | No | 
Status code of the operation result.

**Model restriction**: This API can be used only in the stage model.

 |
| resultInfo | string | No | Yes | 

Description of the operation result.

**Model restriction**: This API can be used only in the stage model.

 |

#### ContinueStateCode

Enumerates the status codes of the quick start result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Mission

| Name | Value | Description |
| :-- | :-- | :-- |
| SUCCESS | 0 | 
Operation succeeded.

**Model restriction**: This API can be used only in the stage model.

 |
| SYSTEM\_ERROR | 1 | 

Operation failed.

**Model restriction**: This API can be used only in the stage model.

 |
