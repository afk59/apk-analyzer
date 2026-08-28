# PhotoEditorExtensionContext

PhotoEditorExtensionContext provides the context environment for the PhotoEditorExtensionAbility. It inherits from ExtensionContext and provides PhotoEditorExtensionAbility related configuration and APIs for saving images.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/62d0X3puT8uVPqAdLd4XJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1B542B567D0F1751B3431447F0B95F9D1681FB6E0E7FE94500C2F687661F53E)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### PhotoEditorExtensionContext.saveEditedContentWithUri

saveEditedContentWithUri(uri: string): Promise<AbilityResult>

Saves an edited image, which is passed in through a URI. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | [URI](../../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md) of the edited image. The format is file://<bundleName>/<sandboxPath>. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<AbilityResult> | Promise used to return an AbilityResult object. The URI of the edited image is stored in **want.uri**. The [URI](../../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md) format is file://<bundleName>/<sandboxPath>. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 29600001 | Internal error. |
| 29600002 | Image input error. |
| 29600003 | Image too big. |

**Example**

import { common, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG = '\[ExamplePhotoEditorAbility\]';

@Entry
@Component
struct Index {
  // Original image
  @State originalImage: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Button('RotateAndSaveImg').onClick(event => {
          hilog.info(0x0000, TAG, \`Start to edit image and save.\`);

          this.originalImage?.rotate(90).then(() => {
            const imagePackerApi: image.ImagePacker = image.createImagePacker();
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
            imagePackerApi.packToData(this.originalImage, packOpts).then((data: ArrayBuffer) => {
              let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
              let filePath = context.filesDir + '/edited.jpg';
              let file: fileIo.File | undefined;
              try{
                file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE
                | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
                let writeLen = fileIo.writeSync(file.fd, data);
                hilog.info(0x0000, TAG, 'write data to file succeed and size is:'
                  + writeLen);
                fileIo.closeSync(file);
                context.saveEditedContentWithUri(filePath).then
                  (data => {
                    hilog.info(0x0000, TAG,
                      \`saveContentEditingWithUri result: ${JSON.stringify(data)}\`);
                  });
              } catch (e) {
                hilog.info(0x0000, TAG, \`writeImage failed:${e}\`);
              } finally {
                fileIo.close(file);
              }
            }).catch((error: BusinessError) => {
              hilog.error(0x0000, TAG,
                'Failed to pack the image. And the error is: ' + String(error));
            })
          })
        }).margin({ top: 10 })
      }
    }
  }
}

#### PhotoEditorExtensionContext.saveEditedContentWithImage

saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>

Saves the passed PixelMap object, which is an edited image. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pixeMap | [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Edited image, which is an image.PixelMap object. |
| option | [image.PackingOption](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interfaces-others/document.md#packingoption) | Yes | Option for image packing. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<AbilityResult> | Promise used to return an AbilityResult object. The URI of the edited image is stored in **want.uri**. The [URI](../../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md) format is file://<bundleName>/<sandboxPath>. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 29600001 | Internal error. |
| 29600002 | Image input error. |
| 29600003 | Image too big. |

**Example**

import { common, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { image } from '@kit.ImageKit';

const TAG = '\[ExamplePhotoEditorAbility\]';

@Entry
@Component
struct Index {
  // Original image
  @State originalImage: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Button('RotateAndSaveImg').onClick(event => {
          hilog.info(0x0000, TAG, \`Start to edit image and save.\`);

          this.originalImage?.rotate(90).then(() => {
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
            try {
              let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
              context.saveEditedContentWithImage(this.originalImage as image.PixelMap,
                packOpts).then(data => {
                  hilog.info(0x0000, TAG,
                    \`saveContentEditingWithImage result: ${JSON.stringify(data)}\`);
                });
            } catch (e) {
              hilog.error(0x0000, TAG, \`saveContentEditingWithImage failed:${e}\`);
              return;
            }
          })
        }).margin({ top: 10 })
      }
    }
  }
}
