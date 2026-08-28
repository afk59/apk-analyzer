# Interface (Image)

The **Image** class is used to obtain image content.

An Image instance is returned when [readNextImage](../interface-imagereceiver/document.md#readnextimage9) and [readLatestImage](../interface-imagereceiver/document.md#readlatestimage9) are called.

Image properties are set only when the Image instance is created and cannot be changed later. These properties do not affect the actual image content. You should always rely on the properties written by the image producer, that is, the content actually sent to the [ImageReceiver](../interface-imagereceiver/document.md) by the data source.

Images occupy a large amount of memory. When you finish using an Image instance, call [release](#release9) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/QTqqfbecRG2kKQt5PY8FUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE7E12E4AEED596714F9E791FB130F88312718FB241EB177606D99F95F21D9C8)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 9.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| clipRect9+ | [Region](../interfaces-others/document.md#region8) | No | No | Image area to be cropped. |
| size9+ | [Size](../interfaces-others/document.md#size) | Yes | No | 
Image size.

If the Image object stores camera preview stream data (YUV image data), the width and height in **size** reflect the dimensions of the YUV image.

If the Image object stores camera capture stream data (JPEG image data), given that it is an encoded file, the width in **size** is the size of the JPEG file, while the height is set to **1**.

The type of data stored in the Image object depends on whether the application passes the surface ID in the receiver to a previewOutput or captureOutput object of the camera.

For details about the best practices of camera preview and photo capture, see [Dual-Channel Preview (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-dual-channel-preview) and [Photo Capture Sample (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-shooting-case).

 |
| format9+ | number | Yes | No | Image format. For details, see [OH\_NativeBuffer\_Format](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_format). |
| timestamp12+ | number | Yes | No | Image timestamp. Timestamps, measured in nanoseconds, are usually monotonically increasing. The specific meaning and baseline of these timestamps are determined by the image producer, which is the camera in the camera preview and photo scenarios. As a result, images from different producers may carry timestamps with distinct meanings and baselines, making direct comparison between them infeasible. To obtain the generation time of a photo, you can use [getImageProperty](../interface-imagesource/document.md#getimageproperty11) to read the related Exif information. |

#### getComponent9+

getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void

Obtains the component buffer from the Image instance based on the color component type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| componentType | [ComponentType](../enums/document.md#componenttype9) | Yes | Component type. (Currently, only **ComponentType:JPEG** is supported. The format actually returned is determined by the producer, for example, camera.) |
| callback | AsyncCallback<[Component](../interfaces-others/document.md#component9)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the component buffer obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG, (err: BusinessError, component: image.Component) => {
    if (err) {
      console.error(\`Failed to get the component.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in getting component.');
    }
  })
}

#### getComponent9+

getComponent(componentType: ComponentType): Promise<Component>

Obtains the component buffer from the Image instance based on the color component type. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| componentType | [ComponentType](../enums/document.md#componenttype9) | Yes | Component type. (Currently, only **ComponentType:JPEG** is supported. The format actually returned is determined by the producer, for example, camera.) |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Component](../interfaces-others/document.md#component9)\> | Promise used to return the component buffer. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
    console.info('Succeeded in getting component.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get the component.code ${error.code},message is ${error.message}\`);
  })
}

#### release9+

release(callback: AsyncCallback<void>): void

Releases this Image instance. This API uses an asynchronous callback to return the result.

The corresponding resources must be released before another image arrives.

Images occupy a large amount of memory. When you finish using an Image instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to release the image instance.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}

#### release9+

release(): Promise<void>

Releases this Image instance. This API uses a promise to return the result.

The corresponding resources must be released before another image arrives.

Images occupy a large amount of memory. When you finish using an Image instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to release the image instance.code ${error.code},message is ${error.message}\`);
  })
}
