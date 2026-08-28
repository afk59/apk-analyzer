# Interface (ImagePacker)

The **ImagePacker** class provides APIs to compress and encode images.

Before calling any API in ImagePacker, you must use [image.createImagePacker](../functions/document.md#imagecreateimagepacker) to create an ImagePacker instance.

During encoding, do not modify or release the ImageSource, PixelMap, or Picture object that is being used as the input. Otherwise, a crash or other undefined behavior may occur.

Images occupy a large amount of memory. When you finish using an ImagePacker instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

Currently, the following formats are supported: jpeg, webp, png, heic12+, and gif18+. (The supported formats may vary depending on the hardware. You can refer to the **supportedFormats** property of ImagePacker to see which ones are supported.)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/pSF63Wp2Rz-GQZMJ5ktZJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D9AB2891376E26F60601FB4AD0C02818905745379F5C6667750D4D9F0E4CA15)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| supportedFormats | Array<string> | Yes | No | Supported formats for image encoding, including jpeg, webp, png, heic12+, and gif18+. (The supported formats may vary depending on the hardware.) |

#### packToData13+

packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>

Compresses or re-encodes an image. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [ImageSource](../interface-imagesource/document.md) | Yes | Image source to compress or re-encode. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the compressed or encoded image data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function PackToData(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToData(imageSourceObj, packOpts)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing the image.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to pack the image.code ${error.code},message is ${error.message}\`);
    })
}

#### packToData13+

packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>

Compresses or re-encodes an image. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/iffX_QrHRlyjW40X63q92Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8DC9377AF376F09A7F1287D89416FA043A4B8525CEF78D0F8FE63B02C276145)

If error code 401 is returned, the parameters are abnormal. The possible cause is that the PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is released after this API is called.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [PixelMap](../interface-pixelmap/document.md) | Yes | PixelMap to compress or re-encode. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the compressed or encoded image data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function PackToData() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToData(pixelMap, packOpts)
      .then((data: ArrayBuffer) => {
        console.info('Succeeded in packing the image.');
      }).catch((error: BusinessError) => {
      console.error(\`Failed to pack the image.code ${error.code},message is ${error.message}\`);
    })
  }).catch((error: BusinessError) => {
    console.error(\`Failed to create PixelMap.code ${error.code},message is ${error.message}\`);
  })
}

#### packing13+

packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>

Compresses or re-encodes an image. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| picture | [Picture](../interface-picture/document.md) | Yes | Picture to compress or re-encode. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the compressed or encoded image data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  let funcName = "Packing";
  if (imagePackerObj != null) {
    let opts: image.PackingOption = {
      format: "image/jpeg",
      quality: 98,
      desiredDynamicRange: image.PackingDynamicRange.AUTO,
      needsPackProperties: true};
    await imagePackerObj.packing(pictureObj, opts).then((data: ArrayBuffer) => {
      console.info(funcName, 'Succeeded in packing the image.'+ data);
    }).catch((error: BusinessError) => {
      console.error(funcName, \`Failed to pack the image.code ${error.code},message is ${error.message}\`);
    });
  }
}

#### packToDataFromPixelmapSequence18+

packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>

Encodes multiple PixelMap objects into GIF data. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pixelmapSequence | Array<[PixelMap](../interface-pixelmap/document.md)\> | Yes | PixelMaps to encode. |
| options | [PackingOptionsForSequence](../interfaces-others/document.md#packingoptionsforsequence18) | Yes | Options for encoding animated images. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the encoded data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Failed to encode image. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function PackToDataFromPixelmapSequence(context : Context) {
  const resourceMgr = context.resourceManager;
  // 'moving\_test.gif' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const fileData = await resourceMgr.getRawFileContent('moving\_test.gif');
  const color = fileData.buffer as ArrayBuffer;
  let imageSource = image.createImageSource(color);
  let pixelMapList = await imageSource.createPixelMapList();
  let ops: image.PackingOptionsForSequence = {
    frameCount: 3, // Set the number of frames in GIF encoding to 3.
    delayTimeList: \[10, 10, 10\], // Set the delay time of three frames in GIF encoding to 100 ms, 100 ms, and 100 ms, respectively.
    disposalTypes: \[3, 2, 3\], // Specify the frame transition modes of the three frames in GIF encoding as 3 (restore to the previous state), 2 (restore to the background color), and 3 (restore to the previous state).
    loopCount: 0 // Set the number of loops in GIF encoding to infinite.
  };
  let packer = image.createImagePacker();
  packer.packToDataFromPixelmapSequence(pixelMapList, ops)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing.');
    }).catch((error: BusinessError) => {
    console.error('Failed to packing.');
  })
}

#### release

release(callback: AsyncCallback<void>): void

Releases this ImagePacker instance. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release((err: BusinessError)=>{
    if (err) {
      console.error(\`Failed to release image packaging.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in releasing image packaging.');
    }
  })
}

#### release

release(): Promise<void>

Releases this ImagePacker instance. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using an ImagePacker instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release().then(() => {
    console.info('Succeeded in releasing image packaging.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to release image packaging.code ${error.code},message is ${error.message}\`);
  })
}

#### packToFile11+

packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void

Encodes the image source into a file based on the specified encoding parameters. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [ImageSource](../interface-imagesource/document.md) | Yes | Image source to encode. |
| fd | number | Yes | File descriptor. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  // 'test.png' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const path: string = context.filesDir + "/test.png";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const filePath: string = context.filesDir + "/image\_source.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to pack the image to file.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in packing the image to file.');
    }
  })
}

#### packToFile11+

packToFile (source: ImageSource, fd: number, options: PackingOption): Promise<void>

Encodes the image source into a file based on the specified encoding parameters. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [ImageSource](../interface-imagesource/document.md) | Yes | Image source to encode. |
| fd | number | Yes | File descriptor. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  // 'test.png' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const path: string = context.filesDir + "/test.png";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const filePath: string = context.filesDir + "/image\_source.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts).then(() => {
    console.info('Succeeded in packing the image to file.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to pack the image to file.code ${error.code},message is ${error.message}\`);
  })
}

#### packToFile11+

packToFile (source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void

Encodes the PixelMap into a file based on the specified encoding parameters. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/WdF8fvSMTnSb7MfZvCG0Fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B93B9294CD6176E15D95D379F53ED024FF5F696245B1FD72963F85CE9FEE95C0)

If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is released after this API is called.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [PixelMap](../interface-pixelmap/document.md) | Yes | PixelMap to encode. |
| fd | number | Yes | File descriptor. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  const path: string = context.filesDir + "/pixel\_map.jpg";
  image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToFile(pixelmap, file.fd, packOpts, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to pack the image to file.code ${err.code},message is ${err.message}\`);
      } else {
        console.info('Succeeded in packing the image to file.');
      }
    })
  })
}

#### packToFile11+

packToFile (source: PixelMap, fd: number, options: PackingOption): Promise<void>

Encodes the PixelMap into a file based on the specified encoding parameters. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/l6Yljgz4SxijKMp1d3RTBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=947976EACD73FF92A4B1CE98D504EB9AD282129F873BC42A78FA66A26110DB05)

If error code 62980115 is returned, the parameters are abnormal. The possible cause is that the PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is released after this API is called.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [PixelMap](../interface-pixelmap/document.md) | Yes | PixelMap to encode. |
| fd | number | Yes | File descriptor. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  const path: string = context.filesDir + "/pixel\_map.jpg";
  image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToFile(pixelmap, file.fd, packOpts)
      .then(() => {
        console.info('Succeeded in packing the image to file.');
      }).catch((error: BusinessError) => {
      console.error(\`Failed to pack the image to file.code ${error.code},message is ${error.message}\`);
    })
  })
}

#### packToFile13+

packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>

Encodes the Picture into a file based on the specified encoding parameters. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| picture | [Picture](../interface-picture/document.md) | Yes | Picture to encode. |
| fd | number | Yes | File descriptor. |
| options | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function PackToFile(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);

  let funcName = "PackToFile";
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  if (imagePackerObj != null) {
    const filePath: string = context.filesDir + "/test.jpg";
    let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
    let packOpts: image.PackingOption = {
      format: "image/jpeg",
      quality: 98,
      desiredDynamicRange: image.PackingDynamicRange.AUTO,
      needsPackProperties: true};
    await imagePackerObj.packToFile(pictureObj, file.fd, packOpts).then(() => {
      console.info(funcName, 'Succeeded in packing the image to file.');
    }).catch((error: BusinessError) => {
      console.error(funcName, \`Failed to pack the image to file.code ${error.code},message is ${error.message}\`);
    });
  }
}

#### packToFileFromPixelmapSequence18+

packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>

Encodes multiple PixelMaps into a GIF file. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pixelmapSequence | Array<[PixelMap](../interface-pixelmap/document.md)\> | Yes | PixelMaps to encode. |
| fd | number | Yes | File descriptor. |
| options | [PackingOptionsForSequence](../interfaces-others/document.md#packingoptionsforsequence18) | Yes | Options for encoding animated images. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Failed to encode image. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const resourceMgr = context.resourceManager;
  // 'moving\_test.gif' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const fileData = await resourceMgr.getRawFileContent('moving\_test.gif');
  const color = fileData.buffer;
  let imageSource = image.createImageSource(color);
  let pixelMapList = await imageSource.createPixelMapList();
  let path: string = context.cacheDir + '/result.gif';
  let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
  let ops: image.PackingOptionsForSequence = {
    frameCount: 3, // Set the number of frames in GIF encoding to 3.
    delayTimeList: \[10, 10, 10\], // Set the delay time of three frames in GIF encoding to 100 ms, 100 ms, and 100 ms, respectively.
    disposalTypes: \[3, 2, 3\], // Specify the frame transition modes of the three frames in GIF encoding as 3 (restore to the previous state), 2 (restore to the background color), and 3 (restore to the previous state).
    loopCount: 0 // Set the number of loops in GIF encoding to infinite.
  };
  let packer = image.createImagePacker();
  packer.packToFileFromPixelmapSequence(pixelMapList, file.fd, ops)
    .then(() => {
      console.info('Succeeded in packToFileMultiFrames.');
    }).catch((error: BusinessError) => {
    console.error('Failed to packToFileMultiFrames.');
  })
}

#### packing(deprecated)

packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void

Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/6rQ4VmnPS6OrQ6qcuGsRQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=304BA564C81C2A024ABFEE1D801F081638789589A52D8D3B946E171BE4534D31)

This API is supported since API version 6 and deprecated since API version 13. Use [packToData](#packtodata13) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [ImageSource](../interface-imagesource/document.md) | Yes | Image source to compress or re-encode. |
| option | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |
| callback | AsyncCallback<ArrayBuffer> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the compressed or encoded image data; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packing(imageSourceObj, packOpts, (err: BusinessError, data: ArrayBuffer) => {
    if (err) {
      console.error(\`Failed to pack the image.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in packing the image.');
    }
  })
}

#### packing(deprecated)

packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>

Compresses or re-encodes an image. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/6WvjiXS2R8qM0E8MZGXJLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD925D569A733C5EE75AB3E116F104F112D91D590A1B62B710C84EBEAB29E099)

This API is supported since API version 6 and deprecated since API version 13. Use [packToData](#packtodata13) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [ImageSource](../interface-imagesource/document.md) | Yes | Image source to compress or re-encode. |
| option | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the compressed or encoded image data. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packing(imageSourceObj, packOpts)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing the image.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to pack the image.code ${error.code},message is ${error.message}\`);
    })
}

#### packing(deprecated)

packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void

Compresses or re-encodes an image. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/f4vVuxWSRAiw-pwAJtKl_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12766193E85627B0AED170267F6267829810A725D2E62E473FDC23E3830210B3)

This API is supported since API version 8 and deprecated since API version 13. Use [packToData](#packtodata13) instead.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/JaU3xbhqSi-3RUb58Ic7AA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA613828EAC450F91D3D8AAC8C41422B184FE6BA30060B9D6DAA18186753706E)

If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is released after this API is called.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [PixelMap](../interface-pixelmap/document.md) | Yes | PixelMap to compress or re-encode. |
| option | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |
| callback | AsyncCallback<ArrayBuffer> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the compressed or encoded image data; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Packing() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packing(pixelMap, packOpts, (err: BusinessError, data: ArrayBuffer) => {
      if (err) {
        console.error(\`Failed to pack the image.code ${err.code},message is ${err.message}\`);
      } else {
        console.info('Succeeded in packing the image.');
      }
    })
  }).catch((error: BusinessError) => {
    console.error(\`Failed to create the PixelMap.code ${error.code},message is ${error.message}\`);
  })
}

#### packing(deprecated)

packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>

Compresses or re-encodes an image. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/pbgRGTiyTeOsv5cLUf649A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4424C45AFFC484EA5DE886030D771EF90F471293835A62649AC007352CF4522E)

This API is supported since API version 8 and deprecated since API version 13. Use [packToData](#packtodata13) instead.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/-YCMuiUsSGOG-7ZNH93IXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC90A7C6A8FD5DA78B824F979E307334734B00B828D26359DC1D97220B3FC4A0)

If the message "PixelMap mismatch" is returned, the parameters are abnormal. The possible cause is that the PixelMap object is released in advance. You need to check the code and ensure that the PixelMap object is released after this API is called.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [PixelMap](../interface-pixelmap/document.md) | Yes | PixelMap to compress or re-encode. |
| option | [PackingOption](../interfaces-others/document.md#packingoption) | Yes | Encoding parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the compressed or encoded image data. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Packing() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packing(pixelMap, packOpts)
      .then((data: ArrayBuffer) => {
        console.info('Succeeded in packing the image.');
      }).catch((error: BusinessError) => {
      console.error(\`Failed to pack the image.code ${error.code},message is ${error.message}\`);
    })
  }).catch((error: BusinessError) => {
    console.error(\`Failed to create PixelMap.code ${error.code},message is ${error.message}\`);
  })
}
