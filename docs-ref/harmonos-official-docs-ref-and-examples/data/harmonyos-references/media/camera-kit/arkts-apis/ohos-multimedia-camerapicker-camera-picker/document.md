# @ohos.multimedia.cameraPicker (Camera Picker)

The module provides APIs for an application to use the system camera to take photos or record videos, depending on the media type specified by the application. The application must call these APIs within a UIAbility. Otherwise, the camera picker cannot be started.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/VjGHgoMNRuKOw1M1HNMY9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23165CA9449E18C7AE4ECB6E83468AA87AA05FB3EA65ABD29B3A39396EF63AA3)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { cameraPicker } from '@kit.CameraKit';

#### cameraPicker.pick

pick(context: Context, mediaTypes: Array<PickerMediaType>, pickerProfile: PickerProfile): Promise<PickerResult>

Starts the camera picker and enters the corresponding mode based on the media type. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/ZHk1GPVVSJSuumx8LzPaXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1653856A3816AE67DB2214271DDDEB0DB998EFB76F2F54744A1177C21AF9E88B)

When an application is running on a widescreen foldable device and the camera picker is launched while the device is unfolded, switching the device from unfolded to folded will automatically move the camera picker to the background.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| mediaTypes | Array<[PickerMediaType](#pickermediatype)\> | Yes | Media type. |
| pickerProfile | [PickerProfile](#pickerprofile) | Yes | Profile of the camera picker. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<PickerResult> | Promise used to return the processing result ([PickerResult](#pickerresult)) of the camera picker. |

**Example**

import { cameraPicker } from '@kit.CameraKit';
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function demo(context: Context) {
  try {
    let pickerProfile: cameraPicker.PickerProfile = {
      cameraPosition: camera.CameraPosition.CAMERA\_POSITION\_BACK
    };
    let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(context,
      \[cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO\], pickerProfile);
    console.info("the pick pickerResult is:" + JSON.stringify(pickerResult));
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`the pick call failed. error code: ${err.code}\`);
  }
}

#### PickerMediaType

Enumerates the media types displayed in the camera picker.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PHOTO | 'photo' | Photo mode. |
| VIDEO | 'video' | Video mode. |

#### PickerProfile

Defines the configuration information about the camera picker.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| cameraPosition | [camera.CameraPosition](../ohos-multimedia-camera-camera-management/enums/document.md#cameraposition) | No | No | Camera position. |
| saveUri | string | No | Yes | URI for saving the configuration information. For details about the default value, see [File URI](../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#constructor10). The **saveUri** parameter is optional. If it is not specified, images and videos are automatically saved to the media library. To prevent them from being saved to the media library, specify a valid file path within your application's sandbox. When you use your own resource path, ensure that the file exists and is writable; otherwise, the save operation fails. |
| videoDuration | number | No | Yes | Maximum video duration, in seconds. The default value is **0**, indicating that the maximum video duration is not set. |

#### PickerResult

Defines the processing result of the camera picker.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| resultCode | number | No | No | Result code. The value **0** means that the processing is successful, and **\-1** means that the processing fails. |
| resultUri | string | No | No | URI of the result. If **saveUri** is empty, **resultUri** is a public media path. If **saveUri** is not empty and the application has the write permission on the URI, the value of **resultUri** is the same as that of **saveUri**. If **saveUri** is not empty and the application does not have the write permission on the URI, **resultUri** cannot be obtained. |
| mediaType | [PickerMediaType](#pickermediatype) | No | No | Media type. |
