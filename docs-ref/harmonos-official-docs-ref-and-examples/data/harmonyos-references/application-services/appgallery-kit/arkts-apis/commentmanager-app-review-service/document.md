# commentManager (App Review Service)

This module provides the in-app review capability, allowing users to leave feedback without navigating to the app details page on AppGallery

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/zPLpKTfCT4WqlRT416K8WQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062504Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FF6BF7D067F3B265DD5B5B2A3C0F12FE0FCEB27123953658E0AF45AA760AA74)

Exceptions need to be captured when an API is called.

**Start version**: 6.0.0(20)

#### Modules to Import

import { commentManager } from '@kit.AppGalleryKit';

#### commentManager.showCommentDialog

showCommentDialog(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void>

Launches an app review pop-up. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Comment

**Start version**: 6.0.0(20)

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

 | 

[common.UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) | [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

App context.

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

1021500001

 | 

Internal system error.

 |
| 

1021500002

 | 

Service request failed.

 |
| 

1021500003

 | 

Failed to connect to AppGallery.

 |
| 

1021500004

 | 

Failed to write parameters.

 |
| 

1021500005

 | 

The app context is invalid.

 |
| 

1021500006

 | 

The user has not signed in to their HUAWEI ID.

 |
| 

1021500007

 | 

The user has already commented on the current version.

 |
| 

1021500008

 | 

The number of comments has reached the maximum limit.

 |
| 

1021500009

 | 

The user has already left a comment, and less than a year has elapsed since then.

 |

**Example**:

import { commentManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'showCommentDialog'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
              commentManager.showCommentDialog(uiContext).then(()=>{
                hilog.info(0, 'TAG', "succeeded in showing commentDialog.");
              }).catch((error: BusinessError<Object>) => {
                hilog.error(0, 'TAG', \`showCommentDialog failed, Code: ${error.code}, message: ${error.message}\`);
              });
            } catch (error) {
              hilog.error(0, 'TAG', \`showCommentDialog failed, Code: ${error.code}, message: ${error.message}\`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
