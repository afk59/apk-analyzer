# Interface (ImageReceiver)

The **ImageReceiver** class provides APIs to obtain the surface ID of a component, read the latest image, read the next image, and release the ImageReceiver instance. The ImageReceiver acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images. The configuration of image properties should be done on the sending side (the producer), such as when creating a camera preview stream with [createPreviewOutput](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/interface-cameramanager/document.md#createpreviewoutput).

Before calling any APIs in ImageReceiver, you must use [image.createImageReceiver](../functions/document.md#imagecreateimagereceiver11) to create an ImageReceiver instance.

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call [release](#release9) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/YI7xcGt6S92o8U1dwFcmuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFD7357FF63B0AB54AB7C61E25653519974C3AD834349B838309245C7A071F7B)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 9.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size9+ | [Size](../interfaces-others/document.md#size) | Yes | No | Image size. This parameter does not affect the size of the received image. The actual returned size is determined by the producer, for example, the camera. |
| capacity9+ | number | Yes | No | Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware. |
| format9+ | [ImageFormat](../enums/document.md#imageformat9) | Yes | No | Image format, which is a constant of [ImageFormat](../enums/document.md#imageformat9). (Currently, only **ImageFormat:JPEG** is supported. The format actually returned is determined by the producer, for example, camera.) |

#### getReceivingSurfaceId9+

getReceivingSurfaceId(callback: AsyncCallback<string>): void

Obtains a surface ID for the camera or other components. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the surface ID obtained. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId((err: BusinessError, id: string) => {
    if (err) {
      console.error(\`Failed to get the ReceivingSurfaceId.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in getting the ReceivingSurfaceId.');
    }
  });
}

#### getReceivingSurfaceId9+

getReceivingSurfaceId(): Promise<string>

Obtains a surface ID for the camera or other components. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the surface ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId().then((id: string) => {
    console.info('Succeeded in getting the ReceivingSurfaceId.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get the ReceivingSurfaceId.code ${error.code},message is ${error.message}\`);
  })
}

#### readLatestImage9+

readLatestImage(callback: AsyncCallback<Image>): void

Reads the latest image from the ImageReceiver instance. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/9oy1P9BoSPWvJdPm2GYU7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12E3C997D7E17EEAA7583B59F4DEEF8DA95EBF88036C8FD759C38E0CD439683A)

This API can be called to receive data only after the [on](#on9) callback is triggered. When the [Image](../interface-image/document.md) object returned by this API is no longer needed, call [release](../interface-image/document.md#release9) to release the object. New data can be received only after the release.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Image](../interface-image/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the latest image obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(\`Failed to read the latest Image.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in reading the latest Image.');
    }
  });
}

#### readLatestImage9+

readLatestImage(): Promise<Image>

Reads the latest image from the ImageReceiver instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/K1ylQDzFQSW4TrAPVUBf9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D60748D130F3EED3833E033E58FC5465AABC3E6FD088745CDA9ABF77487F2942)

This API can be called to receive data only after the [on](#on9) callback is triggered. When the [Image](../interface-image/document.md) object returned by this API is no longer needed, call [release](../interface-image/document.md#release9) to release the object. New data can be received only after the release.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Image](../interface-image/document.md)\> | Promise used to return the latest image. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage().then((img: image.Image) => {
    console.info('Succeeded in reading the latest Image.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to read the latest Image.code ${error.code},message is ${error.message}\`);
  });
}

#### readNextImage9+

readNextImage(callback: AsyncCallback<Image>): void

Reads the next image from the ImageReceiver instance. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/-H9TnCj-QLSw0KQvZn1kKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=180C3C8A549E9DC4C7E3E0F90143CBFD0C5488365190DEDB2B9F57D9014721E2)

This API can be called to receive data only after the [on](#on9) callback is triggered. When the [Image](../interface-image/document.md) object returned by this API is no longer needed, call [release](../interface-image/document.md#release9) to release the object. New data can be received only after the release.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Image](../interface-image/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the next image obtained. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(\`Failed to read the next Image.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in reading the next Image.');
    }
  });
}

#### readNextImage9+

readNextImage(): Promise<Image>

Reads the next image from the ImageReceiver instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/TLs5R3WhT4yvFJZzwh0SVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0D17386BAEE05E96CD6C0F5BE975B917A3F5B40FB214981228F8516AC8EBDA1)

This API can be called to receive data only after the [on](#on9) callback is triggered. When the [Image](../interface-image/document.md) object returned by this API is no longer needed, call [release](../interface-image/document.md#release9) to release the object. New data can be received only after the release.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Image](../interface-image/document.md)\> | Promise used to return the next image. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage().then((img: image.Image) => {
    console.info('Succeeded in reading the next Image.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to read the next Image.code ${error.code},message is ${error.message}\`);
  });
}

#### on9+

on(type: 'imageArrival', callback: AsyncCallback<void>): void

Listens for image arrival events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of event to listen for. The value is fixed at **'imageArrival'**, which is triggered when an image is received. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

async function On(receiver : image.ImageReceiver) {
  receiver.on('imageArrival', () => {
    // Implement the callback logic when an image is received.
  });
}

#### off13+

off(type: 'imageArrival', callback?: AsyncCallback<void>): void

Unregisters the callback function that is triggered when the buffer is released. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of event, which is **'imageArrival'**. |
| callback | AsyncCallback<void> | No | Callback to unregister. |

**Example**

async function Off(receiver : image.ImageReceiver) {
  let callbackFunc = ()=>{
      // Implement the callback logic.
  };
  receiver.on('imageArrival', callbackFunc);
  receiver.off('imageArrival', callbackFunc);
}

#### release9+

release(callback: AsyncCallback<void>): void

Releases this ImageReceiver instance. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to release the receiver.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in releasing the receiver.');
    }
  })
}

#### release9+

release(): Promise<void>

Releases this ImageReceiver instance. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release().then(() => {
    console.info('Succeeded in releasing the receiver.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to release the receiver.code ${error.code},message is ${error.message}\`);
  })
}
